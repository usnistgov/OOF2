# -*- python -*-
# $RCSfile: analysissample.py,v $
# $Revision: 1.65 $
# $Author: langer $
# $Date: 2013/12/11 20:49:07 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Sampling objects.  A sampling object applies to a particular domain,
# and upon invocation (with appropriate parameters), returns a list of
# samples.  In principle, samples can answer quantitative questions
# about themselves, such as:
#  - What is your location?
#  - What is the value of output O(location)^n on you?
#  - (advanced) What fraction of you satisfies x < O(location) < y?

## TODO: There used to be an identifier() method, which wasn't used,
## so it's been commented out.  Either restore it if it's useful, or
## delete it entirely.

#
# Element samples understand "value" to mean "integral".  The area of
# an element can be found by evaluating an output to the zeroth power.
# 
# With that caveat, all of the analysis operations should be able to
# compute themselves by asking questions of this type of their
# samples.  For efficiency, samples can cache expensive data, such as
# their area or important area-fractions.

# Some samples make sense to evaluate directly, like points on a grid
# or points on a line, and others do not, because they have no fixed
# location, like elements and pixels.  Directly-evaluate-able sample
# sets should register themselves with "direct=True", and others
# should not.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import ooferror
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import automatic
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.SWIG.engine import outputval
import math
import string
import types

# Sample objects should have a "columnNames" attribute, which is a
# list of strings which identify the columns of data which are
# provided, and a "columnData" routine, which provides a list of
# strings which make up this data.

# The base class has the output-wrapping "columnData" routine -- this
# takes as input a list of strings identifying the headers that are
# actually used, and picks those items out of the data result from the
# subclass's outputData routine.  This base class routine returns a
# list-enclosed list -- subclasses which need to return multiple data
# sets can return several lists.  The length of the top-level list
# returned from this function is the number of data sets.

## TODONT: Add NodeSample, for printing values directly at Nodes.
## This is hard to do, because we don't have a way of specifying sets
## of Mesh nodes, and it's not a good operation mathematically,
## because it not mesh size invariant.  About the only thing that
## makes sense to do at Nodes is to evaluate Fields, which can be done
## in the MeshInfo toolbox.

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Domains need to indicate what kinds of Sampling methods make sense for
# them, using the constants defined here. 

## TODO: Use the Sample or SampleSet class heirarchy, instead of
## these.  The class heirarchy should reflect the 3 topological
## distinct sampling methods:
### Continuous -- integrals can be performed using shape functions.
### Griddable -- output can be evaluated at points, but the points can
###    be chosen on a grid.
### DiscretePoints -- output can only be evaluated at given points.

class SamplingType(
    enum.EnumClass(
        'GRID',   # Promises existence of get_bounds() and contains().
        'PIXEL',  # Promises existence of get_pixels().
        'ELEMENT',   # Promises existence of get_elements().
        'POINT',     # Promises existence of get_points().
        'LINE',      # Promises existence of get_endpoints().
        'BENTLINE'   # Promises existence of get_elemental_segments().
        )):
    pass

GRID = SamplingType('GRID')
PIXEL = SamplingType('PIXEL')
ELEMENT = SamplingType('ELEMENT')
POINT = SamplingType('POINT')
LINE = SamplingType('LINE')
BENTLINE = SamplingType('BENTLINE')

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class Sample:
    def columnData(self, header):
        datalist = self.outputData()
        return [ [ datalist[self.columnNames.index(x)] for x in header] ]

class ElementSample(Sample):
    columnNames = ["Element"]
    def __init__(self, element):
        self.element = element
        self.index = element.get_index()
    # def identifier(self):
    #     return self.index
    def integrate(self, domain, output, order, power=1):
        femesh = domain.meshctxt.getObject()
        gauss_pts = self.element.integration_points(order)
        pts = [x.mastercoord() for x in gauss_pts]
        wgts = [x.weight() for x in gauss_pts]
        if power==0:
            val = output.instancefn(output)
            return reduce(lambda x,y: x+y, wgts)*val.one()
        else:                           # power > 0
            vals = output.evaluate(femesh, [self.element], [pts])
            if power == 1:
                return reduce(lambda x,y: x+y[0]*y[1], zip(wgts, vals),
                              vals[0].zero())
            if power > 1:
                return reduce(lambda x,y: x+y[0]*(y[1]**power),
                              zip(wgts, vals),
                              vals[0].zero())
        raise ooferror.ErrPyProgrammingError("Impossible situation arose")

    # The ElementSample is actually not used for direct output, but
    # can use this mechanism for debugging purposes.
    def outputData(self):
        return ["Element %d" % self.index]
        


