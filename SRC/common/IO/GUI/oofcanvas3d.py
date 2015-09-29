# -*- python -*-
# $RCSfile: oofcanvas3d.py,v $
# $Revision: 1.13 $
# $Author: langer $
# $Date: 2014/09/27 21:40:35 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import gtk
from gtk import gdk
import math
from ooflib.SWIG.common import ooferror
from ooflib.common import color
from ooflib.common import primitives
from ooflib.common import mainthread
from ooflib.common.IO import voxelpicker
from ooflib.SWIG.common.IO import bitoverlay
from ooflib.SWIG.image import oofimage3d
from ooflib.SWIG.image import resampleimage
#from ooflib.image import oofimage3d

# TODO: NEEDS MAJOR CLEANUP - will be done when we convert to c++

class View:

    def __init__(self,pos,focal,up,angle=30,clip=100):
        self.pos = pos
        self.focal = focal
        self.up = up
        self.angle = angle
        self.clip = clip


class OOFCanvas3DLayer:

    def __init__(self, canvas):
        self.canvas = canvas
        self.resample = None
        self.inputPort = None
        self.image = None
        self.volume = None
        self.polyActor = None
        self.glyphActor = None
        # self.grid can be either a vtkPolyData or a vtkUnstructuredGrid
        self.grid = None
        self.scalarbar = None
        self.showing = True

    def make_current(self):
        self.canvas.current_layer = self

    def clear(self):
        #self.detach_from_pipeline()
        self.resample=None
        self.image=None
        # call from attach/detach?
        #self.canvas.update_highest_showing_volume()
        if self.polyActor is not None:
            self.canvas._Renderer.RemoveActor(self.polyActor)
            self.polyActor = None
            self.grid = None
        if self.glyphActor is not None:
            self.canvas._Renderer.RemoveActor(self.glyphActor)
            self.glyphActor = None

    def show(self):
        if not self.showing: # don't do anything if layer already showing
            self.showing = True
            #self.attach_to_pipeline()
           
    def hide(self):
        if self.showing: # don't do anything if layer already hidden
            self.showing = False
            #self.detach_from_pipeline()

    def raise_to_top(self):
        self.canvas.layers.remove(self)
        self.canvas.layers.insert(0, self)

    def raise_layer(self, howfar):
        index = self.get_index()
        self.canvas.layers.remove(self)
        self.canvas.layers.insert(index-howfar, self)

    def lower_layer(self, howfar):
        index = self.get_index()
        self.canvas.layers.remove(self)
        self.canvas.layers.insert(index+howfar, self)

    def add_image(self, image):
        self.image = image

    def get_index(self):
        return self.canvas.layers.index(self)

    def add_scalarbar(self, lookuptable, textcolor):
        self.scalarbar = vtk.vtkScalarBarActor()
        self.scalarbar.SetLookupTable(lookuptable)
        # TODO 3D: This should be smart about coordinating with the
        # background, and perhaps be settable by the user.
        self.scalarbar.GetLabelTextProperty().SetColor(textcolor.getRed(), 
                                                       textcolor.getGreen(), 
                                                       textcolor.getBlue())
        self.scalarbar.GetLabelTextProperty().ShadowOff()
        self.scalarbar.GetLabelTextProperty().ItalicOff()
        self.scalarbar.SetPosition(.1,.1)
        self.scalarbar.SetWidth(.8)

    def add_resample(self, resample):
        self.resample = resample
        # get the next lowest image layer and make that our input if
        # we don't already have one
        self.find_inputPort()
