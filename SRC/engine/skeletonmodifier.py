# -*- python -*-
# $RCSfile: skeletonmodifier.py,v $
# $Revision: 1.60 $
# $Author: reida $
# $Date: 2014/10/09 14:36:58 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import config
from ooflib.common import parallel_enable
from ooflib.common import registeredclass
from ooflib.common import utils
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
if config.dimension() == 2:
    from ooflib.engine import skeleton
elif config.dimension() == 3:
    from ooflib.engine import skeleton3d as skeleton
from ooflib.engine.IO import skeletongroupparams

import random

########################

# The alpha parameter for computing an element's effective energy is
# defined here so that different commands can share the same Parameter
# object.  Then GUI users won't have to be changing the parameter
# separately in all the different commands that use it.

alphaParameter = parameter.FloatRangeParameter(
    'alpha',
    range=(0., 1.0, 0.01),
    value=0.3,
    tip='alpha controls the relative importance of element shape and homogeneity.  alpha=0 emphasizes shape and ignores homogeneity.  alpha=1 emphasizes homogeneity and ignores shape.'
    )

#########################
                                               
class SkelModTargets(registeredclass.RegisteredClass):
    registry = []
    tip = "Which elements to modify?"
    discussion = """<para>
    <classname>SkelModTargets</classname> objects are used as the
    <varname>targets</varname> parameter in <link
    linkend='RegisteredClass-SkeletonModifier'><classname>SkeletonModifiers</classname></link>.
    They determine which &elems; will be modified when a <xref
    linkend='RegisteredClass-SkeletonModifier'/> is applied to a
    &skel;.
    </para>"""

class AllElements(SkelModTargets):
    def __call__(self, skeleton, context, copy=None):
        if copy:
            return skeleton.elements[:]
        else:
            return skeleton.elements

registeredclass.Registration(
    'All Elements',
    SkelModTargets,
    AllElements, 0,
    tip="Modify all elements.",
    discussion = """<para>
    <classname>AllElements</classname> is a <xref
    linkend='RegisteredClass-SkelModTargets'/> subclass, used as the
    <varname>targets</varname> parameter in <link
    linkend='RegisteredClass-SkeletonModifier'><classname>SkeletonModifiers</classname></link>.
    It specifies that all &elems; of a &skel; are to be modified.
    </para>""")

class SelectedElements(SkelModTargets):
    def __call__(self, skeleton, context, copy=None):
        elements = []
        for parent in context.elementselection.retrieveInOrder():
            try:
                elements.append(parent.getChildren()[-1])
            except IndexError:
                pass
        if copy:
            return elements[:]
        else:
            return elements

registeredclass.Registration(
    'Selected Elements',
    SkelModTargets,
    SelectedElements, 1,
    tip="Modify selected elements.",
    discussion = """<para>
    <classname>SelectedElements</classname> is a <xref
    linkend='RegisteredClass-SkelModTargets'/> subclass, used as the
    <varname>targets</varname> parameter in <link
    linkend='RegisteredClass-SkeletonModifier'><classname>SkeletonModifiers</classname></link>.
    It specifies that only the currently selected &elems; of a &skel;
    are to be modified.
    </para>""")

class HeterogeneousElements(SkelModTargets):
    def __init__(self,threshold = 0.9):
        self.threshold = threshold

    def __call__(self, skeleton, context, copy=None):
        elements = []
        for element in skeleton.elements:
            if element.homogeneity(skeleton.MS) < self.threshold:
                elements.append(element)
        if copy:
            return elements[:]
        else:
            return elements

registeredclass.Registration(
    'Heterogeneous Elements',
    SkelModTargets,
    HeterogeneousElements, ordering = 2,
    params=[
    parameter.FloatRangeParameter('threshold', (0.0, 1.0, 0.01), value=0.9,
                                  tip='Modify elements with homogeneity below the specified threshold.')
    ],
    tip='Modify heterogeneous elements.',
    discussion = """<para>
    <classname>HeterogeneousElements</classname> is a <xref
    linkend='RegisteredClass-SkelModTargets'/> subclass, used as the
    <varname>targets</varname> parameter in <link
    linkend='RegisteredClass-SkeletonModifier'><classname>SkeletonModifiers</classname></link>. It
    specifies that only the &elems; whose <link
    linkend='Section-Concepts-Skeleton-Homogeneity'>homogeneity</link>
    is less than the given <varname>threshold</varname> will be
    modified.
    </para>""")

