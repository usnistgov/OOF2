# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
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
from ooflib.engine.IO import skeletoninfo

from ooflib.common.utils import stringjoin

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import sys

class SkeletonInfoMode:
    # Base class for ElementMode, NodeMode, and SegmentMode.
            
    def __init__(self, toolbox):
        debug.mainthreadTest()
        self.toolbox = toolbox  # SkeletonInfoToolboxGUI
        self.menu = self.toolbox.toolbox.menu  # ie, gfxtoolbox.toolbox.menu

        self.gtk = Gtk.Frame(label=self.targetname + " Information",
                             shadow_type=Gtk.ShadowType.IN)
        gtklogger.setWidgetName(self.gtk, self.targetname + "Information")
        self.table = Gtk.Grid(row_spacing=1, column_spacing=2, margin=2)
        self.gtk.add(self.table)

        self.sbcallbacks = [
            switchboard.requestCallback("groupset member resized",
                                        self.grpsChanged)]
        
    def destroy(self):
        self.built = False
        switchboard.removeCallbacks(self.sbcallbacks)
        mainthread.runBlock(self.gtk.destroy)
        self.toolbox = None  # break circular references

    def grpsChanged(self, context, groupset):
        # Switchboard callback, for when groups have changed.
        # Fleshed out in the subclasses.
        pass

    # Utility routines for constructing GUI components
    
    def labelmaster(self, column, row, labeltext, width=1, height=1):
        debug.mainthreadTest()
        label = Gtk.Label(label=labeltext, halign=Gtk.Align.END, hexpand=False)
        self.table.attach(label, column, row, width, height)

    def entrymaster(self, column, row, editable=False, width=1, height=1):
        debug.mainthreadTest()
        entry = Gtk.Entry(editable=editable,
                          hexpand=True, halign=Gtk.Align.FILL)
        entry.set_width_chars(13)
        self.table.attach(entry, column, row, width, height)
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
                                               name="NodeList",
                                               hexpand=True,
                                               halign=Gtk.Align.FILL)
        self.table.attach(chsr.gtk, column, row, 1,1)
        return chsr

    def updateNodeList(self, chsr, objlist):
        # called only when Skeleton readlock has been obtained.
        namelist = ["Node %d at (%s, %s)" % (obj.index, obj.position().x,
                                             obj.position().y)
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
                                               name="ElementList",
                                               hexpand=True,
                                               halign=Gtk.Align.FILL)
        self.table.attach(chsr.gtk, column, row, 1, 1)
        return chsr
    
    def updateElementList(self, chsr, objlist):
        # called only when Skeleton readlock has been obtained.
        namelist = ["Element %d" % obj.index for obj in objlist]
        mainthread. runBlock(chsr.update, (objlist, namelist))

    def updateGroup(self, obj):
        # called only when Skeleton readlock has been obtained.
        mainthread.runBlock(self.group.set_text,
                            (stringjoin(obj.groups, ', '),))


    def makeSegmentList(self, column, row):
        debug.mainthreadTest()
        chsr = chooser.FramedChooserListWidget(callback=self.showSegmentCB,
                                               dbcallback=self.getSegmentCB,
                                               autoselect=0,
                                               name="SegmentList",
                                               hexpand=True,
                                               halign=Gtk.Align.FILL)
        self.table.attach(chsr.gtk, column, row, 1, 1)
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

        self.labelmaster(0, 0, 'index=')
        self.index = self.entrymaster(1, 0)
        gtklogger.setWidgetName(self.index, "Index")
        
        self.labelmaster(0, 1, 'type=')
        self.type = self.entrymaster(1, 1)
        gtklogger.setWidgetName(self.type, "Type")

        self.labelmaster(0, 2, 'nodes=')
        self.nodes = self.makeNodeList(1, 2)

        self.labelmaster(0, 3, 'segments=')
        self.segs = self.makeSegmentList(1, 3)

        self.labelmaster(0, 4, 'area=')
        self.area = self.entrymaster(1, 4)
        gtklogger.setWidgetName(self.area, "Area")

        self.labelmaster(0, 5, 'dominant pixel=')
        self.domin = self.entrymaster(1, 5)
        gtklogger.setWidgetName(self.domin, "Dom pixel")

        self.labelmaster(0, 6, 'homogeneity=')
        self.homog = self.entrymaster(1, 6)
        gtklogger.setWidgetName(self.homog, "Homog")

        self.labelmaster(0, 7, 'shape energy=')
        self.shape = self.entrymaster(1, 7)
        gtklogger.setWidgetName(self.shape, "Shape")

        self.labelmaster(0, 8, 'element groups=')
        self.group = self.entrymaster(1, 8)
        gtklogger.setWidgetName(self.group, "Group")

        self.labelmaster(0, 9, 'material=')
        self.material = self.entrymaster(1, 9)
        gtklogger.setWidgetName(self.material, "Material")

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
            etype = repr(element.type())[1:-1] # strip quotes
            eindex = repr(element.getIndex())

            self.updateNodeListAngle(self.nodes, element)
            # Clear the selection in the list of nodes if there's
            # nothing in the peeker.
            self.syncPeeker(self.nodes, "Node")

            esegs = element.getSegments(skeleton)
            self.updateSegmentList(self.segs, esegs)
            # Clear the selection in the list of segments if there's
            # nothing in the peeker.
            self.syncPeeker(self.segs, "Segment")

            earea = "%s" % element.area()

            if not element.illegal():
                domCat = element.dominantPixel(skeleton.MS)
                repPix = skeleton.MS.getRepresentativePixel(domCat)
                pixGrp = pixelgroup.pixelGroupNames(skeleton.MS, repPix)
                pixgrps = stringjoin(pixGrp, ", ")
                # Change False to True in this line to get verbose
                # output from the homogeneity calculation.
                ehom = "%f" % element.homogeneity(skeleton.MS, False)
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

        self.labelmaster(0, 0, 'index=')
        self.index = self.entrymaster(1, 0)
        gtklogger.setWidgetName(self.index, "Index")

        self.labelmaster(0, 1, 'position=')
        self.pos = self.entrymaster(1, 1)
        gtklogger.setWidgetName(self.pos, "Position")

        self.labelmaster(0, 2, 'mobility=')
        self.mobility = self.entrymaster(1, 2)
        gtklogger.setWidgetName(self.mobility, "Mobility")

        self.labelmaster(0, 3, 'elements=')
        self.elem = self.makeElementList(1, 3)

        self.labelmaster(0, 4, 'node groups=')
        self.group = self.entrymaster(1, 4)
        gtklogger.setWidgetName(self.group, "Group")

        self.labelmaster(0, 5, 'boundary=')
        self.bndy = self.entrymaster(1, 5)
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
            nindex = repr(node.getIndex())
            npos = "(%s, %s)" % (node.position().x, node.position().y)
            
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

            self.updateElementList(self.elem, node.neighborElements())
            self.syncPeeker(self.elem, "Element")

            self.updateGroup(node)

            bdys = []
            for key, bdy in skeleton.pointboundaries.items():
                if node in bdy.nodes:
                    bdys.append(key)
            bdynames = stringjoin(bdys, ", ")
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
        self.labelmaster(0, 0, 'index=')
        self.index = self.entrymaster(1, 0)
        gtklogger.setWidgetName(self.index, "Index")

        self.labelmaster(0, 1, 'nodes=')
        self.nodes = self.makeNodeList(1, 1)

        self.labelmaster(0, 2, 'elements=')
        self.elem = self.makeElementList(1, 2)

        self.labelmaster(0, 3, 'length=')
        self.length = self.entrymaster(1, 3)
        gtklogger.setWidgetName(self.length, "Length")

        self.labelmaster(0, 4, 'homogeneity=')
        self.homog = self.entrymaster(1, 4)
        gtklogger.setWidgetName(self.homog, "Homogeneity")

        self.labelmaster(0, 5, 'segment groups=')
        self.group = self.entrymaster(1, 5)
        gtklogger.setWidgetName(self.group, "Groups")

        self.labelmaster(0, 6, 'boundary=')
        self.bndy = self.entrymaster(1, 6)
        gtklogger.setWidgetName(self.bndy, "Boundary")

