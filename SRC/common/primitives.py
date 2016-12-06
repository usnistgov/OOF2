# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## Classes representing primitive graphics objects.  Each class should
## have an enclosing_rectangle() function which returns a Rectangle.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import ooferror
from ooflib.common import debug
from ooflib.common import utils
from ooflib.common.IO import parameter
import math
import struct
import types

## TODO OPT: It might be better to have two separate classes, Point2
## and Point3, and set Point to Point2 or Point3 according to the
## value of config.dimension.  That would reduce the number of "if"s.

class Point:
    """
    Point class represents a point in 2 dimensions.  It is more or
    less redundant with oofcpp.Coord, but doesn't have the overhead of
    calling C++ routines for simple operations.  Python graphics
    routines should generally be prepared to receive either Point or
    oofcpp.Coord.
    """
    def __init__(self, x, y, z=0.):
        # This should possibly coerce x and y to floats, since other
        # routines might want to take their ratio.  This *isn't* done
        # here, because it might be slow.
        self.x = x
        self.y = y
        if config.dimension() == 3:
            self.z = z
            
    def __getitem__(self, idx):
        if idx==0: return self.x
        if idx==1: return self.y
        if config.dimension() == 3 and idx==2: return self.z
        raise IndexError
    
    def __setitem__(self, idx, val):
        if idx==0:
            self.x = val
        elif idx==1:
            self.y = val
        elif config.dimension() == 3 and idx==2:
            self.z = val
        else:
            raise IndexError

    def __len__(self):
        return config.dimension()

    # TODO 3D: generalize the rest of this class to 3d....
    def enclosing_rectangle(self):
        if config.dimension() == 2:
            return Rectangle(self, self)
        elif config.dimension() == 3:
            return RectangularPrism(self, self)

    # Multiply accepts mixed point/ipoint objects for dot products,
    # and preserves i-ness if possible.
    def __mul__(self, other):
        if config.dimension() == 2:
            if type(other)==types.InstanceType and \
               (issubclass(other.__class__, self.__class__) or
                issubclass(self.__class__, other.__class__) ):
                return self.x*other.x+self.y*other.y
            elif type(other)==types.FloatType:
                return Point(other*self.x, other*self.y)
            elif type(other)==types.IntType:
                # Return whatever class you already are.
                return self.__class__(other*self.x, other*self.y)
        elif config.dimension() == 3:
            if type(other)==types.InstanceType and \
               (issubclass(other.__class__, self.__class__) or
                issubclass(self.__class__, other.__class__) ):
                return self.x*other.x+self.y*other.y+self.z*other.z
            elif type(other)==types.FloatType:
                return Point(other*self.x, other*self.y, other*self.z)
            elif type(other)==types.IntType:
                # Return whatever class you already are.
                return self.__class__(other*self.x, other*self.y, other*self.z)
        raise TypeError

    def cross(self, other):
        if config.dimension() == 2:
            return self.x*other.y - self.y*other.x
        elif config.dimension() == 3:
            return Point(self.y*other.z-self.z*other.y,
                         self.z*other.x-self.x*other.z,
                         self.x*other.y-self.y*other.x)

    # Power defined only for squaring -- finds the squared magnitude.
    def __pow__(self, other):
        if other!=2:
            print "Power operation only defined for exponent equal to 2."
        if config.dimension() == 2:
            return self.x*self.x+self.y*self.y
        elif config.dimension() == 3:
            return self.x*self.x+self.y*self.y+self.z*self.z

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        # other may not be a Point, so used [0] instead of .x
        if config.dimension() == 2:
            return self.__class__(self.x + other[0], self.y + other[1])
        elif config.dimension() == 3:
            return self.__class__(self.x + other[0], self.y + other[1], self.z + other[2])

    def __sub__(self, other):
        if config.dimension() == 2:
            return self.__class__(self.x - other[0], self.y - other[1])
        elif config.dimension() == 3:
            return self.__class__(self.x - other[0], self.y - other[1], self.z - other[2])            

    def __neg__(self):
        if config.dimension() == 2:
            return self.__class__(-self.x, -self.y)
        elif config.dimension() == 3:
            return self.__class__(-self.x, -self.y, -self.z)

    def __div__(self, other):
        if config.dimension() == 2:
            return Point(self.x/other, self.y/other)
        elif config.dimension() == 3:
            return Point(self.x/other, self.y/other, self.z/other)

    def __hash__(self):
        # Comparison operators are written in terms of __getitem__ so that
        # comparison to Coords and ICoords will work.
        if config.dimension() == 2:
            return hash((self.x, self.y))
        elif config.dimension() == 3:
            return hash((self.x, self.y, self.z))

    def __cmp__(self, other):
        try:
            if self[0] < other[0]: return -1
            if self[0] > other[0]: return 1
            if self[1] < other[1]: return -1
            if self[1] > other[1]: return 1
            if config.dimension() == 3:
                if self[2] < other[2]: return -1
                if self[2] > other[2]: return 1
            return 0
        except:
            return 1

    def __lt__(self, other):
        try:
            if self[0] < other[0]: return 1
            if self[0] > other[0]: return 0
            if self[1] < other[1]: return 1
            if self[1] > other[1]: return 0
            if config.dimension() == 3:
                if self[2] < other[2]: return 1
                if self[2] > other[2]: return 0
        except:
            return 0

    def __gt__(self, other):
        try:
            if self[0] > other[0]: return 1
            if self[0] < other[0]: return 0
            if self[1] > other[1]: return 1
            if self[1] < other[1]: return 0
            if config.dimension() == 3:
                if self[2] > other[2]: return 1
                if self[2] < other[2]: return 0
        except:
            return 1

    def __eq__(self, other):
        try:
            if config.dimension() == 2:
                return self[0]==other[0] and self[1]==other[1]
            if config.dimension() == 3:
                return self[0]==other[0] and self[1]==other[1] and self[2]==other[2]
        except:
            return 0

    def __ne__(self, other):
        try:
            if config.dimension() == 2:
                return self[0]!=other[0] or self[1]!=other[1]
            if config.dimension() == 3:
                return self[0]!=other[0] or self[1]!=other[1] or self[2]!=other[2]
        except:
            return 1

    def __repr__(self):
        if config.dimension() == 2:
            return "Point(%s,%s)" % (self.x, self.y)
        elif config.dimension() == 3:
            return "Point(%s,%s,%s)" % (self.x, self.y, self.z)

