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

## TODO: There's no need anymore for a separate GfxWindowBase base
## class.  All of this can be merged into GfxWindow.  GfxWindowBase
## was useful when the 2D and 3D graphics windows shared a base class.

class GfxWindowBase(subWindow.SubWindow, ghostgfxwindow.GhostGfxWindow):
    def __init__(self, name, gfxmgr, settings=None, clone=False):
        debug.subthreadTest()
        self.gfxlock = lock.Lock()
        mainthread.runBlock(self.preinitialize, (name, gfxmgr, settings, clone))

        ghostgfxwindow.GhostGfxWindow.__init__(self, name, gfxmgr,
                                               settings=settings,
                                               clone=clone)
        self.buttonDown = False
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
            # I'm not sure exactly how, but when loading a script it's
            # possible for treeiter to be None here.
            if treeiter is not None:
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
            cell_renderer.set_property('text', repr(layer))
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
        self.contourmapdata.canvas = None
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
        self.toolboxGUIs.sort(key=lambda tb: tb.toolbox.ordering)
        self.toolboxchooser.update([tb.name() for tb in self.toolboxGUIs])

    def allowMotionEvents(self, mode):
        # mode is one of the MotionAllowed objects defined in
        # oofcanvas.oofcanvasgui
        if self.oofcanvas is not None:
            if mode is None:
                mode = oofcanvasgui.motionNever
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

    def raiseBy_gui(self, menuitem):
        if self.selectedLayer is None:
            guitop.top().message_out('No layer is selected!\n')
        else:
            if parameterwidgets.getParameters(menuitem.get_arg('howfar'),
                                              title="Raise Layer",
                                              parentwindow=self.gtk):
                menuitem.callWithDefaults(n=self.layerID(self.selectedLayer))

    def lowerBy_gui(self, menuitem):
        if self.selectedLayer is None:
            guitop.top().message_out('No layer is selected!\n')
        else:
            if parameterwidgets.getParameters(menuitem.get_arg('howfar'),
                                              title="Lower Layer",
                                              parentwindow=self.gtk):
                menuitem.callWithDefaults(n=self.layerID(self.selectedLayer))


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

    def mouseCB(self, eventtype, pos, button, shift, ctrl, data):
        x, y = pos
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
        
        # It's possible to get a spurious mouse-up without having
        # received the corresponding mouse-down.  For example, a
        # mouse-down in an unfocused window might bring focus to the
        # window without actually passing the mouse click to the
        # window.  The ensuing mouse-up won't have a mouse-down, and
        # that can cause problems.  So ignore mouse-up if there has
        # been no mouse-down.
        # ignoreUp and buttonDown must be computed outside of the
        # acceptEvent block, or else buttonDown won't be set properly
        # if the mouse handler only accepts mouse-up events.
        ignoreUp = eventtype == "up" and not self.buttonDown
        # Set buttonDown for the *next* up.
        if eventtype == 'down':
            self.buttonDown = True
        elif eventtype == 'up':
            self.buttonDown = False

        if eventtype != 'move' or self.mouseHandler.acceptEvent('move'):
            # Mouse up and down events need to be logged even if
            # they're not handled by the mouseHandler, so that the
            # mouse button state is reproduced correctly.
            self.logMouseEvent(eventtype, x, y, button, shift, ctrl)

        if self.mouseHandler.acceptEvent(eventtype):
            # Call the appropriate handler.
            if eventtype == 'up' and not ignoreUp:
                self.mouseHandler.up(x,y, button, shift, ctrl, data)
            elif eventtype == 'down':
                ## For testing OOFCanvas.clickedItems
                # items = self.oofcanvas.clickedItems((x,y))
                # debug.fmsg("clicked on", len(items), "items")
                # debug.fmsg("clicked items=", items)
                self.mouseHandler.down(x,y, button, shift, ctrl, data)
            elif eventtype == 'move':
                self.mouseHandler.move(x,y, button, shift, ctrl, data)
            elif eventtype == 'scroll':
                self.mouseHandler.scroll(x,y, button, shift, ctrl, data)
        elif eventtype == "scroll":
            # If we're here, then the current mousehandler doesn't
            # anything special for scrolling.  Don't ignore the event.
            # Do the obvious thing.
            sx = self.hScrollbar.get_adjustment().get_value()
            self.hScrollbar.get_adjustment().set_value(sx + x)
            sy = self.vScrollbar.get_adjustment().get_value()
            self.vScrollbar.get_adjustment().set_value(sy + y)
            
        _during_callback = 0

    #=--=##=--=##=--=##=--=##=--=#
    
    # GUI logging of canvas events.

    # The OOFCanvas isn't a real GtkWidget, although it contains a
    # GtkWidget, so gui logging isn't done the same way as it's done
    # for GtkWidgets.  If we try to just log the GtkLayout that lives
    # in the OOFCanvas, it's difficult to ensure that the logging
    # callback runs before the mouse handling callback.  By not using
    # most of the gtklogger mechanism, we ensure that logMouseEvent is
    # called before the mouseHandler, and there's no causality paradox
    # in the logs.

    # As a side benefit, canvas mouse events in the log file only
    # contain user coordinates, not pixel coordinates.  It's important
    # to log only the user coordinates, because the canvas size
    # depends on things outside our control (like the fonts used in
    # other widgets in the graphics window), and the conversion from
    # pixel coordinates to user coordinates depends on the canvas
    # size.  Logging only user coordinates means that the gui
    # recordings are portable to different computers.

    # The logged code for each event should just run
    # GfxWindow.mouseCB.  The "data" argument to mouseCB is what was
    # passed in to OOFCanvas::Canvas::setMouseCallback when the
    # callback was installed, in GfxWindow.newCanvas.  On replay, we
    # need to be able to reconstruct that data.  Fortunately for us,
    # it's just None.  If we ever actually use it, we'll have to do
    # something more sophisticated here.

    # HOWEVER, bypassing the OOFCanvas mouseButtonHandler method like
    # this means that rubberbands aren't installed or drawn.  Not only
    # is that part of the GUI not tested, but we need to be sure that
    # it's not used at all during replay, since it won't be
    # initialized properly.

    def simulateMouse(self, eventtype, x, y, button, shift, ctrl):
        self.mouseCB(eventtype, (x, y), button, shift, ctrl, None)

    def logMouseEvent(self, eventtype, x, y, button, shift, ctrl):
        # This replaces gtklogger.signalLogger for OOFCanvas events.
        if gtklogger.recording() and not gtklogger.replaying():
            gtklogger.writeLine(
               "findGfxWindow('%s').simulateMouse('%s', %.8g, %.8g, %d, %s, %s)"
                % (self.name, eventtype, x, y, button, shift, ctrl))

    # Same for mouse clicks on the contourmap canvas
    def simulateCMapMouse(self, eventtype, x, y, button, shift, ctrl):
        self.contourmap_mouse(eventtype, (x, y), button, shift, ctrl, None)
    def logContourMapMouseEvent(self, eventtype, x, y, button, shift, ctrl):
        if gtklogger.recording() and not gtklogger.replaying():
            gtklogger.writeLine(
                "findGfxWindow('%s').simulateCMapMouse('%s', %.8g, %.8g, %d, %s, %s)"
                % (self.name, eventtype, x, y, button, shift, ctrl))

# This makes the "findGfxWindow" function used by the logged mouse
# events available in the Python namespace in which replayed gui log
# files are executed.  It's just the gfxManager's getWindow method,
# renamed to make it a bit shorter.
gtklogger.replayDefine(gfxmanager.gfxManager.getWindow, "findGfxWindow")



