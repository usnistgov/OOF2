# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *

def layerMenuSensitization(menuitem, sensitivity):
    actual = menuSensitive("OOF2 Graphics 1:MenuBar", ["Layer", menuitem])
    if actual != sensitivity:
        print("Layer menu sensitization failed for", menuitem, file=sys.stderr)
        return 0
    return 1
        

def sensitizationCheck0():
    #print gtklogger.findAllWidgets("OOF2 Graphics 1:MenuBar")
    return (layerMenuSensitization("New", 1) and
            layerMenuSensitization("Edit", 0) and
            layerMenuSensitization("Delete", 0) and
            layerMenuSensitization("Hide", 0) and
            layerMenuSensitization("Show", 0) and
            # layerMenuSensitization("Hide_Contour_Map", 0) and
            # layerMenuSensitization("Show_Contour_Map", 0) and
            layerMenuSensitization("Raise", 0) and
            layerMenuSensitization("Lower", 0) and
            layerMenuSensitization("Reorder_All", 0)
            )

def sensitizationCheck1():
    return (layerMenuSensitization("New", 1) and
            layerMenuSensitization("Edit", 1) and
            layerMenuSensitization("Delete", 1) and
            layerMenuSensitization("Hide", 1) and
            layerMenuSensitization("Show", 0) and
            # layerMenuSensitization("Hide_Contour_Map", 0) and
            # layerMenuSensitization("Show_Contour_Map", 0) and
            layerMenuSensitization("Raise", 1) and
            layerMenuSensitization("Lower", 1) and
            layerMenuSensitization("Reorder_All", 0)
            )

def sensitizationCheck2():
    return (layerMenuSensitization("New", 1) and
            layerMenuSensitization("Edit", 1) and
            layerMenuSensitization("Delete", 1) and
            layerMenuSensitization("Hide", 1) and
            layerMenuSensitization("Show", 0) and
            layerMenuSensitization("Freeze", 1) and
            # layerMenuSensitization("Hide_Contour_Map", 0) and
            # layerMenuSensitization("Show_Contour_Map", 0) and
            layerMenuSensitization("Raise", 1) and
            layerMenuSensitization("Lower", 0) and
            layerMenuSensitization("Reorder_All", 1)
            )

def sensitizationCheck3():
    return (layerMenuSensitization("New", 1) and
            layerMenuSensitization("Edit", 1) and
            layerMenuSensitization("Delete", 1) and
            layerMenuSensitization("Hide", 1) and
            layerMenuSensitization("Show", 0) and
            # layerMenuSensitization("Hide_Contour_Map", 0) and
            # layerMenuSensitization("Show_Contour_Map", 0) and
            layerMenuSensitization("Raise", 1) and
            layerMenuSensitization("Lower", 1) and
            layerMenuSensitization("Reorder_All", 1)
            )

def sensitizationCheck4():
    return (layerMenuSensitization("New", 1) and
            layerMenuSensitization("Edit", 1) and
            layerMenuSensitization("Delete", 1) and
            layerMenuSensitization("Hide", 1) and
            layerMenuSensitization("Show", 0) and
            # layerMenuSensitization("Hide_Contour_Map", 0) and
            # layerMenuSensitization("Show_Contour_Map", 0) and
            layerMenuSensitization("Raise", 1) and
            layerMenuSensitization("Lower", 0) and
            layerMenuSensitization("Reorder_All", 0)
            )

def sensitizationCheck5():
    return (layerMenuSensitization("New", 1) and
            layerMenuSensitization("Edit", 1) and
            layerMenuSensitization("Delete", 1) and
            layerMenuSensitization("Hide", 0) and
            layerMenuSensitization("Show", 1) and
            # layerMenuSensitization("Hide_Contour_Map", 0) and
            # layerMenuSensitization("Show_Contour_Map", 0) and
            layerMenuSensitization("Raise", 1) and
            layerMenuSensitization("Lower", 1) and
            layerMenuSensitization("Reorder_All", 0)
            )

def sensitizationCheck6():
    return (layerMenuSensitization("New", 1) and
            layerMenuSensitization("Edit", 1) and
            layerMenuSensitization("Delete", 1) and
            layerMenuSensitization("Hide", 1) and
            layerMenuSensitization("Show", 0) and
            # layerMenuSensitization("Hide_Contour_Map", 1) and
            # layerMenuSensitization("Show_Contour_Map", 0) and
            layerMenuSensitization("Raise", 1) and
            layerMenuSensitization("Lower", 1) and
            layerMenuSensitization("Reorder_All", 0)
            )

def contourLabels():
    return (gtklogger.findWidget(
        "OOF2 Graphics 1:Pane0:Pane1:ContourMap:MapMin"),
            gtklogger.findWidget(
        "OOF2 Graphics 1:Pane0:Pane1:ContourMap:MapMax"))

def contourLevelLabels():
    return (gtklogger.findWidget(
        "OOF2 Graphics 1:Pane0:Pane1:ContourMap:LevelMin"),
            gtklogger.findWidget(
        "OOF2 Graphics 1:Pane0:Pane1:ContourMap:LevelMax"))

def contourBounds(bmin, bmax, tolerance=1.e-6):
    minlabel, maxlabel = contourLabels()
    return (abs(float(maxlabel.get_text()) - bmax) < tolerance and
            abs(float(minlabel.get_text()) - bmin) < tolerance)

def noContourBounds():
    minlabel, maxlabel = contourLabels()
    return minlabel.get_text() == "min" and maxlabel.get_text() == "max"

def contourInterval(bmin, bmax, tolerance=1.e-6):
    minlabel, maxlabel = contourLevelLabels()
    print("minlabel=", minlabel.get_text())
    print("maxlabel=", maxlabel.get_text())
    return (abs(float(maxlabel.get_text()) - bmax) < tolerance and
            abs(float(minlabel.get_text()) - bmin) < tolerance)

def noContourInterval():
    minlabel, maxlabel = contourLevelLabels()
    return minlabel.get_text() == "" and maxlabel.get_text() == ""
    
