# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import lock
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import subthread
from ooflib.common.IO import gfxmanager
from ooflib.common.IO import ghostgfxwindow
from ooflib.common.IO import reporter
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import subWindow

from gi.repository import Gdk

## TODO: There's no need anymore for a separate GfxWindowBase base
## class.  All of this can be merged into GfxWindow.  GfxWindowBase
## was useful when the 2D and 3D graphics windows shared a base class.

class GfxWindowBase(subWindow.SubWindow, ghostgfxwindow.GhostGfxWindow):
    def __init__(self, name, gfxmgr, clone=0):
        debug.subthreadTest()
        self.gfxlock = lock.Lock()
        mainthread.runBlock(self.preinitialize, (name, gfxmgr, clone))

        ghostgfxwindow.GhostGfxWindow.__init__(self, name, gfxmgr,
                                               clone=clone)
        mainthread.runBlock(self.postinitialize, (name, gfxmgr, clone))
        # This whole initialization sequence is complicated.  The
        # reason is that the order of operations is important -- the
        # ghostgfxwindow makes function calls which need to be
        # redefined in the GUI before they occur -- and there is a
        # requirement that the main thread never be locked.
        # Furthermore, the ghostgfxwindow has to create the menu
        # before the SubWindow init gets called.  It could probably be
        # rationalized, but it's not urgent.


    # Functions which, as of now, are specific for 2D vs. 3D
    ################################################

    def preinitialize(self, name, gfxmgr, clone):
        pass

    def postinitialize(self, name, gfxmgr, clone):
        pass

    def newCanvas(self):
        pass

    def newCanvasThread(self):
        pass
    
    ################################################

    def get_oofcanvas(self):
        return self.oofcanvas


    # Zoom Fill Window
    ################################################

    def zoomFillWindow(self, *args, **kwargs):
        # This has args because it's used as a menuitem callback.  The
        # 'lock' argument is not a menu argument, though.  It's only
        # used when zoomFillWindow is called explicitly from within
        # another drawing routine, to indicate that the gfxLock has
        # already been acquired.
        lock = kwargs.get('lock', True) # default is to acquire the lock
        if lock:
            self.acquireGfxLock()
        try:
            mainthread.runBlock(self.zoomFillWindow_thread)
        finally:
            if lock:
                self.releaseGfxLock()    


    # Functions that manipulate the LayerList
    ################################################

    def layersHaveChanged(self):
        self.fillLayerList()
        self.updateTimeControls()
        ghostgfxwindow.GhostGfxWindow.layersHaveChanged(self)

    ## Only call fillLayerList if the whole list needs to be rebuilt.
    def fillLayerList(self):
        mainthread.runBlock(self.fillLayerList_thread)

    def fillLayerList_thread(self):
        debug.mainthreadTest()
        # self.suppressRowOpSignals()
        self.suppressSelectionSignals()
        try:
            self.layerList.clear()
            for layer in self.layers:
                self.layerList.prepend([layer])
                if layer is self.selectedLayer:
                    self.layerListView.get_selection().select_path('0')
        finally:
            # self.allowRowOpSignals()
            self.allowSelectionSignals()

        ## Scroll to selected line.
        if self.selectedLayer is not None:
            selection = self.layerListView.get_selection()
            model, treeiter = selection.get_selected()
            path = model.get_path(treeiter)
            self.layerListView.scroll_to_cell(path)

    # Callbacks for the TreeView for the Layer List.
    ##################################################

    # TODO: move contour map stuff back to gfxwindow?
    
    # TreeView callback for setting the state of the "Show" button 
    def renderShowCell(self, column, cell_renderer, model, iter, data):
        debug.mainthreadTest()
        layer = model[iter][0]
        cell_renderer.set_active(not layer.hidden)
        ## cell_renderer.set_property('active', not layer.hidden)        

    def showcellCB(self, cell_renderer, path):
        layer = self.layerList[path][0]
        if layer.hidden:
            self.menu.Layer.Show(n=self.layerID(layer))
        else:
            self.menu.Layer.Hide(n=self.layerID(layer))

    def renderFreezeCell(self, column, cell_renderer, model, iter, data):
        debug.mainthreadTest()
        layer = model[iter][0]
        cell_renderer.set_active(layer.frozen)

    def freezeCellCB(self, cell_renderer, path):
        layer = self.layerList[path][0]
        if layer.frozen:
            self.menu.Layer.Unfreeze(n=self.layerID(layer))
        else:
            self.menu.Layer.Freeze(n=self.layerID(layer))

    def renderLayerCell(self, column, cell_renderer, model, iter, data):
        debug.mainthreadTest()
        layer = model[iter][0]
        if layer.who is not None:
            txt = "%s(%s)" % (layer.who.getClassName(), layer.who.name())
        else:
            # who is None.  This probably can't happen, but there was
            # comment here wondering if it could, and it's harmless to
            # check for it.
            txt = "???"
        cell_renderer.set_property('text', txt)

    def renderMethodCell(self, column, cell_renderer, model, iter, data):
        debug.mainthreadTest()
        layer = model[iter][0]
        if self.settings.longlayernames:
            cell_renderer.set_property('text', `layer`)
        else:
            cell_renderer.set_property('text', layer.short_name())
                                   
    def selectionChangedCB(self, selection): # self.layerListView callback
        debug.mainthreadTest()
        model, iter = selection.get_selected()
        self.suppressSelectionSignals()
        try:
            if iter is not None:
                layer = model[iter][0]
                self.menu.Layer.Select(n=self.layerID(layer))
            else:
                self.menu.Layer.Deselect(n=self.layerID(self.selectedLayer))
        finally:
            self.allowSelectionSignals()

    def layerDoubleClickCB(self, treeview, path, col):
        # If the user has double-clicked on an unselected layer,
        # selectionChangedCB will be called before layerDoubleClickCB.
        # It's necessary for selectionChangedCB to finish before
        # editLayer_gui is called, or else editLayer_gui may load the
        # wrong layer into the editing window.  Rather than performing
        # some complicated subthread locking dance here, the
        # Layer.Select menu callback has been made UNTHREADABLE so
        # that it will finish on the main thread before this method
        # runs.
        self.editLayer_gui(self.menu.Layer.Edit)

    # TreeView callback that determines if a row is displayed as a
    # separator.
    def layerRowSepFunc(self, model, iter):
        layer = model[iter][0]
        return not (layer.listed or self.settings.listall)

    ## TODO: Reordering by drag and drop is disabled because I can't
    ## figure out how it's supposed to work.  It didn't work properly
    ## in gtk+2 either.
    # # Callbacks for the layerList's "row-inserted" and "row-deleted"
    # # signals, sent when the user reorders layers by dragging them in
    # # the layer list.  "row-inserted" is sent first.
    
    # def listRowInsertedCB(self, model, path, iter):
    #     # "row-inserted" is sent before the row is built, so we can't
    #     # get the actual layer here, just where it's going to be.
    #     self.destination_path = path
    #     self.suppressSelectionSignals()

    # def listRowDeletedCB(self, model, path):
    #     self.allowSelectionSignals()
    #     if self.destination_path is not None:
    #         source_row = path[0]
    #         dest_row = self.destination_path[0]
    #         if source_row > dest_row:
    #             # The layer has been raised.  Remember that indices in the
    #             # gtk ListStore run in the opposite direction from indices
    #             # in the Display's layer list.
    #             layer = model[self.destination_path][0]
    #             # How far has the row moved? The -1 is because the path
    #             # was computed *before* the row was deleted.
    #             delta = source_row - dest_row - 1
    #             if delta > 0:
    #                 self.menu.Layer.Raise.By(n=self.layerID(layer),
    #                                          howfar=delta)
    #         else:                           # source_row < dest_row
    #             # The layer has been lowered.
    #             # After the source row is deleted, the destination row
    #             # number decreases by 1.
    #             layer = model[(dest_row-1,)][0]
    #             delta = dest_row - source_row - 1
    #             if delta > 0:
    #                 self.menu.Layer.Lower.By(n=self.layerID(layer),
    #                                          howfar=delta)
    #         self.destination_path = None

    # # suppressRowOpSignals and allowRowOpSignals are used to make sure
    # # that the row rearrangement callbacks aren't invoked when rows
    # # are manipulated from the program, instead of by the user.
    # def suppressRowOpSignals(self):
    #     debug.mainthreadTest()
    #     for signal in self.rowOpSignals:
    #         signal.block()

    # def allowRowOpSignals(self):
    #     debug.mainthreadTest()
    #     for signal in self.rowOpSignals:
    #         signal.unblock()

    def suppressSelectionSignals(self):
        debug.mainthreadTest()
        self.selsignal.block()

    def allowSelectionSignals(self):
        debug.mainthreadTest()
        self.selsignal.unblock()
        
    # General callbacks
    #######################################################

    # gtk callback 
    def realizeCB(self, *args):         
        if not self.realized:
            self.realized = 1
            # Asynchronously zoom.
            if not self.zoomed:
                subthread.execute(self.zoomFillWindow)
        return False

    # OOFMenu callback
    def close(self, *args): 
        # The subwindow menu-removal can't depend on the existence of
        # .gtk, and it's done in the non-GUI parent, so call it
        # if this is the first time through.
        if not self.closed:
            ghostgfxwindow.GhostGfxWindow.close(self, *args)
            self.closed = 1
        if self.gtk:
            mainthread.runBlock(self.gtk.destroy) # calls destroyCB via gtk

    # gtk callback
    def destroyCB(self, *args):
        # See comment in GhostGfxWindow.close about the order of operations.
        self.oofcanvas = None # break ref. loops so that canvas is destroyed
        if self.gtk:
            for tbgui in self.toolboxGUIs:
                if tbgui.active:
                    tbgui.deactivate()
                tbgui.close()
            del self.toolboxGUIs
            del self.mouseHandler
            if self.menu:
                self.menu.gui_callback=None
            self.gtk = None             # make sure this isn't repeated
            if self.menu:
                self.menu.File.Close()    # calls self.close()

    # Toolbox callbacks
    ##################################################

    def switchToolbox(self, tbname): # toolboxchooser callback
        self.selectToolbox(tbname)

    def selectToolbox(self, tbname):
        debug.mainthreadTest()
        if not (self.current_toolbox and (self.current_toolbox.name()==tbname)):
            self.removeMouseHandler()
            if self.current_toolbox:
                self.current_toolbox.deactivate()
            self.current_toolbox = self.getToolboxGUIByName(tbname)
            self.current_toolbox.activate()
            self.toolboxstack.set_visible_child_name(tbname)

    def getToolboxGUIByName(self, name):
        for tbgui in self.toolboxGUIs:
            if tbgui.name() == name:
                return tbgui

    def makeToolboxGUI(self, tb):
        tbgui = mainthread.runBlock(tb.makeGUI)
        if tbgui:
            tbgui.gtk.show_all()
            self.toolboxGUIs.append(tbgui)
            self.toolboxstack.add_named(tbgui.gtk, tbgui.name())
            self.updateToolboxChooser()
               
    def updateToolboxChooser(self):
        self.toolboxGUIs.sort()
        self.toolboxchooser.update([tb.name() for tb in self.toolboxGUIs])

    def allowMotionEvents(self, mode):
        # mode is one of the MotionAllowed objects defined in
        # OOFCANVAS/oofcanvasgui.swg.
        if self.oofcanvas is not None:
            if mode is None:
                mode = oofcanvasgui.MOTION_NEVER
            return self.oofcanvas.allowMotionEvents(mode)

    # Layer callbacks
    ######################################################
                
    def editLayer_gui(self, menuitem):
        if self.selectedLayer is not None:
            category = menuitem.get_arg("category")
            what = menuitem.get_arg("what")
            how = menuitem.get_arg("how")
            category.value = self.selectedLayer.who.getClassName()
            what.value = self.selectedLayer.who.path()
            how.value = self.selectedLayer
            if parameterwidgets.getParameters(category, what, how,
                                              parentwindow=self.gtk,
                                              title="Edit Graphics Layer"):
                menuitem.callWithDefaults(n=self.layerID(self.selectedLayer))

    def newLayer(self, displaylayer):
        self.updateTimeControls()
        self.fillLayerList()
        
    def deleteLayer_gui(self, menuitem):
        if self.selectedLayer is None:
            guitop.top().message_out('No layer is selected!\n')
        else:
            self.suppressSelectionSignals()
            try:
                self.menu.Layer.Delete(n=self.layerID(self.selectedLayer))
            finally:
                self.allowSelectionSignals()

    def freezeLayer_gui(self, menuitem):
        if self.selectedLayer is not None:
            self.menu.Layer.Freeze(n=self.layerID(self.selectedLayer))

    def unfreezeLayer_gui(self, menuitem):
        if self.selectedLayer is not None:
            self.menu.Layer.Unfreeze(n=self.layerID(self.selectedLayer))

    def hideLayer_gui(self, menuitem):  # OOFMenu GUI callback.
        if self.selectedLayer is None:
            reporter.report('No layer is selected!')
        else:
            self.menu.Layer.Hide(n=self.layerID(self.selectedLayer))

        
    def showLayer_gui(self, menuitem):  # OOFMenu GUI callback
        if self.selectedLayer is None:\
            reporter.report('No layer is selected!')
        else:
            self.menu.Layer.Show(n=self.layerID(self.selectedLayer))

    def selectLayer(self, n):
        if self.selectedLayer is not None:
            self.deselectLayer(self.selectedLayer)
        ghostgfxwindow.GhostGfxWindow.selectLayer(self, n)
        mainthread.runBlock(self.selectLayer_thread, (n,))

    def selectLayer_thread(self, n):
        self.suppressSelectionSignals()
        self.layerListView.get_selection().select_path(self.nLayers()-n-1)
        self.allowSelectionSignals()

    def deselectLayer(self, n):
        if self.selectedLayer is not None:
            mainthread.runBlock(self.deselectLayer_thread, (n,))
            ghostgfxwindow.GhostGfxWindow.deselectLayer(self, n)

    def deselectLayer_thread(self, n):
        self.suppressSelectionSignals()
        self.layerListView.get_selection().unselect_all()
        self.allowSelectionSignals()

    def deselectAll(self):
        # called by createDefaultLayers and sb 'deselect all gfxlayers'
        if self.selectedLayer is not None:
            mainthread.runBlock(self.deselectAll_thread)

    def deselectAll_thread(self):
        self.suppressSelectionSignals()
        self.layerListView.get_selection().unselect_all()
        ghostgfxwindow.GhostGfxWindow.deselectAll(self)
        self.allowSelectionSignals()
        
    def raiseLayer_gui(self, menuitem):
        if self.selectedLayer is None:
            guitop.top().message_out('No layer is selected!\n')
        else:
            self.menu.Layer.Raise.One_Level(
                n=self.layerID(self.selectedLayer))

    def raiseToTop_gui(self, menuitem):
        if self.selectedLayer is None:
            guitop.top().message_out('No layer is selected!\n')
        else:
            self.menu.Layer.Raise.To_Top(
                n=self.layerID(self.selectedLayer))

    def lowerLayer_gui(self, menuitem):
        if self.selectedLayer is None:
            guitop.top().message_out('No layer is selected!\n')
        else:
            self.menu.Layer.Lower.One_Level(
                n=self.layerID(self.selectedLayer))

    def lowerToBottom_gui(self, menuitem):
        if self.selectedLayer is None:
            guitop.top().message_out('No layer is selected!\n')
        else:
            self.menu.Layer.Lower.To_Bottom(
                n=self.layerID(self.selectedLayer))

    def raiseLayerByGUI(self, layer):
        self.menu.Layer.Raise.One_Level(n=self.layerID(layer))

    def lowerLayerByGUI(self, layer):
        self.menu.Layer.Lower.One_Level(n=self.layerID(layer))


    #### Mouse clicks ############

    ## TODO: It would be nice if dragging the mouse from inside the
    ## canvas to outside the canvas made the canvas scroll in the
    ## opposite direction.  Then users could extend a selection past
    ## the part of the canvas that was visible during the mouse-down
    ## event, for example.  Doing this might be tricky.  We'd need to
    ## catch the leave notify event, install a timeout event that
    ## would scroll the canvas (at a rate and direction determined by
    ## the mouse position), and remove the timeout event when the
    ## mouse re-entered the canvas or the button was released.  At
    ## each timeout, we'd scroll the canvas and simulate move events
    ## for the toolbox's mouse handler.  When the event is finished,
    ## we'd want to log the net effect of the scrolling.

    def setMouseHandler(self, handler):
        self.mouseHandler = handler

    def removeMouseHandler(self):
        self.mouseHandler = mousehandler.nullHandler

    def mouseCB(self, eventtype, x, y, button, shift, ctrl, data):
        # "data" is an object that was passed in to
        # Canvas::setMouseCallback() when this method was installed as
        # the callback, in GfxWindow.newCanvas.
        debug.mainthreadTest()
        global _during_callback
        _during_callback = 1

        # Convert from 0,1, to False,True. If log files have a mix of
        # different boolean formats, test scripts that compare log
        # files can fail for trivial reasons.
        shift = bool(shift)
        ctrl = bool(ctrl)
        
        if self.mouseHandler.acceptEvent(eventtype):
            if eventtype == 'up':
                self.mouseHandler.up(x,y, button, shift, ctrl, data)
            elif eventtype == 'down':
                self.mouseHandler.down(x,y, button, shift, ctrl, data)
            elif eventtype == 'move':
                self.mouseHandler.move(x,y, button, shift, ctrl, data)
            elif eventtype == 'scroll':
                self.mouseHandler.scroll(x,y, button, shift, ctrl, data)
        # If the current mousehandler doesn't anything special for
        # scrolling, do the obvious.
        elif eventtype == "scroll":
            sx = self.hScrollbar.get_adjustment().get_value()
            self.hScrollbar.get_adjustment().set_value(sx + x)
            sy = self.vScrollbar.get_adjustment().get_value()
            self.vScrollbar.get_adjustment().set_value(sy + y)
            
        _during_callback = 0

    #=--=##=--=##=--=##=--=##=--=#
    
    # GUI logging of canvas events.

    # We can't just log events in pixel coordinates on the GtkLayout
    # that's within the OOFCanvas, because the canvas size can change
    # and therefore the conversion from pixel to user coordinates
    # isn't reproducible.  We have to log the events in user
    # coordinate, which means that the graphics window is
    # responsible. (The OOFCanvas can't do the logging because we
    # don't want to mix the OOFCanvas and gtklogger code, since both
    # could be distributed independently of other.)

    # The logged code for each event should just run
    # GfxWindow.mouseCB.  The "data" argument to mouseCB is what was
    # passed in to OOFCanvas::Canvas::setMouseCallback when the
    # callback was installed, in GfxWindow.newCanvas.  On replay, we
    # need to be able to reconstruct that data.  Fortunately for us,
    # it's just None.  If we ever actually use it, we'll have to do
    # something more sophisticated here.

    def simulateMouse(self, eventtype, x, y, button, shift, ctrl):
        self.mouseCB(eventtype, x, y, button, shift, ctrl, None)

    def logMouse(self, etype, x, y, button, state):
        #debug.fmsg("x=", x, "y=", y, "button=", button, "state=", state)
        # "etype" is "up", "down", or "move"
        # x and y are pixel coordinates of the event
        # button is which mouse button was used
        # state is a GdkModifierType containing control, shift, etc.
        ux, uy = self.oofcanvas.pixel2user(x, y)
        shift = bool(state & Gdk.ModifierType.SHIFT_MASK != 0)
        ctrl = bool(state & Gdk.ModifierType.CONTROL_MASK != 0)
        return [
            "findGfxWindow('%s').simulateMouse('%s', %.8g, %.8g, %d, %s, %s)"
            % (self.name, etype, ux, uy, button, shift, ctrl)
        ]

# This makes the "findGfxWindow" function used by the logged mouse
# events available in the Python namespace in which replayed gui log
# files are executed.  It's just the gfxManager's getWindow method,
# renamed to make it a bit shorter.
gtklogger.replayDefine(gfxmanager.gfxManager.getWindow, "findGfxWindow")



