# -*- python -*-
# $RCSfile: meshinfoGUI.py,v $
# $Revision: 1.120 $
# $Author: langer $
# $Date: 2011/07/05 19:33:59 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


from ooflib.SWIG.common import config
from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.engine import field
from ooflib.SWIG.engine import planarity
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import subthread
from ooflib.common import primitives
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import toolboxGUI
from ooflib.common.IO.GUI import tooltips
from ooflib.engine import subproblemcontext
from ooflib.engine.IO import meshinfo
from ooflib.engine.IO.GUI import meshdataGUI
import ooflib.engine.mesh

import gtk

xpadding = 3

## TODO: Add a SegmentMode that will display interface materials.

## TODO LATER: Can SkeletonToolboxGUI and MeshToolboxGUI share a base
## class?

class MeshInfoMode:
    # Base class for ElementMode, NodeMode.

    def __init__(self, toolbox, nrows, ncols):
        debug.mainthreadTest()
        self.toolbox = toolbox  # MeshToolboxGUI
        self.menu = self.toolbox.toolbox.menu  # ie, gfxtoolbox.toolbox.menu

        self.gtk = gtk.Frame(self.targetname + " Information")
        self.gtk.set_shadow_type(gtk.SHADOW_IN)
        scroll = gtk.ScrolledWindow()
        gtklogger.logScrollBars(scroll, self.targetname+"Info")
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.gtk.add(scroll)
        # This vbox just keeps the table from expanding inside the
        # scrolledwindow.
        vbox = gtk.VBox()
        scroll.add_with_viewport(vbox)
        self.table = gtk.Table(rows=nrows, columns=ncols)
        vbox.pack_start(self.table, expand=0, fill=0)

    def destroy(self):
        mainthread.runBlock(self.gtk.destroy)
        self.toolbox = None  # break circular references

    def clearQuery(self):
        self.updateNothing()
            
    # Utility routines for constructing GUI components
    
    def labelmaster(self, column, row, labeltext):
        debug.mainthreadTest()
        label = gtk.Label(labeltext)
        label.set_alignment(1.0, 0.5)
        self.table.attach(label, column[0],column[1], row[0],row[1],
                          xpadding=xpadding, xoptions=gtk.FILL)

    def entrymaster(self, column, row, editable=0):
        debug.mainthreadTest()
        entry = gtk.Entry()
        entry.set_size_request(12*guitop.top().digitsize, -1)
        entry.set_editable(editable)
        self.table.attach(entry, column[0],column[1], row[0],row[1],
                          xpadding=xpadding, xoptions=gtk.EXPAND|gtk.FILL)
        return entry

######################
    
