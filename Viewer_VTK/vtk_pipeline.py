#VTK Pipeline to QT GUI
import vtk
import numpy

renderer = vtk.vtkRenderer()
renderer.SetBackground(0.3, 0.4, 0.5)

render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

for sphere_index in range(1):
	source = vtk.vtkSphereSource()
	source.SetRadius(5)
	source.SetCenter(5, 5, 5)
	source.SetPhiResolution(11)
	source.SetThetaResolution(21)

	mapper = vtk.vtkPolyDataMapper()
	mapper.SetInputConnection(source.GetOutputPort())
	actor = vtk.vtkActor()
	actor.SetMapper(mapper)

	renderer.AddActor(actor)

render_window.SetSize(800, 800)
interactor.Initialize()
render_window.Render()
interactor.Start()
