# -*- python -*-
# $RCSfile: tests.py,v $
# $Revision: 1.3 $
# $Author: langer $
# $Date: 2010/01/11 16:41:58 $

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
