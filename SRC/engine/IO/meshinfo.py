# -*- python -*-
# $RCSfile: meshinfo.py,v $
# $Revision: 1.74 $
# $Author: langer $
# $Date: 2010/12/24 22:42:12 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import timestamp
from ooflib.SWIG.common import ooferror
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import ringbuffer
from ooflib.common import toolbox
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO import xmlmenudump

import sys

from ooflib.common import parallel_enable
if parallel_enable.enabled():
    from ooflib.SWIG.common import mpitools
    from ooflib.engine.IO import meshIPC

class MeshQueryContainer:
    def __init__(self, context):
        self.timestamp = timestamp.TimeStamp()
        self.context = context  # mesh context
        self.object = None
        self.mouse_position = None
        self.mesh_position = None
        self.targetname = None

    def set(self, object=None, targetname=None, mouse_position=None,
            mesh_position=None):
        self.object = object
        self.mouse_position = mouse_position
        self.mesh_position = mesh_position
        self.targetname = targetname
        self.timestamp.increment()

    def getTimeStamp(self):
        return self.timestamp

    def clone(self):
        krusty = MeshQueryContainer(self.context)
        krusty.object = self.object
        krusty.targetname = self.targetname
        krusty.mouse_position = self.mouse_position
        krusty.mesh_position = self.mesh_position
        krusty.timestamp.increment()
        return krusty

    def clearable(self):
        return not not self.object

# Peek functionality for "mesh" is going to be limited to "Node".
# There's a remote chance to include "Element" and "Edge" here.
# However, the code is written in a form that can handle these remote chance.
class MeshPeekContainer(MeshQueryContainer):
    def __init__(self, context):
        self.timestamp = timestamp.TimeStamp()
        self.context = context
        self.objects = {"Node":None}

    def assignObject(self, object, objtype):
        self.objects[objtype] = object
        self.timestamp.increment()

    def removeObject(self, objtype):
        self.objects[objtype] = None
        self.timestamp.increment()

    def reset(self):
        self.objects = {"Node":None}
        self.timestamp.increment()

    def getTimeStamp(self):
        return self.timestamp


#############################################################

# The mesh info toolbox has a special attribute, "meshlayer", which
# refers to the display layer in which the referred-to mesh is
# displayed.  The reason for needing the actual layer is that the
# toolbox *display* needs to be able to draw the selected objects
# (elements, nodes) at their displaced position, possibly including
# any enhancements, and the mesh display layer's "where" object has
# all of that data.  Mesh display layers provide coordinate
# transformation routines that convert undisplaced to displaced
# points, and vice versa.
            
