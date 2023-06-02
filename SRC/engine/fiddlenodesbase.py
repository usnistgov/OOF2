# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import crandom
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import progress
from ooflib.common import debug
from ooflib.common import parallel_enable
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common import utils
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import deputy
from ooflib.engine import skeletonmodifier
from ooflib.engine.IO import pbcparams
from ooflib.engine.IO import skeletongroupparams
from ooflib.engine.IO import skeletonmenu
import math
import sys

from ooflib.SWIG.common import ooferror

class IterationManager(registeredclass.RegisteredClass):
    registry = []
    def update(self, delta, total, rate, count, prog):
        pass

    def goodToGo(self):
        # boolean
        pass
    
    def reportSomething(self, delta, total, rate, count):
        if total:
            reduce = abs(100.0*delta/total)
        else:
            reduce = 0.0
        reporter.report("Iteration %d: E = %10.4e, deltaE=%10.4e (%6.3f%%), Acceptance Rate = %4.1f%%"
                        % (count, total, delta, reduce, 100.*rate))

    def reportNothing(self, count):
        reporter.report("Iteration %d: No attempts made, no nodes moved!"
                        % count)
        
    tip = "Stopping criteria for iterative Skeleton modifiers."

    discussion = """<para>
    <classname>IterationManagers</classname> control the repeated
    application of certain <link
    linkend='RegisteredClass-SkeletonModifier'><classname>SkeletonModifiers</classname></link>,
    such as <xref linkend='RegisteredClass-Anneal'/> and <xref
    linkend='RegisteredClass-Smooth'/>.
    </para>"""

    
class FixedIteration(IterationManager):
    def __init__(self, iterations):
        self.iterations = iterations
        self.count = 0

    def update(self, delta, total, rate, count, prog):
        self.count = count
        # reporting
        if delta is not None and rate is not None:
            self.reportSomething(delta, total, rate, count)
        else:
            self.reportNothing(count)
        prog.setFraction(float(count)/self.iterations)
        prog.setMessage("iteration %d/%d" % (count, self.iterations))
        
    def goodToGo(self):
        if self.count < self.iterations:
            return 1
        else:
            return 0
        
    def get_progressbar_type(self):
        return progress.DEFINITE
    
registeredclass.Registration(
    'Fixed Iterations',
    IterationManager,
    FixedIteration, 0,
    params=[
    parameter.IntParameter('iterations', 5,
                        tip='Number of iterations to perform.  Each node is addressed once per iteration.')],
    tip="Repeat operation a fixed number of times.",
    discussion="""<para>
    Repeat a <link linkend='RegisteredClass-SkeletonModifier'>Skeleton
    modification</link> operation a fixed number of times.
    </para>""")

# Convergence condition candidates:
# 1. Acceptance Rate: Accepted_Nodes/Total_Nodes*100
#    Cheap and convenient but sometimes misleading.
#    If A.R. stays below the specified threshold for a specified number of
#    times, the process stops.

# 2. Energy Reduction Rate: Reduced_Energy/Total_Energy*100
#    Expensive but more accurate.
#    If energy reduction stays below the specified threshold for
#    a specified number of times, the process stops.

class ConditionSelector(registeredclass.RegisteredClass):
    registry = []

    tip = "Stopping criteria for conditional iteration of Skeleton modifiers."
    discussion = """<para>

    When using the <xref
    linkend='RegisteredClass-ConditionalIteration'/> <xref
    linkend='RegisteredClass-IterationManager'/> to iterate a <xref
    linkend='RegisteredClass-SkeletonModifier'/>, the actual stopping
    criterion is specified with an object of the
    <classname>ConditionSelector</classname> class.
    </para>"""

class ReductionRateCondition:
    def reductionRateFailed(self, delta, total):
        if delta is None:
            return 1
        # delta is negative, if energy is going down
        reduction = -delta/total*100.
        return reduction < self.reduction_rate

reductionRateParam = parameter.FloatRangeParameter(
    'reduction_rate', (0., 100., 0.1), value=0.1, 
    tip="Minimum allowable energy reduction rate as a percentage of the total energy.")

class AcceptanceRateCondition:
    def acceptanceRateFailed(self, rate):
        if rate is None:
            return 1
        return rate*100. < self.acceptance_rate