utils.OOFdefine('Point', Point)

class PointParameter(parameter.Parameter):
    types = (Point,)

    def __init__(self, name, value=Point(0.,0.), default=None, tip=None):
        parameter.Parameter.__init__(self, name, value, default, tip)
    structfmt = '>dd'
    structlen = struct.calcsize(structfmt)

    def binaryRepr(self, datafile, value):
        return struct.pack(PointParameter.structfmt, value.x, value.y)

    def binaryRead(self, parser):
        b = parser.getBytes(PointParameter.structlen)
        (x,y) = struct.unpack(PointParameter.structfmt, b)
        return Point(x,y)

    def valueDesc(self):
        return "A <link linkend='Object-Point'><classname>Point</classname></link> object (eg, <userinput>Point(1.1, 2.0)</userinput>)."

class ListOfPointsParameter(parameter.Parameter):

    def __init__(self, name, value=None, default=[], tip=None):
        parameter.Parameter.__init__(self, name, value, default, tip)

    def checker(self, x):
        if type(x) is not types.ListType:
            parameter.raiseTypeError(type(x), "list of Points")
        for y in x:
            if not isinstance(y, Point):
                parameter.raiseTypeError("list of %s" % type(y),
                                         "list of Points")
    def valueDesc(self):
        return "A list of <link linkend='Object-Point'><classname>Point</classname></link> objects."


class iPoint(Point):
    "A Point made up of integers. Arithmetic may convert it to a regular Point."
    # Should probably not be derived from Point, for efficiency and so
    # that arithmetic operators don't convert iPoints to Points.
    def __init__(self, x, y, z=0):
        if config.dimension() == 2:
            Point.__init__(self, int(math.floor(x)), int(math.floor(y)))
        elif config.dimension() == 3:
            Point.__init__(self, int(math.floor(x)), int(math.floor(y)), int(math.floor(z)))
    def __repr__(self):
        if config.dimension() == 2:
            return "iPoint(%d,%d)" % (self.x, self.y)
        elif config.dimension() == 3:
            return "iPoint(%d,%d,%d)" % (self.x, self.y, self.z)

