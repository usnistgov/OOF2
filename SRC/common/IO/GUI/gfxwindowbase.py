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
from ooflib.common.IO import ghostgfxwindow
from ooflib.common.IO import reporter
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import subWindow

## TODO: There's no need anymore for a separate GfxWindowBase base
## class.  All of this can be merged into GfxWindow.  GfxWindowBase
## was useful when the 2D and 3D graphics windows shared a base class.

class GfxWindowBase(subWindow.SubWindow, ghostgfxwindow.GhostGfxWindow):
    def __init__(self, name, gfxmgr, clone=0):
        debug.subthreadTest()
        self.gfxlock = lock.Lock()
        mainthread.runBlock(self.preinitialize, (name, gfxmgr, clone))
        self.newCanvas()
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

    def newLayerMembers(self):
        self.fillLayerList()
        self.updateTimeControls()
        ghostgfxwindow.GhostGfxWindow.newLayerMembers(self)

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
        
    # Call layerListRowChanged to notify the TreeView that the data it
    # displays has changed.
    def layerListRowChanged(self, n):
        rowno = len(self.layerList) - 1 - n
        mainthread.runBlock(
            self.layerList.row_changed, (rowno, self.layerList.get_iter(rowno)))

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
            if config.dimension() == 2:
                self.removeMouseHandler()
            if self.current_toolbox:
                self.current_toolbox.deactivate()
            self.current_toolbox = self.getToolboxGUIByName(tbname)
            self.current_toolbox.activate()
            self.toolboxbody.foreach(self.toolboxbody.remove)
            self.toolboxbody.add(self.current_toolbox.gtk)
            self.toolboxbody.show_all()

    def getToolboxGUIByName(self, name):
        for tbgui in self.toolboxGUIs:
            if tbgui.name() == name:
                return tbgui

    def makeToolboxGUI(self, tb):
        tbgui = mainthread.runBlock(tb.makeGUI)
        if tbgui:
            self.toolboxGUIs.append(tbgui)
            self.toolboxGUIs.sort()
            self.updateToolboxChooser()
               
    def updateToolboxChooser(self):
        self.toolboxGUIs.sort()
        self.toolboxchooser.update([tb.name() for tb in self.toolboxGUIs])


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

    # This is an override of the command-line menu callback in
    # ghostgfxwindow.  It exists in addition to the GUI callback
    # below, which is also required because it operates on the
    # current layer.
    def hideLayer(self, menuitem, n):   # OOFMenu callback
        ghostgfxwindow.GhostGfxWindow.hideLayer(self, menuitem, n)
        mainthread.runBlock(self.hideLayer_thread, (menuitem, n))

    def hideLayer_thread(self, menuitem, n):
        self.layers[n].hide()   # hide layer in canvas
        self.layerListRowChanged(n)
        ## TODO GTK3: Do hideLayer_thread and showLayer_thread need to
        ## call show_contourmap_info?  Shouldn't they call draw(),
        ## which calls show_contourmap_info?
        
        # Update the contourmap.
        # self.contourmap_newlayers() # called by GhostGfxWindow.hideLayer
        subthread.execute(self.show_contourmap_info)
        
    def hideLayer_gui(self, menuitem):  # OOFMenu GUI callback.
        if self.selectedLayer is None:
            reporter.report('No layer is selected!')
        else:
            self.menu.Layer.Hide(n=self.layerID(self.selectedLayer))

        
    def showLayer(self, menuitem, n):   # OOFMenu callback.
        ghostgfxwindow.GhostGfxWindow.showLayer(self, menuitem, n)
        mainthread.runBlock(self.showLayer_thread, (menuitem, n))

    def showLayer_thread(self, menuitem, n):
        self.layers[n].show()   # show layer in canvas
        self.layerListRowChanged(n)
        # Update the contourmap.
        # self.contourmap_newlayers() # called by GhostGfxWindow.hideLayer
        subthread.execute(self.show_contourmap_info)

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

    def setMouseHandler(self, handler):
        self.mouseHandler = handler

    def removeMouseHandler(self):
        self.mouseHandler = mousehandler.nullHandler

    def mouseCB(self, eventtype, x, y, button, shift, ctrl, data):
        debug.mainthreadTest()
        global _during_callback
        _during_callback = 1
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
            ## TODO: This should be logged, but we don't want to log
            ## every event (there are a lot of them).  How do we know
            ## when we're done scrolling?  Catch another type of mouse
            ## event (including leave_notify)?
            sx = self.hScrollbar.get_adjustment().get_value()
            self.hScrollbar.get_adjustment().set_value(sx + x)
            sy = self.vScrollbar.get_adjustment().get_value()
            self.vScrollbar.get_adjustment().set_value(sy + y)
            
        _during_callback = 0

    #############################################





