# -*- python -*-
# $RCSfile: skeletoninfoGUI.py,v $
# $Revision: 1.94 $
# $Author: langer $
# $Date: 2011/07/05 19:34:00 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import pixelgroup
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import primitives
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import toolboxGUI
from ooflib.common.IO.GUI import tooltips
from ooflib.engine.IO import skeletoninfo
import gtk
import string
import sys

xpadding = 3
xoptions = gtk.EXPAND|gtk.FILL

class SkeletonInfoMode:
    # Base class for ElementMode, NodeMode, and SegmentMode.
            
    def __init__(self, toolbox):
        debug.mainthreadTest()
        self.toolbox = toolbox  # SkeletonInfoToolboxGUI
        self.menu = self.toolbox.toolbox.menu  # ie, gfxtoolbox.toolbox.menu

        self.gtk = gtk.Frame(self.targetname + " Information")
        self.gtk.set_shadow_type(gtk.SHADOW_IN)
        scroll = gtk.ScrolledWindow()
        gtklogger.logScrollBars(scroll, self.targetname+"Information")
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.gtk.add(scroll)
        # This vbox just keeps the table from expanding inside the
        # scrolledwindow.
        vbox = gtk.VBox()
        scroll.add_with_viewport(vbox)
        self.table = gtk.Table()
        vbox.pack_start(self.table, expand=0, fill=0)

        self.sbcallbacks = [
            switchboard.requestCallback("groupset member resized",
                                        self.grpsChanged)]
        
    def destroy(self):
        self.built = False
        map(switchboard.removeCallback, self.sbcallbacks)
        mainthread.runBlock(self.gtk.destroy)
        self.toolbox = None  # break circular references

    def grpsChanged(self, context, groupset):
        # Switchboard callback, for when groups have changed.
        # Fleshed out in the subclasses.
        pass

    # Utility routines for constructing GUI components
    
    def labelmaster(self, column, row, labeltext):
        debug.mainthreadTest()
        label = gtk.Label(labeltext)
        label.set_alignment(1.0, 0.5)
        self.table.attach(label, column[0],column[1], row[0],row[1],
                          xpadding=xpadding, xoptions=xoptions)

    def entrymaster(self, column, row, editable=0):
        debug.mainthreadTest()
        entry = gtk.Entry()
        entry.set_size_request(13*guitop.top().digitsize, -1)
        entry.set_editable(editable)
        self.table.attach(entry, column[0],column[1], row[0],row[1],
                          xpadding=xpadding, xoptions=xoptions)
        return entry

    # getBlahBlah => double-click callback
    # It is equvalent to "change mode" and "select the object".
    # showBlahBlah => single-click callback
    # It's not changing mode but shows the object.
    def getElementCB(self, element):
        self.toolbox.changeModeWithObject(element, "Element")

    def showElementCB(self, element, interactive):
        peeker = self.toolbox.toolbox.peeker
        if self.built and peeker is not None:
            if element:
                peeker.assignObject(element, "Element")
            else:
                peeker.removeObject("Element")
            if interactive:
                switchboard.notify("redraw")

    def getSegmentCB(self, segment):
        self.toolbox.changeModeWithObject(segment, "Segment")
        
    def showSegmentCB(self, segment, interactive):
        peeker = self.toolbox.toolbox.peeker
        if self.built and peeker is not None:
            if segment:
                peeker.assignObject(segment, "Segment")
            else:
                peeker.removeObject("Segment")
            if interactive:
                switchboard.notify("redraw")
        
    def getNodeCB(self, node):
        self.toolbox.changeModeWithObject(node, "Node")

    def showNodeCB(self, node, interactive):
        peeker = self.toolbox.toolbox.peeker
        if self.built and peeker is not None:
            if node:
                peeker.assignObject(node, "Node")
            else:
                peeker.removeObject("Node")
            if interactive:
                switchboard.notify("redraw")
        
    def makeNodeList(self, column, row):
        debug.mainthreadTest()
        chsr = chooser.FramedChooserListWidget(callback=self.showNodeCB,
                                               dbcallback=self.getNodeCB,
                                               autoselect=0,
                                               name="NodeList")
        self.table.attach(chsr.gtk, column[0], column[1], row[0], row[1],
                          xpadding=xpadding, xoptions=xoptions)
        return chsr

    def updateNodeList(self, chsr, objlist):
        # called only when Skeleton readlock has been obtained.
        if config.dimension() == 2:
            namelist = ["Node %d at (%s, %s)" % (obj.index, obj.position().x,
                                                 obj.position().y)
                        for obj in objlist]
        elif config.dimension() == 3:
            namelist = ["Node %d at (%s, %s, %s)" % (obj.index,
                                                     obj.position().x,
                                                     obj.position().y,
                                                     obj.position().z)
                        for obj in objlist]
        mainthread.runBlock(chsr.update, (objlist, namelist))

    def updateNodeListAngle(self, chsr, element):
        # called only when Skeleton readlock has been obtained.
        namelist = ["Node %d at (%s, %s) (angle: %s)" % \
                   (node.index, node.position().x, node.position().y,
                    element.getRealAngle(element.nodes.index(node)))
                    for node in element.nodes]
        mainthread.runBlock(chsr.update, (element.nodes, namelist))
    
    def makeElementList(self, column, row):
        debug.mainthreadTest()
        chsr = chooser.FramedChooserListWidget(callback=self.showElementCB,
                                               dbcallback=self.getElementCB,
                                               autoselect=0,
                                               name="ElementList")
        self.table.attach(chsr.gtk, column[0], column[1], row[0], row[1],
                          xpadding=xpadding, xoptions=xoptions)
        return chsr
    def updateElementList(self, chsr, objlist):
        # called only when Skeleton readlock has been obtained.
        namelist = ["Element %d" % obj.index for obj in objlist]
        mainthread. runBlock(chsr.update, (objlist, namelist))

    def updateGroup(self, obj):
        # called only when Skeleton readlock has been obtained.
        mainthread.runBlock(self.group.set_text,
                            (string.join(obj.groups, ', '),))

    def makeSegmentList(self, column, row):
        debug.mainthreadTest()
        chsr = chooser.FramedChooserListWidget(callback=self.showSegmentCB,
                                               dbcallback=self.getSegmentCB,
                                               autoselect=0,
                                               name="SegmentList")
        self.table.attach(chsr.gtk, column[0], column[1], row[0], row[1],
                          xpadding=xpadding, xoptions=xoptions)
        return chsr
    def updateSegmentList(self, chsr, objlist):
        # called only when Skeleton readlock has been obtained.        
        namelist = ["Segment %d, nodes (%d, %d) (length: %s)" %
                    (obj.index, obj.nodes()[0].index, obj.nodes()[1].index,
                     obj.length())
                    for obj in objlist]
        mainthread.runBlock(chsr.update, (objlist, namelist))

    def syncPeeker(self, chsr, objtype):
        # Make sure that there's nothing selected in a list if there's
        # nothing stored in the Peeker.
        if (not self.toolbox.toolbox.peeker or
            self.toolbox.toolbox.peeker.objects[objtype] is None):
            mainthread.runBlock(chsr.set_selection, (None,))

