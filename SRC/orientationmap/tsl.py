# -*- python -*-
# $RCSfile: tsl.py,v $
# $Revision: 1.24 $
# $Author: langer $
# $Date: 2012/03/07 16:27:34 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import progress
from ooflib.SWIG.common import corientation
from ooflib.SWIG.orientationmap import orientmapdata
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import utils
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
import math
import os.path

class DataPoint:
    def __init__(self, position, angletuple, phasename):
        self.position = position
        self.angle = corientation.COrientBunge(*angletuple)
        self.phasename = phasename
    def euler(self):
        return self.angle.abg()
    def __repr__(self):
        return "(%s, %s)" % (self.position[0], self.position[1])
    def __cmp__(self, other):
        sy = self.position[1]
        oy = other.position[1]
        if sy < oy:
            return -1
        if sy > oy:
            return 1
        return cmp(self.position[0], other.position[0])

## getrows() splits a list of DataPoints into lists in which x is
## monotonically increasing.

def getrows(datapts):
    datapts.sort()
    row = [datapts[0]]
    for pt in datapts[1:]:
        if pt.position[0] > row[-1].position[0]:
            row.append(pt)
        else:
            yield row
            row = [pt]
    yield row

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class TSLreaderBase(orientmapdata.OrientMapReader):
    def __init__(self, flip_x, flip_y, angle_offset):
        self.flip_x = flip_x
        self.flip_y = flip_y
        self.angle_offset = angle_offset
        self.phaselists = {}
        orientmapdata.OrientMapReader.__init__(self)
    def read(self, filename):
        tslfile = file(filename, "r")
        prog = progress.getProgress(os.path.basename(filename),
                                    progress.DEFINITE)
        try:
            od = self._read(tslfile, prog)
        finally:
            prog.finish()
        return od


    def _read(self, tslfile, prog):
        data, hexgrid = self.readData(tslfile, prog)
        npts = len(data)
        rows = list(getrows(data)) # sorts data
        if hexgrid is None:
            # readData didn't set hexgrid.  The grid is hexagonal if
            # the first two rows don't start at the same x.
            hexgrid = rows[0][0].position[0] != rows[1][0].position[0]

        if hexgrid:
            # Throw out every other row.
            reporter.warn(
                "Converting hexagonal lattice to rectangular"
                " by discarding alternate rows.")
            rows = rows[::2]            # discard odd numbered rows

        nx = len(rows[0])
        ny = len(rows)
        count = 0
        for row in rows:
            count += 1
            if len(row) != nx:
                raise ooferror.ErrUserError(
                    "Orientation map data appears to be incomplete.\n"
                    "len(row 0)=%d len(row %d)=%d" % (nx, count, len(row)))

        # TSL puts the origin at the top left, so it's using a left
        # handed coordinate system!  If flip_y==True, fix that.  Also,
        # make sure there are no negative x or y values.
        ymax = rows[-1][0].position[1]
        ymin = rows[0][0].position[1]
        xmax = rows[0][-1].position[0]
        xmin = rows[0][0].position[0]
        for row in rows:
            for point in row:
                if self.flip_x:
                    point.position[0] = xmax - point.position[0]
                else:
                    point.position[0] = point.position[0] - xmin
                if self.flip_y:
                    point.position[1] = ymax - point.position[1]
                else:
                    point.position[1] = point.position[1] - ymin
    
        # If flipped, the rows are still ordered top to bottom, but
        # the coordinates increase bottom to top.

        # pixel size
        dx = abs(rows[0][1].position[0] - rows[0][0].position[0])
        dy = abs(rows[0][0].position[1] - rows[1][0].position[1])
        pxlsize = primitives.Point(dx, dy)
        
        width = abs(rows[0][0].position[0] - rows[0][-1].position[0])
        height = abs(rows[0][0].position[1] - rows[-1][0].position[1])
        # If we assume that the points are in the centers of the
        # pixels, then the actual physical size is one pixel bigger
        # than the range of the xy values.
        size = primitives.Point(width, height) + pxlsize

        od = orientmapdata.OrientMap(primitives.iPoint(nx, ny), size)
        prog.setMessage("%d/%d orientations" % (0, npts))
        count = 0
        for row in rows:
            for datum in row:
                ij = primitives.iPoint(
                    int(round(datum.position[0]/pxlsize[0])),
                    int(round(datum.position[1]/pxlsize[1])))
                try:
                    self.phaselists[datum.phasename].append(ij)
                except KeyError:
                    self.phaselists[datum.phasename] = [ij]
                self.set_angle(od, ij, datum.euler())
                prog.setMessage("%d/%d orientations" % (count,npts))
                prog.setFraction(float(count)/npts)
                count += 1
                if prog.stopped():

                    return None
        prog.finish()
        return od

    ## postProcess is called after the orientation data has been
    ## assigned to a Microstructure.
    def postProcess(self, microstructure):
        phasenames = self.phaselists.keys()
        phasenames.sort()
        for phasename in phasenames:
            orientmapdata.addPixelsToGroup(microstructure, phasename,
                                           self.phaselists[phasename])

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## TODO: Use grain ID in column 9 to form pixel groups.