class PointSample(Sample):
    columnNames = ["X", "Y"]
    def __init__(self, point):
        self.point = point
    # def identifier(self):
    #     return self.point
    def outputData(self):
        return [`self.point.x`, `self.point.y`]




# Line samples know how far along the line they are, from 0 to 1.
# as well as in physical units.
class LineSample(PointSample):
    columnNames = ["Distance", "Fraction", "X", "Y"]
    def __init__(self, point, fraction, distance):
        PointSample.__init__(self, point)
        self.fraction = fraction
        self.distance = distance
    # def identifier(self):
    #     return (self.point, self.fraction, self.distance)
    def outputData(self):
        return [`self.distance`, `self.fraction`,
                `self.point.x`, `self.point.y`] 


# A portion of a line contained within one element.  "Segment" is a
# primitives.Segment object, and "element" is an FEMesh element.
class ElementLineSample(Sample):
    columnNames = ["Segment", "Distance", "Fraction", "X", "Y"]
    def __init__(self, segment, element, fractions, distances, n_points):
        self.segment = segment
        self.element = element
        # "Fractions" are the fractional distance along the segment
        # at the start and end of this element; distances are
        # similar; n_points is how many points to evaluate at.
        self.fractions = fractions
        self.distances = distances
        self.n_points = n_points
    # def identifier(self):
    #     return (self.segment, self.element)
    # Because there are multiple points, this class has a local
    # evaluate routine.  Returns a tuple of length n_points>2,
    # of evenly-spaced points.  
    def evaluate(self, femesh, output):
        start = self.segment.start()
        end = self.segment.end()
        if self.n_points > 1:
            dx = (end-start)/float(self.n_points-1)
        else:
            dx = 0
        master_point_set = []
        for i in range(self.n_points):
            lab_point = start+i*dx
            master_point_set.append(self.element.to_master(lab_point))
        return output.evaluate( femesh, [self.element],
                                [master_point_set] )
    # This class has multiple data sets, and so overrides the
    # base-class columnData routine.
    def columnData(self, header):
        out_list = []
        start = self.segment.start()
        end = self.segment.end()
        if self.n_points > 1:
            dx = (end-start)/float(self.n_points-1)
            df = (self.fractions[1]-self.fractions[0])/float(self.n_points-1)
            dd = (self.distances[1]-self.distances[0])/float(self.n_points-1)
        else:
            dx = df = dd = 0
        for i in range(self.n_points):
            lab_pt = start+i*dx
            outputData = [`self.segment`, `self.distances[0]+i*dd`,
                          `self.fractions[0]+i*df`, `lab_pt[0]`, `lab_pt[1]`]
            out_list.append( [ outputData[self.columnNames.index(x)]
                              for x in header] )
        return out_list

# Pixels.  PixelSamples can be evaluated at their centers, or
# integrated over.

class PixelSample(Sample):
    columnNames = ["Pixel", "X", "Y"]
    def __init__(self, pixel, size):
        # "pixel" is an iPoint pixel index.
        self.pixel = pixel
        pt_x = float(self.pixel[0])*size[0] + 0.5*size[0]
        pt_y = float(self.pixel[1])*size[1] + 0.5*size[1]
        self.point = primitives.Point(pt_x, pt_y)
    # def identifier(self):
    #     return self.pixel
    def outputData(self):
        return [ "(%d %d)" % (self.pixel[0], self.pixel[1]),
                 `self.point[0]`, `self.point[1]` ]
    # For integration and direct output, pixels are treated as points
    # at their centers.  It may be desirable, at some point, to take
    # the integration operation more seriously.
    def integrate(self, domain, output, power=1):
        if power==0:
            return output.instancefn(output).one()
        v = self.evaluate(domain, output)
        if power==1:
            return v
        v.component_pow(power) # in-place operation! 
        return v
    
    # Evaluate always evaluates at the center, and returns a float.
    def evaluate(self, domain, output):
        real_el = domain.femesh.enclosingElement(domain.skeleton, self.point)
        vlist = output.evaluate(domain.femesh, [real_el],
                                [ [ real_el.to_master(self.point) ] ] )
        return vlist[0]




#################################################################
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#       #       #       #       #       #       #       #       # 


        
# SampleSet objects are containers for many samples, and have
# iterator-like semantics. 

# Each SampleSet subclass must have a class-level "containedClass"
# attribute which is set to the Sample subclass that it contains.

## TODO: Have SampleSet.make_samples and SampleSet.integrate return
## generators instead of lists.  See _getMoments in analyze.py.

