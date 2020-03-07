# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

## TODO GTK3: Rewrite this to use the Cairo based OOFCanvas.  Then
## after all of OOF2 is converted to gtk3, remove the OutputDevice
## class hierarchy, and have the DisplayMethods all use OOFCanvas
## directly.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import coord
from ooflib.SWIG.common import ooferror
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import thread_enable
from ooflib.common.IO import colormap
from ooflib.common.IO import outputdevice
from ooflib.common.IO.GUI import gfxwindow
from ooflib.common.IO.GUI import oof_mainiteration
from ooflib.common.IO.OOFCanvas import oofcanvas
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
        self.canvas = canvas  # OOFCanvas object
        outputdevice.OutputDevice.__init__(self)
        self.lineColor = None
        self.lineWidth = None
        self.fillColor = None
        self.opacity = 1.0
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
        self.currentlayer = self.canvas.newLayer("Layer_%d" % self.nLayers)
        #self.currentlayer.index = self.nLayers
        self.nLayers += 1
        return self.currentlayer

    def end_layer(self):
        self.currentlayer = None

    def set_lineWidth(self, w):         # Set linewidth in pixels
        self.lineWidth = w
        
    def set_lineColor(self, x):
        if type(x) is types.FloatType:
            col = self.colormap(x)
        else:
            col = x
        self.lineColor = \
            oofcanvas.Color(col.red(), col.green(), col.blue()).opacity(1.0)

    def set_fillColor(self, x):
        if type(x) == type(1.0):
            col = self.colormap(x)
        else:
            col = x
        self.fillColor = \
            oofcanvas.Color(col.red(), col.green(), col.blue()).opacity(1.0)

    def set_fillColorAlpha(self, x, alpha):
        if type(x) == type(1.0):
            col = self.colormap(x)
        else:
            col = x
        self.fillColor = \
            oofcanvas.Color(col.red(), col.green(), col.blue()).opacity(alpha)
        
    def draw_segment(self, segment):
        seg = oofcanvas.CanvasSegment(segment.startpt.x, segment.startpt.y,
                                      segment.endpt.x, segment.endpt.y)
        seg.setLineWidth(self.lineWidth)
        seg.setLineColor(self.lineColor)
        self.currentLayer.addItem(seg)
        return seg

    def draw_dot(self, dot):
        ## draw_dot's callers use the old set_lineWidth to set the
        ## dot's size, for unknowns reasons.  Fix this when removing
        ## the OutputDevice classes.
        dot = oofcanvas.CanvasDot(dot.x, dot.y, self.lineWidth)
        dot.setFillColor(self.fillColor)
        self.currentLayer.addItem(dot)
        return dot

    def draw_triangle(self, segment, relativePos):
        triangle = oofcanvas.CanvasArrowhead(segment, relativePos,
                                             self.lineWidth, self.lineWidth)
        triangle.setFillColor(self.fillColor)
        self.currentLayer.addItem(triangle)
        return triangle
        
    def draw_curve(self, curve):
        # curve is a primitives.Curve
        assert self.lineColor is not None
        segs = oofcanvas.CanvasSegments()
        for edge in curve.edges():
            segs.addSegment(edge.startpt.x, edge.startpt.y,
                            edge.endpt.x, edge.endpt.y)
        segs.setLineColor(self.lineColor)
        segs.setLineWidth(self.lineWidth)
        self.currentLayer.addItem(segs)
        return segs
        
    def draw_polygon(self, polygon):
        # polygon is a primitives.Polygon or a list of them
        assert self.lineColor is not None
        self.fillColor = None
        if type(polygon) == types.ListType:
            return [self._draw_one_polygon(p, False) for p in polygon]
        else:
            return self._draw_one_polygon(polygon, False)

    def fill_polygon(self, polygon):
        assert self.fillColor is not None
        self.lineColor = None
        if type(polygon) == types.ListType:
            poly = self.makeCompoundPolygon(polygon)
            return self._draw_one_polygon(poly, True)
        else:
            return self._draw_one_polygon(polygon, True)

    def _draw_one_polygon(self, polygon, filled):
        poly = oofcanvas.CanvasPolygon()
        for pt in polygon.points():
            poly.addPoint(pt.x, pt.y)
        if self.lineColor:
            poly.setLineColor(self.lineColor)
        if filled and self.fillColor:
            poly.setFillColor(self.fillColor)
        self.currentLayer.addItem(poly)
        return poly

    def draw_circle(self, center, radius):
        assert self.lineColor is not None
        circle = oofcanvas.CanvasCircle(center.x, center.y, radius)
        circle.setLineColor(self.lineColor)
        self.currentLayer.addItem(circle)
        return circle
        
    def fill_circle(self, center, radius):
        assert self.fillColor is not None
        circle = oofcanvas.CanvasCircle(center.x, center.y, radius)
        circle.setFillColor(self.fillColor)
        self.currentLayer.addItem(circle)
        return circle

    def draw_image(self, image, offset, size, alpha=1.0):
        img = image.makeCanvasImage(offset, size)
        img.setOpacity(alpha)
        self.currentLayer.addItem(img)
        return img

    # def draw_alpha_image(self, image, offset, size):
    #     # self.canvas.draw_alpha_image(image, offset, size)
    #     img = self.draw_image(image, offset, size)
        
    def comment(self, remark):
        pass



