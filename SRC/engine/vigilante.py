# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import crandom
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import skeletonmodifier

class FixIllegal(skeletonmodifier.SkeletonModifier):
    def apply(self, oldskeleton, context):
        #skel = oldskeleton.properCopy(skeletonpath=context.path())
        # vigilante doesn't really need a properCopy!
        skel = oldskeleton.deputyCopy()
        skel.activate()
        # suckers is a *list* of illegal elements, used to loop over
        # them randomly.  illegalset is a *set* used to quickly tell
        # if an element is known to be illegal.  New elements can be
        # added to both if moving one node fixes two elements and
        # breaks one.
        suckers = list(skel.illegalElements())
        illegalset = {el for el in suckers}
        nguilty = len(suckers)

        # arbitrary number just to keep us out of an infinite loop
        maxiters = 222
        for iteration in range(maxiters):
            crandom.shuffle(suckers)
            movedsomething = self.smoothIllegalElements(
                skel, illegalset, suckers)
            if not movedsomething or len(illegalset) == 0:
                break

        ndone = nguilty - len(illegalset)
        if illegalset:
            reporter.warn("Could not remove all illegal elements!")
        reporter.report("%d illegal element%s removed."
                        % (ndone, "s"*(ndone!=1)))

        ## TODO: There are cases in which this doesn't work, that
        ## could be solved by moving a node *towards* the average
        ## position of its neighbors, but not all the way.  Try moving
        ## problem nodes until their elements become barely legal.

        skel.cleanUp()
        skel.checkIllegality()
        return skel

    def smoothIllegalElements(self, skel, illegalset, suckers):
        movedsomething = False
        for element in suckers:
            if element in illegalset:
                node_indices = list(range(element.nnodes()))
                crandom.shuffle(node_indices)
                for i in node_indices:
                    node = element.nodes[i]
                    #if element.getRealAngle(i) < 0.0:  # bad angle
                    if self.smoothTheNode(skel, node, illegalset, suckers):
                        movedsomething = True
        return movedsomething
    
    def smoothTheNode(self, skel, node, illegalset, suckers):
        # how many illegal elements?
        nguilty = 0
        for e in node.neighborElements(): #periodic?
            if e in illegalset:
                nguilty += 1

        # move a node to its average position w.r.t. its neighbor
        # nodes 
        # TODO 3D: create thing in primitives that returns zero
        # vector of appropriate dimension
        if config.dimension() == 2:
            avgPos = primitives.Point(0.,0.)
        elif config.dimension() == 3:
            avgPos = primitives.Point(0.,0.,0.)
        nbrNodes = node.neighborNodes(skel)
        for n in nbrNodes:
            avgPos += n.position()
        avgPos /= len(nbrNodes)
        skel.moveNodeTo(node, avgPos)
        
        # see if the move removed illegal elements
        still_guilty = []
        for e in node.neighborElements():
            if e.illegal():
                still_guilty.append(e)

        if nguilty <= len(still_guilty): # no improvement
            skel.moveNodeBack(node)
            return False

        # accept the move
        for e in node.neighborElements():
            estillguilty = e in still_guilty
            ewasguilty = e in illegalset
            if ewasguilty and not estillguilty:
                illegalset.remove(e)
            elif estillguilty and not ewasguilty:
                suckers.append(e)
                illegalset.add(e)
        return True
                
#########################

registeredclass.Registration(
    'Fix Illegal Elements', skeletonmodifier.SkeletonModifier,
    FixIllegal,
    ordering=99,
    ok_illegal = 1,  # It can deal with illegal skeletons 
    tip = 'Remove illegal elements from a Skeleton.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/fix_illegal.xml'),
    xrefs=["RegisteredClass-SkeletonIllegalElementDisplay"]
)
