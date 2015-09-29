# -*- python -*-
# $RCSfile: skeletonelement3d.py,v $
# $Revision: 1.14 $
# $Author: langer $
# $Date: 2014/09/27 21:40:56 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.common import coord
from ooflib.SWIG.common import config
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.engine import ooferror2
from ooflib.SWIG.engine import cskeleton
from ooflib.SWIG.engine import material
from ooflib.engine import skeletonselectable
import ooflib.SWIG.common.timestamp
import ooflib.common.microstructure
from ooflib.common import enum
from ooflib.common import debug
from ooflib.common import object_id
from ooflib.common import parallel_enable
from ooflib.common import primitives
from ooflib.engine import skeletonnode
import math

#########################################



class ElementShapeType(enum.EnumClass(('brick', 'topological equivalents of cubes'),
                                      ('tetra', 'tetrahedral elements'))):
    tip = "Shapes of Skeleton Elements."
    discussion = """<para>
    <classname>ElementShapeType</classname> objects are used in a few
    cases where it's necessary to distinguish between &elem; shapes in
    the &oof3d; commands.
    </para>"""
        


# The SkeletonElementBase is the base class for both the
# SkeletonElement and the ProvisionalElement.  It can compute
# geometrical stuff like homogeneity and shape energy, but knows
# nothing about selectability, segments, or neighbors.

class SkeletonElementBase:
    def __init__(self, nodes):
        self.nodes = nodes
        
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.nodes)

    def material(self, skeleton):
        dominantpixel = self.dominantPixel(skeleton.MS)
        if dominantpixel is not None:
            return material.getMaterialFromCategory(skeleton.MS, dominantpixel)

##     def underlyingPixels(self, microstructure):
##         # Returns a list of all pixels that overlap with this element.
## ##         dx, dy = microstructure.sizeOfPixels()
## ##         nx, ny = microstructure.sizeInPixels()
##         return self.underlying_pixels(microstructure) # C++

    def transitionPoint(self, skeleton, edgeno):
        ok, point = \
            cskeleton.CSkeletonElementPtr.transitionPoint(self, skeleton.MS,
                                                          edgeno)
        if ok:
            return point
    
    def energyTotal(self, skeleton, alpha):
        if alpha == 1:
            return self.energyHomogeneity(skeleton.MS)
        return alpha*self.energyHomogeneity(skeleton.MS) + \
               (1.-alpha)*self.energyShape()

##########################
        
class SkeletonElement(SkeletonElementBase,
                      skeletonselectable.SkeletonSelectable):
    def __init__(self, nodes, index):
        SkeletonElementBase.__init__(self, nodes)
        skeletonselectable.SkeletonSelectable.__init__(self, index)

        # Although the CSkeletonElement keeps a list of
        # CSkeletonNodes, the extra information in the Python
        # SkeletonNodes isn't available unless we keep a list of them
        # here, as well.  It's possible that we could move all the
        # extra info into the CSkeletonNode class and swig it.
        # Canonical ordering will still work, because it's based on
        # indices.
        self.nodes = nodes
        
        for node in nodes:
            node.addElement(self)
            
        # When a real mesh is made from the skeleton in which this
        # element lives, self.meshindex gets assigned the index of
        # that element.  This index is the same for all the real meshes.
        self.meshindex = None

        self.ID = object_id.ObjectID()

        # process ID (only meaningful in parallel mode)
        if parallel_enable.enabled():
            from ooflib.SWIG.common import mpitools
            self._procID = mpitools.Rank()
        else:
            self._procID = None

    #def __del__(self):
    #    pass

    # There may be some temptation to provide elements with an
    # index-based equality comparison function.  Doing this is
    # dangerous, as it screws up the parent/child addition machinery
    # in the parent SkeletonSelection class. 
        
    def repr_position(self):
        return self.center()

    def getIndex(self):
        return self.index

    def getNodeIndexIntoList(self,node):
        ## TODO OPT: This seems to be called a lot.  Why not create a
        ## lookup table, or store the index in the node?
        return self.nodes.index(node)

    def type(self):
        return self.shapetype

    def destroy(self, skeleton):
        self.disconnect()
        nnodes = self.nnodes()
        lastnode = self.nodes[-1]
        segments = self.getSegments(skeleton)
        for segment in segments:
            segment.removeElement(skeleton, self)
        for node in self.nodes:
            node.removeElement(skeleton, self)
            lastnode = node