#         self.labelmaster(0, 7, 'material=')
#         self.material = self.entrymaster(1, 7)
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
            sindex = repr(segment.getIndex())
            self.updateNodeList(self.nodes, list(segment.get_nodes()))
            self.syncPeeker(self.nodes, "Node")
            self.updateElementList(self.elem, segment.getElements())
            self.syncPeeker(self.elem, "Element")
            length = repr(segment.length())
            homogval = segment.homogeneity(skeleton.MS)
            if 0.9999 < homogval < 1.0:
                homog = "1 - (%e)" % (1.0-homogval)
            else:
                homog = repr(homogval)
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
        self.mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(self.mainbox)

        self.modeclass = ElementMode
        self.modeobj = None
        self.modeobjdict = {}

        clickbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                           spacing=2, margin=2)
        gtklogger.setWidgetName(clickbox, 'Click')
        self.mainbox.pack_start(clickbox, expand=False, fill=False, padding=0)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        clickbox.pack_start(hbox, expand=False, fill=False, padding=0)
        hbox.pack_start(Gtk.Label(label="Click on an: "),
                        expand=False, fill=False, padding=0)

        self.modebuttons = []
        self.modebuttondict = {}
        for mode in modes:
            if self.modebuttons:
                button = Gtk.RadioButton(label=mode.targetname,
                                        group=self.modebuttons[0])
            else:
                button = Gtk.RadioButton(label=mode.targetname)
            gtklogger.setWidgetName(button, mode.targetname)
            self.modebuttons.append(button)
            button.set_tooltip_text("Show " + mode.targetname + " Information")
            hbox.pack_start(button, expand=False, fill=False, padding=0)
            button.set_active(self.modeclass is mode)
            gtklogger.connect(button, 'clicked', self.changeModeCB, mode)
            self.modebuttondict[mode.targetname] = button

        # Display mouse click coordinates
        table = Gtk.Grid(row_spacing=2, column_spacing=2) 
        clickbox.pack_start(table, expand=False, fill=False, padding=0)

        label = Gtk.Label(label='x=', halign=Gtk.Align.END, hexpand=False)
        table.attach(label, 0,0, 1,1)
        self.xtext = Gtk.Entry(editable=False,
                               hexpand=True, halign=Gtk.Align.FILL)
        gtklogger.setWidgetName(self.xtext,"X Text")
        self.xtext.set_width_chars(13)
        table.attach(self.xtext, 1,0, 1,1)

        label = Gtk.Label(label='y=', halign=Gtk.Align.END, hexpand=False)
        table.attach(label, 0,1, 1,1)
        self.ytext = Gtk.Entry(editable=False,
                               hexpand=True, halign=Gtk.Align.FILL)
        gtklogger.setWidgetName(self.ytext,"Y Text")
        self.ytext.set_width_chars(13)
        table.attach(self.ytext, 1,1, 1,1),
        self.xtext.set_tooltip_text("x coordinate of the mouse click")
        self.ytext.set_tooltip_text("y coordinate of the mouse click")
        # End of clicked point display

        self.infoframe = Gtk.Frame(shadow_type=Gtk.ShadowType.NONE,
                                   vexpand=True)
        self.mainbox.pack_start(self.infoframe, expand=True,
                                fill=True, padding=0)
        
        self.buildInfoGUI(self.modeclass)

        # Buttons at the bottom: Prev, Clear, Next
        buttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        self.prev = gtkutils.prevButton()
        gtklogger.connect(self.prev, 'clicked', self.prevQuery)
        self.prev.set_tooltip_text("Go back to the previous object")
        buttonbox.pack_start(self.prev, expand=False, fill=False, padding=0)
        
        self.clear = gtkutils.StockButton('edit-clear-symbolic', 'Clear')
        gtklogger.setWidgetName(self.clear, 'Clear')
        gtklogger.connect(self.clear, 'clicked', self.clearQuery)
        self.clear.set_tooltip_text("Clear the current query.")
        buttonbox.pack_start(self.clear, expand=True, fill=True, padding=0)

        self.nextb = gtkutils.nextButton()
        gtklogger.connect(self.nextb, 'clicked', self.nextQuery)
        self.nextb.set_tooltip_text("Go on to the next object")
        buttonbox.pack_start(self.nextb, expand=False, fill=False, padding=0)

        self.mainbox.pack_start(buttonbox, expand=False, fill=False, padding=0)

        self.mainbox.show_all()
        self.sensitize()
        
        self.xposition = None
        self.yposition = None

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
        self.nextb.set_sensitive(self.next_able())
        gtklogger.checkpoint(self.gfxwindow().name + " " +
                             self._name + " sensitized")

    def clearable(self):
        try:
            return self.toolbox.querier.clearable()
        except AttributeError:
            return False
        
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

    def deactivate(self):
        toolboxGUI.GfxToolbox.deactivate(self)
        self.gfxwindow().removeMouseHandler()

    def close(self):
        debug.mainthreadTest()
        if self.modeobj:
            self.modeobj.destroy()
        switchboard.removeCallbacks(self.sbcallbacks)
        self.sbcallbacks = []
        toolboxGUI.GfxToolbox.close(self)

    def acceptEvent(self, eventtype):
        return eventtype == 'up'

    def up(self, x, y, button, shift, ctrl, data):
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
        self.modebuttondict[objtype].set_active(True)
        self.modeobj.queryIDcmd()(index=object.index)

    def showPosition(self, point):
        debug.mainthreadTest()
        self.xtext.set_text("%-11.4g" % point[0])
        self.ytext.set_text("%-11.4g" % point[1])
        self.xposition = point[0]
        self.yposition = point[1]
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
                        self.modebuttondict[targetname].set_active, (True,))
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