######################
    
class ElementMode(SkeletonInfoMode):
    nrows=10
    ncols=2
    targetname = "Element"
    def __init__(self, toolbox, querier=None):
        self.built = False
        SkeletonInfoMode.__init__(self, toolbox)

        self.labelmaster((0,1), (0,1), 'index=')
        self.index = self.entrymaster((1,2), (0,1))
        gtklogger.setWidgetName(self.index, "Index")
        
        self.labelmaster((0,1), (1,2), 'type=')
        self.type = self.entrymaster((1,2), (1,2))
        gtklogger.setWidgetName(self.type, "Type")

        self.labelmaster((0,1), (2,3), 'nodes=')
        self.nodes = self.makeNodeList((1,2), (2,3))

        self.labelmaster((0,1), (3,4), 'segments=')
        self.segs = self.makeSegmentList((1,2), (3,4))

        if config.dimension() == 2:
            area = "area="
            Area = "Area"
        elif config.dimension() == 3:
            area = "volume="
            Area = "Volume"
        self.labelmaster((0,1), (4,5), area)
        self.area = self.entrymaster((1,2), (4,5))
        gtklogger.setWidgetName(self.area, Area)

        self.labelmaster((0,1), (5,6), 'dominant pixel=')
        self.domin = self.entrymaster((1,2), (5,6))
        gtklogger.setWidgetName(self.domin, "Dom pixel")

        self.labelmaster((0,1), (6,7), 'homogeneity=')
        self.homog = self.entrymaster((1,2), (6,7))
        gtklogger.setWidgetName(self.homog, "Homog")

        self.labelmaster((0,1), (7,8), 'shape energy=')
        self.shape = self.entrymaster((1,2), (7,8))
        gtklogger.setWidgetName(self.shape,"Shape")

        self.labelmaster((0,1), (8,9), 'element groups=')
        self.group = self.entrymaster((1,2), (8,9))
        gtklogger.setWidgetName(self.group,"Group")

        self.labelmaster((0,1), (9,10), 'material=')
        self.material = self.entrymaster((1,2), (9,10))
        gtklogger.setWidgetName(self.material,"Material")
        self.built = True
        
    def querycmd(self):
        return self.menu.QueryElement
    def queryIDcmd(self):
        return self.menu.QueryElementByID

    def grpsChanged(self, context, groupset):
        querier = self.toolbox.toolbox.querier
        peeker = self.toolbox.toolbox.peeker
        if querier and querier.object and querier.targetname=="Element":
            if groupset is querier.context.elementgroups:
                self.updateSomething(querier)
            
    def updateSomething(self, container):
        debug.subthreadTest()
        element = container.object
        skeleton = container.skeleton

        container.context.begin_reading()
        try:
            etype = `element.type()`[1:-1] # strip quotes
            eindex = `element.getIndex()`

            if config.dimension() == 2:
                self.updateNodeListAngle(self.nodes, element)
            elif config.dimension() == 3:
                self.updateNodeList(self.nodes, element.nodes)
            # Clear the selection in the list of nodes if there's
            # nothing in the peeker.
            self.syncPeeker(self.nodes, "Node")

            esegs = element.getSegments(skeleton)
            self.updateSegmentList(self.segs, esegs)
            # Clear the selection in the list of segments if there's
            # nothing in the peeker.
            self.syncPeeker(self.segs, "Segment")

            if config.dimension() == 2:
                earea = "%s" % element.area()
            elif config.dimension() == 3:
                earea = "%s" % element.volume()

            if not element.illegal():
                domCat = element.dominantPixel(skeleton.MS)
                repPix = skeleton.MS.getRepresentativePixel(domCat)
                pixGrp = pixelgroup.pixelGroupNames(skeleton.MS, repPix)
                pixgrps = string.join(pixGrp, ", ")
                ehom = "%f" % element.homogeneity(skeleton.MS)
                eshape = "%f" % element.energyShape()

                mat = element.material(container.context)
                if mat:
                    matname = mat.name()
                else:
                    matname = "<No material>"
            else:                           # illegal element
                pixgrps = "???"
                ehom = "???"
                eshape = "???"
                matname = "???"
            self.updateGroup(element)
        finally:
            container.context.end_reading()
        mainthread.runBlock(self.updateSomething_thread,
                            (etype, eindex, earea, pixgrps, ehom, eshape,
                             matname))

    def updateSomething_thread(self, etype, eindex, earea, pixgrps, ehom,
                               eshape, matname):
        debug.mainthreadTest()
        self.type.set_text(etype)
        self.index.set_text(eindex)
        self.area.set_text(earea)
        self.domin.set_text(pixgrps)
        self.homog.set_text(ehom)
        self.shape.set_text(eshape)
        self.material.set_text(matname)

    def updateNothing(self):
        debug.mainthreadTest()
        self.type.set_text("")
        self.index.set_text("")
        
        self.nodes.update([])
        self.segs.update([])

        self.area.set_text("")
        self.domin.set_text("")
        self.homog.set_text("")
        self.shape.set_text("")
        self.group.set_text("")
        self.material.set_text("")