##         if self.inputPort is not None:
##             self.resample.SetInputConnection(self.inputPort)
##             self.image = self.resample.GetOutput()
##         else:
##             # This is reached if we lower a resampled layer to where
##             # there is no lower layer.  In that case, do nothing.
##             pass

        #self.attach_to_pipeline()

    def add_grid(self, grid, lineColor, lineWidth, filled=False):
        self.grid = grid
        polyMapper = vtk.vtkDataSetMapper()
        polyMapper.SetInput(self.grid)
        self.polyActor = vtk.vtkActor()
        self.polyActor.SetMapper(polyMapper)
        self.polyActor.GetProperty().SetRepresentationToWireframe()
        self.polyActor.GetProperty().SetAmbient(1.0)
        self.polyActor.GetProperty().SetColor(lineColor.getRed(),
                                              lineColor.getGreen(),
                                              lineColor.getBlue())
        if not filled:
            self.polyActor.GetProperty().SetLineWidth(lineWidth)
            self.polyActor.GetProperty().SetRepresentationToWireframe()
        else:
            self.polyActor.GetProperty().SetRepresentationToSurface()
            

    def add_grid_with_lookuptable(self, grid, lookuptable, mode="cell"):
        self.grid = grid
        polyMapper = vtk.vtkDataSetMapper()
        #polyMapper = vtk.vtkUnstructuredGridVolumeRayCastMapper()
        polyMapper.SetInput(self.grid)
        self.polyActor = vtk.vtkActor()
        self.polyActor.SetMapper(polyMapper)
        #self.volume = vtk.vtkVolume()
        #self.volume.SetMapper(polyMapper)
        polyMapper.SetScalarRange(lookuptable.GetTableRange())
        if mode == "cell":
            polyMapper.SetScalarModeToUseCellData()
        elif mode == "point":
            polyMapper.SetScalarModeToUsePointData()
        polyMapper.SetLookupTable(lookuptable)
        self.polyActor.GetProperty().SetRepresentationToSurface()


    def add_glyphs(self, grid, source, color):
        glyph = vtk.vtkGlyph3D()
        glyph.SetInput(grid)
        glyph.SetSource(source.GetOutput())
        glyph.SetVectorModeToUseNormal()
        glyphmapper = vtk.vtkPolyDataMapper()
        glyphmapper.SetInput(glyph.GetOutput())
        self.glyphActor = vtk.vtkActor()
        self.glyphActor.SetMapper(glyphmapper)
        self.glyphActor.GetProperty().SetColor(color.getRed(),
                                               color.getGreen(),
                                               color.getBlue())
    
    def add_dot(self, pos, lineColor, lineWidth):
        if self.polyActor is None:
            self.points = vtk.vtkPoints()
            self.points.SetNumberOfPoints(100)
            self.grid = vtk.vtkPolyData()
            self.grid.Allocate(100,100)
            self.grid.SetPoints(self.points)
            mapper = vtk.vtkDataSetMapper()
            mapper.SetInput(self.grid)
            self.polyActor = vtk.vtkActor()
            self.polyActor.SetMapper(mapper)

        id = self.points.GetNumberOfPoints()
        self.points.InsertNextPoint(pos[0],pos[1],pos[2])
        vertex = vtk.vtkVertex()
        vertex.GetPointIds().SetId(0,id)
        self.grid.InsertNextCell(vertex.GetCellType(), vertex.GetPointIds())
        self.polyActor.GetProperty().SetPointSize(lineWidth)
        self.polyActor.GetProperty().SetColor(lineColor.getRed(),
                                             lineColor.getGreen(),
                                             lineColor.getBlue())
            
            


    def set_input(self, port):
        self.resample.SetInputConnection(port)


    # TODO: eventually we should have different classes for the
    # different types of layers
    def get_output(self):
        if self.resample is not None:
            return self.resample.GetOutput().GetProducerPort()
        if self.image is not None:
            return self.image.GetProducerPort()

    def get_extent(self):
        if self.resample is not None:
            return self.resample.GetExtent()
        if self.image is not None:
            return self.image.GetExtent()

    def find_inputPort(self):
        index = self.get_index()
        self.inputPort = None
        for layer in self.canvas.layers[index+1:]:
            if layer.image is not None and self.inputPort is None:
                self.inputPort = layer.image.GetProducerPort()
        

    def attach_to_pipeline(self):
        # find next layer with resample member and inject our input
        if self.image is not None:
            index = self.get_index()
            under_opaque_layer = False
            for layer in self.canvas.layers[:index]:
                if layer.resample is not None and not under_opaque_layer:
                    layer.inputPort = self.image.GetProducerPort()
                    layer.resample.SetInputConnection(layer.inputPort)
                elif layer.resample is None and layer.image is not None:
                    under_opaque_layer = True


    def detach_from_pipeline(self):
        self.find_inputPort()
        if self.image is not None:
            index = self.get_index()
            for layer in self.canvas.layers[:index]:
                if layer.resample is not None:
                    layer.inputPort = self.inputPort
                    layer.resample.SetInputConnection(layer.inputPort)
        if self.resample is not None:
            self.resample.RemoveAllInputs()


    def destroy(self):
        self.clear()


        
        

class OOFCanvas3D(gtk.DrawingArea):    

    def __init__(self, settings):

        gtk.DrawingArea.__init__(self)

        self._RenderWindow = vtk.vtkRenderWindow()
        # for the ghost graphics window
        #if self.offscreen:
            #self._RenderWindow.OffScreenRenderingOn()
            #self._RenderWindow.SetOffScreenRendering(1)
        #    self._RenderWindow.SetSize(600,600)
        self.__Created = 0
        self.__Exposed = 0

        # This controls the quality of the images, the lower the
        # number, the better the quality.  _DesiredUpdateRate is for
        # interactive stuff (tumbling, rubberband, etc),
        # _StillUpdateRate is for still. TODO 3D: This should probably
        # be something the user can set.
        self._DesiredUpdateRate = 1
        self._StillUpdateRate = 0.0001

        self.connectSignals()

        # need this to be able to handle key_press events.
        self.set_flags(gtk.CAN_FOCUS)
        # default size
        self.set_size_request(300, 300)

        self._Renderer =  vtk.vtkRenderer()
        self._RenderWindow.AddRenderer(self._Renderer)
        self._Camera = self._Renderer.GetActiveCamera()
        
        # using two renderers with different viewports for the main
        # display and the scalarbar widget. 
        width = settings.contourpanewidth
        if settings.showcontourpane:
            self._ContourRenderer = vtk.vtkRenderer()
            self._Renderer.SetViewport(0,0,1-width,1)
            self._ContourRenderer.SetViewport(1-width,0,1,1)
            self._RenderWindow.AddRenderer(self._ContourRenderer)
        else:
            self._Renderer.SetViewport(0,0,1,1)
            self._ContourRenderer = None

        # point smoothing seems to be cheap so we always do it
        self._RenderWindow.PointSmoothingOn()
        if settings.antialias:
            # there are two simple ways to achieve smoothing in vtk,
            # the "LineSmoothing" option appears to be cheaper and
            # better than the actual anti-aliasing option.
            # self._RenderWindow.SetAAFrames(6)
            self._RenderWindow.LineSmoothingOn()
            self._RenderWindow.PolygonSmoothingOn()

        #self._ViewportCenterX = 0
        #self._ViewportCenterY = 0

        self._ClippingRange = (0,0)
        
        self._Picker = voxelpicker.VoxelPicker()
        self._Picker.SetTolerance(.5)
        
        #self._OldFocus = None

        # these record the previous mouse position
        self._LastX = 0
        self._LastY = 0

        self.empty = True
        self.current_layer = None
        self.layers = []

        self.mouse_callback = None
        self.rubberband = None
        self.mousedown = False
        self.mousedown_point = None

        self.lineWidth = None
        self.lineColor = None
        self.glyphSize = None
        self.lookupTable = None
        self.fillColor = None

        # objects used by volume actor
        self.volproperty = vtk.vtkVolumeProperty()
        self.volproperty.IndependentComponentsOff()
