# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *
import gtk

removefile('rank3mat.dat')

base = "Dialog-Parametrize Couplings;PiezoElectricity"

def checkNames(vars):
    # Make sure all args are of the form d[123][123456].  This checks
    # that the test script is written correctly.  It's not an oof2
    # check, per se.
    for var in vars.keys():
        if var[0] != 'd' or var[1] not in '123' or var[2] not in '123456':
            print("Unexpected var name:", var, file=sys.stderr)
            return 0
    return 1

def testDij(widgetname, **aijs):
    if checkNames(aijs):
        dct = {}
        for i in range(1, 4):
            for j in range(i, 7):
                aijname = "d%d%d" % (i,j)
                wijname = "%d,%d" % (i-1, j-1)
                dct[wijname] = aijs.get(aijname, 0.0)
        return gtkMultiFloatCompare(dct, widgetbase=base+";"+widgetname+":dijk")

def sensitiveDij(widgetname, **aijs):
    if checkNames(aijs):
        for i in range(1, 4):
            for j in range(i, 7):
                aijname = "d%d%d" % (i,j)
                wijname = "%d,%d" % (i-1, j-1)
                nominal = aijs.get(aijname, 0)
                fullwname = base+";"+widgetname+":dijk:"+wijname
                actual = is_sensitive(fullwname)
                if actual != nominal:
                    print("Sensitization test failed for", \
                          fullwname, file=sys.stderr)
                    return 0
        return 1

