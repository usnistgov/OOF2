# -*- python -*-
# $RCSfile: tests.py,v $
# $Revision: 1.5 $
# $Author: langer $
# $Date: 2014/09/27 21:41:59 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *

def sensitization0():
    return (sensitizationCheck({"New" : 0,
                                "Rename" : 0,
                                "Copy" : 0,
                                "Delete" : 0,
                                "Save" : 0,
                                "Pane:ElementOps:OK" : 0},
                               base="OOF2:FE Mesh Page")
            and
            sensitizationCheck({"New" : 0,
                                "Rename" : 0,
                                "Edit" : 0,
                                "Copy" : 0,
                                "Info" : 0,
                                "Delete" : 0},
                               base="OOF2:FE Mesh Page:Pane:Subproblems"))

def sensitization1():
    return (sensitizationCheck({"New" : 1,
                               "Rename" : 0,
                               "Copy" : 0,
                               "Delete" : 0,
                               "Save" : 0,
                               "Pane:ElementOps:OK" : 0},
                              base="OOF2:FE Mesh Page")
            and
            sensitizationCheck({"New" : 0,
                                "Rename" : 0,
                                "Edit" : 0,
                                "Copy" : 0,
                                "Info" : 0,
                                "Delete" : 0},
                               base="OOF2:FE Mesh Page:Pane:Subproblems"))

def sensitization2():
    return (sensitizationCheck({"New" : 1,
                               "Rename" : 1,
                               "Copy" : 1,
                               "Delete" : 1,
                               "Save" : 1,
                               "Pane:ElementOps:OK" : 1},
                              base="OOF2:FE Mesh Page")
            and
            sensitizationCheck({"New" : 1,
                                "Rename" : 0,
                                "Edit" : 0,
                                "Copy" : 1,
                                "Info" : 1,
                                "Delete" : 0},
                               base="OOF2:FE Mesh Page:Pane:Subproblems"))

def sensitization3():
    return (sensitizationCheck({"New" : 1,
                               "Rename" : 1,
                               "Copy" : 1,
                               "Delete" : 1,
                               "Save" : 1,
                               "Pane:ElementOps:OK" : 1},
                              base="OOF2:FE Mesh Page")
            and
            sensitizationCheck({"New" : 1,
                                "Rename" : 1,
                                "Edit" : 1,
                                "Copy" : 1,
                                "Info" : 1,
                                "Delete" : 1},
                               base="OOF2:FE Mesh Page:Pane:Subproblems"))

def sensitization4():
    return (sensitizationCheck({"New" : 1,
                               "Rename" : 1,
                               "Copy" : 1,
                               "Delete" : 1,
                               "Save" : 1,
                               "Pane:ElementOps:OK" : 1},
                              base="OOF2:FE Mesh Page")
            and
            sensitizationCheck({"New" : 1,
                                "Rename" : 0,
                                "Edit" : 0,
                                "Copy" : 0,
                                "Info" : 0,
                                "Delete" : 0},
                               base="OOF2:FE Mesh Page:Pane:Subproblems"))


def subproblemNameCheck(*names):
    return chooserCheck(
       'OOF2:FE Mesh Page:Pane:Subproblems:subprobChooserScroll:subprobChooser',
       names)

def selectedSubproblem(name):
    if name:
        return chooserListStateCheck(
      'OOF2:FE Mesh Page:Pane:Subproblems:subprobChooserScroll:subprobChooser',
      [name])
    else:
        return chooserListStateCheck(
      'OOF2:FE Mesh Page:Pane:Subproblems:subprobChooserScroll:subprobChooser',
      [])