#         self.red = vtk.vtkColorTransferFunction()
#         self.red.AddRGBSegment(0,0,0,0,255,1,0,0)
#         self.volproperty.SetColor(0,self.red)
#         self.green = vtk.vtkColorTransferFunction()
#         self.green.AddRGBSegment(0,0,0,0,255,0,1,0)
#         self.volproperty.SetColor(1,self.green)
#         self.blue = vtk.vtkColorTransferFunction()
#         self.blue.AddRGBSegment(0,0,0,0,255,0,0,1)
#         self.volproperty.SetColor(2,self.blue)
        self.opacity = vtk.vtkPiecewiseFunction()
        self.opacity.AddSegment(0,1,255,0)
        self.volproperty.SetScalarOpacity(self.opacity)

        self.planeActors = []
        
        self.set_bgColor(settings.bgcolor)
        self.set_contourmap_bgColor(settings.contourmap_bgcolor)
        self.set_contourmap_textcolor(settings.contourmap_textcolor)
        self.set_margin(settings.margin)

        self.clip = 100


    def set_mouse_callback(self, callback):
        self.mouse_callback = callback
        self.connect("event", self.mouse_event)
            

    def set_margin(self, fraction):
        self.margin = fraction

    
    def get_view(self):
        pos = self._Camera.GetPosition()
        focal = self._Camera.GetFocalPoint()
        up = self._Camera.GetViewUp()
        angle = self._Camera.GetViewAngle()
        clip = self.clip

        return View(pos,focal,up,angle,clip)


    def set_view(self, view):
        self._Camera.SetPosition(view.pos)
        self._Camera.SetFocalPoint(view.focal)
        self._Camera.SetViewUp(view.up)
        self._Camera.SetViewAngle(view.angle)
        self.calculateclipping(view.clip)
        self.setSampleDistances()
        self.render()
    

    def mouse_event(self, wid, event):
        # TODO 3D: not sure if this is doing everything the C++ 2D version does...
        # check that we are not dragging another window around....
        eventtype = None
        (x, y) = self.get_pointer()
        if event.type == gdk.BUTTON_PRESS:
            eventtype = "down"
            self.mousedown = True
            self.mousedown_point = self.screenCoordsTo3DCoords(x,y)
            self._RenderWindow.SetDesiredUpdateRate(self._DesiredUpdateRate)
            # if we do this here, we won't need to do it in toolbarGUI
        if event.type == gdk.BUTTON_RELEASE:
            eventtype = "up"
            if self.rubberband and self.rubberband.active():
                self.rubberband.stop(self._Renderer)
                self.render()
            self.mousedown = False
            self._RenderWindow.SetDesiredUpdateRate(self._StillUpdateRate)
        if event.type == gdk.MOTION_NOTIFY:
            eventtype = "move"
            if self.mousedown and self.rubberband:
                if not self.rubberband.active():
                    self.rubberband.start(self.mousedown_point)
                if self.rubberband.active(): 
                    # we don't want to use "else" here because the
                    # call above can change whether it is active.  We
                    # use this condition because
                    # screenCoordsTo3DCoords and render are expensive
                    # and make things like tumbling laggy.
                    newpoint = self.screenCoordsTo3DCoords(x,y)
                    self.rubberband.redraw(self._Renderer, newpoint)
                    self.render()
        if eventtype is not None:
            shift = (event.state & gdk.SHIFT_MASK) != 0
            ctrl = (event.state & gdk.CONTROL_MASK) != 0
            # TODO 3D: maybe x,y,z should be calculated here. The
            # arguments to all mousehandler objects would have to be
            # changed.
            self.mouse_callback(eventtype, x, y, shift, ctrl)
        
    def newLayer(self):
        self.current_layer = OOFCanvas3DLayer(self)
        self.layers.insert(0,self.current_layer)
        return self.current_layer
                    

    def is_empty(self):
        # self.empty is set to true by self.clear
        # set to false by self.draw_dot, self.draw_triangle,
        # self.draw_segment(s), self.draw_curve... and draw_image
        return self.empty

    def set_bgColor(self, color):
        self._Renderer.SetBackground(color.getRed(), color.getGreen(), color.getBlue())

    def set_contourmap_bgColor(self, color):
        if self._ContourRenderer is not None:
            self._ContourRenderer.SetBackground(color.getRed(), color.getGreen(), color.getBlue())

    def set_contourmap_textcolor(self, color):
        self.contourmap_textcolor = color

    def set_lineColor(self, color):
        self.lineColor = color

    def set_fillColor(self, color, alpha=1):
        self.fillColor = color

    def set_lineWidth(self, width):
        self.lineWidth = width

    def set_glyphSize(self, size):
        self.glyphSize = size
        
    def set_lookupTable(self, lut):
        self.lookupTable = lut

    def get_next_layer(self, layer):
        idx = self.layers.index(layer)
        return self.layers[idx+1]

    def construct_pipeline(self):
        self.remove_all_volumes()

        # construct the pipeline from the top down
        #layerscopy = self.layers[:]
        if len(self.layers):
            layer = self.layers[0]
            #layer = layerscopy.pop(0)
            while layer.image is None and self.layers.index(layer) < (len(self.layers)-1):
            # for layer in self.layers:
                if layer.showing and layer.resample is not None:
                    layer.resample.RemoveAllInputs()
                    # get next lowest showing layer, if any
                    #nextlayer = layerscopy.pop(0)
                    try:
                        nextlayer = self.get_next_layer(layer)
                        output = nextlayer.get_output()
                        while not nextlayer.showing or output is None:
                            nextlayer = self.get_next_layer(nextlayer)
                            output = nextlayer.get_output()
                        layer.set_input(nextlayer.get_output())
                        layer = nextlayer
                    except IndexError:
                        print "rlly sorry, no layers for input"
                        break
                else:
                    layer = self.get_next_layer(layer)

                

    # This should be the only function that adds an actor or volume to the renderer.
    def update_displayed_layers(self):
        self.remove_all_props()
                
        grid_layers = []

        for layer in self.layers:

            # add the grid layers to a list  
            if layer.showing and layer.polyActor is not None:
                grid_layers.append(layer)
                
            # if there is an unstructured grid / polydata volume
            # add that to the renderer and stop