acceptanceRateParam = parameter.FloatRangeParameter(
    'acceptance_rate', (0., 100., 0.1), value=7,
    tip='Minimum allowable move acceptance rate as a percentage of the number of movable nodes.'
    )

class Either(ConditionSelector,
             ReductionRateCondition, AcceptanceRateCondition):
    def __init__(self, reduction_rate, acceptance_rate):
        self.reduction_rate = reduction_rate
        self.acceptance_rate = acceptance_rate
    def __call__(self, delta, total, rate, count):
        return self.reductionRateFailed(delta, total) or \
               self.acceptanceRateFailed(rate)
    
registeredclass.Registration(
    'Either',
    ConditionSelector,
    Either, 3,
    params=[acceptanceRateParam, reductionRateParam],
    tip="Iteration stops when either the energy reduction rate or move acceptance rate falls below the given thresholds.",
    discussion="""<para>
    When the <varname>condition</varname> parameter of a <xref
    linkend='RegisteredClass-ConditionalIteration'/> is set to
    <classname>Either</classname>, iteration of a <xref
    linkend='RegisteredClass-SkeletonModifier'/> will stop when either
    the <xref linkend='RegisteredClass-AcceptanceRate'/> or <xref
    linkend='RegisteredClass-ReductionRate'/> criterion is satisfied.
    </para>""")

class Both(ConditionSelector,
           ReductionRateCondition, AcceptanceRateCondition):
    def __init__(self, reduction_rate, acceptance_rate):
        self.reduction_rate = reduction_rate
        self.acceptance_rate = acceptance_rate
    def __call__(self, delta, total, rate, count):
        return self.reductionRateFailed(delta, total) and \
               self.acceptanceRateFailed(rate)
    
registeredclass.Registration(
    'Both',
    ConditionSelector,
    Both, 2,
    params=[reductionRateParam, acceptanceRateParam],
    tip="Iteration stops when both the energy reduction rate and move acceptance rate fall below the given thresholds.",
    discussion="""<para>
    When the <varname>condition</varname> parameter of a <xref
    linkend='RegisteredClass-ConditionalIteration'/> is set to
    <classname>Both</classname>, iteration of a <xref
    linkend='RegisteredClass-SkeletonModifier'/> will stop when both
    the <xref linkend='RegisteredClass-AcceptanceRate'/> or <xref
    linkend='RegisteredClass-ReductionRate'/> criteria are satisfied.
    </para>""")
                 
class ReductionRate(ConditionSelector, ReductionRateCondition):
    def __init__(self, reduction_rate):
        self.reduction_rate = reduction_rate
    def __call__(self, delta, total, rate, count):
        return self.reductionRateFailed(delta, total)
                 
