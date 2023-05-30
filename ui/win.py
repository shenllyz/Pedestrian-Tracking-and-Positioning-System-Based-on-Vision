# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import qrcs

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1272, 840)
        mainWindow.setMouseTracking(True)
        icon = QIcon()
        icon.addFile(u":/img/icon/\u56fe\u72471.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet(u"#mainWindow{border:none;}")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_18 = QGroupBox(self.centralwidget)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setStyleSheet(u"#groupBox_18{border-image: url(:/img/icon/background.jpg);\n"
"border: 0px solid #42adff;\n"
"border-radius:5px;}")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.groupBox_18)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 45))
        self.groupBox.setMaximumSize(QSize(16777215, 45))
        self.groupBox.setStyleSheet(u"#groupBox{\n"
"background-color: rgba(75, 75, 75, 200);\n"
"border: 0px solid #42adff;\n"
"border-left: 0px solid rgba(29, 83, 185, 255);\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
";\n"
"border-radius:0px;}")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(40, 40))
        self.label_7.setMaximumSize(QSize(40, 40))
        self.label_7.setStyleSheet(u"image: url(:/img/icon/yolo.png);")

        self.horizontalLayout.addWidget(self.label_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_8 = QGroupBox(self.groupBox_18)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(320, 0))
        self.groupBox_8.setMaximumSize(QSize(320, 16777215))
        self.groupBox_8.setStyleSheet(u"#groupBox_8{\n"
"background-color: rgba(75, 75, 75, 200);\n"
"border: 0px solid #42adff;\n"
"border-radius:0px;}\n"
"")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_2 = QGroupBox(self.groupBox_8)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 42))
        self.groupBox_2.setMaximumSize(QSize(16777215, 42))
        self.groupBox_2.setStyleSheet(u"#groupBox_2{\n"
"border: 0px solid #42adff;\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
"border-radius:0px;}")
        self.horizontalLayout_35 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(11, 0, 11, 0)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setStyleSheet(u"QLabel\n"
"{\n"
"	font-size: 22px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-weight: bold;\n"
" 		border-radius:9px;\n"
"		background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"\n"
"}\n"
"")

        self.horizontalLayout_35.addWidget(self.label_5)

        self.horizontalSpacer_13 = QSpacerItem(37, 39, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_13)


        self.verticalLayout_9.addWidget(self.groupBox_2)

        self.groupBox_11 = QGroupBox(self.groupBox_8)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.groupBox_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(80, 16777215))
        self.label_10.setStyleSheet(u"QLabel\n"
"{\n"
"	font-size: 18px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-weight: bold;\n"
" 		border-radius:9px;\n"
"		background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.groupBox_5 = QGroupBox(self.groupBox_11)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"#groupBox_5{\n"
"background-color: rgba(48,148,243,0);\n"
"border: 0px solid #42adff;\n"
"border-left: 0px solid #d9d9d9;\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-radius:0px;}")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.fileButton = QPushButton(self.groupBox_5)
        self.fileButton.setObjectName(u"fileButton")
        self.fileButton.setMinimumSize(QSize(55, 28))
        self.fileButton.setMaximumSize(QSize(16777215, 28))
        self.fileButton.setStyleSheet(u"QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(200, 200, 200,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
""
                        "                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        icon1 = QIcon()
        icon1.addFile(u"icon/\u6253\u5f00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fileButton.setIcon(icon1)

        self.horizontalLayout_8.addWidget(self.fileButton)

        self.cameraButton = QPushButton(self.groupBox_5)
        self.cameraButton.setObjectName(u"cameraButton")
        self.cameraButton.setMinimumSize(QSize(55, 28))
        self.cameraButton.setMaximumSize(QSize(16777215, 28))
        self.cameraButton.setStyleSheet(u"QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(48,148,243,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"   "
                        "                  border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        icon2 = QIcon()
        icon2.addFile(u"icon/\u6444\u50cf\u5934\u5f00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cameraButton.setIcon(icon2)

        self.horizontalLayout_8.addWidget(self.cameraButton)


        self.horizontalLayout_11.addWidget(self.groupBox_5)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)


        self.verticalLayout_9.addWidget(self.groupBox_11)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel\n"
"{\n"
"	font-size: 18px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-weight: bold;\n"
" 		border-radius:9px;\n"
"		background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.BoxSizeSpinBox = QDoubleSpinBox(self.groupBox_8)
        self.BoxSizeSpinBox.setObjectName(u"BoxSizeSpinBox")
        self.BoxSizeSpinBox.setMinimumSize(QSize(50, 0))
        self.BoxSizeSpinBox.setMaximumSize(QSize(50, 16777215))
        self.BoxSizeSpinBox.setAutoFillBackground(False)
        self.BoxSizeSpinBox.setStyleSheet(u"QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
"")
        self.BoxSizeSpinBox.setMinimum(1.000000000000000)
        self.BoxSizeSpinBox.setMaximum(10.000000000000000)
        self.BoxSizeSpinBox.setSingleStep(1.000000000000000)
        self.BoxSizeSpinBox.setValue(2.000000000000000)

        self.horizontalLayout_2.addWidget(self.BoxSizeSpinBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.groupBox_8)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setFamily(u"Microsoft YaHei")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"QLabel\n"
"{\n"
"	font-size: 18px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-weight: bold;\n"
" 		border-radius:9px;\n"
"		background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.confSpinBox = QDoubleSpinBox(self.groupBox_8)
        self.confSpinBox.setObjectName(u"confSpinBox")
        self.confSpinBox.setMinimumSize(QSize(50, 0))
        self.confSpinBox.setMaximumSize(QSize(50, 16777215))
        self.confSpinBox.setAutoFillBackground(False)
        self.confSpinBox.setStyleSheet(u"QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
"")
        self.confSpinBox.setMinimum(0.000000000000000)
        self.confSpinBox.setMaximum(1.000000000000000)
        self.confSpinBox.setSingleStep(0.050000000000000)
        self.confSpinBox.setValue(0.250000000000000)

        self.horizontalLayout_3.addWidget(self.confSpinBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.groupBox_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel\n"
"{\n"
"	font-size: 18px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-weight: bold;\n"
" 		border-radius:9px;\n"
"		background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.iouSpinBox = QDoubleSpinBox(self.groupBox_8)
        self.iouSpinBox.setObjectName(u"iouSpinBox")
        self.iouSpinBox.setMinimumSize(QSize(50, 0))
        self.iouSpinBox.setMaximumSize(QSize(50, 16777215))
        self.iouSpinBox.setAutoFillBackground(False)
        self.iouSpinBox.setStyleSheet(u"QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
"")
        self.iouSpinBox.setMinimum(0.000000000000000)
        self.iouSpinBox.setMaximum(1.000000000000000)
        self.iouSpinBox.setSingleStep(0.050000000000000)
        self.iouSpinBox.setValue(0.400000000000000)

        self.horizontalLayout_4.addWidget(self.iouSpinBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.groupBox_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel\n"
"{\n"
"	font-size: 18px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-weight: bold;\n"
" 		border-radius:9px;\n"
"		background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.TrackSpinBox = QDoubleSpinBox(self.groupBox_8)
        self.TrackSpinBox.setObjectName(u"TrackSpinBox")
        self.TrackSpinBox.setMinimumSize(QSize(50, 0))
        self.TrackSpinBox.setMaximumSize(QSize(50, 16777215))
        self.TrackSpinBox.setAutoFillBackground(False)
        self.TrackSpinBox.setStyleSheet(u"QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u5c55\u5f00.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/\u7bad\u5934_\u5217\u8868\u6536\u8d77.png);}\n"
"")
        self.TrackSpinBox.setDecimals(0)
        self.TrackSpinBox.setMinimum(0.000000000000000)
        self.TrackSpinBox.setMaximum(200.000000000000000)
        self.TrackSpinBox.setSingleStep(5.000000000000000)
        self.TrackSpinBox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.TrackSpinBox.setValue(20.000000000000000)

        self.horizontalLayout_13.addWidget(self.TrackSpinBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.tabWidget = QTabWidget(self.groupBox_8)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"font-size: 13px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-weight: bold;\n"
" 		border-radius:9px;\n"
"		background-color: rgba(118, 118, 118, 200);\n"
"color: rgb(218, 218, 218); ")
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_9 = QGroupBox(self.tab)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(0, 42))
        self.groupBox_9.setMaximumSize(QSize(16777215, 42))
        self.groupBox_9.setStyleSheet(u"#groupBox_9{\n"
"border: 0px solid #42adff;\n"
"border-top: 1px solid rgba(200, 200, 200,100);\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
"border-radius:0px;}")
        self.horizontalLayout_38 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(11, 0, 11, 0)
        self.label_11 = QLabel(self.groupBox_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel\n"
"{\n"
"	font-size: 22px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-weight: bold;\n"
" 		border-radius:9px;\n"
"		background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")

        self.horizontalLayout_38.addWidget(self.label_11)

        self.horizontalSpacer_15 = QSpacerItem(37, 39, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_15)


        self.verticalLayout.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.tab)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(0, 42))
        self.groupBox_10.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_10.setStyleSheet(u"#groupBox_10{\n"
"border: 0px solid #42adff;\n"
"border-radius:0px;}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.resultWidget = QListWidget(self.groupBox_10)
        self.resultWidget.setObjectName(u"resultWidget")
        self.resultWidget.setStyleSheet(u"QListWidget{\n"
"background-color: rgba(12, 28, 77, 0);\n"
"\n"
"border-radius:0px;\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.resultWidget)


        self.verticalLayout.addWidget(self.groupBox_10)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setAutoFillBackground(False)
        self.tab_2.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_6 = QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"#groupBox_6{\n"
"border: 0px solid #42adff;\n"
"border-top: 1px solid rgba(200, 200, 200,100);\n"
"border-bottom: 1px solid rgba(200, 200, 200,100); \n"
"border-radius:0px;}")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel\n"
"{\n"
"	font-size: 18px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-weight: bold;\n"
" 		border-radius:9px;\n"
"		background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.fileButton_2 = QPushButton(self.groupBox_6)
        self.fileButton_2.setObjectName(u"fileButton_2")
        self.fileButton_2.setMinimumSize(QSize(55, 28))
        self.fileButton_2.setMaximumSize(QSize(16777215, 28))
        self.fileButton_2.setStyleSheet(u"QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(200, 200, 200,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
""
                        "                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.fileButton_2.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.fileButton_2)


        self.verticalLayout_5.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.person_img = QLabel(self.groupBox_7)
        self.person_img.setObjectName(u"person_img")
        self.person_img.setMinimumSize(QSize(1, 0))
        self.person_img.setStyleSheet(u"border: 1px solid white;")

        self.verticalLayout_7.addWidget(self.person_img)


        self.verticalLayout_5.addWidget(self.groupBox_7)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 20)
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 1)
        self.verticalLayout_9.setStretch(2, 1)
        self.verticalLayout_9.setStretch(3, 1)
        self.verticalLayout_9.setStretch(4, 1)
        self.verticalLayout_9.setStretch(5, 1)
        self.verticalLayout_9.setStretch(6, 10)

        self.horizontalLayout_7.addWidget(self.groupBox_8)

        self.groupBox_201 = QGroupBox(self.groupBox_18)
        self.groupBox_201.setObjectName(u"groupBox_201")
        self.groupBox_201.setStyleSheet(u"#groupBox_201{\n"
"background-color: rgba(95, 95, 95, 200);\n"
"border: 0px solid #42adff;\n"
"border-left: 1px solid rgba(200, 200, 200,100);\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-radius:0px;}")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_201)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_3 = QGroupBox(self.groupBox_201)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 42))
        self.groupBox_3.setMaximumSize(QSize(16777215, 42))
        self.groupBox_3.setStyleSheet(u"#groupBox_3{\n"
"border: 0px solid #42adff;\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
"border-radius:0px;}")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(11, 0, 11, 0)
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setStyleSheet(u"QLabel\n"
"{\n"
"	font-size: 22px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-weight: bold;\n"
" 		border-radius:9px;\n"
"		background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)

        self.fps_label = QLabel(self.groupBox_3)
        self.fps_label.setObjectName(u"fps_label")
        self.fps_label.setMinimumSize(QSize(100, 40))
        self.fps_label.setMaximumSize(QSize(100, 40))
        self.fps_label.setStyleSheet(u"QLabel\n"
"{\n"
"	font-size: 20px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-weight: bold;\n"
" 		border-radius:9px;\n"
"		background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.fps_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.fps_label)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.splitter = QSplitter(self.groupBox_201)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setStyleSheet(u"#splitter::handle{background: 1px solid  rgba(200, 200, 200,100);}")
        self.splitter.setFrameShape(QFrame.NoFrame)
        self.splitter.setLineWidth(10)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.raw_video = QLabel(self.splitter)
        self.raw_video.setObjectName(u"raw_video")
        self.raw_video.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.raw_video.sizePolicy().hasHeightForWidth())
        self.raw_video.setSizePolicy(sizePolicy1)
        self.raw_video.setMinimumSize(QSize(200, 0))
        self.raw_video.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(36)
        self.raw_video.setFont(font1)
        self.raw_video.setCursor(QCursor(Qt.ArrowCursor))
        self.raw_video.setFocusPolicy(Qt.NoFocus)
        self.raw_video.setStyleSheet(u"color: rgb(218, 218, 218);\n"
"")
        self.raw_video.setScaledContents(False)
        self.raw_video.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.raw_video)
        self.out_video = QLabel(self.splitter)
        self.out_video.setObjectName(u"out_video")
        self.out_video.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.out_video.sizePolicy().hasHeightForWidth())
        self.out_video.setSizePolicy(sizePolicy2)
        self.out_video.setMinimumSize(QSize(200, 0))
        self.out_video.setFont(font1)
        self.out_video.setCursor(QCursor(Qt.ArrowCursor))
        self.out_video.setStyleSheet(u"color: rgb(218, 218, 218);\n"
"")
        self.out_video.setScaledContents(False)
        self.out_video.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.out_video)

        self.verticalLayout_4.addWidget(self.splitter)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.runButton = QPushButton(self.groupBox_201)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setMinimumSize(QSize(40, 40))
        self.runButton.setStyleSheet(u"QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        icon3 = QIcon()
        icon3.addFile(u"icon/\u6682\u505c.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u"icon/\u8fd0\u884c.png", QSize(), QIcon.Normal, QIcon.On)
        icon3.addFile(u"icon/\u6682\u505c.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.runButton.setIcon(icon3)
        self.runButton.setIconSize(QSize(30, 30))
        self.runButton.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.runButton)

        self.stopButton = QPushButton(self.groupBox_201)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(40, 40))
        self.stopButton.setStyleSheet(u"QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        icon4 = QIcon()
        icon4.addFile(u"icon/\u7ec8\u6b62.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon4)
        self.stopButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_12.addWidget(self.stopButton)

        self.progressBar = QProgressBar(self.groupBox_201)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 5))
        self.progressBar.setStyleSheet(u"QProgressBar{ color: rgb(255, 255, 255); font:12pt; border-radius:2px; text-align:center; border:none; background-color: rgba(215, 215, 215,100);} \n"
"QProgressBar:chunk{ border-radius:0px; background: rgba(55, 55, 55, 200);}")
        self.progressBar.setMaximum(1000)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout_12.addWidget(self.progressBar)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_7.addWidget(self.groupBox_201)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.groupBox_4 = QGroupBox(self.groupBox_18)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 30))
        self.groupBox_4.setMaximumSize(QSize(16777215, 30))
        self.groupBox_4.setStyleSheet(u"#groupBox_4{\n"
"background-color: rgba(75, 75, 75, 200);\n"
"border: 0px solid #42adff;\n"
"border-left: 0px solid rgba(29, 83, 185, 255);\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-top: 1px solid rgba(200, 200, 200,100);\n"
"border-radius:0px;}")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.statistic_label = QLabel(self.groupBox_4)
        self.statistic_label.setObjectName(u"statistic_label")
        self.statistic_label.setMouseTracking(False)
        self.statistic_label.setStyleSheet(u"QLabel\n"
"{\n"
"	font-size: 16px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-weight: light;\n"
" 		border-radius:9px;\n"
"		background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.statistic_label)


        self.verticalLayout_6.addWidget(self.groupBox_4)


        self.verticalLayout_2.addWidget(self.groupBox_18)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u884c\u4eba\u68c0\u6d4b\u8ddf\u8e2a\u7cfb\u7edf", None))
        self.groupBox_18.setTitle("")
        self.groupBox.setTitle("")
        self.label_7.setText("")
        self.groupBox_8.setTitle("")
        self.groupBox_2.setTitle("")
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"setting", None))
        self.groupBox_11.setTitle("")
        self.label_10.setText(QCoreApplication.translate("mainWindow", u"input", None))
        self.groupBox_5.setTitle("")
