# -*- python -*-
# $RCSfile: skeletoninfodisplay.py,v $
# $Revision: 1.27 $
# $Author: langer $
# $Date: 2010/12/21 03:35:12 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.common import config
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

    def draw(self, gfxwindow, device):
        toolbox = gfxwindow.getToolboxByName("Skeleton_Info")
        # Drawing "queried" item.
        if toolbox.querier and toolbox.querier.object:
            self.drawFuncs[toolbox.querier.targetname](device,
                                                       toolbox.querier.object,
                                                       which="query")
        # Drawing "peeked" item.
        if toolbox.peeker:
            for objtype, obj in toolbox.peeker.objects.items():
                if obj:
                    self.drawFuncs[objtype](device, obj, which="peek")

    def drawElement(self, device, element, which="query"):
        device.set_lineColor(self.colors[which])
        device.set_lineWidth(self.element_width)
        if config.dimension() == 2:
            for i in range(element.nnodes()):
                n0 = element.nodes[i]
                n1 = element.nodes[(i+1)%element.nnodes()]
                device.draw_segment(primitives.Segment(n0.position(),
                                                       n1.position()))
        elif config.dimension() == 3:
            device.draw_cell(element)

    def drawSegment(self, device, segment, which="query"):
        device.set_lineColor(self.colors[which])
        device.set_lineWidth(self.segment_width)
        if config.dimension() == 2:
            device.draw_segment(primitives.Segment(segment.nodes()[0].position(),
                                                   segment.nodes()[1].position()))
        elif config.dimension() == 3:
            # this is a hack, later on when vtk and oof are more
            # streamlined, we shouldn't have to create a vtkLine
            # twice.
            device.draw_cell(segment.getVtkLine())

    def drawNode(self, device, node, which="query"):
        device.set_lineColor(self.colors[which])
        device.set_lineWidth(self.node_size)
        device.draw_dot(node.position())

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
if config.dimension() == 2:
    widthRange = (0,10)
# In vtk, line widths of 0 cause errors
elif config.dimension() == 3:
    widthRange = (1,10)

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
    parameter.IntRangeParameter('node_size', widthRange, defaultSkelInfoNodeSize,
                                tip="Node size."),
    parameter.IntRangeParameter('element_width', widthRange,
                                defaultSkelInfoElemWidth,
                                tip="Line width for elements."),
    parameter.IntRangeParameter('segment_width', widthRange,
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
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/skeletoninfodisplay.xml')
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
    def draw(self, gfxwindow, device):
        skel = self.who().resolve(gfxwindow).getObject()
        elements = skel.getIllegalElements()
        if elements:
            device.set_lineColor(self.color)
            device.set_lineWidth(self.linewidth)
            if config.dimension() == 2:
                for el in elements:
                    for i in range(el.nnodes()):
                        n0 = el.nodes[i]
                        n1 = el.nodes[(i+1)%el.nnodes()]
                        device.draw_segment(primitives.Segment(n0.position(),
                                                               n1.position()))
            elif config.dimension() == 3:
                if len(elements):
                    gridPoints = skel.getPoints()
                    grid = vtk.vtkUnstructuredGrid()
                    numCells = len(elements)
                    grid.Allocate(numCells,numCells)
                    grid.SetPoints(gridPoints)
                    for el in elements:
                        grid.InsertNextCell(el.getCellType(), el.getPointIds())
                        device.draw_unstructuredgrid(grid)

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
    parameter.IntRangeParameter('linewidth', widthRange, defaultSkelIllegalWidth,
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
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/skeletonillegaldisplay.xml')
    )

def defaultSkeletonIllegalDisplay():
    return skeletonIllegalDisplay(color=defaultSkelIllegalColor,
                                  linewidth=defaultSkelIllegalWidth)

ghostgfxwindow.PredefinedLayer('Skeleton', '<topmost>',
                               defaultSkeletonIllegalDisplay)
