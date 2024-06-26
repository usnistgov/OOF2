# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *

def pixelGroupListCheck(*grps):
    return chooserListCheck(
        'OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList',
        grps)

def selectedGroupCheck(grp):
    if grp is None:
        return chooserListStateCheck(
            'OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList',
            [])
    return chooserListStateCheck(
        'OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList',
        [grp])

def microstructureCheck(msname):
    return chooserStateCheck('OOF2:Microstructure Page:Microstructure', msname)

def meshableCheck(active):
    return (gtklogger.findWidget(
        'OOF2:Microstructure Page:Pane:PixelGroups:Meshable').get_active()
            == active)

def sensitization0(): # no microstructure
    return sensitizationCheck(
        {'New' : 0,
         'Rename' : 0,
         'Copy' : 0,
         'Delete' : 0,
         'Meshable' : 0,
         'Add' : 0,
         'Remove' : 0,
         'Clear' : 0,
         'Info' : 0},
        base='OOF2:Microstructure Page:Pane:PixelGroups')

def sensitization1(): # no selected group
    return sensitizationCheck(
        {'New' : 1,
         'Rename' : 0,
         'Copy' : 0,
         'Delete' : 0,
         'Meshable' : 0,
         'Add' : 0,
         'Remove' : 0,
         'Clear' : 0,
         'Info' : 0},
        base='OOF2:Microstructure Page:Pane:PixelGroups')

def sensitization2(): #selected empty group, no selected pixels
    return sensitizationCheck(
        {'New' : 1,
         'Rename' : 1,
         'Copy' : 1,
         'Delete' : 1,
         'Meshable' : 1,
         'Add' : 0,
         'Remove' : 0,
         'Clear' : 0,
         'Info' : 1},
        base='OOF2:Microstructure Page:Pane:PixelGroups')

def sensitization3(): # selected empty group, selected pixels
    return sensitizationCheck(
        {'New' : 1,
         'Rename' : 1,
         'Copy' : 1,
         'Delete' : 1,
         'Meshable' : 1,
         'Add' : 1,
         'Remove' : 0,
         'Clear' : 0,
         'Info' : 1},
        base='OOF2:Microstructure Page:Pane:PixelGroups')

def sensitization4(): # selected non-empty group, selected pixels
    return sensitizationCheck(
        {'New' : 1,
         'Rename' : 1,
         'Copy' : 1,
         'Delete' : 1,
         'Meshable' : 1,
         'Add' : 1,
         'Remove' : 1,
         'Clear' : 1,
         'Info' : 1},
        base='OOF2:Microstructure Page:Pane:PixelGroups')

def sensitization5(): # selected non-empty group, no selected pixels
    return sensitizationCheck(
        {'New' : 1,
         'Rename' : 1,
         'Copy' : 1,
         'Delete' : 1,
         'Meshable' : 1,
         'Add' : 0,
         'Remove' : 0,
         'Clear' : 1,
         'Info' : 1},
        base='OOF2:Microstructure Page:Pane:PixelGroups')