class BadlyShapedElements(SkelModTargets):
    def __init__(self,threshold = 0.4):
        self.threshold = threshold

    def __call__(self, skeleton, context, copy=None):
        elements = []
        for element in skeleton.elements:
            if element.energyShape() > self.threshold:
                elements.append(element)
        if copy:
            return elements[:]
        else:
            return elements

registeredclass.Registration(
    'Badly Shaped Elements',
    SkelModTargets,
    BadlyShapedElements, ordering = 3,
    params=[
    parameter.FloatRangeParameter('threshold', (0.0, 1.0, 0.01), value=0.4,
                                  tip="The threshold shape energy -- 0.0 for the perfect shape and 1.0 for the worst shape.")],
    tip='Modify badly shaped elements.',
    discussion = """<para>
    <classname>BadlyShapedElements</classname> is a <xref
    linkend='RegisteredClass-SkelModTargets'/> subclass, used as the
    <varname>targets</varname> parameter in <link
    linkend='RegisteredClass-SkeletonModifier'><classname>SkeletonModifiers</classname></link>. It
    specifies that only the &elems; whose <link
    linkend='Section-Concepts-Skeleton-Shape_Energy'>shape
    energy</link> is greater than the given
    <varname>threshold</varname> will be modified.
    </para>""")

class ElementsInGroup(SkelModTargets):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, context, copy=None):
        elements = context.elementgroups.get_group(self.group)
        if copy:
            return elements[:]
        return elements

registeredclass.Registration(
    'Elements In Group',
    SkelModTargets,
    ElementsInGroup,
    ordering=2.5,
    params=[skeletongroupparams.ElementGroupParameter('group',
                                                      tip='Choose the elements in this group')],
    tip='Operate on an Element group',
    discussion="""<para>

    <classname>ElementsInGroup</classname> is a <xref
    linkend='RegisteredClass-SkelModTargets'/> subclass, used as the
    <varname>targets</varname> parameter in <link
    linkend='RegisteredClass-SkeletonModifier'><classname>SkeletonModifiers</classname></link>. It
    specifies that only the &elems; in a particular &elemgroup; will
    be modified.

    </para>""")

#################################################

# How do you determine if the modification is accepted or not.
# At this point, this could be commonly used for SplitQuads, SwapEdges,
# MergeTriangles, and Rationalize which use "ProvisionalChange" mechanism.

class SkelModCriterion(registeredclass.RegisteredClass):
    registry = []
    def __call__(self, changes, skel):
        # Child classes must provide __call__ method with
        # ProvisionalChanges, Skeleton as arguments
        pass    
    def hopeless(self):
        return 0
    
    tip = "Acceptance criteria for skeleton modifications."
    discussion = xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/skelmodcriterion.xml')

class LimitedSkelModCriterion(SkelModCriterion):
    _hopeless = 0
    def withinTheLimit(self, change, skel):
        homog_before = {}
        homog_after = {}
        shape_before = {}
        shape_after = {}
        for el in change.elBefore():
            homog_before[el] = el.homogeneity(skel.MS)
            shape_before[el] = el.energyShape()
        change.makeNodeMove(skel)
        for el in change.elAfter():
            key = el.getPositionHash()
            try:
                homogeneity = skel.cachedHomogeneities[key]
                el.setHomogeneityData(homogeneity)
            except KeyError:
                homogeneity = el.getHomogeneityData()
                skel.cachedHomogeneities[key] = homogeneity            
            homog_after[el] = el.homogeneity(skel.MS)
            shape_after[el] = el.energyShape()
        change.moveNodeBack(skel)
        # In parallel-mode, changes from other processes also need
        # to be considered.
        if parallel_enable.enabled():
            for i, h0,h1, s0,s1 in zip(range(len(change.parallelHomog0)),
                                       change.parallelHomog0,
                                       change.parallelHomog1,
                                       change.parallelShape0,
                                       change.parallelShape1):
                homog_before[i] = h0
                homog_after[i] = h1
                shape_before[i] = s0
                shape_after[i] = s1
                
        for el in homog_after:
            if homog_after[el] < self.homogeneity:
                try:
                    if homog_before[el] > homog_after[el]:
                        self._hopeless = 1
                        return 0
                except KeyError:
                    self._hopeless = 1
                    return 0
            if shape_after[el] > self.shape_energy:
                try:
                    if shape_before[el] < shape_after[el]:
                        self._hopeless = 1
                        return 0
                except KeyError:
                    self._hopeless = 1
                    return 0
        return 1
    
    def hopeless(self):
        return self._hopeless
    

