# -*- python -*-
# $RCSfile: tests.py,v $
# $Revision: 1.4 $
# $Author: langer $
# $Date: 2014/09/27 21:42:02 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *
import sys

fieldlist = 'OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers'

def listCheck(*names):
    fields = treeViewColValues(fieldlist, 0)
    for field, name in map(None, treeViewColValues(fieldlist, 0), names):
        if field.name() != name:
            print >> sys.stderr, field.name(), "!=", name
            return False
    return True

def selection(which):
    return listViewSelectedRowNo(fieldlist) == which
        

def sensitization0():
    # No fields selected and no initializers assigned.
    return sensitizationCheck({'Set'     : False,
                               'CopyInit': False,
                               'Clear'   : False,
                               'ClearAll': False,
                               'Apply'   : False,
                               'ApplyAt' : False
                               },
                              base='OOF2:Solver Page:VPane:FieldInit')

def sensitization1():
    # Field defined and selected, with no initializer.
    return sensitizationCheck({'Set'     : True,
                               'CopyInit': False,
                               'Clear'   : False,
                               'ClearAll': False,
                               'Apply'   : False,
                               'ApplyAt' : False
                               },
                              base='OOF2:Solver Page:VPane:FieldInit')

def sensitization2():
    # Field defined and selected, with an initializer assigned.
    return sensitizationCheck({'Set'     : True,
                               'CopyInit': True,
                               'Clear'   : True,
                               'ClearAll': True,
                               'Apply'   : True,
                               'ApplyAt' : True
                               },
                              base='OOF2:Solver Page:VPane:FieldInit')

def sensitization3():
    # Field defined and selected, with initializers assigned to some
    # fields, but not the selected one.
    return sensitizationCheck({'Set'     : True,
                               'CopyInit': True,
                               'Clear'   : False,
                               'ClearAll': True,
                               'Apply'   : True,
                               'ApplyAt' : True
                               },
                              base='OOF2:Solver Page:VPane:FieldInit')

def sensitization4():
    # Fields defined, but none selected, with at least one initializer assigned.
    return sensitizationCheck({'Set'     : False,
                               'CopyInit': True,
                               'Clear'   : False,
                               'ClearAll': True,
                               'Apply'   : True,
                               'ApplyAt' : True
                               },
                              base='OOF2:Solver Page:VPane:FieldInit')


def checkTime(time):
    from ooflib.engine import mesh
    meshctxt = mesh.meshes['microstructure:skeleton:mesh']
    return meshctxt.getCurrentTime() == time