class TSLreader(TSLreaderBase):
    def readData(self, tslfile, prog):
        count = 1                       # line counter
        lines = tslfile.readlines()
        nlines = len(lines)
        data = utils.ReservableList(nlines)
        angletype = None
        for line in lines:
            if line[0] == '#':
                if line.startswith("Column 1-3", 2):
                    if "radians" in line:
                        angletype = "radians"
                    else:
                        angletype = "degrees"
            else:                       # line[0] != '#'
                substrings = line.split()
                if len(substrings) < 5:
                    raise ooferror.ErrUserError(
                        "Too few numbers in line %d of %s" 
                        % (count, tslfile.name))
                values = map(float, substrings[:5])
                if angletype == "radians":
                    angles = values[:3]
                    angles[0] = angles[0] - math.radians(self.angle_offset)
                elif angletype == "degrees":
                    angles[0] = angles[0] - self.angle_offset
                    angles = map(math.radians, values[:3])
                else:
                    raise ooferror.ErrDataFileError(
                        "Angle type not specified in TSL data file")
                data.append(DataPoint(
                    primitives.Point(values[3], values[4]), # position
                    angles,
                    ' '.join(substrings[10:])))    # phase name
            count += 1      # count actual file lines, comments and all
            prog.setMessage("read %d/%d lines" % (count, nlines))
            prog.setFraction(float(count)/nlines)
        npts = len(data)
        debug.fmsg("read %d lines, %d data points" % (count, npts))
        return data, None       # None ==> hexgrid not detected yet

orientmapdata.OrientMapRegistration(
    'TSL', TSLreader,
    ordering=2,
    params=[
        parameter.BooleanParameter(
            'flip_x', False, tip='Flip data, swapping x and -x.'),
        parameter.BooleanParameter(
            'flip_y', True, tip='Flip data, swapping y and -y.'),
        parameter.FloatParameter(
            'angle_offset', 0,
            tip='Subtract this angle (in degrees) from phi1.')
        ],
    tip="TSL .ang file (old format)")
        

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class TSLreader2(TSLreaderBase):
    def readData(self, tslfile, prog):
        count = 1
        lines = tslfile.readlines()
        nlines = len(lines)
        data = utils.ReservableList(nlines)
        hexgrid = False
        for line in lines:
            if line[0] == '#':  # line is in the header
                if line.startswith('# GRID: HexGrid'):
                    hexgrid = True
            else:               # line is not a header line
                substrings = line.split()
                if len(substrings) < 5:
                    raise ooferror.ErrUserError(
                        "Not enough columns in line %d of %s"
                        % (count, tslfile.name))
                if len(substrings) >= 8:
                    phase = substrings[7]
                else:
                    phase = 'phase0'
                values = map(float, substrings[:5])
                position = primitives.Point(values[3], values[4])
                angles = values[:3]
                angles[0] = angles[0] - math.radians(self.angle_offset)
                data.append(DataPoint(position, angles, 'phase'+phase))
            count += 1
            prog.setMessage("read %d/%d lines" % (count, nlines))
            prog.setFraction(float(count)/nlines)
        debug.fmsg("read %d lines, %d data points" % (count, len(data)))
        return data, hexgrid


orientmapdata.OrientMapRegistration(
    'TSL2', TSLreader2,
    ordering=2.1,
    params=[
        parameter.BooleanParameter(
            'flip_x', False, tip='Flip data, swapping x and -x.'),
        parameter.BooleanParameter(
            'flip_y', True, tip='Flip data, swapping y and -y.'),
        parameter.FloatParameter(
            'angle_offset', 90, default=0,
            tip='Subtract this angle (in degrees) from phi1.')
        ],
    tip="TSL .ang file with phase id in column 8")