class ElementMode(MeshInfoMode):
    targetname = "Element"
    def __init__(self, toolbox, querier=None):
        self.built = False
        MeshInfoMode.__init__(self, toolbox, nrows=4, ncols=2)

        self.labelmaster((0,1), (0,1), 'index=')
        self.index = self.entrymaster((1,2), (0,1))
        gtklogger.setWidgetName(self.index, 'index')

        self.labelmaster((0,1), (1,2), 'type=')
        self.type = self.entrymaster((1,2), (1,2))
        gtklogger.setWidgetName(self.type, 'type')

        self.labelmaster((0,1), (2,3), 'nodes=')
        self.nodes = self.makeNodeList((1,2), (2,3))

        self.labelmaster((0,1), (3,4), 'material=')
        self.material = self.entrymaster((1,2), (3,4))
        gtklogger.setWidgetName(self.material, 'material')
        self.built = True

    def makeNodeList(self, column, row):
        debug.mainthreadTest()
        chsr = chooser.FramedChooserListWidget(callback=self.showNodeCB,
                                               dbcallback=self.getNodeCB,
                                               autoselect=0, name="NodeList")
        self.table.attach(chsr.gtk, column[0], column[1], row[0], row[1],
                          xpadding=xpadding, xoptions=gtk.EXPAND|gtk.FILL)
        return chsr

    def getNodeCB(self, node):          # callback for dbl click on node list
        self.toolbox.changeModeWithObject(node, NodeMode)

    def showNodeCB(self, node, interactive):
        # Callback for single click on node list, or when list
        # selection is changed for any reason.  This can happen during
        # gui construction, so we have to be careful not to run
        # prematurely.
        peeker = self.toolbox.toolbox.peeker
        if self.built and peeker is not None: # also called during construction!
            if node:
                self.toolbox.toolbox.peeker.assignObject(node, "Node")
            else:
                self.toolbox.toolbox.peeker.removeObject("Node")
            if interactive:
                switchboard.notify("redraw")

    def menucmd(self):
        return self.menu.QueryElement
            
    def updateSomething(self, container):
        debug.mainthreadTest()
        element = container.object
        femesh = container.context.femesh()
        coord = container.mesh_position
        
        self.type.set_text(element.masterelement().name())
        self.index.set_text(`element.get_index()`)

        ## We can't just pass element.node_iterator() in to
        ## updateNodeList() because the iterator doesn't quite act
        ## like a list.  The ChooserListWidget uses list.index(),
        ## which the iterator doesn't have.
        self.updateNodeList(self.nodes,
                            [node for node in element.node_iterator()])

        ## If a node is selected in the list, then it's been peeked at
        ## and should be highlighted.  The peeker might not be in the
        ## correct state if this function has been called as a result
        ## of a Prev or Next button press, so we have to reassign the
        ## peeker here.
        selectednode = self.nodes.get_value()
        if selectednode is not None:
            self.toolbox.toolbox.peeker.assignObject(selectednode, "Node")
        else:
            self.toolbox.toolbox.peeker.removeObject("Node")

        mat = element.material()
        if mat:
            self.material.set_text(mat.name())
        else:
            self.material.set_text("<No material>")

    def updateNodeList(self, chsr, nodes):
        if config.dimension() == 2:
            namelist = ["%s %d at (%s, %s)" % 
                        (node.classname(), node.index(),
                         node.position().x, node.position().y)
                        for node in nodes]
        elif config.dimension() == 3:
            namelist = ["%s %d at (%s, %s, %s)" % 
                        (node.classname(), node.index(),
                         node.position().x, node.position().y, node.position().z)
                        for node in nodes]
        chsr.update(nodes, namelist)

    def updateNothing(self):
        debug.mainthreadTest()
        self.type.set_text("")
        self.index.set_text("")
        self.nodes.update([])
        self.material.set_text("")

######################
    
