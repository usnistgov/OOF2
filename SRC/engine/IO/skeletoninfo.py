# -*- python -*-
# $RCSfile: skeletoninfo.py,v $
# $Revision: 1.46 $
# $Author: langer $
# $Date: 2011/04/12 18:05:49 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import timestamp
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import ringbuffer
from ooflib.common import toolbox
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import deputy
if config.dimension() == 2:
    from ooflib.engine import skeletonelement
elif config.dimension() == 3:
    from ooflib.engine import skeletonelement3d as skeletonelement
from ooflib.engine import skeletonnode
from ooflib.engine import skeletonsegment

from ooflib.common import parallel_enable
if parallel_enable.enabled():
    from ooflib.SWIG.common import mpitools
    from ooflib.engine.IO import skeletonIPC

SkeletonElement = skeletonelement.SkeletonElement
SkeletonSegment = skeletonsegment.SkeletonSegment
SkeletonNode = skeletonnode.SkeletonNode

## TODO: Rewrite this entire toolbox.  It's a mess. It's been patched
## and repatched to keep it working, but there's not much elegance
## left in the code...

class SkeletonQueryContainer:
    def __init__(self, context):
#         self.timestamp = timestamp.TimeStamp()
        self.context = context
        self.skeleton = context.getObject()
        self.object = None
        self.position = None
        self.targetname = None

    def set(self, context=None, object=None, targetname=None, position=None):
        self.context = context
        self.object = object
        self.targetname = targetname
        self.position = position
#         self.timestamp.increment()

    def reset(self):
        self.set()
        self.context = None
        self.skeleton = None

#     def getTimeStamp(self):
#         return self.timestamp

    def clone(self):
        krusty = SkeletonQueryContainer(self.context)
        krusty.skeleton = self.skeleton
        krusty.object = self.object
        krusty.targetname = self.targetname
        krusty.position = self.position
#         krusty.timestamp.increment()
        return krusty

    def clearable(self):
        return not not self.object

    def __repr__(self):
        return "SkeletonQueryContainer(%s, %s, %s)" % (self.object, self.position, self.targetname)

class SkeletonPeekContainer(SkeletonQueryContainer):
    def __init__(self, toolbox, context):
        self.toolbox = toolbox
#         self.timestamp = timestamp.TimeStamp()
        self.context = context
        self.skeleton = context.getObject()
        # self.objects is used by skeletoninfodisplay.py
        self.objects = {"Element":None, "Segment":None, "Node":None}

    def assignObject(self, object, objtype):
        self.objects[objtype] = object
        self.toolbox.timestamp.increment()
#         self.timestamp.increment()

    def removeObject(self, objtype):
        self.objects[objtype] = None
        self.toolbox.timestamp.increment()
#         self.timestamp.increment()

    def reset(self):
        self.objects = {"Element":None, "Segment":None, "Node":None}
#         self.timestamp.increment()
        self.context = None
        self.skeleton = None

#     def getTimeStamp(self):
#         return self.timestamp

##################################################################
            
