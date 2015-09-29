# -*- python -*-
# $RCSfile: DIR.py,v $
# $Revision: 1.9 $
# $Author: langer $
# $Date: 2014/09/27 21:41:12 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

dirname = 'nonlinear'
if not DIM_3:
    clib = 'oof2engine'
else:
    clib = 'oof3dengine'
cfiles  = [
    # 'nonlinear.C',
    'general_nonlinear_elasticity.C']
hfiles  = [
    # 'nonlinear.h',
    'general_nonlinear_elasticity.h']
swigpyfiles = [
    # 'nonlinear.spy',
    'general_nonlinear_elasticity.spy']
swigfiles = [
    # 'nonlinear.swg',
    'general_nonlinear_elasticity.swg']