class iPointParameter(parameter.Parameter):
    types = (iPoint,)
    def __init__(self, name, value=iPoint(0,0), default=None, tip=None):
        parameter.Parameter.__init__(self, name, value, default, tip)
    structfmt = '>ii'
    structlen = struct.calcsize(structfmt)
    def binaryRepr(self, datafile, value):
        return struct.pack(iPointParameter.structfmt, value.x, value.y)
    def binaryRead(self, parser):
        b = parser.getBytes(iPointParameter.structlen)
        (x,y) = struct.unpack(iPointParameter.structfmt, b)
        return iPoint(x,y)
    def valueDesc(self):
        return "An <link linkend='Object-iPoint'><classname>iPoint</classname></link> (integer Point) object (eg <userinput>iPoint(1,2)</userinput>)."


utils.OOFdefine('iPoint', iPoint)

def pontify(ptlist):
    # Convert a Thing of Stuff to a Thing of Points.  Thing is
    # probably Curve or Polygon, and Stuff is probably MasterCoord or
    # Coord, but it doeesn't really matter.  Points can be faster to
    # use since they don't have any swig overhead.
    if config.dimension() == 2:
        if type(ptlist) == types.ListType:
            return [Point(pt[0], pt[1]) for pt in ptlist]
        return ptlist.__class__([Point(pt[0], pt[1]) for pt in ptlist])
    elif config.dimension() == 3:
        if type(ptlist) == types.ListType:
            return [Point(pt[0], pt[1], pt[2]) for pt in ptlist]
        return ptlist.__class__([Point(pt[0], pt[1], pt[2]) for pt in ptlist])

## Documentation for Point and iPoint classes

from ooflib.common.IO import xmlmenudump
xmlmenudump.XMLObjectDoc('iPoint',
                         xmlmenudump.loadFile('DISCUSSIONS/common/object/ipoint.xml'))

xmlmenudump.XMLObjectDoc('Point',
                         xmlmenudump.loadFile('DISCUSSIONS/common/object/point.xml'))


######################

class Rectangle:
    """
    A Rectangle is a pair of points at diagonally opposite corners.
    """
    def __init__(self, pt0, pt1):
        # Don't assume that args pt0 and pt1 have .x and .y data
        self.lowleft = Point(min(pt0[0], pt1[0]), min(pt0[1], pt1[1]))
        self.upright = Point(max(pt0[0], pt1[0]), max(pt0[1], pt1[1]))
    def enclosing_rectangle(self):
        return self
    def xmin(self):
        return self.lowleft.x
    def xmax(self):
        return self.upright.x
    def ymin(self):
        return self.lowleft.y
    def ymax(self):
        return self.upright.y
    def lowerleft(self):
        return self.lowleft
    def upperright(self):
        return self.upright
    def swallow(self, obj):
        """
        Expand a Rectangle to include the given obj.  The obj must have
        an enclosing_rectangle() function.
        """
        try:
            encl = obj.enclosing_rectangle()
        except AttributeError:
            print obj
            raise
        self.lowleft.x = min(self.lowleft.x, encl.xmin())
        self.lowleft.y = min(self.lowleft.y, encl.ymin())
        self.upright.x = max(self.upright.x, encl.xmax())
        self.upright.y = max(self.upright.y, encl.ymax())
    def area(self):
        return (self.xmax()-self.xmin())*(self.ymax()-self.ymin())
    def __repr__(self):
        return "Rectangle(%s,%s)" % (`self.lowleft`, `self.upright`)

utils.OOFdefine('Rectangle', Rectangle)

class iRectangle(Rectangle):
    def __init__(self, pt0, pt1):
        self.lowleft = iPoint(min(pt0[0], pt1[0]), min(pt0[1], pt1[1]))
        self.upright = iPoint(max(pt0[0], pt1[0]), max(pt0[1], pt1[1]))
    def points(self):
        return [iPoint(i,j)
                for i in range(self.lowleft.x, self.upright.x)
                for j in range(self.lowleft.y, self.upright.y)]
    def inclusivePoints(self):
        return [iPoint(i,j)
                for i in range(self.lowleft.x, self.upright.x+1)
                for j in range(self.lowleft.y, self.upright.y+1)]

utils.OOFdefine('iRectangle', Rectangle)

