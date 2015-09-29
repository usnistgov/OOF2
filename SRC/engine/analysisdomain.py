# -*- python -*-
# $RCSfile: analysisdomain.py,v $
# $Revision: 1.53 $
# $Author: langer $
# $Date: 2013/12/05 20:38:18 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Domain objects.  These are part of the post-solution mesh analysis
# process.  A "domain" is a user-specified portion of a mesh or that
# mesh's microstructure, specified in terms of mesh or microstructure
# objects, like pixels, elements, cross-sections, etc.

# One cannot actually evalute an output on a domain -- it's necessary
# to sample the domain first, and the sample objects are the
# numerically savvy components.  There can be more than one sampling
# of a domain.

from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import pixelgroup
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import microstructure
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import pixelgroupparam
from ooflib.common.IO import placeholder
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
from ooflib.engine import analysissample
from ooflib.engine import skeletoncontext
from ooflib.engine.IO import meshcsparams
from ooflib.engine.IO import skeletongroupparams
from ooflib.common import parallel_enable
import ooflib.engine.mesh

import sys

class Domain(registeredclass.RegisteredClass):
    registry = []
    def set_mesh(self, mesh):
        if mesh is not None:
            self.mesh = mesh
            self.meshctxt = ooflib.engine.mesh.meshes[mesh]
            self.femesh = self.meshctxt.getObject()
            self.skeleton = self.femesh.skeleton
            self.skelcontext = skeletoncontext.skeletonContexts[
                skeletoncontext.extractSkeletonPath(mesh)]
            self.ms = self.meshctxt.getMicrostructure()
            self.mscontext = self.skelcontext.getParent()
        else:
            self.mesh = None
            self.meshctxt = None
            self.femesh = None
            self.skeleton = None
            self.skelcontext = None
            self.ms = None
            self.mscontext = None
    def read_lock(self):
        self.meshctxt.begin_reading()
        self.skelcontext.begin_reading()
        self.mscontext.begin_reading()
    def read_release(self):
        self.mscontext.end_reading()
        self.skelcontext.end_reading()
        self.meshctxt.end_reading()

    tip = "A specified region of &mesh; or its &micro; for sampling."
    discussion = xmlmenudump.loadFile('DISCUSSIONS/engine/reg/domain.xml')


# Each subclass implements some subset of retrieval functions, which
# return information about the domain, in the form of a bounding-box
# rectangle, or a list of objects (elements, points).  The caller is
# expected to be something that will then construct sample objects, or
# wrap the returned objects in sample objects.

# Retrieval functions are things like get_bounds, get_pixels,
# get_endpoints.  Not all retrieval functions exist for all domains,
# and some retrieval functions might be expensive.  They should return
# None or an empty list if the domain is empty.

# Units, where they make sense, are physical units on the
# microstructure.

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# An object for operating on the entire mesh.
class EntireMesh(Domain):
    # Returns a bounding rectangle.
    def get_bounds(self):
        if parallel_enable.enabled():
            return self.skeleton.localbounds
        else:
            return primitives.Rectangle(primitives.Point(0.0,0.0),
                                        self.ms.size())
    
    # Returns a list of iPoint pixel indices.
    def get_pixels(self):
        return self.ms.coords()

    def contains(self, pt):
        return True

    # Returns a list of all the elements.  This maybe should return the
    # iterator, to save memory?  The number of elements could be large.
    def get_elements(self):
        el_list = []
        iter = self.femesh.element_iterator()
        while not iter.end():
            el_list.append(iter.element())
            iter.next()
        return el_list
        