######################

# TODO: Display adjoining segments in NodeMode.
    
class NodeMode(SkeletonInfoMode):
    targetname = "Node"
    nrows = 6
    ncols = 2
    def __init__(self, toolbox, querier=None):
        self.built = False
        SkeletonInfoMode.__init__(self, toolbox)

        self.labelmaster((0,1), (0,1), 'index=')
        self.index = self.entrymaster((1,2), (0,1))
        gtklogger.setWidgetName(self.index, "Index")

        self.labelmaster((0,1), (1,2), 'position=')
        self.pos = self.entrymaster((1,2), (1,2))
        gtklogger.setWidgetName(self.pos, "Position")

        self.labelmaster((0,1), (2,3), 'mobility=')
        self.mobility = self.entrymaster((1,2), (2,3))
        gtklogger.setWidgetName(self.mobility, "Mobility")

        self.labelmaster((0,1), (3,4), 'elements=')
        self.elem = self.makeElementList((1,2), (3,4))

        self.labelmaster((0,1), (4,5), 'node groups=')
        self.group = self.entrymaster((1,2), (4,5))
        gtklogger.setWidgetName(self.group, "Group")

        self.labelmaster((0,1), (5,6), 'boundary=')
        self.bndy = self.entrymaster((1,2), (5,6))
        gtklogger.setWidgetName(self.bndy, "Boundary")
        self.built = True
        
    def grpsChanged(self, context, groupset):
        querier = self.toolbox.toolbox.querier
        peeker = self.toolbox.toolbox.peeker
        if querier and querier.object and querier.targetname=="Node":
            if groupset is querier.context.nodegroups:
                self.updateSomething(querier)

    def updateSomething(self, container):
        debug.subthreadTest()
        node = container.object
        skeleton = container.skeleton
        container.context.begin_reading()
        try:
            nindex = `node.getIndex()`
            if config.dimension() == 2:
                npos = "(%s, %s)" % (node.position().x, node.position().y)
            elif config.dimension() == 3:
                npos = "(%s, %s, %s)" % (node.position().x, 
                                         node.position().y, node.position().z)
            
            if config.dimension() == 2:
                if node.movable_x() and node.movable_y():
                    nmob = "free"
                elif node.movable_x() and not node.movable_y():
                    nmob = "x only"
                elif not node.movable_x() and node.movable_y():
                    nmob = "y only"
                elif node.pinned():
                    nmob = "pinned"
                else:
                    nmob = "fixed"
            elif config.dimension() == 3:
                if node.movable_x() and node.movable_y() and node.movable_z():
                    nmob = "free"
                elif node.movable_x() and node.movable_y() and not node.movable_z():
                    nmob = "x and y only"
                elif node.movable_x() and not node.movable_y() and node.movable_z():
                    nmob = "x and z only"
                elif not node.movable_x() and node.movable_y() and node.movable_z():
                    nmob = "y and z only"
                elif node.movable_x() and not node.movable_y() and not node.movable_z():
                    nmob = "x only"
                elif not node.movable_x() and node.movable_y() and not node.movable_z():
                    nmob = "y only"
                elif not node.movable_x() and not node.movable_y() and node.movable_z():
                    nmob = "z only"
                elif node.pinned():
                    nmob = "pinned"
                else:
                    nmob = "fixed"

            self.updateElementList(self.elem, node.neighborElements())
            self.syncPeeker(self.elem, "Element")

            self.updateGroup(node)

            bdys = []
            for key, bdy in skeleton.pointboundaries.items():
                if node in bdy.nodes:
                    bdys.append(key)
            bdynames = string.join(bdys, ", ")
        finally:
            container.context.end_reading()
        mainthread.runBlock(self.updateSomething_thread,
                            (nindex, npos, nmob, bdynames))

    def updateSomething_thread(self, nindex, npos, nmob, bdynames):
        debug.mainthreadTest()
        self.index.set_text(nindex)
        self.pos.set_text(npos)
        self.mobility.set_text(nmob)
        self.bndy.set_text(bdynames)

            
    def updateNothing(self):
        debug.mainthreadTest()
        self.index.set_text("")
        self.pos.set_text("")
        self.mobility.set_text("")
        self.elem.update([])
        self.group.set_text("")
        self.bndy.set_text("")

    def querycmd(self):
        return self.menu.QueryNode
    def queryIDcmd(self):
        return self.menu.QueryNodeByID

