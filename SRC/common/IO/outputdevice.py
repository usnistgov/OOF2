# -*- python -*-
# $RCSfile: outputdevice.py,v $
# $Revision: 1.49 $
# $Author: langer $
# $Date: 2014/09/27 21:40:31 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 



## The OutputDevice class (as of now) doesn't do much except provide
## stubs for all of the output primitives.  The derived classes have
## to override these methods, of course.  The stubs raise exceptions,
## so if a particular device doesn't support a particular operation,
## the program can tell the user that he or she is trying to do
## something impossible.

## Some of the primitive functions have implementations here, when
## they can be defined in terms of simpler primitives.  They should be
## overridden in derived classes if the derived class can define them
## more efficiently.

from ooflib.common import mainthread
from ooflib.common import subthread
from ooflib.common import debug
from ooflib.common import color
from ooflib.common.IO import colormap
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import lock

class OutputDevice:
    def __init__(self):
        self.colormap = colormap.GrayMap

    def unsupported(self, op):
        raise UnsupportedOperation(self.__class__.__name__, op)

    def has_alpha(self):                # is transparency supported?
        return False
    
    def clear(self):
        self.unsupported("clear")

    def show(self):
        self.unsupported("show")


    def set_lineWidth(self, w):
        "set_lineWidth(w):  w in units determined by boundingBox"
        self.unsupported("set_lineWidth")

    def set_glyphSize(self, x):
        self.unsupported("set_glyphSize")

    def set_lineColor(self, x):
        """
        should accept two forms:
        set_lineColor(x):  0 <= x <= 1, color determined by colormap
        set_lineColor(Color)
        """
        self.unsupported("set_lineColor")

    def set_fillColor(self, x):
        """
        should accept two forms:
        set_fillColor(x):  0 <= x <= 1, color determined by colormap
        set_fillColor(Color)
        """
        self.unsupported("set_fillColor")

    def set_fillColorAlpha(self, x, a):
        self.unsupported("set_fillColorAlpha")

    def set_colormap(self, colormap):
        """
        set_colormap(map)
        map is a function or callable object which
        maps the interval [0,1] to a Color object.
        """
        self.colormap = colormap


    def draw_segment(self, segment):
        self.unsupported("draw_segment")

    def draw_segments(self, seglist):
        for seg in seglist:
            self.draw_segment(seg)

    def draw_curve(self, curve):
        # Drawing a curve by drawing segments is inefficient, since it
        # addresses each point twice.
        self.draw_segments(curve.edges())

    def draw_dot(self, dot):
        self.unsupported("draw_dot")

    def draw_triangle(self, segment, angle):
        self.unsupported("draw_triangle")

    def draw_polygon(self, polygon):
        if type(polygon) == ListType:
            for pgon in polygon:
                self.draw_segments(pgon.edges())
        else:
            self.draw_segments(polygon.edges())

    def draw_cone_glyphs(self, polydata):
        self.unsupported("draw_cone_glyphs")

    def draw_unstructuredgrid(self, polyhedra):
        self.unsupported("draw_unstructuredgrid")

    def draw_filled_unstructuredgrid(self, grid):
        self.unsupported("draw_filled_unstructuredgrid")

    def draw_unstructuredgrid_with_lookuptable(self, grid, lookuptable, mode, scalarbar):
        self.unsupported("draw_unstructuredgrid_with_lookuptable")

    def fill_polygon(self, polygon):
        self.unsupported("fill_polygon")

    def draw_circle(self, center, radius):
        self.unsupported("draw_circle")

    def fill_circle(self, center, radius):
        self.unsupported("fill_circle")

    def draw_image(self, image, offset, size):
        # image must have a method 'sizeInPixels()' which returns the
        # size in pixels as a tuple of ints and a method
        # 'stringimage()' which returns a string of the form expected
        # by GdkImlibImage.  The 'size' argument to draw_image is
        # (width, height) in physical units.
        self.unsupported("draw_image")

    def draw_shaped_image(self, image, offset, size, shapecolor):
        # Just like draw_image, but pixels whose color is shapecolor
        # aren't drawn.
        self.unsupported("draw_shaped_image")

    def draw_alpha_image(self, image, offset, size):
        # image must have a method alphastringimage(alpha)
        self.unsupported("draw_alpha_image")

    def set_font(self, font):
        self.unsupported("set_font")

    def set_fontsize(self, size):
        self.unsupported("set_fontsize")

    def draw_label(self, position, text):
        self.unsupported("draw_label")

    def comment(self, remark):
        pass

    def purge(self):
        pass

    def begin_layer(self): 
        return NullLayer()

    def end_layer(self): 
        pass

    def flush(self):
        pass

    def destroy(self):
        pass

class UnsupportedOperation(ooferror.ErrError):
    def __init__(self, devname, op):
        self.devname = devname
        self.opname = op
    def __repr__(self):
        return "Operation %s not available on output device." % self.opname

##########################################################