class NodeMode(MeshInfoMode):
    targetname = "Node"
    fieldspacing = 6 # spacing between Fields in the table
    def __init__(self, toolbox, querier=None):
        self.built = False
        MeshInfoMode.__init__(self, toolbox, nrows=3, ncols=3)

        self.labelmaster((0,1), (0,1), 'index=')
        self.index = self.entrymaster((1,3), (0,1))
        gtklogger.setWidgetName(self.index, 'index')

        self.labelmaster((0,1), (1,2), 'type=')
        self.type = self.entrymaster((1,3), (1,2))
        gtklogger.setWidgetName(self.type, 'type')

        self.labelmaster((0,1), (2,3), 'position=')
        self.pos = self.entrymaster((1,3), (2,3))
        gtklogger.setWidgetName(self.pos, 'position')

        self.baserows = self.table.get_property("n-rows")
        self.table.set_col_spacing(1, 4)
        self.fieldslisted = None
        # fieldvalEntries is a dict of the gtk.Entrys for displaying
        # the values of the DoFs at a Node.  The keys are (Field,
        # component) tuples.
        self.fieldvalEntries = {}
        # fieldvalWidgets contains the labels and separators in the
        # part of the gtk.Table used to display the DoF values. This
        # part of the table is dynamic, so we need to keep track of
        # these extra widgets so that they can be destroyed when the
        # table is rebuilt.
        self.fieldvalWidgets = set()
        self.built = True

    def updateSomething(self, container):
        debug.mainthreadTest()
        node = container.object
        femesh = container.context.femesh()
        
        self.index.set_text(`node.index()`)
        self.type.set_text(node.classname())
        if config.dimension() == 2:
            self.pos.set_text("(%s, %s)" %
                              (node.position().x, node.position().y))
        elif config.dimension() == 3:
            self.pos.set_text("(%s, %s, %s)" %
                              (node.position().x, node.position().y,
                               node.position().z))

        fieldnames = node.fieldNames()

        # Find out which fields are defined at the node
        nfieldrows = 0
        listedfields = []
        for fieldname in fieldnames:
            fld = field.getField(fieldname)
            zfld = fld.out_of_plane()
            tfld = fld.time_derivative()
            nfieldrows += fld.ndof()
            listedfields.append(fld)
            if node.hasField(zfld):
                listedfields.append(zfld)
                nfieldrows += zfld.ndof()
            if node.hasField(tfld):
                listedfields.append(tfld)
                nfieldrows += tfld.ndof()
        # Rebuild the table of field values, but only if the fields
        # have changed.
        if self.fieldslisted != listedfields:
            for entry in self.fieldvalEntries.values():
                entry.destroy()
            for widget in self.fieldvalWidgets:
                widget.destroy()
            self.fieldvalEntries.clear()
            self.fieldvalWidgets.clear()
            self.table.resize(rows=self.baserows + nfieldrows, columns=3)
            fldrow = self.baserows # starting row for a field
            for fld in listedfields:
                sep = gtk.HSeparator()
                self.fieldvalWidgets.add(sep)
                self.table.attach(sep, 0,3, fldrow,fldrow+1,xoptions=gtk.FILL)
                fldrow += 1
                label = gtk.Label(fld.name())
                label.set_alignment(1.0, 0.5)
                self.fieldvalWidgets.add(label)
                self.table.attach(label,
                                  0,1, fldrow,fldrow+fld.ndof(),
                                  xoptions=0)
                fcomp = fld.iterator(planarity.ALL_INDICES)
                while not fcomp.end():
                    row = fldrow + fcomp.integer()
                    label = gtk.Label(" " + fcomp.shortrepr()+"=")
                    self.fieldvalWidgets.add(label)
                    self.table.attach(label, 1,2, row,row+1, xoptions=gtk.FILL)
                    e = gtk.Entry()
                    e.set_size_request(10*guitop.top().charsize, -1)
                    e.set_editable(False)
                    self.fieldvalEntries[(fld, fcomp.integer())] = e
                    self.table.attach(e, 2,3, row,row+1,
                                      xoptions=gtk.EXPAND|gtk.FILL)
                    fcomp.next()
                    
                fldrow += fld.ndof()
            self.table.show_all()
            self.fieldslisted = listedfields

        # Fill in the field values in the table.
        for fld in self.fieldslisted:
            fcomp = fld.iterator(planarity.ALL_INDICES)
            while not fcomp.end():
                e = self.fieldvalEntries[(fld, fcomp.integer())]
                e.set_text("%-13.6g"%fld.value(femesh, node, fcomp.integer()))
                fcomp.next()
            

    def updateNothing(self):
        debug.mainthreadTest()
        self.index.set_text("")
        self.type.set_text("")
        self.pos.set_text("")
        
    def menucmd(self):
        return self.menu.QueryNode


############################################################################

modes = [ElementMode, NodeMode]

############################################################################
############################################################################

