# -*- python -*-
# $RCSfile: canvasoutput.py,v $
# $Revision: 1.57 $
# $Author: langer $
# $Date: 2014/12/31 01:32:23 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import coord
from ooflib.SWIG.common import ooferror
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import thread_enable
from ooflib.common.IO import colormap
from ooflib.common.IO import outputdevice
if config.dimension() == 2: 
    from ooflib.common.IO.GUI import gfxwindow
elif config.dimension() == 3:
    from ooflib.common.IO.GUI import gfxwindow3d as gfxwindow
from ooflib.common.IO.GUI import oof_mainiteration
import types

import time, sys

def point2Coord(point):
    "Convert a Point (pure Python) to Coord (swigged C++)"
    return coord.Coord(point[0], point[1])

# def seg2CSeg(segment):
#     "Convert a Segment (pure Python) to a CSegment (swigged C++)"
#     return CSegment(point2Coord(segment.startpt), point2Coord(segment.endpt))


class CanvasOutput(outputdevice.OutputDevice):
    def __init__(self, canvas):
        self.canvas = canvas  # OOFCanvas object, C++ wrapper for GtkCanvas
        outputdevice.OutputDevice.__init__(self)

        self.set_lineColor(color.black)
        self.set_fillColor(color.black)
        self.colormap = colormap.GrayMap()
        self.nLayers = 0

        self.currentlayer = None        # OOFCanvasLayer object

    def has_alpha(self):
        return True;
    
    def clear(self):
        debug.mainthreadTest()
        self.canvas.clear()

    def show(self):
        debug.mainthreadTest()
        self.canvas.show()
        # Displays which want to show animations will be calling
        # show() many times in one gtk main loop pass.  The display
        # doesn't actually get updated unless events are processed, so
        # we have to call mainiteration() here.  This has the
        # unfortunate side effect of allowing all sorts of button
        # clicks and other user events, so we should be careful to
        # disable the GUI when the program is busy.  Also, calling
        # mainiteration() appears to be a no-no during mouse event
        # callbacks, so we check for that here as well.
        if not thread_enable.query():
            if not gfxwindow.during_callback():
                oof_mainiteration.mainiteration_loop(False)
            
    def begin_layer(self):
        debug.mainthreadTest()
        self.currentlayer = self.canvas.newLayer()
        self.currentlayer.index = self.nLayers
        self.nLayers += 1
        return self.currentlayer

    def end_layer(self):
        self.currentlayer = None

    def set_lineWidth(self, w):         # Set linewidth in pixels
        debug.mainthreadTest()
        self.canvas.set_lineWidth(w)
        
    def set_lineColor(self, x):
        debug.mainthreadTest()
        if type(x) is types.FloatType:
            self.canvas.set_lineColor(self.colormap(x))
        else:
            self.canvas.set_lineColor(x)

    def set_glyphSize(self, x):
        debug.mainthreadTest()
        self.canvas.set_glyphSize(x)
        
    def set_fillColor(self, x):
        debug.mainthreadTest()
        if type(x) == type(1.0):
            self.canvas.set_fillColor(self.colormap(x), 255)
        else:
            self.canvas.set_fillColor(x, 255)

    def set_fillColorAlpha(self, x, alpha):
        debug.mainthreadTest()
        if type(x) == type(1.0):
            self.canvas.set_fillColor(self.colormap(x), alpha)
        else:
            self.canvas.set_fillColor(x, alpha)
        
    def draw_segment(self, segment):
        debug.mainthreadTest()
        self.canvas.draw_segment(segment)

    def draw_dot(self, dot):
        debug.mainthreadTest()
        self.canvas.draw_dot(dot)

    def draw_scalarbar(self, lookuptable):
        debug.mainthreadTest()
        self.canvas.draw_scalarbar(lookuptable)

    def draw_voxel(self, voxel):
        debug.mainthreadTest()
        self.canvas.draw_voxel(voxel)

    def draw_cell(self, cell, filled=False):
        debug.mainthreadTest()
        self.canvas.draw_cell(cell, filled)

    def draw_triangle(self, segment, angle):
        debug.mainthreadTest()
        self.canvas.draw_triangle(segment, angle)
        
    # This function is currently not called, the contouring routines
    # use "draw_curve", and the segment drawers draw segments one at a
    # time.
    def draw_segments(self, seglist):
        debug.mainthreadTest()
        self.canvas.draw_segments(seglist)

    def draw_curve(self, curve):
        debug.mainthreadTest()
        self.canvas.draw_curve(curve)
        
    def draw_polygon(self, polygon):
        debug.mainthreadTest()
        if type(polygon) == types.ListType:
            for pgon in polygon:
                self.canvas.draw_polygon(pgon)
        else:
            self.canvas.draw_polygon(polygon)

    def draw_cone_glyphs(self, polydata):
        debug.mainthreadTest()
        self.canvas.draw_cone_glyphs(polydata)

    def draw_unstructuredgrid(self, polyhedra):
        debug.mainthreadTest()
        self.canvas.draw_unstructuredgrid(polyhedra)

    def draw_unstructuredgrid_with_lookuptable(self, grid, lookuptable, mode="cell", scalarbar=True):
        debug.mainthreadTest()
        self.canvas.draw_unstructuredgrid_with_lookuptable(grid, lookuptable, mode, scalarbar)

    def draw_filled_unstructuredgrid(self, grid):
        debug.mainthreadTest()
        self.canvas.draw_filled_unstructuredgrid(grid)

    def fill_polygon(self, polygon):
        debug.mainthreadTest()
        if type(polygon) == types.ListType:
            p = primitives.makeCompoundPolygon(polygon)
            self.canvas.fill_polygon(p)
        else:
            self.canvas.fill_polygon(polygon)

    def draw_circle(self, center, radius):
        debug.mainthreadTest()
        self.canvas.draw_circle(point2Coord(center), radius)
        
    def fill_circle(self, center, radius):
        debug.mainthreadTest()
        self.canvas.fill_circle(point2Coord(center), radius)

    def draw_image(self, image, offset, size):
        debug.mainthreadTest()
        self.canvas.draw_image(image, offset, size)

    def draw_alpha_image(self, image, offset, size):
        debug.mainthreadTest()
        self.canvas.draw_alpha_image(image, offset, size)
        

    def comment(self, remark): pass