registeredclass.Registration(
    'Entire Mesh',
    Domain,
    EntireMesh,
    0,
    params=[],
    sample_types = [analysissample.GRID, analysissample.PIXEL,
                    analysissample.ELEMENT],
    tip='Use the entire Mesh as a post-processing domain.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/entire_mesh.xml'))

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Pixel selection or group -- these actually live on
# the host microstructure, so you have to go there to get 'em.
class PixelGroup(Domain):
    def __init__(self, pixels):
        self.pixels = pixels
    def _pixels_from_group(self):
        if self.pixels == placeholder.selection:
            return  self.ms.pixelselection.getSelection()
        elif self.pixels == placeholder.every:
            return self.ms.coords()
        else:
            group = self.ms.findGroup(self.pixels)
            if group:
                return group.members()
    def get_pixels(self):
        return self._pixels_from_group()
    def contains(self, pt):
        ipt = self.ms.pixelFromPoint(pt)
        if self.pixels == placeholder.selection:
            return self.ms.pixelselection.getObject().isSelected(ipt)
        elif self.pixels == placeholder.every:
            return True
        else:
            groups = pixelgroup.pixelGroupNames(self.ms, ipt)
            return self.pixels in groups
    def get_bounds(self):
        ms_size = self.ms.size()
        pixels = self._pixels_from_group()
        if pixels:
            maxx=0.0
            maxy=0.0
            minx=ms_size[0]
            miny=ms_size[1]
            pixel_size = self.ms.sizeOfPixels()

            if parallel_enable.enabled():
                boundsxmin=self.skeleton.localbounds.xmin()
                boundsxmax=self.skeleton.localbounds.xmax()
                boundsymin=self.skeleton.localbounds.ymin()
                boundsymax=self.skeleton.localbounds.ymax()
                for p in pixels:
                    low_x = p[0]*pixel_size[0]
                    hi_x = low_x + pixel_size[0]
                    low_y = p[1]*pixel_size[1]
                    hi_y = low_y + pixel_size[1]
                    if low_x >= boundsxmin:
                        minx = min(minx, low_x)
                    if low_y >= boundsymin:
                        miny = min(miny, low_y)
                    if hi_x <= boundsxmax:
                        maxx = max(maxx, hi_x)
                    if hi_y <= boundsymax:
                        maxy = max(maxy, hi_y)
            else:
                for p in pixels:
                    low_x = p[0]*pixel_size[0]
                    hi_x = low_x + pixel_size[0]
                    low_y = p[1]*pixel_size[1]
                    hi_y = low_y + pixel_size[1]
                    minx = min(minx, low_x)
                    miny = min(miny, low_y)
                    maxx = max(maxx, hi_x)
                    maxy = max(maxy, hi_y)

            return primitives.Rectangle(primitives.Point(minx, miny),
                                        primitives.Point(maxx, maxy))
    
