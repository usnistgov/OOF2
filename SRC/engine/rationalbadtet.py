# -*- python -*-
# $RCSfile: rationalbadtet.py,v $
# $Revision: 1.10 $
# $Author: langer $
# $Date: 2014/09/27 21:40:55 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common import utils
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import rationalize
from ooflib.engine import skeletonelement3d
from ooflib.engine import skeleton3d as skeleton


import math

Rationalizer = rationalize.Rationalizer
ProvisionalChanges = skeleton.ProvisionalChanges
ProvisionalTetra = skeletonelement3d.ProvisionalTetra
SkeletonTetra = skeletonelement3d.SkeletonTetra

degree2radian = math.pi/180
degreesq2radiansq = degree2radian*degree2radian

class RemoveBadTetrahedra(Rationalizer):

    def __init__(self, acute_angle, obtuse_angle): 
        self.acute_angle = acute_angle
        self.obtuse_angle = obtuse_angle
        self.acute = math.cos(acute_angle*degree2radian)
        self.obtuse = math.cos(obtuse_angle*degree2radian)
        # for now we assume that the square of the bad angles given by
        # the user can be used to determine bad solid angles.  TODO
        # MAYBE: we might want to add another user option for this.
        self.small_solid = self.acute_angle*self.acute_angle*degreesq2radiansq
        self.large_solid = self.obtuse_angle*self.obtuse_angle*degreesq2radiansq


    def findAndFix(self, skel, element):
        anglesByFace = element.getAnglesByFace()
        solidAngles = element.getSolidAnglesList()
        dihedralAngles = element.getDihedralAnglesList()
        #print [[math.acos(angle)/degree2radian for angle in angles] for angles in anglesByFace]
        #print [angle/degreesq2radiansq for angle in solidAngles]
        #print [math.acos(angle)/degree2radian for angle in dihedralAngles]

        obtuse_angles = []
        acute_angles = []
        for i in range(len(anglesByFace)):
            for j in range(len(anglesByFace[i])):
                if anglesByFace[i][j] <= self.obtuse:
                    obtuse_angles.append((i,j))
                if anglesByFace[i][j] >= self.acute:
                    acute_angles.append((i,j))

        large_solid_angles = []
        small_solid_angles = []
        for i in range(len(solidAngles)):
            if solidAngles[i] <= self.small_solid:
                small_solid_angles.append(i)
            if solidAngles[i] >= self.large_solid:
                large_solid_angles.append(i)
        # if there are three small solid angles, we treat the fourth as a large angle
        if len(small_solid_angles) == 3:
            large_solid_angles = [id for id in range(4) if id not in small_solid_angles]

        large_dihedral_angles = []
        small_dihedral_angles = []
        for i in range(len(dihedralAngles)):
            if dihedralAngles[i] <= self.obtuse:
                large_dihedral_angles.append(i)
            if dihedralAngles[i] >= self.acute:
                small_dihedral_angles.append(i)

#         print obtuse_angles
#         print acute_angles
#         print large_solid_angles
#         print small_solid_angles
#         print large_dihedral_angles
#         print small_dihedral_angles
#         print "\n\n"

        if len(obtuse_angles)+len(acute_angles)+len(large_solid_angles)+len(small_solid_angles)+\
                len(large_dihedral_angles)+len(small_dihedral_angles)==0:
            return []

        return self.fix(skel, element, obtuse_angles, acute_angles, large_solid_angles,
                        small_solid_angles, large_dihedral_angles, small_dihedral_angles)


    def fixAll(self, skel, element):
        pass

    def fix(self, skel, element, obtuse_angles, acute_angles, large_solid_angles,
            small_solid_angles, large_dihedral_angles, small_dihedral_angles):
        return _removeBadTetra(skel, element, obtuse_angles, acute_angles, large_solid_angles,
                               small_solid_angles, large_dihedral_angles, small_dihedral_angles)


registeredclass.Registration(
    'Remove Bad Tetrahedra',
    Rationalizer,
    RemoveBadTetrahedra,
    gerund = 'removing bad tetrahedra',
    ordering=20000,                     # do this last!
    params=[
    parameter.FloatRangeParameter('acute_angle', (0.0, 45.0, 0.5),
                                  value = 15.0,
                                  tip = 'Minimum acceptable acute interior angle, in degrees'),
    parameter.FloatRangeParameter('obtuse_angle', (90.0, 180.0, 1.0),
                                  value = 150.0,
                                  tip = 'Maximum acceptable obtuse interior angle, in degrees')],
    tip = 'Remove triangles with extreme interior solid angles.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/ration_sharp.xml'))

