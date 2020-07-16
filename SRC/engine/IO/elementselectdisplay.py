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


class SkeletonElementSelectionDisplay(display.DisplayMethod):
    def __init__(self, color):
        self.color = color
        display.DisplayMethod.__init__(self)

    def draw(self, gfxwindow, canvaslayer):
        skel = self.who.resolve(gfxwindow)
        if skel is not None:
            skel.elementselection.begin_reading()
            clr = color.canvasColor(self.color)
            try:
                for e in skel.elementselection.retrieve():
                    poly = oofcanvas.CanvasPolygon()
                    for n in e.nodes:
                        pt = n.position()
                        poly.addPoint(pt.x, pt.y)
                    poly.setFillColor(clr)
                    canvaslayer.addItem(poly)
            finally:
                skel.elementselection.end_reading()
    def getTimeStamp(self, gfxwindow):
        return max(self.timestamp,
                   self.who.resolve(gfxwindow).elementselection.timestamp)
                
                
# This object should be created via the registration, and not
# directly via the initializer, because the registration creation
# method gives it a timestamp.

defaultSelectedElementColor = color.RGBAColor(0.88, 0.14, 0.07, 0.6)

def _setSelectedElementParams(menuitem, color):
    global defaultSelectedElementColor
    defaultSelectedElementColor = color

selectedElementParams = [
    color.TranslucentColorParameter('color', defaultSelectedElementColor,
                                    tip="Color for the selected elements.")
]

mainmenu.gfxdefaultsmenu.Skeletons.addItem(oofmenu.OOFMenuItem(
    'Selected_Elements',
    callback=_setSelectedElementParams,
    ordering=1,
    params=selectedElementParams,
    help="Set default parameters for displaying selected skeleton elements.",
    discussion="""<para>

    Set default parameters for the
    <xref linkend="RegisteredClass-SkeletonElementSelectionDisplay"/>,
    which displays the currently selected &skel; &elems; in the graphics
    window.  See
    <xref linkend="RegisteredClass-SkeletonElementSelectionDisplay"/>
    for a discussion of the parameters. This command may be put in the
    &oof2rc; file to set defaults for all &oof2; sessions.
    
    </para>"""))

elementSelectDisplay = registeredclass.Registration(
    'Selected Elements',
    display.DisplayMethod,
    SkeletonElementSelectionDisplay,
    params=selectedElementParams,
    ordering=2.0,
    layerordering=display.SemiPlanar,
    whoclasses=('Skeleton',),
    tip="Display the currently selected elements",
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/elementselectdisplay.xml')
)

def predefinedElemSelLayer():
    return elementSelectDisplay(color=defaultSelectedElementColor)

ghostgfxwindow.PredefinedLayer('Skeleton', '<topmost>', predefinedElemSelLayer)