class SampleSet(registeredclass.RegisteredClass):
    registry = []
    # The kwargs passed in here will be column names, with
    # boolean attributes.
    def __init__(self, **kwargs):
        self.sample_list = []
        self.__dict__.update(kwargs)
    def __len__(self):
        return len(self.sample_list)
    def __getitem__(self, idx):
        return self.sample_list[idx]
    def get_col_names(self):
        # This version of get_col_names only applies to "direct"
        # subclasses.  The function is redefined in the
        # NonDirectSubclass that's automatically generated in the
        # DirectSampleSetRegistration function.  TODO: This is the
        # wrong way to do it, because there are other SampleSet
        # subclasses that aren't direct, and they need to redefine
        # get_col_names too.  The *default* behavior should be to add
        # this specialized version to the "direct" subclasses, instead
        # of removing it from the nondirect ones.
        ## TODO maybe none of that matters if we get rid of the "Stat"
        ## sample sets.
        col_names = [x for x in self.containedClass.columnNames
                     if getattr(self, _attr_from_colname(x))]
        return col_names

    tip = "Container for samples. Outputs are evaluated at samples."
    discussion = xmlmenudump.loadFile('DISCUSSIONS/engine/reg/sampleset.xml')

# Utility function, for encapsulating the transformation from column
# names to attribute names.  The booleans that indicate which columns
# should be shown are stored in the instance __dict__ as
# "show_<column_name>".  It's done this way because the
# RegisteredClass machinery requires that each parameter correspond to
# an object attribute with the same name.

def _attr_from_colname(colname):
    return "show_"+string.lower(colname)


#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#

# Set of elements.
class ElementSampleSet(SampleSet):
    containedClass = ElementSample
    def __init__(self, order, **kwargs):
        self.order = order
        SampleSet.__init__(self, **kwargs)
    def make_samples(self, domain):
        self.sample_list = []
        els = domain.get_elements()
        for e in els:
            self.sample_list.append(ElementSample(e))
        return len(els) > 0
    def integrate(self, domain, output, power=1):
        if self.order==automatic.automatic:
            order=2            # TODO: Do something cleverer here.
        else:
            order = self.order
        vals = [x.integrate(domain, output, order, power)
                for x in self.sample_list]
        return zip(self.sample_list, vals)
    def get_col_names(self):    # see comment in SampleSet.
        return []


registeredclass.Registration(
    "Element Set",
    SampleSet,
    ElementSampleSet,
    10,
    params=[parameter.AutoIntParameter("order", automatic.automatic,
           tip="Set the order of integration to use during this computation.")],
    sample_type=ELEMENT,
    direct=False,
    tip='Data will be integrated over Element areas.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/elementset.xml')
    )

#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#

# Trick function which creates the registrations for SampleSet
# objects.  Makes both a "direct" and an "indirect" version of each
# sample set, the former used for point-wise data output, and the
# latter used for statistical or composite data output.  The
# non-direct subclass is created locally and registered in this
# function, but its registration is not returned, so it's a bit sneaky
# that way.

# TODO: Would it be better to use a metaclass?

# The 'direct' flag passed to the Registration is used by the GUI
# widget to help it decide which Registrations to list.

def DirectSampleSetRegistration(name, subclass, ordering, params=[],
                                secret=0, tip=None, discussion=None,
                                **kwargs):

    class NonDirectSubclass(subclass):
        def get_col_names(self):
            return []

    NonDirectSubclass.__name__ = "Stat"+subclass.__name__
    
    non_direct_params = params[:]

    ## TODO: Do we still need the Stat sample sets?

    registeredclass.Registration(
        name,
        SampleSet,
        NonDirectSubclass,
        ordering,
        params=non_direct_params,
        secret=secret,
        tip=tip,
        direct=False,
        discussion="""<para>
        <classname>%(statname)s</classname> is a version of <xref
        linkend='RegisteredClass-%(name)s'/> that is used when the
        <link linkend='MenuItem-OOF.Mesh.Analyze'>analysis
        operation</link> is one of the statistics functions.  It is
        identical, except that it does not have the
        <varname>show_*</varname> parameters, which would be
        meaningless in this context.
        </para>""" % {'name': subclass.__name__,
                      'statname' : NonDirectSubclass.__name__ },
        **kwargs)

    # Now pile on the extra parameters.
    for c_name in subclass.containedClass.columnNames:
        params.append(parameter.BooleanParameter(
            _attr_from_colname(c_name), 1, default=1,
            tip="Include or exclude this data from the output.") )

    return registeredclass.Registration(
        name, SampleSet, subclass, ordering, params, secret,
        tip, discussion, direct=True, **kwargs)

