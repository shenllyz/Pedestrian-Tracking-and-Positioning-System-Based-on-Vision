import sys
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent, QCamera
from PySide2.QtCore import QUrl
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtUiTools import QUiLoader
import win
import cv2
import numpy as np
from PySide2.QtGui import QIcon
from PySide2.QtGui import QImage, QPixmap
import time


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
        self.stopButton.clicked.connect(self.stop)  # stopCamera
        self.runButton.clicked.connect(self.pause)
        self.cap = None
        self.progressBar = self.progressBar
        self.ProgressLength = 1000  # max length of progress bar
        self.count = 0
        self.total_frame = 0

    def updateLength(self):
        if(self.total_Frame != -1): # if not camera
            percent = int((self.count / self.total_Frame) * self.ProgressLength)
            return percent
        else:
            return 0
    def dealFrame(self, frame):  # display video on Qlabel via opencv
        frame_height, frame_width, _ = frame.shape
        label_height = self.raw_video.height()
        label_width = self.raw_video.width()

        aspect_ratio = frame_width / frame_height
        if label_width / label_height > aspect_ratio:
            # fit to height
            resized_height = label_height
            resized_width = int(label_height * aspect_ratio)
        else:
            # fit to width
            resized_width = label_width
            resized_height = int(label_width / aspect_ratio)

        frame = cv2.resize(frame, (resized_width, resized_height))
        # convert OpenCV format to QImage
        bytes_per_line = 3 * resized_width
        q_img = QtGui.QImage(frame.data, resized_width, resized_height, bytes_per_line,
                             QtGui.QImage.Format_RGB888).rgbSwapped()

        # set QImage as the image for raw_video
        self.raw_video.setPixmap(QtGui.QPixmap.fromImage(q_img))
        # maintain Qt event loop
        QtCore.QCoreApplication.processEvents()

    def closeVedio(self):
        self.cap.release()
        cv2.destroyAllWindows()


    def get_cap(self, file_path):
        self.cap = cv2.VideoCapture(file_path)

    def get_delay(self):
        fps = self.cap.get(cv2.CAP_PROP_FPS)  # Get the frames per second of the video
        return int(1000 / fps);

    def pause(self):
        if (self.cap):
            self.play = not self.play
            self.loop(self.ShowFrame)

    def loop(self, func, initFunc=None):
        if (initFunc):

            if (self.cap):
                self.count = 0
                self.closeVedio()

            if (not initFunc()):
                return
            self.play = True

        while True:
            self.total_Frame = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)


            if not self.play:
                return

            if (not func()):
                return
            self.count = self.count + 1
            cv2.waitKey(self.get_delay())

            self.progressBar.setValue(self.updateLength())

    def ShowFrame(self):
        ret, frame = self.cap.read()
        if (ret):
            self.dealFrame(frame)
        return ret

    def fileInit(self):
        pixmap = QPixmap()
        self.raw_video.setPixmap(pixmap)
        options = QtWidgets.QFileDialog.Options()
        media_path, _ = QtWidgets.QFileDialog.getOpenFileUrl(self, "QFileDialog.getOpenFileUrl()", "",
                                                             "MP4 Files (*.mp4);;All Files (*)", options=options)
        file_path = media_path.toLocalFile()
        # print(filt_path)
        if (file_path == ""):
            return False
        self.get_cap(file_path)
        return True

    def cameraInit(self):
        self.get_cap(0)
        return True

    def stop(self):
        if(not self.cap):
            return
        self.play = False
        self.closeVedio()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('yolo.png'))
    player = Mainwindow()
    player.show()

    app.exec_()