class MeshInfoToolbox(toolbox.Toolbox):
    def __init__(self, gfxwindow):
        toolbox.Toolbox.__init__(self, 'Mesh_Info', gfxwindow)
        self.whoset = ('Mesh',)
        self.querier = None
        self.peeker = None      
        self.records = ringbuffer.RingBuffer(49)
        self.meshlayer = None
        self.last_position = None # Most recent mouse-click position.

        self.sbcallbacks = [
            switchboard.requestCallback((self.gfxwindow(), "layers changed"),
                                        self.newLayers)]
            
    def close(self):
        map(switchboard.removeCallback, self.sbcallbacks)

    def makeMenu(self, menu):
        self.menu = menu
        menu.addItem(oofmenu.OOFMenuItem(
            'QueryElement',
            callback=self.queryElem,
            params=[primitives.PointParameter('position', tip='Target point.')],
            help="Query an FE element at a given point.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/query_mesh_elem.xml')
            ))
        menu.addItem(oofmenu.OOFMenuItem(
            'QueryNode',
            callback=self.queryNode,
            params=[primitives.PointParameter('position', tip='Target point.')],
            help="Query an FE node at a given point.",
            discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/query_mesh_node.xml')
            ))

    def activate(self):
        meshcontext = self.gfxwindow().topwho(*self.whoset)
        self.meshlayer = self.gfxwindow().topwholayer(*self.whoset)
        if meshcontext is not None:
            if not self.querier:
                self.querier = MeshQueryContainer(meshcontext)
            if not self.peeker:
                self.peeker = MeshPeekContainer(meshcontext)
        else:
            self.querier = None
            self.peeker = None

    def meshcontext(self):
        return self.gfxwindow().topwho(*self.whoset)

    def newLayers(self):        # sb "layers changed" callback
        self.meshlayer = self.gfxwindow().topwholayer(*self.whoset)
        lastmesh = None
        if self.querier:
            lastmesh = self.querier.context
        meshctxt = self.meshcontext()
        if lastmesh is not meshctxt:
            self.resetRecords()
            if meshctxt is None:
                if self.querier is not None:
                    self.querier.set()
                if self.peeker is not None:
                    self.peeker.reset()
                self.querier.context = None
            else:
                self.querier = MeshQueryContainer(meshctxt)
                self.peeker = MeshPeekContainer(meshctxt)
            switchboard.notify((self, "new layers"))

    def resetRecords(self):
        self.records.clear()

    def resetPeeker(self):
        if self.peeker is not None:
            self.peeker.reset()

    # "position" is mouse position.
    def queryElem(self, menuitem, position):
        context = self.gfxwindow().topwho(*self.whoset)
        if not context:
            return

        if parallel_enable.enabled():
            meshIPC.ipcmeshmenu.Mesh_Info_Query(targetname="Element",
                                                position=position,
                                                mesh=context.path())
            if mpitools.Rank()>0:
                return

        if position == self.last_position:
            meshpos = self.querier.mesh_position
        else:
            if config.dimension() == 2:
                try:
                    context.restoreCachedData(self.gfxwindow().displayTime)
                    try:
                        meshpos = self.meshlayer.undisplaced_from_displaced(
                            self.gfxwindow(), position)
                    finally:
                        context.releaseCachedData()
                except ooferror.ErrBoundsError:
                    return
            elif config.dimension() == 3:
                # skip handling displaced meshes in 3D for now. 
                # TODO 3D Later: figure this out
                meshpos = position
            
        femesh = context.getObject()
        skeleton = context.getSkeleton()
        selem = skeleton.enclosingElement(meshpos)
        felem = femesh.getElement(selem.meshindex)
        self.finishQuery(felem, felem, "Element", position, meshpos)

    def queryNode(self, menuitem, position):
        context = self.gfxwindow().topwho(*self.whoset)
        if not context:
            return

        if parallel_enable.enabled():
            meshIPC.ipcmeshmenu.Mesh_Info_Query(
                targetname="Node",
                position=position,mesh=context.path())
            if mpitools.Rank()>0:
                return

        if position == self.last_position:
            meshpos = self.querier.mesh_position
        else:
            if config.dimension() == 2:
                try:
                    context.restoreCachedData(self.gfxwindow().displayTime)
                    try:
                        meshpos = self.meshlayer.undisplaced_from_displaced(
                            self.gfxwindow(), position)
                    finally:
                        context.releaseCachedData()
                except ooferror.ErrBoundsError:
                    return
            elif config.dimension() == 3:
                # skip handling displaced meshes in 3D for now.  
                # TODO 3D Later: figure this out
                meshpos = position

        femesh = context.getObject()
        skeleton = context.getSkeleton()
        selem = skeleton.enclosingElement(meshpos)
        felem = femesh.getElement(selem.meshindex)
        if config.dimension() == 2:
            fnode = femesh.closestNode(meshpos.x, meshpos.y)
        elif config.dimension() == 3:
            fnode = femesh.closestNode(meshpos.x, meshpos.y, meshpos.z)
        self.finishQuery(fnode, felem, "Node", position, meshpos)

    def finishQuery(self, object, element, targetname, mouse_pos, mesh_pos):
        # TODO LATER: Mesh toolboxes can ignore queries if they are
        # "out of bounds" in the sense that the clicked-on element is
        # empty.  Maintaining a consistent state when the
        # hideEmptyElements setting is changed is quite tricky, so for
        # now, we just accept and process these events.  Below is the
        # code to ignore them.
        
        # if element.material() is None and  \
        #        self.gfxwindow().settings.hideEmptyElements:
        #     return

        self.last_position = mouse_pos
        self.querier.set(object=object, targetname=targetname,
                         mouse_position=mouse_pos,
                         mesh_position=mesh_pos)
        self.records.push(self.querier.clone())
        self.peeker.reset()
        self.querysignal()

    def querysignal(self):
        switchboard.notify((self.gfxwindow(),"query mesh"))
        switchboard.notify((self.gfxwindow(), "meshinfo click"),
                           self.querier.mesh_position)
        self.redraw()

    def clearQuerier(self):
        self.last_position = None
        if self.querier:
            self.querier.set()
            self.peeker.reset()
            self.redraw()
        switchboard.notify((self, "clear"))

    def currentPoint(self):
        try:
            currentquerier = self.records.current()
        except IndexError:
            return
        if currentquerier:
            return currentquerier.mesh_position

    def redraw(self):
        switchboard.notify("redraw")

    def prev_able(self):
        return not self.records.atBottom()

    def next_able(self):
        return not self.records.atTop()
    tip = "Get information about a Mesh."
    discussion="""<para>
    Get information about a &mesh;, including &field; values, based on
    mouse input.
    </para>"""

toolbox.registerToolboxClass(MeshInfoToolbox, ordering=3.0)
