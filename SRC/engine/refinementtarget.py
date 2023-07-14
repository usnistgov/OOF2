# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import progress
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import registeredclass
from ooflib.common import utils
from ooflib.common.IO import parameter
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
from ooflib.engine import skeleton
from ooflib.engine.IO import skeletongroupparams

import math

class RefinementTarget(registeredclass.RegisteredClass):
    registry = []
    tip = "Determine which Skeleton segments will be refined."
    discussion = xmlmenudump.loadFile('DISCUSSIONS/engine/reg/refinementtarget.xml')

# ElementRefinementTarget marks all segments of the elements that
# match the given criterion.  If you don't want to mark all segments,
# use SegmentRefinementTarget instead.

class ElementRefinementTarget(RefinementTarget):
    def markElement(self, skeleton, element, divider, markedSegs):
        nnodes = element.nnodes()
        for i in range(nnodes):
            divider.markSegment(skeleton,
                               element.nodes[i], element.nodes[(i+1)%nnodes],
                               markedSegs)
    def __call__(self, skeleton, context, divider, markedSegs, criterion):
        prog = progress.findProgress("Refine")
        eliter = self.iterator(context) # self.iterator is from subclass
        for element in eliter:
            if criterion(skeleton, element):
                self.markElement(skeleton, element, divider, markedSegs)
            if prog.stopped():
                return
            prog.setFraction(eliter.fraction())
            prog.setMessage(
                f"checked {eliter.nexamined()}/{eliter.ntotal()} elements")
            

class SegmentRefinementTarget(RefinementTarget):
    def markSegment(self, skeleton, context, segment, divider, markedSegs):
        divider.markSegment(skeleton,
                           segment.nodes()[0], segment.nodes()[1], markedSegs)
    def __call__(self, skeleton, context, divider, markedSegs, criterion):
        prog = progress.findProgress("Refine")
        segiter = self.iterator(context)
        for segment in segiter:
            if criterion(skeleton, segment):
                self.markSegment(skeleton, context, segment, divider,
                                 markedSegs)
            if prog.stopped():
                return
            prog.setFraction(segiter.fraction())
            prog.setMessage(
                f"checked {segiter.nexamined()}/{segiter.ntotal()} segments")
        

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class CheckAllElements(ElementRefinementTarget):
    def iterator(self, skeletoncontext):
        return skeletoncontext.getObject().activeElements()
    
registeredclass.Registration(
    'All Elements',
    RefinementTarget,
    CheckAllElements,
    ordering=2,
    tip="Refine all elements.",
    discussion= "<para>Refine all segments of all elements.</para>")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class CheckSelectedElements(ElementRefinementTarget):
    def iterator(self, skeletoncontext):
        return skeletoncontext.getObject().selectedElements()
    
registeredclass.Registration(
    'Selected Elements',
    RefinementTarget,
    CheckSelectedElements,
    ordering=1,
    tip="Refine selected elements.",
    discussion= """<para>
    Refine all segments of the currently selected elements.
    </para>""")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class CheckElementsInGroup(ElementRefinementTarget):
    def __init__(self, group):
        self.group = group
    def iterator(self, skeletoncontext):
        return skeleton.SkeletonElementGroupIterator(
            skeletoncontext, self.group,
            lambda e: e.active(skeletoncontext.getObject()))
    
registeredclass.Registration(
    'Elements In Group',
    RefinementTarget,
    CheckElementsInGroup,
    ordering=1.5,
    params=[skeletongroupparams.ElementGroupParameter('group',
                                                      tip='Refine the elements in this group.')],
    tip="Refine elements in an element group.",
    discussion= """<para>
    Refine all segments of the elements in the given element group.
    </para>""")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class CheckHomogeneity(ElementRefinementTarget):
    def __init__(self, threshold):
        self.threshold = threshold

    def iterator(self, context):
        skel = context.getObject()
        return skeleton.SkeletonElementIterator(
            skel,
            (lambda e: e.active(skel) and
            e.homogeneity(skel.MS,False) < self.threshold))

registeredclass.Registration(
    'Heterogeneous Elements',
    RefinementTarget,
    CheckHomogeneity,
    ordering=0,
    params=[parameter.FloatRangeParameter(
        'threshold',
        (0.0, 1.0, 0.05),
        value=0.9,
        tip='Refine elements whose homogeneity is less than this.')
                             ],
    tip='Refine heterogeneous elements.',
    discussion=
    """<para>
    Any elements whose <link
    linkend='Section-Concepts-Skeleton-Homogeneity'>homogeneity</link>
    is less than the given <varname>threshold</varname> will be
    refined.  <xref linkend='Figure-refine'/> illustrates the
    refinement of all elements with homogeneity less than 1.0.
    </para>""")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# SegmentChooser subclasses are used as parameters in
