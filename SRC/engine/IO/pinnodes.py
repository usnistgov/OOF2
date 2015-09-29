# -*- python -*-
# $RCSfile: pinnodes.py,v $
# $Revision: 1.37 $
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
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.common.IO import whoville
from ooflib.engine import skeletoncontext

# Toolbox for pinning nodes.  Pinned nodes don't move during mesh
# modification operations.  They *can* move during equilibration --
# they're not boundary conditions.  Pinned nodes are treated much like
# Skeleton Selectables, and share a lot of code with them.

class PinnedNodesToolbox(toolbox.Toolbox):
    def __init__(self, gfxwindow):
        toolbox.Toolbox.__init__(self, 'Pin_Nodes', gfxwindow)
        self.skeleton_param = whoville.WhoParameter(
            'skeleton', whoville.getClass('Skeleton'),
            tip=parameter.emptyTipString)
                                                    

    def makeMenu(self, menu):
        self.menu = menu
        menu.addItem(oofmenu.OOFMenuItem(
            'Pin',
            callback = self.pin,
            params=[self.skeleton_param,
                    primitives.PointParameter('point', tip='Target point.')],
            help="Pin the node closest to the given point.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/pin.xml')
            ))
        menu.addItem(oofmenu.OOFMenuItem(
            'UnPin',
            callback = self.unpin,
            params=[self.skeleton_param,
                    primitives.PointParameter('point', tip='Target point.')],
            help="Unpin the node closest to the given point.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/unpin.xml')
            ))
        menu.addItem(oofmenu.OOFMenuItem(
            'TogglePin',
            callback=self.togglepin,
            params=[self.skeleton_param,
                    primitives.PointParameter('point', tip='Target point.')],
            help="Toggle the pinnedness of the node closest to the given point.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/toggle_pin.xml')
            ))
        menu.addItem(oofmenu.OOFMenuItem(
            'UnPinAll',
            callback = self.unpinall,
            params=[self.skeleton_param],
            help="Unpin all nodes.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/unpin_all.xml')
            ))
        menu.addItem(oofmenu.OOFMenuItem(
            'Invert',
            callback = self.invert,
            params=[self.skeleton_param],
            help="Invert pinned nodes.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/invert_pin.xml')
            ))

        menu.addItem(oofmenu.OOFMenuItem(
            'Undo',
            callback=self.undoPin,
            params=[self.skeleton_param],
            help="Undo the latest pin.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/undo_pin.xml')
            ))
        menu.addItem(oofmenu.OOFMenuItem(
            'Redo',
            callback=self.redoPin,
            params=[self.skeleton_param],
            help="Redo the latest undone pin.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/redo_pin.xml')
            ))

    def pin(self, menuitem, skeleton, point):
        skelcontext = skeletoncontext.skeletonContexts[skeleton]
        skelcontext.pinnednodes.start()
        skelcontext.pinnednodes.pinPoint(point)
        skelcontext.pinnednodes.signal()

    def unpin(self, menuitem, skeleton, point):
        skelcontext = skeletoncontext.skeletonContexts[skeleton]
        skelcontext.pinnednodes.start()
        skelcontext.pinnednodes.unpinPoint(point)
        skelcontext.pinnednodes.signal()

    def togglepin(self, menuitem, skeleton, point):
        skelcontext = skeletoncontext.skeletonContexts[skeleton]
        skelcontext.pinnednodes.start()
        skelcontext.pinnednodes.togglepinPoint(point)
        skelcontext.pinnednodes.signal()

    def invert(self, menuitem, skeleton):
        skelcontext = skeletoncontext.skeletonContexts[skeleton]
        newpinned = skelcontext.getObject().notPinnedNodes()
        skelcontext.pinnednodes.start()
        skelcontext.pinnednodes.clear()
        skelcontext.pinnednodes.pin(newpinned)
        skelcontext.pinnednodes.signal()

    def unpinall(self, menuitem, skeleton):
        skelcontext = skeletoncontext.skeletonContexts[skeleton]
        skelcontext.pinnednodes.start()
        skelcontext.pinnednodes.clear()
        skelcontext.pinnednodes.signal()

    def undoPin(self, menuitem, skeleton):
        skelcontext = skeletoncontext.skeletonContexts[skeleton]
        skelcontext.pinnednodes.undo()
        skelcontext.pinnednodes.signal()

    def redoPin(self, menuitem, skeleton):
        skelcontext = skeletoncontext.skeletonContexts[skeleton]
        skelcontext.pinnednodes.redo()
        skelcontext.pinnednodes.signal()
            
    tip="Pin nodes."

    discussion="""<para>
    Pinned nodes are immobile during &skel; modifications.  This menu
    contains tools for pinning and unpinning nodes with mouse input.
    </para>"""

toolbox.registerToolboxClass(PinnedNodesToolbox, ordering=2.7)