##     # def getFEelement(self):
##     #     return self.element

    def getSegmentNodes(self, segmentId):
        # necessary in 3D because segments are no longer 1 to 1 with
        # nodes
        localIds = self.segToNodeMap()[segmentId]
        return [self.nodes[localIds[0]],self.nodes[localIds[1]]]
        

    def getSegments(self, skeleton):
        segments = []
        nsegments = self.getNumberOfEdges()
        for pair in self.segToNodeMap():
            n1 = self.nodes[pair[0]]
            n2 = self.nodes[pair[1]]
            segments.append(skeleton.findSegment(n1,n2))
        return segments
            

    def active(self, skeleton):
        for node in self.nodes:
            if node.active(skeleton):
                return 1
        return 0

    def new_child(self,index):
        raise ooferror.ErrPyProgrammingError(
            "Attempt to clone element parent class.")

    def segment_node_iterator(self):
        segment_nodes = []
        n = self.getNumberOfEdges()
        for i in range(n):
            segment_nodes.append(self.getSegmentNodes(i))
        return segment_nodes

##     def segment_iterator(self, skel):
##         segments = []
##         for i in range(self.nnodes()):
##             n0 = self.nodes[i]
##             n1 = self.nodes[(i+1)%self.nnodes()]
##             segments.append(skel.findSegment(n0, n1))
##         return segments

##     def edgeNeighbors(self, skeleton, loopRange=0):
##         # Search for edge-sharing neighborhood for a given element and return
##         # a list of them.
##         nnodes = self.nnodes()
##         edgeNeighborList = [None]*nnodes
##         for i in range(nnodes):
##             segment = skeleton.findSegment(self.nodes[i],
##                                            self.nodes[(i+1)%nnodes])
##             if segment is not None:
##                 edgeNeighborList[i] = segment.getOtherElement(self)

##             # this should only work if the segment is on a periodic boundary
##             # in which case the above call to getOtherElement should have
##             # returned nothing
##             partners = self.nodes[i].getPartnerPair(self.nodes[(i+1)%nnodes])
##             if partners is not None:
##                 segment = skeleton.findSegment(partners[0],partners[1])
##                 if segment is not None:
##                     edgeNeighborList[i] = segment.getOtherElement(self)

##         return edgeNeighborList

##     def getEdgeLengthsList(self):
##         list = []
##         for i in range(self.nnodes()):
##             list.append(self.edgeLength(i))
##         return list

##     def getShortestEdge(self):
##         list = self.getEdgeLengthsList()
##         minEdge = list[0]
##         index = 0
##         for i in range(1, self.nnodes()):
##             if list[i] < minEdge:
##                 minEdge = list[i]
##                 index = i
##         return index
    
    def getAnglesByFace(self):
        list = []
        numFaces = self.getNumberOfFaces()
        faceToNodeMap = self.faceToNodeMap()
        for i in range(numFaces):
            faceangles = []
            for j in range(len(faceToNodeMap[i])):
                faceangles.append(self.cosCornerAngle(i,j))
            list.append(faceangles)
        return list


    def getSolidAnglesList(self):
        list = []
        for i in range(self.nnodes()):
            list.append(self.solidCornerAngle(i))
        return list

    def getDihedralAnglesList(self):
        list = []
        for f1,f2 in self.segToFaceMap():
            list.append(self.cosDihedralAngle(f1,f2));
        return list;
            
    
##     def getBiggestAngle(self):
##         list = self.getAnglesList()
##         maxAngle = list[0]  # cosine of the angle
##         index = 0
##         for i in range(1, self.nnodes()):
##             if list[i] < maxAngle:
##                 maxAngle = list[i]
##                 index = i
##         return index

    def getSister(self, skeleton, sharedNodes):
         # returns the element that shares a face defined by sharedNodes
         elements = []
         numNodes = len(sharedNodes)
         for node in sharedNodes:
             elements.extend(node.aperiodicNeighborElements(skeleton))
         for e in elements:
             if elements.count(e) == numNodes and e is not self:
                 return e
         return None
    
    def getSisterPeriodic(self, skeleton, sharedNodes):
         # returns the element that shares a face defined by sharedNodes
         elements = []
         numNodes = len(sharedNodes)
         for node in sharedNodes:
             elements.extend(node.neighborElements(skeleton))
         for e in elements:
             if elements.count(e) == numNodes and e is not self:
                 return e
         return None