#             if layer.showing and layer.volume is not None:
#                 print "got volume"
#                 self._Renderer.AddVolume(layer.volume)
#                 if layer.scalarbar is not None:
#                     self._ContourRenderer.AddActor(layer.scalarbar)
#                 #self.setSampleDistances()
#                 #self.empty = False
#                 break 

            # the "output" is the output for image volumes, this part
            # adds the highest showing image volume
            output = layer.get_output()
            if layer.showing and output is not None:
                mapper = vtk.vtkFixedPointVolumeRayCastMapper()
                mapper.IntermixIntersectingGeometryOn()
                mapper.SetInputConnection(output)
                mapper.Update()
                volume = vtk.vtkVolume()
                volume.SetMapper(mapper) 
                volume.SetProperty(self.volproperty)

        
                # TODO 3D: For some reason this particular line causes
                # a seg fault in threaded text mode.  Figure this out
                # if it's still a problem after cleaning up graphics
                # window stuff.
                self._Renderer.AddVolume(volume)
                self.setSampleDistances()
                self.empty = False
                break 

        # add the topmost scalar bar
        for layer in grid_layers:
            if layer.scalarbar is not None and self._ContourRenderer is not None:
                self._ContourRenderer.AddActor(layer.scalarbar)
                self.empty = False
                break

        # draw the grid from the bottom up
        grid_layers.reverse()
        for layer in grid_layers:
            self._Renderer.AddActor(layer.polyActor)
            if layer.glyphActor is not None:
                self._Renderer.AddActor(layer.glyphActor)

        # draw the plane actors
        for actor in self.planeActors:
            self._Renderer.AddActor(actor)

       

    def remove_all_volumes(self):
        volumes = self._Renderer.GetVolumes()
        volumes.InitTraversal()
        for i in xrange(volumes.GetNumberOfItems()):
            volume = volumes.GetNextItem()
            self._Renderer.RemoveVolume(volume)

    def remove_all_actors(self):
        actors = self._Renderer.GetActors()
        actors.InitTraversal()
        for i in xrange(actors.GetNumberOfItems()):
            actor = actors.GetNextItem()
            self._Renderer.RemoveActor(actor)

    # Props are the superclass that includes volumes, 3D actors and 2D actors.
    def remove_all_props(self):
        self._Renderer.RemoveAllViewProps()
        if self._ContourRenderer is not None:
            self._ContourRenderer.RemoveAllViewProps()


    def draw_scalarbar(self, lookuptable):
        self.current_layer.add_scalarbar(lookuptable, self.contourmap_textcolor)


    def draw_voxel(self, voxel):

        voxelPoints = vtk.vtkPoints()
        voxelPoints.SetNumberOfPoints(8)
        voxelPoints.InsertPoint(0, voxel.x, voxel.y, voxel.z)
        voxelPoints.InsertPoint(1, voxel.x+1, voxel.y, voxel.z)
        voxelPoints.InsertPoint(2, voxel.x, voxel.y+1, voxel.z)
        voxelPoints.InsertPoint(3, voxel.x+1, voxel.y+1, voxel.z)
        voxelPoints.InsertPoint(4, voxel.x, voxel.y, voxel.z+1)
        voxelPoints.InsertPoint(5, voxel.x+1, voxel.y, voxel.z+1)
        voxelPoints.InsertPoint(6, voxel.x, voxel.y+1, voxel.z+1)
        voxelPoints.InsertPoint(7, voxel.x+1, voxel.y+1, voxel.z+1)
        voxel = vtk.vtkVoxel()
        for i in xrange(8):
            voxel.GetPointIds().SetId(i,i)
        voxelGrid = vtk.vtkUnstructuredGrid()
        voxelGrid.Allocate(1, 1)
        voxelGrid.InsertNextCell(voxel.GetCellType(), voxel.GetPointIds())
        voxelGrid.SetPoints(voxelPoints)
        self.current_layer.add_grid(voxelGrid, self.lineColor, self.lineWidth)


    def draw_cell(self, cell, filled=False):
        cellPoints = cell.GetPoints()
        type = cell.GetCellType()
        numpts = cellPoints.GetNumberOfPoints()
        newcell = vtk.vtkGenericCell()
        newcell.SetCellType(type)
        #if self.current_layer.grid is None:
        cellGrid = vtk.vtkUnstructuredGrid()
        cellGrid.Allocate(1,1)
        cellGrid.SetPoints(cellPoints)
        for i in xrange(numpts):
            newcell.GetPointIds().SetId(i,i)
        #else:
        #    cellGrid = self.current_layer.grid
        #    numExistingPoints = cellGrid.GetPoints().GetNumberOfPoints()
        #    for i in xrange(numpts):
        #        cellGrid.GetPoints().InsertNextPoint(cellPoints.GetPoint(i))
        #        newcell.GetPointIds().SetId(i,numExistingPoints+i)
        cellGrid.InsertNextCell(type, newcell.GetPointIds())
        self.current_layer.add_grid(cellGrid, self.lineColor, self.lineWidth, filled)
        


    def draw_alpha_image(self, bitmap, location, size):
        resample = resampleimage.ResampleImage()
        resample.SetBitmap(bitmap)
        self.current_layer.add_resample(resample)
                  

    def draw_image(self, oofimage, offset, size):
        image = oofimage.getImageData()
        self.current_layer.add_image(image)
        self._Picker.SetImage(image)
        #self.update_highest_showing_volume()

    def draw_unstructuredgrid(self, grid):
        self.current_layer.add_grid(grid, self.lineColor, self.lineWidth, 
                                        filled=False)


    def draw_unstructuredgrid_with_lookuptable(self, grid, lookuptable, mode="cell", scalarbar=True):
        self.current_layer.add_grid_with_lookuptable(grid, lookuptable, mode)
        if scalarbar:
            self.current_layer.add_scalarbar(lookuptable, self.contourmap_textcolor)


    def draw_filled_unstructuredgrid(self, grid):
        self.current_layer.add_grid(grid, self.lineColor, self.lineWidth, 
                                        filled=True)


    def draw_dot(self, pos):
        self.current_layer.add_dot(pos, self.lineColor, self.lineWidth)

    def draw_cone_glyphs(self, grid):
        cone = vtk.vtkConeSource()
        cone.SetRadius(float(self.glyphSize)/2)
        cone.SetHeight(self.glyphSize)
        cone.SetResolution(20)
        self.current_layer.add_glyphs(grid, cone, self.lineColor)

       
    def connectSignals(self):
        self.connect("realize", self.onRealize)
        self.connect("expose_event", self.onExpose)
        self.connect("configure_event", self.onConfigure)
        self.connect("delete_event", self.onDestroy)
        self.add_events(gdk.EXPOSURE_MASK|
                        gdk.BUTTON_PRESS_MASK |
                        gdk.BUTTON_RELEASE_MASK |
                        gdk.KEY_PRESS_MASK |
                        gdk.POINTER_MOTION_MASK |
                        gdk.POINTER_MOTION_HINT_MASK |
                        gdk.ENTER_NOTIFY_MASK |
                        gdk.LEAVE_NOTIFY_MASK)

    def getRenderWindow(self):
        return self._RenderWindow

    def getRenderer(self):
        return self._Renderer

    def getCamera(self):
        return self._Camera

