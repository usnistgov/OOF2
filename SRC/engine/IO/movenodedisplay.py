# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.common import color
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import display
from ooflib.common.IO import ghostgfxwindow
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
import types

import oofcanvas

class MoveNodeDisplay(display.DisplayMethod):
    def __init__(self, color, size):
        self.color = color
        self.size = size
        display.DisplayMethod.__init__(self)

    def draw(self, gfxwindow):
        toolbox = gfxwindow.getToolboxByName("Move_Nodes")
        node = toolbox.selectednode.node()
        if node and toolbox.selectednode.visible:
            dot = oofcanvas.CanvasDot.create(node.position(), self.size)
            dot.setFillColor(color.canvasColor(self.color))
            self.canvaslayer.addItem(dot)

    def getTimeStamp(self, gfxwindow):
        toolbox = gfxwindow.getToolboxByName("Move_Nodes")
        return max(self.timestamp,
                   toolbox.selectednode.getTimeStamp())

defaultMoveNodeColor = color.RGBAColor(1.0, 0.5, 0.5, 1.0)
defaultMoveNodeSize = 5

def _setDefaultMoveNodeParams(menuitem, color, size):
    global defaultMoveNodeSize
    global defaultMoveNodeColor
    defaultMoveNodeColor = color
    defaultMoveNodeSize = size

movenodeparams = [
    color.TranslucentColorParameter(
        'color', defaultMoveNodeColor,
        tip="Color for the to-be-moved node."),
    parameter.IntRangeParameter(
        'size', (0,20), defaultMoveNodeSize,
        tip="Node size.")]

mainmenu.gfxdefaultsmenu.Skeletons.addItem(oofmenu.OOFMenuItem(
    'Moving_Nodes',
    callback=_setDefaultMoveNodeParams,
    params=movenodeparams,
    ordering=7,
    help="Set default parameters for the Move Node toolbox displays.",
    discussion="""<para>

    Set default parameters governing how the
    <link linkend="Section-Graphics-MoveNodes">Move Nodes Toolbox</link>
    displays the moving node in the graphics window.  See
    <xref linkend="RegisteredClass-MoveNodeDisplay"/> for details.
    This command can be put in the &oof2rc; file to set the defaults for
    all &oof2; sessions.

    </para>"""))

moveNodeDisplay = registeredclass.Registration(
    'Moving Nodes',
    display.DisplayMethod,
    MoveNodeDisplay,
    params=movenodeparams,
    ordering=3.0,
    layerordering=display.PointLike(1),
    whoclasses=('Skeleton',),
    tip="Display the node being moved by the Move Node toolbox.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/movenodedisplay.xml')
    )

def defaultMoveNodeDisplay():
    return moveNodeDisplay(color=defaultMoveNodeColor,
                           size=defaultMoveNodeSize)

ghostgfxwindow.PredefinedLayer('Skeleton', '<topmost>', defaultMoveNodeDisplay)
