# -*- python -*-
# $RCSfile: microstructurePage.py,v $
# $Revision: 1.9 $
# $Author: langer $
# $Date: 2010/06/02 20:25:35 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import switchboard
from ooflib.SWIG.orientationmap import orientmapdata
from ooflib.common.IO import microstructuremenu
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import microstructurePage
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import tooltips
import gtk
import os

# Create a MicrostructurePageInfoPlugIn that displays the Orientation
# map file name in the page's info box.

def _orientationmapinfo(microstructure):
    filename = orientmapdata.getOrientationMapFile(microstructure.getObject())
    if filename:
        direct, basename = os.path.split(filename)
        return 'Orientation Map file: ' + basename + '\ndirectory: ' + direct
    return 'Orientation Map file: <None>'

plugin = microstructurePage.addMicrostructureInfo(callback=_orientationmapinfo,
                                                  ordering=1)

def _updateCB(ms):
    plugin.update()
    
switchboard.requestCallback('OrientationMap changed', _updateCB)

####################

# Add a button to the Microstructure page for the "New from
# Orientation Map" command.

def _newMSfromOrientationMap(button):
    menuitem = microstructuremenu.micromenu.Create_From_OrientationMap_File
    if parameterwidgets.getParameters(
        title='Create Microstructure from Orientation Map file',
        *menuitem.params):
        menuitem.callWithDefaults()

newfromorientmapbutton = gtkutils.StockButton(gtk.STOCK_NEW,
                                        "New from Orientation Map")
gtklogger.setWidgetName(newfromorientmapbutton, "NewFromOrientationMap")
gtklogger.connect(newfromorientmapbutton, 'clicked', _newMSfromOrientationMap)
tooltips.set_tooltip_text(newfromorientmapbutton,
    "Create a new Microstructure from an Orientation Map data file.")

microstructurePage.addNewButton(newfromorientmapbutton)

