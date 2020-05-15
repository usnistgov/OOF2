# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common.IO.OOFCANVAS import oofcanvas
from ooflib.SWIG.common import config
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import display
from ooflib.common.IO import ghostgfxwindow
from ooflib.common.IO import gfxmanager
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import skeletonboundary
import math
import string

# Special parameter class for skeleton boundaries.  Returns a
# list of strings corresponding to the names of boundaries in a
# given skeleton.  The custom class is primarily to allow for a
# special skeleton-smart widget.

class SkeletonBoundaryListParameter(parameter.ListOfStringsParameter):
    pass


# Layer for showing the boundaries (point and edge) of a skeleton.
class SkeletonBoundaryDisplay(display.DisplayMethod):
    def __init__(self, boundaries, color, linewidth, dotsize, arrowsize):
        self.boundaries = boundaries
        self.color = color
        self.linewidth = linewidth
        self.dotsize = dotsize
        self.arrowsize = arrowsize
        display.DisplayMethod.__init__(self)

    def draw(self, gfxwindow, canvaslayer):
        skel = self.who.resolve(gfxwindow)
        skelobj = skel.getObject()
        clr = color.canvasColor(self.color)
        for k in self.boundaries:
            try:
                b = skelobj.edgeboundaries[k]
            except KeyError:
                pass
            else:
                for e in b.edges:
                    nodes = e.get_nodes()
                    pt0 = nodes[0].position()
                    pt1 = nodes[1].position()
                    seg = oofcanvas.CanvasSegment(pt0.x, pt0.y, pt1.x, pt1.y)
                    seg.setLineWidth(self.linewidth)
                    seg.setLineWidthInPixels()
                    seg.setLineColor(clr)
                    arrow = oofcanvas.CanvasArrowhead(
                        seg, 0.5, 0.7*self.arrowsize, self.arrowsize, False)
                    canvaslayer.addItem(seg)
                    canvaslayer.addItem(arrow)

        for k in self.boundaries:
            try:
                b = skelobj.pointboundaries[k]
            except KeyError:
                pass
            else:
                for n in b.nodes:
                    dot = oofcanvas.CanvasDot(n.position().x, n.position().y,
                                              self.dotsize)
                    dot.setFillColor(clr)
                    canvaslayer.addItem(dot)

    def getTimeStamp(self, gfxwindow):
        return max( self.timestamp,
                    self.who.resolve(gfxwindow).bdytimestamp )

widthRange = (0,10)
                    
skeletonBoundaryDisplay = registeredclass.Registration(
    'Boundaries', display.DisplayMethod,
    SkeletonBoundaryDisplay,
    params=[SkeletonBoundaryListParameter('boundaries', [],
                                      tip="Boundaries to display."),
            color.ColorParameter('color', value=color.gray50,
                                 tip="Color for the displayed boundaries."),
            parameter.IntRangeParameter('linewidth', widthRange, 3,
                                        tip="Line width for edge boundaries."),
            parameter.IntRangeParameter('dotsize', widthRange, 4,
                                        tip="Dot radius for point boundaries."),
            parameter.IntRangeParameter('arrowsize', (0, 30), 15,
                                        tip="Arrow size for edge boundaries.")],
    ordering=1.0,
    layerordering=display.SemiLinear(2),
    whoclasses=('Skeleton',),
    tip="Display some or all of the boundaries of the Skeleton",
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/skeletonbdydisplay.xml')
    )

# Layer for showing the selected boundary (point and edge) of a skeleton.