#if QT_CONFIG(tooltip)
        self.fileButton.setToolTip(QCoreApplication.translate("mainWindow", u"file", None))
#endif // QT_CONFIG(tooltip)
        self.fileButton.setText("")
#if QT_CONFIG(tooltip)
        self.cameraButton.setToolTip(QCoreApplication.translate("mainWindow", u"camera", None))
#endif // QT_CONFIG(tooltip)
        self.cameraButton.setText("")
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Box Size                         ", None))
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"Confidence Threshold ", None))
        self.label_9.setText(QCoreApplication.translate("mainWindow", u" IOU Threshold              ", None))
        self.label_12.setText(QCoreApplication.translate("mainWindow", u" Track Length                 ", None))
        self.groupBox_9.setTitle("")
        self.label_11.setText(QCoreApplication.translate("mainWindow", u"Statistics", None))
        self.groupBox_10.setTitle("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"Multiple Object Tracking", None))
        self.groupBox_6.setTitle("")
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"Choose Target Person", None))
#if QT_CONFIG(tooltip)
        self.fileButton_2.setToolTip(QCoreApplication.translate("mainWindow", u"file", None))
#endif // QT_CONFIG(tooltip)
        self.fileButton_2.setText("")
        self.groupBox_7.setTitle("")
        self.person_img.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("mainWindow", u"Person Re-ID", None))
        self.groupBox_201.setTitle("")
        self.groupBox_3.setTitle("")
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"view", None))
        self.fps_label.setText("")
        self.raw_video.setText("")
        self.out_video.setText("")
        self.runButton.setText("")
        self.stopButton.setText("")
        self.groupBox_4.setTitle("")
        self.statistic_label.setText("")
    # retranslateUi