# new classes for 3D - or we could generalize the classes above, but
# the terminology would be confusing
class RectangularPrism:
    """
    A Rectangular is a pair of 3D points at diagonally opposite corners.
    """
    def __init__(self, pt0, pt1):
        # Don't assume that args pt0 and pt1 have .x and .y data
        self.lowleftback = Point(min(pt0[0], pt1[0]), min(pt0[1], pt1[1]), min(pt0[2],pt1[2]))
        self.uprightfront = Point(max(pt0[0], pt1[0]), max(pt0[1], pt1[1]), max(pt0[2],pt1[2]))
    def enclosing_rectangle(self):
        return self
    def xmin(self):
        return self.lowleftback.x
    def xmax(self):
        return self.uprightfront.x
    def ymin(self):
        return self.lowleftback.y
    def ymax(self):
        return self.uprightfront.y
    def zmin(self):
        return self.lowleftback.z
    def zmax(self):
        return self.uprightfront.z
    def lowerleftback(self):
        return self.lowleftback
    def upperrightfront(self):
        return self.uprightfront
    def swallow(self, obj):
        """
        Expand a Rectangle to include the given obj.  The obj must have
        an enclosing_rectangle() function.
        """
        try:
            encl = obj.enclosing_rectangle()
        except AttributeError:
            print obj
            raise
        self.lowleftback.x = min(self.lowleftback.x, encl.xmin())
        self.lowleftback.y = min(self.lowleftback.y, encl.ymin())
        self.lowleftback.z = min(self.lowleftback.z, encl.zmin())
        self.uprightfront.x = max(self.uprightfront.x, encl.xmax())
        self.uprightfront.y = max(self.uprightfront.y, encl.ymax())
        self.uprightfront.z = max(self.uprightfront.z, encl.zmax())
    def volume(self):
        return (self.xmax()-self.xmin())*(self.ymax()-self.ymin())*(self.zmax()-self.zmin())
    def __repr__(self):
        return "RectangularPrism(%s,%s)" % (`self.lowleftback`, `self.uprightfront`)

utils.OOFdefine('RectangularPrism', RectangularPrism)

class iRectangularPrism(RectangularPrism):
    def __init__(self, pt0, pt1):
        self.lowleftback = iPoint(min(pt0[0], pt1[0]), min(pt0[1], pt1[1]), min(pt0[2],pt1[2]))
        self.uprightfront = iPoint(max(pt0[0], pt1[0]), max(pt0[1], pt1[1]), max(pt0[2],pt1[2]))
    def points(self):
        return [iPoint(i,j,k)
                for i in range(self.lowleftback.x, self.uprightfront.x)
                for j in range(self.lowleftback.y, self.uprightfront.y)
                for k in range(self.lowleftback.z, self.uprightfront.z)]
    def inclusivePoints(self):
        return [iPoint(i,j,k)
                for i in range(self.lowleftback.x, self.uprightfront.x+1)
                for j in range(self.lowleftback.y, self.uprightfront.y+1)
                for k in range(self.lowleftback.z, self.uprightfront.z+1)]

utils.OOFdefine('iRectangularPrism', RectangularPrism)

#################################

# Utility function for finding intersections between the segment
# p1->p2 and the segment p3->p4.  Used by Segment.intersectWith and
# Polygon.makeCompoundPolygon.

## TODO OPT: Move this to C++?  It looks like a lot of arithmetic for Python.
def _point_intersect(p1, p2, p3, p4):
    # Check endpoints explicitly first.  If we didn't do this here,
    # then intersections that were supposed to be exactly at endpoints
    # might not be (due to roundoff error) and checks for endpoint
    # intersections (such as in Polygon.intersections) might fail.
    if p1 == p3 or p1 == p4:
        return p1
    if p2 == p3 or p2 == p4:
        return p2

    # Guard against argument-order-induced round-off inconsistencies
    # by putting the arguments in standard order.
    if p1>p2:
        t=p1
        p1=p2
        p2=t

    if p3>p4:
        t=p3
        p3=p4
        p4=t
        
    x1 = p1.x;  y1 = p1.y
    x2 = p2.x;  y2 = p2.y
    x3 = p3.x;  y3 = p3.y
    x4 = p4.x;  y4 = p4.y

    denom = (y4-y3)*(x2-x1)-(x4-x3)*(y2-y1)
    if denom==0.0: return None # Lines are parallel.

    # Check for existence of an intersection -- this is necessary
    # because end-point-to-interior intersections can be missed due to
    # round-off if you do a bounds-check on the intersection point
    # after it has been computed.

    # Are p1 and p2 on the same side of p3->p4?  They are if the
    # cross-product has the same sign.
    c1 = (p4-p3).cross(p1-p3)
    c2 = (p4-p3).cross(p2-p3)
    p34mag = (p4-p3)**2
    
    if c1*c2 > 0:
        return None

    # Explicitly check the cross-product-is-zero "tee" case, which
    # otherwise is subject to roundoff in the generic point-finder.
    
    if c1==0: # p1 lies on p3->p4, do bounds check.
        f = ((p1-p3)*(p4-p3))/p34mag
        if (f>0) and (f<1):
            return p1

    if c2==0: # p2 lies on p3->p4.
        f = ((p2-p3)*(p4-p3))/p34mag
        if (f>0) and (f<1):
            return p2
        
        
    # Are p3 and p4 on the same side of p1->p2?
    c3 = (p2-p1).cross(p3-p1)
    c4 = (p2-p1).cross(p4-p1)
    p12mag = (p2-p1)**2

    if c3*c4 > 0:
        return None

    # Check "tee" case.
    
    if c3==0: # p3 lies on p1->p2.
        f = ((p3-p1)*(p2-p1))/p12mag
        if (f>0) and (f<1):
            return p3

    if c4==0: # p4 lies on p1->p2
        f = ((p4-p1)*(p2-p1))/p12mag
        if (f>0) and (f<1):
            return p4

    # Intersection is generic.  Find it.
    ua_nu = (x4-x3)*(y1-y3)-(y4-y3)*(x1-x3)
    ua = ua_nu/denom
    return p1 + ua*(p2-p1)


