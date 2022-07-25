# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


# Base class for Selection toolboxes.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import ooferror
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import subthread
from ooflib.common import mainthread
from ooflib.common import utils
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import historian
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import toolboxGUI

import oofcanvas
from oofcanvas import oofcanvasgui

import sys
from gi.repository import Gtk
from gi.repository import Gdk

class HistoricalSelection:
    def __init__(self, selectionMethod, points):
        # Store a copy of the selection method.
        self.selectionMethod = selectionMethod
        self.points = points            # mouse coordinates
    def __repr__(self):
        return "HistoricalSelection(%s, %s)" %\
               (self.selectionMethod, self.points)


# Base class common to all selection toolboxes.  Needs access to the
# selectionmethod registry in order to build the
# registeredclassfactory.

# Subclasses *must* provide:
#  getSource()  returns the Who object within which the selection is made
#  finish_up()  completes the selection operation
#  undoCB()     gtk callback for undo button
#  redoCB()
#  clearCB()
#  invertCB()
#  methodFactory()  Returns a RegisteredClassFactory for the
#                                                 appropriate registry.

class GenericSelectToolboxGUI(toolboxGUI.GfxToolbox,
                              mousehandler.MouseHandler):
    def __init__(self, name, toolbox, method):
        debug.mainthreadTest()
        toolboxGUI.GfxToolbox.__init__(self, name, toolbox)
        self.method = method            # RegisteredClass of selection methods
        self.points = []                # locations of mouse events
        # Was a modifier key pressed during the last button event?
        self.shift = False                 
        self.ctrl = False
        self.rb = None          # rubberband

        outerbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(outerbox)

        # Retrieve the registered class factory from the subclass.
        self.selectionMethodFactory = self.methodFactory(
            shadow_type=Gtk.ShadowType.IN, margin=2)
        self.selectionMethodFactory.gtk.set_vexpand(True)
        outerbox.pack_start(self.selectionMethodFactory.gtk,
                            expand=True, fill=True, padding=0)
        self.historian = historian.Historian(self.setHistory,
                                             self.sensitizeHistory)
        self.selectionMethodFactory.set_callback(self.historian.stateChangeCB)

        # Undo, Redo, Clear, and Invert buttons.  The callbacks for
        # these have to be defined in the derived classes.
        hbox = Gtk.HBox(orientation=Gtk.Orientation.HORIZONTAL,
                        homogeneous=True, spacing=2,
                        margin_start=2, margin_end=2)
        outerbox.pack_start(hbox, expand=False, fill=False, padding=0)
        self.undobutton = gtkutils.StockButton("edit-undo-symbolic", "Undo")
        self.redobutton = gtkutils.StockButton("edit-redo-symbolic", "Redo")
        hbox.pack_start(self.undobutton, expand=True, fill=True, padding=0)
        hbox.pack_start(self.redobutton, expand=True, fill=True, padding=0)
        gtklogger.setWidgetName(self.undobutton, "Undo")
        gtklogger.setWidgetName(self.redobutton, "Redo")
        gtklogger.connect(self.undobutton, 'clicked', self.undoCB)
        gtklogger.connect(self.redobutton, 'clicked', self.redoCB)
        self.undobutton.set_tooltip_text(
            "Undo the previous selection operation.")
        self.redobutton.set_tooltip_text(
            "Redo an undone selection operation.")

        self.clearbutton = gtkutils.StockButton("edit-clear-symbolic", "Clear")
        gtklogger.setWidgetName(self.clearbutton, "Clear")
        hbox.pack_start(self.clearbutton, expand=True, fill=True, padding=0)
        gtklogger.connect(self.clearbutton, 'clicked', self.clearCB)
        self.clearbutton.set_tooltip_text("Unselect all objects.")

        self.invertbutton = Gtk.Button('Invert')
        gtklogger.setWidgetName(self.invertbutton, "Invert")
        hbox.pack_start(self.invertbutton, expand=True, fill=True, padding=0)
        gtklogger.connect(self.invertbutton, 'clicked', self.invertCB)
        self.invertbutton.set_tooltip_text(
            "Select all unselected objects, and deselect all selected objects.")

        # Selection history
        frame = Gtk.Frame(label='History', margin=2)
        frame.set_shadow_type(Gtk.ShadowType.IN)
        outerbox.pack_start(frame, expand=False, fill=False, padding=0)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                       margin=2)

        frame.add(vbox)
        
        table = Gtk.Grid(row_spacing=1, column_spacing=1)
        vbox.pack_start(table, expand=False, fill=False, padding=0)
        table.attach(Gtk.Label('down'), 0,0, 1,1)
        table.attach(Gtk.Label('up'),   0,1, 1,1)

        self.xdownentry = Gtk.Entry()
        self.ydownentry = Gtk.Entry()
        self.xupentry = Gtk.Entry()
        self.yupentry = Gtk.Entry()
        gtklogger.setWidgetName(self.xdownentry, 'xdown')
        gtklogger.setWidgetName(self.ydownentry, 'ydown')
        gtklogger.setWidgetName(self.xupentry, 'xup')
        gtklogger.setWidgetName(self.yupentry, 'yup') # yessirree, Bob!
        entries = [self.xdownentry, self.ydownentry,
                   self.xupentry, self.yupentry]
        self.entrychangedsignals = []
        for entry in entries:
            entry.set_width_chars(12)
            self.entrychangedsignals.append(
                gtklogger.connect(entry, "changed", self.poschanged))
        table.attach(self.xdownentry, 1,0, 1,1)
        table.attach(self.ydownentry, 2,0, 1,1)
        table.attach(self.xupentry, 1,1, 1,1)
        table.attach(self.yupentry, 2,1, 1,1)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        vbox.pack_start(hbox, expand=False, fill=False, padding=0)
        self.prevmethodbutton = gtkutils.prevButton()
        self.repeatbutton = gtkutils.StockButton("view-refresh-symbolic",
                                                 "Repeat")
        gtklogger.setWidgetName(self.repeatbutton, 'Repeat')
        self.nextmethodbutton = gtkutils.nextButton()
        hbox.pack_start(self.prevmethodbutton, expand=False, fill=False,
                        padding=0)
        hbox.pack_start(self.repeatbutton, expand=True, fill=False, padding=0)
        hbox.pack_start(self.nextmethodbutton, expand=False, fill=False,
                        padding=0)
        gtklogger.connect(self.repeatbutton, 'clicked', self.repeatCB)
        gtklogger.connect(self.repeatbutton, 'button-release-event',
                          self.repeateventCB)
        gtklogger.connect(self.prevmethodbutton, 'clicked',
                          self.historian.prevCB)
        gtklogger.connect(self.nextmethodbutton, 'clicked',
                         self.historian.nextCB)
        self.prevmethodbutton.set_tooltip_text(
            "Recall the settings and mouse coordinates"
            " for the previous selection method.")
        self.nextmethodbutton.set_tooltip_text(
            "Recall the settings and mouse coordinates"
            " for the next selection method.")
        self.repeatbutton.set_tooltip_text(
            "Execute the selection method as if the mouse had been clicked"
            " at the above coordinates.  Hold the shift key to retain the"
            " previous selection.  Hold the control key to toggle the"
            " selection state of the selected pixels.")
        

        # Selection information
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                       spacing=2, margin=2)
        outerbox.pack_start(hbox, expand=False, fill=False, padding=0)
        hbox.pack_start(Gtk.Label('Selection size: '),
                        expand=False, fill=False, padding=0)
        self.sizetext = Gtk.Entry()
        gtklogger.setWidgetName(self.sizetext, 'size')
        hbox.pack_start(self.sizetext, expand=True, fill=True, padding=0)
        self.sizetext.set_editable(False)
        self.sizetext.set_width_chars(12)

        # switchboard callbacks
        self.sbcallbacks = [
            switchboard.requestCallbackMain(method,
                                            self.updateSelectionMethods),
            switchboard.requestCallback((self.toolbox.gfxwindow(),
                                         'layers changed'),
                                        self.setInfo_subthread)
        ]

    def activate(self):
        toolboxGUI.GfxToolbox.activate(self)
        self.sensitize()
        self.sensitizeHistory()
        self.setInfo()
        self.gfxwindow().setMouseHandler(self)
        self.motionFlag = self.gfxwindow().allowMotionEvents(
            oofcanvasgui.MotionAllowed_MOUSEDOWN)

    def deactivate(self):
        self.gfxwindow().setRubberBand(None)
        toolboxGUI.GfxToolbox.deactivate(self)
        self.gfxwindow().allowMotionEvents(self.motionFlag)

    def close(self):
        list(map(switchboard.removeCallback, self.sbcallbacks))
        toolboxGUI.GfxToolbox.close(self)

    def getSourceName(self):
        source = self.getSource()
        if source is not None:
            return source.path()

    def layerChangeCB(self):
        # Called when layers have been added, removed, or moved in the gfxwindow
        self.sensitize()

    def newSelection(self, selectionMethod, pointlist): # switchboard callback
        debug.mainthreadTest()
        if selectionMethod is not None:
            self.historian.record(HistoricalSelection(selectionMethod,
                                                      pointlist))
            self.setCoordDisplay(selectionMethod.getRegistration(), pointlist)
            self.selectionMethodFactory.setByRegistration(
                selectionMethod.getRegistration())
            self.sensitize()

    def changedSelection(self):         # switchboard callback
        self.sensitize()
        self.setInfo()

    def poschanged(self, *args):
        self.sensitizeHistory()
            
    def setHistory(self, historicalSelection):
        self.selectionMethodFactory.set(historicalSelection.selectionMethod,
                                        interactive=1)
        self.setCoordDisplay(
            historicalSelection.selectionMethod.getRegistration(),
            historicalSelection.points)

    def sensitize(self):
        subthread.execute(self.sensitize_subthread)

    def sensitize_subthread(self):
        debug.subthreadTest()

        source = self.getSource()
        try:        # The source may not have been completely built yet...
            selection = source.getSelectionContext(**self.toolbox.extrakwargs)
        except AttributeError:
            selection = None
        if source is None or selection is None:
            (u,r,c,i) = (0,0,0,0)
        else:
            selection.begin_reading()
            try:
                u = selection.undoable()
                r = selection.redoable()
                c = selection.clearable()
                i = 1
            finally:
                selection.end_reading()
        mainthread.runBlock(self._set_button_sensitivities, (u,r,c,i))
        gtklogger.checkpoint(self.gfxwindow().name + " " +
                             self._name + " sensitized")
        
    def _set_button_sensitivities(self, u,r,c,i):
        debug.mainthreadTest()
        self.undobutton.set_sensitive(u)
        self.redobutton.set_sensitive(r)
        self.clearbutton.set_sensitive(c)
        self.invertbutton.set_sensitive(i)
        self.sensitizeHistory()

    def sensitizeHistory(self):
        debug.mainthreadTest()
        self.nextmethodbutton.set_sensitive(self.historian.nextSensitive())
        self.prevmethodbutton.set_sensitive(self.historian.prevSensitive())
        self.repeatbutton.set_sensitive(len(self.historian) > 0
                                        and self.repeatable())

    def setInfo(self):
        debug.mainthreadTest()
        subthread.execute(self.setInfo_subthread)

    def setInfo_subthread(self):
        debug.subthreadTest()
            
        source = self.getSource()
        if source is not None:
            source.begin_reading()
            try:
                selection = source.getSelectionContext(
                    **self.toolbox.extrakwargs)
                ## Selection can be None because an Image must be created
                ## before a Microstructure, but the selection source for
                ## an Image is its Microstructure.
                if selection is not None:
                    selection.begin_reading()
                    try:
                        n = selection.size()
                        m = selection.maxSize()
                        if m > 0:
                            sizetextdata = "%d (%g%%)" % (n, 100.*n/m)
                        else:
                            sizetextdata = "0"
                    finally:
                        selection.end_reading()
                else:
                    sizetextdata = '0'
            finally:
                source.end_reading()
        else:
            sizetextdata = self.toolbox.emptyMessage()

        mainthread.runBlock(self._write_text, (sizetextdata,))
        gtklogger.checkpoint("selection info updated " + self._name)
            
    def _write_text(self, txt):
        self.sizetext.set_text(txt)
        
    def updateSelectionMethods(self):
        selmeth = self.selectionMethodFactory.getRegistration().name()
        self.selectionMethodFactory.update(self.method.registry, obj=selmeth)

    ###################################

    # Command history
    
    def repeatCB(self, button):
        debug.mainthreadTest()
        selmeth = self.selectionMethodFactory.getRegistration()
        if selmeth is not None:
            # Get the coordinates of the points from the widgets.  If
            # the selection method uses 'move' events, then those
            # points have to come from the Historian, because there's
            # no widget for them.
            if 'move' in selmeth.events:
                points = self.historian.current().points[:]
            else:
                points = [None]         # dummy array, will be filled later
            # Also, the list of points from the Historian might not
            # have the right length. 
            if 'up' in selmeth.events and 'down' in selmeth.events:
                # need two points, at least
                if len(points) == 1:
                    points.append(None)
            # Get the (possibly) edited values from the widgets
            try:
                if 'down' in selmeth.events:
                    if config.dimension() == 2:
                        points[0] = primitives.Point(
                            utils.OOFeval(self.xdownentry.get_text()),
                            utils.OOFeval(self.ydownentry.get_text()))
                    elif config.dimension() == 3:
                        points[0] = primitives.Point(
                            utils.OOFeval(self.xdownentry.get_text()),
                            utils.OOFeval(self.ydownentry.get_text()),
                            utils.OOFeval(self.zdownentry.get_text()))
                if 'up' in selmeth.events:
                    if config.dimension() == 2:
                        points[-1] = primitives.Point(
                            utils.OOFeval(self.xupentry.get_text()),
                            utils.OOFeval(self.yupentry.get_text()))
                    elif config.dimension() == 3:
                        points[-1] = primitives.Point(
                            utils.OOFeval(self.xupentry.get_text()),
                            utils.OOFeval(self.yupentry.get_text()),
                            utils.OOFeval(self.zupentry.get_text()))                      
            except:        # Shouldn't happen, if sensitization is working
                raise ooferror.ErrProgrammingError(
                    "Can't evaluate coordinates!")
            actual_who = self.getSource()
            if actual_who:
                self.selectionMethodFactory.set_defaults()
                menuitem = getattr(self.toolbox.menu, selmeth.name())
                self.toolbox.setSourceParams(menuitem, actual_who)
                menuitem.callWithDefaults(points=points,
                                          shift=self.shift, ctrl=self.ctrl)

    def repeateventCB(self, button, gdkevent):
        # Callback for 'button-release-event' on the 'Repeat' button.
        # This function is called before repeatCB and stores the
        # modifier key state.  This function is called whenever the
        # mouse is released as long as it was pushed on the 'Repeat'
        # button, so it can't be used as the actual button callback.
        # repeatCB is called only if the mouse is actually released on
        # the button, but doesn't have access to the modifier keys
        # like repeateventCB does.
        self.shift = (gdkevent.state & Gdk.ModifierType.SHIFT_MASK != 0)
        self.ctrl = (gdkevent.state & Gdk.ModifierType.CONTROL_MASK != 0)

    def repeatable(self):
        # Check that the mouse coord entry widgets contain appropriate
        # data.
        debug.mainthreadTest()
        selmeth = self.selectionMethodFactory.getRegistration()
        try:
            if 'down' in selmeth.events:
                # OOFeval raises exceptions if the text is not a valid
                # Python expression
                utils.OOFeval(self.xdownentry.get_text())
                utils.OOFeval(self.ydownentry.get_text())
                if config.dimension() == 3:
                    utils.OOFeval(self.zdownentry.get_text())
            if 'up' in selmeth.events:
                utils.OOFeval(self.xupentry.get_text())
                utils.OOFeval(self.yupentry.get_text())
                if config.dimension() == 3:
                    utils.OOFeval(self.zupentry.get_text())
        except:
            return 0
        return 1

    def setCoordDisplay(self, selectionMethodReg, points):
        debug.mainthreadTest()
        for sig in self.entrychangedsignals:
            sig.block()
        try:
            if 'down' in selectionMethodReg.events:
                self.xdownentry.set_text(("%-8g" % points[0].x).rstrip())
                self.ydownentry.set_text(("%-8g" % points[0].y).rstrip())
            else:
                self.xdownentry.set_text('--')
                self.ydownentry.set_text('--')
            if 'up' in selectionMethodReg.events:
                self.xupentry.set_text(("%-8g" % points[-1].x).rstrip())
                self.yupentry.set_text(("%-8g" % points[-1].y).rstrip())
            else:
                self.xupentry.set_text('--')
                self.yupentry.set_text('--')
        finally:
            for sig in self.entrychangedsignals:
                sig.unblock()


    ###################################
        
    # MouseHandler functions
    
    def down(self, x, y, button, shift, ctrl, data):  # mouse down
        debug.mainthreadTest()
        self.selmeth = self.selectionMethodFactory.getRegistration()
        ## TODO: Illegal entries in the selectionMethodFactory can
        ## cause problems here.  Need to catch exceptions and do
        ## something sensible.
        self.selectionMethodFactory.set_defaults()

        # A reference is kept to the RubberBand so that it's not
        # destroyed too early.  It's not actually used in Python after
        # it's set up here.
        self.rb = self.selmeth.getRubberBand(self.selmeth)
        ## TODO: Make the rubberband width, etc, settable by the user
        if self.rb is not None:
            self.rb.setLineWidth(1)
            self.rb.setColor(oofcanvas.black)
            self.rb.setDashColor(oofcanvas.white)
            self.rb.setDashLength(7)
        self.gfxwindow().setRubberBand(self.rb)
        # Start collecting points
        self.points = [primitives.Point(x,y)]

    def move(self, x, y, button, shift, ctrl, data):  # mouse move
        # Continue the collection of points, if it's been started...
        if self.points:
            self.points.append(primitives.Point(x,y))

    def up(self, x, y, button, shift, ctrl, data):    # mouse up
        debug.mainthreadTest()
        self.gfxwindow().setRubberBand(None)
        self.rb = None
        # Finish the collection of points. If the mouse up position is
        # the same as the last move event position, don't duplicate it.
        pt = primitives.Point(x,y)
        if len(self.points) == 0 or self.points[-1] != pt:
            self.points.append(pt)
        if self.selmeth is not None:
            # Construct the list of points that the method needs
            ptlist = []
            if 'down' in self.selmeth.events:
                ptlist.append(self.points[0])
            if 'move' in self.selmeth.events and len(self.points) > 2:
                ptlist += self.points[1:-2]
            if 'up' in self.selmeth.events:
                ptlist.append(self.points[-1])

            source = self.getSource()

            if source:
                # We've done as much generic work as we can do --
                # we have a mouse-up event, a set of points,
                # a selection method, and a who.
                # Child classes know what to do next.
                self.finish_up(ptlist, shift, ctrl, self.selmeth)
                
            self.points = []            # get ready for next event
            
    def acceptEvent(self, eventtype):
        return eventtype in ('up', 'down', 'move')