class NullDevice(OutputDevice):
    def clear(self): pass
    def unsupported(x): pass
    def show(self): pass
    def set_lineWidth(self, w): pass
    def set_glyphSize(self, x): pass
    def set_lineColor(self, x): pass
    def set_fillColor(self, x): pass
    def set_fillColorAlpha(self, x, a): pass
    def set_colormap(self, colormap): pass
    def draw_segment(self, segment): pass
    def draw_segments(self, seglist): pass
    def draw_curve(self, curve): pass
    def draw_polygon(self, polygon): pass
    def draw_cone_glyphs(self, polydata): pass
    def draw_unstructuredgrid(self, polyhedra): pass
    def draw_filled_unstructuredgrid(self, grid): pass
    def draw_unstructuredgrid_with_lookuptable(self, grid, lookuptable, mode, scalarbar): pass
    def fill_polygon(self, polygon): pass
    def draw_circle(self, center, radius): pass
    def fill_circle(self, center, radius): pass
    def draw_image(self, image, offset, size): pass
    def draw_alpha_image(self, *args): pass
    def draw_shaped_image(self, *args): pass
    def draw_dot(self, dot): pass
    def draw_triangle(self, segment, angle): pass
    def set_font(self, font): pass
    def set_fontsize(self, size): pass
    def draw_label(self, position, text): pass
    def comment(self, remark): pass
    def end_layer(self): pass
    def set_background(self, *args): pass

class NullLayer:
    def __init__(self):
        self.hidden = False
    def hide(self):
        self.hidden = True
    def show(self):
        self.hidden = False
    def clear(self):
        pass
    def make_current(self):
        pass
    def raise_layer(self, howfar=1):
        pass
    def raise_to_top(self):
        pass
    def lower_layer(self, howfar=1):
        pass

###############################################################
    
BUFSIZE = 50000 ## Size of buffer of DeviceBuffer

##
## The DeviceBuffer class accumulates a list of commands that will be
## executed in the main thread. These commands are gtk calls that will
## not and should not be executed on any child thread.
##
##  The list is flushed when it has reached a maximum size.
##

class DeviceBuffer:
    def __init__(self):
        self.buf = []                   ## list of stored commands
        self.destroyflag = False        # buffer has been destroyed
        self.lock = lock.SLock()

    def __len__(self):
        return len(self.buf)
        
    def set_destroyflag(self):
        # This function is called by an external thread.  The thread
        # that's adding commands to the buffer checks destroyflag as
        # it adds commands, and aborts itself if the flag is set.
        self.destroyflag = True
        
    def append(self, cmd, *args):
        ## adds a command and its arguments to the list
        if self.destroyflag:
            self.purge()
            if not mainthread.mainthread():
                raise subthread.StopThread
        self.lock.acquire()
        self.buf.append((cmd, args))
        self.lock.release()
        if len(self.buf) > BUFSIZE:
            self.flush()
    def purge(self):
        self.lock.acquire()
        self.buf = []
        self.lock.release()
        
    def flush(self): ## sends list of commands to main thread
        if not self.destroyflag:
            mainthread.run(self.executeBuffer) # not blocking!
        else:
            self.purge()

    def flush_wait(self): # Blocking version of flush.
        if not self.destroyflag:
            mainthread.runBlock(self.executeBuffer) # Blocking!
        else:
            self.purge()
        
    def executeBuffer(self):
        # This runs only on the main thread, because it performs GUI
        # operations on the canvas in the usual case.
        self.lock.acquire()
        bufref = self.buf
        self.buf = []
        self.lock.release()
        for (func, args) in bufref:
            if self.destroyflag:
                return
            func(*args)

## Untested cute way to avoid reproducing OutputDevice functions in
## the BufferedOutputDevice class.  It's probably too much of a
## performance hit.
        
##class BODproxy:
##    def __init__(self, buffereddevice, name):
##        self.name = name
##        self.buffereddevice = buffereddevice
##    def __call__(self, *args):
##        self.buffereddevice.buffer.append(
##            getattr(self.buffereddevice.device, self.name), *args)

##
## The BufferedOutputDevice delays the execution of the OutputDevice
## commands by sending the device's commands to a DeviceBuffer (see above),
## where they will be stored until the maximum buffer size is reached.
## The buffer is executed in the main thread. 
##


class BufferedOutputDevice (OutputDevice):
    def __init__(self, device):
        self.device = device
        self.buffer = DeviceBuffer()

