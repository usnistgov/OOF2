# -*- python -*-
# $RCSfile: typename.py,v $
# $Revision: 1.6 $
# $Author: langer $
# $Date: 2014/09/27 21:40:33 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Used by TypeChecker.__repr__() in parameter.py.

import types

reversetypedir = {}

for name, tipe in types.__dict__.items():
    if type(tipe) is types.TypeType:
        reversetypedir[tipe] = name


def typename(tipe):
    if type(tipe) is types.ClassType:
        return tipe.__name__
    if type(tipe) is types.InstanceType:
        return tipe.__class__.__name__
    return reversetypedir[tipe]
