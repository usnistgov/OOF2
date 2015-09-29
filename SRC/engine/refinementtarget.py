# -*- python -*-
# $RCSfile: refinementtarget.py,v $
# $Revision: 1.22 $
# $Author: langer $
# $Date: 2010/12/07 21:57:03 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import progress
from ooflib.common import enum
from ooflib.common import registeredclass
from ooflib.common import utils
from ooflib.common.IO import parameter
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
from ooflib.engine.IO import skeletongroupparams

import math

class RefinementTarget(registeredclass.RegisteredClass):
    registry = []

    # Derived classes must override either __call__ or preprocess.
    def preprocess(self, skeleton, divisions, markedEdges):
        pass
    def __call__(self, skeleton, context, divisions, markedEdges, criterion):
        pass

    def markSegment(self, segment, divisions, markedEdges):
        markedEdges.mark(segment.nodes()[0], segment.nodes()[1], divisions)

    def markElement(self, element, divisions, markedEdges):
        nnodes = element.nnodes()
        if config.dimension() == 2:
            for i in range(nnodes):
                markedEdges.mark(element.nodes[i], element.nodes[(i+1)%nnodes],
                                 divisions)
        elif config.dimension() == 3:
            nsegments = element.getNumberOfEdges()
            for i in range(nsegments):
                segnodes = element.getSegmentNodes(i)
                markedEdges.mark(segnodes[0], segnodes[1], divisions)
    

    tip = "Determine which Skeleton segments will be refined."
    discussion = xmlmenudump.loadFile('DISCUSSIONS/engine/reg/refinementtarget.xml')

#########################################

class CheckAllElements(RefinementTarget):     
    def __call__(self, skeleton, context, divisions, markedEdges, criterion):
        prog = progress.findProgress("Refine")
        elements = skeleton.activeElements()
        n = len(elements)
        for i, element in enumerate(elements):
            if criterion(skeleton, element):
                self.markElement(element, divisions, markedEdges)
            if prog.stopped() :
                return
            prog.setFraction(1.0*(i+1)/n)
            prog.setMessage("checked %d/%d elements" % (i+1, n))

registeredclass.Registration(
    'All Elements',
    RefinementTarget,
    CheckAllElements,
    ordering=2,
    tip="Refine all elements.",
    discussion= "<para>Refine all segments of all elements.</para>")

###########################

class CheckSelectedElements(RefinementTarget):
    def __call__(self, skeleton, context, divisions, markedEdges, criterion):
        prog = progress.findProgress("Refine")
        elements = context.elementselection.retrieve()
        n = len(elements)
        for i, element in enumerate(elements):
            if element.active(skeleton) and criterion(skeleton, element):
                self.markElement(element, divisions, markedEdges)
            if prog.stopped():
                return
            else:
                prog.setFraction(1.0*(i+1)/n)
                prog.setMessage("checked %d/%d selected elements" % (i+1, n))

registeredclass.Registration(
    'Selected Elements',
    RefinementTarget,
    CheckSelectedElements,
    ordering=1,
    tip="Refine selected elements.",
    discussion= """<para>
    Refine all segments of the currently selected elements.
    </para>""")

class CheckElementsInGroup(RefinementTarget):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, context, divisions, markedEdges, criterion):
        prog = progress.findProgress("Refine")
        elements = context.elementgroups.get_group(self.group)
        n = len(elements)
##        for i in range(n):
##            element = elements[i]
        for i, element in enumerate(elements):
            if element.active(skeleton) and criterion(skeleton, element):
                self.markElement(element, divisions, markedEdges)
            if prog.stopped() :
                return
            prog.setFraction(1.0*(i+1)/n)
            prog.setMessage("checked %d/%d grouped elements" % (i+1, n))

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

######################

class CheckHomogeneity(RefinementTarget):
    def __init__(self, threshold):
        self.threshold = threshold
        
    def __call__(self, skeleton, context, divisions, markedEdges, criterion):
        prog = progress.findProgress("Refine")
        elements = skeleton.activeElements()
        n = len(elements)
        for i, element in enumerate(elements):
            if element.homogeneity(skeleton.MS) < self.threshold and \
               criterion(skeleton, element):
                self.markElement(element, divisions, markedEdges)
            if prog.stopped() :
                return
            prog.setFraction(1.0*(i+1)/n)
            prog.setMessage("checked %d/%d elements" % (i+1, n))
                