class SkeletonInfoToolbox(toolbox.Toolbox):
    def __init__(self, gfxwindow):
        toolbox.Toolbox.__init__(self, 'Skeleton_Info', gfxwindow)
        self.whoset = ('Skeleton',)
        self.querier = None
        self.peeker = None        
        self.records = ringbuffer.RingBuffer(49)
        self.timestamp = timestamp.TimeStamp()
        self.timestamp.backdate()

        self.sbcallbacks = [
            # Looks for a skeleton on the gfx window.
            switchboard.requestCallback((self.gfxwindow(), "layers changed"),
                                        self.newLayers),
            # Looks for a skeleton modification.
            switchboard.requestCallback(('who changed', 'Skeleton'),
                                        self.skelChanged)
            ]

    def close(self):
        map(switchboard.removeCallback, self.sbcallbacks)
        self.sbcallbacks = []

    def getSkeletonContext(self):
        return self.gfxwindow().topwho(*self.whoset)

    def makeMenu(self, menu):
        self.menu = menu
        menu.addItem(oofmenu.OOFMenuItem(
            'QueryElement',
            callback=self.queryElem,
            params=[primitives.PointParameter('position', tip='Target point.')],
            help="Query the element closest to the given point.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/engine/menu/query_skel_elem.xml')
            ))
        menu.addItem(oofmenu.OOFMenuItem(
            'QueryElementByID',
            callback=self.queryElemByID,
            params=[parameter.IntParameter('index', tip="Element index.")],
            help="Query the element with the given index.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/engine/menu/query_skel_elem_id.xml')))
        menu.addItem(oofmenu.OOFMenuItem(
            'QuerySegment',
            callback=self.querySgmt,
            params=[primitives.PointParameter('position', tip='Target point.')],
            help="Query the segment closest to the given point.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/engine/menu/query_skel_sgmt.xml')
            ))
        menu.addItem(oofmenu.OOFMenuItem(
            'QuerySegmentByID',
            callback=self.querySgmtByID,
            params=[parameter.IntParameter('index', tip="Segment index.")],
            help="Query the segment with the given index.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/engine/menu/query_skel_sgmt_id.xml')))
        menu.addItem(oofmenu.OOFMenuItem(
            'QueryNode',
            callback=self.queryNode,
            params=[primitives.PointParameter('position', tip='Target point.')],
            help="Query the node closest to the given point.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/engine/menu/query_skel_node.xml')
            ))
        menu.addItem(oofmenu.OOFMenuItem(
            'QueryNodeByID',
            callback=self.queryNodeByID,
            params=[parameter.IntParameter('index', tip="Node index.",)],
            help="Query the node with the given index.",
            discussion=xmlmenudump.loadFile(
                    'DISCUSSIONS/engine/menu/query_skel_node_id.xml')))


    def activate(self):
        # Called when this toolbox has been brought to the front.
        skelcontext = self.getSkeletonContext()
        if skelcontext is not None:
            if not self.querier:
                self.querier = SkeletonQueryContainer(skelcontext)
            if not self.peeker:
                self.peeker = SkeletonPeekContainer(self, skelcontext)
        else:
            self.querier = None
            self.peeker = None

    def newLayers(self):
        lastskel = None
        if self.querier:
            lastskel = self.querier.context
        skelcontext = self.getSkeletonContext()
        if lastskel is not skelcontext:
            self.resetRecords()
            if skelcontext is None:
                self.clearQuerier()
            else:
                self.querier = SkeletonQueryContainer(skelcontext)
                self.peeker = SkeletonPeekContainer(self, skelcontext)
            self.timestamp.increment()
            switchboard.notify((self, "new skeleton"))

    def skelChanged(self, context):
        skelcontext = self.getSkeletonContext()
        if context is not skelcontext:
            return
        if not skelcontext:     # No skeleton on the gfx window.
            self.clearQuerier()
            self.resetRecords()
        elif isinstance(context.getObject(), deputy.DeputySkeleton):
            if self.querier:
                if (context.getObject().sheriffSkeleton() is 
                    self.querier.skeleton):
                    # The modification only moved nodes.  It is not
                    # necessary to dump all the records.  Just reflect
                    # new node positions, if applicable.
                    self.querysignal()
                else:
                    self.resetRecords()
                    self.querier = SkeletonQueryContainer(skelcontext)
                    self.peeker = SkeletonPeekContainer(self, skelcontext)
                    self.querysignal()                    
            else:
                self.querier = SkeletonQueryContainer(skelcontext)
                self.peeker = SkeletonPeekContainer(self, skelcontext)
        else:
            # The skeleton has been modified.  The query records
            # should be reset, since "prev", "next" would be
            # meaningless after modifications such as "Refine" or
            # "Rationalize".
            self.resetRecords()
            self.querier = SkeletonQueryContainer(skelcontext)
            self.peeker = SkeletonPeekContainer(self, skelcontext)
            self.querysignal()
        self.timestamp.increment()
        
    def resetRecords(self):
        self.records.clear()

    def queryElem(self, menuitem, position):
        context = self.getSkeletonContext()
        if not context:
            return
        skeleton = context.getObject()

        if parallel_enable.enabled():
            skeletonIPC.smenu.Skel_Info_Query(targetname="Element",
                                              position=position,skeleton=context.path())
            if mpitools.Rank()>0:
                return

        elem = skeleton.enclosingElement(position)
        if not elem:
            reporter.report("Try to click ON an Element, dude.")
        else:
            self.finishQuery(context, elem, "Element", position)

    def queryElemByID(self, menuitem, index):
        context = self.getSkeletonContext()
        if context:
            skeleton = context.getObject()
            for e in skeleton.elements:
                if e.index == index:
                    self.finishQuery(context, e, "Element", e.repr_position())

    def querySgmt(self, menuitem, position):
        context = self.getSkeletonContext()
        if not context:
            return
        skeleton = context.getObject()

        if parallel_enable.enabled():
            skeletonIPC.smenu.Skel_Info_Query(targetname="Segment",
                                              position=position,skeleton=context.path())
            if mpitools.Rank()>0:
                return

        sgmt = skeleton.nearestSgmt(position)
        if not sgmt:
            reporter.report("Avoid clicking OUTSIDE of a skeleton.")
        else:
            self.finishQuery(context, sgmt, "Segment", position)

    def querySgmtByID(self, menuitem, index):
        context = self.getSkeletonContext()
        if context:
            skeleton = context.getObject()
            for s in skeleton.segments.values():
                if s.index == index:
                    self.finishQuery(context, s, "Segment", s.repr_position())

    def queryNode(self, menuitem, position):            
        context = self.getSkeletonContext()
        if not context:
            return
        skeleton = context.getObject()

        if parallel_enable.enabled():
            skeletonIPC.smenu.Skel_Info_Query(
                targetname="Node", position=position,skeleton=context.path())
            if mpitools.Rank()>0:
                return

        node = skeleton.nearestNode(position)
        if not node:
            reporter.report("Avoid clicking OUTSIDE of a skeleton.")
        else:
            self.finishQuery(context, node, "Node", position)

    def queryNodeByID(self, menuitem, index):
        context = self.getSkeletonContext()
        if context:
            skeleton = context.getObject()
            for n in skeleton.nodes:
                if n.index == index:
                    self.finishQuery(context, n, "Node", n.repr_position())

    def finishQuery(self, context, object, targetname, position):
        if self.querier:
            self.querier.set(context=context, object=object,
                             targetname=targetname, position=position)
        else:
            self.querier = SkeletonQueryContainer(context)
            self.querier.set(context=context, object=object,
                             targetname=targetname, position=position)
        self.records.push(self.querier.clone())
        if self.peeker is None:
            self.peeker = SkeletonPeekContainer(self, context)
        self.peeker.reset()
        self.timestamp.increment()
        self.querysignal()
        switchboard.notify("redraw")
        
    def querysignal(self):
        switchboard.notify((self.gfxwindow(),"query skeleton"))

    def clearQuerier(self):
        self.querier = None
        self.peeker = None
        self.timestamp.increment()
        
    def prev_able(self):
        return not self.records.atBottom()

    def next_able(self):
        return not self.records.atTop()

    tip="Get information about Skeleton components."
    discussion="""<para>
    Get information about &skel; components, based on mouse input.
    </para>"""
    
toolbox.registerToolboxClass(SkeletonInfoToolbox, ordering=2.0)
