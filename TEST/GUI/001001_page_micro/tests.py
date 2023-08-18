# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *

def sensitization0():
    return sensitizationCheck(
        {'Microstructure' : 0,
         'New' : 1,
         'NewFromImage' : 0,
         'NewFromFile' : 1,
         'Rename' : 0,
         'Copy' : 0,
         'Delete' : 0,
         'Save' : 0,
         'Pane:PixelGroups:New' : 0,
         'Pane:PixelGroups:Auto': 0,
         'Pane:PixelGroups:Rename' : 0,
         'Pane:PixelGroups:Copy' : 0,
         'Pane:PixelGroups:Delete' : 0,
         'Pane:PixelGroups:Meshable' : 0,
         'Pane:PixelGroups:Add' : 0,
         'Pane:PixelGroups:Remove' : 0,
         'Pane:PixelGroups:Clear' : 0,
         'Pane:PixelGroups:Info' : 0
         },
        base='OOF2:Microstructure Page')

def sensitization1():
    return sensitizationCheck(
        {'Microstructure' : 1,
         'New' : 1,
         'NewFromImage' : 0,
         'NewFromFile' : 1,
         'Rename' : 1,
         'Copy' : 1,
         'Delete' : 1,
         'Save' : 1,
         'Pane:PixelGroups:New' : 1,
         'Pane:PixelGroups:Auto': 1,
         'Pane:PixelGroups:Rename' : 0,
         'Pane:PixelGroups:Copy' : 0,
         'Pane:PixelGroups:Delete' : 0,
         'Pane:PixelGroups:Meshable' : 0,
         'Pane:PixelGroups:Add' : 0,
         'Pane:PixelGroups:Remove' : 0,
         'Pane:PixelGroups:Clear' : 0,
         'Pane:PixelGroups:Info' : 0
         },
        base='OOF2:Microstructure Page')

def meshableButtonState(yesno):
    return yesno == gtklogger.findWidget(
        'OOF2:Microstructure Page:Pane:PixelGroups:Meshable').get_active()

def sensitization2():
    return sensitizationCheck(
        {'Microstructure' : 1,
         'New' : 1,
         'NewFromImage' : 0,
         'NewFromFile' : 1,
         'Rename' : 1,
         'Copy' : 1,
         'Delete' : 1,
         'Save' : 1,
         'Pane:PixelGroups:New' : 1,
         'Pane:PixelGroups:Auto': 1,
         'Pane:PixelGroups:Rename' : 1,
         'Pane:PixelGroups:Copy' : 1,
         'Pane:PixelGroups:Delete' : 1,
         'Pane:PixelGroups:Meshable' : 1,
         'Pane:PixelGroups:Add' : 0,
         'Pane:PixelGroups:Remove' : 0,
         'Pane:PixelGroups:Clear' : 0,
         'Pane:PixelGroups:Info' : 1
         },
        base='OOF2:Microstructure Page')

def sensitization3():
    return sensitizationCheck(
        {'Microstructure' : 1,
         'New' : 1,
         'NewFromImage' : 0,
         'NewFromFile' : 1,
         'Rename' : 1,
         'Copy' : 1,
         'Delete' : 1,
         'Save' : 1,
         'Pane:PixelGroups:New' : 1,
         'Pane:PixelGroups:Auto': 1,
         'Pane:PixelGroups:Rename' : 1,
         'Pane:PixelGroups:Copy' : 1,
         'Pane:PixelGroups:Delete' : 1,
         'Pane:PixelGroups:Meshable' : 1,
         'Pane:PixelGroups:Add' : 1,
         'Pane:PixelGroups:Remove' : 0,
         'Pane:PixelGroups:Clear' : 0,
         'Pane:PixelGroups:Info' : 1
         },
        base='OOF2:Microstructure Page')

