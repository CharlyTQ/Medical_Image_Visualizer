# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_vtk.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 556)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.utility_Frame = QtWidgets.QFrame(self.centralwidget)
        self.utility_Frame.setGeometry(QtCore.QRect(10, 40, 191, 401))
        self.utility_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.utility_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.utility_Frame.setObjectName("utility_Frame")
        self.layoutWidget = QtWidgets.QWidget(self.utility_Frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 171, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.res_Slider = QtWidgets.QSlider(self.layoutWidget)
        self.res_Slider.setOrientation(QtCore.Qt.Vertical)
        self.res_Slider.setObjectName("res_Slider")
        self.horizontalLayout.addWidget(self.res_Slider)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.vtk_Frame = QtWidgets.QFrame(self.centralwidget)
        self.vtk_Frame.setGeometry(QtCore.QRect(220, 40, 400, 400))
        self.vtk_Frame.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.vtk_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vtk_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vtk_Frame.setObjectName("vtk_Frame")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(220, 450, 401, 61))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(9, 30, 381, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ax_Button = QtWidgets.QRadioButton(self.layoutWidget2)
        self.ax_Button.setChecked(True)
        self.ax_Button.setObjectName("ax_Button")
        self.horizontalLayout_2.addWidget(self.ax_Button)
        self.cor_Button = QtWidgets.QRadioButton(self.layoutWidget2)
        self.cor_Button.setObjectName("cor_Button")
        self.horizontalLayout_2.addWidget(self.cor_Button)
        self.sag_Button = QtWidgets.QRadioButton(self.layoutWidget2)
        self.sag_Button.setObjectName("sag_Button")
        self.horizontalLayout_2.addWidget(self.sag_Button)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 22))
        self.menubar.setObjectName("menubar")
        self.menuOpen_File = QtWidgets.QMenu(self.menubar)
        self.menuOpen_File.setObjectName("menuOpen_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.menuOpen_File.addAction(self.actionOpen_File)
        self.menubar.addAction(self.menuOpen_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "View Selection"))
        self.ax_Button.setText(_translate("MainWindow", "Axial"))
        self.cor_Button.setText(_translate("MainWindow", "Coronal"))
        self.sag_Button.setText(_translate("MainWindow", "Sagittal"))
        self.label.setText(_translate("MainWindow", "Slice"))
        self.menuOpen_File.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
