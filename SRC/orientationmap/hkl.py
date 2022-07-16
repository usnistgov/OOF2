# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import progress
from ooflib.SWIG.engine import corientation
from ooflib.SWIG.orientationmap import orientmapdata
from ooflib.common import debug
from ooflib.common import primitives
import math
import os.path

from ooflib.common.utils import stringsplit

class HKLreader(orientmapdata.OrientMapReader):
    def __init__(self):
        self.phaselists = {}
        orientmapdata.OrientMapReader.__init__(self)
    def read(self, filename):
        hklfile = file(filename, "r")
        lineiter = iter(hklfile)
        line = next(lineiter)
        while not line.startswith('XCells'):
            line = next(lineiter)
        xcells = int(stringsplit(line)[1])
        line = next(lineiter)
        ycells = int(stringsplit(line)[1])
        line = next(lineiter)
        xstep = float(stringsplit(line)[1])
        line = next(lineiter)
        ystep = float(stringsplit(line)[1])
        line = next(lineiter)


        od = orientmapdata.OrientMap(
            primitives.iPoint(xcells, ycells),
            primitives.Point(xcells*xstep, ycells*ystep))
        
        while not stringsplit(line)[0] == 'Phase':
            line = next(lineiter)
        prog = progress.getProgress(os.path.basename(filename),
                                    progress.DEFINITE)
        try:
            count = 0
            npts = xcells*ycells
            for line in lineiter:
                vals = stringsplit(line)
                phase = vals[0]
                x = float(vals[1])
                y = float(vals[2])
                angles = list(map(float, vals[5:8]))
                mad = float(vals[8])  # mean angular deviation
                ij = primitives.iPoint(
                    int(round(x/xstep)),
                    ycells-1-int(round(y/ystep)))
                try:
                    self.phaselists[phase].append(ij)
                except KeyError:
                    self.phaselists[phase] = [ij]
                self.set_angle(
                    od, ij, 
                    corientation.COrientBunge(*list(map(math.radians, angles))))
                prog.setFraction(float(count)/npts)
                prog.setMessage("%d/%d orientations" % (count, npts))
                count += 1
                if prog.stopped():
                    return None
        finally:
            prog.finish()
        return od

    ## postProcess is called after the orientation data has been
    ## assigned to a Microstructure.
    def postProcess(self, microstructure):
        phasenames = sorted(list(self.phaselists.keys()))
        for phasename in phasenames:
            orientmapdata.addPixelsToGroup(microstructure, 'Phase_' + phasename,
                                           self.phaselists[phasename])

orientmapdata.OrientMapRegistration(
    'HKL', HKLreader,
    ordering=3,
    tip='HKL channel text file')
