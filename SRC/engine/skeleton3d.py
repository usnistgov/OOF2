# -*- python -*-
# $RCSfile: skeleton3d.py,v $
# $Revision: 1.21 $
# $Author: langer $
# $Date: 2014/09/27 21:40:56 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# A Skeleton contains the geometry of a finite element mesh, without
# any of the details.  It has lists of SkeletonElements,
# SkeletonNodes, and SkeletonEdgeBoundary (made up of SkeletonEdges).
# but no intermediate nodes, materials, or shape functions.

## TODO: This file has not been updated to use new (April 2009)
## Progress objects.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import coord
from ooflib.SWIG.common import timestamp
from ooflib.SWIG.engine import femesh
from ooflib.SWIG.engine import elementlocator
from ooflib.SWIG.common import switchboard
#not used?
#from ooflib.SWIG.engine import cskeleton
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import parallel_enable
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common import utils
from ooflib.common import microstructure
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import skeletonboundary
from ooflib.engine import skeletoncontext
from ooflib.engine import skeletondiff
from ooflib.engine import skeletonelement3d
from ooflib.engine import skeletongroups
from ooflib.engine import skeletonnode
from ooflib.engine import skeletonsegment
from ooflib.engine import skeletonselectable
#Interface branch
from ooflib.engine import materialmanager

from ooflib.common import mainthread



import math
import random
import time
import types
import weakref
import sys

Registration = registeredclass.Registration

SkeletonNode = skeletonnode.SkeletonNode
PeriodicSkeletonNode = skeletonnode.PeriodicSkeletonNode
SkeletonEdgeBoundary = skeletonboundary.SkeletonEdgeBoundary
ExteriorSkeletonEdgeBoundary = skeletonboundary.ExteriorSkeletonEdgeBoundary
SkeletonPointBoundary = skeletonboundary.SkeletonPointBoundary
ExteriorSkeletonPointBoundary = skeletonboundary.ExteriorSkeletonPointBoundary
SkeletonEdge = skeletonsegment.SkeletonEdge
#SkeletonBrick = skeletonelement3d.SkeletonBrick
SkeletonTetra = skeletonelement3d.SkeletonTetra
SkeletonSegment = skeletonsegment.SkeletonSegment

# TODO: when this stabilizes, compare to skeleton.py and separate
# duplicate code.

# Tetrahedral skeleton arrangements

class Arrangement(
    enum.EnumClass(('moderate', 'going both ways'),
                   ('middling', 'going both ways, the other way'))):
    tip = "Arrangement for tetrahedral initial Skeleton."
    discussion = xmlmenudump.loadFile('DISCUSSIONS/engine/enum/arrangement.xml')
    
utils.OOFdefine('Arrangement', Arrangement)

# Known arrangements.
moderate = Arrangement('moderate')
middling = Arrangement('middling')

class SkeletonGeometry(registeredclass.RegisteredClass):
    registry = []
    def __init__(self, type):
        self.type = type
    tip = "Element shape for the initial Skeleton."
    discussion = """<para>
    <classname>SkeletonGeometry</classname> objects are used to
    specify the shape of the &elems; in the uniform &skel; created by
    <xref linkend='MenuItem-OOF.Skeleton.New'/>.
    </para>"""


    def createGridOfNodes(self, skel, pBar, m, n, l):
        # The brick skeleton begins with a grid of nodes.
        btmlftfrnt = skel.getPointBoundary('bottomleftfront', exterior=1)
        btmrgtfrnt = skel.getPointBoundary('bottomrightfront', exterior=1)
        toplftfrnt = skel.getPointBoundary('topleftfront', exterior=1)
        toprgtfrnt = skel.getPointBoundary('toprightfront', exterior=1)
        btmlftback = skel.getPointBoundary('bottomleftback', exterior=1)
        btmrgtback = skel.getPointBoundary('bottomrightback', exterior=1)
        toplftback = skel.getPointBoundary('topleftback', exterior=1)
        toprgtback = skel.getPointBoundary('toprightback', exterior=1)

        # here, and throughout the file i and n are for the y
        # coordinate, j and m are for the x coordinate, and k and l
        # are for the z coordinate

        ## create nodes and selected point boundaries.
        dx = (skel.MS.size()[0]*1.0)/m   # Promote numerators to floating-point.
        dy = (skel.MS.size()[1]*1.0)/n
        dz = (skel.MS.size()[2]*1.0)/l
        pBar.set_message("allocating nodes")
        tot_items = (m + 1)*(n + 1)*(l + 1)
        for i in range(n+1):
            for j in range(m+1):
                for k in range(l+1):
                    # set upper and right edges exactly to avoid roundoff
                    if j == m:
                        x = skel.MS.size()[0]
                    else:
                        x = j*dx
                    if i == n:
                        y = skel.MS.size()[1]
                    else:
                        y = i*dy
                    if k == l:
                        z = skel.MS.size()[2]
                    else:
                        z = k*dz

                    node = skel.newNode(x,y,z)
                    # set node partners index formula = i*(m+1)*(l+1)+j*(l+1)+k
                    if self.top_bottom_periodicity and i==n:
                        node.addPartner(skel.getNode(j*(l+1)+k))
                        
                        if self.left_right_periodicity and j==0:
                            node.addPartner(skel.getNode(m*(l+1)+k))
                            
                            if self.front_back_periodicity and k==0:
                                node.addPartner(skel.getNode(m*(l+1)+l))
                            if self.front_back_periodicity and k==l:
                                node.addPartner(skel.getNode(m*(l+1)))
                                               
                        if self.left_right_periodicity and j==m:
                            node.addPartner(skel.getNode(k))
                            if self.front_back_periodicity and k==0:
                                node.addPartner(skel.getNode(l))
                            if self.front_back_periodicity and k==l:
                                node.addPartner(skel.getNode(0))

                        if self.front_back_periodicity and k==0:
                            node.addPartner(skel.getNode(j*(l+1)+l))
                        if self.front_back_periodicity and k==l:
                            node.addPartner(skel.getNode(j*(l+1)))

                    if self.left_right_periodicity and j==m:
                        node.addPartner(skel.getNode(i*(m+1)*(l+1)+k))

                        if self.front_back_periodicity and k==0:
                            node.addPartner(skel.getNode(i*(m+1)*(l+1)+l))
                        if self.front_back_periodicity and k==l:
                            node.addPartner(skel.getNode(i*(m+1)*(l+1)))

                        
                    if self.front_back_periodicity and k==l:
                        node.addPartner(skel.getNode(i*(m+1)*(l+1)+j*(l+1)))

                    # add nodes to corner boundaries
                    if i==0 and j==0 and k==0:
                        btmlftback.addNode(node)
                    if i==0 and j==m and k==0:
                        btmrgtback.addNode(node)
                    if i==n and j==0 and k==0:
                        toplftback.addNode(node)
                    if i==n and j==m and k==0:
                        toprgtback.addNode(node)                   
                    if i==0 and j==0 and k==l:
                        btmlftfrnt.addNode(node)
                    if i==0 and j==m and k==l:
                        btmrgtfrnt.addNode(node)
                    if i==n and j==0 and k==l:
                        toplftfrnt.addNode(node)
                    if i==n and j==m and k==l:
                        toprgtfrnt.addNode(node)
                    if pBar.query_stop():
                        pBar.set_failure()
                        pBar.set_message("Failed")
                        return None
                    else:                   
                        pBar.set_progress(1.0* (i*(m+1)*(l+1)+j*(l+1)+k+1) /tot_items)


    def addGridSegmentsToBoundaries(self, skel, i, j, k, m, n, l):
        # index formula = i*(m+1)*(l+1)+j*(l+1)+k

        if j == 0 and k == 0:
            llb = i*(m+1)*(l+1)                    # lower left back
            ulb = (i+1)*(m+1)*(l+1)                # upper left back
            lftback = skel.getEdgeBoundary('leftback', exterior = 1)
            segment = skel.segments[
                skeletonnode.canonical_order(skel.nodes[ulb],
                                             skel.nodes[llb])]
            edge = SkeletonEdge(segment)
            edge.set_direction(skel.nodes[ulb], skel.nodes[llb])
            lftback.addEdge(edge)

        if j == 0 and k == (l-1):
            ulf = (i+1)*(m+1)*(l+1)+l              # upper left front
            llf = i*(m+1)*(l+1)+l                  # lower left front 
            lftfrnt = skel.getEdgeBoundary('leftfront', exterior = 1)
            segment = skel.segments[
                skeletonnode.canonical_order(skel.nodes[ulf],
                                             skel.nodes[llf])]
            edge = SkeletonEdge(segment)
            edge.set_direction(skel.nodes[ulf], skel.nodes[llf])
            lftfrnt.addEdge(edge)
 
        if j == (m-1) and k == 0:
            lrb = i*(m+1)*(l+1)+m*(l+1)            # lower right back
            urb = (i+1)*(m+1)*(l+1)+m*(l+1)        # upper right back 
            rgtback = skel.getEdgeBoundary('rightback', exterior=1)
            segment = skel.segments[
                skeletonnode.canonical_order(skel.nodes[lrb],
                                             skel.nodes[urb])]
            edge = SkeletonEdge(segment)
            edge.set_direction(skel.nodes[lrb], skel.nodes[urb])
            rgtback.addEdge(edge)

        if j == (m-1) and k == (l-1):
            lrf = i*(m+1)*(l+1)+m*(l+1)+l          # lower right front
            urf = (i+1)*(m+1)*(l+1)+m*(l+1)+l      # upper right front
            rgtfrnt = skel.getEdgeBoundary('rightfront', exterior=1)
            segment = skel.segments[
                skeletonnode.canonical_order(skel.nodes[lrf],
                                             skel.nodes[urf])]
            edge = SkeletonEdge(segment)
            edge.set_direction(skel.nodes[lrf], skel.nodes[urf])
            rgtfrnt.addEdge(edge)

        if i == 0 and k == 0:
            llb = j*(l+1)                           # lower left back
            lrb = (j+1)*(l+1)                       # lower right back
            btmback = skel.getEdgeBoundary('bottomback', exterior=1)
            segment = skel.segments[
                skeletonnode.canonical_order(skel.nodes[llb],
                                             skel.nodes[lrb])]
            edge = SkeletonEdge(segment)
            edge.set_direction(skel.nodes[llb], skel.nodes[lrb])
            btmback.addEdge(edge)
            
        if i == 0 and k == (l-1):
            lrf = (j+1)*(l+1)+l                    # lower right front
            llf = j*(l+1)+l                        # lower left front 
            btmfrnt = skel.getEdgeBoundary('bottomfront', exterior=1)
            segment = skel.segments[
                skeletonnode.canonical_order(skel.nodes[llf],
                                             skel.nodes[lrf])]
            edge = SkeletonEdge(segment)
            edge.set_direction(skel.nodes[llf], skel.nodes[lrf])
            btmfrnt.addEdge(edge)

        if i == (n-1) and k == 0:
            ulb = n*(m+1)*(l+1)+j*(l+1)            # upper left back
            urb = n*(m+1)*(l+1)+(j+1)*(l+1)        # upper right back 
            topback = skel.getEdgeBoundary('topback', exterior=1)
            segment = skel.segments[
                skeletonnode.canonical_order(skel.nodes[urb],
                                             skel.nodes[ulb])]
            edge = SkeletonEdge(segment)
            edge.set_direction(skel.nodes[urb], skel.nodes[ulb])
            topback.addEdge(edge)

        if i == (n-1) and k == (l-1):
            ulf = n*(m+1)*(l+1)+j*(l+1)+l          # upper left front
            urf = n*(m+1)*(l+1)+(j+1)*(l+1)+l      # upper right front
            topfrnt = skel.getEdgeBoundary('topfront', exterior=1)
            segment = skel.segments[
                skeletonnode.canonical_order(skel.nodes[urf],
                                             skel.nodes[ulf])]
            edge = SkeletonEdge(segment)
            edge.set_direction(skel.nodes[urf], skel.nodes[ulf])
            topfrnt.addEdge(edge)

        if  i == 0 and j == 0:
            llb = k                                # lower left back
            llf = k+1                              # lower left front 
            btmleft = skel.getEdgeBoundary('bottomleft', exterior=1)
            segment = skel.segments[
                skeletonnode.canonical_order(skel.nodes[llb],
                                             skel.nodes[llf])]
            edge = SkeletonEdge(segment)
            edge.set_direction(skel.nodes[llb], skel.nodes[llf])
            btmleft.addEdge(edge)

        if  i == 0 and j == (m-1):
            lrb = m*(l+1)+k                        # lower right back
            lrf = m*(l+1)+k+1                      # lower right front 
            btmrght = skel.getEdgeBoundary('bottomright', exterior=1)
            segment = skel.segments[
                skeletonnode.canonical_order(skel.nodes[lrb],
                                             skel.nodes[lrf])]
            edge = SkeletonEdge(segment)
            edge.set_direction(skel.nodes[lrb], skel.nodes[lrf])
            btmrght.addEdge(edge)

        if  i == (n-1) and j == 0:
            tlb = n*(m+1)*(l+1)+k                  # top left back
            tlf = n*(m+1)*(l+1)+k+1                # top left front 
            topleft = skel.getEdgeBoundary('topleft', exterior=1)
            segment = skel.segments[
                skeletonnode.canonical_order(skel.nodes[tlb],
                                             skel.nodes[tlf])]
            edge = SkeletonEdge(segment)
            edge.set_direction(skel.nodes[tlb], skel.nodes[tlf])
            topleft.addEdge(edge)

        if  i == (n-1) and j == (m-1):
            trb = n*(m+1)*(l+1)+m*(l+1)+k          # top right back
            trf = n*(m+1)*(l+1)+m*(l+1)+k+1        # top right front 
            toprght = skel.getEdgeBoundary('topright', exterior=1)
            segment = skel.segments[
                skeletonnode.canonical_order(skel.nodes[trb],
                                             skel.nodes[trf])]
            edge = SkeletonEdge(segment)
            edge.set_direction(skel.nodes[trb], skel.nodes[trf])
            toprght.addEdge(edge)

           

