# -*- python -*-
# $RCSfile: genericreader.py,v $
# $Revision: 1.7 $
# $Author: langer $
# $Date: 2012/04/18 20:26:13 $

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
from ooflib.common import enum
from ooflib.common import primitives
from ooflib.common import utils
from ooflib.common.IO import formatchars
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.engine.IO import orientationmatrix
import math
import os.path

class DataPoint(object):
    def __init__(self, position, angletuple, groups):
        self.position = position
        self.angletuple = angletuple
        self.groups = groups    # list of groups to which this pixel belongs
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
    assert len(datapts) > 0
    datapts.sort()
    row = [datapts[0]]
    for pt in datapts[1:]:
        if pt.position[0] > row[-1].position[0]:
            row.append(pt)
        else:
            yield row
            row = [pt]
    yield row

class AngleUnits(enum.EnumClass('Radians', 'Degrees')):
    pass

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class GenericReader(orientmapdata.OrientMapReader):
    def __init__(self, comment_character, separator,
                 angle_column, angle_type, angle_units, angle_offset, 
                 xy_column, scale_factor, flip_x, flip_y, groups):
        self.comment_character = comment_character
        self.separator = separator
        self.angle_type = angle_type
        self.angle_units = angle_units
        self.angle_offset = angle_offset
        self.angle_column = angle_column
        self.xy_column = xy_column
        self.scale_factor = scale_factor
        self.flip_x = flip_x
        self.flip_y = flip_y
        # groups is a list of (name template, column number) tuples.
        # Each pixel will be put in a group whose name is the template
        # applied to the value of the data in the associated column.
        self.groups = groups
        # If any of the templates don't contain '%s', append it to
        # them.  Otherwise all of the pixels will end up in the same
        # group.
        for i, grp in enumerate(self.groups):
            if grp[0].find('%s') == -1:
                self.groups[i] = (grp[0] + '%s', grp[1])
        
        self.groupmembers = {}  # lists of coords for each group
        orientmapdata.OrientMapReader.__init__(self)
    def read(self, filename):
        datafile = file(filename, "r")
        prog = progress.getProgress(os.path.basename(filename),
                                    progress.DEFINITE)
        try:
            od = self._read(datafile, prog)
        finally:
            prog.finish()
        return od
    
    def _read(self, datafile, prog):
        # readData gets data from the file, but does no processing
        data = self.readData(datafile, prog)
        rows = list(getrows(data)) # sorts data
        # The grid is hexagonal if the first two rows don't start at the same x.
        if rows[0][0].position[0] != rows[1][0].position[0]:
            # Throw out every other row.
            reporter.warn(
                "Converting hexagonal lattice to rectangular"
                " by discarding alternate rows.")
            rows = rows[::2]    # discard odd numbered rows

        # Check that all rows are the same length, and flip the
        # coordinates if requested.
        nx = len(rows[0])
        ny = len(rows)
        ymax = rows[-1][0].position[1]
        ymin = rows[0][0].position[1]
        xmax = rows[0][-1].position[0]
        xmin = rows[0][0].position[0]
        count = 0
        for row in rows:
            count += 1
            if len(row) != nx:
                raise ooferror.ErrUserError(
                    "Orientation map data appears to be incomplete.\n"
                    "len(row 0)=%d len(row %d)=%d" % (nx, count, len(row)))
            for point in row:
                if self.flip_x:
                    point.position[0] = xmax - point.position[0]
                else:
                    point.position[0] = point.position[0] - xmin
                if self.flip_y:
                    point.position[1] = ymax - point.position[1]
                else:
                    point.position[1] = point.position[1] - ymin

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

        npts = len(rows)*len(rows[0])

        od = orientmapdata.OrientMap(primitives.iPoint(nx, ny),
                                     size*self.scale_factor)
        prog.setMessage("%d/%d orientations" % (0, npts))
        count = 0
        for row in rows:
            for datum in row:
                ij = primitives.iPoint(
                    int(round(datum.position[0]/pxlsize[0])),
                    int(round(datum.position[1]/pxlsize[1])))
                for groupname in datum.groups:
                    try:
                        self.groupmembers[groupname].append(ij)
                    except KeyError:
                        self.groupmembers[groupname] = [ij]
                if self.angle_units == 'Degrees':
                    offset = math.radians(self.angle_offset)
                    angleargs = datum.angletuple
                else:           # angle units are Radians
                    offset = self.angle_offset
                    # All Orientation subclasses that take angle args
                    # assume that they're in degrees.  They have a
                    # static radians2Degrees method that converts the
                    # angle args from radians to degrees.
                    angleargs = self.angle_type.radians2Degrees(
                        *datum.angletuple)
                # Create an instance of the Orientation subclass.
                orient = self.angle_type(*angleargs)
                if self.angle_offset != 0:
                    orient = orient.rotateXY(self.angle_offset)

                # Insert this point into the OrientMap object.
                self.set_angle(od, ij, orient.corient)

                prog.setMessage("%d/%d orientations" % (count, npts))
                prog.setFraction(float(count)/npts)
                count += 1
                if prog.stopped():
                    return None
        return od

    def readData(self, datafile, prog):
        count = 1
        lines = datafile.readlines()
        nlines = len(lines)
        data = utils.ReservableList(nlines)
        # The number of angle components to read is the number of
        # parameters in the Registration for the selected Orientation
        # subclass.
        for reg in orientationmatrix.Orientation.registry:
            if reg.subclass == self.angle_type:
                nAngleComps = len(reg.params)
                break

        xycol0 = self.xy_column - 1   # UI uses fortran indexing
        xycol1 = xycol0 + 2           # TODO: Are there 3D EBSD files?
        acol0 = self.angle_column - 1 # UI uses fortran indexing
        acol1 = acol0 + nAngleComps

        # Look for the last non-blank non-comment line in the file,
        # and examine it to find out what data lines look like.  This
        # information will be used to skip the header lines at the top
        # of the file.

        for i in xrange(len(lines)-1, -1, -1):
            line = lines[i].strip()
            if line and line[0] != self.comment_character:
                words = self.separator.split(line)
                nwords = len(words)
                lastline = i
                break
                
        # Loop over the lines in reverse, and stop at the first one
        # that can't be handled.  That will be the last header line.
        for i in xrange(lastline, -1, -1):
            line = lines[i]
            if line[0] != self.comment_character:  # Skip comments
                cols = self.separator.split(line)
                if len(cols) != nwords:
                    break
                try:
                    angletuple = map(float, cols[acol0:acol1])
                    position = primitives.Point(
                        *map(float, cols[xycol0:xycol1]))
                except ValueError: # Ran into the header.  Quit reading.
                    break
                grps = [template.replace('%s', cols[gcol-1])
                        for (template, gcol) in self.groups]
                data.append(DataPoint(position, angletuple, grps))
                    
                    
            count += 1          # count actual lines, comments and all
            prog.setMessage("read %d/%d lines" % (count, nlines))
            prog.setFraction(float(count)/nlines)
        npts = len(data)
        reporter.report(
            "Read %d lines, found %d data points" % (len(lines), npts))
        return data

    ## postProcess is called after the orientation data has been
    ## assigned to a Microstructure.
    def postProcess(self, microstructure):
        groupnames = self.groupmembers.keys()
        groupnames.sort()
        for groupname in groupnames:
            orientmapdata.addPixelsToGroup(microstructure, groupname,
                                           self.groupmembers[groupname])

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class GroupColumnParameter(parameter.ListOfStringIntTuplesParameter):
    pass

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

