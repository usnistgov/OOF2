# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import ooferror

from ooflib.SWIG.common import config
from ooflib.SWIG.common import lock
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import primitives
from ooflib.common import subthread
from ooflib.common import utils
from ooflib.common.IO import mainmenu
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import toolboxGUI
from ooflib.engine.IO import movenode

from ooflib.common.runtimeflags import digits 

import oofcanvas
from oofcanvas import oofcanvasgui

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

## TODO PYTHON3: Fix keyboard mode

class MoveNodeToolboxGUI(toolboxGUI.GfxToolbox, mousehandler.MouseHandler):
    def __init__(self, movenodetoolbox):
        debug.mainthreadTest()
        self.downed = 0                 # is the mouse button down?
        self.moving = 0                 # in the middle of a move
        self.movingnode = None          # node being moved
        # writable should only be set by self.set_writable, which
        # issues a checkpoint.
        self.writable = True            # is the top most Skeleton writable?
        self.mode = "Mouse"
        self.mouselock = lock.Lock()
        
        toolboxGUI.GfxToolbox.__init__(self, "Move Nodes", movenodetoolbox)
        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                          spacing=2, margin=2)
        self.gtk.add(mainbox)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        mainbox.pack_start(hbox, expand=False, fill=False, padding=0)
        gtklogger.setWidgetName(hbox, "MoveWith")
        hbox.pack_start(Gtk.Label(label="Move with: "),
                        expand=False, fill=False, padding=0)

        modes = [("Mouse", "Click and drag a node to move it."),
                 ("Keyboard",
                  "Select a node, type a position, and click the Move button")
                 ]
        self.modebuttons = []
        for mode, tip in modes:
            if self.modebuttons:
                button = Gtk.RadioButton(label=mode,
                                         group=self.modebuttons[0])
            else:
                button = Gtk.RadioButton(label=mode)
            gtklogger.setWidgetName(button, mode)
            self.modebuttons.append(button)
            button.set_tooltip_text(tip)
            hbox.pack_start(button, expand=False, fill=False, padding=0)
            button.set_active(self.mode is mode)
            gtklogger.connect(button, 'clicked', self.changeMode, mode)

        # allow illegal move?
        self.allow_illegal = Gtk.CheckButton(label="Allow illegal moves")
        gtklogger.setWidgetName(self.allow_illegal, "AllowIllegal")
        mainbox.pack_start(self.allow_illegal,
                           expand=False, fill=False, padding=0)
        mainbox.pack_start(
            Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL),
            expand=False, fill=False, padding=0)
        gtklogger.connect(self.allow_illegal, "clicked", self.illegal_status)
        if movenodetoolbox.allow_illegal:
            self.allow_illegal.set_active(True)
        else:
            self.allow_illegal.set_active(False)

        self.table = Gtk.Grid(row_spacing=2, column_spacing=2)
        r = 2
        mainbox.pack_start(self.table, expand=False, fill=False, padding=0)

        label = Gtk.Label(label='x=', halign=Gtk.Align.END, hexpand=False)
        self.table.attach(label, 0,0, 1,1)
        self.xtext = Gtk.Entry(editable=True,
                               halign=Gtk.Align.FILL, hexpand=True)
        self.table.attach(self.xtext, 1,0, 1,1)
        gtklogger.setWidgetName(self.xtext, "x")
        self.xsignal = gtklogger.connect_passive(self.xtext, 'changed')
        self.xtext.set_width_chars(12)
        self.xtext.set_tooltip_text("x position of the mouse")

        label = Gtk.Label(label='y=', halign=Gtk.Align.END, hexpand=False)
        self.table.attach(label, 0,1, 1,1)
        self.ytext = Gtk.Entry(editable=True,
                               halign=Gtk.Align.FILL, hexpand=True)
        self.table.attach(self.ytext, 1,1, 1,1)
        gtklogger.setWidgetName(self.ytext, 'y')
        self.ysignal = gtklogger.connect_passive(self.ytext, 'changed')
        self.ytext.set_width_chars(12)
        self.ytext.set_tooltip_text("y position of the mouse")

        label = Gtk.Label(label="Change in... ",
                          halign=Gtk.Align.END, hexpand=False)
        self.table.attach(label, 0,2, 1,1)

        label = Gtk.Label(label="shape energy=",
                          halign=Gtk.Align.END, hexpand=False)
        self.table.attach(label, 0,3, 1,1)
        self.shapetext = Gtk.Entry(editable=False,
                                   hexpand=True, halign=Gtk.Align.FILL)
        gtklogger.setWidgetName(self.shapetext,"shape")
        self.shapetext.set_width_chars(12)
        self.table.attach(self.shapetext, 1,3, 1,1)
        self.shapetext.set_tooltip_text("total change in shape energy")

        label = Gtk.Label(label="homogeneity=",
                          halign=Gtk.Align.END, hexpand=False)
        self.table.attach(label, 0,4, 1,1)
        self.homogtext = Gtk.Entry(editable=False,
                                   hexpand=True, halign=Gtk.Align.FILL)
        gtklogger.setWidgetName(self.homogtext,"homog")
        self.homogtext.set_width_chars(12)
        self.table.attach(self.homogtext, 1,4, 1,1)
        self.homogtext.set_tooltip_text("total change in homogeneity")

        mainbox.pack_start(
            Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL),
            expand=False, fill=False, padding=0)

        self.statusText = Gtk.Label(valign=Gtk.Align.END)
        gtklogger.setWidgetName(self.statusText, "Status")
        mainbox.pack_start(self.statusText, expand=True, fill=False, padding=0)
        
        bbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                       valign=Gtk.Align.END, vexpand=True,
                       halign=Gtk.Align.FILL, homogeneous=True, spacing=2)
        mainbox.pack_start(bbox, expand=True, fill=True, padding=0)
        self.undobutton = gtkutils.StockButton("edit-undo-symbolic", "Undo")
        self.undobutton.set_tooltip_text("Undo the latest node move.")
        self.movebutton = Gtk.Button(label='Move')
        self.movebutton.set_tooltip_text(
            "Move the selected node to the specified position.")
        self.redobutton = gtkutils.StockButton("edit-redo-symbolic", "Redo")
        self.redobutton.set_tooltip_text("Redo the latest UNDO.")

        gtklogger.setWidgetName(self.undobutton, 'Undo')
        gtklogger.setWidgetName(self.redobutton, 'Redo')
        gtklogger.setWidgetName(self.movebutton, 'Move')
        bbox.pack_start(self.undobutton, expand=True, fill=True, padding=0)
        bbox.pack_start(self.movebutton, expand=True, fill=True, padding=0)
        bbox.pack_start(self.redobutton, expand=True, fill=True, padding=0)
        gtklogger.connect(self.undobutton, 'clicked', self.undoCB)
        gtklogger.connect(self.movebutton, 'clicked', self.moveCB)
        gtklogger.connect(self.redobutton, 'clicked', self.redoCB)

        self.sbcallbacks = [
            switchboard.requestCallbackMain(('who changed', 'Skeleton'),
                                            self.skelChanged),
            switchboard.requestCallbackMain("made reservation",
                                            self.rsrvChanged,
                                            1),
            switchboard.requestCallbackMain("cancelled reservation",
                                            self.rsrvChanged, 0),
            switchboard.requestCallbackMain(("node selected",
                                             movenodetoolbox),
                                            self.nodeSelected),
            switchboard.requestCallbackMain(("illegal-move status changed",
                                             movenodetoolbox),
                                            self.illegal_status_changed),
            switchboard.requestCallbackMain(("skeleton changed", 
                                             movenodetoolbox),
                                            self.layersChanged)
            ]
        self.move_info(None, '---', '---', '')

    def node(self):
        return self.toolbox.selectednode.node()

    def illegal_status_changed(self, status):
        debug.mainthreadTest()
        self.allow_illegal.set_active(status)
        
    def illegal_status(self, gtkobj):
        debug.mainthreadTest()
        if self.allow_illegal.get_active():
            self.toolbox.menu.AllowIllegal(allowed=True)
        else:
            self.toolbox.menu.AllowIllegal(allowed=False)
            
    def changeMode(self, button, mode):
        debug.mainthreadTest()
        if button.get_active():
            self.mode = mode
            self.toolbox.selectednode.set_visible(mode=="Keyboard")
            if self.mode == "Mouse":
                self.move_info(None, "---", "---", "")
            else:
                if self.node() is not None:
                    self.move_info(self.node().position(),
                                   "---", "---", "")
            self.sensitize()
            switchboard.notify('redraw')

    def getSkeletonContext(self):
        return self.gfxwindow().topwho('Skeleton')
    
    def getSkeleton(self):
        return self.gfxwindow().topmost('Skeleton')

    def illegalityText(self):
        skel = self.getSkeleton()
        if skel:
            n = self.getSkeleton().nillegal()
            if n:
                return "%d illegal element%s in the skeleton.\n" % (n,
                                                                    "s"*(n!=1))
        return ""

    def skelChanged(self, skelcontext): # sb ("who changed", "Skeleton")
        debug.mainthreadTest()
        if skelcontext is self.getSkeletonContext():
            self.statusText.set_text(self.illegalityText())
            self.sensitize()
        
    def sensitize(self):
        debug.mainthreadTest()
        skeletoncontext = self.getSkeletonContext()
        reserved = skeletoncontext is not None and \
                   skeletoncontext.query_reservation()
        self.undobutton.set_sensitive(skeletoncontext is not None
                                      and not reserved
                                      and skeletoncontext.undoable())
        self.redobutton.set_sensitive(skeletoncontext is not None
                                      and not reserved
                                      and skeletoncontext.redoable())
        
        self.movebutton.set_sensitive(self.mode == "Keyboard"
                                      and self.node() is not None
                                      and not reserved)
        editable = (self.mode == "Keyboard" and self.node() is not None)
        self.xtext.set_editable(editable)
        self.ytext.set_editable(editable)

        gtklogger.checkpoint(self.gfxwindow().name + " " +
                             self._name + " sensitized")

    def rsrvChanged(self, reserved, whocls):
        skelcontext = self.getSkeletonContext()
        if (skelcontext and skelcontext.path() == whocls.path()):
            self.sensitize()
            self.set_writable(not reserved)

    def set_writable(self, val):
        self.writable = val
        # This checkpoint is required because the state of
        # self.writable affects which mouse events are processed.
        # Those mouse events can trigger other checkpoints, so if the
        # writable flag is set wrongly, the other checkpoints might
        # not be reached.
        gtklogger.checkpoint("Move Node toolbox writable changed")

    def nodeChanged(self):
        # See comment in set_writable()
        gtklogger.checkpoint("Move Node toolbox node changed")
        
    # Notice if the new topmost skeleton is writable.  Callback for
    # switchboard "skeleton changed" signal, which is emitted by the
    # non-gui part of this toolbox when the topmost gfxwindow skeleton
    # changes (in response to the "layers changed" switchboard signal).
    def layersChanged(self, *args): # switchboard "skeleton changed"
        skelcontext = self.getSkeletonContext()
        self.set_writable(skelcontext and not skelcontext.query_reservation())
        mainthread.runBlock(self.move_info, 
                            (None, "---", "---", self.illegalityText()))
        mainthread.runBlock(self.sensitize)

    def activate(self):
        toolboxGUI.GfxToolbox.activate(self)
        self.gfxwindow().setMouseHandler(self)
        self.motionFlag = self.gfxwindow().allowMotionEvents(
            oofcanvasgui.MotionAllowed_MOUSEDOWN)
        self.sensitize()

    def deactivate(self):
        toolboxGUI.GfxToolbox.deactivate(self)
        self.gfxwindow().removeMouseHandler()
        self.gfxwindow().allowMotionEvents(self.motionFlag)

    def close(self):
        switchboard.removeCallbacks(self.sbcallbacks)
        toolboxGUI.GfxToolbox.close(self)

    def move_info(self, point, homogtext, shapetext, labeltext):
        debug.mainthreadTest()
        self.showPosition(point)
        self.homogtext.set_text(homogtext)
        self.shapetext.set_text(shapetext)
        self.statusText.set_text(labeltext)
        gtklogger.checkpoint("Move Node toolbox info updated")

    def showPosition(self, point, dummy1=None, dummy2=None):
        debug.mainthreadTest()
        self.xsignal.block()
        self.ysignal.block()
        try:
            if point is None:
                self.xtext.set_text('---')
                self.ytext.set_text('---')
            else:
                self.xtext.set_text(("%-11.4g" % point[0]).rstrip())
                self.ytext.set_text(("%-11.4g" % point[1]).rstrip())
        finally:
            self.xsignal.unblock()
            self.ysignal.unblock()

    def acceptEvent(self, eventtype):
        if not self.writable: # Don't accept events if the skeleton is busy.
            return 0       
        if self.mode == "Mouse":
            return eventtype=='down' or \
                   (self.downed and eventtype in ('move', 'up'))
        elif self.mode == "Keyboard":
            return eventtype=='up'

    def down(self, x, y, button, shift, ctrl, data):
        # The RubberBand object needs to be created on the main thread
        # before this method returns, because the Canvas will want to
        # use it right away.  A reference to it is held here to ensure
        # that it won't be destroyed before we're done with it.
        ## TODO GTK3: Make rubber band parameters settable.
        self.rb = oofcanvasgui.SpiderRubberBand()
        self.rb.setLineWidth(1)
        self.rb.setColor(oofcanvas.black)
        self.rb.setDashColor(oofcanvas.white)
        self.rb.setDashLength(7)
        self.gfxwindow().setRubberBand(self.rb)
        subthread.execute(self.down_subthread, (x,y,button,shift,ctrl))

    def down_subthread(self, x, y, button, shift, ctrl):
        debug.subthreadTest()
        self.mouselock.acquire()
        try:
            self.downed = 1
            point = self.getPoint(x,y)

            skel = mainthread.runBlock(self.getSkeleton)
            skelctxt = mainthread.runBlock(self.getSkeletonContext)
            reserved = skel is not None and skelctxt.query_reservation()
            if skel is not None and not reserved and point is not None:
                self.movingnode = skel.nearestNode(point)
                self.nodeChanged()
                # Store this point for use by the up callback's call to MoveNode
                self.downpt = point
                if self.movingnode.pinned():
                    self.nodeChanged()
                    self.movingnode = None
                else:
                    # Mouse-down events are only accepted in Mouse mode,
                    # so the end_reading() call corresponding to this
                    # begin_reading() is in the "Mouse" section of the
                    # up() callback.
                    skelctxt.begin_reading()
                    self.nbrnodes = self.movingnode.aperiodicNeighborNodes(skel)
                    self.nbrelements = self.movingnode.neighborElements()
                    self.startpt = self.movingnode.position()
                    # Get initial values of homogeneity and shape energy
                    self.homogeneity0 = 0.0
                    self.shapeenergy0 = 0.0
                    for element in self.nbrelements:
                        if not element.illegal():
                            self.homogeneity0 += element.homogeneity(skel.MS,
                                                                     False)
                            self.shapeenergy0 += element.energyShape()

                    mainthread.runBlock(
                        self.rb.addPoints,
                        ([n.position() for n in self.nbrnodes],))
                    self.rb.update((x, y))
                    # Don't do a full GfxWindow.draw.  There's no need
                    # to refresh anything except the rubberband here.
                    mainthread.runBlock(self.gfxwindow().oofcanvas.draw)
                    
            gtklogger.checkpoint("Move Node toolbox down event")
        finally:
            self.mouselock.release()

        if self.movingnode:
            # The position of the mouse down event is not necessarily
            # exactly the original position of the node, so the
            # handler needs to incorporate a move to the position of
            # the event.
            self.move_thread(self.getSkeleton(), x, y, button, shift, ctrl)
            
    def move(self, x, y, button, shift, ctrl, data):
        skeleton = self.getSkeleton()
        subthread.execute(self.move_thread,
                          (skeleton, x, y, button, shift, ctrl))
    def move_thread(self, skeleton, x, y, button, shift, ctrl):
        debug.subthreadTest()
        self.mouselock.acquire()
        try:
            if self.movingnode is not None:
                self.moving = 1
                homogeneity = 0.0
                shapeenergy = 0.0
                point = self.getPoint(x,y)
                # It's generally forbidden to call node.moveTo instead of
                # skeleton.moveNodeTo, but since we're going to move the
                # node back (see up(), below), it's ok.
                if point is not None:
                    self.movingnode.moveTo(point)
                if self.movingnode.illegal():
                    homogtext = "---"
                    shapetext = "---"
                    labeltext = "Illegal node position!"
                else:
                    for element in self.nbrelements:
                        # Evaluating homogeneity and shape energy is
                        # safe, because the Skeleton's read lock was
                        # acquired when the mouse went down.
                        homogeneity += element.homogeneity(skeleton.MS, False)
                        shapeenergy += element.energyShape()
                    dh = homogeneity - self.homogeneity0
                    homogtext = f"{dh:.{digits()}f}"
                    ds = shapeenergy - self.shapeenergy0
                    shapetext = f"{ds:.{digits()}f}"
                    labeltext = ""
                mainthread.runBlock(self.move_info,
                                    (point, homogtext, shapetext, labeltext))
                gtklogger.checkpoint("Move Node toolbox move event")
        finally:
            self.mouselock.release()

    # self.allow_illegal CheckButton to decide whether or not illegal
    # moves are allowed, and if it gets an illegal-and-not-allowed
    # move, the move is not performed -- no menu items are called,
    # nothing is scripted.

    def up(self, x, y, button, shift, ctrl, data):
        # "Downed" must be cleared at the earliest opportunity,
        # otherwise spurious "move" events can be processed,
        # unilaterally changing the node position.
        self.downed = 0
        self.rb = None
        self.gfxwindow().setRubberBand(None)
        subthread.execute(self.up_subthread, (x, y, button, shift, ctrl))

    def up_subthread(self, x, y, button, shift, ctrl):
        debug.subthreadTest()
        self.mouselock.acquire()
        try:
            point = self.getPoint(x,y)
            if self.mode == "Mouse":
                skelcontext = mainthread.runBlock(self.getSkeletonContext)
                if skelcontext is not None:
                    skelcontext.end_reading()
                if self.moving:
                    self.moving = 0 # Dunmovin, CA is east of the Sierra Nevada
                    mainthread.runBlock(self.showPosition, (point,))
                    # Accept/reject conditon:
                    # Allow_illegal is ON : unconditionally accept everything
                    # Allow_illegal is OFF : any node associated with
                    # illegal nodes before or after will not be moved.
                    aige = mainthread.runBlock(self.allow_illegal.get_active)
                    if self.movingnode.illegal() and not aige:
                        # Restore the state of the skeleton, and show
                        # the original position in the toolbox.
                        self.movingnode.moveTo(self.startpt)
                        mainthread.runBlock(self.showPosition, (self.startpt,))
                        mainthread.runBlock(self.statusText.set_text,
                                            (self.illegalityText(),))
                    else:
                        # Restore the state of the skeleton so that the non-GUI
                        # movenode command can do the real work.
                        self.movingnode.moveTo(self.startpt)
                        try:
                            self.toolbox.menu.MoveNode(
                                origin=self.downpt,
                                destination=point)
                        finally:
                            self.gfxwindow().setRubberBand(None)
                            self.nbrnodes = []

            elif self.mode == "Keyboard":
                self.toolbox.menu.SelectNode(position=point)
            gtklogger.checkpoint("Move Node toolbox up event")
        finally:
            self.mouselock.release()

    def nodeSelected(self):             # sb ("node selected", toolbox)
        # This is called via the switchboard after the SelectNode menu
        # callback has finished.  It must be called this way, so that
        # the menu callback is guaranteed to have finished and
        # self.toolbox.selectednode has been set.
        self.nodeChanged()
        self.showPosition(self.node().position())
        self.sensitize()
        
    def undoCB(self, button):
        mainmenu.OOF.Skeleton.Undo(skeleton=self.getSkeletonContext().path())

    def redoCB(self, button):
        mainmenu.OOF.Skeleton.Redo(skeleton=self.getSkeletonContext().path())

    # Move button callback in Keyboard mode
    def moveCB(self, button):
        debug.mainthreadTest()
        x = utils.OOFeval(self.xtext.get_text())
        y = utils.OOFeval(self.ytext.get_text())
        point = primitives.Point(x,y)
        skelctxt = self.getSkeletonContext()
        subthread.execute(self.kbmove_subthread, (skelctxt, point))

    def kbmove_subthread(self, skelctxt, point):
        debug.subthreadTest()
        # In order to prohibit illegal node moves, we have to actually
        # move the node, check it, and move the node back.  If it's
        # ok, then we call the menu item, which makes the permanent
        # move.
        skelctxt.begin_writing()
        skeleton = skelctxt.getObject()
        try:
            # Compute initial energy of neighboring elements
            neighbors = self.node().neighborElements()

            homogeneity0 = 0.0
            shapeenergy0 = 0.0
            for element in neighbors:
                if element.illegal():
                    continue
                homogeneity0 += element.homogeneity(skeleton.MS, False)
                shapeenergy0 += element.energyShape()

            # Energy after node move
            self.node().moveTo(point)
            illegal = False
            homogeneity = 0.0
            shapeenergy = 0.0
            for element in neighbors:
                if element.illegal():
                    illegal = True
                    break
                else:
                    homogeneity += element.homogeneity(skeleton.MS, False)
                    shapeenergy += element.energyShape()
            self.node().moveBack()
        finally:
            skelctxt.end_writing()

        if illegal:
            if self.allow_illegal.get_active():
                mainthread.runBlock(self.move_info, (point, "---", "---", ""))
                self.toolbox.menu.MoveNode(origin=self.node().position(),
                                           destination=point)
                
            else:
                # Illegal move not allowed.  Reset the x and y text so
                # that the user can try again.
                mainthread.runBlock(
                    self.move_info,
                    (self.node().position(),
                     "---", "---", ""))
        else:
            mainthread.runBlock(self.move_info,
                                (point,
                                 "%-11.4g" % (homogeneity - homogeneity0),
                                 "%-11.4g" % (shapeenergy - shapeenergy0),
                                 ""))
            self.toolbox.menu.MoveNode(origin=self.node().position(),
                                       destination=point)

def _makeGUI(self):
    return MoveNodeToolboxGUI(self)

movenode.MoveNodeToolbox.makeGUI = _makeGUI
