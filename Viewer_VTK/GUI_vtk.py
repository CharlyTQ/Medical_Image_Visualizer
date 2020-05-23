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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vtk_Frame = QtWidgets.QFrame(self.centralwidget)
        self.vtk_Frame.setGeometry(QtCore.QRect(220, 39, 561, 491))
        self.vtk_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vtk_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vtk_Frame.setObjectName("vtk_Frame")
        self.utility_Frame = QtWidgets.QFrame(self.centralwidget)
        self.utility_Frame.setGeometry(QtCore.QRect(9, 40, 201, 491))
        self.utility_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.utility_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.utility_Frame.setObjectName("utility_Frame")
        self.view_Box = QtWidgets.QComboBox(self.utility_Frame)
        self.view_Box.setGeometry(QtCore.QRect(20, 20, 151, 25))
        self.view_Box.setObjectName("view_Box")
        self.view_Box.addItem("")
        self.view_Box.addItem("")
        self.view_Box.addItem("")
        self.radioButton = QtWidgets.QRadioButton(self.utility_Frame)
        self.radioButton.setGeometry(QtCore.QRect(10, 80, 112, 23))
        self.radioButton.setObjectName("radioButton")
        self.widget = QtWidgets.QWidget(self.utility_Frame)
        self.widget.setGeometry(QtCore.QRect(0, 130, 201, 381))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.res_Slider = QtWidgets.QSlider(self.widget)
        self.res_Slider.setOrientation(QtCore.Qt.Vertical)
        self.res_Slider.setObjectName("res_Slider")
        self.horizontalLayout.addWidget(self.res_Slider)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.dir_Label = QtWidgets.QLabel(self.centralwidget)
        self.dir_Label.setGeometry(QtCore.QRect(16, 10, 761, 20))
        self.dir_Label.setObjectName("dir_Label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuOpen_File = QtWidgets.QMenu(self.menubar)
        self.menuOpen_File.setObjectName("menuOpen_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOpen_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.view_Box.setItemText(0, _translate("MainWindow", "Points"))
        self.view_Box.setItemText(1, _translate("MainWindow", "Wireframe"))
        self.view_Box.setItemText(2, _translate("MainWindow", "Surface"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.dir_Label.setText(_translate("MainWindow", "File Path:"))
        self.menuOpen_File.setTitle(_translate("MainWindow", "Open File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