registeredclass.Registration(
    'Energy Reduction Rate',
    ConditionSelector,
    ReductionRate, 1,
    params=[reductionRateParam],
    tip="Iteration stops when the energy reduction rate falls below the given threshold.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/reduction_rate.xml'))

class AcceptanceRate(ConditionSelector, AcceptanceRateCondition):
    def __init__(self, acceptance_rate):
        self.acceptance_rate = acceptance_rate
    def __call__(self, delta, total, rate, count):
        return self.acceptanceRateFailed(rate)
                 
registeredclass.Registration(
    'Acceptance Rate',
    ConditionSelector,
    AcceptanceRate, 0,
    params=[acceptanceRateParam],
    tip="Iteration stops when the move acceptance rate falls below the given threshold.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/acceptance_rate.xml'))

class ConditionalIteration(IterationManager):
    def __init__(self,
                 condition,
                 extra,
                 maximum):
        self.condition = condition
        self.maximum = maximum          # max no. of steps allowed
        self.extra = extra              # allow this many consecutive bad steps
        self.nbad = 0                   # no. of consecutive bad steps
        self.count = 0                  # total no. of steps

    def update(self, delta, total, rate, count, prog):
        self.count = count
        if self.condition(delta, total, rate, count):
            self.nbad += 1
        else:
            self.nbad = 0
        # reporting
        if delta is not None and rate is not None:
            self.reportSomething(delta, total, rate, count)
        else:
            self.reportNothing(count)
        prog.pulse()

    def goodToGo(self):
        return not (self.nbad > self.extra or self.count >= self.maximum)
    def get_progressbar_type(self):
        return progress.INDEFINITE

registeredclass.Registration(
    'Conditional Iteration',
    IterationManager,
    ConditionalIteration, 1,
    params=[
    parameter.RegisteredParameter('condition', ConditionSelector,
                                  tip='Which exit condition to use.'),
    parameter.IntParameter('extra', 0,
                           tip="Number of extra steps to take to ensure that the condition is met."),
    parameter.IntParameter('maximum', 100,
                        tip="Maximum number of iterations, despite the exit condition.")],
    tip='Iteration stops when a given condition is satisfied.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/conditional_iteration.xml'))
            
#############################################################

class FiddleNodesTargets(registeredclass.RegisteredClass):
    registry = []
    tip = "Set target Nodes for Skeleton modifiers."
    discussion = """<para>
    <classname>FiddleNodesTargets</classname> objects are used as the
    <varname>targets</varname> parameter in <link
    linkend='RegisteredClass-SkeletonModifier'><classname>SkeletonModifiers</classname></link>
    that move &nodes; around.
    </para> """

class AllNodes(FiddleNodesTargets):
    def __call__(self, context, prevnodes):
        if prevnodes:
            return prevnodes
        return (n for n in context.getObject().activeNodes() if n.movable())

registeredclass.Registration(
    'All Nodes',
    FiddleNodesTargets,
    AllNodes, 0,
    tip="Try moving all nodes.",
    discussion="""<para>

    Apply a &node; motion <xref
    linkend='RegisteredClass-SkeletonModifier'/> (such as <xref
    linkend='RegisteredClass-Anneal'/>) to all &nodes; in the &skel;.

    </para>""")

class SelectedNodes(FiddleNodesTargets):
    def __call__(self, context, prevnodes):
        if prevnodes:
            return prevnodes
        skel = context.getObject()
        # Use retrieveInOrder() so that results are repeatable in tests
        return context.nodeselection.retrieveInOrder(
            lambda n: n.movable() and n.active(skel))

registeredclass.Registration(
    'Selected Nodes',
    FiddleNodesTargets,
    SelectedNodes, 1,
    tip="Try moving only the selected nodes.",
    discussion="""<para>
    Apply a &node; motion <xref
    linkend='RegisteredClass-SkeletonModifier'/> (such as <xref
    linkend='RegisteredClass-Anneal'/>) to only the currently selected
    &nodes; in the &skel;.
    </para> """)

class NodesInGroup(FiddleNodesTargets):
    def __init__(self, group):
        self.group = group
    def __call__(self, context, prevnodes):
        if prevnodes:
            return prevnodes
        skel = context.getObject()
        return (n for n in context.nodegroups.get_group(self.group)
                if n.movable() and n.active(skel))

registeredclass.Registration(
    'Nodes in Group',
    FiddleNodesTargets,
    NodesInGroup,
    ordering=1.5,
    params=[skeletongroupparams.NodeGroupParameter('group',
                                                   tip='Try moving nodes in this group')],
    tip="Try moving only the nodes in a given group",
    discussion="""<para>
    Apply a &node; motion <xref
    linkend='RegisteredClass-SkeletonModifier'/> (such as <xref
    linkend='RegisteredClass-Anneal'/>) to only the 
    &nodes; in a given node group.
    </para> """)

class NonBoundaryNodes(FiddleNodesTargets):
    def __init__(self, ignorePBC=False):
        self.ignorePBC = ignorePBC
    def __call__(self, context, prevnodes):
        if prevnodes:
            return prevnodes
        skel = context.getObject()
        for node in skel.node_iterator():
            if node.active(skel):
                if self.ignorePBC:
                    elements = node.aperiodicNeighborElements()
                else:
                    elements = node.neighborElements()
                category = None
                for el in elements:
                    cat = el.dominantPixel(skel.MS)
                    if cat == category or category == None:
                        category = cat
                    else:
                        # One of the neighbor elements has a different
                        # category than the others, so this is a boundary
                        # node.  Skip it.
                        break
                else:
                    yield node
                
registeredclass.Registration(
    'Non-boundary Nodes',
    FiddleNodesTargets,
    NonBoundaryNodes,
    ordering=1.6,
    params=[pbcparams.PBCBooleanParameter('ignorePBC', False,
                                          tip='Ignore periodicity?')],
    tip="Only move nodes that aren't on internal boundaries")
                

class FiddleSelectedElements(FiddleNodesTargets):
    def __call__(self, context, prevnodes):
        if prevnodes:
            return prevnodes
        nodedict = {}
        skel = context.getObject()
        # Use retrieveInOrder so that results are repeatable in tests
        for element in context.elementselection.retrieveInOrder(
                lambda e: e.active(skel)):
            for nd in element.nodes:
                nodedict[nd] = 1
        # keys of a dict are retrieved in the order they were added
        return (n for n in nodedict if n.movable())

registeredclass.Registration(
    'Selected Elements',
    FiddleNodesTargets,
    FiddleSelectedElements, 2.0,
    tip="Try moving nodes of selected elements.",
    discussion="""<para>
    Apply a &node; motion <xref
    linkend='RegisteredClass-SkeletonModifier'/> (such as <xref
    linkend='RegisteredClass-Anneal'/>) to the &nodes; of the
    currently selected &elems; in the &skel;.
    </para>""")

class FiddleHeterogeneousElements(FiddleNodesTargets):
    def __init__(self, threshold=0.9):
        self.threshold = threshold
    def __call__(self, context, prevnodes):
        # The other FiddleNodesTargets classes make sure to compute
        # the list of nodes just once, by returning prevnodes
        # unchanged if its not None.  This one recomputes it each time
        # it's called, so that elements that become homogeneous during
        # the process won't be processed further.
        nodedict = {}
        skel = context.getObject()
        for element in skel.activeElements():
            if element.homogeneity(skel.MS, False) < self.threshold:
                for node in element.nodes:
                    nodedict[node] = 1
        return (n for n in nodedict if n.movable())

registeredclass.Registration(
    'Heterogeneous Elements',
    FiddleNodesTargets,
    FiddleHeterogeneousElements,
    ordering=2.1,
    params = [
    parameter.FloatRangeParameter('threshold', (0.0, 1.0, 0.01), value=0.9,
                                  tip='Anneal elements with homogeneity below the specified threshold.')
    ],
    tip="Try moving nodes of heterogeneous elements.",
    discussion="""<para>
    Apply a &node; motion <xref
    linkend='RegisteredClass-SkeletonModifier'/> (such as <xref
    linkend='RegisteredClass-Anneal'/>) to the &nodes; of the <link
    linkend='Section-Concepts-Skeleton-Homogeneity'>heterogeneous</link>
    &elems; in the &skel;.
    </para>""")

class FiddleElementsInGroup(FiddleNodesTargets):
    def __init__(self, group):
        self.group = group
    def __call__(self, context, prevnodes):
        if prevnodes:
            return prevnodes
        # Use a dict instead of a set here.  Sets don't return their
        # items in a guaranteed order, and if the order changes in a
        # future version of python, the test scripts will break.
        nodedict = {}
        for element in context.elementgroups.get_group(self.group):
            if element.active(context.getObject()):
                for nd in element.nodes:
                    nodedict[nd] = 1
        return (n for n in nodedict if n.movable())
    
registeredclass.Registration(
    'Elements in Group',
    FiddleNodesTargets,
    FiddleElementsInGroup,
    ordering=2.5,
    params=[skeletongroupparams.ElementGroupParameter('group',
                                                      tip='Move the nodes belonging to elements in this group')],
    tip="Move nodes of elements in a given element group",
    discussion="""<para>
    Apply a &node; motion <xref
    linkend='RegisteredClass-SkeletonModifier'/> (such as <xref
    linkend='RegisteredClass-Anneal'/>) to the &nodes; of the &elems;
    in a given &elem; group.
    </para>""")

#####################################################

class FiddleNodesMovePosition(registeredclass.RegisteredClass):
    # FiddleNodesMovePosition is a RegisteredClass because it's used
    # as an argument in the IPC menu for parallel node fiddling.
    registry = []
    def __call__(self, skeleton, node):
        pass

    if parallel_enable.enabled():
        # Parallel stuff
        def active(self, skeleton, node):
            pass
        
        def passive(self, skeleton, stopper):
            pass

class FiddleNodes:
    def __init__(self, targets, criterion, T, iteration):
        self.targets = targets
        self.criterion = criterion
        self.T = T
        self.iteration = iteration
        self.nok = 0
        self.nbad = 0
        self.deltaE = 0
        self.totalE = 0
        ## self.movedPosition is set in derived classes.
    def makeProgress(self):
        return progress.getProgress(self.__class__.__name__,
                                     self.iteration.get_progressbar_type())
        
    def apply(self, oldskeleton, context):
        prog = self.makeProgress()
        prog.setMessage(self.intro)
        return oldskeleton.deputyCopy()

    def updateIteration(self, prog):
        if self.nok+self.nbad > 0:
            self.iteration.update(self.deltaE, self.totalE,
                                  (1.0*self.nok)/(self.nok+self.nbad),
                                  self.count, prog)
        else:  
            self.iteration.update(None, None, None, self.count, prog)
        
    def postProcess(self, context):
        ## global Pcount
        ## Pcount += 1
        skeleton = context.getObject()
        self.count = 0
        before = skeleton.energyTotal(self.criterion.alpha)
        self.activenodes = None

        prog = self.makeProgress()
        prog.setMessage(self.header)
        try:
            while self.iteration.goodToGo():
                self.count += 1
                # the context acquires the writing permissions inside
                # coreProcess.
                self.coreProcess(context)
                self.updateIteration(prog)
                skeleton.updateGeometry()
                switchboard.notify("skeleton homogeneity changed",
                                   context.path())
                if prog.stopped():
                    break
            switchboard.notify("skeleton nodes moved", context)
            if prog.stopped():
                return

            after = skeleton.energyTotal(self.criterion.alpha)
            if before:
                rate = 100.0*(before-after)/before
            else:
                rate = 0.0
            diffE = after - before
            reporter.report("%s deltaE = %10.4e (%6.3f%%)"
                            % (self.outro, diffE, rate))
        finally:
            self.activenodes = None
            prog.finish()

    def coreProcess(self, context):
        ## NOTE FOR DEVELOPERS:
        #### if a change is made to this function, make sure that the
        #### SAME changes are made, in a consistent way in
        #### fiddlenodesbaseParallel.py.  Or not.  The parallel code
        #### is very out of date and should just be rewritten.
        skeleton = context.getObject()

        self.totalE = skeleton.energyTotal(self.criterion.alpha)
        self.nok = self.nbad = 0
        self.deltaE = 0.
        # TODO: If the Skeleton is periodic and a node and its partner
        # are both active, only one of them should be in activenodes.
        self.activenodes = list(self.targets(context, self.activenodes))
        crandom.shuffle(self.activenodes)
        j = 0
        context.begin_writing()

        prog = self.makeProgress()
        try:
            for node in self.activenodes:
                change = deputy.DeputyProvisionalChanges()
                change.moveNode(node, self.movedPosition(skeleton, node),
                                skeleton)
                bestchange = self.criterion([change], skeleton)

                if bestchange is not None:
                    self.nok += 1
                    self.deltaE += bestchange.deltaE(skeleton,
                                                     self.criterion.alpha)
                    bestchange.accept(skeleton)
                # Failed to meet the specified criterion ... but
                elif (self.T>0.0 and 
                      not change.illegal(skeleton) and 
                      not self.criterion.hopeless()):
                    diffE = change.deltaE(skeleton, self.criterion.alpha)
                    if math.exp(-diffE/self.T) > crandom.rndm():
                        self.nok += 1
                        self.deltaE += diffE
                        change.accept(skeleton)
                    else:
                        self.nbad += 1
                else:
                    self.nbad += 1
                        
                if prog.stopped():
                    return

            skeleton.timestamp.increment()
        finally:
            prog.finish()
            context.end_writing()
            switchboard.notify("redraw")

    # Parallel function
    if parallel_enable.enabled():
        def apply_parallel(self, oldskeleton, context):
            pass  # Look in "fiddlenodesbaseParallel.py"

        def updateIteration_parallel(self):
            pass  # "fiddlenodesbaseParallel.py"

        def postProcess_parallel(self, context):
            pass  # Defined in "fiddlenodesbaseParallel.py"

        def coreProcess_parallel(self, context):
            pass  # defined in "fiddlenodesParallel.py"
    

if parallel_enable.enabled():
    from ooflib.engine import fiddlenodesbaseParallel
    FiddleNodes.apply_parallel = \
    fiddlenodesbaseParallel._apply                           
    FiddleNodes.postProcess_parallel = \
    fiddlenodesbaseParallel._postProcess
##    FiddleNodes.coreProcess_parallel = \
##    fiddlenodesbaseParallel._coreProcess
    FiddleNodes.updateIteration_parallel = \
    fiddlenodesbaseParallel._updateIteration