class MeshToolboxGUI(toolboxGUI.GfxToolbox, mousehandler.MouseHandler):
    def __init__(self, meshinfo):
        toolboxGUI.GfxToolbox.__init__(self, "Mesh Info", meshinfo)
        self.mainbox = gtk.VBox()
        self.gtk.add(self.mainbox)

        self.modeclass = ElementMode
        self.modeobj = None
        self.modeobjdict = {}

        clickframe = gtk.Frame()
        gtklogger.setWidgetName(clickframe, 'Click')
        clickframe.set_shadow_type(gtk.SHADOW_IN)
        self.mainbox.pack_start(clickframe, expand=0, fill=0)
        clickbox = gtk.VBox()
        clickframe.add(clickbox)

        hbox = gtk.HBox()
        clickbox.pack_start(hbox, expand=0, fill=0)
        hbox.pack_start(gtk.Label("Click on an: "), expand=0, fill=0)

        self.modebuttons = []
        self.modebuttonsignals = []
        for mode in modes:
            if self.modebuttons:
                button = gtk.RadioButton(label=mode.targetname,
                                        group=self.modebuttons[0])
            else:
                button = gtk.RadioButton(label=mode.targetname)
            gtklogger.setWidgetName(button, mode.targetname)
            self.modebuttons.append(button)
            tooltips.set_tooltip_text(button,
                               "Show " + mode.targetname + " information")
            hbox.pack_start(button, expand=0, fill=0)
            button.set_active(self.modeclass is mode)
            self.modebuttonsignals.append(
                gtklogger.connect(button, 'clicked', self.changeModeCB, mode))
                        
        # Display mouse click coordinates
        self.table = gtk.Table(columns=2, rows=config.dimension()+1)
        clickbox.pack_start(self.table, expand=0, fill=0)

        label = gtk.Label('x=')
        label.set_alignment(1.0, 0.5)
        self.table.attach(label, 0,1, 0,1, xpadding=5, xoptions=gtk.FILL)
        self.xtext = gtk.Entry()
        gtklogger.setWidgetName(self.xtext,'X')
        self.xtext.set_editable(0)
        self.xtext.set_size_request(13*guitop.top().charsize, -1)
        self.table.attach(self.xtext, 1,2, 0,1,
                          xpadding=5, xoptions=gtk.EXPAND|gtk.FILL)
        tooltips.set_tooltip_text(self.xtext,"x coordinate of the mouse click")
        label = gtk.Label('y=')
        label.set_alignment(1.0, 0.5)
        self.table.attach(label, 0,1, 1,2, xpadding=5, xoptions=gtk.FILL)
        self.ytext = gtk.Entry()
        gtklogger.setWidgetName(self.ytext,'Y')
        self.ytext.set_size_request(13*guitop.top().charsize, -1)
        self.ytext.set_editable(0)
        self.table.attach(self.ytext, 1,2, 1,2,
                          xpadding=5, xoptions=gtk.EXPAND|gtk.FILL)
        tooltips.set_tooltip_text(self.ytext,"y coordinate of the mouse click")
        if config.dimension() == 3:
            label = gtk.Label('z=')
            label.set_alignment(1.0, 0.5)
            self.table.attach(label, 0,1, 2,3, xpadding=5, xoptions=gtk.FILL)
            self.ztext = gtk.Entry()
            gtklogger.setWidgetName(self.ztext,'Z')
            self.ztext.set_size_request(13*guitop.top().charsize, -1)
            self.ztext.set_editable(0)
            self.table.attach(self.ztext, 1,2, 2,3,
                              xpadding=5, xoptions=gtk.EXPAND|gtk.FILL)
            tooltips.set_tooltip_text(self.ztext,"z coordinate of the mouse click")
            

        # End of clicked point display

        self.infoframe = gtk.Frame()
        self.infoframe.set_shadow_type(gtk.SHADOW_NONE)
        self.mainbox.pack_start(self.infoframe, expand=1, fill=1)
        self.meshcontext = self.toolbox.meshcontext()
        self.buildInfoGUI(self.modeclass)
        # End of query data display

        align = gtk.Alignment(xalign=0.5)
        self.mainbox.pack_start(align, expand=0, fill=0, padding=2)
        centerbox = gtk.HBox()
        align.add(centerbox)
        self.meshdatabutton = gtkutils.StockButton(gtk.STOCK_DIALOG_INFO,
                                                   'New Data Viewer...')
        gtklogger.setWidgetName(self.meshdatabutton, "NewDataViewer")
        centerbox.pack_start(self.meshdatabutton, expand=0, fill=0)
        gtklogger.connect(self.meshdatabutton, 'clicked', self.meshdataCB)
        tooltips.set_tooltip_text(self.meshdatabutton,
                             "Open a window to display fields, fluxes, and other quantities evaluated at the mouse click location.")

        buttonbox = gtk.HBox()
        self.mainbox.pack_start(buttonbox, expand=0, fill=0)
        self.prev = gtkutils.prevButton()
        tooltips.set_tooltip_text(self.prev,"Go back to the previous object.")
        gtklogger.connect(self.prev, 'clicked', self.prevQuery)
        buttonbox.pack_start(self.prev, expand=0, fill=0, padding=2)
        
        self.clear = gtk.Button(stock=gtk.STOCK_CLEAR)
        gtklogger.setWidgetName(self.clear, 'Clear')
        gtklogger.connect(self.clear, 'clicked', self.clearQuery)
        tooltips.set_tooltip_text(self.clear,"Clear the current query.")
        buttonbox.pack_start(self.clear, expand=1, fill=1, padding=2)

        self.next = gtkutils.nextButton()
        tooltips.set_tooltip_text(self.next,"Go to the next object.")
        gtklogger.connect(self.next, 'clicked', self.nextQuery)
        buttonbox.pack_start(self.next, expand=0, fill=0, padding=2)

        self.mainbox.show_all()
        self.sensitize()

        self.mouse_xposition = None
        self.mouse_yposition = None
        self.mesh_xposition = None
        self.mesh_yposition = None
        if config.dimension() == 3:
            self.mouse_zposition = None
            self.mesh_zposition = None
        
        self.sbcallbacks = [
            switchboard.requestCallbackMain((self.toolbox.gfxwindow(),
                                             "query mesh"),
                                            self.updateQuery),
            switchboard.requestCallbackMain("mesh changed",
                                            self.meshChanged),
            switchboard.requestCallbackMain("mesh data changed",
                                            self.meshDataChanged),
            switchboard.requestCallbackMain("subproblem changed",
                                            self.subproblemChanged),
            switchboard.requestCallbackMain( (self.toolbox, "new layers"),
                                             self.newLayers),
            switchboard.requestCallbackMain( (self.toolbox, "clear"),
                                             self.toolboxClear),
            switchboard.requestCallbackMain((self.toolbox.gfxwindow(),
                                             "time changed"),
                                            self.updateQuery)
            ]
        
    def buildInfoGUI(self, modeclass):
        debug.mainthreadTest()
        if self.modeobj and self.modeobj.__class__ is modeclass:
            return
        if self.modeobj:
            self.infoframe.remove(self.modeobj.gtk)
        # Reuse existing modeobj if possible
        try:
            self.modeobj = self.modeobjdict[modeclass]
        except KeyError:
            self.modeobj = self.modeobjdict[modeclass] = modeclass(self)
        self.infoframe.add(self.modeobj.gtk)

    def updateQuery(self):
        if not self.toolbox.querier:
            return
        # See if there's anything to update
        if self.toolbox.querier.object:
            # Change mode if needed.
            self.handleMode(self.toolbox.querier.targetname)
            self.showPosition(self.toolbox.querier.mouse_position,
                              self.toolbox.querier.mesh_position)
            subthread.execute(self._updateQuerySubthread)
        else:
            self.modeobj.updateNothing()
        self.sensitize()

    def _updateQuerySubthread(self):
        self.meshcontext.restoreCachedData(self.gfxwindow().displayTime)
        try:
            mainthread.runBlock(self.modeobj.updateSomething,
                                (self.toolbox.querier,))
        finally:
            self.meshcontext.releaseCachedData()
        gtklogger.checkpoint(self.gfxwindow().name + " " +
                             self._name + " updated")
        

    def newLayers(self, *args):
        debug.mainthreadTest()
        self.meshcontext = self.toolbox.meshcontext()
        for v in self.modeobjdict.values():
            v.clearQuery()

        # Changed layers mean changed meanings for mouse data -- clear
        # old data out.
        self.clearPositionData()

        if self.meshcontext is not None:
            self.buildInfoGUI(self.modeclass)
            self.mainbox.show_all()
            self.updateQuery()

        self.sensitize()

    def toolboxClear(self):
        self.clearPositionData()
        gtklogger.checkpoint(self.gfxwindow().name + " " +
                             self._name + " cleared")

    def meshChanged(self, meshcontext):
        debug.mainthreadTest()
        if self.meshcontext is meshcontext:
            self.buildInfoGUI(self.modeclass)
            self.mainbox.show_all()
            self.updateQuery()
            self.sensitize()
    def meshDataChanged(self, meshcontext):
        debug.mainthreadTest()
        if self.meshcontext is meshcontext:
            self.updateQuery()
    def subproblemChanged(self, subpcontext):
        self.meshChanged(subpcontext.getParent())

    def sensitize(self):
        debug.mainthreadTest()
        self.clear.set_sensitive(self.clearable())
        self.prev.set_sensitive(self.prev_able())
        self.next.set_sensitive(self.next_able())

        gtklogger.checkpoint(self.gfxwindow().name + " " +
                             self._name + " sensitized")

    def clearable(self):
        try:
            return self.toolbox.querier.clearable()
        except AttributeError:
            return 0

    def prev_able(self):
        return self.toolbox.prev_able()

    def next_able(self):
        return self.toolbox.next_able()

    def activate(self):
        toolboxGUI.GfxToolbox.activate(self)
        self.gfxwindow().setMouseHandler(self)
        self.toolbox.resetRecords()
        self.sensitize()
        if config.dimension() == 3:
            self.gfxwindow().toolbar.setSelect()

    def close(self):
        if self.modeobj:
            self.modeobj.destroy()
        map(switchboard.removeCallback, self.sbcallbacks)
        toolboxGUI.GfxToolbox.close(self)

    def acceptEvent(self, eventtype):
        return eventtype == 'up'

    def up(self, x, y, shift, ctrl):
        pos = self.getPoint(x,y)
        self.modeobj.menucmd()(position=pos)

    def changeMode(self, mode):
        debug.mainthreadTest()
        self.modeclass = mode
        self.buildInfoGUI(mode)
        self.mainbox.show_all()
        self.toolbox.resetPeeker()
        # Automatically query object with a current mouse-click point.
        # The menu item call here can be suppressed by setting
        # mouse_xposition to None, which is done in blockAutoQuery().
        if self.mouse_xposition is not None and \
               self.mouse_yposition is not None:
            pos = self.getPoint(self.mouse_xposition, self.mouse_yposition)
            self.modeobj.menucmd()(position=pos)

    def changeModeCB(self, button, mode):
        if self.modeclass is not mode:
            self.changeMode(mode)

    def blockAutoQuery(self):
        self.mouse_xposition = None
        self.mouse_yposition = None
        self.mesh_xposition = None
        self.mesh_yposition = None
        if config.dimension() == 3:
            self.mesh_zposition = None

    def changeModeWithObject(self, object, mode):
        # Called from double-click callback on the node list.  Always
        # switches modes, so it always issues a menu command.
        self.blockAutoQuery()
        self.changeModeAndSetButton(mode)
        if mode.targetname == "Element":
            pos = self.toolbox.meshlayer.displaced_from_undisplaced(
                self.toolbox.gfxwindow(), object.center())
        elif mode.targetname == "Node":
            pos = self.toolbox.meshlayer.displaced_from_undisplaced(
                self.toolbox.gfxwindow(), object.position())
        self.modeobj.menucmd()(position=pos)
        
    def showPosition(self, mouse, mesh):
        debug.mainthreadTest()
        self.xtext.set_text("%-13.6g" % mesh[0])
        self.ytext.set_text("%-13.6g" % mesh[1])
        self.mouse_xposition = mouse[0]
        self.mouse_yposition = mouse[1]
        self.mesh_xposition = mesh[0]
        self.mesh_yposition = mesh[1]
        if config.dimension() == 3:
            self.ztext.set_text("%-13.6g" % mesh[2])
            self.mesh_zposition = mesh[2]
        gtklogger.checkpoint(self.gfxwindow().name + " " +
                             self._name + " showed position")

    def clearPositionData(self):
        debug.mainthreadTest()
        self.xtext.set_text("")
        self.ytext.set_text("")
        self.mouse_xposition = None
        self.mouse_yposition = None
        self.mesh_xposition = None
        self.mesh_yposition = None
        if config.dimension() == 3:
            self.ztext.set_text("")
            self.mesh_zposition = None
        gtklogger.checkpoint(self.gfxwindow().name + " " +
                             self._name + " cleared position")

    def prevQuery(self, gtkobj):
        prev = self.toolbox.records.prev().clone()
        targetname = prev.targetname
        self.handleMode(targetname)
        self.toolbox.querier = prev
        self.toolbox.querysignal()      # updates info and redraws

    def clearQuery(self, gtkobj):
        self.mouse_xposition = None
        self.mouse_yposition = None
        self.mesh_xposition = None
        self.mesh_yposition = None
        if config.dimension() == 3:
            self.mesh_zposition = None
        for v in self.modeobjdict.values():
            v.clearQuery()
        self.toolbox.clearQuerier()
        
    def nextQuery(self, gtkobj):
        next = self.toolbox.records.next().clone()
        targetname = next.targetname
        self.handleMode(targetname)
        self.toolbox.querier = next
        self.toolbox.querysignal()      # updates info and redraws

    def handleMode(self, targetname):
        for mode in modes:
            if mode.targetname==targetname:
                if self.modeclass is not mode:
                    self.blockAutoQuery()
                    self.changeModeAndSetButton(mode)
                break

    def changeModeAndSetButton(self, mode):
        debug.mainthreadTest()
        modeindex = modes.index(mode)
        self.modebuttonsignals[modeindex].block()
        self.modebuttons[modeindex].set_active(1)
        self.modebuttonsignals[modeindex].unblock()
        self.changeMode(mode)

    def meshdataCB(self, button):
        meshdataGUI.openMeshData(self.gfxwindow(), 
                                 self.gfxwindow().displayTime,
                                 self.toolbox.currentPoint())
                              

def _makeGUI(self):
    return MeshToolboxGUI(self)

meshinfo.MeshInfoToolbox.makeGUI = _makeGUI