registeredclass.Registration(
    'Heterogeneous Elements',
    RefinementTarget,
    CheckHomogeneity,
    ordering=0,
    params=[parameter.FloatRangeParameter('threshold', (0.0, 1.0, 0.05),
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

#####################

class SegmentChooser(registeredclass.RegisteredClass):
    registry = []

    tip = "Choose sets of segments be refined."
    discussion = xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/segment_chooser.xml')

class FromAllSegments(SegmentChooser):
    def getSegments(self, context):
        return context.getObject().activeSegments()

registeredclass.Registration(
    'All Segments',
    SegmentChooser,
    FromAllSegments,
    4,
    tip="Examine all segments.",
    discussion= """<para>
    When choosing <link
    linkend='RegisteredClass-CheckHeterogeneousEdges'>heterogeneous</link>
    &sgmts; to <link linkend='RegisteredClass-Refine'>refine</link>,
    consider all &sgmts; of the &skel;.
    </para>""")

class FromSelectedSegments(SegmentChooser):
    def getSegments(self, context):
        segments = []
        for seg in context.segmentselection.retrieve():
            if seg.active(context.getObject()):
                segments.append(seg)
        return segments

registeredclass.Registration(
    'Selected Segments',
    SegmentChooser,
    FromSelectedSegments,
    ordering=1,
    tip="Examine selected segments.",
    discussion= """<para>
    When choosing <link
    linkend='RegisteredClass-CheckHeterogeneousEdges'>heterogeneous</link>
    &sgmts; to <link linkend='RegisteredClass-Refine'>refine</link>,
    consider only the currently selected &sgmts;.
    </para>""")

class FromSelectedElements(SegmentChooser):
    def getSegments(self, context):
        segments = set()
        for elem in context.elementselection.retrieve():
            if config.dimension() == 2:
                for i in range(elem.nnodes()):
                    n0 = elem.nodes[i]
                    n1 = elem.nodes[(i+1)%elem.nnodes()]
            elif config.dimension() == 3:
                for i in range(elem.getNumberOfEdges()):
                    (n0, n1) = elem.getSegmentNodes(i)
            seg = context.getObject().findSegment(n0, n1)
            if seg.active(context.getObject()):
                segments.add(seg)
        # TODO: Does the return value have to be a list?  Can it be
        # left as a set?
        return list(segments)

registeredclass.Registration(
    'Selected Elements',
    SegmentChooser,
    FromSelectedElements,
    ordering=1,
    tip="Examine segments from segments of currently selected elements.",
    discussion= """<para>
    When choosing <link
    linkend='RegisteredClass-CheckHeterogeneousEdges'>heterogeneous</link>
    &sgmts; to <link linkend='RegisteredClass-Refine'>refine</link>,
    consider only the edges of the currently selected &elems;.
    </para>""")

class CheckHeterogeneousEdges(RefinementTarget):
    def __init__(self, threshold, choose_from):
        self.threshold = threshold
        self.choose_from = choose_from
        
    def __call__(self, skeleton, context, divisions, markedEdges, criterion):
        microstructure = skeleton.MS
        prog = progress.findProgress("Refine")
        segments = self.choose_from.getSegments(context)
        n = len(segments)
        for i, segment in enumerate(segments):
            if segment.homogeneity(microstructure) < self.threshold:
                self.markSegment(segment, divisions, markedEdges)
            if prog.stopped():
                return
            prog.setFraction(1.0*(i+1)/n)
            prog.setMessage("checked %d/%d segments" % (i+1, n))

registeredclass.Registration(
    'Heterogeneous Segments',
    RefinementTarget,
    CheckHeterogeneousEdges,
    ordering=3,
    params=[parameter.FloatRangeParameter('threshold', (0.0, 1.0, 0.05),
                                          value=0.9,
                                          tip="Refine segments whose homogeneity is less than this."),
            parameter.RegisteredParameter('choose_from', SegmentChooser,
                                          tip='Segments to consider.')],
    tip="Divide heterogeneous segments.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/check_hetero_segs.xml'))

class CheckSelectedEdges(RefinementTarget):
    def __call__(self, skeleton, context, divisions, markedEdges, criterion):
        prog = progress.findProgress("Refine")
        segments = context.segmentselection.retrieve()
        n = len(segments)
        for i, segment in enumerate(segments):
            if segment.active(skeleton):
                self.markSegment(segment, divisions, markedEdges)
            if prog.stopped():
                return
            prog.setFraction(1.0*(i+1)/n)
            prog.setMessage("checked %d/%d segments" % (i+1, n))

registeredclass.Registration(
    'Selected Segments',
    RefinementTarget,
    CheckSelectedEdges,
    ordering=3,
    tip="Divide selected segments.",
    discussion="""<para>
    <xref linkend='RegisteredClass-Refine'/> all currently selected &sgmts;.
    </para>""")

class CheckSegmentGroup(RefinementTarget):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, context, divisions, markedEdges, criterion):
        prog = progress.findProgress("Refine")
        segments = context.segmentgroups.get_group(self.group)
        n = len(segments)
        for i, segment in enumerate(segments):
            if segment.active(skeleton):
                self.markSegment(segment, divisions, markedEdges)
            if prog.stopped():
                return
            prog.setFraction(1.0*(i+1)/n)
            prog.setMessage("checked %d/%d segments" % (i+1, n))


registeredclass.Registration(
    'Segments in Group',
    RefinementTarget,
    CheckSegmentGroup,
    ordering=3.5,
    params=[skeletongroupparams.SegmentGroupParameter('group',
                                                      tip='Examine segments in this group')],
    tip="Refine segments in a segment group",
    discussion="""<para>
    Refine a Skeleton by divided the segments in the given segment group.
    </para>"""
    )

#####################

if config.dimension() == 2:
    # So far, this rule only does anything for quads in 2D and since
    # we only have tets in 3D for now, it's disabled.

    class CheckAspectRatio(RefinementTarget):
       def __init__(self, threshold, only_quads=True):
           self.threshold = threshold
           self.only_quads = only_quads
       def __call__(self, skeleton, context, divisions, markedEdges, criterion):
           prog = progress.findProgress("Refine")
           elements = skeleton.activeElements()
           n = len(elements)
           for i, element in enumerate(elements):
               if (criterion(skeleton, element) and (element.nnodes() == 4 or
                                                     not self.only_quads)):
                   for segment in element.getAspectRatioSegments(self.threshold,
                                                                 skeleton):
                       if segment.active(skeleton):
                           self.markSegment(segment, divisions, markedEdges)
               if prog.stopped():
                   return
               prog.setFraction(1.0*(i+1)/n)
               prog.setMessage("checked %d/%d elements" % (i+1, n))



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
## TODO: explain only_quads in the manual!
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/check_aspect.xml'))

    ##################################################
