# -*- python -*-
# $RCSfile: movenode.py,v $
# $Revision: 1.35 $
# $Author: langer $
# $Date: 2014/09/27 21:40:59 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import toolbox
from ooflib.common import ringbuffer
from ooflib.common import parallel_enable
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.SWIG.common import timestamp
from ooflib.common import primitives
from ooflib.engine import skeletondiff

class SelectedNode:
    def __init__(self, node=None):
        self.timestamp = timestamp.TimeStamp()
        self.node_ = node
        # visible is set by the gui toolbox when it switches into
        # keyboard mode.
        self.visible = node is not None

    def __repr__(self):
        return "MoveNodeSelection(%s)" % self.node

    def set(self, node=None):
        self.node_ = node
        if node is None: 
            visible = False
        self.timestamp.increment()
        return self

    def set_visible(self, val):
        self.visible = val
        self.timestamp.increment()

    def node(self):
        return self.node_

    def getTimeStamp(self):
        return self.timestamp

##########################################################################

class MoveNodeToolbox(toolbox.Toolbox):
    def __init__(self, gfxwindow):
        toolbox.Toolbox.__init__(self, 'Move_Nodes', gfxwindow)
        self.whoset = ('Skeleton',)
        self.selectednode = SelectedNode()
        self.allow_illegal=0
        self.skeleton = None
        self.sbcallbacks = [
            switchboard.requestCallback((self.gfxwindow(), "layers changed"),
                                        self.layersChangedCB)]

    def close(self):
        map(switchboard.removeCallback, self.sbcallbacks)
        
    def getSkeletonContext(self):
        return self.gfxwindow().topwho(*self.whoset)

    def makeMenu(self, menu):
        self.menu = menu
        menu.addItem(oofmenu.OOFMenuItem(
            'MoveNode',
            threadable=oofmenu.THREADABLE,
            callback = self.moveNode,
            params=[primitives.PointParameter('origin',
                                              tip=parameter.emptyTipString),
                    primitives.PointParameter('destination',
                                              tip=parameter.emptyTipString)],
            help="Move a node to another positon.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/move_node.xml')
            ))
        menu.addItem(oofmenu.OOFMenuItem(
            'SelectNode',
            callback = self.selectNode,
            params=[primitives.PointParameter('position',
                                              tip=parameter.emptyTipString)],
            help="Select a node to move.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/select_move_node.xml')
            ))
        menu.addItem(oofmenu.OOFMenuItem(
            'AllowIllegal',
            callback = self.allowIllegal,
            params=[parameter.BooleanParameter('allowed', 0,
                                               tip=parameter.emptyTipString)],
            help="Are illegal elements allowed?",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/allow_illegal.xml')
            ))

    def activate(self):
        pass
        
    def moveNode(self, menuitem, origin, destination):
        skelcontext = self.gfxwindow().topwho('Skeleton')
        if skelcontext:
            #
            if parallel_enable.enabled():
                from ooflib.engine.IO import skeletonIPC
                skeletonIPC.smenu.Move_Node_Helper(origin=origin,
                                                   destination=destination,
                                                   allow_illegal=self.allow_illegal,
                                                   skeletonpath=skelcontext.path())
                return
            #
            skeleton = skelcontext.getObject().deputyCopy()
            skeleton.activate()
            node = skeleton.nearestNode(origin)
            skelcontext.reserve()
            skelcontext.begin_writing()
            try:
                skeleton.moveNodeTo(node, destination)
                if node.illegal():
                    if self.allow_illegal==1:
                        skeleton.setIllegal()
                    else:
                        node.moveBack()
                elif skeleton.illegal(): # node motion may have rehabilitated
                    skeleton.checkIllegality()
                skelcontext.pushModification(skeleton)
            finally:
                skelcontext.end_writing()
                skelcontext.cancel_reservation()
            skeleton.needsHash()
            switchboard.notify('redraw')

    def selectNode(self, menuitem, position):
        context = apply(self.gfxwindow().topwho, self.whoset)
        if context:
            skeleton = context.getObject()
            self.selectednode.set(skeleton.nearestNode(position))
            switchboard.notify('redraw')
            switchboard.notify(("node selected", self))

    def allowIllegal(self, menuitem, allowed):
        self.allow_illegal=allowed
        switchboard.notify(("illegal-move status changed", self), allowed)

    def layersChangedCB(self):  # sb (gfxwindow, "layers changed")
        skelctxt = self.getSkeletonContext()
        if skelctxt is not self.skeleton:
            self.skeleton = skelctxt
            self.selectednode.set() # clears selection
            switchboard.notify(("skeleton changed", self))

    tip="Move Skeleton nodes interactively."
    discussion="""<para>
    Menu commands for moving &skel; nodes, based on mouse input.
    </para>"""
toolbox.registerToolboxClass(MoveNodeToolbox, ordering=2.6)
