# -*- python -*-
# $RCSfile: pixelselection.py,v $
# $Revision: 1.30 $
# $Author: langer $
# $Date: 2012/04/18 18:19:21 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


# There is one set of selected pixels for each Microstructure.  It's
# maintained as a list of iPoints and as a BitmapOverlay for quick
# drawing.

# PixelSelections have to know their Microstructures at the C++ level
# so that they can find their active areas.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import cpixelselection
from ooflib.common import color
from ooflib.common import debug
from ooflib.common.IO import bitoverlaydisplay
from ooflib.common.IO import ghostgfxwindow
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import whoville
from ooflib.common.IO import topwho       # required for '<top microstructure>'
import types

class PixelSelection(cpixelselection.CPixelSelection):
    def __repr__(self):
        return "PixelSelection(%s)" % len(self)
    def getMicrostructure(self):
        cms = self.getCMicrostructure()
        # Find which Microstructure corresponds to this CMicrostructure.
        return common.microstructure.microStructures[cms.name()]

#####################################

class PixelSelectionContext(whoville.WhoDoUndo):
    def getMicrostructure(self):
        return self.getObject().getMicrostructure()
    def start(self):
        newselection = self.getObject().clone()
        self.pushModification(newselection)

    # These have an embedded active area check.
    def select(self, selectioncourier):
        self.getObject().select(selectioncourier)
    def unselect(self, selectioncourier):
        self.getObject().unselect(selectioncourier)
    def toggle(self, selectioncourier):
        self.getObject().toggle(selectioncourier)
    def selectSelected(self, selectioncourier):
        self.getObject().selectSelected(selectioncourier)
    def clearAndSelect(self, selectioncourier):
        self.getObject().clear()
        self.getObject().select(selectioncourier)
    def selectFromGroup(self, group):
        # Used when copying the pixel selection from one
        # Microstructure to another.  Does *not* check the active
        # area.
        self.getObject().setFromGroup(group)
    def clear(self):
        self.getObject().clear()
    def invert(self):
        self.getObject().invert()
    def getSelection(self):
        return self.getObject().members()
    def getSelectionAsGroup(self):
        return self.getObject().getPixelGroup()
    def undo(self):
        self.undoModification()
    def redo(self):
        self.redoModification()
    def clearable(self):
        sz = self.size()
        if sz is not None:
            return sz != 0
        return 0
    def size(self):
        obj = self.getObject()
        if obj is not None:
            return len(self.getObject())
        return 0
    def getBitmap(self):
        return self.getObject().getBitmap()

##################
    
pixelselectionWhoClass = whoville.WhoDoUndoClass(
    'Pixel Selection',
    instanceClass=PixelSelectionContext,
    ordering=999,
    secret=0,
    proxyClasses=['<top microstructure>'])

###################

defaultPixelSelectionColor = color.RGBColor(1.0, 0.22, 0.09)
defaultTintOpacity = 0.6
defaultVoxelOpacity = 1.0

def _setDefaultPixelSelectionParams(menuitem, color, tintOpacity,
                                    voxelOpacity=1):
    global defaultPixelSelectionColor
    global defaultTintOpacity
    global defaultVoxelOpacity
    defaultPixelSelectionColor = color
    defaultTintOpacity = tintOpacity
    defaultVoxelOpacity = voxelOpacity


if config.dimension() == 2:
    colorparams=[
        color.ColorParameter(
            'color',
            defaultPixelSelectionColor,
            tip='Color of selected pixels.'),
                 parameter.FloatRangeParameter(
            'tintOpacity',
            (0., 1., 0.01), defaultTintOpacity,
            tip='Opacity of tint of selected pixels.'
            '  0 is transparent, 1 is opaque.')]
if config.dimension() == 3:
    colorparams=[
        color.ColorParameter(
            'color',
            defaultPixelSelectionColor,
            tip='Color of selected voxels.'),
        parameter.FloatRangeParameter(
            'tintOpacity',
            (0., 1., 0.01), defaultTintOpacity,
            tip='Opacity of tint of selected voxels.'
            '  0 is transparent, 1 is opaque.'),
        parameter.FloatRangeParameter(
            'voxelOpacity',
            (0., 1., 0.01), defaultVoxelOpacity,
            tip='Opacity of selected voxels.  0 is transparent, 1 is opaque.')]


mainmenu.gfxdefaultsmenu.Pixels.addItem(oofmenu.OOFMenuItem(
    'Pixel_Selection',
    callback=_setDefaultPixelSelectionParams,
    params = colorparams,
    help="Set default parameters for displaying selected pixels.",
    discussion="""<para>

    Set default parameters for the <xref
    linkend="RegisteredClass-BitmapOverlayDisplayMethod"/> that is used
    to display <link linkend="Section-Concepts-Microstructure-PixelSelection">pixel selections</link>.
    This command can be put in the &oof2rc; file to set defaults for all
    &oof2; sessions.

    </para>"""))

def predefinedPixelSelectionLayer():
    if config.dimension() == 2:
        return bitoverlaydisplay.bitmapOverlay(color=defaultPixelSelectionColor,
                                               tintOpacity=defaultTintOpacity)
    if config.dimension() == 3:
        return bitoverlaydisplay.bitmapOverlay(color=defaultPixelSelectionColor,
                                               tintOpacity=defaultTintOpacity,
                                               voxelOpacity=defaultVoxelOpacity)

ghostgfxwindow.PredefinedLayer('Pixel Selection', '<top microstructure>',
                               predefinedPixelSelectionLayer)