# class BrickSkeleton(SkeletonGeometry):
#     def __init__(self, left_right_periodicity=False,
#                  top_bottom_periodicity=False,
#                  front_back_periodicity=False):
#         SkeletonGeometry.__init__(self, 'quad')
#         self.left_right_periodicity = left_right_periodicity
#         self.top_bottom_periodicity = top_bottom_periodicity
#         self.front_back_periodicity = front_back_periodicity
#     def __call__(self, m, n, l, microStructure, preset_homog=0):
#         # Create a skeleton of quadrilateral elements, n rows by m
#         # columns.  The width and height of the entire skeleton are h
#         # and w.
#         pBar = progressbar.getProgress()
#         skel = Skeleton(microStructure, self.left_right_periodicity,
#                         self.top_bottom_periodicity,
#                         self.front_back_periodicity)
#         skel.reserveNodes((m+1)*(n+1)*(l+1))
#         skel.reserveElements(m*n*l)

#         ## create nodes and selected point boundaries.
#         self.createGridOfNodes(skel,pBar,m,n,l)

#         ## create elements and edges
#         pBar.set_message("creating elements from nodes")
#         tot_items = m*n*l
#         ## loop over elements
#         for i in range(n):                  
#             for j in range(m):              
#                 for k in range(l):
#                     ulf = (i+1)*(m+1)*(l+1)+j*(l+1)+k        # upper left front
#                     urf = (i+1)*(m+1)*(l+1)+(j+1)*(l+1)+k    # upper right front
#                     lrf = i*(m+1)*(l+1)+(j+1)*(l+1)+k        # lower right front
#                     llf = i*(m+1)*(l+1)+j*(l+1)+k            # lower left front 
#                     ulb = (i+1)*(m+1)*(l+1)+j*(l+1)+k+1      # upper left back
#                     urb = (i+1)*(m+1)*(l+1)+(j+1)*(l+1)+k+1  # upper right back 
#                     lrb = i*(m+1)*(l+1)+(j+1)*(l+1)+k+1      # lower right back
#                     llb = i*(m+1)*(l+1)+j*(l+1)+k+1          # lower left back
#                     el = skel.newElement([skel.nodes[ulf],skel.nodes[urf],
#                                           skel.nodes[lrf],skel.nodes[llf],
#                                           skel.nodes[ulb],skel.nodes[urb],
#                                           skel.nodes[lrb],skel.nodes[llb]])
#                     # Simple skeleton -- set the homogeneity to "1".
#                     if preset_homog:
#                         dom_pixel = microStructure.categoryFromPoint(
#                             el.repr_position())
#                         el.setHomogeneous(dom_pixel)

#                     # Element constructors make the segments, we can use them
#                     # to make the edges and add them to the boundaries.
#                     self.addGridSegmentsToBoundaries(skel, i, j, k, m, n, l)
#                     el.findHomogeneityAndDominantPixel(skel.MS)

#                     if pBar.query_stop():
#                         pBar.set_failure()
#                         pBar.set_message("Failed")
#                         return None
#                     else:
#                         rectangle_count = i*m*l+j*l+k
#                         pBar.set_progress(float(rectangle_count)/tot_items)
#                         pBar.set_message("Creating elements: %d/%d" %\
#                                      (rectangle_count, tot_items) )
#         if not pBar.query_stop():
#             pBar.set_message("Succeeded")
#             pBar.set_success()
#         return skel

## Registration(
##     'BrickSkeleton',
##     SkeletonGeometry,
##     BrickSkeleton,
##     0,
##     params=[parameter.BooleanParameter('left_right_periodicity',value=False,default=False,
##                   tip="Whether or not the skeleton has left-right periodicity"),
##             parameter.BooleanParameter('top_bottom_periodicity',value=False,default=False,
##                   tip="Whether or not the skeleton has top-bottom periodicity"),
##             parameter.BooleanParameter('front_back_periodicity',value=False,default=False,
##                   tip="Whether or not the skeleton has rront-back periodicity")],
##     tip="A Skeleton of brick shaped elements.",
##     discussion="""<para>
##     <classname>BrickSkeleton</classname> is used as the
##     <varname>skeleton_geometry</varname> argument of <xref
##     linkend='MenuItem-OOF.Skeleton.New'/>, specifying that it is to
##     create a &skel; with brick &elems;.
##     </para>""")
    
class TetraSkeleton(SkeletonGeometry):
    def __init__(self, arrangement=moderate, left_right_periodicity=False,
                 top_bottom_periodicity=False,
                 front_back_periodicity=False):
        SkeletonGeometry.__init__(self, 'tetra')
        self.arrangement = arrangement
        self.left_right_periodicity = left_right_periodicity
        self.top_bottom_periodicity = top_bottom_periodicity
        self.front_back_periodicity = front_back_periodicity
    def __call__(self, m, n, l, microStructure, preset_homog=0):
        # Create a skeleton of tetrahedral elements, n rows by m
        # columns.  The width and height of the entire skeleton are h
        # and w.
        pBar = progressbar.getProgress()
        skel = Skeleton(microStructure, self.left_right_periodicity,
                        self.top_bottom_periodicity,
                        self.front_back_periodicity)
        skel.reserveNodes((m+1)*(n+1)*(l+1))
        skel.reserveElements(5*m*n*l)

        ## create nodes and selected point boundaries.
        self.createGridOfNodes(skel,pBar,m,n,l)

        ## create elements and edges
        pBar.set_message("creating elements from nodes")
        tot_items = m*n*l
        if self.arrangement == moderate:
            flip = 0
        elif self.arrangement == middling:
            flip = 1
        else:
            debug.fmsg('unknown arrangement!', self.arrangement)
        ## loop over elements
        for i in range(n):                  
            for j in range(m):              
                for k in range(l):

                    ulf = (i+1)*(m+1)*(l+1)+j*(l+1)+k+1      # upper left front
                    urf = (i+1)*(m+1)*(l+1)+(j+1)*(l+1)+k+1  # upper right front
                    lrf = i*(m+1)*(l+1)+(j+1)*(l+1)+k+1      # lower right front
                    llf = i*(m+1)*(l+1)+j*(l+1)+k+1          # lower left front 
                    ulb = (i+1)*(m+1)*(l+1)+j*(l+1)+k        # upper left back
                    urb = (i+1)*(m+1)*(l+1)+(j+1)*(l+1)+k    # upper right back 
                    lrb = i*(m+1)*(l+1)+(j+1)*(l+1)+k        # lower right back
                    llb = i*(m+1)*(l+1)+j*(l+1)+k            # lower left back

                    # Divide points of brick into 5 tetras.  One
                    # diagonal of each face becomes a segment.  There
                    # are two ways to do this, and we must alternate
                    # between them, so the skeleton is consistent.
                    # So the only "arrangements" are moderate and middling.
                    if not flip:
                        el1 = skel.newElement([skel.nodes[llf],skel.nodes[urf],
                                              skel.nodes[lrf],skel.nodes[lrb]])
                        el2 = skel.newElement([skel.nodes[llf],skel.nodes[ulf],
                                              skel.nodes[urf],skel.nodes[ulb]])
                        el3 = skel.newElement([skel.nodes[lrb],skel.nodes[urf],
                                              skel.nodes[urb],skel.nodes[ulb]])
                        el4 = skel.newElement([skel.nodes[llf],skel.nodes[lrb],
                                              skel.nodes[llb],skel.nodes[ulb]])
                        el5 = skel.newElement([skel.nodes[llf],skel.nodes[ulb],
                                              skel.nodes[urf],skel.nodes[lrb]])

                    else:
                        el1 = skel.newElement([skel.nodes[llf],skel.nodes[ulf],
                                              skel.nodes[lrf],skel.nodes[llb]])
                        el2 = skel.newElement([skel.nodes[ulf],skel.nodes[urf],
                                              skel.nodes[lrf],skel.nodes[urb]])
                        el3 = skel.newElement([skel.nodes[ulf],skel.nodes[ulb],
                                              skel.nodes[urb],skel.nodes[llb]])
                        el4 = skel.newElement([skel.nodes[lrf],skel.nodes[urb],
                                              skel.nodes[lrb],skel.nodes[llb]])
                        el5 = skel.newElement([skel.nodes[ulf],skel.nodes[urb],
                                              skel.nodes[lrf],skel.nodes[llb]])


                    flip = not flip

                    # Simple skeleton -- set the homogeneity to "1".
                    if preset_homog:
                        dom_pixel = microStructure.categoryFromPoint(
                            el1.repr_position())
                        el1.setHomogeneous(dom_pixel)
                        dom_pixel = microStructure.categoryFromPoint(
                            el2.repr_position())
                        el2.setHomogeneous(dom_pixel)
                        dom_pixel = microStructure.categoryFromPoint(
                            el3.repr_position())
                        el3.setHomogeneous(dom_pixel)
                        dom_pixel = microStructure.categoryFromPoint(
                            el4.repr_position())
                        el4.setHomogeneous(dom_pixel)
                        dom_pixel = microStructure.categoryFromPoint(
                            el5.repr_position())
                        el5.setHomogeneous(dom_pixel)

                    # Element constructors make the segments, we can use them
                    # to make the edges and add them to the boundaries.
                    self.addGridSegmentsToBoundaries(skel, i, j, k, m, n, l)
                    
                    el1.findHomogeneityAndDominantPixel(skel.MS)
                    el2.findHomogeneityAndDominantPixel(skel.MS)
                    el3.findHomogeneityAndDominantPixel(skel.MS)
                    el4.findHomogeneityAndDominantPixel(skel.MS)
                    el5.findHomogeneityAndDominantPixel(skel.MS)

                    if pBar.query_stop():
                        pBar.set_failure()
                        pBar.set_message("Failed")
                        return None
                    else:
                        rectangle_count = i*m*l+j*l+k
                        pBar.set_progress(float(rectangle_count)/tot_items)
                        pBar.set_message("Creating elements: %d/%d" %\
                                     (5*rectangle_count, 5*tot_items) )

                if l%2==0:
                    flip = not flip
            if m%2==0:
                flip = not flip
                
        if not pBar.query_stop():
            pBar.set_message("Succeeded")
            pBar.set_success()
        return skel