# RefinementTargets that identify particular segments.  They need to
# provide a getSegments() method that returns an instance of a
# SkeletonSegmentIterator subclass.

class SegmentChooser(registeredclass.RegisteredClass):
    registry = []
    tip = "Choose sets of segments be refined."
    discussion = xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/segment_chooser.xml')

class FromAllSegments(SegmentChooser):
    def getSegments(self, context):
        return skeleton.SkeletonSegmentIterator(context.getObject())

registeredclass.Registration(
    'All Segments',
    SegmentChooser,
    FromAllSegments,
    4,
    tip="Examine all segments.",
    discussion= """<para>
    When choosing <link
    linkend='RegisteredClass-CheckHeterogeneousSegments'>heterogeneous</link>
    &sgmts; to <link linkend='RegisteredClass-Refine'>refine</link>,
    consider all &sgmts; of the &skel;.
    </para>""")

class SelectedSegmentsIterator(skeleton.SkeletonSegmentIterator):
    def __init__(self, context):
        self.context = context
        skeleton.SkeletonSegmentIterator.__init__(self, context.getObject())
    def total(self):
        return self.context.segmentselection.size()
    def targets(self):
        for seg in self.context.segmentselection.retrieve():
            if seg.active(self.context.getObject()):
                yield seg

class FromSelectedSegments(SegmentChooser):
    def getSegments(self, context):
        return SelectedSegmentsIterator(context)

registeredclass.Registration(
    'Selected Segments',
    SegmentChooser,
    FromSelectedSegments,
    ordering=1,
    tip="Examine selected segments.",
    discussion= """<para>
    When choosing <link
    linkend='RegisteredClass-CheckHeterogeneousSegments'>heterogeneous</link>
    &sgmts; to <link linkend='RegisteredClass-Refine'>refine</link>,
    consider only the currently selected &sgmts;.
    </para>""")

class SegsFromSelectedElementsIterator(skeleton.SkeletonSegmentIterator):
    def __init__(self, context):
        self.context = context
        skeleton.SkeletonSegmentIterator.__init__(self, context.getObject())
    # TODO: There should be a total() method that returns the total
    # number of segments that will be returned, but we don't know that
    # without actually doing the loop.  Without it, the fraction
    # reported by the progress bar will be incorrect. 
    def targets(self):
        usedsegments = set()
        for elem in self.context.elementselection.retrieve():
            for i in range(elem.nnodes()):
                n0 = elem.nodes[i]
                n1 = elem.nodes[(i+1)%elem.nnodes()]
                seg = self.context.getObject().findSegment(n0, n1)
                if seg.active(self.context.getObject()):
                    if seg not in usedsegments:
                        usedsegments.add(seg)
                        yield seg

class FromSelectedElements(SegmentChooser):
    def getSegments(self, context):
        return SegsFromSelectedElementsIterator(context)
                
registeredclass.Registration(
    'Selected Elements',
    SegmentChooser,
    FromSelectedElements,
    ordering=1,
    tip="Examine segments from segments of currently selected elements.",
    discussion= """<para>
    When choosing <link
    linkend='RegisteredClass-CheckHeterogeneousSegments'>heterogeneous</link>
    &sgmts; to <link linkend='RegisteredClass-Refine'>refine</link>,
    consider only the edges of the currently selected &elems;.
    </para>""")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## TODO LATER: These classes are oddly defined.
## CheckHeterogeneousSegments uses a SegmentChooser to choose the set
## of segments to consider.  The choices are SelectedElements,
## SelectedSegments, and AllSegments.  But CheckSelectedEdges doesn't
## use a SegmentChooser, although it could. CheckAllEdges with a
## SegmentChooser could reproduce CheckSelectedSegments and
## CheckSegmentGroup and Check...
##
## In fact, there could be a top level Elements option, with an
## ElementChooser parameter that switches between All Elements,
## Selected Elements, Selected Segments, and Element Group.  A top
## level Segments option would have a SegmentChooser with equivalent
## options.

# Currently implemented/2.2.2/2.1.19 scheme
#
# Refine
#   targets
#     Heterogeneous Elements
#        threshold
#     Selected Elements
#     Elements in Group
#       group name
#     All Elements
#     Aspect Ratio
#       threshold
#       only_quads
#     Heterogeneous Segments
#       threshold (0-1)
#       choose from            <--- Why doesn't Het. Elements have this option?
#          Selected Elements
#          Selected Segments
#          All Segments
#     Selected Segments
#     Segments in Group
#       group name
#     AMR
#   criterion  (Unconditional or Minimum Area)
#   divider (Bisection, Trisection, or Transition Points)
#   rules (Quick, Large)
#   alpha (0-1)

