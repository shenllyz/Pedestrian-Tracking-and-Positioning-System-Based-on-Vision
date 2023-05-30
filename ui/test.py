# with open('win.py', 'r', encoding='UTF-16LE') as file:
#     content = file.read()
#
# with open('win.py', 'w', encoding='UTF-8') as file:
#     file.write(content)
import os
import shutil
import sys
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtCore import QThread, Signal

from ui import win
import cv2
import numpy as np
from PySide2.QtGui import QIcon
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtGui import QCloseEvent
import torch
import time
import torch.nn.functional as F
# yolo中部分文件路径固定，必须添加根目录
sys.path.append("..\\yolov5-5.0")
sys.path.append("..\\person_search")
from models.experimental import attempt_load
from utils.general import non_max_suppression, scale_coords
from utils.plots import plot_one_box
from utils.torch_utils import select_device
from utils.datasets import letterbox
from deepsort.deep_sort.deep_sort.deep_sort import DeepSort
from deepsort.deep_sort.utils.parser import get_config
from person_search.reid.data.transforms import build_transforms
from person_search.reid.data import make_data_loader
from person_search.reid.config import cfg as reidCfg
from PIL import Image
from person_search.reid.modeling import build_model


class CapPlayer:
    def __init__(self, cap=None):
        self.playable = False
        self.cap = cap
        self.total_Frame = 0
        pass

    def get_cap(self, file_path):
        self.cap = cv2.VideoCapture(file_path)
        self.total_Frame = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)

    def get_delay(self):
        fps = self.cap.get(cv2.CAP_PROP_FPS)  # Get the frames per second of the video
        return int(1000 / fps)

    def nextFrame(self):
        if (self.playable):
            ret, frame = self.cap.read()
            if (ret):
                return frame
            else:
                self.playable = False
        return None

    def closeVedio(self):

        self.playable = False
        if (self.cap):
            self.cap.release()
        cv2.destroyAllWindows()


class MOTPlayer:
    def __init__(self, cap=None):
        self.playable = False
        self.num_person = 0
        self.conf_thres = 0.25
        self.iou_thres = 0.45
        self.boxsize = 2
        self.deepsort = None
        self.num_recent_points = 20  # track line length

    def nextFrame(self, frame, device, model):
        return self.detect_person(frame, device, model)

    def closeVedio(self):
        self.playable = False
        cv2.destroyAllWindows()


    def detect_person(self, frame, device, model):
        self.num_person = 0 # 初始化人数计数器
        im0 = frame.copy()

        # 预处理图像
        img = letterbox(frame, new_shape=(640, 640))[0]  # 使用letterbox函数
        img = img[:, :, ::-1].transpose(2, 0, 1)
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to(device)  # 将 NumPy 数组转换为 PyTorch 张量
        img = img.float()
        img /= 255.0

        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # 推理
        with torch.no_grad():  # 关闭自动求导
            pred = model(img)[0]

        # Apply NMS
        pred = non_max_suppression(pred, self.conf_thres , self.iou_thres , classes=[0], agnostic=False)

        bbox_xywh = []
        confidences = []
        clss = []

        for det in pred:
            if len(det):
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()  # 将边界框坐标从预处理后的图像坐标空间转换为原始图像坐标空间
                # 针对每个检测到的边界框，将其标记在原始图像中
                for *xyxy, conf, cls in det:
                    self.num_person += 1  # 检测到人，计数器加1
                    x1, y1, x2, y2 = [int(x) for x in xyxy]
                    w, h = x2 - x1, y2 - y1
                    bbox_xywh.append([x1 + w / 2, y1 + h / 2, w, h])
                    confidences.append(conf)
                    clss.append(cls)

        # DeepSORT 更新
        track_results = self.deepsort.update(np.array(bbox_xywh), confidences, clss, im0)

        # 绘制跟踪结果及轨迹

        for x1, y1, x2, y2, cls, track_id in track_results:
            label = f'Person ID-{track_id}'
            plot_one_box((x1, y1, x2, y2), im0, label=label, color=(0, 0, 255), line_thickness=self.boxsize)

            # 绘制轨迹
            track_history = self.deepsort.track_history.get(track_id, [])
            hits_threshold = 30  # 设定 hits 阈值
            for i in range(max(1, len(track_history) - self.num_recent_points + 1), len(track_history)):
                x1, y1, hits1 = track_history[i - 1]
                x2, y2, hits2 = track_history[i]
                if hits1 >= hits_threshold and hits2 >= hits_threshold:
                    cv2.line(im0, (x1, y1), (x2, y2), (0, 255, 0), 2)
        return im0