##     def setDesiredUpdateRate(self, rate):
##         self._DesiredUpdateRate = rate

##     def getDesiredUpdateRate(self):
##         return self._DesiredUpdateRate 
   
##     def SetStillUpdateRate(self, rate):
##         self._StillUpdateRate = rate

##     def GetStillUpdateRate(self):
##         return self._StillUpdateRate

    def getPicker(self):
        return self._Picker

    # This should only be called by higher level classes (with the
    # exception of the expose callback).  Rendering is expensive, we
    # only want to render when we are really ready.
    def render(self):
        if self.__Exposed:
            mainthread.run(self._RenderWindow.Render)
            

    def update_volume_and_render_threaded(self):
        if self.__Exposed:
            self.construct_pipeline()
            self.update_displayed_layers()
            self._RenderWindow.Render()

    def update_volume_and_render(self):
        mainthread.run(self.update_volume_and_render_threaded)

    def onRealize(self, *args):
        if self.__Created == 0:
            # you can't get the xid without the window being realized.
            self.realize()
            win_id = str(self.widget.window.xid)
            self._RenderWindow.SetWindowInfo(win_id)
            self.__Created = 1
        return True

    def onConfigure(self, wid, event=None):
        self.widget=wid
        sz = self._RenderWindow.GetSize()
        
        if (event.width != sz[0]) or (event.height != sz[1]):
            self._RenderWindow.SetSize(event.width, event.height)
        return True

    def onExpose(self, *args):
        if not self.__Exposed:
            self.__Exposed = 1
        self.render()
        return True

    def onDestroy(self, *args):
        self.hide()
        del self._RenderWindow
        self.destroy()
        return True



    def updateXY(self,x,y):

        windowX,windowY  = self._RenderWindow.GetSize() #self.widget.window.get_size()

        vx,vy = (0,0)
        if (windowX > 1):
            vx = float(x)/(windowX-1)
        if (windowY > 1):
            vy = (windowY-float(y)-1)/(windowY-1)
        (vpxmin,vpymin,vpxmax,vpymax) = self._Renderer.GetViewport()