######################
    
class SegmentMode(SkeletonInfoMode):
    targetname = "Segment"
    ## TODO: This should display the material associated with a
    ## segment if the segment is part of a SkeletonBoundary which has
    ## a material assigned to it.  The machinery to do that isn't
    ## done, so the lines here that display the material are commented
    ## out.
    nrows = 7 # Change back to 8 if the 'material' lines below are restored
    ncols = 2
    def __init__(self, toolbox, querier=None):
        self.built = False
        SkeletonInfoMode.__init__(self, toolbox)
        self.labelmaster((0,1), (0,1), 'index=')
        self.index = self.entrymaster((1,2), (0,1))
        gtklogger.setWidgetName(self.index, "Index")

        self.labelmaster((0,1), (1,2), 'nodes=')
        self.nodes = self.makeNodeList((1,2), (1,2))

        self.labelmaster((0,1), (2,3), 'elements=')
        self.elem = self.makeElementList((1,2), (2,3))

        self.labelmaster((0,1), (3,4), 'length=')
        self.length = self.entrymaster((1,2), (3,4))
        gtklogger.setWidgetName(self.length, "Length")

        self.labelmaster((0,1), (4,5), 'homogeneity=')
        self.homog = self.entrymaster((1,2), (4,5))
        gtklogger.setWidgetName(self.homog, "Homogeneity")

        self.labelmaster((0,1), (5,6), 'segment groups=')
        self.group = self.entrymaster((1,2), (5,6))
        gtklogger.setWidgetName(self.group, "Groups")

        self.labelmaster((0,1), (6,7), 'boundary=')
        self.bndy = self.entrymaster((1,2), (6,7))
        gtklogger.setWidgetName(self.bndy, "Boundary")