##    def __getattr__(self, name):
##        return BODproxy(self, name)
        
    def has_alpha(self):
        return self.device.has_alpha()
        
    def clear(self):
        self.buffer.append(self.device.clear)

    def show(self):
        self.buffer.append(self.device.show)
        self.buffer.flush()

    def set_lineWidth(self, w):
        self.buffer.append(self.device.set_lineWidth, w)

    def set_glyphSize(self, x):
        self.buffer.append(self.device.set_glyphSize, x)

    def set_lineColor(self,x):
        self.buffer.append(self.device.set_lineColor, x)

    def set_fillColor(self,x):
        self.buffer.append(self.device.set_fillColor, x)

    def set_fillColorAlpha(self, x, a):
        self.buffer.append(self.device.set_fillColorAlpha, x, a)

    def set_colormap(self,colormap):
        self.buffer.append(self.device.set_colormap, colormap)

    def draw_segment(self,segment):
        self.buffer.append(self.device.draw_segment, segment)
        
    def draw_segments(self, seglist):
        self.buffer.append(self.device.draw_segments, seglist)

    def draw_curve(self, curve):
        self.buffer.append(self.device.draw_curve, curve)

    def draw_polygon(self, polygon):
        self.buffer.append(self.device.draw_polygon, polygon)
    
    def draw_cone_glyphs(self, polydata):
        self.buffer.append(self.device.draw_cone_glyphs, polydata)

    def draw_unstructuredgrid(self, polyhedra):
        self.buffer.append(self.device.draw_unstructuredgrid, polyhedra)

    def draw_filled_unstructuredgrid(self, grid):
        self.buffer.append(self.device.draw_filled_unstructuredgrid, grid)

    def draw_unstructuredgrid_with_lookuptable(self, grid, lookuptable, mode="cell", scalarbar="true"):
        self.buffer.append(self.device.draw_unstructuredgrid_with_lookuptable, grid, lookuptable, mode, scalarbar)

    def fill_polygon(self, polygon):
        self.buffer.append(self.device.fill_polygon, polygon)

    def draw_dot(self, dot):
        self.buffer.append(self.device.draw_dot, dot)

    def draw_scalarbar(self, lookuptable):
        self.buffer.append(self.device.draw_scalarbar, lookuptable)

    def draw_voxel(self, voxel):
        self.buffer.append(self.device.draw_voxel, voxel)

    def draw_cell(self, cell, filled=False):
        self.buffer.append(self.device.draw_cell, cell, filled)

    def draw_triangle(self, segment, angle):
        self.buffer.append(self.device.draw_triangle, segment, angle)

    def draw_circle(self, center, radius):
        self.buffer.append(self.device.draw_circle, center, radius)

    def fill_circle(self, center, radius):
        self.buffer.append(self.device.fill_circle, center, radius)

    def draw_image(self, image, offset, size):
        self.buffer.append(self.device.draw_image, image, offset, size)

    def draw_alpha_image(self, image, offset, size):
        self.buffer.append(self.device.draw_alpha_image, image, offset, size)

    def draw_shaped_image(self, image, offset, size, shapecolor):
        self.buffer.append(self.device.draw_shaped_image, image, offset,
                           size, shapecolor)

    def set_font(self, font):
        self.buffer.append(self.device.set_font, font)

    def set_fontsize(self, size):
        self.buffer.append(self.device.set_fontsize, size)

    def draw_label(self, position, text):
        self.buffer.append(device.draw_label, position, text)
        
    def comment(self, remark):
        self.buffer.append(self.device.comment, remark)

    def begin_layer(self):
        return BufferedOOFCanvasLayer(self)

    def end_layer(self):
        self.buffer.append(self.device.end_layer)

    def flush(self):
        self.buffer.flush()

    def flush_wait(self):
        self.buffer.flush_wait()
        
    def destroy(self):
        self.buffer.set_destroyflag()

##
## BufferedOOFCanvasLayer also delays the execution of an OOFCanvasLayer
## command for those calls from the canvas that are meant to be executed
## in the main thread. Some calls need to be executed right away. For this
## case, the command is put in the buffer and the buffer is immediately
## flushed.
##

class BufferedOOFCanvasLayer:
    def __init__ (self, buffereddevice):
        self.layer = None
        self.buffer = buffereddevice.buffer
        self.device = buffereddevice.device
        self.buffer.append(self.really_begin)
    def really_begin(self):
        self.layer = self.device.begin_layer()

    def raise_layer(self, x):
        self.buffer.append(self.really_raise_layer, x)
    def really_raise_layer(self,x):
        self.layer.raise_layer(x)
        
    def raise_to_top(self):
        self.buffer.append(self.really_raise_to_top)
    def really_raise_to_top(self):
        self.layer.raise_to_top()
        
    def lower_layer(self, layer):
        self.buffer.append(self.really_lower_layer, layer)
    def really_lower_layer(self, layer):
        self.layer.lower_layer(layer)
        
    def show(self):
        self.buffer.append(self.really_show)
    def really_show(self):
        self.layer.show()
        
    def hide(self):
        self.buffer.append(self.really_hide)
    def really_hide(self):
        self.layer.hide()
        
    def clear(self):
        self.buffer.append(self.really_clear)
    def really_clear(self):
        self.layer.clear()

    def make_current(self):
        self.buffer.append(self.really_make_current)
    def really_make_current(self):
        self.layer.make_current()
        
    def destroy(self):
        self.buffer.append(self.really_destroy)
    def really_destroy(self):
        self.layer.destroy()

