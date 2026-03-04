# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import os
from generics import *

def imagePageSensitizationCheck0():
    # before any image modifications
    return sensitizationCheck(
        {
        'Prev' : 0,
        'OK' : 1,
        'Next' : 0,
        'Undo' : 0,
        'Redo' : 0
        },
        base='OOF2:Image Page:Pane')

def imagePageSensitizationCheck1():
    # after one image modification
    return sensitizationCheck(
        {
        'Prev' : 0,
        'OK' : 1,
        'Next' : 0,
        'Undo' : 1,
        'Redo' : 0
        },
        base='OOF2:Image Page:Pane')

def imagePageSensitizationCheck2():
    # after two image modifications
    return sensitizationCheck(
        {
        'Prev' : 1,
        'OK' : 1,
        'Next' : 0,
        'Undo' : 1,
        'Redo' : 0
        },
        base='OOF2:Image Page:Pane')

def imagePageSensitizationCheck3():
    # new image, but old methods available
    return sensitizationCheck(
        {
        'Prev' : 1,
        'OK' : 1,
        'Next' : 0,
        'Undo' : 0,
        'Redo' : 0
        },
        base='OOF2:Image Page:Pane')

def imagePageSensitizationCheck4():
    # Undo once
    return sensitizationCheck(
        {
        'Prev' : 1,
        'OK' : 1,
        'Next' : 0,
        'Undo' : 1,
        'Redo' : 1
        },
        base='OOF2:Image Page:Pane')

def imagePageSensitizationCheck5():
    # Undo all
    return sensitizationCheck(
        {
        'Prev' : 1,
        'OK' : 1,
        'Next' : 0,
        'Undo' : 0,
        'Redo' : 1
        },
        base='OOF2:Image Page:Pane')

_grouplist = "OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList"
def groupListCheck(*groups):
    return chooserListCheck(_grouplist, groups)

def groupListStateCheck(group):
    return chooserListStateCheck(_grouplist, [group])

def autoModeCheck():
    return gtklogger.findWidget('Dialog-Create new pixel group:name').autowidget.automatic

def newPixelGroupSensitizationCheck0():
    # Pixelgroup name entry widget is in automatic mode
    return (sensitizationCheck(
        {
            "widget_GTK_RESPONSE_OK" : 1,
            "widget_GTK_RESPONSE_CANCEL" : 1,
            "name" : 1
        },
        base="Dialog-Create new pixel group")
            and
            autoModeCheck())

# def newPixelGroupSensitizationCheck1():
#     return sensitizationCheck(
#         {
#         "gtk-ok" : 0,
#         "gtk-cancel" : 1
#         },
#         base="Dialog-Create new pixel group")

def newPixelGroupSensitizationCheck1():
    # PixelGroup name entry widget is not in automatic mode
    return (sensitizationCheck(
        {
            'widget_GTK_RESPONSE_OK' : 1,
            'widget_GTK_RESPONSE_CANCEL' : 1,
            'name' : 1
        },
        base="Dialog-Create new pixel group")
            and
            not autoModeCheck())
            
# def newPixelGroupSensitizationCheck3():
#     # When Auto is not clicked, but Text is empty
#     return sensitizationCheck(
#         {
#         'gtk-ok' : 0,
#         'gtk-cancel' : 1,
#         'name:Auto' : 1,
#         'name:Text' : 1
#         },
#         base="Dialog-Create new pixel group")
