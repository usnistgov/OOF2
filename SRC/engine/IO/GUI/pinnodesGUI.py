# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common.IO.GUI.OOFCANVAS import oofcanvasgui
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import utils
from ooflib.common.IO import mainmenu
from ooflib.common.IO import reporter
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import toolboxGUI
from ooflib.engine.IO import pinnodes

from gi.repository import Gtk

class PinnedNodesToolboxGUI(toolboxGUI.GfxToolbox, mousehandler.MouseHandler):
    def __init__(self, pinnodestoolbox):
        debug.mainthreadTest()

        toolboxGUI.GfxToolbox.__init__(self, "Pin Nodes", pinnodestoolbox)
        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                          spacing=2, margin=2)
        self.gtk.add(mainbox)

        infoframe = Gtk.Frame()
        mainbox.pack_start(infoframe, expand=False, fill=False, padding=0)
        info = Gtk.Label("""Click a node to pin it,
Shift-click to unpin it,
And Ctrl-click to toggle.""")
        infoframe.add(info)
            
       
        self.table = Gtk.Grid(row_spacing=2, column_spacing=2,
                              vexpand=False, valign=Gtk.Align.START)
        mainbox.pack_start(self.table, expand=False, fill=False, padding=0)

        label = Gtk.Label('Mouse', hexpand=False,
                          halign=Gtk.Align.END, valign=Gtk.Align.CENTER)
        self.table.attach(label, 0,0, 1,2)

        label = Gtk.Label('x=', hexpand=False, halign=Gtk.Align.END)
        self.table.attach(label, 1,0, 1,1)
        self.xtext = Gtk.Entry(editable=False,
                               hexpand=True, halign=Gtk.Align.FILL)
        gtklogger.setWidgetName(self.xtext,"Mouse X")
        self.xtext.set_width_chars(12)
        self.table.attach(self.xtext, 2,0, 1,1)
        self.xtext.set_tooltip_text("x position of the mouse")

        label = Gtk.Label('y=', hexpand=False, halign=Gtk.Align.END)
        self.table.attach(label, 1,1, 1,1)
        self.ytext = Gtk.Entry(editable=False,
                               hexpand=True, halign=Gtk.Align.FILL)
        gtklogger.setWidgetName(self.ytext,"Mouse Y")
        self.ytext.set_width_chars(12)
        self.table.attach(self.ytext, 2,1, 1,1)
        self.ytext.set_tooltip_text("y position of the mouse")

        self.table.attach(
            Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL,
                          vexpand=False, valign=Gtk.Align.CENTER),
                    0,2, 3,1)

        label = Gtk.Label("Node", hexpand=False,
                          halign=Gtk.Align.END, valign=Gtk.Align.CENTER)
        self.table.attach(label, 0,3, 1,2)

        label = Gtk.Label('x=', hexpand=False, halign=Gtk.Align.END)
        self.table.attach(label, 1,3, 1,1)
        self.nodextext = Gtk.Entry(editable=False,
                                   hexpand=True, halign=Gtk.Align.FILL)
        gtklogger.setWidgetName(self.nodextext,"Node X")
        self.nodextext.set_width_chars(12)
        self.table.attach(self.nodextext, 2,3, 1,1)

        label = Gtk.Label('y=', hexpand=False, halign=Gtk.Align.END)
        self.table.attach(label, 1,4, 1,1)
        self.nodeytext = Gtk.Entry(editable=False,
                                   hexpand=True, halign=Gtk.Align.FILL)
        gtklogger.setWidgetName(self.nodeytext,"Node Y")
        self.nodeytext.set_width_chars(12)
        self.table.attach(self.nodeytext, 2,4, 1,1)

        # pintext displays either "pinned" or "unpinned" depending on
        # the state of the node under the mouse cursor.
        self.pintext = Gtk.Label(hexpand=False, halign=Gtk.Align.START,
                                 vexpand=False, valign=Gtk.Align.START)
        gtklogger.setWidgetName(self.pintext,"Pin Label")
        self.table.attach(self.pintext, 2,5, 1,1)

        self.status = Gtk.Label(hexpand=True, vexpand=True,
                                halign=Gtk.Align.START,
                                valign=Gtk.Align.END)
        gtklogger.setWidgetName(self.status,"Status")
        mainbox.pack_start(self.status, expand=True, fill=True, padding=0)
        
        # 2x2 box of buttons
        modbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        mainbox.pack_end(modbox, expand=False, fill=False, padding=0)

        bbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                        homogeneous=True, spacing=2)
        modbox.pack_end(bbox1, expand=False, fill=False, padding=0)

        self.undobutton = gtkutils.StockButton("edit-undo-symbolic", "Undo")
        gtklogger.setWidgetName(self.undobutton, 'Undo')
        gtklogger.connect(self.undobutton, "clicked", self.undoCB)
        self.undobutton.set_tooltip_text("Undo the latest action.")
        bbox1.pack_start(self.undobutton, expand=True, fill=True, padding=0)

        self.redobutton = gtkutils.StockButton("edit-redo-symbolic", "Redo")
        gtklogger.setWidgetName(self.redobutton, 'Redo')
        gtklogger.connect(self.redobutton, "clicked", self.redoCB)
        self.redobutton.set_tooltip_text("Redo the latest undone action.")
        bbox1.pack_start(self.redobutton, expand=True, fill=True, padding=0)

        bbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                        homogeneous=True, spacing=2)
        modbox.pack_end(bbox2, expand=False, fill=False, padding=0)

        self.unpinallbutton = Gtk.Button("Unpin All")
        gtklogger.setWidgetName(self.unpinallbutton, 'UnPinAll')
        gtklogger.connect(self.unpinallbutton, "clicked", self.unpinallCB)
        self.unpinallbutton.set_tooltip_text("Unpin all the pinned nodes.")
        bbox2.pack_start(self.unpinallbutton, expand=True, fill=True, padding=0)

        self.invertbutton = Gtk.Button("Invert")
        gtklogger.setWidgetName(self.invertbutton, 'Invert')
        gtklogger.connect(self.invertbutton, "clicked", self.invertCB)
        self.invertbutton.set_tooltip_text(
            "Invert - pin the unpinned and unpin the pinned.")
        bbox2.pack_start(self.invertbutton, expand=True, fill=True, padding=0)

        # self.skeleton_context is set by self.update().
        self.skeleton_context = None

        self.current_node = None

    def update(self, *args):
        debug.mainthreadTest()
        ctxt = self.gfxwindow().topwho('Skeleton')
        if ctxt:
            n = len(ctxt.pinnednodes.retrieve())
        else:
            n = 0
        self.status.set_text("%d node%s pinned." % (n, 's'*(n!=1)))

        self.unpinallbutton.set_sensitive(ctxt is not None and n > 0)
        self.undobutton.set_sensitive(ctxt is not None and
                                      ctxt.pinnednodes.undoable())
        self.redobutton.set_sensitive(ctxt is not None and
                                      ctxt.pinnednodes.redoable())
        self.invertbutton.set_sensitive(ctxt is not None)

        self.skeleton_context = ctxt

        if self.current_node:
            self.set_pintext(self.current_node)
            self.current_node = None
            
        gtklogger.checkpoint(self.gfxwindow().name + " " +
                             self._name + " updated")

    # Switchboard, "new pinned nodes".
    def newPinState(self, *args):
        self.update()
        switchboard.notify("redraw")


    def activate(self):
        toolboxGUI.GfxToolbox.activate(self)
        self.gfxwindow().setMouseHandler(self)
        self.oldMotionFlag = self.gfxwindow().allowMotionEvents(
            oofcanvasgui.MOTION_ALWAYS)
        self.sbcallbacks = [
            switchboard.requestCallbackMain(('who changed', 'Skeleton'),
                                            self.skelChanged),
            switchboard.requestCallbackMain((self.gfxwindow(),
                                             'layers changed'),
                                            self.update),
            switchboard.requestCallbackMain("new pinned nodes",
                                            self.newPinState)
            ]
        self.update()

    # Called when a skeleton has changed.
    def skelChanged(self, skelcontext):
        if skelcontext is self.skeleton_context:
            self.update()

    def deactivate(self):
        toolboxGUI.GfxToolbox.deactivate(self)
        self.gfxwindow().removeMouseHandler()
        self.gfxwindow().allowMotionEvents(self.oldMotionFlag)
        map(switchboard.removeCallback, self.sbcallbacks)

    def showPosition(self, point):
        debug.mainthreadTest()
        self.xtext.set_text("%-11.4g" % point[0])
        self.ytext.set_text("%-11.4g" % point[1])

    def acceptEvent(self, eventtype):
        return eventtype in ('move', 'up')

    def set_pintext(self, node):
        if node:
            if node.pinned():
                self.pintext.set_text('pinned')
            else:
                self.pintext.set_text('unpinned')
        else:
            self.pintext.set_text('')

    def up(self, x, y, button, shift, ctrl, data):
        debug.mainthreadTest()
        thepoint = self.getPoint(x,y)
        self.showPosition(thepoint)
        # Perhaps shift and ctrl should be handled by the menu
        # commands, as they are in pixel selection.
        if self.skeleton_context:

            # We need to establish that there is a current node being
            # operated on before we call the menu item -- the menu
            # item may change that nodes selection state, and if so,
            # the selection-state text will be updated in "update" in
            # response to the "new pinned nodes" switchboard callback.
            # The reason for not just doing that call here is that it
            # gives rise to a race condition -- the menu item is
            # threaded, and so is the switchboard callback, this
            # routine can complete before the node's state has been
            # changed.
            
            skel = self.skeleton_context.getObject()
            if thepoint is not None:
                node = skel.nearestNode(thepoint)
                self.current_node = node
                
                # TODO OPT: Can we pass "node" in to the menu item,
                # instead of forcing it to re-run the nearestNode
                # routine?
                
                path = self.skeleton_context.path()
                if shift:
                    self.toolbox.menu.UnPin(
                        skeleton=path, point = thepoint)
                elif ctrl:
                    self.toolbox.menu.TogglePin(
                        skeleton=path, point = thepoint)
                else:
                    self.toolbox.menu.Pin(
                        skeleton=path, point = thepoint)

    def move(self, x, y, button, shift, ctrl, data):
        debug.mainthreadTest()
        self.xtext.set_text("%-11.4g" % x)
        self.ytext.set_text("%-11.4g" % y)
        point = primitives.Point(x,y)
        if self.skeleton_context and point is not None:
            skel = self.skeleton_context.getObject()
            node = skel.nearestNode(point)
            if node:
                pos = node.position()
                self.nodextext.set_text("%-11.4g" % pos.x)
                self.nodeytext.set_text("%-11.4g" % pos.y)
                self.set_pintext(node)
        else:
            self.nodextext.set_text('')
            self.nodeytext.set_text('')
            self.set_pintext(None)
        gtklogger.checkpoint("Pin Nodes toolbox move event")

    # The buttons for which these are callbacks are not sensitized if
    # self.skeleton_context is None.
    def invertCB(self, button):
        self.toolbox.menu.Invert(skeleton=self.skeleton_context.path())
    
    def undoCB(self, button):
        self.toolbox.menu.Undo(skeleton=self.skeleton_context.path())

    def unpinallCB(self, button):
        self.toolbox.menu.UnPinAll(skeleton=self.skeleton_context.path())

    def redoCB(self, button):
        self.toolbox.menu.Redo(skeleton=self.skeleton_context.path())

def _makeGUI(self):
    return PinnedNodesToolboxGUI(self)

pinnodes.PinnedNodesToolbox.makeGUI = _makeGUI
