import sys
import os
import vtk

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from GUI_vtk import Ui_MainWindow
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class MainFramework(QMainWindow,Ui_MainWindow):
    
    def __init__(self):

        QMainWindow.__init__(self)

        self.setupUi(self)
        self.setWindowTitle("Medical Image Viewer")

        #Mainframe Variables

        self.map = None
        self.reader = None
        self.cam = None
        self.center_cam = None
        self.size = None

        self.spinBox.setEnabled(False)
        self.res_Slider.setMaximum(200)

        self.actionOpen_File.triggered.connect(self.open_File)
        self.res_Slider.valueChanged.connect(self.valuechange)
        self.ax_Button.clicked.connect(self.changeView)
        self.cor_Button.clicked.connect(self.changeView)
        self.sag_Button.clicked.connect(self.changeView)

        #VTK Viewer

        self.vtk_Viewer = QVTKRenderWindowInteractor(self.vtk_Frame)
        self.vtk_Viewer.SetSize(800,800)
        self.ren = vtk.vtkRenderer()
        self.vtk_Viewer.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtk_Viewer.GetRenderWindow().GetInteractor()
        style = vtk.vtkInteractorStyleImage()
        style.SetInteractionModeToImageSlicing()
        self.iren.SetInteractorStyle(style)

    def open_File(self):
        path = os.path.join(os.path.dirname(sys.argv[0]))
        file_dialog = QFileDialog(self,"Open File",path,"Naïve Image Formats (*.nii *.nii.gz)")
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        if file_dialog.exec_() == file_dialog.Accepted:
            self.reader = vtk.vtkNIFTIImageReader()
            self.reader.SetFileName('brain1.nii')
            self.reader.Update()
            self.path_Label.setText('File Name: brain1')
            self.path_Label.adjustSize()

            #Data Processing
            self.size = self.reader.GetOutput().GetDimensions()
            center = self.reader.GetOutput().GetCenter()
            spacing = self.reader.GetOutput().GetSpacing()
            print('size:' + str(self.size))
            print('center:' + str(center))

            self.center_cam = (center[0], center[1], center[2])

            #Get graysacle Range
            vrange = self.reader.GetOutput().GetScalarRange()

            #Set Image Slicer Mappers for each view

            self.map = vtk.vtkImageSliceMapper()
            self.map.BorderOn()
            self.map.SliceAtFocalPointOn()
            self.map.SliceFacesCameraOn()
            self.map.SetInputConnection(self.reader.GetOutputPort())

            self.slice = vtk.vtkImageSlice()
            self.slice.SetMapper(self.map)
            self.slice.GetProperty().SetColorWindow(vrange[1]-vrange[0])
            self.slice.GetProperty().SetColorLevel(0.5*(vrange[0]+vrange[1]))

            self.ren.AddActor(self.slice)

            self.cam = self.ren.GetActiveCamera()
            self.cam.ParallelProjectionOn()
            self.cam.SetParallelScale(0.5*spacing[1]*self.size[1])
            self.cam.SetFocalPoint(self.center_cam[0], self.center_cam[1], self.center_cam[2])
            print(self.center_cam)

            self.changeView()
            self.spinBox.setEnabled(True)

        else:
            print("Operation Failed")

    def valuechange(self):
        s = self.res_Slider.value()
        self.spinBox.setValue(s)

        if self.ax_Button.isChecked():
            #Axial Plane
            self.cam.SetFocalPoint(self.center_cam[0], self.center_cam[1], s)

        if self.cor_Button.isChecked():
            #Coronal Plane
            self.cam.SetFocalPoint(self.center_cam[0], s, self.center_cam[2])

        if self.sag_Button.isChecked():
            #Sagital Plane
            self.cam.SetFocalPoint(s, self.center_cam[1], self.center_cam[2])
        
        self.show()
        self.iren.Initialize()

    def changeView(self):
        if self.reader:
            if self.cor_Button.isChecked():
            #Coronal Plane
                self.cam.SetFocalPoint(self.center_cam[0], self.center_cam[1], self.center_cam[2])
                self.cam.SetPosition(95.5,0,88)
                self.res_Slider.setMaximum(self.size[1])
                self.res_Slider.setValue(self.center_cam[1])

            if self.sag_Button.isChecked():
            #Sagital Plane
                self.cam.SetFocalPoint(self.center_cam[0], self.center_cam[1], self.center_cam[2])
                self.cam.SetPosition(256,95.5,87.5)
                self.res_Slider.setMaximum(self.size[0])
                self.res_Slider.setValue(self.center_cam[0])

            #Axial Plane
            if self.ax_Button.isChecked():
                self.cam.SetFocalPoint(self.center_cam[0], self.center_cam[1], self.center_cam[2])
                self.cam.SetPosition(87.5,95.5,256)
                self.res_Slider.setMaximum(self.size[2])
                self.res_Slider.setValue(self.center_cam[2])

            self.show()
            self.iren.Initialize()


if __name__ == "__main__":
 
    app = QApplication(sys.argv)
    MyApplication = MainFramework()
    MyApplication.show()
    sys.exit(app.exec_()) 