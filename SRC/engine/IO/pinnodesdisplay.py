# -*- python -*-
# $RCSfile: pinnodesdisplay.py,v $
# $Revision: 1.16 $
# $Author: langer $
# $Date: 2014/09/27 21:40:59 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

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
    def draw(self, gfxwindow, device):
        skel = self.who().resolve(gfxwindow)
        device.set_lineColor(self.color)
        device.set_lineWidth(self.size)
        for node in skel.pinnednodes.retrieve():
            device.draw_dot(node.position())
    def getTimeStamp(self, gfxwindow):
        return max(self.timestamp,
                   self.who().resolve(gfxwindow).pinnednodes.timestamp)

defaultPinNodeColor = color.RGBColor(0.93, 0.93, 0.0)
defaultPinNodeSize = 2

def _setPinNodeParams(menuitem, color, size):
    global defaultPinNodeColor
    global defaultPinNodeSize
    defaultPinNodeColor = color
    defaultPinNodeSize = size

pinnodeparams = [
    color.ColorParameter('color', defaultPinNodeColor,
                         tip="Color for the pinned nodes."),
    parameter.IntRangeParameter('size', (0,10), defaultPinNodeSize,
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
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/pinnodesdisplay.xml')
    )

def defaultPinnedNodesDisplay():
    return pinnedNodesDisplay(color=defaultPinNodeColor,
                              size=defaultPinNodeSize)

ghostgfxwindow.PredefinedLayer('Skeleton', '<topmost>',
                               defaultPinnedNodesDisplay)