class Segment:
    """
    A Segment is a directed pair of points.
    """
    def __init__(self, end1, end2):
        self.startpt = end1
        self.endpt = end2
    def start(self):
        return self.startpt
    def end(self):
        return self.endpt
    def enclosing_rectangle(self):
        return Rectangle(self.startpt, self.endpt)
    def __repr__(self):
        return "Segment(%s, %s)" % (`self.startpt`, `self.endpt`)
    def __cmp__(self, other):
        try:
            if self.startpt < other.startpt: return -1
            if self.startpt > other.startpt: return 1
            if self.endpt < other.endpt: return -1
            if self.endpt > other.endpt: return 1
            return 0
        except AttributeError:
            return 1
    def __lt__(self, other):
        try:
            if self.startpt < other.startpt: return 1
            if self.startpt > other.startpt: return 0
            if self.endpt < other.endpt: return 1
            return 0
        except AttributeError:
            return 0
    def __gt__(self, other):
        try:
            if self.startpt > other.startpt: return 1
            if self.startpt < other.startpt: return 0
            if self.endpt > other.endpt: return 1
            return 0
        except AttributeError:
            return 0
    def __eq__(self, other):
        try:
            return self.startpt == other.startpt and self.endpt == other.endpt
        except AttributeError:
            return 0
    def __ne__(self, other):
        try:
            return self.startpt != other.startpt or self.endpt != other.endpt
        except AttributeError:
            return 1
    
    def __hash__(self):
        return hash((self.startpt, self.endpt))

    def intersection(self, other):
        return _point_intersect(self.startpt, self.endpt,
                                other.startpt, other.endpt)
        
utils.OOFdefine('Segment', Segment)

######################

class Curve:
    """
    A Curve is a directed list of points.  It can be used as a list of
    Segments, too.
    """
    def __init__(self, ptlist):
        if type(ptlist) == type(()):
            self.pts = list(ptlist)
        elif isinstance(ptlist, Curve):
            self.pts = ptlist.pts
        else:
            self.pts = ptlist
    def points(self):
        return self.pts
    def append(self, pt):
        self.pts.append(pt)
    def prepend(self, pt):
        self.pts = [pt] + self.pts
    def join(self, curve):
        self.pts += curve.pts
    def join_front(self, curve):
        self.pts = curve.pts + self.pts
    def __len__(self):
        """
        The length of a curve is the number of points it contains,
        not the number of segments!
        """
        return len(self.pts)
    def __getitem__(self, idx):
        return self.pts[idx]
    def __setitem__(self, idx, val):
        self.pts[idx] = val
    def __getslice__(self, i, j):
        return Curve(self.pts[i:j])
    class CurveEdges:
        """ Aux class used when viewing a Curve as a list of Segments. """
        def __init__(self, curve):
            self.curve = curve
        def __getitem__(self, idx):
            return Segment(self.curve.pts[idx], self.curve.pts[idx+1])
        def __len__(self):
            return len(self.curve.pts)-1
    def edges(self):
        return Curve.CurveEdges(self)
    def enclosing_rectangle(self):
        xmin = self.pts[0][0]
        xmax = xmin
        ymax = self.pts[0][1]
        ymin = ymax
        for pt in self.pts:
            xmin = min(xmin, pt[0])
            xmax = max(xmax, pt[0])
            ymin = min(ymin, pt[1])
            ymax = max(ymax, pt[1])
        return Rectangle(Point(xmin, ymin), Point(xmax, ymax))
