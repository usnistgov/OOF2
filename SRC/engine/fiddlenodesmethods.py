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
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import parallel_enable
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import deputy
from ooflib.engine import fiddlenodesbase
from ooflib.engine import skeletonmodifier

from functools import reduce


FiddleNodes = fiddlenodesbase.FiddleNodes
FiddleNodesTargets = fiddlenodesbase.FiddleNodesTargets
IterationManager = fiddlenodesbase.IterationManager


class AnnealMovePosition(fiddlenodesbase.FiddleNodesMovePosition):
    def __init__(self, delta):
        self.delta = delta

    def __call__(self, skeleton, node):
        px, py = skeleton.MS.sizeOfPixels()
        dx = crandom.gauss(0.0, self.delta*px)
        dy = crandom.gauss(0.0, self.delta*py)
        return primitives.Point(node.position()[0]+dx,
                                node.position()[1]+dy)
        
    
registeredclass.Registration(
    'Anneal Move Position',
    fiddlenodesbase.FiddleNodesMovePosition,
    AnnealMovePosition,
    ordering=0,
    params = [
    parameter.FloatParameter(
        "delta", 1.0,
        tip='width of gaussian distribution of node motions, in pixel units')
    ])


class Anneal(FiddleNodes, skeletonmodifier.SkeletonModifier):
    def __init__(self, targets, criterion, T, delta, iteration):
        FiddleNodes.__init__(self, targets, criterion, T, iteration)
        self.delta = delta
        self.intro = "Preparing to anneal skeleton...      "
        self.header = "Annealing skeleton: "
        self.outro = "Annealing done: "
        self.movedPosition = AnnealMovePosition(self.delta)

if parallel_enable.enabled():
    from ooflib.engine import fiddlenodesbaseParallel
    Anneal.coreProcess_parallel = fiddlenodesbaseParallel._annealCoreProcess


registeredclass.Registration(
    'Anneal',
    skeletonmodifier.SkeletonModifier,
    Anneal,
    ordering=3,
    params=[
        parameter.RegisteredParameter(
            'targets', FiddleNodesTargets, tip='Which nodes to move.'),
        parameter.RegisteredParameter(
            'criterion', skeletonmodifier.SkelModCriterion,
            tip = 'Acceptance criterion'),
        parameter.FloatParameter(
            'T', value = 0.0,
            tip='Failed moves will be accepted if T>0 and exp(-diffE/T) > r, where diffE is the energy gained and r is a random number between 0 and 1.'),
        parameter.FloatParameter(
            'delta', value=1.0,
            tip='Width of the distribution of attempted node motions, in units of the pixel size.'),
        parameter.RegisteredParameter(
            'iteration', IterationManager, tip='Iteration method.')
    ],
    tip='Move nodes randomly to improve element shape and homogeneity.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/anneal.xml')
    )

#################################################

class SmoothMovePosition(fiddlenodesbase.FiddleNodesMovePosition):
    def __call__(self, skeleton, node):
        if parallel_enable.enabled():
            if node.isShared():  # Implicitly, it's mine too.
                return self.active(skeleton, node)

        if config.dimension() == 2:
            avgPos = primitives.Point(0.,0.)
        elif config.dimension() == 3:
            avgPos = primitives.Point(0.,0.,0.)
        nbrNodes = node.neighborNodes(skeleton)

        for n in nbrNodes:
            avgPos += skeleton.nodePosition(n)
        avgPos /= len(nbrNodes)
        return avgPos

    # not updated for 3d
    if parallel_enable.enabled():
        def active(self, skeleton, node):  # Parallel mode -- owner of shared node
            from ooflib.SWIG.common import mpitools
            # Need to get neighboring nodes
            shared = node.sharedWith()
            remote_indices = [node.remoteIndex(s) for s in shared]
            mpitools.Isend_Ints(remote_indices, shared)
            positions = mpitools.Irecv_DoubleVecs(shared)  # [[], [] ...]
            positions = reduce(lambda x,y: x+y, positions)  # []
            positions = [[positions[2*i], positions[2*i+1]]
                          for i in range(len(positions)/2)]
            # Add my own neighbors
            nbrNodes = node.neighborNodes(skeleton)
            positions += [[skeleton.nodePosition(n).x,
                           skeleton.nodePosition(n).y]
                          for n in nbrNodes]
            # Averaging
            x = 0.
            y = 0.
            for p in positions:
                x += p[0]
                y += p[1]
            x /= len(positions)
            y /= len(positions)
            return primitives.Point(x, y)

        def passive(self, skeleton, stopper):  # Parallel mode -- share-holder
            from ooflib.SWIG.common import mpitools
            _rank = mpitools.Rank()
            # Getting the node index (local)
            index = mpitools.Recv_Int(stopper)
            node = skeleton.getNodeWithIndex(index)
            # Get the neighbor nodes (but not ones are shared with stoppers,
            # since they are already accounted for at "stopper".)
            nbrNodes = node.neighborNodes(skeleton)
            positions = []
            for nd in nbrNodes:
                if _rank == nd.master():  # my own node
                    positions.append(skeleton.nodePosition(nd).x)
                    positions.append(skeleton.nodePosition(nd).y)
            mpitools.Send_DoubleVec(positions, stopper)
    
registeredclass.Registration(
    'Smooth Move Position',
    fiddlenodesbase.FiddleNodesMovePosition,
    SmoothMovePosition,
    ordering=1)


class Smooth(FiddleNodes, skeletonmodifier.SkeletonModifier):
    def __init__(self, targets, criterion, T, iteration):
        FiddleNodes.__init__(self, targets, criterion, T, iteration)
        self.intro = "Preparing to smooth skeleton...      "
        self.header = "Smoothing skeleton: "
        self.outro = "Smoothing done: "
        self.movedPosition = SmoothMovePosition()

if parallel_enable.enabled():
    from ooflib.engine import fiddlenodesbaseParallel
    Smooth.coreProcess_parallel = fiddlenodesbaseParallel._smoothCoreProcess
    

registeredclass.Registration(
    'Smooth',
    skeletonmodifier.SkeletonModifier,
    Smooth,
    ordering=4,
    params=[parameter.RegisteredParameter('targets', FiddleNodesTargets,
                                          tip='Which nodes to move.'),
            parameter.RegisteredParameter('criterion',
                                          skeletonmodifier.SkelModCriterion,
                                          tip = 'Acceptance criterion'),
            parameter.FloatParameter('T', value=0.0,
                                     tip='Failed moves will be accepted if T>0 and exp(-diffE/T) > r, where diffE is the energy gained and r is a random number between 0 and 1.'),
            parameter.RegisteredParameter('iteration', IterationManager,
                                          tip='Iteration method.')
    ],
    tip='Move nodes to the average position of their neighbors.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/smooth.xml'))


