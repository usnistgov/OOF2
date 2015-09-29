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

def solvable():
    return sensitizationCheck({"OOF2:Solver Page:solve" : True})

def unsolvable():
    return sensitizationCheck({"OOF2:Solver Page:solve" : False})

def details(strng):
    return gtkTextviewTail('OOF2 Messages 1:Text', strng)

subplist = 'OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList'

def selection(which):
    return listViewSelectedRowNo(subplist) == which

def listCheck(*names):
    for s, n in map(None, treeViewColValues(subplist, 0), names):
        if s.name() != n:
            print >> sys.stderr, s.name(), "!=", n
            return False
    return True

def sensitization0():
    # No selected subproblems and no solvers
    return sensitizationCheck({'Set'      : False,
                               'Remove'   : False,
                               'RemoveAll': False,
                               'First'    : False,
                               'Earlier'  : False,
                               'Later'    : False,
                               'Last'     : False},
        base='OOF2:Solver Page:VPane:Subproblems')

def sensitization1():
    # One subproblem, selected, with no solver.
    return sensitizationCheck({'Set'      : True,
                               'Remove'   : False,
                               'RemoveAll': False,
                               'First'    : False,
                               'Earlier'  : False,
                               'Later'    : False,
                               'Last'     : False},
        base='OOF2:Solver Page:VPane:Subproblems')

def sensitization2():
    # One subproblem, selected, with a solver.
    return sensitizationCheck({'Set'      : True,
                               'Remove'   : True,
                               'RemoveAll': True,
                               'First'    : False,
                               'Earlier'  : False,
                               'Later'    : False,
                               'Last'     : False},
        base='OOF2:Solver Page:VPane:Subproblems')

def sensitization3():
    # More than one subproblem, first one selected, no solvers.
    return sensitizationCheck({'Set'      : True,
                               'Remove'   : False,
                               'RemoveAll': False,
                               'First'    : False,
                               'Earlier'  : False,
                               'Later'    : True,
                               'Last'     : True},
        base='OOF2:Solver Page:VPane:Subproblems')

def sensitization4():
    # More than one subproblem, first one selected, with a solver.
    return sensitizationCheck({'Set'      : True,
                               'Remove'   : True,
                               'RemoveAll': True,
                               'First'    : False,
                               'Earlier'  : False,
                               'Later'    : True,
                               'Last'     : True},
        base='OOF2:Solver Page:VPane:Subproblems')

def sensitization5():
    # More than one subproblem, last one selected, unselected one has a solver.
    return sensitizationCheck({'Set'      : True,
                               'Remove'   : False,
                               'RemoveAll': True,
                               'First'    : True,
                               'Earlier'  : True,
                               'Later'    : False,
                               'Last'     : False},
        base='OOF2:Solver Page:VPane:Subproblems')

def sensitization6():
    # More than one subproblem, last one selected, with a solver.
    return sensitizationCheck({'Set'      : True,
                               'Remove'   : True,
                               'RemoveAll': True,
                               'First'    : True,
                               'Earlier'  : True,
                               'Later'    : False,
                               'Last'     : False},
        base='OOF2:Solver Page:VPane:Subproblems')

def sensitization7():
    # More than one subproblem, last one selected, no solvers.
    return sensitizationCheck({'Set'      : True,
                               'Remove'   : False,
                               'RemoveAll': False,
                               'First'    : True,
                               'Earlier'  : True,
                               'Later'    : False,
                               'Last'     : False},
        base='OOF2:Solver Page:VPane:Subproblems')

def sensitization8():
    # More than two subproblems, middle one selected, no solvers.
    return sensitizationCheck({'Set'      : True,
                               'Remove'   : False,
                               'RemoveAll': False,
                               'First'    : True,
                               'Earlier'  : True,
                               'Later'    : True,
                               'Last'     : True},
        base='OOF2:Solver Page:VPane:Subproblems')