Registration(
    'TetraSkeleton',
    SkeletonGeometry,
    TetraSkeleton,
    0,
    params=[enum.EnumParameter('arrangement', Arrangement, moderate,
                       tip="How to arrange tetrahedral elements in a Skeleton"),
            parameter.BooleanParameter('left_right_periodicity',value=False,default=False,
                  tip="Whether or not the skeleton has left-right periodicity"),
            parameter.BooleanParameter('top_bottom_periodicity',value=False,default=False,
                  tip="Whether or not the skeleton has top-bottom periodicity"),
            parameter.BooleanParameter('front_back_periodicity',value=False,default=False,
                  tip="Whether or not the skeleton has rront-back periodicity")],
    tip="A Skeleton of tetrahedral elements.",
    discussion="""<para>
    <classname>TetraSkeleton</classname> is used as the
    <varname>skeleton_geometry</varname> argument of <xref
    linkend='MenuItem-OOF.Skeleton.New'/>, specifying that it is to
    create a &skel; with tetrahedral &elems;.
    </para>""")

######################

# SkeletonBase is provided just so different kinds of skeletons
# (Skeleton, DeputySkeleton) can be checked for in a single
# isinstance() call.

class SkeletonBase:
    def __init__(self):
        self._illegal = 0
        # Appears in the Skeleton Page
        self.homogeneityIndex = None
        self.illegalCount = None
        
        # Keep track of when the skeleton geometry last changed, and
        # when the homogeneity index was last updated.  Geometry
        # changes happen when new elements are added to the skeleton,
        # or when they are detected in the
        # findHomogeneityandDominantPixel routine of member skeleton
        # elements.
        self.homogeneity_index_computation_time = timestamp.TimeStamp()
        self.homogeneity_index_computation_time.backdate()
        self.most_recent_geometry_change = timestamp.TimeStamp()
        self.illegal_count_computation_time = timestamp.TimeStamp()
        self.illegal_count_computation_time.backdate()

    def destroy(self):
        pass

    def updateGeometry(self):
        self.most_recent_geometry_change.increment()
        
    def setHomogeneityIndex(self):
        # Tempting though it may be, do not lock the MS here.  This
        # can be called with the skeleton already locked, which
        # implicitly locks the MS.
        homogIndex = 0.0
        illegalcount = 0
        for e in self.elements:
            if not e.illegal():
                homogIndex += e.volume()*e.homogeneity(self.MS)
            else:
                illegalcount += 1
                
        homogIndex /= self.volume()

        self.illegalCount = illegalcount
        self.homogeneityIndex = homogIndex
        self.homogeneity_index_computation_time.increment()
        self.illegal_count_computation_time.increment()

    def getIllegalCount(self):
        if self.illegalCount is None or (self.illegal_count_computation_time
                                         < self.most_recent_geometry_change):
            illegalCount = 0
            for e in self.elements:
                if e.illegal():
                    illegalCount += 1
            self.illegalCount = illegalCount
            self.illegal_count_computation_time.increment()
        return self.illegalCount

    def getIllegalElements(self):
        return [e for e in self.elements if e.illegal()]
    
    def getHomogeneityIndex(self):
        if (self.homogeneity_index_computation_time < self.MS.getTimeStamp()
            or self.homogeneity_index_computation_time <
            self.most_recent_geometry_change):
            self.setHomogeneityIndex()
        return self.homogeneityIndex

          
    def enclosingElement(self, point):
        if self._needElementLocator:
            self.createElementLocator()
        #TODO 3D: would be nice to figure out why typemaps aren't working!
        elId = self.elementLocator.getElementIdFromPoint(point[0], point[1], point[2])
        return self.elements[elId]
        

    def nearestSgmt(self, point):
        if self._needElementLocator:
            self.createElementLocator()
        #TODO 3D: would be nice to figure out why typemaps aren't working!
        elId = self.elementLocator.getElementIdFromPoint(point[0], point[1], point[2])
        element = self.elements[elId]
        weights = element.getWeights(point[0], point[1], point[2])
        id1 = weights.index(max(weights))
        weights.remove(max(weights))
        id2 = weights.index(max(weights))
        if id2 >= id1: id2 += 1
        return self.getSegment(element.nodes[id1], element.nodes[id2])
        

    ## Call setIllegal() after creating an illegal element.
    def setIllegal(self):
        self._illegal = 1
    def illegal(self):
        return self._illegal

    ## Call checkIllegality after any operation that may have changed
    ## an illegal skeleton into a legal one.  Operations that change
    ## legal skeletons into illegal ones should be able to check
    ## legality themselves (without searching all elements) and should
    ## call setIllegal() directly.
    def checkIllegality(self):
        for el in self.elements:
            if el.illegal():
                self._illegal = 1
                return
        self._illegal = 0

    def countShapes(self):
        shapecounts = {}
        for name in skeletonelement3d.ElementShapeType.names:
            shapecounts[name] = 0
        for e in self.elements:
            shapecounts[e.type().name] += 1
        return shapecounts

    

#####################

# Skeleton objects live in a SkeletonContext stack, and many of their
# operations are invoked via the Context, which does important
# bookkeeppiinngg.

class Skeleton(SkeletonBase):
    """
    The geometrical information for a mesh, without any of the
    complications of nodes, shapefunctions, or materials.
    """
    def __init__(self,microStructure, left_right_periodicity=False,
                 top_bottom_periodicity=False,
                 front_back_periodicity=False):
        SkeletonBase.__init__(self)
        self.MS = microStructure        # Microstructure object, not context
        self._size = self.MS.size()
        self._volume = self._size[0]*self._size[1]*self._size[2]
        self.nodemovehistory = skeletondiff.NodeMoveHistory()
        self.elements = utils.ReservableList()
        self._found_element = None      # used in enclosingElement().
        self.nodes = utils.ReservableList()
        self.segments = {}              # Nondirected edges.
        self.edgeboundaries = {}
        self.pointboundaries = {}
        self.timestamp = timestamp.TimeStamp()
#         self.meshes = []                # list of Mesh objects for real meshes
        self.left_right_periodicity = left_right_periodicity
        self.top_bottom_periodicity = top_bottom_periodicity
        self.front_back_periodicity = front_back_periodicity


        # VTK Storage Objects. This is for a first pass at
        # incorporating vtk into the actual data storage for the
        # skeleton. TODO 3D: clean up function cruft and get rid of
        # redundancies as much as possible in skeleton storage.
        self.skelpoints = vtk.vtkPoints()
        self.skelgrid = vtk.vtkUnstructuredGrid()
        self.skelgrid.SetPoints(self.skelpoints)
        self.skellines = vtk.vtkCellArray() # we need a set of lines for drawing
        
        # When elements and nodes are deleted from the mesh, they
        # aren't immediately removed from the lists in the Skeleton.
        # They're only removed when cleanUp() is called.  washMe
        # indicates whether or not cleanUp() is necessary.
        self.washMe = 0
        
        self._needHash = 1
        self._needElementLocator = 1

        self.deputy = None              # currently active DeputySkeleton
        self.deputylist = []            # all deputies
        self._deferreddestruction = 0
        self._destroyed = 0


        # Getting rid of storing the name or skeleton path.
        # A problem showed up when a microstructure or skeleton
        # was renamed and _name did not get updated. Instead of
        # fixing the code to get _name updated correctly,
        # we chose to get rid of it. _name is usually used
        # to index into skeletonContexts.
##        self._name = ""

        self.setIndexBase() # Default is to start from zero.
        
        # Decided not to meddle with the exisiting indexing and also not to
        # introduce a new indexing.
        # Instead, dictionaries -- ex) node.index: index in self.nodes
        # With this a node can be fetched with "index" efficiently,
        # which is crucial in parallel mode.
        # ex) def getNodeWithIndex(index):
        #         return self.nodes[node_index_dict[index]]
        # The first values for these dictionaries always starts from 0,
        # which is not a surprise.
        # It could be useful in serial mode too, but at this point
        # these are only maintained in parallel mode.
        self.node_index_count = 0
        self.elem_index_count = 0
        self.node_index_dict = {}
        self.elem_index_dict = {}

        self.cachedHomogeneities = {}

        # geometric info of all Skeletons (in parallel mode)
        if parallel_enable.enabled():
            self.all_skeletons = None

    # Current index data for each of the three types of skeleton
    # objects are stored here -- these get incremented when new
    # objects of the indicated type are created in this skeleton.
    # These indices should start at zero, and proceed contiguously
    # within a skeleton context.
    def setIndexBase(self, node_index_base=0,
                     segment_index_base=0,
                     element_index_base=0):
        self.node_index = node_index_base
        self.segment_index = segment_index_base
        self.element_index = element_index_base

        # Used in parallel mode -- these will not be changed
        if parallel_enable.enabled():
            self.node_index0 = node_index_base
            self.segment_index0 = segment_index_base
            self.element_index0 = element_index_base

    def reserveElements(self, n):
        self.elements.reserve(n)
        self.skelgrid.Allocate(n,n)

    def reserveNodes(self, n):
        self.nodes.reserve(n)
        self.skelpoints.SetNumberOfPoints(n)

    def isDeputy(self):
        return 0

    def clearCachedHomogeneities(self):
        self.cachedHomogeneities = {}
        
    def destroy(self, skelcontext):
        SkeletonBase.destroy(self)
        ## NOTE: destroy() may be called more than once, if the
        ## Skeleton has deputies.  If the Skeleton has deputies when
        ## it is destroyed, the _deferreddestruction flag is set, and
        ## destroy() will be called again when the last deputy is
        ## destroyed.  That means that destroy() can't leave lists of
        ## destroyed objects lying around -- it must actually replace
        ## the lists with empty lists.

        self._destroyed = 1             # see NOTE above
        
        # Any data shared with deputies must not be deleted until the
        # deputies are done with it.
        if self.ndeputies() == 0:
            for ebdy in skelcontext.edgeboundaries.values():
                ebdy.remove(self)
            for pbdy in skelcontext.pointboundaries.values():
                pbdy.remove(self)
            del self.MS
            self.disconnect()
        else:
            self._deferreddestruction = 1

        for el in self.elements:
            el.destroy(self)
        self.elements = []
            
    def destroyed(self):
        return self._destroyed