#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#

# PointSampleSet is the base class for SampleSets that consist of a
# bunch of points, as opposed to a bunch of other things, like
# elements or pixels.  All point sample sets share an "evaluate"
# routine.  It returns a vector of tuples, each of the form
# (point-sample, value-at-point).

class PointSampleSet(SampleSet):
    def evaluate(self, domain, output):
        return self.integrate(domain, output, power=1)
    def integrate(self, domain, output, power=1):
        femesh = domain.femesh
        skeleton = domain.skeleton
        res = []
        count = 0
        # At this point, p's have to be PointSample objects.
        for p in self.sample_list:
            count += 1
            real_el = femesh.enclosingElement(skeleton, p.point)
            mcoord = real_el.to_master(p.point)
            if power==0:
                val = output.instancefn(output).one()
                res.append((p, val))
            else:
                val = output.evaluate(femesh, [real_el], [[mcoord]])[0]
                # "val" is a list, known to be of length 1.
                if power == 1:
                    res.append( (p, val) )
                else:
                    val.component_pow(power)
                    res.append( (p, val) )
        return res
    
#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#
#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#
    
# Grid on a box.
class GridSampleSet(PointSampleSet):
    containedClass = PointSample
    def __init__(self, x_points, y_points, **kwargs):
        self.x_points = x_points
        self.y_points = y_points
        SampleSet.__init__(self, **kwargs)
    def make_samples(self, domain):
        self.sample_list = []
        box = domain.get_bounds()
        if box:
            bxmin = box.xmin()
            bymin = box.ymin()
            if self.x_points > 1:
                dx = float(box.xmax()-bxmin)/float(self.x_points-1)
            else:
                dx = 0
            if self.y_points > 1:
                dy = float(box.ymax()-bymin)/float(self.y_points-1)
            else:
                dy = 0
            for j in range(self.y_points):
                for i in range(self.x_points):
                    pt = primitives.Point(bxmin+i*dx, bymin+j*dy)
                    if domain.contains(pt):
                        self.sample_list.append(PointSample(pt))
            return 1
                   
DirectSampleSetRegistration(
    "Grid Points",
    GridSampleSet,
    20,
    params=[parameter.IntParameter(
            'x_points', 10,
            tip="Total number of points horizontally in the grid."),
            parameter.IntParameter(
            'y_points', 10,
            tip="Total number of points vertically in the grid.")],
    sample_type=GRID,
    tip='Evaluate data on a rectangular grid of points.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/gridsampleset.xml')
    )


#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#

# Grid of given delta-x, delta-y.
class SpacedGridSampleSet(PointSampleSet):
    containedClass = PointSample
    def __init__(self, delta_x, delta_y, **kwargs):
        self.delta_x = delta_x
        self.delta_y = delta_y
        SampleSet.__init__(self, **kwargs)
    def make_samples(self, domain):
        self.sample_list = []
        box = domain.get_bounds()
        if box:
            bxmin = box.xmin()
            bymin = box.ymin()
            bxmax = box.xmax()
            bymax = box.ymax()
            (x,y)=(bxmin,bymin)
            while 1:
                pt = primitives.Point(x,y)
                if domain.contains(pt):
                    self.sample_list.append(PointSample(pt))
                x += self.delta_x
                if x > bxmax:
                    x = bxmin
                    y += self.delta_y
                    if y > bymax:
                        return 1        # done
                    

DirectSampleSetRegistration(
    "Spaced Grid Points",
    SpacedGridSampleSet,
    21,
    params=[parameter.FloatParameter(
            'delta_x', 0.1,
            tip="Horizontal spacing between grid points."),
            parameter.FloatParameter(
            'delta_y', 0.1,
            tip="Vertical spacing between grid points.")],
    sample_type=GRID,
    tip='Evaluate data on a rectangular grid of points.',
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/spacedgridsampleset.xml')
    )

#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#

class DiscretePointSampleSet(PointSampleSet):
    containedClass = PointSample
    def make_samples(self, domain):
        self.sample_list = [PointSample(p) for p in domain.get_points()]
        return 1

DirectSampleSetRegistration(
    "Discrete Points",
    DiscretePointSampleSet,
    ordering=1,
    sample_type=POINT,
    tip='Evaluate data at a the given point(s).',
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/discreteptsampleset.xml')
    )

#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#

# Regular array of points on a straight line.