#         self.labelmaster((0,1), (7,8), 'material=')
#         self.material = self.entrymaster((1,2), (7,8))
#         gtklogger.setWidgetName(self.material, "Material")

        self.built = True

    def grpsChanged(self, context, groupset):
        querier = self.toolbox.toolbox.querier
        peeker = self.toolbox.toolbox.peeker
        if querier and querier.object and querier.targetname=="Segment":
            if groupset is querier.context.segmentgroups:
                self.updateSomething(querier)
            
    def updateSomething(self, container):
        debug.subthreadTest()
        segment = container.object
        skeleton = container.skeleton
        container.context.begin_reading()
        try:
            sindex = `segment.getIndex()`
            self.updateNodeList(self.nodes, list(segment.get_nodes()))
            self.syncPeeker(self.nodes, "Node")
            self.updateElementList(self.elem, segment.getElements())
            self.syncPeeker(self.elem, "Element")
            length = `segment.length()`
            homogval = segment.homogeneity(skeleton.MS)
            if 0.9999 < homogval < 1.0:
                homog = "1 - (%e)" % (1.0-homogval)
            else:
                homog = `homogval`
            self.updateGroup(segment)

            bdynames = ','.join(
                segment.boundaryNames(container.context.getObject()))
#             mat = segment.material(container.context)
#             if mat:
#                 matname = mat.name()
#             else:
#                 matname = "<No material>"
        finally:
            container.context.end_reading()
        mainthread.runBlock(self.updateSomething_thread,
                            (sindex, length, homog, bdynames,
                             #matname
                             ))
    def updateSomething_thread(self, sindex, length, homog, bdynames,
                               #matname
                               ):
        debug.mainthreadTest()
        self.index.set_text(sindex)
        self.length.set_text(length)
        self.homog.set_text(homog)
        self.bndy.set_text(bdynames)
#         self.material.set_text(matname)
            
    def updateNothing(self):
        debug.mainthreadTest()
        self.index.set_text("")
        self.nodes.update([])
        self.elem.update([])
        self.length.set_text("")
        self.group.set_text("")
        self.bndy.set_text("")
        self.homog.set_text("")
#         self.material.set_text("")

    def querycmd(self):
        return self.menu.QuerySegment
    def queryIDcmd(self):
        return self.menu.QuerySegmentByID

############################################################################

modes = [ElementMode, NodeMode, SegmentMode]