##     def replacementNodes(self, oldnode, newnode):
##         nodelist = self.nodes[:]
##         which = nodelist.index(oldnode)
##         nodelist[which] = newnode
##         return nodelist

    def getPositionHash(self):
        sortedpositions = [n.position() for n in self.nodes]
        sortedpositions.sort()
        hashable = []
        for pos in sortedpositions:
            for i in range(3):
                hashable.append(pos[i])
        return hash(tuple(hashable))

    def realelement(self, skeleton, mesh, index, fe_node,
                    curnodeindex, elemdict, materialfunc):
        # Create a real element corresponding to this skeleton
        # element. The elemdict argument is a dictionary (keyed by the
        # number of sides of the element) of MasterElement objects,
        # which contain the information needed to construct the real
        # elements.  "index" is the SkeletonElement's position in the
        # Skeleton's list, and "fe_node" is a dictionary of real nodes
        # in the FEMesh, indexed by their corresponding SkeletonNode
        # objects.  The lists give the nodes in the order in which
        # they were added to the element.
        
        # Be safe with indices.
        if self.meshindex is None: # Zero is nontrivial index.
            self.meshindex = index
        else:
            if index != self.meshindex:
                raise ooferror2.ErrPyProgrammingError(
                    "Index mismatch in element construction.")
                
        nnewnodes = 0
        ncn = len(self.nodes) # Corner nodes.

        # elemdict is a dictionary of MasterElements, keyed by number
        # of sides.
        elementtype = elemdict[self.nnodes()]
        nodes = []                      # real nodes for this element

        for i in range(len(self.nodes)):  # i.e. for each edge...
            c0 = self.nodes[i]
            nodes.append(fe_node[c0])     # Corner nodes already exist.
            c1 = self.nodes[(i+1)%ncn]
            cset = skeletonnode.canonical_order(c0, c1)

            # Look up this edge in the dictionary.  If it's there,
            # then nodes have been created on the edge already, and we
            # should reuse them.

            try:
                xtranodes = mesh.getEdgeNodes(cset)
                # The nodes were created by the neighboring element.
                # Since elements traverse their edges counterclockwise
                # when creating nodes, the preexisting nodes are in
                # the wrong order for the current element.
                xtranodes.reverse()
            except KeyError:
                # The edge wasn't in the dictionary.  It's a new edge.
                xtranodes  = []
                # Loop over all protonodes on the current
                # edge of the new element
                for newproto in elementtype.protodic[i]:
                    masterxy = primitives.Point(newproto.mastercoord()[0],
                                           newproto.mastercoord()[1])
                    realxyz = self.frommaster(masterxyz, 0)
                    newnode = _makenewnode(mesh, newproto,
                                           coord.Coord(realxyz.x, realxyz.y, realxyz.z))
                    nnewnodes = nnewnodes + 1
                    xtranodes.append(newnode)
                mesh.addEdgeNodes(cset, xtranodes)

            nodes = nodes + xtranodes

        # Interior nodes at the end.
        for newproto in elementtype.protodic['interior']:
            masterxy = primitives.Point(newproto.mastercoord()[0],
                                        newproto.mastercoord()[1])
            realxyz = self.frommaster(masterxyz, 0)
            newnode = _makenewnode(mesh, newproto,
                                   coord.Coord(realxyz.x, realxyz.y, realxyz.z))
            nnewnodes = nnewnodes + 1
            nodes.append(newnode)
            mesh.addInternalNodes(self, newnode)

        # Having constructed the list of nodes, call the real
        # element's constructor.
        realel = elementtype.build(self, materialfunc(self, skeleton), nodes)
        # Long-lost cousin of Kal-El and Jor-El.
        
        mesh.addElement(realel)               # Add to mesh.
        # Tell the element about its exterior edges.
        #for edge in self.exterior_edges:
        #    realel.set_exterior(fe_node[edge[0]], fe_node[edge[1]])

        return nnewnodes

    def realmaterial(self, skeleton):
        return self.material(skeleton)


