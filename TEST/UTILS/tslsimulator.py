# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Generate a TSL data file for testing OOF2.

import getopt
import math
import random
import sys

def generate(phile, nx, ny, width, height, anglegenerator):
    print("""# Header: tslsimulator.py
# 
# Column 1-3: phi1, PHI, phi2 (orientation of point in radians)
# Column 4-5: x, y (coordinates of point in microns)
# Column 6:   IQ (image quality)
# Column 7:   CI (confidence index)
# Column 8:   Fit (degrees)
# Column 9:   Grain ID (integer)
# Column 10:  edge (1 for grains at edges of scan and 0 for interior grains)
# Column 11:  phase name """,
file=phile)
    dx = width/(nx-1.)
    dy = height/(ny-1.)
    x = 0
    y = 0
    for j in range(ny):
        y = j*dy
        for i in range(nx):
           x = i*dx
           phi0, theta, phi1, groupname = anglegenerator(x, y)
           print(phi0, theta, phi1, x, y, end=' ', file=phile)
           print(f"0.0 1.0 0.0 1 1 {groupname}", file=phile)


class ConstantAngle(object):
    def __init__(self, phi0, theta, phi1):
        self.phi0 = math.radians(phi0)
        self.theta = math.radians(theta)
        self.phi1 = math.radians(phi1)
    def __call__(self, x, y):
        return self.phi0, self.theta, self.phi1, "constant"

class Gauss(object):
    def __init__(self, phi0, theta, phi1, spread):
        self.phi0 = math.radians(phi0)
        self.theta = math.radians(theta)
        self.phi1 = math.radians(phi1)
        self.spread = math.radians(spread)
    def __call__(self, x, y):
        return (self.phi0 + random.gauss(0, self.spread),
                self.theta + random.gauss(0, self.spread),
                self.phi1, #+ random.gauss(0, self.spread)
                "gauss"
                )

class TwoAngles(object):
    def __init__(self, phi0A, thetaA, phi1A, phi0B, thetaB, phi1B):
        self.phi0A = math.radians(phi0A)
        self.thetaA = math.radians(thetaA)
        self.phi1A = math.radians(phi1A)
        self.phi0B = math.radians(phi0B)
        self.thetaB = math.radians(thetaB)
        self.phi1B = math.radians(phi1B)
    def __call__(self, x, y):
        if x > y:
            return self.phi0A, self.thetaA, self.phi1A, "bottom"
        else:
            return self.phi0B, self.thetaB, self.phi1B, "top"

if __name__=='__main__':
    opts, args = getopt.getopt(sys.argv[1:], "f:x:y:w:h:m:",
                               ["file=", "nx=", "ny=", "width=", "height=",
                                "mode="])
    phile = sys.stdout
    nx = 10
    ny = 10
    width = 1.
    height = 1.
    mode = ConstantAngle(0, 0, 0)
    
    for o, v in opts:
        if o in ("-f", "--file"):
            phile = open(v, 'w')
        if o in ("-x", "--nx"):
            nx = int(v)
        if o in ("-y", "--ny"):
            ny = int(v)
        if o in ("-w", "--width"):
            width = float(v)
        if o in ("-h", "--height"):
            height = float(v)
        if o in ("-m", "--mode"):
            mode = eval(v)

    generate(phile, nx, ny, width, height, mode)
    phile.close()

    
           
