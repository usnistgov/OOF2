# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *
import sys, math, time

def checkCanvasPPU(initial_ppu, factor, tol=1.0e-6):
    # Assume there is only one graphics window.
    ppu = initial_ppu*factor
    import ooflib.common.IO.gfxmanager as gfxmanager
    gw = gfxmanager.gfxManager.windows[-1]
    res = gw.oofcanvas.getPixelsPerUnit()
    check = math.fabs(res-ppu)
    print("checkCanvasPPU: initial=%f, current=%f, factor=%f, diff=%f, tol=%f" % (initial_ppu, res, factor, check, tol), file=sys.stderr)
    if not check<tol:
        print("Canvas PPU failed, %f !< %f." % (check, tol), file=sys.stderr)
        return False
    return True
    

def getCanvasPPU():
    import ooflib.common.IO.gfxmanager as gfxmanager
    gw = gfxmanager.gfxManager.windows[-1]
    return gw.oofcanvas.getPixelsPerUnit()
