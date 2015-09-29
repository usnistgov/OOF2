# -*- python -*-
# $RCSfile: meshinfodisplay.py,v $
# $Revision: 1.30 $
# $Author: langer $
# $Date: 2010/12/04 03:50:03 $

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

class MeshInfoDisplay(display.DisplayMethod):
    def __init__(self, query_color, peek_color, node_size,
                 element_width):
        self.query_color = query_color
        self.peek_color = peek_color
        self.colors = {"query": self.query_color, "peek": self.peek_color}
        self.node_size = node_size
        self.element_width = element_width
        display.DisplayMethod.__init__(self)
        self.drawFuncs = {"Element": self.drawElement,
                          "Node": self.drawNode}


    def draw(self, gfxwindow, device):
        toolbox = gfxwindow.getToolboxByName("Mesh_Info")
        mesh = toolbox.meshcontext()
        mesh.begin_reading()
        mesh.restoreCachedData(gfxwindow.displayTime)
        try:
            # Draw "queried" item.
            if toolbox.querier and toolbox.querier.object:
                self.drawFuncs[toolbox.querier.targetname](device, toolbox, 
                                                           toolbox.querier.object,
                                                           which="query")
            # Draw "peeked" item.
            if toolbox.peeker and toolbox.peeker.objects.values():
                for objtype in toolbox.peeker.objects:
                    if toolbox.peeker.objects[objtype]:
                        self.drawFuncs[objtype](device, toolbox, 
                                                toolbox.peeker.objects[objtype],
                                                which="peek")
        finally:
            mesh.releaseCachedData()
            mesh.end_reading()

    def drawElement(self, device, toolbox, element, which="query"):
        device.set_lineColor(self.colors[which])
        device.set_lineWidth(self.element_width)
        if config.dimension() == 2:
            node_iter = element.cornernode_iterator().exteriornode_iterator()
            p_list = [node.position() for node in node_iter]
            displaced_p_list = [
                toolbox.meshlayer.displaced_from_undisplaced(
                toolbox.gfxwindow, x) for x in p_list]
            for i in range(len(displaced_p_list)):
                p0 = displaced_p_list[i]
                p1 = displaced_p_list[(i+1)%len(displaced_p_list)]
                device.draw_segment(primitives.Segment(p0, p1))
        elif config.dimension() == 3:
            device.draw_cell(element)


    def drawNode(self, device, toolbox, node, which="query"):
        device.set_lineColor(self.colors[which])
        device.set_lineWidth(self.node_size)
        if config.dimension() == 2:
            displaced_position = toolbox.meshlayer.displaced_from_undisplaced(
                toolbox.gfxwindow(), node.position())
            device.draw_dot(displaced_position)
        elif config.dimension() == 3:
            device.draw_dot(node.position())

    def getTimeStamp(self, gfxwindow):
        toolbox = gfxwindow.getToolboxByName("Mesh_Info")
        if toolbox.querier and toolbox.peeker:
            return max(self.timestamp,
                       gfxwindow.displayTimeChanged,
                       toolbox.querier.getTimeStamp(),
                       toolbox.peeker.getTimeStamp())
        elif toolbox.querier and not toolbox.peeker:
            return max(self.timestamp,
                       gfxwindow.displayTimeChanged,
                       toolbox.querier.getTimeStamp())
        else:
            return self.timestamp
                
# This object should be created via the registration, and not
# directly via the initializer, because the registration creation
# method gives it a timestamp.

defaultQueryColor = color.RGBColor(0.0, 0.5, 1.0)
defaultPeekColor = color.RGBColor(1.0, 0.5, 0.5)
defaultNodeSize = 3
defaultElementWidth = 2
if config.dimension() == 2:
    widthRange = (0,10)
# In vtk, line widths of 0 cause errors
elif config.dimension() == 3:
    widthRange = (1,10)

def _setMeshInfoParams(menuitem, query_color, peek_color, node_size,
                       element_width):
    global defaultQueryColor
    global defaultPeekColor
    global defaultNodeSize
    global defaultElementWidth
    defaultQueryColor = query_color
    defaultPeekColor = peek_color
    defaultNodeSize = node_size
    defaultElementWidth = element_width

meshinfoparams = [
    color.ColorParameter('query_color', defaultQueryColor,
                         tip="Color for the queried object."),
    color.ColorParameter('peek_color', defaultPeekColor,
                         tip="Color for the peeked object."),
    parameter.IntRangeParameter('node_size', widthRange, defaultNodeSize,
                                tip="Node size."),
    parameter.IntRangeParameter('element_width', widthRange,
                                defaultElementWidth,
                                tip="Line thickness for element edge.")]

mainmenu.gfxdefaultsmenu.Meshes.addItem(oofmenu.OOFMenuItem(
    "Mesh_Info",
    callback=_setMeshInfoParams,
    params=meshinfoparams,
    ordering=1,
    help="Set default parameters for Mesh Info displays.",
    discussion="""<para>

    Set default parameters for
    <link linkend="RegisteredClass-MeshInfoDisplay"><classname>MeshInfoDisplays</classname></link>.
    See <xref linkend="RegisteredClass-MeshInfoDisplay"/> for the details.
    This command may be placed in the &oof2rc; file to set a default value
    for all &oof2; sessions.
    
    </para>"""))

meshInfoDisplay = registeredclass.Registration(
    'Info',
    display.DisplayMethod,
    MeshInfoDisplay,
    params=meshinfoparams,
    ordering=4.0,
    layerordering=display.PointLike(100),
    whoclasses=('Mesh',),
    tip="Set display parameters for the decorations used by the Mesh Info toolbox.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/meshinfodisplay.xml')
    )

def defaultMeshInfoDisplay():
    return meshInfoDisplay(query_color=defaultQueryColor,
                           peek_color=defaultPeekColor,
                           node_size=defaultNodeSize,
                           element_width=defaultElementWidth)
ghostgfxwindow.PredefinedLayer('Mesh', '<topmost>', defaultMeshInfoDisplay)
