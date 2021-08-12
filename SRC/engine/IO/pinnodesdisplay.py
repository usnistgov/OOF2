# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.common.IO.OOFCANVAS import oofcanvas
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common.IO import display
from ooflib.common.IO import ghostgfxwindow
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump

class PinnedNodesDisplay(display.DisplayMethod):
    def __init__(self, color, size):
        self.color = color
        self.size = size
        display.DisplayMethod.__init__(self)
    def draw(self, gfxwindow):
        skel = self.who.resolve(gfxwindow)
        clr = color.canvasColor(self.color)
        for node in skel.pinnednodes.retrieve():
            pt = node.position()
            dot = oofcanvas.CanvasDot(pt, 1.2*self.size)
            dot.setFillColor(oofcanvas.white.opacity(self.color.getAlpha()))
            self.canvaslayer.addItem(dot)
            dot = oofcanvas.CanvasDot(pt, self.size)
            dot.setFillColor(clr)
            self.canvaslayer.addItem(dot)
    def getTimeStamp(self, gfxwindow):
        return max(self.timestamp,
                   self.who.resolve(gfxwindow).pinnednodes.timestamp)

defaultPinNodeColor = color.RGBAColor(0.93, 0.93, 0.0, 1.0)
defaultPinNodeSize = 5

def _setPinNodeParams(menuitem, color, size):
    global defaultPinNodeColor
    global defaultPinNodeSize
    defaultPinNodeColor = color
    defaultPinNodeSize = size

pinnodeparams = [
    color.TranslucentColorParameter('color', defaultPinNodeColor,
                                    tip="Color for the pinned nodes."),
    parameter.IntRangeParameter('size', (0,20), defaultPinNodeSize,
                                tip="Node size.")]

mainmenu.gfxdefaultsmenu.Skeletons.addItem(oofmenu.OOFMenuItem(
    'Pinned_Nodes',
    callback=_setPinNodeParams,
    params=pinnodeparams,
    ordering=6,
    help="Set default parameters for displaying pinned skeleton nodes.",
    discussion="""<para>

    Set the default parameters for the
    <xref linkend="RegisteredClass-PinnedNodesDisplay"/>, which
    graphically indicates which &nodes; are
    <link linkend="Section-Concepts-Pin">pinned</link>.
    This command may be put in the &oof2rc; file to set defaults
    for all &oof2; sessions.

    </para>"""))

pinnedNodesDisplay = registeredclass.Registration(
    'Pinned Nodes',
    display.DisplayMethod,
    PinnedNodesDisplay,
    params=pinnodeparams,
    layerordering=display.PointLike(2),
    ordering=3.1,
    whoclasses=('Skeleton',),
    tip="Display the pinned nodes.",
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/pinnodesdisplay.xml')
    )

def defaultPinnedNodesDisplay():
    return pinnedNodesDisplay(color=defaultPinNodeColor,
                              size=defaultPinNodeSize)

ghostgfxwindow.PredefinedLayer('Skeleton', '<topmost>',
                               defaultPinnedNodesDisplay)
