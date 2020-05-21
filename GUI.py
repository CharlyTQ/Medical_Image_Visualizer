# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.slice_Slider = QtWidgets.QSlider(self.centralwidget)
        self.slice_Slider.setGeometry(QtCore.QRect(400, 90, 22, 371))
        self.slice_Slider.setAcceptDrops(False)
        self.slice_Slider.setOrientation(QtCore.Qt.Vertical)
        self.slice_Slider.setObjectName("slice_Slider")
        self.value_Min = QtWidgets.QLabel(self.centralwidget)
        self.value_Min.setGeometry(QtCore.QRect(430, 450, 47, 13))
        self.value_Min.setObjectName("value_Min")
        self.value_Max = QtWidgets.QLabel(self.centralwidget)
        self.value_Max.setGeometry(QtCore.QRect(420, 80, 47, 13))
        self.value_Max.setObjectName("value_Max")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label_1.setObjectName("label_1")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(420, 240, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.simple_view = MPL_WIDGET(self.centralwidget)
        self.simple_view.setGeometry(QtCore.QRect(30, 60, 341, 431))
        self.simple_view.setObjectName("simple_view")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(680, 70, 118, 83))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ax_Button = QtWidgets.QRadioButton(self.layoutWidget)
        self.ax_Button.setObjectName("ax_Button")
        self.verticalLayout.addWidget(self.ax_Button)
        self.sag_Button = QtWidgets.QRadioButton(self.layoutWidget)
        self.sag_Button.setObjectName("sag_Button")
        self.verticalLayout.addWidget(self.sag_Button)
        self.cor_Button = QtWidgets.QRadioButton(self.layoutWidget)
        self.cor_Button.setObjectName("cor_Button")
        self.verticalLayout.addWidget(self.cor_Button)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(510, 160, 401, 331))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.filter_Enable = QtWidgets.QPushButton(self.layoutWidget1)
        self.filter_Enable.setObjectName("filter_Enable")
        self.horizontalLayout_5.addWidget(self.filter_Enable)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.reset_Button = QtWidgets.QPushButton(self.layoutWidget1)
        self.reset_Button.setObjectName("reset_Button")
        self.horizontalLayout_5.addWidget(self.reset_Button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.filter_Group = QtWidgets.QGroupBox(self.layoutWidget1)
        self.filter_Group.setObjectName("filter_Group")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.filter_Group)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.blur_Button = QtWidgets.QRadioButton(self.filter_Group)
        self.blur_Button.setObjectName("blur_Button")
        self.horizontalLayout.addWidget(self.blur_Button)
        self.gauss_Button = QtWidgets.QRadioButton(self.filter_Group)
        self.gauss_Button.setObjectName("gauss_Button")
        self.horizontalLayout.addWidget(self.gauss_Button)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.filterValue_1 = QtWidgets.QLabel(self.filter_Group)
        self.filterValue_1.setObjectName("filterValue_1")
        self.verticalLayout_4.addWidget(self.filterValue_1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.kernel_Slider = QtWidgets.QSlider(self.filter_Group)
        self.kernel_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.kernel_Slider.setObjectName("kernel_Slider")
        self.horizontalLayout_4.addWidget(self.kernel_Slider)
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.filter_Group)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.horizontalLayout_4.addWidget(self.lcdNumber_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.filterValue_2 = QtWidgets.QLabel(self.filter_Group)
        self.filterValue_2.setObjectName("filterValue_2")
        self.verticalLayout_3.addWidget(self.filterValue_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.x_Slider = QtWidgets.QSlider(self.filter_Group)
        self.x_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.x_Slider.setObjectName("x_Slider")
        self.horizontalLayout_3.addWidget(self.x_Slider)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.filter_Group)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_3.addWidget(self.lcdNumber_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.filterValue_3 = QtWidgets.QLabel(self.filter_Group)
        self.filterValue_3.setObjectName("filterValue_3")
        self.verticalLayout_3.addWidget(self.filterValue_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.y_Slider = QtWidgets.QSlider(self.filter_Group)
        self.y_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.y_Slider.setObjectName("y_Slider")
        self.horizontalLayout_2.addWidget(self.y_Slider)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.filter_Group)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout_2.addWidget(self.lcdNumber_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.filter_Group)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.menuFile.addAction(self.actionOpen_File)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.value_Min.setText(_translate("MainWindow", "Min"))
        self.value_Max.setText(_translate("MainWindow", "Max"))
        self.label_1.setText(_translate("MainWindow", "File Path:"))
        self.ax_Button.setText(_translate("MainWindow", "Axial View"))
        self.sag_Button.setText(_translate("MainWindow", "Sagittal View"))
        self.cor_Button.setText(_translate("MainWindow", "Coronal View"))
        self.filter_Enable.setText(_translate("MainWindow", "Apply Filters"))
        self.reset_Button.setText(_translate("MainWindow", "Reset"))
        self.filter_Group.setTitle(_translate("MainWindow", "Filters"))
        self.blur_Button.setText(_translate("MainWindow", "Bluring"))
        self.gauss_Button.setText(_translate("MainWindow", "Gaussian"))
        self.filterValue_1.setText(_translate("MainWindow", "Kernel Size"))
        self.filterValue_2.setText(_translate("MainWindow", "Sigma X"))
        self.filterValue_3.setText(_translate("MainWindow", "Sigma Y"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
from mplwidget import MPL_WIDGET


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