registeredclass.Registration(
    'Pixel Group',
    Domain,
    PixelGroup,
    10,
    params=[pixelgroupparam.PixelAggregateParameter('pixels',
                                                    tip=parameter.emptyTipString)],
    sample_types = [analysissample.GRID, analysissample.PIXEL],
    tip="Use a pixel group as a post-processing domain.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/pixelgroup_domain.xml'))

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Cross-section -- currently, all cross-sections are straight, so the
# endpoints provide a complete description.  Also, the elemental
# segments are straight.  This is named "CrossSectionDomain" to
# distinguish it from the CrossSection class which represents actual
# cross-sections in the mesh.

class CrossSectionDomain(Domain):
    def __init__(self, cross_section):
        self.cross_section=cross_section
        
    def get_endpoints(self):
        # Dimension-independent version copied from OOF3D for testing
        # here.
        DIM = 2
        cs_obj = self.meshctxt.getCrossSection(self.cross_section)
        bounds = self.meshctxt.size()
        errmsg = ("Segment %s, %s is entirely outside the mesh."
                  %(cs_obj.start, cs_obj.end))
        # Check that both endpoints aren't out of bounds on the same
        # side of the bounding box in any dimension.
        for i in range(DIM):
            if ((cs_obj.start[i] < 0 and cs_obj.end[i] < 0) or
                (cs_obj.start[i] > bounds[i] and cs_obj.end[i] > bounds[i])):
                raise ooferror.ErrUserError(errmsg)
        
        # If an endpoint is out of bounds in any dimension, project it
        # back onto the bounding planes.  First, clone the endpoints
        # so that we aren't modifying the data in the cross section
        # object.
        real_start = primitives.Point(*tuple(cs_obj.start))
        real_end = primitives.Point(*tuple(cs_obj.end))
        for i in range(DIM):
            direction = real_end - real_start
            otherdims = [(i+j)%DIM 
                         for j in range(1, DIM)]
            if real_start[i] < 0:
                # direction[i] can't be zero if real_start[i] < 0 or
                # else the bounding box check above would have failed.
                alpha = -real_start[i]/direction[i]
                for j in otherdims:
                    real_start[j] += alpha*direction[j]
                real_start[i] = 0 # don't allow roundoff
            elif real_start[i] > bounds[i]:
                alpha = (real_start[i] - bounds[i])/direction[i]
                for j in otherdims:
                    real_start[j] -= alpha*direction[j]
                real_start[i] = bounds[i]

            if real_end[i] < 0:
                alpha = -real_end[i]/direction[i]
                for j in otherdims:
                    real_end[j] += alpha*direction[j]
                real_end[i] = 0
            elif real_end[i] > bounds[i]:
                alpha = (real_end[i] - bounds[i])/direction[i]
                for j in otherdims:
                    real_end[j] -= alpha*direction[j]
                real_end[i] = bounds[i]

        # Check that the clipped segment isn't infinitesimal.  This
        # can happen if it grazes a corner of the Microstructure.
        seg = real_end - real_start
        if seg*seg == 0:
            raise ooferror.ErrUserError(errmsg)

        # Check that the modified points are within bounds.  It's
        # possible that they're not if the original points were placed
        # sufficiently perversely.
        for i in range(DIM):
            if not (0 <= real_start[i] <= bounds[i] and
                    0 <= real_end[i] <= bounds[i]):
                raise ooferror.ErrUserError(errmsg)

        return (real_start, real_end)


    # Builds (and returns) a list of tuples, each consisting of a
    # primitives.Segment object and a mesh element.  These occur in
    # order from start to end, which map exactly once on to the cross
    # section, and whose boundaries correspond to intersections of the
    # cross-section with element boundaries.
    def get_elemental_segments(self):
        cs_obj = self.meshctxt.getCrossSection(self.cross_section)

        (real_start, real_end) = self.get_endpoints()
        
        local_segment = primitives.Segment(real_start, real_end)
        skeleton = self.skeleton

        start_el = skeleton.enclosingElement(real_start)

        result = []

        # "last" means "most recent", and is distinct from "final".
        last_pt = cs_obj.start
        last_el = start_el

        try:
            # HACK: Because of round-off, the first call to this
            # function can see two intersections, but the first one is
            # spurious.  If this happens, re-run it, but tell it about
            # the spurious intersection.
            (isec, new_el) = \
                   skeleton.get_intersection_and_next_element(
                local_segment, last_el, None)
        except ooferror.ErrPyProgrammingError, e:
            if e.summary()=="Segment exits element multiple times.":
                (isec, new_el) = \
                       skeleton.get_intersection_and_next_element(
                    local_segment, last_el, real_start)
            else:
                raise 
            

        # If the *first* call yields no intersections, then the
        # whole cross-section lies within one element.  Return
        # a single segment made up of the whole cross-section.
        if not isec:
            result.append( (primitives.Segment(last_pt, real_end),
                            self.femesh.getElement(last_el.meshindex))  )
            return result

        # Otherwise, keep iterating until you get to the end.
        while new_el:
            result.append( (primitives.Segment(last_pt, isec),
                            self.femesh.getElement(last_el.meshindex))  )
            last_pt = isec
            last_el = new_el
            (isec, new_el) = \
                   skeleton.get_intersection_and_next_element(
                local_segment, last_el, last_pt)

        # Bolt on the final one.
        result.append( (primitives.Segment(last_pt, real_end),
                        self.femesh.getElement(last_el.meshindex))  )

        return result


registeredclass.Registration(
    'Cross Section',
    Domain,
    CrossSectionDomain,
    20,
    params=[meshcsparams.MeshCrossSectionParameter('cross_section',
                                      tip='The cross section to sample.')],
    sample_types = [analysissample.BENTLINE, analysissample.LINE],
    tip='Use a Mesh cross section as the post-processing domain.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/xsection_domain.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class ElementGroup(Domain):
    def __init__(self, elements):
        self.elements = elements # name of an element group
    def _elements_from_aggregate(self):
        skel_els = []
        if self.elements == placeholder.selection:
            skel_els = self.skelcontext.elementselection.retrieveFromSkeleton(
                self.skeleton)
        else:
            skel_els = self.skelcontext.elementgroups.get_groupFromSkeleton(
                self.elements, self.skeleton)
        return [self.femesh.getElement(s.meshindex) for s in skel_els]

    def get_bounds(self):
        first = 1
        for e in self._elements_from_aggregate():
            for n in e.cornernode_iterator():
                pos = n.position()
                if first:
                    xmin = pos[0]
                    xmax = pos[0]
                    ymin = pos[1]
                    ymax = pos[1]
                    first = None
                else:
                    xmin = min(pos[0], xmin)
                    xmax = max(pos[0], xmax)
                    ymin = min(pos[1], ymin)
                    ymax = max(pos[1], ymax)
        if not first:
            return primitives.Rectangle(primitives.Point(xmin, ymin),
                                        primitives.Point(xmax, ymax) )

    def contains(self, pt):
        skelel = self.skeleton.enclosingElement(pt)
        if self.elements == placeholder.selection:
            return skelel.isSelected()
        return self.elements in skelel.groups
            
                
    def get_elements(self):
        return self._elements_from_aggregate()

registeredclass.Registration(
    'Element Group',
    Domain,
    ElementGroup,
    30,
    params=[skeletongroupparams.ElementAggregateParameter('elements',
                                                          tip='Elements to sample.')],
    sample_types=[analysissample.GRID, analysissample.ELEMENT],
    tip='Use an element group as the post-processing domain.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/element_group_domain.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class SinglePoint(Domain):
    def __init__(self, point):
        self.point = point
    def get_points(self):
        return [self.point]

registeredclass.Registration(
    'Single Point',
    Domain,
    SinglePoint,
    ordering=0.5,
    params=[primitives.PointParameter(
            'point', tip='Undisplaced position of the sample point.')
            ],
    sample_types=[analysissample.POINT],
    tip='Use a single point for the post-processing domain.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/pointdomain.xml')
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class SegmentSide(enum.EnumClass('LEFT', 'RIGHT')):
    tip="The side of an element edge on which output data should be computed."
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/enum/segmentside.xml')

class SkeletonEdgeBoundaryDomain(Domain):
    def __init__(self, boundary, side):
        self.boundary = boundary
        self.side = side
    # Builds (and returns) a list of tuples, each consisting of a
    # primitives.Segment object and a mesh element. 
    def get_elemental_segments(self):
        result = []
        skel = self.meshctxt.getParent().getObject()
        bdy = skel.edgeboundaries[self.boundary]
        for edge in bdy.edges:
            nodes = edge.get_nodes()
            if self.side == 'LEFT':
                el = edge.getLeftElement()
            else:
                el = edge.getRightElement()
            result.append((primitives.Segment(nodes[0].position(),
                                              nodes[1].position()),
                           self.femesh.getElement(el.meshindex)))
        return result

registeredclass.Registration(
    'Edge Boundary',
    Domain,
    SkeletonEdgeBoundaryDomain,
    25,
    params=[
        skeletongroupparams.SkeletonEdgeBoundaryParameter(
            'boundary',
            tip="The name of the boundary on which to evaluate the output."),
        enum.EnumParameter(
            'side', SegmentSide,
            tip="Use the element on this side, if both exist.")],
    sample_types = [analysissample.BENTLINE],
    tip="Use a Skeleton edge boundary as the post-processing domain.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/skeledgedomain.xml')
)
    
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Evaluating outputs at the nodes of a Skeleton PointBoundary is sort
# of weird, because if a point boundary contains more than one node,
# it's possible that the corresponding boundary in the Mesh should
# contain intermediate nodes, if the Mesh elements are high order.
# SkeletonPointBoundaryDomain is provided for completeness, but
# probably only makes sense when the boundary in question consists of
# a single node.  The same consideration applies to setting boundary
# conditions on a point boundary.

class SkeletonPointBoundaryDomain(Domain):
    def __init__(self, boundary):
        self.boundary = boundary
    def get_points(self):
        skel = self.meshctxt.getParent().getObject()
        bdy = skel.pointboundaries[self.boundary]
        return [n.position() for n in bdy.nodes]

registeredclass.Registration(
    'Point Boundary',
    Domain,
    SkeletonPointBoundaryDomain,
    26,
    params=[
        skeletongroupparams.SkeletonPointBoundaryParameter(
            'boundary',
            tip='The name of the boundary on which to evaluate the output.')],
    sample_types = [analysissample.POINT],
    tip="Use a Skeleton point boundary as the post-processing domain.",
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/skelptbdydomain.xml')
)

