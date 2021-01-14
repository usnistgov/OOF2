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
    # No Mesh
    return (
        sensitizationCheck({'New' : 0,
                            'Rename' : 0,
                            'Edit' : 0,
                            'Copy' : 0,
                            'CopyAll' : 0,
                            'Delete' : 0},
                           base='OOF2:Boundary Conditions Page:Condition'
                           ))

def sensitization1():
    # Mesh exists, BCs exist, Fields/Eqns defined, BC selected
    return (
        sensitizationCheck({'New' : 1,
                            'Rename' : 1,
                            'Edit' : 1,
                            'Copy' : 1,
                            'CopyAll' : 1,
                            'Delete' : 1},
                           base='OOF2:Boundary Conditions Page:Condition'
                           ))

def sensitization2():
    # Mesh exists, BCs exist, Fields/Eqns defined, no selection
    return (
        sensitizationCheck({'New' : 1,
                            'Rename' : 0,
                            'Edit' : 0,
                            'Copy' : 0,
                            'CopyAll' : 1,
                            'Delete' : 0},
                           base='OOF2:Boundary Conditions Page:Condition'
                           ))

def sensitization3():
    # Mesh exists, BCs exist, no Fields/Eqns defined, no selection.
    # This is a peculiar state that can arise if a BC is copied from
    # another Mesh, or if fields and eqns are undefined after a BC is
    # created.
    return (
        sensitizationCheck({'New' : 0,
                            'Rename' : 0,
                            'Edit' : 0,
                            'Copy' : 0,
                            'CopyAll' : 1,
                            'Delete' : 0},
                           base='OOF2:Boundary Conditions Page:Condition'
                           ))

def bcNameCheck(*names):
    return list(names) == treeViewColValues(
        'OOF2:Boundary Conditions Page:Condition:BCScroll:BCList', 0)

def bcSelectCheck(name):
    return name == treeViewSelectCheck(
        'OOF2:Boundary Conditions Page:Condition:BCScroll:BCList', 0)
