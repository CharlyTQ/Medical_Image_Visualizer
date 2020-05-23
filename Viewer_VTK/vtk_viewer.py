import sys
import os
import vtk

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from GUI_vtk import Ui_MainWindow

class MainFramework(QMainWindow,Ui_MainWindow):

	def __init__(self):

		QMainWindow.__init__(self)

		self.setupUi(self)
		self.setWindowTitle("Medical Image Viewer (VTK)")

if __name__ == "__main__":

	app = QApplication(sys.argv)
	MyApplication = MainFramework()
	MyApplication.show()
	sys.exit(app.exec_()) 