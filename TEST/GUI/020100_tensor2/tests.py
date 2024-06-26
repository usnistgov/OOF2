# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *

removefile('rank2mat.dat')

base = "Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic"

def testAij(widgetname, **aijs):
    dct = {}
    for i in range(1, 4):
        for j in range(i, 4):
            aijname = "a%d%d" % (i,j)
            wijname = "%d,%d" % (i-1, j-1)
            dct[wijname] = aijs.get(aijname, 0.)
    return gtkMultiFloatCompare(dct, widgetbase=base+";"+widgetname+":alpha")

def sensitiveAij(widgetname, **aijs):
    for i in range(1, 4):
        for j in range(i, 4):
            aijname = "a%d%d" % (i,j)
            wijname = "%d,%d" % (i-1, j-1)
            nominal= aijs.get(aijname, 0)
            fullwname = base+";"+widgetname+":alpha:"+wijname
            actual = is_sensitive(fullwname)
            if actual != nominal:
                print("Sensitization test failed for", fullwname, file=sys.stderr)
                return 0
    return 1