############################################################################
############################################################################

class SkeletonInfoToolboxGUI(toolboxGUI.GfxToolbox, mousehandler.MouseHandler):
    def __init__(self, skeletoninfo):
        toolboxGUI.GfxToolbox.__init__(self, "Skeleton Info", skeletoninfo)
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
        self.modebuttondict = {}
        for mode in modes:
            if self.modebuttons:
                button = gtk.RadioButton(label=mode.targetname,
                                        group=self.modebuttons[0])
            else:
                button = gtk.RadioButton(label=mode.targetname)
            gtklogger.setWidgetName(button, mode.targetname)
            self.modebuttons.append(button)
            tooltips.set_tooltip_text(button,
                               "Show " + mode.targetname + " Information")
            hbox.pack_start(button, expand=0, fill=0)
            button.set_active(self.modeclass is mode)
            gtklogger.connect(button, 'clicked', self.changeModeCB, mode)
            self.modebuttondict[mode.targetname] = button

        # Display mouse click coordinates
        if config.dimension() == 2:
            table = gtk.Table(columns=2, rows=2) 
        elif config.dimension() == 3:
            table = gtk.Table(columns=2, rows=3) 
        clickbox.pack_start(table, expand=0, fill=0)

        label = gtk.Label('x=')
        label.set_alignment(1.0, 0.5)
        table.attach(label, 0,1, 0,1, xpadding=5, xoptions=gtk.FILL)
        self.xtext = gtk.Entry()
        gtklogger.setWidgetName(self.xtext,"X Text")
        self.xtext.set_editable(0)
        self.xtext.set_size_request(13*guitop.top().digitsize, -1)
        table.attach(self.xtext, 1,2, 0,1,
                          xpadding=5, xoptions=gtk.EXPAND|gtk.FILL)
        label = gtk.Label('y=')
        label.set_alignment(1.0, 0.5)
        table.attach(label, 0,1, 1,2, xpadding=5, xoptions=gtk.FILL)
        self.ytext = gtk.Entry()
        gtklogger.setWidgetName(self.ytext,"Y Text")
        self.ytext.set_size_request(13*guitop.top().digitsize, -1)        
        self.ytext.set_editable(0)
        table.attach(self.ytext, 1,2, 1,2,
                          xpadding=5, xoptions=gtk.EXPAND|gtk.FILL)
        if config.dimension() == 3:
            label = gtk.Label('z=')
            label.set_alignment(1.0, 0.5)
            table.attach(label, 0,1, 2,3, xpadding=5, xoptions=gtk.FILL)
            self.ztext = gtk.Entry()
            gtklogger.setWidgetName(self.ztext,"Z Text")
            self.ztext.set_size_request(13*guitop.top().digitsize, -1)        
            self.ztext.set_editable(0)
            table.attach(self.ztext, 1,2, 2,3,
                         xpadding=5, xoptions=gtk.EXPAND|gtk.FILL)
        tooltips.set_tooltip_text(self.xtext,"x coordinate of the mouse click")
        tooltips.set_tooltip_text(self.ytext,"y coordinate of the mouse click")
        if config.dimension() == 3:
            tooltips.set_tooltip_text(self.ztext,"z coordinate of the mouse click")
        # End of clicked point display

        self.infoframe = gtk.Frame()
        self.infoframe.set_shadow_type(gtk.SHADOW_NONE)
        self.mainbox.pack_start(self.infoframe, expand=1, fill=1)
        
        self.buildInfoGUI(self.modeclass)

        # Buttons at the bottom: Prev, Clear, Next
        buttonbox = gtk.HBox()
        self.prev = gtkutils.prevButton()
        gtklogger.connect(self.prev, 'clicked', self.prevQuery)
        tooltips.set_tooltip_text(self.prev,
                             "Go back to the previous object")
        buttonbox.pack_start(self.prev, expand=0, fill=0, padding=2)
        
        self.clear = gtk.Button(stock=gtk.STOCK_CLEAR)
        gtklogger.setWidgetName(self.clear, 'Clear')
        gtklogger.connect(self.clear, 'clicked', self.clearQuery)
        tooltips.set_tooltip_text(self.clear,"Clear the current query.")
        buttonbox.pack_start(self.clear, expand=1, fill=1, padding=2)

        self.next = gtkutils.nextButton()
        gtklogger.connect(self.next, 'clicked', self.nextQuery)
        tooltips.set_tooltip_text(self.next,"Go on to the next object")
        buttonbox.pack_start(self.next, expand=0, fill=0, padding=2)

        self.mainbox.pack_start(buttonbox, expand=0, fill=0, padding=2)

        self.mainbox.show_all()
        self.sensitize()
        
        self.xposition = None
        self.yposition = None
        if config.dimension() == 3:
            self.zposition = None

        self.sbcallbacks = [
            switchboard.requestCallback((self.toolbox.gfxwindow(),
                                         "query skeleton"),
                                        self.updateQuery),
            switchboard.requestCallback('changed pixel group', self.grpchanged),
            switchboard.requestCallback('changed pixel groups', self.grpschngd),
            switchboard.requestCallback('destroy pixel group', self.grpdestroy),
            switchboard.requestCallback('renamed pixel group', self.grprenamed),
            switchboard.requestCallback('materials changed in microstructure',
                                        self.matchanged),
            switchboard.requestCallback('materials changed in skeleton',
                                        self.matchangedSkel),
            switchboard.requestCallbackMain( (self.toolbox, "new skeleton"),
                                             self.newSkeleton)
            ]
        
    def buildInfoGUI(self, modeclass):
        debug.mainthreadTest()
        if self.modeobj and self.modeobj.__class__ is modeclass:
            return
        if self.modeobj:
            self.infoframe.remove(self.modeobj.gtk)
        # Reuse existing modeobj, if possible.
        try:
            self.modeobj = self.modeobjdict[modeclass]
        except KeyError:
            self.modeobj = self.modeobjdict[modeclass] = modeclass(self)
        self.infoframe.add(self.modeobj.gtk)

    def sensitize(self):
        mainthread.runBlock(self.sensitize_thread)
    def sensitize_thread(self):
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
        # TODO LATER: Toolbox history gets cleared on re-activation --
        # is this the desired behavior?
        toolboxGUI.GfxToolbox.activate(self)
        self.gfxwindow().setMouseHandler(self)
        self.toolbox.resetRecords()
        self.sensitize()
        if config.dimension() == 3:
            self.gfxwindow().toolbar.setSelect()

    def deactivate(self):
        toolboxGUI.GfxToolbox.deactivate(self)
        self.gfxwindow().removeMouseHandler()

    def close(self):
        debug.mainthreadTest()
        if self.modeobj:
            self.modeobj.destroy()
        map(switchboard.removeCallback, self.sbcallbacks)
        self.sbcallbacks = []
        toolboxGUI.GfxToolbox.close(self)

    def acceptEvent(self, eventtype):
        return eventtype == 'up'

    def up(self, x, y, shift, ctrl):
        pos = self.getPoint(x,y)
        self.modeobj.querycmd()(position=pos)

    def updateQuery(self):
        if not self.toolbox.querier:
            return
        # See if there's anything to update ...
        if self.toolbox.querier.object:
            # Change mode if needed.
            self.handleMode(self.toolbox.querier.targetname)
            querier = self.toolbox.querier
            self.modeobj.updateSomething(querier)
            mainthread.runBlock(self.showPosition,(querier.position,))
        else:
            mainthread.runBlock(self.modeobj.updateNothing)
        switchboard.notify("redraw")
        self.sensitize()

    def newSkeleton(self):
        self.clearAll()

    def changeMode(self, mode):
        debug.mainthreadTest()
        self.modeclass = mode
        self.buildInfoGUI(mode)
        self.mainbox.show_all()
        try:
            self.toolbox.peeker.reset()
        except AttributeError:
            pass
        # If there's a recorded mouse-click position, an appropriate object
        # will be queried automatically when changing mode.
        ## TODO: Is this the right thing to do?  When switching modes
        ## by double-clicking in a list, the mouse position is
        ## replaced by the repr_position of the double-clicked object.
        ## Switching back to the first mode using the mode buttons
        ## then does NOT return to the object selected in the first
        ## mode, because the repr_position is not old mouse click
        ## position.
        if self.xposition is not None and self.yposition is not None:
            self.modeobj.querycmd()(position=primitives.Point(self.xposition,
                                                             self.yposition))

    def changeModeCB(self, button, mode):
        if self.modeclass is not mode:
            self.changeMode(mode)

    def clearPosition(self):
        self.xposition = None
        self.yposition = None

    def changeModeWithObject(self, object, objtype):
        ## This uses object.index instead of object.repr_position so
        ## that it's possible to use peek mode to investigate illegal
        ## elements, overlapping nodes, etc.  The trouble with using
        ## the object index is that it's not very user friendly.
        debug.mainthreadTest()
        self.clearPosition()
        self.modebuttondict[objtype].set_active(1)
        self.modeobj.queryIDcmd()(index=object.index)

    def showPosition(self, point):
        debug.mainthreadTest()
        self.xtext.set_text("%-11.4g" % point[0])
        self.ytext.set_text("%-11.4g" % point[1])
        self.xposition = point[0]
        self.yposition = point[1]
        if config.dimension() == 3:
            self.ztext.set_text("%-11.4g" % point[2])
            self.zposition = point[2]
        gtklogger.checkpoint(self.gfxwindow().name + " " +
                             self._name + " showed position")

    def prevQuery(self, gtkobj):
        # TODO LATER: This has odd behavior -- you can go "previous"
        # through the toolbox, but then switching modes means you
        # can't go "next" again, because it runs a new query.
        prev = self.toolbox.records.prev().clone()
        targetname = prev.targetname
        self.handleMode(targetname)
        self.toolbox.querier = prev
        self.toolbox.querysignal() # calls self.updateQuery on subthread

    def clearQuery(self, gtkobj): # gtk callback for the Clear button
        self.clearAll()
        switchboard.notify("redraw")

    def clearAll(self):
        debug.mainthreadTest()
        self.clearPosition()
        self.xtext.set_text("")
        self.ytext.set_text("")
        if config.dimension() == 3:
            self.ztext.set_text("")
        for v in self.modeobjdict.values():
            v.updateNothing()
        self.toolbox.clearQuerier() # clears peeker too
        self.toolbox.resetRecords()
        self.sensitize()

    def nextQuery(self, gtkobj):
        next = self.toolbox.records.next().clone()
        targetname = next.targetname
        self.handleMode(targetname)
        self.toolbox.querier = next
        self.toolbox.querysignal() # calls self.updateQuery on subthread

    def handleMode(self, targetname):
        for mode in modes:
            if mode.targetname == targetname:
                if self.modeclass is not mode:
                    self.clearPosition()
                    # Call changeModeCB on main thread
                    mainthread.runBlock(
                        self.modebuttondict[targetname].set_active, (1,))
                break


    def grpchanged(self, group, ms_name):
        if self.modeobj.targetname:
            skelcontext = self.toolbox.getSkeletonContext()
            if skelcontext and skelcontext.getMicrostructure().name()==ms_name:
                self.updateQuery()

    def grpschngd(self, ms_name):
        if self.modeobj.targetname:
            skelcontext = self.toolbox.getSkeletonContext()
            if skelcontext and skelcontext.getMicrostructure().name()==ms_name:
                self.updateQuery()

    def grpdestroy(self, group, ms_name):
        if self.modeobj.targetname:
            skelcontext = self.toolbox.getSkeletonContext()
            if skelcontext and skelcontext.getMicrostructure().name()==ms_name:
                self.updateQuery()          
    def grprenamed(self, group, oldname, newname):
        if self.modeobj.targetname:
            self.updateQuery()
    def matchanged(self, ms):
        if self.modeobj.targetname:
            skelcontext = self.toolbox.getSkeletonContext()
            if skelcontext and skelcontext.getMicrostructure() is ms:
                self.updateQuery()
    def matchangedSkel(self, skelctxt):
        if self.modeobj.targetname:
            if skelctxt is self.toolbox.getSkeletonContext():
                self.updateQuery()
                

def _makeGUI(self):
    return SkeletonInfoToolboxGUI(self)

skeletoninfo.SkeletonInfoToolbox.makeGUI = _makeGUI