class AverageEnergy(SkelModCriterion):
    def __init__(self, alpha):
        self.alpha = alpha
    # Finds the best available change(lowering average energy the most)
    # that is legal.
    def __call__(self, changes, skel):
        bestE = 0.0
        bestchange = None
        for change in changes:
            if not (change is None or change.illegal(skel)):
                diff = change.deltaE(skel, self.alpha)  # energy difference
                if diff <= bestE:
                    bestchange = change
                    bestE = diff
                    
        for change in changes:
            if change is not None and change is not bestchange:
                change.removeAddedNodes(skel)
        return bestchange

    # For rationalize ... has to go eventually
    def addSubstitute(self, elements, newel):
        elements.append(newel)
        return  1
    
registeredclass.Registration(
    'Average Energy',
    SkelModCriterion,
    AverageEnergy,
    ordering=0,
    params=[alphaParameter],
    tip = 'Accept the change, if any, that improves the average energy the most.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/average_energy.xml'))


#class AverageEnergyBestOf(SkelModCriterion):
#    def __init__(self, alpha, num):
#        self.alpha = alpha
#        self.num = num
    # Finds the best available change(lowering average energy the most)
    # that is legal.
#    def __call__(self, changes, skel):
#        bestE = 0.0
#        bestchange = None
#        changesconsidered = []
#        for change in changes:
#            if not (change is None or change.illegal(skel) or change.deltaEBound(skel, self.alpha) >= 0):
#                changesconsidered.append(change)
#        if len(changesconsidered) > self.num:
#            changesconsidered = changesconsidered[:self.num]
#        for change in changesconsidered:
#            diff = change.deltaE(skel, self.alpha)  # energy difference
#            if diff <= bestE:
#                bestchange = change
#                bestE = diff
#                    
#        for change in changes:
#            if change is not None and change is not bestchange:
#                change.removeAddedNodes(skel)
#        return bestchange

    # For rationalize ... has to go eventually
#    def addSubstitute(self, elements, newel):
#        elements.append(newel)
#        return  1    

#registeredclass.Registration(
#    'Average Energy Best Of',
#    SkelModCriterion,
#    AverageEnergyBestOf,
#    ordering=4,
#    params=[alphaParameter, parameter.IntParameter('num', value=5, tip="number of possibilities to consider")],
#    tip = 'Accept the change, if any, that improves the average energy the most.  Limit the number of possibilities considered.',
#    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/average_energy.xml'))


# Accept any modification as long as it stays in the legal boundaries
class Unconditional(SkelModCriterion):
    def __init__(self, alpha):
        self.alpha = alpha
    # Finds the best available change (with minimum average energy,
    # regardless of it's lower than before or not) that is legal.
    def __call__(self, changes, skel):
        bestE = None
        bestchange = None
        for change in changes:
            if not (change is None or change.illegal(skel)):
                # Reads ... are  you the first non-trivial in the list?
                if bestE is None and bestchange is None:
                    bestchange = change
                    bestE = change.deltaE(skel, self.alpha)
                else:
                    diff = change.deltaE(skel, self.alpha)
                    if diff <= bestE:
                        bestchange = change
                        bestE = diff
        for change in changes:
            if change is bestchange:
                continue
            if change is not None:
                change.removeAddedNodes(skel)
        return bestchange

    # For rationalize ... has to go eventually
    def addSubstitute(self, elements, newel):
        return 0
    
registeredclass.Registration(
    'Unconditional', SkelModCriterion,
    Unconditional,
    ordering=1,
    params=[alphaParameter],
    tip = 'Unconditionally accept the best change even if it increases the energy.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/unconditional.xml'))

