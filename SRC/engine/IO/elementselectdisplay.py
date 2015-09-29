# -*- python -*-
# $RCSfile: elementselectdisplay.py,v $
# $Revision: 1.25 $
# $Author: langer $
# $Date: 2014/09/27 21:40:58 $

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


class SkeletonElementSelectionDisplay(display.DisplayMethod):
    def __init__(self, color, opacity):
        self.color = color
        self.opacity = opacity
        display.DisplayMethod.__init__(self)

    def draw(self, gfxwindow, device):
        skel = self.who().resolve(gfxwindow)
        if skel is not None:
            device.set_lineColor(self.color)
            device.set_fillColorAlpha(self.color, color.alpha(self.opacity))
            skel.elementselection.begin_reading()
            try:
                if config.dimension() == 2:
                    for e in skel.elementselection.retrieve():
                        device.fill_polygon(primitives.Polygon([x.position()
                                                                for x in e.nodes]))
                elif config.dimension() == 3:
                    if len(skel.elementselection.retrieve()):
                        gridPoints = skel.getObject().getPoints()
                        grid = vtk.vtkUnstructuredGrid()
                        numCells = len(skel.elementselection.retrieve())
                        grid.Allocate(numCells,numCells)
                        grid.SetPoints(gridPoints)
                        for e in skel.elementselection.retrieve():
                            grid.InsertNextCell(e.getCellType(), e.getPointIds())
                        device.draw_filled_unstructuredgrid(grid)


                        
            finally:
                skel.elementselection.end_reading()
    def getTimeStamp(self, gfxwindow):
        return max(self.timestamp,
                   self.who().resolve(gfxwindow).elementselection.timestamp)
                
                
# This object should be created via the registration, and not
# directly via the initializer, because the registration creation
# method gives it a timestamp.

defaultSelectedElementColor = color.RGBColor(0.88, 0.14, 0.07)
defaultSelectedElementOpacity = 0.6

def _setSelectedElementParams(menuitem, color, opacity):
    global defaultSelectedElementColor
    global defaultSelectedElementOpacity
    defaultSelectedElementColor = color
    defaultSelectedElementOpacity = opacity

selectedElementParams = [
    color.ColorParameter('color', defaultSelectedElementColor,
                         tip="Color for the selected elements."),
    parameter.FloatRangeParameter('opacity', (0., 1., 0.01),
                                  defaultSelectedElementOpacity,
                                  tip="Opacity of the selected elements.")]

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
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/elementselectdisplay.xml'))
                                                

def predefinedElemSelLayer():
    return elementSelectDisplay(color=defaultSelectedElementColor,
                                opacity=defaultSelectedElementOpacity)

ghostgfxwindow.PredefinedLayer('Skeleton', '<topmost>', predefinedElemSelLayer)
