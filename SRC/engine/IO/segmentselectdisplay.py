# -*- python -*-
# $RCSfile: segmentselectdisplay.py,v $
# $Revision: 1.29 $
# $Author: langer $
# $Date: 2010/12/07 21:57:05 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.common import color
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import display
from ooflib.common.IO import ghostgfxwindow
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump

# This object should be created via the registration, and not
# directly via the initializer, because the registration creation
# method gives it a timestamp.

class SkeletonSegmentSelectionDisplay(display.DisplayMethod):
    def __init__(self, color, line_width):
        self.color = color
        self.line_width = line_width
        display.DisplayMethod.__init__(self)
    def draw(self, gfxwindow, device):
        skel = self.who().resolve(gfxwindow)
        if skel is not None:
            device.set_lineColor(self.color)
            device.set_lineWidth(self.line_width)
            if config.dimension() == 2:
                for s in skel.segmentselection.retrieve():
                    device.draw_segment(primitives.Segment(s.nodes()[0].position(),
                                                           s.nodes()[1].position()))
            elif config.dimension() == 3:
                numsegs = len(skel.segmentselection.retrieve())
                if numsegs:
                    gridPoints = skel.getObject().getPoints()
                    grid = vtk.vtkUnstructuredGrid()
                    grid.Allocate(numsegs,numsegs)
                    grid.SetPoints(gridPoints)
                    for s in skel.segmentselection.retrieve():
                        line = s.getVtkLine()
                        grid.InsertNextCell(line.GetCellType(), line.GetPointIds())
                    device.draw_unstructuredgrid(grid)

    def getTimeStamp(self, gfxwindow):
        return max(self.timestamp,
                   self.who().resolve(gfxwindow).segmentselection.timestamp)
            
defaultSegSelColor = color.RGBColor(0.13, 0.93, 0.25)
defaultSegSelWidth = 2

def _setSegSelParams(menuitme, color, line_width):
    global defaultSegSelColor
    global defaultSegSelWidth
    defaultSegSelColor = color
    defaultSegSelWidth = line_width

segselparams = [
    color.ColorParameter('color', defaultSegSelColor,
                         tip="Color for the selected segments."),
    parameter.IntRangeParameter('line_width', (0,10), defaultSegSelWidth,
                                tip="Line width.")]

mainmenu.gfxdefaultsmenu.Skeletons.addItem(oofmenu.OOFMenuItem(
    'Selected_Segments',
    callback=_setSegSelParams,
    ordering=3,
    params=segselparams,
    help="Set default parameters for displaying selected skeleton segments.",
    discussion="""<para>

    Set default parameters for the
    <xref linkend="RegisteredClass-SkeletonSegmentSelectionDisplay"/>,
    which displays the currently selected &skel; &sgmts; in the graphics
    window.  See
    <xref linkend="RegisteredClass-SkeletonSegmentSelectionDisplay"/>
    for a discussion of the parameters. This command may be put in the
    &oof2rc; file to set defaults for all &oof2; sessions.
    
    </para>"""))

segmentSelectDisplay = registeredclass.Registration(
    'Selected Segments',
    display.DisplayMethod,
    SkeletonSegmentSelectionDisplay,
    params=segselparams,
    ordering=2.1,
    layerordering=display.SemiLinear(4),
    whoclasses=('Skeleton',),
    tip="Display the currently selected segments.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/segmentselectdisplay.xml')
    )

def defaultSegmentSelectDisplay():
    return segmentSelectDisplay(color=defaultSegSelColor,
                                line_width=defaultSegSelWidth)

ghostgfxwindow.PredefinedLayer('Skeleton', '<topmost>',
                               defaultSegmentSelectDisplay)
