# -*- python -*-
# $RCSfile: DIR.py,v $
# $Revision: 1.6 $
# $Author: langer $
# $Date: 2014/09/27 21:40:10 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

dirname = 'diffusion'

if not DIM_3:
    clib = 'oof2engine'
else:
    clib = 'oof3dengine'

cfiles      = ['diffusion.C','charge.C','ion.C']
hfiles      = ['diffusion.h','charge.h','ion.h']
swigpyfiles = ['diffusion.spy','charge.spy','ion.spy']
swigfiles   = ['diffusion.swg','charge.swg','ion.swg']
pyfiles     = ['diff_problem.py']