## The above function could be written like this, but it would probably be
## substantially slower, since swallow(obj) converts obj to a Rectangle:
##    def enclosing_rectangle(self):
##        rect = self.pts[0].enclosing_rectangle()
##        for pt in self.pts[1:]:
##            rect.swallow(pt)
##        return rect
    def __repr__(self):
        return "Curve(%s)" % `self.pts`

utils.OOFdefine('Curve', Curve)

class Polygon(Curve):
    """
    A Polygon is created from a list of Points, but it can be also
    used as a list of Segments.  It's a closed Curve.
    """
    class PolygonEdges:
        """
        Auxiliary class used when treating a Polygon as a list of Segments.
        """
        def __init__(self, pgon):
            self.polygon = pgon
        def __getitem__(self, idx):
            if idx == len(self.polygon.pts) - 1:
                return Segment(self.polygon.pts[-1], self.polygon.pts[0])
            return Segment(self.polygon.pts[idx], self.polygon.pts[idx+1])
        def __len__(self):
            return len(self.polygon.pts)


    # Return all points where this polygon intersects the segment
    # joining p1 and p2, excluding points the points p1 and p2 themselves.
    def intersections(self, p1, p2):
        result = []
        # Manually include the wrap-around, so we get all segments.
        for (p3, p4) in utils.list_pairs( self.pts + [self.pts[0]] ):
            isec = _point_intersect(p1,p2,p3,p4)
            if isec is not None:
                # Exclude intersections resulting from end-point adjacency.
                if isec!=p1 and isec!=p2:
                    result.append(isec)
        return result

    # Find a segment which does not intersect either this polygon or
    # the other, and use it to join these two polygons.  This
    # mechanism does not care about polygon orientation, it just
    # unconditionally joins the polygons.  It turns two disjoint
    # polygons into one polygon composed of two blobs connected by a
    # zero-width isthmus.
    #
    # This is used to convert lists into compound polygons.  It's
    # called by makeCompoundPolygon (directly below), which in turn is
    # used by the fill_polygon method in canvasoutput.py.
    def joinPolygon(self, other):
        for (i, p1) in enumerate(self.pts):
            for (j, p2) in enumerate(other.pts):
                # See if the segment (p1, p2) intersects any side of
                # either polygon.
                if not (self.intersections(p1, p2) or
                        other.intersections(p1, p2) ):
                    # Merge the lists.
                    return Polygon(self.pts[:i+1] + other.pts[j:] +
                                   other.pts[:j+1] + self.pts[i:])
        
    def join(self, other):
        # joinPolygon used to be called "join", which got confused
        # with Curve.join, so the name was changed.  This is here to
        # find out if Polygon.join is called elsewhere.
        raise ooferror.ErrPyProgrammingError("Polygon.join was called.")

    def edges(self):
        return Polygon.PolygonEdges(self)
    def __repr__(self):
        return "Polygon(%s)" % `self.pts`

# Function for taking a list of polygons representing the boundary of
# a non-simply-connected polygon and returning a degenerate but
# simply-connected version of it.
def makeCompoundPolygon(plist):
    p0 = plist[0]
    for pn in plist[1:]:
        p0 = p0.joinPolygon(pn)
    return p0

utils.OOFdefine('Polygon', Polygon)

######################
######################

if __name__ == '__main__':
    p1 = Point(0,0)
    p2 = Point(1,0)
    p3 = Point(1,1)
    p4 = Point(0,1)

    poly = Polygon([p1,p2,p3,p4])
    curve = Curve([p1,p2,p3,p4])
    print "Points"
    for point in poly.points():
        print point
    print "Curve Edges"
    for edge in curve.edges():
        print edge
    print "Polygon Edges"
    for edge in poly.edges():
        print edge

    print "p1=",p1
    print "poly=", poly
    print "curve=", curve
    print "curve.enclosing_rectangle=", curve.enclosing_rectangle()
        