class LineSampleSet(PointSampleSet):
    containedClass = LineSample
    def __init__(self, n_points, **kwargs):
        self.n_points = n_points
        SampleSet.__init__(self, **kwargs)
    def make_samples(self, domain):
        self.sample_list = []
        (start,end)=domain.get_endpoints()
        length=math.sqrt( (end-start)**2 )
        # This way of accumulating distances may have roundoff problems.
        # Should be done more sensibly.
        if self.n_points > 1:
            ds = (end-start)*(1.0/float(self.n_points-1))
        else:
            ds = 0
        dsl = math.sqrt(ds**2)
        for i in range(self.n_points):
            local_point = start+i*ds
            distance = i*dsl
            fraction = float(distance)/float(length)
            self.sample_list.append(
                LineSample(local_point, fraction, distance))
        return 1

DirectSampleSetRegistration(
    "Line Points",
    LineSampleSet,
    30,
    params=[parameter.IntParameter(
            'n_points', 50,
            tip="Number of evenly-spaced points"
            " at which to sample the cross section.")],
    sample_type=LINE,
    tip='Evaluate data at evenly spaced points on a line.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/linesampleset.xml')
    )

#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#

# ElementSegmentSampleSet is a collection of straight segments given
# by the intersection of a line with the element edges (eg a
# CrossSection) or by the element edges that make up Skeleton
# EdgeBoundary.  The segments in the collection do not have to be
# parallel to one another, or even contiguous.

class ElementSegmentSampleSet(SampleSet):
    containedClass = ElementLineSample
    def __init__(self, n_points, **kwargs):
        if n_points < 2:
            raise ooferror.ErrUserError("n_points must be greater than 1!")
        self.n_points = n_points
        SampleSet.__init__(self, **kwargs)
    def make_samples(self, domain):
        tempdata = []
        totallength = 0.0
        for (seg, el) in domain.get_elemental_segments():
            seglength = math.sqrt((seg.end() - seg.start())**2)
            tempdata.append((seg, el, totallength, totallength+seglength))
            totallength += seglength
        self.sample_list = [
            ElementLineSample(seg, el, (dist1/totallength, dist2/totallength),
                              (dist1, dist2), self.n_points)
            for seg, el, dist1, dist2 in tempdata]
        return 1
    def evaluate(self, domain, output):
        res = []
        femesh = domain.femesh
        for s in self.sample_list:
            res.append( (s, s.evaluate(femesh, output)) )
        return res

    def integrate(self, domain, output, power=1):
        result = []
        one = output.instancefn(output).one()
        for s in self.sample_list:
            start = s.segment.start()
            end = s.segment.end()
            lgth = math.sqrt( (end-start)**2 )
            if power==0:
                result.append(lgth*one)
            else:
                dx = lgth/float(self.n_points-1)
                vals = s.evaluate(domain.femesh, output)
                if power!=1:
                    for x in vals:
                        x.component_pow(power)
                rval = (vals[0] + vals[1])*dx/2.0
                for i in range(1, len(vals)-1):
                    rval += (vals[i]+vals[i+1])*dx/2.0
                result.append(rval)

        return zip(self.sample_list, result)

            
DirectSampleSetRegistration(
    "Element Segments",
    ElementSegmentSampleSet,
    40,
    params=[parameter.IntRangeParameter(
            "n_points",
            # HACK:  This range should actually be unbounded above.
            [2,25],
            tip="Number of sample points per element")], 
    sample_type=BENTLINE,
    tip='Evaluate data on line segments within Elements.',
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/elementsegmentsample.xml')
    )

#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#

class PixelSampleSet(SampleSet):
    containedClass = PixelSample
    def __init__(self, **kwargs):
        SampleSet.__init__(self, **kwargs)
    def make_samples(self, domain):
        size = domain.ms.sizeOfPixels()
        self.sample_list = [PixelSample(x, size) for x in domain.get_pixels()]
        return len(self.sample_list) > 0
    def evaluate(self, domain, output):
        res = []
        for s in self.sample_list:
            res.append( (s, s.evaluate(domain, output)) )
        return res
        
    def integrate(self, domain, output, power=1):
        vals = [x.integrate(domain, output, power) 
                for x in self.sample_list]
        return zip(self.sample_list, vals)
    

DirectSampleSetRegistration(
    "Pixels",
    PixelSampleSet,
    50,
    params=[],
    sample_type=PIXEL,
    tip='Evaluate data at the centers of pixels.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/pixelsampleset.xml')
    )


####################

class SamplingParameter(parameter.RegisteredParameter):
    def __init__(self, name, value=None, default=None, tip=None):
        parameter.RegisteredParameter.__init__(self, name, reg=SampleSet,
                                               default=default, tip=tip)