class ProvisionalElement(SkeletonElementBase):
    def __init__(self, nodes, parents):
        SkeletonElementBase.__init__(self, nodes)
        self.parents = parents
    def accept(self, skeleton):
        element = skeleton.newElement(self.nodes, parents=self.parents)
        element.copyHomogeneity(self)
        return element

#####################################################    



class SkeletonTetra(SkeletonElement, cskeleton.CSkeletonTetra):
    # four nodes,  four triangle faces, 6 segments
    def __init__(self,nodes,index):
        cskeleton.CSkeletonTetra.__init__(self, *nodes)
        SkeletonElement.__init__(self,nodes,index)
        self.shapetype = ElementShapeType('tetra')

    # If we find ourselves needing these maps in C, we should move
    # them there.  For now, keep as Python objects.
    def segToNodeMap(self):
        # the order indicates the direction of the edge
        return [(0,1),(1,2),(2,0),(0,3),(1,3),(2,3)]

    def faceToNodeMap(self):
        return [(0,1,3),(1,2,3),(2,0,3),(0,2,1)]

    # maps segments to the two faces they border
    def segToFaceMap(self):
        return [(0,3),(1,3),(2,3),(0,2),(0,1),(1,2)]

    @staticmethod
    def opposingSegsList():
        return [(0,5), (1,3), (2,4)]

    def new_child(self, index):
        node_children = [ x.getChildren()[-1] for x in self.nodes ]
        new = SkeletonTetra(node_children, index)
        new.copyHomogeneity(self)
        return new

        

class ProvisionalTetra(ProvisionalElement, cskeleton.CSkeletonTetra):
    def __init__(self, nodes, parents):
        cskeleton.CSkeletonTetra.__init__(self, *nodes)
        ProvisionalElement.__init__(self, nodes, parents)

    def onBoundary(self, skel):
        # check if all node positions are on a boundary, so that we
        # can leave this element out if it if flattened TODO 3D: add
        # conditions such that it returns false if boundary is
        # periodic
        size = skel.MS.size()
        pos = [node.position() for node in self.nodes]
        for i in range(3):
            if pos[0][i]==0.0 and pos[1][i]==0.0 and pos[2][i]==0.0 and pos[3][i]==0.0:
                return True
            if pos[0][i]==size[i] and pos[1][i]==size[i] and pos[2][i]==size[i] and pos[3][i]==size[i]:
                return True
        return False


def getProvisionalElement(nodes, parents):
    if len(nodes) == 4:
        return ProvisionalTetra(nodes, parents)

###########################

def _makenewnode(mesh, protonode, coord):
    """Make a new node in mesh at coord, given a protonode."""
    if protonode.func():
        return mesh.newFuncNode(coord)
    return mesh.newMapNode(coord)

def _makenewnode_shares(mesh, protonode, coord,
                        edgenode0, edgenode1, newindex, protocount,
                        protodiclength, maxnnodes):
    if protonode.func():
        newProcList=[]
        newRemoteIndexList=[]
        #Find the processes that share both edgenode0 and edgenode1.
        #In this scheme, the same index for the node gets used by the sharing processes
        for procs0 in edgenode0.sharedWith():
            for procs1 in edgenode1.sharedWith():
                if procs0==procs1:
                    newProcList.append(procs0)
                    remoteindex0=edgenode0.remoteIndex(procs0)
                    remoteindex1=edgenode1.remoteIndex(procs1)
                    #The sense of edge traversal is from remoteindex1 to remoteindex0 in procs0
                    if remoteindex1 < remoteindex0:
                        newremoteindex=maxnnodes+100*remoteindex1+protodiclength- \
                                        protocount-1
                    else:
                        newremoteindex=maxnnodes+100*remoteindex0+50+protodiclength- \
                                        protocount-1
                    newRemoteIndexList.append(newremoteindex)
##        print "procs", newProcList
##        print "remoteindex", newRemoteIndexList
##        print "index", newindex
##        print "c0", edgenode0.index
##        print "c1", edgenode1.index
##        print "--------"
        return mesh.newFuncNode_shares(coord,
                                       newProcList,
                                       newRemoteIndexList,
                                       newindex)
    #Don't know yet how to handle mapnodes
    return mesh.newMapNode(coord)

############################