class SelectedSkeletonBoundaryDisplay(display.DisplayMethod):
    def __init__(self, color, linewidth, dotsize, arrowsize):
        self.color = color
        self.linewidth = linewidth
        self.dotsize = dotsize
        self.arrowsize = arrowsize
        display.DisplayMethod.__init__(self)
        
    def draw(self, gfxwindow, canvaslayer):
        skel = self.who.resolve(gfxwindow)
        skelobj = skel.getObject()
        bdy = skel.getSelectedBoundary()  # SkelContextBoundary
        if bdy is not None:
            # bdy.draw calls either drawEdgeBoundary or drawPointBoundary
            bdy.draw(self, canvaslayer, skelobj)

    def drawEdgeBoundary(self, bdy, skelobj, canvaslayer):
        b = bdy.boundary(skelobj)
        clr = color.canvasColor(self.color)
        for e in b.edges:
            nodes = e.get_nodes()
            n0 = nodes[0].position()
            n1 = nodes[1].position()
            seg = oofcanvas.CanvasSegment(n0.x, n0.y, n1.x, n1.y)
            seg.setLineColor(clr)
            seg.setLineWidth(self.linewidth)
            seg.setLineWidthInPixels()
            arrow = oofcanvas.CanvasArrowhead(seg, 0.5, 0.7*self.arrowsize,
                                              self.arrowsize, False)
            arrow.setPixelSize()
            canvaslayer.addItem(seg)
            canvaslayer.addItem(arrow)

    def drawPointBoundary(self, bdy, skelobj, canvaslayer):
        b = bdy.boundary(skelobj)
        clr = color.canvasColor(self.color)
        for n in b.nodes:
            dot = oofcanvas.CanvasDot(n.position().x, n.position().y,
                                      self.dotsize)
            dot.setFillColor(clr)
            canvaslayer.addItem(dot)
    
    def getTimeStamp(self, gfxwindow):
        skelcontext = self.who.resolve(gfxwindow)
        bdy = skelcontext.getSelectedBoundary()
        if bdy is not None:
            return max(self.timestamp, skelcontext.bdyselected,
                       skelcontext.getSelectedBoundary().timestamp)
        return max(self.timestamp, skelcontext.bdyselected)

defaultSelSkelBdyColor = color.orange
defaultSelSkelBdyLineWidth = 4
defaultSelSkelBdyDotSize = 4
defaultSelSkelBdyArrowSize = 10
arrowparam = parameter.IntRangeParameter('arrowsize', (0, 20),
                                         defaultSelSkelBdyArrowSize,
                                         tip="Arrow size for edge boundaries.")

def _setSelSkelBdyParams(menuitem, color, linewidth, dotsize, arrowsize):
    global defaultSelSkelBdyColor
    global defaultSelSkelBdyLineWidth
    global defaultSelSkelBdyDotSize
    global defaultSelSkelBdyArrowSize
    defaultSelSkelBdyColor = color
    defaultSelSkelBdyLineWidth = linewidth
    defaultSelSkelBdyDotSize = dotsize
    defaultSelSkelBdyArrowSize = arrowsize

selskelbdyparams = [
    color.ColorParameter('color', value=defaultSelSkelBdyColor,
                         tip="Color for the selected boundary."),
    parameter.IntRangeParameter('linewidth', widthRange,
                                defaultSelSkelBdyLineWidth,
                                tip="Line width for edge boundaries."),
    parameter.IntRangeParameter('dotsize', widthRange,
                                defaultSelSkelBdyDotSize,
                                tip="Dot radius for point boundaries."),
    arrowparam
    ]

mainmenu.gfxdefaultsmenu.Skeletons.addItem(oofmenu.OOFMenuItem(
    "Selected_Boundary",
    callback=_setSelSkelBdyParams,
    params=selskelbdyparams,
    ordering=4.5,
    help="Set default parameters for displaying selected skeleton boundaries.",
    discussion="""<para>

    This command sets the default parameters for the
    <xref linkend="RegisteredClass-SelectedSkeletonBoundaryDisplay"/>,
    which displays the currently
    <link linkend="Section-Tasks-SkeletonBoundaries">selected
    <classname>Skeleton</classname> boundaries</link>.  Put this command
    in the &oof2rc; file to set default values for all &oof2; sessions.
    
    </para>"""))
                    
selectedSkeletonBoundaryDisplay = registeredclass.Registration(
    'Selected Boundary', display.DisplayMethod,
    SelectedSkeletonBoundaryDisplay,
    params=selskelbdyparams,
    ordering=2.3,
    layerordering=display.SemiLinear(1),
    whoclasses=('Skeleton',),
    tip="Display the currently selected boundary.",
    discussion = xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/skeletonselbdydisplay.xml')
    )

def defaultSelectedSkeletonBoundaryDisplay():
    return selectedSkeletonBoundaryDisplay(
        color=defaultSelSkelBdyColor,
        linewidth=defaultSelSkelBdyLineWidth,
        dotsize=defaultSelSkelBdyDotSize,
        arrowsize=defaultSelSkelBdyArrowSize)

ghostgfxwindow.PredefinedLayer('Skeleton', '<topmost>',
                               defaultSelectedSkeletonBoundaryDisplay)
