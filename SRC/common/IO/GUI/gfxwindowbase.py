# -*- python -*-
# $RCSfile: gfxwindowbase.py,v $
# $Revision: 1.16 $
# $Author: langer $
# $Date: 2009/12/14 20:37:20 $

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
from ooflib.common.IO import layereditor
from ooflib.common.IO import reporter
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import subWindow


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
        self.suppressRowOpSignals()
        self.suppressSelectionSignals()
        try:
            self.layerList.clear()
            for layer in self.display:
                self.layerList.prepend([layer])
                if layer is self.selectedLayer:
                    self.layerListView.get_selection().select_path('0')
        finally:
            self.allowRowOpSignals()
            self.allowSelectionSignals()
            

    # Callbacks for the TreeView for the Layer List.
    ##################################################

    # TODO: move contour map stuff back to gfxwindow?
    
    # TreeView callback for setting the state of the "Show" button 
    def renderShowCell(self, column, cell_renderer, model, iter):
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

    def renderFreezeCell(self, column, cell_renderer, model, iter):
        debug.mainthreadTest()
        layer = model[iter][0]
        cell_renderer.set_active(layer.frozen)

    def freezeCellCB(self, cell_renderer, path):
        layer = self.layerList[path][0]
        if layer.frozen:
            self.menu.Layer.Unfreeze(n=self.layerID(layer))
        else:
            self.menu.Layer.Freeze(n=self.layerID(layer))

    def renderCMapCell(self, column, cell_renderer, model, iter):
        debug.mainthreadTest()
        layer = model[iter][0]
        if layer.contour_capable(self):
            cell_renderer.set_property('activatable', True)
            cell_renderer.set_active(layer is self.current_contourmap_method)
        else:
            cell_renderer.set_property('activatable', False)
            cell_renderer.set_property('active', False)

    def cmapcellCB(self, cell_renderer, path):
        layer = self.layerList[path][0]
        if layer is self.current_contourmap_method:
            self.menu.Layer.Hide_Contour_Map(n=self.layerID(layer))
        else:
            self.menu.Layer.Show_Contour_Map(n=self.layerID(layer))

    def renderLayerCell(self, column, cell_renderer, model, iter):
        debug.mainthreadTest()
        layer = model[iter][0]
        who = layer.who()
        if who is not None:
            txt = "%s(%s)" % (who.getClassName(), who.name())
        else:
            # who is None.  This probably can't happen, but there was
            # comment here wondering if it could, and it's harmless to
            # check for it.
            txt = "???"
        cell_renderer.set_property('text', txt)

    def renderMethodCell(self, column, cell_renderer, model, iter):
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
        if self.selectedLayer is not None:
            layereditor.menu.LayerSet.Edit(
                window=self.name, layer_number=self.layerID(self.selectedLayer))

    # TreeView callback that determines if a row is displayed as a
    # separator.
    def layerRowSepFunc(self, model, iter):
        layer = model[iter][0]
        return not (layer.listed or self.settings.listall)

    # Callbacks for the layerList's "row-inserted" and "row-deleted"
    # signals, sent when the user reorders layers by dragging them in
    # the layer list.  "row-inserted" is sent first.
    
    def listRowInsertedCB(self, model, path, iter):
        # "row-inserted" is sent before the row is built, so we can't
        # get the actual layer here, just where it's going to be.
        self.destination_path = path
        self.suppressSelectionSignals()

    def listRowDeletedCB(self, model, path):
        self.allowSelectionSignals()
        if self.destination_path is not None:
            source_row = path[0]
            dest_row = self.destination_path[0]
            if source_row > dest_row:
                # The layer has been raised.  Remember that indices in the
                # gtk ListStore run in the opposite direction from indices
                # in the Display's layer list.
                layer = model[self.destination_path][0]
                # How far has the row moved? The -1 is because the path
                # was computed *before* the row was deleted.
                delta = source_row - dest_row - 1
                if delta > 0:
                    self.menu.Layer.Raise.By(n=self.layerID(layer),
                                             howfar=delta)
            else:                           # source_row < dest_row
                # The layer has been lowered.
                # After the source row is deleted, the destination row
                # number decreases by 1.
                layer = model[(dest_row-1,)][0]
                delta = dest_row - source_row - 1
                if delta > 0:
                    self.menu.Layer.Lower.By(n=self.layerID(layer),
                                             howfar=delta)
            self.destination_path = None

    # suppressRowOpSignals and allowRowOpSignals are used to make sure
    # that the row rearrangement callbacks aren't invoked when rows
    # are manipulated from the program, instead of by the user.
    def suppressRowOpSignals(self):
        debug.mainthreadTest()
        for signal in self.rowOpSignals:
            signal.block()

    def allowRowOpSignals(self):
        debug.mainthreadTest()
        for signal in self.rowOpSignals:
            signal.unblock()

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
        self.layerList.row_changed(rowno, self.layerList.get_iter(rowno))

    def replaceLayer(self, count, oldlayer, newlayer):
        self.acquireGfxLock()
        try:
            ghostgfxwindow.GhostGfxWindow.replaceLayer(self, count,
                                                       oldlayer, newlayer)
            for row in self.layerList:
                if row[0] is oldlayer:
                    row[0] = newlayer
                    break
        finally:
            self.releaseGfxLock()


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
        if self.gtk:
            ## tell all the miniThreads to stop and go home.
            self.device.destroy()
            if config.dimension() == 2:
                self.contourmapdata.device.destroy()
            
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

    def switchToolbox(self, chooser, tbname): # toolboxchooser callback
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
                
    def newLayer_gui(self, menuitem):
        layereditor.menu.LayerSet.New(window=self.name)

    def editLayer_gui(self, menuitem):
        layereditor.menu.LayerSet.Edit(
            window=self.name, layer_number=self.layerID(self.selectedLayer))

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
        self.display.hide_layer(self.device, n) # hide layer in canvas
        self.layerListRowChanged(n)
        # Update the contourmap.
        if config.dimension() == 2:
            self.contourmap_newlayers()
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
        self.display.show_layer(self.device, n) # show layer in canvas
        self.layerListRowChanged(n)
        # Update the contourmap.
        if config.dimension() == 2:
            self.contourmap_newlayers()
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
        self.layerListView.get_selection().select_path(len(self.display)-n-1)
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
        
    # At layer-removal time, it's necessary to explicitly redraw the
    # contourmap, because the main canvas layers have not been redrawn,
    # so the usual automatic redraw has not taken place.
    def removeLayer(self, layer):
        ghostgfxwindow.GhostGfxWindow.removeLayer(self, layer)
        if config.dimension() == 2:
            self.show_contourmap_info()
    
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

    def mouseCB(self, eventtype, x, y, shift, ctrl):
        debug.mainthreadTest()
        global _during_callback
        _during_callback = 1
        if self.mouseHandler.acceptEvent(eventtype):
            if eventtype == 'up':
                self.mouseHandler.up(x,y, shift, ctrl)
            elif eventtype == 'down':
                self.mouseHandler.down(x,y, shift, ctrl)
            elif eventtype == 'move':
                self.mouseHandler.move(x,y, shift, ctrl)
        _during_callback = 0

    #############################################