def sensitization4():
    return sensitizationCheck(
        {'Microstructure' : 1,
         'New' : 1,
         'NewFromImage' : 0,
         'NewFromFile' : 1,
         'Rename' : 1,
         'Copy' : 1,
         'Delete' : 1,
         'Save' : 1,
         'Pane:PixelGroups:New' : 1,
         'Pane:PixelGroups:Auto': 1,
         'Pane:PixelGroups:Rename' : 1,
         'Pane:PixelGroups:Copy' : 1,
         'Pane:PixelGroups:Delete' : 1,
         'Pane:PixelGroups:Meshable' : 1,
         'Pane:PixelGroups:Add' : 1,
         'Pane:PixelGroups:Remove' : 1,
         'Pane:PixelGroups:Clear' : 1,
         'Pane:PixelGroups:Info' : 1
         },
        base='OOF2:Microstructure Page')

def sensitization5():
    return sensitizationCheck(
        {'Microstructure' : 1,
         'New' : 1,
         'NewFromImage' : 0,
         'NewFromFile' : 1,
         'Rename' : 1,
         'Copy' : 1,
         'Delete' : 1,
         'Save' : 1,
         'Pane:PixelGroups:New' : 1,
         'Pane:PixelGroups:Auto': 1,
         'Pane:PixelGroups:Rename' : 1,
         'Pane:PixelGroups:Copy' : 1,
         'Pane:PixelGroups:Delete' : 1,
         'Pane:PixelGroups:Meshable' : 1,
         'Pane:PixelGroups:Add' : 1,
         'Pane:PixelGroups:Remove' : 0,
         'Pane:PixelGroups:Clear' : 0,
         'Pane:PixelGroups:Info' : 1
         },
        base='OOF2:Microstructure Page')

def sensitization6():
    return sensitizationCheck(
        {'Microstructure' : 1,
         'New' : 1,
         'NewFromImage' : 1,
         'NewFromFile' : 1,
         'Rename' : 1,
         'Copy' : 1,
         'Delete' : 1,
         'Save' : 1,
         'Pane:PixelGroups:New' : 1,
         'Pane:PixelGroups:Auto': 1,
         'Pane:PixelGroups:Rename' : 0,
         'Pane:PixelGroups:Copy' : 0,
         'Pane:PixelGroups:Delete' : 0,
         'Pane:PixelGroups:Meshable' : 0,
         'Pane:PixelGroups:Add' : 0,
         'Pane:PixelGroups:Remove' : 0,
         'Pane:PixelGroups:Clear' : 0,
         'Pane:PixelGroups:Info' : 0
         },
        base='OOF2:Microstructure Page')

def sensitization7():
    return sensitizationCheck(
        {'Microstructure' : 1,
         'New' : 1,
         'NewFromImage' : 1,
         'NewFromFile' : 1,
         'Rename' : 1,
         'Copy' : 1,
         'Delete' : 1,
         'Save' : 1,
         'Pane:PixelGroups:New' : 1,
         'Pane:PixelGroups:Auto': 1,
         'Pane:PixelGroups:Rename' : 1,
         'Pane:PixelGroups:Copy' : 1,
         'Pane:PixelGroups:Delete' : 1,
         'Pane:PixelGroups:Meshable' : 1,
         'Pane:PixelGroups:Add' : 1,
         'Pane:PixelGroups:Remove' : 0,
         'Pane:PixelGroups:Clear' : 0,
         'Pane:PixelGroups:Info' : 1
         },
        base='OOF2:Microstructure Page')

def stackStateTest(mode, *args):
    stack = gtklogger.findWidget(
        'OOF2:Microstructure Page:Pane:PixelGroups:Stack')
    if mode == "message":
        label = gtklogger.findWidget(
            'OOF2:Microstructure Page:Pane:PixelGroups:Stack:Message')
        return (stack.get_visible_child() is label
                and label.get_text() == args[0])
    elif mode == "list":
        liszt = gtklogger.findWidget(
            'OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll')
        return stack.get_visible_child() is liszt
    print("Unexpected mode for stackStateText:", mode, file=sys.stderr)
    return False