#         if (vx >= vpxmin and vx <= vpxmax and
#             vy >= vpymin and vy <= vpymax):
#             self._ViewportCenterX = float(windowX)*(vpxmax-vpxmin)/2.0\
#                                     +vpxmin
#             self._ViewportCenterY = float(windowY)*(vpymax-vpymin)/2.0\
#                                     +vpymin

        self._LastX = x
        self._LastY = y



    def mouseTumble(self,x,y):            
        self._Camera.Azimuth(self._LastX - x)
        self._Camera.Elevation(y - self._LastY)
        self._Camera.OrthogonalizeViewUp()

        self._LastX = x
        self._LastY = y


    def mouseTrack(self,x,y):
        
        # if we click on a voxel, we will track that voxel, otherwise
        # we track the focal point.
        clickedVoxel = self.voxelInfo(x,y)
        fPoint = self._Camera.GetFocalPoint()
        if clickedVoxel is not None:
            trackPoint = clickedVoxel
        else:
            trackPoint = fPoint

        # convert track point to display coordinates
        self._Renderer.SetWorldPoint(trackPoint[0],trackPoint[1],trackPoint[2],1.0)
        self._Renderer.WorldToDisplay()
        dPoint = self._Renderer.GetDisplayPoint()

        # add mouse displacement to track point in display coordinates
        aPoint0 = (x - self._LastX)
        aPoint1 = -(y - self._LastY)
        newDPoint = (dPoint[0]+aPoint0,dPoint[1]+aPoint1,dPoint[2])

        #convert newDisplayPoint to world coordinates
        self._Renderer.SetDisplayPoint(newDPoint[0],newDPoint[1],newDPoint[2])
        self._Renderer.DisplayToWorld()
        rPoint = list(self._Renderer.GetWorldPoint())
        if (rPoint[3] != 0.0):
            rPoint[0] = rPoint[0]/rPoint[3]
            rPoint[1] = rPoint[1]/rPoint[3]
            rPoint[2] = rPoint[2]/rPoint[3]

        self._LastX = x
        self._LastY = y

        # track by displacement in display coordinates
        self.track(trackPoint[0] - rPoint[0],
                   trackPoint[1] - rPoint[1],
                   trackPoint[2] - rPoint[2])
           

    def track(self,x,y,z):
        (pPoint0,pPoint1,pPoint2) = self._Camera.GetPosition()
        (fPoint0,fPoint1,fPoint2) = self._Camera.GetFocalPoint()
        self._Camera.SetFocalPoint(x + fPoint0, 
                             y + fPoint1,
                             z + fPoint2) 
                
        self._Camera.SetPosition(x + pPoint0, 
                           y + pPoint1,
                           z + pPoint2)
        


    def mouseDolly(self,x,y):
        dollyFactor = math.pow(1.02,(0.5*(self._LastY - y)))
        self.dolly(dollyFactor)
        self._LastX = x
        self._LastY = y


    def dolly(self,dollyFactor):
        self._Camera.Dolly(dollyFactor)        
        #self.render()

    def dollyfill(self):
        # first, recenter the image
        d = self._Camera.GetDistance()
        dop = self._Camera.GetDirectionOfProjection()
        (dummy, width, dummy, height, dummy, depth) = \
                self._Renderer.ComputeVisiblePropBounds()
        fp = (float(width)/2, float(height)/2, float(depth)/2)
        self._Camera.SetFocalPoint(fp)
        self._Camera.SetPosition(fp[0]-d*dop[0],fp[1]-d*dop[1],fp[2]-d*dop[2])

        # Find the corner that is either closest to or furthest from
        # the viewport edges and dolly such that the width or height
        # of the projection is a 1-2*self.margin the width or height
        # of the viewport. Since this corner is likely not in the
        # focal plane, we must take into account the depth.
        largest = 0
        fraction = 1-2*self.margin
        # one way to do this is to dolly in a loop until we converge
        # on the given fraction, only render after converging
        while math.fabs(largest-fraction) > 1e-3:
            largest = 0
            world_corners = self.getWorldCorners()
            for corner in world_corners:
                self._Renderer.SetWorldPoint(corner[0],corner[1],corner[2],1.0)
                self._Renderer.WorldToView()
                view = self._Renderer.GetViewPoint()
                largest = max(largest, math.fabs(view[0]), math.fabs(view[1]))

            dollyfactor =  fraction/largest

            self._Camera.Dolly(dollyfactor)        


    def reset(self):
        self._Renderer.ResetCamera()           


    def setSampleDistances(self):
        # calculate dimensions of window in voxel units
        angle = float(self._Camera.GetViewAngle())/2*(math.pi/180)
        #TODO: this gives height at focal depth, but really we want
        #the closest point in the image
        height = 2*self._Camera.GetDistance()*math.tan(angle)
        #window_height = self.widget.window.get_size()[1]
        window_height = self._RenderWindow.GetSize()[1]
        sample_distance = min(height/window_height, .2)
        # there should be only one volume, but we do it this way
        # anyway since the renderer can only return a VolumeCollection
        # type, and someday we might want to have more than one volume
        # at a time.  We only need to update the sample distances for
        # the volumes that are currently showing.
        numvolumes = self._Renderer.VisibleVolumeCount()
        volumes = self._Renderer.GetVolumes()
        volumes.InitTraversal()
        for i in xrange(numvolumes):
            volume = volumes.GetNextVolume()
            if volume is not None:
                mapper = volume.GetMapper()
                mapper.SetSampleDistance(sample_distance)
                mapper.SetInteractiveSampleDistance(2*sample_distance)       


    def resetClippingRange(self):
        
        self._Renderer.ResetCameraClippingRange()
        self._ClippingRange = self._Camera.GetClippingRange()
        self.removePlaneActors()
 
    def getClippingRange(self):
        return self._ClippingRange


    def screenCoordsTo3DCoords(self, selectionX, selectionY):
        # We need to use the renderer to convert coordinate systems in
        # order to find which point in the 3D structure, the 2D mouse
        # is pointing to.  We use the bounds of the image (or skeleton
        # or whatever) and the clipping plane to find the topmost
        # visible point.

        bounds = self.getBounds()

        windowY = self._RenderWindow.GetSize()[1] #self.widget.window.get_size()[1]
        selectionY = windowY - selectionY - 1

        pickPosition = [0.0,0.0,0.0]
        point = None

        # get camera focal point and position, convert to display
        # coordinates
        cameraPos = list(self._Camera.GetPosition())
        cameraPos.append(1.0)
        cameraFP = list(self._Camera.GetFocalPoint())
        cameraFP.append(1.0)

        self._Renderer.SetWorldPoint(cameraFP)
        self._Renderer.WorldToDisplay()
        displayCoords = self._Renderer.GetDisplayPoint()
        selectionZ = displayCoords[2]

        # convert selection point into world coordinates
        self._Renderer.SetDisplayPoint(selectionX, selectionY, selectionZ)
        self._Renderer.DisplayToWorld()
        worldCoords = self._Renderer.GetWorldPoint()
        if (worldCoords[3] == 0.0):
            raise PyProgrammingError("Bad homogenous coordinates")
            return None
        for i in xrange(3):
            pickPosition[i] = worldCoords[i]/worldCoords[3]
            
        # compute ray endpoints. The ray is along the line running
        # from the camera position to the selection point, starting where
        # this line intersects the front clipping plane, and terminating
        # where this line intersects the back clipping plane.
        ray = [0.0,0.0,0.0]
        for i in xrange(3):
            ray[i] = pickPosition[i] - cameraPos[i]
        cameraDOP = self._Camera.GetDirectionOfProjection()

        rayLength = cameraDOP[0]*ray[0]+cameraDOP[1]*ray[1]+cameraDOP[2]*ray[2]
        if rayLength == 0.0:
            raise PyProgrammingError("Zero ray length")
            return None

        clipRange = self._Camera.GetClippingRange()

        tF = clipRange[0] / rayLength
        tB = clipRange[1] / rayLength
        p1World = [0.0,0.0,0.0,0.0]
        p2World = [0.0,0.0,0.0,0.0]
        for i in xrange(3):
            p1World[i] = cameraPos[i] + tF*ray[i]
            p2World[i] = cameraPos[i] + tB*ray[i]
        p1World[3] = p2World[3] = 1.0

        # Compute the tolerance in world coordinates.  Do this by
        # determining the world coordinates of the diagonal points of the
        # window, computing the width of the window in world coordinates, and 
        # multiplying by the tolerance.
        viewport = self._Renderer.GetViewport()
        winSize = self._Renderer.GetRenderWindow().GetSize()
        x = winSize[0] + viewport[0]
        y = winSize[1] + viewport[1]
        self._Renderer.SetDisplayPoint(x,y,selectionZ)
        self._Renderer.DisplayToWorld()
        windowLowerLeft = self._Renderer.GetWorldPoint()

        x = winSize[0] + viewport[2]
        y = winSize[1] + viewport[3]
        self._Renderer.SetDisplayPoint(x,y,selectionZ)
        self._Renderer.DisplayToWorld()
        windowUpperRight = self._Renderer.GetWorldPoint()

        tol = 0.0
        for i in xrange(3):
            tol += (windowUpperRight[i] - windowLowerLeft[i]) * \
                (windowUpperRight[i] - windowLowerLeft[i])

        tol = math.sqrt(tol) * 0.025 #self.tol # TODO 3D: set sensible tolerance

        # end of stuff that was basically copied from vtkPicker::Pick

        # at this point, p1World is the point (in world coordinates)
        # where the ray intersects the first clipping plane, p2Worls
        # is where the ray intersects the back clipping plane.  tol is
        # the tolerance in world coordinates.

        # we want the point indices and/or point id of the
        # voxel that 1. intersects the ray 2. is in the front
        # 3. is within the bounds of the skeleton

        # simple strategy, increment along the ray by the
        # tolerance until we find a point that is within the
        # given bounds.

        # If we don't find something in the given bounds, then we
        # return the point on the near clipping plane

        currentPoint = p1World[0:3]
        lengthTraversed = 0.0
        rayInClippingRange = [p2World[0]-p1World[0], p2World[1]-p1World[1], p2World[2]-p1World[2]]
        rayInCRLength = math.sqrt(rayInClippingRange[0]**2+rayInClippingRange[1]**2+
                                  rayInClippingRange[2]**2)
        direction = [rayInClippingRange[0]/rayInCRLength, rayInClippingRange[1]/rayInCRLength, 
                     rayInClippingRange[2]/rayInCRLength]
        inc = (direction[0]*tol,direction[1]*tol,direction[2]*tol)
        while (lengthTraversed <= rayInCRLength and point is None):
            if currentPoint[0] >= bounds[0] and currentPoint[0] <= bounds[1] and \
                    currentPoint[1] >= bounds[2] and currentPoint[1] <= bounds[3] and \
                    currentPoint[2] >= bounds[4] and currentPoint[2] <= bounds[5]:
                point = primitives.Point(currentPoint[0],
                                            currentPoint[1],
                                            currentPoint[2])
            currentPoint = [currentPoint[0]+inc[0],currentPoint[1]+inc[1],currentPoint[2]+inc[2]]
            lengthTraversed += tol

        if point is None:
            point = primitives.Point(p1World[0],p1World[1],p1World[2])
        return point


    def voxelInfo(self,x,y):
        # TODO 3D: get rid of voxel picker...
        picker = self._Picker

        windowY = self._RenderWindow.GetSize()[1] #self.widget.window.get_size()[1]
        foundVox = picker.Pick(x,(windowY - y - 1),0.0,self._Renderer)

        if foundVox:
            pointid = picker.GetPointId()
            voxelPoint = picker.GetPickedVoxel()

            return voxelPoint


     # Clipping Plane
    ###############################################################

    def calculateclipping(self, percent):

        if percent != 100:
            # figure out the distance from the camera to the nearest
            # corner and the furthest corner
            self.removePlaneActors()
            world_corners = self.getWorldCorners()
            cp = self._Camera.GetPosition()
            camera_position = primitives.Point(cp[0],cp[1],cp[2])
            p = self._Camera.GetDirectionOfProjection()
            projection = primitives.Point(p[0],p[1],p[2])
            near = self._Camera.GetDistance()*1e20
            far = 0
            for corner in world_corners:
                # calculate distance along direction of projection to corner
                dist = projection*(corner-camera_position)
                if dist < near:
                    near = dist
                if dist > far:
                    far = dist
            newnear = far - (far-near)*(percent/100)
            self._Camera.SetClippingRange(newnear,far)
            #self.cutGrid(projection,camera_position+(1+1e-5)*newnear*projection)
        else:
            self.resetClippingRange()

        self.clip = percent