#     def destroy_meshes(self):
#         # Loop over a copy of the mesh list instead of the list
#         # itself, because Mesh.destroy() calls Skeleton.remove_mesh(),
#         # which removes items from the list and messes up the
#         # iteration.
#         meshes = self.meshes[:]
#         for mesh in meshes:
#             mesh.lockAndDelete()        # removes from self.meshes
#         self.meshes = []                # see NOTE in destroy(), above

    def __repr__(self):
        return 'Skeleton(%d)' % id(self)

    def getPoints(self):
        return self.skelpoints
    
    def disconnect(self):
        for s in self.nodes + self.segments.values() + self.elements:
            s.disconnect()

    def getTimeStamp(self):
        return self.timestamp
##         return max(self.timestamp, self.MS.getTimeStamp())

#     def materialsChanged(self, ms):
#         ## called from SkeletonContext.materialsChanged()
#         if ms is self.MS:
#             for mesh in self.meshes:
#                 mesh.refreshMaterials(self)

    def hashNodes(self):
        # in 3D, the hashing is taken care of by the vtkPointLocator class
        self.pointLocator = vtk.vtkMergePoints()
        #self.pointLocator.InitPointInsertion(self.skelpoints, self.skelpoints.GetBounds())
        self.pointLocator.SetDataSet(self.skelgrid)
        self.pointLocator.SetDivisions(4,4,4)
        self._needHash = 0

    def needsHash(self):
        self._needHash = 1

    def createElementLocator(self):
        self.elementLocator = elementlocator.ElementLocator()
        self.elementLocator.SetDataSet(self.skelgrid)
        self.elementLocator.BuildLocator()
        self._needElementLocator = 0

    def nnodes(self):
        self.cleanUp()
        return len(self.nodes)
                                   
    def nelements(self):                # for compatiblity w/ Element output
        self.cleanUp()
        return len(self.elements)

    def element_iterator(self):         # for compatiblity w/ Element output
        self.cleanUp()
        return self.elements

    def node_iterator(self):
        self.cleanUp()
        return self.nodes

    def segment_iterator(self):
        self.cleanUp()
        return self.segments.values()

    # This returns the position in the skeleton's node list
    # which is not the same as node.getIndex()
##     def getNodeIndex(self, node):
##         return self.nodes.index(node)

    def notPinnedNodes(self):
        return [n for n in self.node_iterator() if not n.pinned()]

##     def getElementIndex(self, elem):
##         return self.elements.index(elem)

    def nillegal(self):
        n = 0
        for e in self.elements:
            if e.illegal():
                n += 1
        return n

    # Returns a tuple containing maximum x-extent and maximum y-extent
    # of the skeleton. 
    def size(self):
        return self._size

    def volume(self):
        return self._volume

    # convenience function to encapsulate coordinates in a
    # dimensionally independent structure TODO: Eventually we should
    # get rid of things that pass x, y, z separately because it makes
    # things difficult for doing 2D and 3D in the same code.
    # Eventually this function should replace newNode.
    def newNodeFromPoint(self, point):
        return self.newNode(point.x, point.y, point.z)
        
    def newNode(self, x, y, z):
        if (self.left_right_periodicity and (x == 0.0 or x == self.size()[0])) \
           or (self.top_bottom_periodicity and
               (y == 0.0 or y == self.size()[1])) \
           or (self.front_back_periodicity and
               (z == 0.0 or z == self.size()[2])):
            c = PeriodicSkeletonNode(x,y,z,self.skelpoints,index=self.node_index)
        else:
            c = SkeletonNode(x,y,z,self.skelpoints,index=self.node_index)

        self.node_index += 1
        if x == 0.0 or x == self.size()[0]:
            c.setMobilityX(0)
        if y == 0.0 or y == self.size()[1]:
            c.setMobilityY(0)
        if z == 0.0 or z == self.size()[2]:
            c.setMobilityZ(0)
        self.nodes.append(c)
        
        self.node_index_dict[c.index] = self.node_index_count
        self.node_index_count += 1
                
        return c

    # Only elements with nonzero area are constructed here.  The
    # line-elements are expected to be done in the boundary code.
    def newElement(self, nodes, parents=[]):
        nnodes = len(nodes)

        # For now, we only have brick and tetra elements implemented.
        # If we implement both Square Pyramids and Triangular
        # Bipyramids, we won't be able to use the number of nodes to
        # distinguish between them.

        #if nnodes == 8:
        #    el=SkeletonBrick(nodes, self.element_index)

            # In 3D, each node is connected to at least 3 other nodes, so
            # we cannot simply loop over the nodes and connect them
            # consecutively.
            
##                __________
##               /|4       /|5
##              /_________/ |
##             |0 |      1| |
##             |          | |
##             |  |       | |
##             |  _7_ _ _ |_|6
##             | /        | /
##             |/_________|/
##              3         2
            
        self.element_index += 1

        if nnodes == 4:
            el=SkeletonTetra(nodes, self.element_index)

##             /\1
##            / |\
##           /    \
##          /   |  \
##         /        \
##        /     |3   \
##       /    .   .   \
##      /  .         . \
##    0/________________\2

         
        self.elements.append(el)
        for parent in parents:
            el.add_parent(parent)
            parent.add_child(el)
            
        # Add this element's edges to the dictionary of segments.
        # fetchSegment returns an existing SkeletonSegment, or makes one
        # if necessary.


        for pairs in el.segToNodeMap():
            segment = self.fetchSegment(nodes[pairs[0]],nodes[pairs[1]])
            segment.addElement(el)
        
        self.updateGeometry()

        if parallel_enable.enabled():
            self.elem_index_dict[el.index] = self.elem_index_count
            self.elem_index_count += 1

##          self.skelgrid.InsertNextCell(el.GetCellType(),
##                                       el.GetPointIds())

        el.AddCellToGrid(self.skelgrid)
        bounds = self.skelgrid.GetBounds()

        return el

    def loadElement(self, *indices):
        nodes = [self.nodes[index] for index in indices]
        return self.newElement(nodes)

    def loadEdge(self, node0, node1):
        seg = self.getSegment(node0, node1)
        edge = skeletonsegment.SkeletonEdge(seg)
        if seg.nodes()[0] == node0:
            edge.direction = 1
        else:
            edge.direction = -1
        return edge

    def removeElements(self, *elements):
        self.washMe = 1
        # We use the ExtractCells filter to extract all but the
        # deleted cells from the skelgrid.  First we need a list of
        # indices (starting from 0) that we are not deleting.
        # Actually this seems to corrupt elements we add later?
        #list = vtk.vtkIdList()
        #print "in removeElements"
        #print [(el.index, self.elements.index(el)) for el in elements]
        #for el in self.elements:
        #    if el not in elements:
        #        list.InsertNextId(self.elements.index(el))
        #extract = vtk.vtkExtractCells()
        #extract.SetCellList(list)
        #extract.SetInput(self.skelgrid)
        #self.skelgrid = extract.GetOutput()
        #self.skelgrid.Update()
        for el in elements:
            el.defunct = 1
            el.destroy(self)

    def removeNode(self, node):
        # Called only by SkeletonNode.destroy() which is called by
        # SkeletonNode.removeElement() when the node's last element is
        # removed.
        self.washMe = 1
        node.defunct = 1
        
        # Need to update  self.node_index_dict in parallel mode
        #if parallel_enable.enabled():
        #node_index = node.getIndex()
        #list_index = self.node_index_dict[node_index]
            # "node_index" will be deleted from the dict and all the nodes
        #del self.node_index_dict[node_index]
        #affected_nodes = [self.nodes[i].getIndex()
        #                  for i in range(list_index+1, self.nnodes())]
        #for an in affected_nodes:
        #    self.node_index_dict[an] -= 1
        #    self.node_index_count -= 1
            
    def cleanUp(self):
        if self.washMe:
            self.elements = filter(lambda e: not hasattr(e, 'defunct'),
                                   self.elements)
            self.nodes = filter(lambda n: not hasattr(n, 'defunct'), self.nodes)
            # easier and more robust to just rebuild the whole node_index_dict here
            self.node_index_dict = {}
            # don't call nnodes as it causes recursion
            for i in range(len(self.nodes)):
                self.node_index_dict[self.nodes[i].getIndex()] = i
            self.washMe = 0

    def rebuildSkelGrid(self):
        # This is messy, and ideally, when skeleton storage is
        # consolidated better, it won't be necessary. 
        self.skelgrid = vtk.vtkUnstructuredGrid()
        self.skelgrid.SetPoints(self.skelpoints)
        n = self.nelements()
        self.skelgrid.Allocate(n,n)
        for e in self.elements:
            e.AddCellToGrid(self.skelgrid)
        self.hashNodes()
        self.createElementLocator()
        
    def updateVtkCellPoints(self):
        for element in self.elements:
            element.updateVtkCellPoints()

    def getElement(self, index):
        return self.elements[index]
    
    def getElementWithIndex(self, index):
        return self.elements[ self.elem_index_dict[index] ]

    # This returns a node based on its position in the skeleton's
    # node list.  
    def getNode(self, index):
        return self.nodes[index]

    # This returns a node based on its unique index number: the inverse
    # operation of node.getIndex(). TODO: change name of "index" to distinguish
    # between list position and unique ID - nodeID for instance...
    # this indexing is only maintained in parallel...
    def getNodeWithIndex(self, index):
        return self.nodes[ self.node_index_dict[index] ]

    # getSegment returns an existing segment joining the given nodes,
    # or creates a segment if such a segment doesn't already exist.
    def getSegment(self, node0, node1):
        nodes = skeletonnode.canonical_order(node0, node1)
        try:
            return self.segments[nodes]
        except KeyError:
            segment = SkeletonSegment(nodes, self.segment_index)
            self.skellines.InsertNextCell(segment.getVtkLine())
            self.segment_index += 1
            self.segments[nodes] = segment
            return segment

    # fetchSegment is just like getSegment, but it should be faster in
    # the case where the Segment is likely *not* to be in the
    # dictionary already.
    def fetchSegment(self, node0, node1):
        nodes = skeletonnode.canonical_order(node0, node1)
        if nodes in self.segments:
            return self.segments[nodes]
        segment = SkeletonSegment(nodes, self.segment_index)
        self.skellines.InsertNextCell(segment.getVtkLine())
        self.segment_index += 1
        self.segments[nodes] = segment
        return segment

    # findSegment returns an existing segment joining the given nodes,
    # or None if such a segment doesn't exist.
    def findSegment(self, node0, node1):
        try:
            return self.segments[skeletonnode.canonical_order(node0, node1)]
        except KeyError:
            return None

    def removeSegment(self, key):
        # Called only by SkeletonSegment.destroy(), which is called by
        # SkeletonSegment.removeElement when the segment's last
        # element is removed.
        del self.segments[key]
        # There is no convenient way to remove a cell from a
        # vtkCellArray, so for the skellines, which are really just
        # for visualization anyway, it's easier and more efficient to
        # just rebuild them at the end of a modification that changes
        # segments a lot, such as rationalize.  For this, use the
        # function rebuildSkellines.

    def rebuildSkellines(self):
        newskellines = vtk.vtkCellArray()
        for seg in self.segments.values():
            newskellines.InsertNextCell(seg.getVtkLine())
        self.skellines = newskellines


    # Geometry comparison function -- returns 0 if this skeleton has
    # the same size, area, elements, segments, and boundaries as the
    # other, and if all the nodes are within tolerance of the
    # positions of the other; otherwise returns a string describing
    # what went wrong.  Note that these objects must not only be
    # topologically equivalent, but must also be indexed the same for
    # the comparison to succeed.  Does not care about the skeleton
    # name, or about microstructure stuff like pixels, or about group
    # membership or selection status.  The former is properly the
    # responsibility of the microstructure, and the latter the
    # responsibility of the skeleton context.
    def compare(self, other, tolerance):
        if self._size != other._size:
            return "Size mismatch"
        if self._volume != other._volume:
            return "Volume mismatch"

        if len(self.elements)!=len(other.elements):
            return "Element count mismatch"
        if len(self.segments)!=len(other.segments):
            return "Segment count mismatch"
        if len(self.nodes)!=len(other.nodes):
            return "Node count mismatch"

        # Make sure elements have the same node indices.
        for (e1,e2) in zip(self.elements, other.elements):
            if [x.index for x in e1.nodes]!=[x.index for x in e2.nodes]:
                return "Element node indexing mismatch"

        for (s1,s2) in zip(self.segments.values(), other.segments.values()):
            if [x.index for x in s1.nodes()]!=[x.index for x in s2.nodes()]:
                return "Segment node indexing mismatch"

        # Basic topology is right, now quantitatively check node locations.
        tol2 = tolerance**2
        for (n1,n2) in zip(self.nodes, other.nodes):
            if (n1.position()-n2.position())**2 > tol2:
                return "Node outside of tolerance, %s-%s=%s" % \
                       (`n1.position()`, `n2.position()`,
                       `n1.position()-n2.position()`)

        if len(self.edgeboundaries)!=len(other.edgeboundaries):
            return "Edge boundary count mismatch"
        if len(self.pointboundaries)!=len(other.pointboundaries):
            return "Point boundary count mismatch"

        # The boundary tests do *not* assume that the boundaries are
        # in the same order in the two skeletons.
        for key, b1 in self.edgeboundaries.items():
            try:
                b2 = other.edgeboundaries[key]
            except KeyError:
                return "Edge boundary name mismatch: %s" % key
                
            if b1.size()!=b2.size():
                return "Edge boundary size mismatch: %s" % key
            for (e1,e2) in zip(b1.edges, b2.edges):
                if [x.index for x in e1.get_nodes()] != \
                       [x.index for x in e2.get_nodes()]:
                    return "Edge boundary node mismatch: %s" % key

        for key, b1 in self.pointboundaries.items():
            try:
                b2 = other.pointboundaries[key]
            except KeyError:
                return "Point boundary name mismatch: %s" % key
            if b1.size()!=b2.size():
                return "Point boundary size mismatch: %s" % key
            for (n1,n2) in zip(b1.nodes, b2.nodes):
                if n1.index != n2.index:
                    return "Point boundary node index mismatch: %s" % key

        return 0 # Success! 

    #The skeletonpath argument replaces self._name. The only time skeletonContexts
    #is indexed by skeletonpath is when fresh==False, and only to be able to
    #call setIndexBase. If fresh==True, there is no need to supply skeletonpath.
    def properCopy(self, skeletonpath=None, fresh=False):

        # Copy the current skeleton properly so that the new skeleton
        # and the current skeleton are totally independent.  If
        # "fresh" is True, then node, segment, and element indices
        # start at zero.  Otherwise, index-base data is retrieved from
        # the skeleton context.  "fresh" will be true during adaptive
        # mesh refinement.
        
        self.cleanUp()
        # create a new skeleton
        newSkeleton=Skeleton(self.MS)
        if not fresh:
##            context = skeletoncontext.skeletonContexts[self._name]
            context = skeletoncontext.skeletonContexts[skeletonpath]
            newSkeleton.setIndexBase(*context.next_indices)

        # Make new nodes which have different indices, but are children
        # of the old nodes.
        #newSkeleton.nodes = []
        for n in self.nodes:
            newSkeleton.nodes.append(n.copy_child(newSkeleton.node_index,newSkeleton.skelpoints))
            newSkeleton.node_index += 1

        newSkeleton.left_right_periodicity = self.left_right_periodicity
        newSkeleton.top_bottom_periodicity = self.top_bottom_periodicity
        newSkeleton.front_back_periodicity = self.front_back_periodicity

        # rebuild the node partnerships - must be done in separate loop
        # after all nodes are created
        for n in self.nodes:
            for p in n.getPartners():
                n.getChildren()[-1].addPartner(p.getChildren()[-1])

        #Copy the following information also:
        #SkeletonNode _shared_with = []  # except me
        #             _remote_index = {}  # procID : remote index
        if parallel_enable.enabled():
            for n1,n2 in zip(self.nodes,newSkeleton.nodes):
                n2._shared_with=n1._shared_with[:]
                n2._remote_index=n1._remote_index.copy()

        # newSkeleton.nodes = [ n.copy_child() for n in self.nodes ] 

        newSkeleton.elements = []
        n = len(self.elements)
        newSkeleton.skelgrid.Allocate(n,n)
        # TODO 3D: Maybe skeleton Modifications that call proper copy
        # should call rebuildSkellines and rebuildSkelgrid instead of
        # doing it here.
        for e in self.elements:
            idx = newSkeleton.element_index
            newel = e.copy_child(idx)
            newSkeleton.elements.append(newel)
            newel.AddCellToGrid(newSkeleton.skelgrid)
            newSkeleton.element_index += 1
            
        # newSkeleton.elements = [ e.copy_child() for e in self.elements ]

        # Make new segments which have equivalent indices (with new
        # nodes), but are children of the old segments.
        for s in self.segments.values():
            new_seg = s.copy_child(newSkeleton.segment_index)
            newSkeleton.segment_index += 1
            newSkeleton.segments[new_seg.nodes()] = new_seg
            newSkeleton.skellines.InsertNextCell(new_seg.getVtkLine())

        newSkeleton._illegal = self._illegal

        for on, nn in zip(self.nodes, newSkeleton.nodes):
            newSkeleton.node_index_dict[nn.index] = newSkeleton.node_index_count
            newSkeleton.node_index_count += 1

        return newSkeleton
            

    #The skeletonpath argument replaces self._name. The only time skeletonContexts
    #is indexed by skeletonpath is when fresh==False, and only to be able to
    #call setIndexBase. If fresh==True, there is no need to supply skeletonpath.
    def improperCopy(self, skeletonpath=None, fresh=False):
        # Copy a Skeleton, but *not* the elements or segments.  Just
        # nodes.  Used when refining, where the elements and segments
        # are recreated by Refine.apply().
        self.cleanUp()
        newSkeleton = Skeleton(self.MS)
        if not fresh:
