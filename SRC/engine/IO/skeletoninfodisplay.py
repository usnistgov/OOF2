# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.common import config
from ooflib.SWIG.common.IO.OOFCANVAS import oofcanvas
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import display
from ooflib.common.IO import ghostgfxwindow
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump

def draw_elements(canvaslayer, elements, lineWidth, color):
    segs = oofcanvas.CanvasSegments()
    segs.setLineWidth(lineWidth)
    segs.setLineWidthInPixels()
    segs.setLineColor(color)
    for element in elements:
        for i in range(element.nnodes()):
            n0 = element.nodes[i].position()
            n1 = element.nodes[(i+1)%element.nnodes()].position()
            segs.addSegment(n0.x, n0.y, n1.x, n1.y)
    canvaslayer.addItem(segs)

class SkeletonInfoDisplay(display.DisplayMethod):
    def __init__(self, query_color, peek_color, node_size,
                 element_width, segment_width):
        self.query_color = query_color
        self.peek_color = peek_color
        self.colors = {"query": self.query_color, "peek": self.peek_color}
        self.node_size = node_size
        self.element_width = element_width
        self.segment_width = segment_width
        display.DisplayMethod.__init__(self)
        self.drawFuncs = {"Element": self.drawElement,
                          "Segment": self.drawSegment,
                          "Node": self.drawNode}

    def draw(self, gfxwindow, canvaslayer):
        toolbox = gfxwindow.getToolboxByName("Skeleton_Info")
        # Drawing "queried" item.
        if toolbox.querier and toolbox.querier.object:
            self.drawFuncs[toolbox.querier.targetname](canvaslayer,
                                                       toolbox.querier.object,
                                                       which="query")
        # Drawing "peeked" item.
        if toolbox.peeker:
            for objtype, obj in toolbox.peeker.objects.items():
                if obj:
                    self.drawFuncs[objtype](canvaslayer, obj, which="peek")

    def drawElement(self, canvaslayer, element, which="query"):
        draw_elements(canvaslayer, [element], 1.4*self.element_width,
                      oofcanvas.white)
        draw_elements(canvaslayer, [element], self.element_width,
                      color.canvasColor(self.colors[which]))
                      
    def drawSegment(self, canvaslayer, segment, which="query"):
        n0 = segment.nodes()[0].position()
        n1 = segment.nodes()[1].position()

        seg = oofcanvas.CanvasSegment(n0.x, n0.y, n1.x, n1.y)
        seg.setLineWidth(1.4*self.segment_width)
        seg.setLineWidthInPixels()
        seg.setLineColor(oofcanvas.white)
        canvaslayer.addItem(seg)

        seg = oofcanvas.CanvasSegment(n0.x, n0.y, n1.x, n1.y)
        seg.setLineWidth(self.segment_width)
        seg.setLineWidthInPixels()
        seg.setLineColor(color.canvasColor(self.colors[which]))
        canvaslayer.addItem(seg)

    def drawNode(self, canvaslayer, node, which="query"):
        dot = oofcanvas.CanvasDot(node.position().x, node.position().y,
                                  1.2*self.node_size)
        dot.setFillColor(oofcanvas.white)
        canvaslayer.addItem(dot)
        
        dot = oofcanvas.CanvasDot(node.position().x, node.position().y,
                                  self.node_size)
        dot.setFillColor(color.canvasColor(self.colors[which]))
        canvaslayer.addItem(dot)
        
    def getTimeStamp(self, gfxwindow):
        toolbox = gfxwindow.getToolboxByName("Skeleton_Info")
        return max(self.timestamp, toolbox.timestamp)

                
# This object should be created via the registration, and not
# directly via the initializer, because the registration creation
# method gives it a timestamp.

defaultSkelInfoQueryColor = color.RGBColor(0.0, 0.5, 1.0)
defaultSkelInfoPeekColor = color.RGBColor(1.0, 0.5, 0.5)
defaultSkelInfoNodeSize = 3
defaultSkelInfoElemWidth = 3
defaultSkelInfoSgmtWidth = 3
widthRange = (0, 10, 0.1)

def _setSkelInfoParams(menuitem, query_color, peek_color, node_size,
                       element_width, segment_width):
    global defaultSkelInfoQueryColor
    global defaultSkelInfoPeekColor
    global defaultSkelInfoNodeSize
    global defaultSkelInfoElemWidth
    global defaultSkelInfoSgmtWidth
    defaultSkelInfoQueryColor = query_color
    defaultSkelInfoPeekColor = peek_color
    defaultSkelInfoNodeSize = node_size
    defaultSkelInfoElemWidth = element_width
    defaultSkelInfoSgmtWidth = segment_width