class ReIDPlayer:
    def __init__(self, cap=None):
        self.playable = False
        self.num_person = 0
        self.conf_thres = 0.25
        self.iou_thres = 0.40
        self.boxsize = 2
        self.dist_thres= 1.2
        self.reidModel = None  # initialize your re-id model here
        self.query_feats = []  # 测试特征
        self.num_recent_points = 20  # track line length
        self.reidCfg = reidCfg
        self.device = torch.device('cuda:0')
        self.track_history = []
        # ---------- 行人重识别模型初始化 ---------------------------------------
    def initialize_model(self):

        self.track_history.clear()

        self.query_feats = []  # 测试特征

        self.query_loader, self.num_query = make_data_loader(self.reidCfg)  # 验证集预处理


        self.reidModel = build_model(self.reidCfg, num_classes=1501)  # 模型初始化


        self.reidModel.load_param(self.reidCfg.TEST.WEIGHT)  # 加载权重


        self.reidModel.to(self.device).eval()  # 模型测试

        start_time = time.time()  # 记录开始时间
        for i, batch in enumerate(self.query_loader):
            print(i)
            end_time = time.time()
            print(end_time - start_time)
            with torch.no_grad():
                img, pid, camid = batch  # 返回图片，ID，相机ID
                img = img.to(self.device)  # 将图片放入gpu
                feat = self.reidModel(img)  # 一共2张待查询图片，每张图片特征向量2048 torch.Size([2, 2048])
                self.query_feats.append(feat)  # 获得特征值列表
        end_time = time.time()
        print(end_time - start_time)
        self.query_feats = torch.cat(self.query_feats, dim=0)  # torch.Size([2, 2048])
        print(self.query_feats)
        print("The query feature is normalized")
        self.query_feats = F.normalize(self.query_feats, dim=1, p=2)  # 计算出查询图片的特征向量
        print(self.query_feats)

    def nextFrame(self, frame, device, model):
        return self.person_reid(frame, device, model)

    def closeVedio(self):
        self.playable = False
        cv2.destroyAllWindows()

    def person_reid(self, frame, device, model, imgsz=(640, 640)):
        im0 = frame.copy()  # 复制输入的帧
        im = letterbox(frame, new_shape=imgsz)[0]  # 对帧进行letterbox处理，调整大小并添加黑边
        im = im[:, :, ::-1].transpose(2, 0, 1)  # 调整通道顺序和维度顺序
        im = np.ascontiguousarray(im)  # 转换为连续的内存布局
        im = torch.from_numpy(im).to(device)  # 将NumPy数组转换为PyTorch张量，并将其移动到指定的设备
        im = im.float()  # 转换为浮点型
        im /= 255.0  # 归一化到0-1范围
        if len(im.shape) == 3:  # 如果张量的维度为3，则添加一个维度
            im = im[None]

        t = time.time()
        with torch.no_grad():  # 关闭自动求导
            pred = model(im)[0]  # 使用模型对图像进行预测
        pred = non_max_suppression(pred, self.conf_thres, self.iou_thres)  # 对预测结果进行非最大抑制

        with torch.no_grad():
            for i, det in enumerate(pred):
                if len(det):
                    det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0.shape).round()  # 对检测到的边界框进行缩放和舍入

                    gallery_img = []
                    gallery_loc = []  # 用于存放边界框坐标的列表
                    for *xyxy, conf, cls in reversed(det):
                        if int(cls) == 0:
                            xmin = int(xyxy[0])
                            ymin = int(xyxy[1])
                            xmax = int(xyxy[2])
                            ymax = int(xyxy[3])
                            w = xmax - xmin
                            h = ymax - ymin
                            if w * h > 500:  # 根据面积阈值筛选边界框
                                gallery_loc.append((xmin, ymin, xmax, ymax))
                                crop_img = im0[ymin:ymax, xmin:xmax]  # 根据边界框裁剪图像
                                crop_img = Image.fromarray(cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB))
                                crop_img = build_transforms(self.reidCfg)(crop_img).unsqueeze(0)
                                gallery_img.append(crop_img)  # 将处理后的图像添加到列表中

                    if gallery_img:
                        gallery_img = torch.cat(gallery_img, dim=0)  # 拼接图像张量
                        gallery_img = gallery_img.to(device)
                        gallery_feats = self.reidModel(gallery_img)  # 使用行人重识别模型提取特征向量
                        gallery_feats = torch.nn.functional.normalize(gallery_feats, dim=1, p=2)  # 对特征向量进行归一化
                        m, n = self.query_feats.shape[0], gallery_feats.shape[0]
                        # 计算特征向量之间的欧氏距离
                        distmat = torch.pow(self.query_feats, 2).sum(dim=1, keepdim=True).expand(m, n) + \
                                  torch.pow(gallery_feats, 2).sum(dim=1, keepdim=True).expand(n, m).t()
                        distmat.addmm_(self.query_feats, gallery_feats.t(), beta=1, alpha=-2)
                        distmat = distmat.cpu().numpy()  # 将距离矩阵转换为NumPy数组
                        distmat = distmat.sum(axis=0)  # 对query中同一行人的多个结果求和
                        index = distmat.argmin()  # 找到距离最小的索引
                        if distmat[index] < self.dist_thres:  # 如果距离小于阈值，则认为匹配成功
                            plot_one_box(gallery_loc[index], im0, label='find!', color=(0, 0, 255),
                                         line_thickness=self.boxsize)  # 在图像上绘制边界框和文本
                            xmin, ymin, xmax, ymax = gallery_loc[index]  # 获取匹配成功的边界框坐标
                            w = xmax - xmin
                            h = ymax - ymin
                            bbox_center = [xmin + w / 2, ymin + h / 2]  # 计算边界框的中心点坐标
                            self.track_history.append(bbox_center)  # 更新轨迹历史
                            if len(self.track_history) > self.num_recent_points:
                                self.track_history.pop(0)  # 如果轨迹历史长度超过限制，则删除最旧的点

                            self.track_history = self.track_history[-self.num_recent_points:]  # 更新轨迹历史长度
                            for i in range(1, len(self.track_history)):  # 绘制轨迹线
                                x1, y1 = self.track_history[i - 1]
                                x2, y2 = self.track_history[i]
                                cv2.line(im0, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                        else:
                            self.track_history.clear()  # 如果人物未检测到，则清空轨迹历史
                    else:
                        self.track_history.clear()  # 如果没有检测到人物，则清空轨迹历史

        return im0  # 返回绘制了轨迹的帧


class Mainwindow(QtWidgets.QMainWindow, win.Ui_mainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.button1 = self.fileButton # button for MP4
        self.button2 = self.cameraButton
        self.button3 = self.fileButton_2 #button for JPG
        self.stopButton = self.stopButton
        self.button1.clicked.connect(self.fileInit)
        self.button2.clicked.connect(self.cameraInit)
        self.button3.clicked.connect(self.personInit)
        self.tabWidget.currentChanged.connect(self.check_current_tab)
        self.stopButton.clicked.connect(self.stop)  # stopCamera
        self.runButton.clicked.connect(self.pauseSwitch)
        self.BoxSizeSpinBox.valueChanged.connect(lambda x: self.change_val(x, 'BoxSizeSpinBox'))
        self.confSpinBox.valueChanged.connect(lambda x: self.change_val(x, 'confSpinBox'))
        self.iouSpinBox.valueChanged.connect(lambda x: self.change_val(x, 'iouSpinBox'))
        self.TrackSpinBox.valueChanged.connect(lambda x: self.change_val(x, 'TrackSpinBox'))
        self.select_person = ['',''] # 0 previous person  1: current person

        self.frame_update_interval = 10  # 设置每3帧更新一次FPS
        self.frame_count_for_fps = 0  # 添加一个变量用于计算帧数
        self.fps_label = self.fps_label
        self.sys_mode = 0; # 0--multiple object tracking mode
                           # 1--Person Re-ID mode


        self.resultWidget =self.resultWidget
        self.progressBar = self.progressBar
        self.player1 = CapPlayer();
        self.player2 = MOTPlayer();
        self.player3 = ReIDPlayer();

        self.pause_play_count = True  # False = pause; True = play;

        self.ProgressLength = 1000  # max length of progress bar
        self.count = 0

        self.cfg = get_config()
        self.cfg.merge_from_file("../deepsort/deep_sort/configs/deep_sort.yaml")

        # Load YOLOv5 model
        gpu_count = torch.cuda.device_count()  # 初始化gpu
        print(torch.cuda.is_available())
        self.device = select_device('cuda:0')

        self.model = attempt_load('..\\yolov5-5.0\\yolov5s.pt', map_location=self.device)
        self.model.to(self.device).eval()

        self.looper = None

    def check_current_tab(self):
        if self.tabWidget.currentIndex() == 0:   # multiple object tracking
            print("当前显示的是tab")
        elif self.tabWidget.currentIndex() == 1:    # person Re-ID
            print("当前显示的是tab_2")

    def show_person_num(self, num_person):
        self.resultWidget.clear()  # 清空列表
        self.resultWidget.addItem(f"Number of people detected: {num_person}")  # 将检测到的人数添加到列表中
    def show_fps(self,processing_time):
        if processing_time > 0:
            fps = 1 / processing_time  # 计算FPS
        else:
            fps = 0
        self.fps_label.setText(f"FPS: {round(fps)}")

    def change_val(self, x, flag):
        if flag == 'BoxSizeSpinBox':
            self.player2.boxsize = int(x)
            self.player3.boxsize = int(x)
        elif flag == 'confSpinBox':
            self.player2.conf_thres = float(x)
            self.player3.conf_thres = float(x)
        elif flag == 'iouSpinBox':
            self.player2.iou_thres = float(x)
            self.player3.iou_thres = float(x)
        elif flag == 'TrackSpinBox':
            self.player2.num_recent_points = int(x)
            self.player3.num_recent_points = int(x)
    def updateLength(self):
        if (self.player1.total_Frame != -1):  # if not camera
            percent = int((self.count / self.player1.total_Frame) * self.ProgressLength)
            return percent
        else:
            return 0

    def showFrame(self, frame, target_label):  # display video on Qlabel via opencv
        frame_height, frame_width, _ = frame.shape
        label_height = target_label.height()
        label_width = target_label.width()
        # 计算显示图像时的高度和宽度,使得每一帧视频尺寸跟ui同比缩放
        aspect_ratio = frame_width / frame_height
        if label_width / label_height > aspect_ratio:
            resized_height = label_height
            resized_width = int(label_height * aspect_ratio)
        else:
            resized_width = label_width
            resized_height = int(label_width / aspect_ratio)

        frame = cv2.resize(frame, (resized_width, resized_height))
        bytes_per_line = 3 * resized_width
        q_img = QtGui.QImage(frame.data, resized_width, resized_height, bytes_per_line,
                             QtGui.QImage.Format_RGB888).rgbSwapped()

        target_label.setPixmap(QtGui.QPixmap.fromImage(q_img))
        QtCore.QCoreApplication.processEvents()

    def pauseSwitch(self):
        self.pause_play_count = not self.pause_play_count
        if (self.player1.cap):
            if (self.pause_play_count):
                self.player1.playable = True
            else:
                self.player1.playable = False
        # self.player2.playable = not self.player2.playable
        if (self.player1.playable):
            self.resume()

    def stop(self):
        self.player1.playable = False
        self.player2.playable = False
        self.player3.playable = False
        self.player1.closeVedio()
        self.player2.closeVedio()
        self.player3.closeVedio()

    def get_looper(self):
        if self.looper is None or not self.looper.gi_running:
            self.looper = self.loop()
        return self.looper

    def loop(self):   #循环输出视频流
        # if self.sys_mode == 1 and not self.init_thread.is_model_initialized():
        #     yield
        playerList = [self.player1, self.player2]
        while True:
            playing = False

            if (self.player1.playable ):
                frame = self.player1.nextFrame()
                if frame is not None:
                    start_time = time.time()  # 记录开始时间
                    if self.sys_mode == 0:
                        self.showFrame(frame, self.raw_video)
                        self.showFrame(self.player2.nextFrame(frame,self.device,self.model), self.out_video)
                        self.show_person_num(self.player2.num_person)
                    elif self.sys_mode == 1:
                        self.showFrame(frame, self.raw_video)
                        self.showFrame(self.player3.nextFrame(frame,self.device,self.model), self.out_video)

                    end_time = time.time()  # 记录结束时间
                    self.frame_count_for_fps += 1  # 增加帧计数
                    # 只在达到帧数间隔时更新FPS
                    if self.frame_count_for_fps % self.frame_update_interval == 0:
                        processing_time = end_time - start_time  # 计算处理时间
                        self.show_fps(processing_time)

            playing = playing or self.player1.playable
            if not playing:
                yield
            else:
                self.count += 1
               # cv2.waitKey(self.player1.get_delay())
                self.progressBar.setValue(self.updateLength())

    def resume(self):
        looper = self.get_looper()
        if (not looper.gi_running):
            looper.__next__()

    def convert_cvimage_to_pixmap(self, image):
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        qimage = QtGui.QImage(image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QtGui.QPixmap.fromImage(qimage)
        return pixmap



    def personInit(self):
        options = QtWidgets.QFileDialog.Options()
        media_path, _ = QtWidgets.QFileDialog.getOpenFileUrl(self, "QFileDialog.getOpenFileUrl()", "",
                                                             "Image Files (*.png *.jpg);;All Files (*)",
                                                             options=options)
        file_path = media_path.toLocalFile()

        if file_path != "":
            query_dir = os.path.normpath(os.path.abspath('../person_search/query'))
            file_path = os.path.normpath(file_path)
            if file_path.startswith(query_dir):
                pass
            # 如果文件不在 '../person_search/query' 路径下
            if not file_path.startswith(query_dir):
                # 检查 '../person_search/query' 路径下是否存在 .jpg 或 .png 文件
                for filename in os.listdir(query_dir):
                    if filename.endswith('.jpg') or filename.endswith('.png'):
                        # 如果存在，则删除
                        os.remove(os.path.join(query_dir, filename))

                # 复制 file_path 的文件到 '../person_search/query' 路径下
                new_path = os.path.join(query_dir, os.path.basename(file_path))
                shutil.copy2(file_path, new_path)
                # 更新 file_path
                file_path = new_path

            if self.select_person[1] != '':
                self.select_person[0] = self.select_person[1]
                self.select_person[1] = file_path
            else:
                self.select_person[1] = file_path

            print(self.select_person)
            if (self.select_person[0] == '') or (self.select_person[0] != self.select_person[1]):
                self.statistic_label.setText("Re-ID model is loading")
                self.player3.initialize_model()
                self.statistic_label.setText("Re-ID model successfully loaded")

            # 加载并调整图像大小
            image = cv2.imread(file_path)
            image = cv2.resize(image, (self.person_img.width(), self.person_img.height()))  # 将图像调整为 person_img 的尺寸
            pixmap = self.convert_cvimage_to_pixmap(image)
            self.person_img.setPixmap(pixmap)



    def fileInit(self):

        pixmap = QPixmap()
        self.raw_video.setPixmap(pixmap)
        self.out_video.setPixmap(pixmap)
        options = QtWidgets.QFileDialog.Options()
        media_path, _ = QtWidgets.QFileDialog.getOpenFileUrl(self, "QFileDialog.getOpenFileUrl()", "",
                                                             "MP4 Files (*.mp4);;All Files (*)", options=options)
        file_path = media_path.toLocalFile()
        if (file_path == ""):
            return False

        self.player1.get_cap(file_path)
        self.player1.playable = True

        if self.tabWidget.currentIndex() == 0:  #multiple object tracking mode

            self.sys_mode = 0
            # initilize deepsort model
            self.player2.deepsort = DeepSort(self.cfg.DEEPSORT.REID_CKPT,
                                             max_dist=self.cfg.DEEPSORT.MAX_DIST,
                                             min_confidence=self.cfg.DEEPSORT.MIN_CONFIDENCE,
                                             nms_max_overlap=self.cfg.DEEPSORT.NMS_MAX_OVERLAP,
                                             max_iou_distance=self.cfg.DEEPSORT.MAX_IOU_DISTANCE,
                                             max_age=self.cfg.DEEPSORT.MAX_AGE, n_init=self.cfg.DEEPSORT.N_INIT,
                                             nn_budget=self.cfg.DEEPSORT.NN_BUDGET,
                                             use_cuda=True)
            self.player2.playable = True

        elif self.tabWidget.currentIndex() == 1 :   #person Re-ID mode
            self.sys_mode = 1
            if(self.select_person[1] == ''):
                self.statistic_label.setText("Please select the target person first!")
                return
            else:
                 self.player3.playable = True

        self.count = 0
        self.resume()
        return True



    def cameraInit(self):

        self.player1.get_cap(1)
        self.player1.playable = True

        if self.tabWidget.currentIndex() == 0:  # multiple object tracking mode
            # initilize deepsort model
            self.sys_mode = 0

            self.player2.deepsort = DeepSort(self.cfg.DEEPSORT.REID_CKPT,
                                             max_dist=self.cfg.DEEPSORT.MAX_DIST,
                                             min_confidence=self.cfg.DEEPSORT.MIN_CONFIDENCE,
                                             nms_max_overlap=self.cfg.DEEPSORT.NMS_MAX_OVERLAP,
                                             max_iou_distance=self.cfg.DEEPSORT.MAX_IOU_DISTANCE,
                                             max_age=self.cfg.DEEPSORT.MAX_AGE, n_init=self.cfg.DEEPSORT.N_INIT,
                                             nn_budget=self.cfg.DEEPSORT.NN_BUDGET,
                                             use_cuda=True)
            self.player2.playable = True

        elif self.tabWidget.currentIndex() == 1:  # person Re-ID mode
            self.sys_mode = 1
            if (self.select_person[1] == ''):
                self.statistic_label.setText("Please select the target person first!")
                return
            else:
                self.player3.playable = True

        self.count = 0
        self.resume()
        return True






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = Mainwindow()
    player.show()
    app.exec_()