##            context = skeletoncontext.skeletonContexts[self._name]
            context = skeletoncontext.skeletonContexts[skeletonpath]
            newSkeleton.setIndexBase(*context.next_indices)

        #newSkeleton.nodes = []
        for n in self.nodes:
            newSkeleton.nodes.append(n.copy_child(newSkeleton.node_index,newSkeleton.skelpoints))
            newSkeleton.node_index += 1
        # newSkeleton.nodes = [n.copy_child() for n in self.nodes]
        # TODO: Storing the positions in vtk points by unique id leads
        # to bound errors as the unset points in the vtkPoints object
        # can be garbage!

        newSkeleton.left_right_periodicity = self.left_right_periodicity
        newSkeleton.top_bottom_periodicity = self.top_bottom_periodicity
        newSkeleton.front_back_periodicity = self.front_back_periodicity

        # rebuild the node partnerships - must be done in separate loop
        # after all nodes are created
        for n in self.nodes:
            for p in n.getPartners():
                n.getChildren()[-1].addPartner(p.getChildren()[-1])

        newSkeleton._illegal = self._illegal

        for on, nn in zip(self.nodes, newSkeleton.nodes):
            newSkeleton.node_index_dict[nn.index] = newSkeleton.node_index_count
            newSkeleton.node_index_count += 1
        # In parallel mode, node keeps a dict of remote indices,
        # {rank: remote_index, ...}. This dict has been copied over but
        # it's useless -- the copied skeleton has new indices for nodes.
        if parallel_enable.enabled():
            from ooflib.SWIG.common import mpitools
            offsets = mpitools.Allgather_Int(newSkeleton.node_index0 - \
                                             self.node_index0)
            if on.isShared():
                    for rank, index in on._remote_index.items():
                        nn.sharesWith(rank, index + offsets[rank])
        
        return newSkeleton

    ###################

    # The following routines are redefined in the DeputySkeleton
    # class.  A DeputySkeleton is a skeleton that differs from another
    # skeleton only in the position of its nodes.  See
    # engine/deputy.py. 

    def getIndexBase(self):
        return (self.node_index, self.segment_index, self.element_index)

    def deputyCopy(self):
        from ooflib.engine import deputy  # delayed import to avoid loops
        # A "copy" that doesn't actually make a copy, but just keeps
        # track of which nodes have been moved.
        return deputy.DeputySkeleton(self)

    def sheriffSkeleton(self):          # The sheriff isn't the deputy
        return self

    def deputize(self, deputy):         # install a new deputy
        if self.deputy:
            self.deputy.deactivate()
        self.deputy = deputy

    def addDeputy(self, dep):
        # Called by DeputySkeleton.__init__()
        self.deputylist.append(dep)

    def removeDeputy(self, dep, skelcontext):
        # Called by DeputySkeleton.destroy()
        self.deputylist.remove(dep)
        if self._deferreddestruction and self.ndeputies() == 0:
            self.destroy(skelcontext)

    def ndeputies(self):
        return len(self.deputylist)

    def activate(self):
        if self.deputy:
            self.deputy.deactivate()
            self.deputy = None

    def moveNodeTo(self, node, position):
        node.moveTo(position)
        for partner in node.getPartners():
            partner.moveTo(position)

    def moveNodeBy(self, node, delta):
        node.moveBy(delta)
        for partner in node.getPartners():
            partner.moveBy(delta)

    def moveNodeBack(self, node):
        node.moveBack()
        for partner in node.getPartners():
            partner.moveBack()

    def getMovedNodes(self):
        return {}

    def nodePosition(self, node):
        # Gets the position of the node in this skeleton even if a
        # deputy is active.
        if self.deputy:
            return self.deputy.originalPosition(node)
        return node.position()
            
    def newSelectionTracker(self, selectionset):
        return skeletonselectable.SelectionTracker()

    def newGroupTracker(self, groupset):
        return skeletongroups.GroupTracker()

    def newPinnedNodeTracker(self):
        return skeletonnode.PinnedNodeTracker(self)

    def promoteTrackers(self, context):
        pass

    #######################
    def weightedEnergyTotal(self, alpha):
        self.cleanUp()
        return reduce(lambda x,y: x+y,
                      [el.area()*el.energyTotal(self, alpha)
                       for el in self.elements])

    def energyTotal(self, alpha):
        self.cleanUp()
        total = 0.
        for el in self.elements:
            total += el.energyTotal(self, alpha)
        return total

    def illegalElements(self):
        return [e for e in self.elements if e.illegal()]

    def activeElements(self):
        self.cleanUp()
        return [e for e in self.elements if e.active(self)]

    def activeNodes(self):
        self.cleanUp()
        return [n for n in self.nodes if n.active(self)]

    def activeSegments(self):
        self.cleanUp()
        return [s for s in self.segments.values() if s.active(self)]
                    
    def nearestNode(self, point):
        if self._needHash:
            self.hashNodes()
        nodeid = self.pointLocator.FindClosestPoint(point[0],point[1],point[2])
        #return self.nodes[nodeid]
        return self.getNodeWithIndex(nodeid)

    def mergeNode(self, node0, node1):

        change = ProvisionalMerge(self, node0, node1)
        change = self.addElementsToChange(node0, node1, change)
        if change is None:
            return
        partners = node0.getPartnerPair(node1)
        if partners is not None:
            change = self.addElementsToChange(partners[0], partners[1],
                                              change)
            if change is None:
                return

        return change

    # helper function for mergeNode encapsulates code that is repeated
    # for partners
    def addElementsToChange(self, node0, node1, change):

        if not node0.canMergeWith(node1):
            return None

        doomedSegment = self.findSegment(node0, node1)
        if doomedSegment is None:
            return None

        # use aperiodic versions of getElements.
        # elements that contain both nodes to be merged
        topElements = doomedSegment.getElements() # topologically changing
        # elements containing node0 but not node1 don't change topology
        isoElements = [elephant
                       for elephant in node0.aperiodicNeighborElements()
                       if elephant not in topElements]

        node0.moveTo(node1.position())
        for element in isoElements:
            if element.illegal():
                node0.moveBack()
                return None
        # Make sure to move the node back to where it was, because the
        # merge may still be rejected.
        node0.moveBack()

        for oldelement in isoElements:
            newnodes = oldelement.nodes[:]
            newnodes[newnodes.index(node0)] = node1
            change.substituteElement(
                oldelement,
                skeletonelement3d.getProvisionalElement(newnodes,
                                                        oldelement.getParents()))
        for oldelement in topElements:
            change.removeElements(oldelement)

        return change


    ########################################################################

    def getPointBoundary(self, name, exterior=None):
        try:
            return self.pointboundaries[name]
        except KeyError:
            if exterior:
                bdy = ExteriorSkeletonPointBoundary(name)
            else:
                bdy = SkeletonPointBoundary(name)
            self.pointboundaries[name] = bdy
            return bdy

    def getEdgeBoundary(self, name, exterior=None):
        try:
            return self.edgeboundaries[name] # existing bdy with this name
        except KeyError:                 # didn't find existing bdy
            if exterior:
                bdy = ExteriorSkeletonEdgeBoundary(name)
            else:
                bdy = SkeletonEdgeBoundary(name)       # create it
            self.edgeboundaries[name] = bdy  # save it
            return bdy

    # The SkeletonContext has already ensured that there is no collision.
    # This routine is called from the SkelContextBoundary object's
    # rename routine.
    def renameBoundary(self, oldname, newname):
        if oldname in self.edgeboundaries.keys():
            self.edgeboundaries[newname]=self.edgeboundaries[oldname]
            del self.edgeboundaries[oldname]
            self.edgeboundaries[newname].rename(newname)
        elif oldname in self.pointboundaries.keys():
            self.pointboundaries[newname]=self.pointboundaries[oldname]
            del self.pointboundaries[oldname]
            self.pointboundaries[newname].rename(newname)

#         # Context-level function, because boundary conditions need
#         # to remain consistent.
#         for mctxt in self.meshes:
#             mctxt.renameBoundary(oldname, newname)

    # Build a new edge boundary from the passed-in list of segments,
    # and return it.  The boundary should "point" from the first
    # segment to the last.  Startnode is required if there is only
    # one segment, and is ignored in the other cases.
    #
    # Caller must provide a topologically trivial list of segments
    # with length greater than zero, so all we have to do here is
    # figure out the directions for the edges.
    def makeEdgeBoundary(self, name, segments=None, startnode=None,
                         exterior=None):
        if (name in self.edgeboundaries.keys()) or \
               (name in self.pointboundaries.keys()):
            raise ooferror.ErrPyProgrammingError(
                "Boundary '%s' already exists." % name)
        
        bdy = self.getEdgeBoundary(name, exterior) # Guaranteed to be new.
        
        if segments is None: 
            return bdy # Return "empty" boundary -- used for stack propagation.

        if len(segments)==1:
            if startnode:
                seg = segments[0]
                if startnode==seg.nodes()[0]:
                    bdy.addEdge(SkeletonEdge(seg, 1))
                else: # startnode==seg.nodes()[1]:
                    bdy.addEdge(SkeletonEdge(seg, -1))
            else:
                raise ooferror.ErrPyProgrammingError(
                    "Singleton segment boundaries require a starting node!")

        else: # Length of the segment list is greater than one.
            for i in range(len(segments)-1):
                seg1 = segments[i]
                seg2 = segments[i+1]
                nodes_and_partners = list(seg2.nodes()) + \
                                     seg2.nodes()[0].getPartners() + \
                                     seg2.nodes()[1].getPartners()
                if seg1.nodes()[0] in nodes_and_partners: #seg2.nodes():
                    bdy.addEdge(SkeletonEdge(seg1, -1))
                else: #  seg1.nodes()[1] in nodes_and_partners: #seg2.nodes():
                    bdy.addEdge(SkeletonEdge(seg1, 1))
            # For the final segment, need to check the one previous.
            seg1 = segments[-2]
            seg2 = segments[-1]
            nodes_and_partners = list(seg1.nodes()) + \
                                 seg1.nodes()[0].getPartners() + \
                                 seg1.nodes()[1].getPartners()
            if seg2.nodes()[0] in nodes_and_partners: #seg1.nodes():
                bdy.addEdge(SkeletonEdge(seg2, 1))
            else: #  seg2.nodes()[1] in seg1.nodes():
                bdy.addEdge(SkeletonEdge(seg2, -1))

#         # Write this boundary to any meshes we have.
#         for mctxt in self.meshes:
#             mctxt.newEdgeBoundary(name, bdy)
                
        return bdy
            

    # Build a new point boundary from the passed-in list of nodes,
    # and return it.  
    def makePointBoundary(self, name, nodes=None, exterior=None):
        if (name in self.pointboundaries.keys()) or \
               (name in self.edgeboundaries.keys()):
            raise ooferror.ErrPyProgrammingError(
                "Boundary '%s' already exists." % name)

        bdy = self.getPointBoundary(name, exterior)

        # Correctly returns an empty boundary if nodes==None.
        if nodes:
            for n in nodes:
                bdy.addNode(n)

#         for mctxt in self.meshes:
#             mctxt.newPointBoundary(name, bdy)

        return bdy
    

    def removeBoundary(self, name):
        if name in self.pointboundaries.keys():
            del self.pointboundaries[name]
        elif name in self.edgeboundaries.keys():
            del self.edgeboundaries[name]

#         # Remove it from the meshes.
#         for mctxt in self.meshes:
#             # Let the mesh *context* do it, because that's where the
#             # boundary conditions live.
#             mctxt.removeBoundary(name)


    # The named boundary has been modified -- change the versions in
    # the mesh to match.  Don't just remove and replace, as this
    # destroys valuable boundary condition info.
    def pushBoundaryToMesh(self, mctxt, name):
        if name in self.pointboundaries.keys():
            b = self.pointboundaries[name]
            mctxt.replacePointBoundary(name, b)
        elif name in self.edgeboundaries.keys():
            b = self.edgeboundaries[name]
            mctxt.replaceEdgeBoundary(name, b)


    def mapBoundary(self, bdy, skeleton, **kwargs):
        # double dispatch wrapper for SkelContextBoundary.map().

        # Copy boundary information from the given skeleton to this
        # skeleton.  The given skeleton might be a deputy, which
        # doesn't have any boundary information, so actually copy from
        # the deputy's sheriff.

        # mapBoundary is a no-op in the DeputySkeleton class, so we
        # don't have to worry about copying boundary data *to* a
        # deputy.  However, if the given source skeleton is a deputy,
        # there's a chance that this skeleton is its sheriff, in which
        # case we don't actually have to copy anything.
        omar = skeleton.sheriffSkeleton()
        if omar is not self.sheriffSkeleton():
            bdy.map(omar, self, **kwargs)


    def find_geometrical_boundaries(self):
        for el in self.elements:
            el.exterior_edges = []

        for seg in self.segment_iterator():
            if seg.nElements() == 1:
                seg.getElements()[0].exterior_edges.append(seg.nodes())

    ##############################

    def quick_sanity_check(self):
        # Just check for illegal elements and consistent volume.  For
        # a more thorough check, see sanity_check(), below.
        sane = True
        volume = 0.
        for element in self.elements:
            volume += element.volume()
            if element.illegal():
                reporter.report("illegal element", element.index,
                                [n.position() for n in element.nodes])
                sane = False
        reporter.report("Total element volume is", volume)
        reporter.report("Microstructure volume is", self.MS.volume())
        if sane:
            reporter.report("*** Skeleton quick sanity check passed. ***")
        else:
            reporter.report("*** Skeleton quick sanity check failed. ***")
        return sane

    def sanity_check(self):
        sane = True
        for element in self.elements:
            if element.illegal():
                reporter.report("illegal element", element.index,
                                [n.position() for n in element.nodes])
                sane = False
            for node in element.nodes:
                if node not in self.nodes:
                    reporter.report("element", element.index, "contains a node",
                                    node.index, "not in the skeleton")
                    sane = False
                if element not in node.aperiodicNeighborElements():
                    reporter.report("inconsistent neighborNodes for node",
                                    node.index, " and element", element.index)
                    sane = False
            segs = element.getSegments(self)
            if None in segs:
                reporter.report("Element", element.index,
                                "is missing a segment")
                sane = False
        for node in self.nodes:
            for element in node.aperiodicNeighborElements():
                if element not in self.elements:
                    reporter.report("node", node.index, "contains an element",
                                    element.index, "not in the skeleton")
                    sane = False
            if not node.aperiodicNeighborElements():
                reporter.report("Node", node.index, "at", node.position(),
                                "has no elements!")
                sane = False
            # Check that nodes on periodic boundaries have partners
            x = node.position().x
            y = node.position().y
            xmax = self.MS.size().x
            ymax = self.MS.size().y
            if self.left_right_periodicity and (x == 0.0 or x == xmax):
                p = node.getDirectedPartner('x')
                if not p or ((x == 0.0 and p.position().x != xmax) or
                             (x ==  xmax and p.position().x != 0.0)):
                    reporter.report(node.__class__.__name__, node.index,
                                    "at", node.position(),
                                    "has no periodic partner in x")
                    reporter.report("   partners are at",
                                    [(ptnr.position(), ptnr.index)
                                     for ptnr in node.getPartners()])
                    sane = False
            if self.top_bottom_periodicity and (y == 0.0 or y == ymax):
                p = node.getDirectedPartner('y')
                if not p or ((y == 0.0 and p.position().y != ymax) or
                             (y == ymax and p.position().y != 0.0)):
                    reporter.report(node.__class__.__name__, node.index,
                                    "at", node.position(),
                                    "has no periodic partner in y")
                    reporter.report("   partners are at",
                                    [(ptnr.position(), ptnr.index)
                                     for ptnr in node.getPartners()])
                    reporter.report([ptnr.position()-primitives.Point(x, ymax)
                                     for ptnr in node.getPartners()])
                    sane = False
            # Check self consistency of partner lists
            for partner in node.getPartners():
                if node not in partner.getPartners():
                    reporter.report("Inconsistent partner lists for",
                                    node.__class__.__name__, node.index,
                                    "at", node.position(), "and",
                                    partner.__class__.__name__, partner.index,
                                    "at", partner.position())
            
                    sane = False
        for segment in self.segments.values():
            elements = segment.getElements()
            for element in elements:
                if element not in self.elements:
                    reporter.report("segment",
                                    [n.index for n in segment.nodes()],
                                    "contains an element", element.index, 
                                    "not in the skeleton")
                    sane = False
            for node in segment.nodes():
                if node not in self.nodes:
                    reporter.report("segment",
                                    [n.index for n in segment.nodes()], 
                                    "contains a node", node.index,
                                    "not in the skeleton")
                    sane = False
            
        if sane:
            reporter.report("*** Skeleton Sanity Check passed. ***")
        else:
            reporter.report("*** Skeleton sanity check failed. ***")
        return sane

                
