import sys
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
import win
import cv2
import numpy as np
from PySide2.QtGui import QIcon
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtGui import QCloseEvent
import torch
import time
# yolo中部分文件路径固定，必须添加根目录
sys.path.append("..\\yolov5-5.0")
from models.experimental import attempt_load
from utils.general import non_max_suppression, scale_coords
from utils.plots import plot_one_box
from utils.torch_utils import select_device
from utils.datasets import letterbox

from mot.src.deep_reid import DeepReid

class Mainwindow(QtWidgets.QMainWindow, win.Ui_mainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.play = True
        self.button1 = self.fileButton
        self.button2 = self.cameraButton
        self.stopButton = self.stopButton
        self.button1.clicked.connect(lambda: self.loop(self.ShowFrame, self.fileInit))
        self.button2.clicked.connect(lambda: self.loop(self.ShowFrame, self.cameraInit))
        self.BoxSizeSpinBox.valueChanged.connect(lambda x: self.change_val(x, 'BoxSizeSpinBox'))
        self.confSpinBox.valueChanged.connect(lambda x: self.change_val(x, 'confSpinBox'))
        self.iouSpinBox.valueChanged.connect(lambda x: self.change_val(x, 'iouSpinBox'))
        self.stopButton.clicked.connect(self.stop)  # stopCamera
        self.runButton.clicked.connect(self.pause)
        self.conf_thres = 0.25
        self.iou_thres = 0.45
        self.boxsize = 2

        self.frame_update_interval = 10  # 设置每3帧更新一次FPS
        self.frame_count_for_fps = 0  # 添加一个变量用于计算帧数
        self.fps_label = self.fps_label

        self.resultWidget = self.resultWidget
        self.cap = None
        self.current_video = None
        self.progressBar = self.progressBar
        self.ProgressLength = 1000  # max length of progress bar
        self.count = 0
        self.current_count = 0 #当前视频第几帧
        self.total_frame = 0
        self.pause_play_count = True  # False = pause; True = play;
        # Load YOLOv5 model
        gpu_count = torch.cuda.device_count() #初始化gpu
        print(torch.cuda.is_available())
        self.device = select_device('cuda:0')

        self.model = attempt_load('..\\yolov5-5.0\\yolov5s.pt', map_location=self.device)
        self.model.to(self.device).eval()
        self.deep_reid=DeepReid(extractor_config="..\\mot\\src\\configs\\config-test.yaml",
                      extractor_weights="../mot/src/weights/model_final.pth",
                      tracker_config="../mot/src/configs/deep_sort.yaml",
                      device=self.device)


    def change_val(self, x, flag):
        if flag == 'BoxSizeSpinBox':
            self.boxsize = int(x)
        elif flag == 'confSpinBox':
            self.conf_thres = float(x)
        elif flag == 'iouSpinBox':
            self.iou_thres = float(x)

    def show_person_num(self, num_person):
        self.resultWidget.clear()  # 清空列表
        self.resultWidget.addItem(f"Number of people detected: {num_person}")  # 将检测到的人数添加到列表中

    def detect_person(self, frame):
        num_person = 0  # 初始化人数计数器
        if self.current_count != self.count:
            return frame
        im0 = frame.copy()

        # 预处理图像
        img = letterbox(frame, new_shape=(640, 640))[0]  # 使用letterbox函数
        img = img[:, :, ::-1].transpose(2, 0, 1)
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to(self.device)  # 将 NumPy 数组转换为 PyTorch 张量
        img = img.float()
        img /= 255.0

        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # 推理
        with torch.no_grad():  # 关闭自动求导
            pred = self.model(img)[0]

        # Apply NMS
        pred = non_max_suppression(pred, self.conf_thres, self.iou_thres, classes=[0], agnostic=False)

        # 处理检测结果
        bbox_xyxy = []
        confidences = []
        for det in pred:
            if len(det):
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
                for *xyxy, conf, cls in reversed(det):
                    num_person += 1  # 检测到人，计数器加1
                    bbox_xyxy.append(list(map(int, xyxy)))
                    confidences.append(float(conf))

        outputs, added_track_ids = self.deep_reid.update(np.array(bbox_xyxy), confidences, im0)

        for track_id, track_info in outputs.items():
            bbox_xyxy = track_info['bbox']
            conf = track_info['confidence']
            label = f'Person ID-{track_id} '  #{round(conf, 2)}
            plot_one_box(bbox_xyxy, im0, label=label, color=(0, 0, 255), line_thickness=self.boxsize)

        self.show_person_num(num_person)
        return im0

    # def detect_person(self, frame):
    #     num_person = 0  # 初始化人数计数器
    #
    #     if self.current_count != self.count:
    #         return frame
    #     im0 = frame.copy()
    #
    #     # 预处理图像
    #     img = letterbox(frame, new_shape=(640, 640))[0]  # 使用letterbox函数
    #     img = img[:, :, ::-1].transpose(2, 0, 1)
    #     img = np.ascontiguousarray(img)
    #     img = torch.from_numpy(img).to(self.device)  # 将 NumPy 数组转换为 PyTorch 张量
    #     img = img.float()
    #     img /= 255.0
    #
    #     if img.ndimension() == 3:
    #         img = img.unsqueeze(0)
    #
    #     # 推理
    #     with torch.no_grad():  # 关闭自动求导
    #         pred = self.model(img)[0]
    #
    #         # Apply NMS
    #         pred = non_max_suppression(pred, self.conf_thres, self.iou_thres, classes=[0], agnostic=False)
    #
    #     # 处理检测结果
    #     for det in pred:
    #         if len(det):
    #             det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()  # 将边界框坐标从预处理后的图像坐标空间转换为原始图像坐标空间
    #             # 针对每个检测到的边界框，将其标记在原始图像中
    #             for *xyxy, conf, cls in reversed(det):
    #                 num_person += 1  # 检测到人，计数器加1
    #                 label = f'Person {round(float(conf), 2)}'
    #                 plot_one_box(xyxy, im0, label=label, color=(0, 0, 255), line_thickness=self.boxsize)
    #
    #     self.resultWidget.clear()  # 清空列表
    #     self.resultWidget.addItem(f"Number of people detected: {num_person}")  # 将检测到的人数添加到列表中
    #
    #     return im0

    def closeEvent(self, event: QCloseEvent):
        # 在这里执行停止摄像头调用的操作
        self.closeVedio()
        # 最后要调用父类的closeEvent方法，否则窗口无法正常关闭
        super().closeEvent(event)

    def updateLength(self):
        if (self.total_Frame > 0):  # if not camera
            percent = int((self.count / self.total_Frame) * self.ProgressLength)
            return percent
        else:
            return 0

    def dealFrame(self, frame, target_label):  # display video on Qlabel via opencv
        frame_height, frame_width, _ = frame.shape
        label_height = target_label.height()
        label_width = target_label.width()
        #计算显示图像时的高度和宽度,使得每一帧视频尺寸跟ui同比缩放
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

    def closeVedio(self):

        if self.cap:
            self.cap.release()
            cv2.destroyAllWindows()

    def get_cap(self, file_path):
        self.cap = cv2.VideoCapture(file_path)

    def get_delay(self):

        fps = self.cap.get(cv2.CAP_PROP_FPS)  # Get the frames per second of the video
        if fps:
            return int(1000 / fps)
        else:
            return 1

    def pause(self):
        self.pause_play_count = not self.pause_play_count
        if (self.cap):
            if(self.pause_play_count):
                self.play = True
            else:
                self.play = False

            self.loop(self.ShowFrame)


    def loop(self, func, initFunc=None):
        if (initFunc):

            if (self.cap):
                self.count = 0
                self.closeVedio()

            if (not initFunc()):
                return
            self.play = True

        while self.cap.isOpened():

            if not self.play:
                return

            if (not func()):
                return
            self.count = self.count + 1
           # cv2.waitKey(self.get_delay())

            self.progressBar.setValue(self.updateLength())

    def ShowFrame(self):
        start_time = time.time()  # 记录开始时间

        ret, frame = self.cap.read()
        self.total_Frame = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        if ret and self.current_video == self.cap:
            self.dealFrame(frame, self.raw_video)  # Display raw video
            self.current_count = self.count
            detected_frame = self.detect_person(frame)
            self.dealFrame(detected_frame, self.out_video)  # Display detected objects

        end_time = time.time()  # 记录结束时间
        processing_time = end_time - start_time  # 计算处理时间
        fps = 1 / processing_time  # 计算FPS

        self.frame_count_for_fps += 1  # 增加帧计数

        # 只在达到帧数间隔时更新FPS
        if self.frame_count_for_fps % self.frame_update_interval == 0:
            self.fps_label.setText(f"FPS: {round(fps)}")

        return ret


    def fileInit(self):

        pixmap = QPixmap()
        self.raw_video.setPixmap(pixmap)
        self.out_video.setPixmap(pixmap)
        options = QtWidgets.QFileDialog.Options()
        media_path, _ = QtWidgets.QFileDialog.getOpenFileUrl(self, "QFileDialog.getOpenFileUrl()", "",
                                                             "Video Files (*.mp4 *.avi);;All Files (*)", options=options)
        file_path = media_path.toLocalFile()
        # print(filt_path)
        if (file_path == ""):
            return False

        self.stop()  # Stop the current video before loading a new one
        self.get_cap(file_path)

        self.current_video = self.cap  # Update the current_video
        self.deep_reid = DeepReid(extractor_config="..\\mot\\src\\configs\\config-test.yaml",
                                 extractor_weights="../mot/src/weights/model_final.pth",
                                 tracker_config="../mot/src/configs/deep_sort.yaml",
                                 device=self.device)
        return True

    def cameraInit(self):
        self.get_cap(0)
        self.current_video = self.cap  # Update the current_video
        return True

    def stop(self):
        if (not self.cap or not self.play):
            return
        self.play = False
        self.closeVedio()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('yolo.png'))
    player = Mainwindow()

    player.show()

    app.exec_()