# Potential new scheme:
#
# Refine
#   targets
#     Elements
#        All
#        Heterogeneous
#        Selected
#        Group
#           group name
#        From Selected Segments
#        Aspect Ratio
#          threshold
#          only_quads
#        AMR?
#     Segments
#        All
#        Heterogeneous
#        Selected
#        Group
#           Name
#        From Selected Elements
#   criterion  (Unconditional or Minimum Area)
#   divider (Bisection, Trisection, or Transition Points)
#   rules (Quick, Large)
#   alpha (0-1)
#
# But that doesn't have the useful functionality of hte choose from option.

# Maybe the better thing would be to have a bunch of checkboxes to
# select which criteria to use.  The current "criterion" argument
# would be deleted.  Objects would be refined if they meet all of the
# chosen criteria.
#
# Refine
#   targets
#     Elements
#       * all
#       * homogeneity < threshold
#       * group == name
#       * selected
#       * area > min
#       * aspect ratio > min
#       * AMR
#       * has a selected segment
#       * has a selected node
#     Segments
#       * all
#       * homogeneity < threshold
#       * group = name
#       * selected
#       * has a selected element
#       * has a selected node
#
# "all" would be automatically selected if none of the other criteria
# are chosen.  Checking "all" would deselect the other criteria, and
# vice versa.  Deselecting "all" would put the widget in an illegal
# state and desensitize the OK button.

class CheckHeterogeneousSegments(SegmentRefinementTarget):
    def __init__(self, threshold, choose_from):
        self.threshold = threshold
        self.choose_from = choose_from

    def iterator(self, context):
        skel = context.getObject()
        micro = context.getMicrostructure()
        return skeleton.SkeletonSegmentIterator(
            skel,
            condition=lambda s: (s.active(skel) and
                                 s.homogeneity(micro) < self.threshold))

registeredclass.Registration(
    'Heterogeneous Segments',
    RefinementTarget,
    CheckHeterogeneousSegments,
    ordering=3,
    params=[
        parameter.FloatRangeParameter(
            'threshold', (0.0, 1.0, 0.05),
            value=0.9,
            tip="Refine segments whose homogeneity is less than this."),
        parameter.RegisteredParameter('choose_from', SegmentChooser,
                                      tip='Segments to consider.')],
    tip="Divide heterogeneous segments.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/check_hetero_segs.xml'))

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class CheckSelectedEdges(SegmentRefinementTarget):
    def iterator(self, context):
        skel = context.getObject()
        return skeleton.SkeletonSegmentIterator(
            skel,
            condition=lambda s: (s.isSelected() and s.active(skel)))
        
registeredclass.Registration(
    'Selected Segments',
    RefinementTarget,
    CheckSelectedEdges,
    ordering=3,
    tip="Divide selected segments.",
    discussion="""<para>
    <xref linkend='RegisteredClass-Refine'/> all currently selected &sgmts;.
    </para>""")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class CheckSegmentsInGroup(SegmentRefinementTarget):
    def __init__(self, group):
        self.group = group
    def iterator(self, context):
        skel = context.getObject()
        return skeleton.SkeletonSegmentGroupIterator(
            context, self.group,
            condition=lambda s: s.active(skel))
        
registeredclass.Registration(
    'Segments in Group',
    RefinementTarget,
    CheckSegmentsInGroup,
    ordering=3.5,
    params=[skeletongroupparams.SegmentGroupParameter(
        'group', tip='Examine segments in this group')],
    tip="Refine segments in a segment group",
    discussion="""<para>
    Refine a Skeleton by divided the segments in the given segment group.
    </para>"""
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class AspectSegmentIterator(skeleton.SkeletonSegmentIterator):
    def __init__(self, skel, threshold, only_quads, condition=lambda x: True):
        self.threshold = threshold
        self.only_quads = only_quads
        skeleton.SkeletonSegmentIterator.__init__(self, skel, condition)
    def targets(self):
        for element in self.skeleton.activeElements():
            if (element.nnodes() == 4 or not self.only_quads):
                for segment in element.getAspectRatioSegments(self.threshold,
                                                              self.skeleton):
                    yield segment

class CheckAspectRatio(SegmentRefinementTarget):
    def __init__(self, threshold, only_quads=True):
        self.threshold = threshold
        self.only_quads = only_quads
    def iterator(self, context):
        skel = context.getObject()
        return AspectSegmentIterator(skel, self.threshold, self.only_quads,
                                     condition=lambda x: x.active(skel))
       
registeredclass.Registration(
    'Aspect Ratio',
    RefinementTarget,
    CheckAspectRatio,
    ordering=2.5,
    params=[
        parameter.FloatParameter(
            'threshold', value=5.0,
            tip="Refine the long edges of elements whose aspect ratio is greater than this"),
        parameter.BooleanParameter(
            'only_quads', value=True,
            tip="Restrict the refinement to quadrilaterals?")],
    tip="Divide elements with extreme aspect ratios.",
    ## TODO: explain only_quads in the manual!  Also, aspect ratio is
    ## now computed differently.
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/check_aspect.xml'))