# ## ### #### ##### ###### ####### ######## ####### ###### ##### #### ### ## #

## Create a real mesh from a Skeleton, using the given element types.

# For now, in 3D, we are ignoring interfaces.
# tet - 4 nodes, 6 edges, 4 faces
# cube - 8 nodes, 12 edges, 6 faces
# wedge - 6 nodes, 9 edges, 5 faces
# square pyramid - 5 nodes, 8 edges, 5 faces

    def femesh(self, edict, set_materials, skelpath):
        # edict[n] is the n-corner-noded master element.  Find the
        # interpolation order of the elements.  They all have the same
        # order, so just pick one.
        
        order = edict.values()[0].fun_order()

        # set_materials is a function that will be called to assign
        # materials to elements.
        pbar = progressbar.getProgress()
        self.cleanUp()

        # Local dictionary of finite-element nodes, indexed by
        # SkeletonNode objects.
        fe_node = {}
        
        # Find which elements and edges are on the geometrical
        # boundaries of the system.
        self.find_geometrical_boundaries()

        realmesh = femesh.FEMesh(self.MS, order)

        # Reserve space in FEMesh::funcnodes and FEMesh::mapnodes so
        # that the vectors aren't continually reallocated.
        nels = {}                       # number of elements of each type
        for n in edict.keys():
            nels[n] = 0
        for el in self.elements:
            nels[el.nnodes()] += 1

        nfuncnodes = self.nnodes() + len(self.segments)*(order-1)
        for n, masterelem in edict.items():
            nfuncnodes += nels[n]*masterelem.ninteriorfuncnodes()
        realmesh.reserveFuncNodes(nfuncnodes)

        masterel = edict[edict.keys()[0]]
        nmapperside = masterel.nexteriormapnodes_only()/masterel.nsides()
        nmapnodes = len(self.segments)*nmapperside
        for n, masterelem in edict.items():
            nmapnodes += nels[n]*masterelem.ninteriormapnodes_only()
        realmesh.reserveMapNodes(nmapnodes)

        # Make the real nodes at the corners of the elements.  These
        # nodes are always both mapping and function nodes.  A
        # "meshindex" attribute is written into the skeleton node.
        mnodecount = self.nnodes()
        for i in xrange(mnodecount):
            cur = self.nodes[i]
            realnode = realmesh.newFuncNode(coord.Coord(cur.position().x,
                                                        cur.position().y,
                                                        cur.position().z)) 
            fe_node[cur] = realnode
            #cur.setMeshIndex(realnode.index())
                
            if pbar.query_stop() !=0 \
               or pbar.get_success() is progressbar.FAILED:
                pbar.set_failure()
                pbar.set_progress(1)
                pbar.set_message("Interrupted")
                return
            else:
                pbar.set_progress(1.0*(i+1)/mnodecount)
                pbar.set_message("Allocating nodes: %d/%d"%(i+1, mnodecount))

        # Loop over elements.
        numelements = self.nelements()
        realmesh.reserveElements(numelements)
        for mesh_idx in xrange(numelements):
            el = self.elements[mesh_idx]
            # Index correspondence happens here -- the skeleton
            # elements are assigned indices in the order that their
            # corresponding real elements are created/assigned.
            # (Skeletonelement3d.realelement sets self.meshindex when it
            # creates the real element.)
            mnodecount += el.realelement(self, realmesh, mesh_idx,
                                         fe_node, mnodecount,
                                         edict, set_materials)
            if pbar.query_stop() !=0 \
                   or pbar.get_success() is progressbar.FAILED:
                pbar.set_failure()
                pbar.set_progress(1)
                pbar.set_message("Interrupted")
                return
            else:
                pbar.set_progress(1.0*(mesh_idx+1)/numelements)
                pbar.set_message("Allocating elements: %d/%d"%(mesh_idx+1, numelements))

        # Then do boundaries.
        # Note that edgeboundaries and pointboundaries are in separate lists
        # in the skeleton, but in a single list in the real mesh.

        # Point boundaries first.
        dict_size = len(self.pointboundaries)
        dict_index = 0
        for bdkey, pointbndy in self.pointboundaries.items():
            realbndy = realmesh.newPointBoundary(bdkey)
            for node in pointbndy.nodes:
                realbndy.addNode(fe_node[node]) # Preserve order of nodes.

                if pbar.query_stop() !=0 \
                       or pbar.get_success() is progressbar.FAILED:
                    pbar.set_failure()
                    pbar.set_progress(1)
                    pbar.set_message("Interrupted")
                    return
                else:
                    pbar.set_progress(1.0*(dict_index+1)/dict_size)
                    pbar.set_message("Allocating point boundaries: %d/%d"%(dict_index+1, dict_size))
            dict_index +=1
        # ... then edge boundaries.
        dict_size = len(self.edgeboundaries)
        dict_index = 0
        for bdkey, edgebndy in self.edgeboundaries.items():
            edgebndy.sequence()
            realbndy = realmesh.newEdgeBoundary(bdkey)
            for skeletonedge in edgebndy.edges:
                # Look up the corresponding element from the skeleton.
                skelel = skeletonedge.segment.getElements()[0]
                realel = realmesh.getElement(skelel.meshindex)

                edge_nodes = skeletonedge.get_nodes()
                realn0 = fe_node[edge_nodes[0]]    # First real node.
                realn1 = fe_node[edge_nodes[1]]    # Second real node.
                realbndy.addEdge(realel.getBndyEdge(realn0,realn1))
                if pbar.query_stop() !=0 \
                       or pbar.get_success() is progressbar.FAILED:
                    pbar.set_failure()
                    pbar.set_progress(1)
                    pbar.set_message("Interrupted")
                    return
                else:
                    pbar.set_progress(1.0*(dict_index+1)/dict_size)
                    pbar.set_message("Allocating edge boundaries: %d/%d"%(dict_index+1, dict_size))
            dict_index +=1

        return realmesh


############################################################################

####################### femesh_shares, for parallel  #####################
    #This version of the method indicates the funcnodes that are shared between processes.
    # This sharing information is assumed to have been created by Haan's code.
    # The sharing information should reach the dofs, fields and equations later.
    def femesh_shares(self, edict, set_materials):
        # edict[n] is the n-sided master element.  Find the
        # interpolation order of the elements.  They all have the same
        # order, so just pick one.
        
        #order = edict[edict.keys()[0]].fun_order()
        #This should do the same thing
        order = edict.values()[0].fun_order()

        # set_materials is a function that will be called to assign
        # materials to elements.
        pbar = progressbar.getProgress()

        self.cleanUp()

        # Local dictionary of finite-element nodes, indexed by
        # SkeletonNode objects.
        fe_node = {}
        
        # Find which elements and edges are on the geometrical
        # boundaries of the system.
        self.find_geometrical_boundaries()

        realmesh = femesh.FEMesh(self.MS, order)

        # Reserve space in FEMesh::funcnodes and FEMesh::mapnodes so
        # that the vectors aren't continually reallocated.
        nels = {}                       # number of elements of each type
        for n in edict.keys():
            nels[n] = 0
        for el in self.elements:
            nels[el.nnodes()] += 1

        nfuncnodes = self.nnodes() + len(self.segments)*(order-1)
        for n, masterelem in edict.items():
            nfuncnodes += nels[n]*masterelem.ninteriorfuncnodes()
        realmesh.reserveFuncNodes(nfuncnodes)

        masterel = edict[edict.keys()[0]]
        nmapperside = masterel.nexteriormapnodes_only()/masterel.nsides()
        nmapnodes = len(self.segments)*nmapperside
        for n, masterelem in edict.items():
            nmapnodes += nels[n]*masterelem.ninteriormapnodes_only()
        realmesh.reserveMapNodes(nmapnodes)

        # Make the real nodes at the corners of the elements.  These
        # nodes are always both mapping and function nodes.  A
        # "meshindex" attribute is written into the skeleton node.
        mnodecount = self.nnodes()
        for i in range(self.nnodes()):
            cur = self.nodes[i]
            #Have to include the local skeleton index and the
            #"remote" indices, as well as the processes that share that node.
            realnode = realmesh.newFuncNode_shares(coord.Coord(cur.position().x,
                                                               cur.position().y),
                                                   cur.sharedWith(),
                                                   [cur.remoteIndex(procnum)
                                                    for procnum in cur.sharedWith()],
                                                   cur.index
                                                   )
            
            fe_node[cur] = realnode
            #cur.setMeshIndex(realnode.index())
            if pbar.query_stop() !=0 \
               or pbar.get_success() is progressbar.FAILED:
                pbar.set_failure()
                pbar.set_progress(1)
                pbar.set_message("Interrupted")
                return
            else:
                pbar.set_progress(1.0*(i+1)/mnodecount)
                pbar.set_message("Allocating nodes: %d/%d"%(i+1, mnodecount))
        
        # Loop over elements.
        numelements = self.nelements()
        realmesh.reserveElements(numelements)
        for mesh_idx in range(self.nelements()):
            el = self.elements[mesh_idx]

            # Index correspondence happens here -- the skeleton
            # elements are assigned indices in the order that their
            # corresponding real elements are created/assigned.
            # (Skeletonelement3d.realelement sets self.meshindex when it
            # creates the real element.)
            mnodecount += el.realelement_shares(self, realmesh, mesh_idx, fe_node,
                                         mnodecount, edict, set_materials)
            if pbar.query_stop() !=0 \
                   or pbar.get_success() is progressbar.FAILED:
                pbar.set_failure()
                pbar.set_progress(1)
                pbar.set_message("Interrupted")
                return
            else:
                pbar.set_progress(1.0*(mesh_idx+1)/numelements)
                pbar.set_message("Allocating elements: %d/%d"%(mesh_idx+1, numelements))

        # Then do boundaries.
        # Note that edgeboundaries and pointboundaries are in separate lists
        # in the skeleton, but in a single list in the real mesh.

        # Point boundaries first.
        dict_size = len(self.pointboundaries)
        dict_index = 0
        for bdkey, pointbndy in self.pointboundaries.items():
            realbndy = realmesh.newPointBoundary(bdkey)
            for node in pointbndy.nodes:
                realbndy.addNode(fe_node[node]) # Preserve order of nodes.
                if pbar.query_stop() !=0 \
                       or pbar.get_success() is progressbar.FAILED:
                    pbar.set_failure()
                    pbar.set_progress(1)
                    pbar.set_message("Interrupted")
                    return
                else:
                    pbar.set_progress(1.0*(dict_index+1)/dict_size)
                    pbar.set_message("Allocating point boundaries: %d/%d"%(dict_index+1, dict_size))
            dict_index +=1
        # ... then edge boundaries.
        dict_size = len(self.edgeboundaries)
        dict_index = 0
        for bdkey, edgebndy in self.edgeboundaries.items():
            edgebndy.sequence()
            realbndy = realmesh.newEdgeBoundary(bdkey)
            for skeletonedge in edgebndy.edges:
                # Look up the corresponding element from the skeleton.
                skelel = skeletonedge.segment.getElements()[0]
                realel = realmesh.getElement(skelel.meshindex)
                
                edge_nodes = skeletonedge.get_nodes()
                realn0 = fe_node[edge_nodes[0]]    # First real node.
                realn1 = fe_node[edge_nodes[1]]    # Second real node.
                realbndy.addEdge(realel.getBndyEdge(realn0,realn1))
                if pbar.query_stop() !=0 \
                       or pbar.get_success() is progressbar.FAILED:
                    pbar.set_failure()
                    pbar.set_progress(1)
                    pbar.set_message("Interrupted")
                    return
                else:
                    pbar.set_progress(1.0*(dict_index+1)/dict_size)
                    pbar.set_message("Allocating edge boundaries: %d/%d"%(dict_index+1, dict_size))
            dict_index +=1
        return realmesh

