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
 	
	with open("GUI_vtk.ui") as ui_file:
		with open("GUI_vtk.py","w") as py_ui_file:
			uic.compileUi(ui_file,py_ui_file)

	app = QApplication(sys.argv)
	MyApplication = MainFramework()
	MyApplication.show()
	sys.exit(app.exec_()) 