orientmapdata.OrientMapRegistration(
    'Generic',
    GenericReader,
    ordering=0,
    params=[
        parameter.StringParameter(
            "comment_character", '#',
            tip="Skip input lines beginning with this character."),
        parameter.RegisteredParameter(
            "separator", 
            formatchars.InputSeparator,
            formatchars.WhiteSpaceSeparator(),
            tip="How columns are divided in the input file."),
        parameter.PositiveIntParameter(
            'angle_column', 1,
            tip='First column of angle data.'),
        parameter.MetaRegisteredParameter(
            'angle_type', orientationmatrix.Orientation,
            orientationmatrix.Bunge,
            tip="The way in which orientations are specified in the input file."
            ),
        enum.EnumParameter(
            'angle_units', AngleUnits, 'Radians',
            tip="The units used for angles in the input file."),
        parameter.FloatParameter(
            'angle_offset', 0,
            tip="An xy-plane rotation to apply to all input orientations,"
            " in degrees.  In the Abg format, the angle is added to gamma."
            " In Bunge, it's subtracted from phi1."),
        parameter.PositiveIntParameter(
            'xy_column', 4, tip='First column of position data.'),
        parameter.FloatParameter(
            'scale_factor', 1.0,
            tip="All x and y values will be multiplied by this factor."),
        parameter.BooleanParameter(
            'flip_x', False, tip='Flip data in the x direction.'),
        parameter.BooleanParameter(
            'flip_y', True, tip='Flip data in the y direction.'),
        GroupColumnParameter(
            "groups", [],
            tip=
            "Templates for creating pixel groups from column data. "
            "Pixels with different values in the column will be put into "
            "different pixel groups.  A '%s' in the groupname will be "
            "replaced by the contents of the column.")
        ],
    tip="Generic EBSD data reader.")