########################## end femesh_shares ###############################

## end of class Skeleton

########################################################################


def newEmptySkeleton(name, msname, left_right_periodicity=False,
             top_bottom_periodicity=False,
             front_back_periodicity=False):
    mscontext = microstructure.microStructures[msname]
    ms = mscontext.getObject()
    skel = Skeleton(ms, left_right_periodicity, top_bottom_periodicity, front_back_periodicity)
    skeletoncontext.skeletonContexts.add([msname, name], skel, parent=mscontext)
    return skel

# skeleton_geometry is an object of type SkeletonGeometry, class defined above.
def initialSkeleton(name, ms, nx, ny, nz, skeleton_geometry):
    skel = skeleton_geometry(nx, ny, nz, ms)
    if skel is not None:
        mscontext = microstructure.microStructures[ms.name()]
        skeletoncontext.skeletonContexts.add([ms.name(), name],
                                             skel, parent=mscontext)
    return skel

# Parallel initial skeleton
if parallel_enable.enabled():
    def initialSkeletonParallel(name, ms, nx, ny, nz, skeleton_geometry):
        from ooflib.engine.IO import skeletonIPC
        skeletonIPC.smenu.Initialize(name=name, microstructure=ms,
                                     x_elements=nx, y_elements=ny,
                                     skeleton_geometry=skeleton_geometry)

# Create pixel-to-element skeleton. Thus, homogeneity of all elements will
# be set to "1".
def simpleSkeleton(name, ms, nx, ny, nz, skeleton_geometry):
    skel = skeleton_geometry(nx, ny, nz, ms, preset_homog=True)
    mscontext = microstructure.microStructures[ms.name()]
    skeletoncontext.skeletonContexts.add([ms.name(), name], skel,
                                         parent=mscontext)
    return skel

###########################

## TODO: Remove the 'skeleton' argument in all ProvisionalChanges
## methods, because self.skeleton can now be used instead.  Should do
## same thing in DeputyProvisionalChanges?

class ProvisionalChanges:
    def __init__(self, skeleton):
        self.skeleton = skeleton        # Skeleton object. Not context.
        self.removed = []               # elements to be removed 
        self.inserted = []              # provisional elements added
        self.substitutions = []         # pairs (old, new) of el. substitutions
        self.seg_subs = {}              # {old:[new segs] ...}
        self.movednodes = []            # list of MoveNode objects
        self.cachedDeltaE = None        # Energy difference
        self.cachedDeltaEBound = None        # Energy difference
        self.before = None              # Elements before the change
        self.after = None               # Elements after the change
    def removeAddedNodes(self, skeleton):
        # redefined by subclasses that add nodes
        pass
            
    class MoveNode:                     # nested class definition
        def __init__(self, node=None, position=None, mobility=None):
            self.node = node
            self.position = position
            self.mobility = mobility

    def removeElements(self, *elements):
        for element in elements:
            self.removed.append(element)

    def insertElements(self, *elements):
        for element in elements:
            self.inserted.append(element)

    def substituteElement(self, old, new):
        # Old and new elements must have the same number of nodes, and
        # corresponding nodes must be in the same positions in the
        # element's node lists, so that the correct parent-child
        # relationships may be made for the corresponding segments.
        self.substitutions.append([old, new])
        self.removed.append(old)

    def substituteSegment(self, old, new):  # "new" has to be a list
        self.seg_subs[old] = new

    def moveNode(self, node, position, mobility=(1,1,1)):
        self.movednodes.append(
            self.MoveNode(node=node, position=position, mobility=mobility))

    def nRemoved(self):
        return len(self.removed)

    def nInserted(self):
        return len(self.inserted)

    def elBefore(self):
        if self.before is None:
            self.before = self.removed + [o for o,n in self.substitutions]
            for mvnode in self.movednodes:
                # TODO: Should this be aperiodic?
                for nbr in mvnode.node.aperiodicNeighborElements():
                    if nbr not in self.before and nbr is not None:
                        self.before.append(nbr)
        return self.before

    def elAfter(self):
        if self.after is None:
            self.after = self.inserted + [n for o,n in self.substitutions]
            for mvnode in self.movednodes:
                # TODO: Should this be aperiodic?
                for nbr in mvnode.node.aperiodicNeighborElements():
                    if (nbr not in self.removed) and (nbr not in self.after):
                        self.after.append(nbr)
        return self.after

    def makeNodeMove(self, skeleton):
        for mvnode in self.movednodes:
            mvnode.node.moveTo(mvnode.position)

    def moveNodeBack(self, skeleton):
        for mvnode in self.movednodes:
            mvnode.node.moveBack()        

    def illegal(self, skeleton):
        # Will this change produce any illegal elements?
        verboten = 0
        # Move nodes accordingly to simulate the change
        self.makeNodeMove(self.skeleton)
        # Check elements
        for element in self.elAfter():
            if element.illegal():
                verboten = 1
                break
        # Move nodes back
        self.moveNodeBack(self.skeleton)
        return verboten

    def deltaE(self, skeleton, alpha):
        # Return the change in energy per element if this move were to
        # be accepted.
        if self.cachedDeltaE is None:
            # Energy before the change
            oldE = 0.0
            for element in self.elBefore():
                oldE += element.energyTotal(self.skeleton, alpha)
            oldE /= len(self.elBefore())
            # Move nodes accordingly to simulate the change
            self.makeNodeMove(self.skeleton)
            # Energy after the change
            newE = 0.0
            for element in self.elAfter():
                newE += element.energyTotal(self.skeleton, alpha)
            if len(self.elAfter()) != 0:
                newE /= len(self.elAfter())
            # Move node back
            self.moveNodeBack(self.skeleton)
            # Energy differnce due to the change
            self.cachedDeltaE = newE - oldE
        return self.cachedDeltaE

    def deltaEBound(self, skeleton, alpha):
        # Return the maximum possible deltaE -- assuming all elements
        # become homogenous after the change
        if self.cachedDeltaEBound is None:
            # Energy before the change
            oldE = 0.0
            for element in self.elBefore():
                oldE += element.energyTotal(self.skeleton, alpha)
            oldE /= len(self.elBefore())
            # Move nodes accordingly to simulate the change
            self.makeNodeMove(self.skeleton)
            # Energy after the change
            newE = 0.0
            for element in self.elAfter():
                newE += (1.-alpha)*element.energyShape()
            newE /= len(self.elAfter())
            # Move node back
            self.moveNodeBack(self.skeleton)
            # Energy differnce due to the change
            self.cachedDeltaEBound = newE - oldE        
        return self.cachedDeltaEBound

    def accept(self, skeleton):
        # Create actual elements to replace the provisional ones.  The
        # actual elements replace their predecessors in the
        # ProvisionalChanges object, so that they're available to the
        # calling routine.
        self.inserted = [element.accept(self.skeleton) for element in self.inserted]
        for mvnode in self.movednodes:
            mvnode.node.moveTo(mvnode.position)
            if mvnode.mobility:
                mvnode.node.setMobilityX(mvnode.mobility[0])
                mvnode.node.setMobilityY(mvnode.mobility[1])
                mvnode.node.setMobilityZ(mvnode.mobility[2])
        for pair in self.substitutions:
            old, new = pair
            newelement = new.accept(self.skeleton)
            pair[1] = newelement
            oldsegments = old.getSegments(self.skeleton)
            newsegments = newelement.getSegments(self.skeleton)
            for oldseg, newseg in zip(oldsegments, newsegments):
                for parent in oldseg.getParents():
                    newseg.add_parent(parent)
                    parent.add_child(newseg)
            # Call Skeleton.removeElements only *after* the segment
            # parents have been reestablished, because removing the
            # elements may remove the segments from the skeleton.
            # self.skeleton.removeElements(old)
        for old in self.seg_subs.keys():
            new_segs = self.seg_subs[old]
            for new in new_segs:
                for parent in old.getParents():
                    new.add_parent(parent)
                    parent.add_child(new)
        self.skeleton.removeElements(*self.removed)


class ProvisionalInsertion(ProvisionalChanges):
    def __init__(self, skeleton):
        ProvisionalChanges.__init__(self, skeleton)
        self.addedNodes = []

    def addNode(self, node):
        self.addedNodes.append(node)
        
    def removeAddedNodes(self, skeleton):
        ## TODO: Remove argument and use self.skeleton instead?
        for n in self.addedNodes:
            n.destroy(self.skeleton)

class ProvisionalMerge(ProvisionalChanges):
    def __init__(self, skeleton, node0, node1):
        ProvisionalChanges.__init__(self, skeleton)
        self.node0 = node0
        self.node1 = node1
        
    def accept(self, skeleton):
        ## TODO: Remove argument and use self.skeleton instead?
        self.node0.makeSibling(self.node1)
        ProvisionalChanges.accept(self, self.skeleton)

