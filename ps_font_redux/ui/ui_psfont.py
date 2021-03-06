# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'psfont.ui',
# licensing of 'psfont.ui' applies.
#
# Created: Mon May 13 16:12:57 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(380, 280)
        MainWindow.statusBar().setSizeGripEnabled(False)
        MainWindow.setFixedSize(380, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 236))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Blur_checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.Blur_checkBox.setIconSize(QtCore.QSize(16, 16))
        self.Blur_checkBox.setObjectName("Blur_checkBox")
        self.verticalLayout.addWidget(self.Blur_checkBox)
        self.Blur_Slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.Blur_Slider.setEnabled(False)
        self.Blur_Slider.setMinimum(1)
        self.Blur_Slider.setMaximum(20)
        self.Blur_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Blur_Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Blur_Slider.setTickInterval(1)
        self.Blur_Slider.setObjectName("Blur_Slider")
        self.verticalLayout.addWidget(self.Blur_Slider)
        self.tex1_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tex1_label.setObjectName("tex1_label")
        self.verticalLayout.addWidget(self.tex1_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.texture1_path = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.texture1_path.setObjectName("texture1_path")
        self.horizontalLayout.addWidget(self.texture1_path)
        self.texture1_browse = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.texture1_browse.setObjectName("texture1_browse")
        self.horizontalLayout.addWidget(self.texture1_browse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tex2_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tex2_label.setObjectName("tex2_label")
        self.verticalLayout.addWidget(self.tex2_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.texture2_path = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.texture2_path.setObjectName("texture2_path")
        self.horizontalLayout_2.addWidget(self.texture2_path)
        self.texture2_browse = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.texture2_browse.setObjectName("texture2_browse")
        self.horizontalLayout_2.addWidget(self.texture2_browse)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.font_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.font_label.setObjectName("font_label")
        self.verticalLayout.addWidget(self.font_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.font_path = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.font_path.setObjectName("font_path")
        self.horizontalLayout_3.addWidget(self.font_path)
        self.font_browse = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.font_browse.setObjectName("font_browse")
        self.horizontalLayout_3.addWidget(self.font_browse)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.start_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.Blur_checkBox.setText(QtWidgets.QApplication.translate("MainWindow", "Background blur", None, -1))
        self.tex1_label.setText(QtWidgets.QApplication.translate("MainWindow", "Fill Texture", None, -1))
        self.texture1_browse.setText(QtWidgets.QApplication.translate("MainWindow", "Browse", None, -1))
        self.tex2_label.setText(QtWidgets.QApplication.translate("MainWindow", "Outline Texture", None, -1))
        self.texture2_browse.setText(QtWidgets.QApplication.translate("MainWindow", "Browse", None, -1))
        self.font_label.setText(QtWidgets.QApplication.translate("MainWindow", "Font file", None, -1))
        self.font_browse.setText(QtWidgets.QApplication.translate("MainWindow", "Browse", None, -1))
        self.start_button.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None, -1))