class LimitedAverageEnergy(LimitedSkelModCriterion):
    def __init__(self, alpha, homogeneity, shape_energy):
        self.alpha = alpha
        self.homogeneity = homogeneity
        self.shape_energy = shape_energy
    def __call__(self, changes, skel):
        bestE = 0.0
        bestchange = None
        for change in changes:
            if not (change is None or change.illegal(skel)) and \
               self.withinTheLimit(change, skel):
                diff = change.deltaE(skel, self.alpha)  # energy difference
                if diff <= bestE:
                    bestchange = change
                    bestE = diff

        for change in changes:
            if change is not bestchange:
                change.removeAddedNodes(skel)
        return bestchange

    # For rationalize ... has to go eventually
    def addSubstitute(self, elements, newel):
        elements.append(newel)
        return  1
    
registeredclass.Registration(
    'Limited Average Energy',
    SkelModCriterion,
    LimitedAverageEnergy,
    ordering=2,
    params=[alphaParameter,
            parameter.FloatRangeParameter('homogeneity', (0.0, 1.0, 0.01),
                                          value=0.9,
                                        tip='Minimum acceptable homogeneity.'),
            parameter.FloatRangeParameter('shape_energy', (0.0, 1.0, 0.01),
                                          value=0.4,
                                        tip='Maximum acceptable shape energy.')
            ],
    tip = 'Accepts the change that lowers the average energy AND meets specified conditions on homogeneity and shape energy.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/limited_average.xml'))

# Accept any modification as long as it stays in the legal boundaries
class LimitedUnconditional(LimitedSkelModCriterion):
    def __init__(self, alpha, homogeneity, shape_energy):
        self.alpha = alpha
        self.homogeneity = homogeneity
        self.shape_energy = shape_energy
    # Finds the best available change(with minimum average energy,
    # regardless of it's lower than before or not)
    # that is legal.
    def __call__(self, changes, skel):
        bestE = None
        bestchange = None
        for change in changes:
            if not (change is None or change.illegal(skel)) and \
               self.withinTheLimit(change, skel):
                # Reads ... is this the first non-trivial one in the list?
                if bestE is None and bestchange is None:
                    bestchange = change
                    bestE = change.deltaE(skel, self.alpha)
                else:
                    diff = change.deltaE(skel, self.alpha)
                    if diff <= bestE:
                        bestchange = change
                        bestE = diff

        for change in changes:
            if change is not bestchange:
                change.removeAddedNodes(skel)
        return bestchange
    
    # For rationalize ... has to go eventually
    def addSubstitute(self, elements, newel):
        return 0

registeredclass.Registration(
    'Limited Unconditional', SkelModCriterion,
    LimitedUnconditional,
    ordering=3,
    params=[alphaParameter,
            parameter.FloatRangeParameter('homogeneity', (0.0, 1.0, 0.01),
                                          value=0.9,
                                         tip='Minimum acceptable homogeneity.'),
            parameter.FloatRangeParameter('shape_energy', (0.0, 1.0, 0.01),
                                          value=0.4,
                                        tip='Maxiumum acceptable shape energy.')
            ],
    tip = 'Accepts any change that meets specified conditions on homogeneity and shape energy.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/limited_unconditional.xml'))

# SkeletonModifier is the base class for skeleton modifiers (who
# woulda guessed?).  They must have an "apply" method, which takes a
# skeleton argument and returns a new skeleton.  They can have an
# optional "postProcess" method, which receives the new skeleton as an
# argument.  apply() is called before the SkeletonContext is informed
# of the new skeleton (and hence before it can be drawn).
# postProcess() is called afterwards, so it can profitably issue
# "redraw" messages.

class SkeletonModifier(registeredclass.RegisteredClass):
    ok_illegal = 0  # can it handle illegal skeletons?
    registry = []
    def postProcess(self, context):
        pass

    def postProcess_parallel(self, context):
        pass

    tip = "Tools to modify Skeletons."
    discussion = """<para>

    <classname>SkeletonModifiers</classname> are applied to &skels; by
    the <xref linkend='MenuItem-OOF.Skeleton.Modify'/> command.

    </para>"""

    
class NamedSkeletonModifiers:

    def __init__(self):
        self.data={}

    def __setitem__(self,key,value):
	self.data[key]=value

    def __getitem__(self,key):
	return self.data[key]

namedSkeletonModifiers=NamedSkeletonModifiers()
utils.OOFdefine('namedSkeletonModifiers',namedSkeletonModifiers)