def _removeBadTetra(skel, element, obtuse_angles, acute_angles, large_solid_angles, 
                    small_solid_angles, large_dihedral_angles, small_dihedral_angles):

    faceToNodeMap = element.faceToNodeMap()

    changes = []
    
    # merge nodes opposite an acute face angle
    for i,j in acute_angles:
        facenodes = faceToNodeMap[i]
        node0 = element.nodes[facenodes[(j+1)%3]]
        node1 = element.nodes[facenodes[(j+2)%3]]
        changes.append(skel.mergeNode(node0, node1))
        changes.append(skel.mergeNode(node1, node0))

    # handle tets with a large solid angle - either flatten or do a 2
    # to 3 split with the neighbor on the opposing face, if any
    for obtusenodeidx in set(large_solid_angles) | set([faceToNodeMap[i][j] for i,j in obtuse_angles]):
        for k in range(len(faceToNodeMap)):
            if obtusenodeidx not in faceToNodeMap[k]:
                oppfacenodes = [element.nodes[l] for l in faceToNodeMap[k]]
        borderelement = element.getSisterPeriodic(skel, oppfacenodes)
        if borderelement is not None:
            for node in borderelement.nodes:
                if node not in oppfacenodes:
                    oppnode = node
            changes.extend(_tetTetSplit(skel, element.nodes[obtusenodeidx], 
                                       oppnode, element, borderelement))
        else:
            changes.extend(_tetNoneSplit(skel, element.nodes[obtusenodeidx], element))

    # flatten tets with two large dihedral angles on opposite segments
    # and split elements that share those segments.
    if tuple(large_dihedral_angles) in SkeletonTetra.opposingSegsList():
       changes.extend(_removeFlat(skel, large_dihedral_angles, element))
        

    return changes

def _midpoints(skel, node0, node1):
    n0pos = node0.position()
    n1pos = node1.position()
    partners = node0.getPartnerPair(node1)
    if not partners:
        return 0.5*(n0pos + n1pos), None

        # TODO 3D: fill in periodic case!

def _centroidAndMidpoints(skel, nodes):
    n = len(nodes)
    points = []
    pairs = [(nodes[i],nodes[(i+1)%n]) for i in range(n)]
    periodic = True
    for n0,n1 in pairs:
        points.append(_midpoints(skel,n0,n1))
        periodic = periodic and (points[-1][1] is not None)
    centroid = primitives.Point(0.0,0.0,0.0)
    for node in nodes:
        centroid += (1.0/n)*node.position()
    if not periodic:
        partner = None
    # TODO 3D: fill in case where we need the periodic partner of the centroid
    points.append((centroid,partner))
    return points

def _getMobility(nodes):
    mob_x = False
    mob_y = False
    mob_z = False
    for node in nodes:
        mob_x = mob_x or node.movable_x()
        mob_y = mob_y or node.movable_y()
        mob_z = mob_z or node.movable_z()
    return (mob_x, mob_y, mob_z)

def _tetNoneSplit(skel, obtusenode, tet):
    changes = []
    
    for face in tet.faceToNodeMap():
        facenodes = [tet.nodes[i] for i in face]
        if obtusenode not in facenodes:
            oppnodes = facenodes
    midpoints = _centroidAndMidpoints(skel, oppnodes)
    centroid = midpoints[3][0]

    if obtusenode.canMoveTo(centroid):
        change = skeleton.ProvisionalChanges(skel)
        change.moveNode(obtusenode, centroid, _getMobility(oppnodes))
        change.removeElements(tet)
        changes.append(change)

    for i in range(3):
        midpoint = midpoints[i][0]
        if obtusenode.canMoveTo(midpoint):
            change = skeleton.ProvisionalChanges(skel)
            change.moveNode(obtusenode, midpoint, _getMobility([oppnodes[i], oppnodes[(i+1)%3]]))
            # we also need to remove the second tet that is collapsed,
            # if any
            sharednodes = [obtusenode, oppnodes[i], oppnodes[(i+1)%3]]
            collapsedelement = tet.getSisterPeriodic(skel, sharednodes)
            change.removeElements(tet)
            if collapsedelement is not None:
                change.removeElements(collapsedelement)
            changes.append(change)
    
    return changes


# helper function for splitting an element in half, given a midpoint
def _splitElementInHalf(el, pair, new, change, skel):
    change.removeElements(el)
    newels = []
    for old in pair:
        nodes = el.nodes[:]
        idx = nodes.index(old)
        nodes[idx]=new
        tet = ProvisionalTetra(nodes,parents=[el])
        if not tet.onBoundary(skel):   
            change.insertElements(tet)