# vtk wants to triangulate every surface when it cuts.  We just want
# the outlines of the cells.  TODO: Dig into vtk code and re-write if
# necessary to do What We Want.  Also, need to make this work better
# with layers such that the outline is drawn if the poly object is
# drawn when the volume is already clipped.

#     def cutGrid(self, normal, origin):
#         plane = vtk.vtkPlane()
#         plane.SetNormal(normal.x,normal.y,normal.z)
#         plane.SetOrigin(origin.x,origin.y,origin.z)
#         cutter = vtk.vtkCutter()
#         cutter.SetCutFunction(plane)
#         for layer in self.layers:
#             if layer.grid is not None:
#                 grid = layer.grid
#                 print grid
#                 color = layer.polyActor.GetProperty().GetColor()
#                 lineWidth = layer.polyActor.GetProperty().GetLineWidth()
#                 scalarmode = layer.polyActor.GetMapper().GetScalarMode()
#                 lut = layer.polyActor.GetMapper().GetLookupTable()
#                 representation = layer.polyActor.GetProperty().GetRepresentation()
                
#                 cutter.SetInput(grid)
#                 planePoly = cutter.GetOutput()
#                 cutter.Update()
#                 planeMapper = vtk.vtkPolyDataMapper()
#                 planeMapper.SetInput(planePoly)
#                 planeMapper.SetScalarMode(scalarmode)
#                 planeMapper.SetLookupTable(lut)
#                 planeActor = vtk.vtkActor()
#                 planeActor.SetMapper(planeMapper)
#                 planeActor.GetProperty().SetRepresentation(representation)
#                 #planeActor.GetProperty().SetColor(color)
#                 #planeActor.GetProperty().SetLineWidth(lineWidth)
#                 #planeActor.GetProperty().SetLineStipplePattern(31)
#                 #planeActor.GetProperty().SetLineStippleRepeatFactor(1)
#                 self.planeActors.append(planeActor)


    def removePlaneActors(self):
        for actor in self.planeActors:
            self._Renderer.RemoveActor(actor)
        self.planeActors = []
       

    def getWorldCorners(self):
        # get the corners of the visible props in world coordinates
        bounds = self._Renderer.ComputeVisiblePropBounds()
        return [primitives.Point(bounds[0],bounds[2],bounds[4]),
                primitives.Point(bounds[0],bounds[2],bounds[5]),
                primitives.Point(bounds[0],bounds[3],bounds[4]),
                primitives.Point(bounds[0],bounds[3],bounds[5]),
                primitives.Point(bounds[1],bounds[2],bounds[4]),
                primitives.Point(bounds[1],bounds[2],bounds[5]),
                primitives.Point(bounds[1],bounds[3],bounds[4]),
                primitives.Point(bounds[1],bounds[3],bounds[5])]

    def getBounds(self):
        return self._Renderer.ComputeVisiblePropBounds()
     
    def set_rubberband(self, rb):
        self.rubberband = rb;
                
    # This must be called within a mainthread.runBlock
    def saveImageThreaded(self, filename):
        w2i = vtk.vtkWindowToImageFilter()
        writer = vtk.vtkTIFFWriter()
        w2i.SetInput(self._RenderWindow)
        w2i.Update()
        writer.SetInputConnection(w2i.GetOutputPort())
        writer.SetFileName(filename)
        self._RenderWindow.Render()
        writer.Write()













