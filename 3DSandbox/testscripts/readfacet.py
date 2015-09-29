import vtk
import sys, os
from math import *

reader = vtk.vtkFacetReader()
reader.SetFileName("edges")
edges = reader.GetOutput()
edges.Update()


edgesmapper = vtk.vtkDataSetMapper()
edgesmapper.SetInput(edges)
edgesactor = vtk.vtkActor()
edgesactor.SetMapper(edgesmapper)
edgesactor.GetProperty().SetRepresentationToWireframe()
#edgesactor.GetProperty().SetColor(0,0,0)
edgesactor.GetProperty().SetLineWidth(3)

reader2 = vtk.vtkFacetReader()
reader2.SetFileName("tri")
poly = reader2.GetOutput()
poly.Update()


polymapper = vtk.vtkDataSetMapper()
polymapper.SetInput(poly)
polyactor = vtk.vtkActor()
polyactor.SetMapper(polymapper)
polyactor.GetProperty().SetRepresentationToWireframe()
#polyactor.GetProperty().SetColor(0,0,0)
polyactor.GetProperty().SetLineWidth(3)


# axes actor
axes = vtk.vtkAxesActor()
axes.SetTotalLength(2,2,2)

# more non-intuitive vtk stuff.  SetFontSize changes boldness because
# letters are always scaled to fill width and height defined by the
# actor.
axes.GetXAxisCaptionActor2D().SetWidth(.125)
axes.GetXAxisCaptionActor2D().SetHeight(.05)
axes.GetYAxisCaptionActor2D().SetWidth(.125)
axes.GetYAxisCaptionActor2D().SetHeight(.05)
axes.GetZAxisCaptionActor2D().SetWidth(.125)
axes.GetZAxisCaptionActor2D().SetHeight(.05)


# display

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(600, 600)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
ren.SetBackground(.8,.8,.8)

ren.AddActor(polyactor)
ren.AddActor(edgesactor)
ren.AddActor(axes)

ren.ResetCamera()
ren.GetActiveCamera().ParallelProjectionOn()
ren.ResetCameraClippingRange()

# Render the scene and start interaction.
iren.Initialize()
renWin.Render()
iren.Start()