def _tetTetSplit(skel, obtusenode, oppnode, tet1, tet2):
    # obtusenode is the node in tet1 with a large solid angle, oppnode
    # is the node in tet2 that is NOT shared between tet1 and tet2.

    # TODO 3D: Update this for periodic skeletons

    changes = []
    faces = tet2.faceToNodeMap()

    unSharedFaces = []
    for face in faces:
        if oppnode in [tet2.nodes[i] for i in face]:
            unSharedFaces.append(face)
        tet1facenodes = [tet1.nodes[i] for i in face]
        if obtusenode not in tet1facenodes:
            sharedNodes = tet1facenodes
    midpoints = _centroidAndMidpoints(skel, sharedNodes)
    periodic = midpoints[-1][1] is not None


    # first just split the two into three, without moving the obtusenode
    if not periodic:
        change = skeleton.ProvisionalChanges(skel)
        change.removeElements(tet1, tet2)
        parents = tet1.getParents() + tet2.getParents()
        tetra = []
        for face in unSharedFaces:
            nodes = [tet2.nodes[i] for i in face]
            nodes.reverse()
            nodes.append(obtusenode)
            change.insertElements(ProvisionalTetra(nodes,parents=parents))
        changes.append(change)

        # for the first three midpoints, we can move the node to the
        # midpoint of the segment and split neighbors that share the
        # segment, or we can not move the node and just split the
        # neighbors
        for i in range(3):
            # the nodes that define this particular midpoint
            pair = (sharedNodes[i],sharedNodes[(i+1)%3])
            midpoint = midpoints[i][0]
            collapsedfacenodes = [obtusenode, pair[0], pair[1]]
            collapsedtet = tet1.getSisterPeriodic(skel, collapsedfacenodes)
            segment = skel.findSegment(pair[0],pair[1])
            splitelements = segment.getElements()[:]
            splitelements.remove(tet1)
            if collapsedtet in splitelements:
                splitelements.remove(collapsedtet)
            if obtusenode.canMoveTo(midpoint):
                change = skeleton.ProvisionalChanges(skel)
                change.moveNode(obtusenode, midpoint, _getMobility(pair))
                change.removeElements(tet1)
                if collapsedtet is not None:
                    change.removeElements(collapsedtet)
                for el in splitelements:
                    _splitElementInHalf(el, pair, obtusenode, change, skel)
                changes.append(change)
            # now, without moving the node
            if not segment.isExternal(skel.MS):
                change = skeleton.ProvisionalChanges(skel)
                change.removeElements(tet1)
                if collapsedtet is not None:
                    change.removeElements(collapsedtet)
                for el in splitelements:
                    _splitElementInHalf(el, pair, obtusenode, change, skel)
                changes.append(change)
      

        # also try collapsing the obtuse node to the midpoint
        centroid = midpoints[3][0]
        if obtusenode.canMoveTo(centroid):
            change = skeleton.ProvisionalChanges(skel)
            change.moveNode(obtusenode, centroid, _getMobility(sharedNodes))
            change.removeElements(tet1, tet2)
            tetra = []
            for face in unSharedFaces:
                nodes = [tet2.nodes[i] for i in face]
                nodes.reverse()
                nodes.append(obtusenode)
                change.insertElements(ProvisionalTetra(nodes,parents=tet2.getParents()))
            changes.append(change)

    return changes


def _removeFlat(skel, segs, element):
    # get the pairs of nodes that define the two segs with large
    # dihedral angles
    nodes = [ [element.nodes[i] for i in element.segToNodeMap()[segs[i]]] for i in range(2)]
    # get the midpoints of those two segs
    midpoints = [ _midpoints(skel, nodes[i][0], nodes[i][1]) for i in range(2)]
    # the splitpoints are each of the above midpoints as well as their
    # average, unless one of the segments is on an outside face - in
    # that case, only use that segment's midpoint
    if skel.findSegment(nodes[0][0],nodes[0][1]).isExternal(skel.MS):
        splitpoints = [midpoints[0][0]]
    elif  skel.findSegment(nodes[1][0],nodes[1][1]).isExternal(skel.MS):
        splitpoints = [midpoints[1][0]]
    else:
        splitpoints = [0.5*(midpoints[0][0]+midpoints[1][0]), midpoints[0][0], midpoints[1][0]]
    changes = []
    for point in splitpoints:
        new = skel.newNodeFromPoint(point)
        change = skeleton.ProvisionalInsertion(skel)
        change.addNode(new)
        change.removeElements(element)
        for i in range(2):
            segment = skel.findSegment(nodes[i][0], nodes[i][1])
            splitelements = segment.getElements()[:]
            splitelements.remove(element)
            for el in splitelements:
                _splitElementInHalf(el, nodes[i], new, change, skel)
        changes.append(change)
    return changes
           
    