skelinfoparams = [
    color.ColorParameter('query_color', defaultSkelInfoQueryColor,
                         tip="Color for the queried objects."),
    color.ColorParameter('peek_color', defaultSkelInfoPeekColor,
                         tip="Color for the peeked objects."),
    parameter.FloatRangeParameter('node_size', widthRange,
                                  defaultSkelInfoNodeSize,
                                  tip="Node size."),
    parameter.FloatRangeParameter('element_width', widthRange,
                                  defaultSkelInfoElemWidth,
                                  tip="Line width for elements."),
    parameter.FloatRangeParameter('segment_width', widthRange,
                                  defaultSkelInfoSgmtWidth,
                                  tip="Line width for segments.")]

mainmenu.gfxdefaultsmenu.Skeletons.addItem(oofmenu.OOFMenuItem(
    'Skeleton_Info',
    callback=_setSkelInfoParams,
    ordering=1,
    params=skelinfoparams,
    help="Set default parameters for the skeleton info toolbox display.",
    discussion="""<para>

    Set default parameters for the
    <xref linkend="RegisteredClass-SkeletonInfoDisplay"/> used by the
    <link linkend="Section-Graphics-SkeletonInfo">Skeleton Info</link> toolbox.
    See <xref linkend="RegisteredClass-SkeletonInfoDisplay"/> for the details.
    This command can be placed in the &oof2rc; file to set values for all
    &oof2; sessions.

    </para>"""))

skeletonInfoDisplay = registeredclass.Registration(
    'Info',
    display.DisplayMethod,
    SkeletonInfoDisplay,
    params=skelinfoparams,
    ordering=4.0,
    layerordering=display.SemiLinear(3),
    whoclasses=('Skeleton',),
    tip="Set parameters for the decorations used by the Skeleton Info toolbox.",
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/skeletoninfodisplay.xml')
    )

def defaultSkeletonInfoDisplay():
    return skeletonInfoDisplay(query_color=defaultSkelInfoQueryColor,
                               peek_color=defaultSkelInfoPeekColor,
                               node_size=defaultSkelInfoNodeSize,
                               element_width=defaultSkelInfoElemWidth,
                               segment_width=defaultSkelInfoSgmtWidth)

ghostgfxwindow.PredefinedLayer('Skeleton', '<topmost>',
                               defaultSkeletonInfoDisplay)

#########################################

class SkeletonIllegalElementDisplay(display.DisplayMethod):
    def __init__(self, color, linewidth):
        self.color = color
        self.linewidth = linewidth
        display.DisplayMethod.__init__(self)
    def draw(self, gfxwindow, canvaslayer):
        skel = self.who.resolve(gfxwindow).getObject()
        elements = skel.getIllegalElements()
        if elements:
            draw_elements(canvaslayer, elements, 1.4*self.linewidth,
                          oofcanvas.white)
            draw_elements(canvaslayer, elements, self.linewidth,
                          color.canvasColor(self.color))

defaultSkelIllegalColor = color.RGBColor(1.0, 0.01, 0.01)
defaultSkelIllegalWidth = 4

def _setSkelIllegalParams(menuitem, color, linewidth):
    global defaultSkelIllegalColor
    global defaultSkelIllegalWidth
    defaultSkelIllegalColor = color
    defaultSkelIllegalWidth = linewidth

skelillegalparams = [
    color.ColorParameter('color', defaultSkelIllegalColor,
                         tip="Color for illegal elements."),
    parameter.FloatRangeParameter('linewidth', widthRange,
                                  defaultSkelIllegalWidth,
                                  tip="Line width")]

mainmenu.gfxdefaultsmenu.Skeletons.addItem(oofmenu.OOFMenuItem(
    "Illegal_Elements",
    ordering=8,
    callback=_setSkelIllegalParams,
    params=skelillegalparams,
    help="Set default parameters for displaying illegal skeleton elements.",
    discussion="""<para>

    Set the default parameters for the
    <xref linkend="RegisteredClass-SkeletonIllegalElementDisplay"/> that
    highlights the
    <link linkend="Section-Concepts-Skeleton-Illegality">illegal</link>
    &elems; in a graphics window.  See
    <xref linkend="RegisteredClass-SkeletonIllegalElementDisplay"/> for
    the details.  This command may be placed in the &oof2rc; file
    to set default values for all &oof2; sessions.
    
    </para>"""))

skeletonIllegalDisplay = registeredclass.Registration(
    'Illegal Elements',
    display.DisplayMethod,
    SkeletonIllegalElementDisplay,
    params=skelillegalparams,
    ordering=4.1,
    layerordering=display.SemiLinear(3.1),
    whoclasses=('Skeleton',),
    tip="Display illegal elements in a Skeleton",
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/skeletonillegaldisplay.xml')
    )

def defaultSkeletonIllegalDisplay():
    return skeletonIllegalDisplay(color=defaultSkelIllegalColor,
                                  linewidth=defaultSkelIllegalWidth)

ghostgfxwindow.PredefinedLayer('Skeleton', '<topmost>',
                               defaultSkeletonIllegalDisplay)
