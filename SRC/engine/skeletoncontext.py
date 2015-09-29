# -*- python -*-
# $RCSfile: skeletoncontext.py,v $
# $Revision: 1.153 $
# $Author: langer $
# $Date: 2013/04/18 19:30:11 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# A SkeletonContext is a subclass WhoDoUndo class.


from ooflib.SWIG.common import config
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import timestamp
from ooflib.common import debug
from ooflib.common import labeltree
from ooflib.common import microstructure
from ooflib.common import parallel_enable
from ooflib.common import runtimeflags
from ooflib.common import utils
from ooflib.common.IO import whoville
from ooflib.engine import materialmanager
from ooflib.engine import skeletonboundary
from ooflib.engine import skeletongroups
from ooflib.engine import skeletonnode
from ooflib.engine import skeletonselectable
from ooflib.engine.IO import movenode
import string
import sys

# When propagating boundaries, Deputies shouldn't be around - since they
# don't have nothing to do with boundaries!
# Takes a list of skeletons and removes Deputies.
def withoutDeputies(skels):
    return [skel for skel in skels if not skel.isDeputy()]

class SkeletonContext(whoville.WhoDoUndo):
    def __init__(self, name, classname, skel, parent):
        # All of the args have to be given, although not all are used.
        # This is because the constructor is called by WhoClass.add,
        # which assumes that the arguments are the same as those of
        # Who.__init__.  Probably a better solution using
        # RegisteredClasses could be found.

        # Keep track of node/segment/element index data (in that
        # order), so selectables can be uniquely identified within
        # this context, independently of which skeleton they're in.
        # This used to be done in the individual selectable classes,
        # but for repeatability reasons, it's desirable to restart the
        # indices in each context, ensuring that skeleton copies
        # really are absolutely identical in every respect.
        self.next_indices = (0, 0, 0)

        self.edgeboundaries = utils.OrderedDict() 
        self.pointboundaries = utils.OrderedDict()
        self.selectedBdyName = None
        # There are two boundary timestamps, one for keeping track of
        # changes in the currently selected boundary, and another for
        # keeping track of changes to the configuration of boundaries
        # in any of these skeletons.  They are queried by their
        # respective displays in skeletonbdydisplay.py.
        self.bdyselected = timestamp.TimeStamp()
        self.bdytimestamp = timestamp.TimeStamp()

        # Various selection objects live here.  Instance the
        # selections from their constructors.  To get the current
        # selection, do "context.elementselection.retrieve()".
        self.nodeselection = skeletonselectable.NodeSelection(self)
        self.segmentselection = skeletonselectable.SegmentSelection(self)
        self.elementselection = skeletonselectable.ElementSelection(self)
        self.pinnednodes = skeletonnode.PinnedNodeSelection(self)

        # These attribute names (nodegroups, segmentgroups,
        # elementgroups) are used in the generic menu callback in
        # IO/skeletongroupmenu.py.  Also in skeletonselectionmod.py.
        # Change them in all places (or none, of course.)
        self.nodegroups = skeletongroups.NodeGroupSet(self)
        self.segmentgroups = skeletongroups.SegmentGroupSet(self)
        self.elementgroups = skeletongroups.ElementGroupSet(self)
        
        # WhoDoUndo.__init__ calls pushModification, so timing is
        # important.  pushModification calls implied_select for all
        # the selections, so the selection objects have to exist at
        # this point.
        whoville.WhoDoUndo.__init__(self, name, 'Skeleton', skel, parent)

        # Overwrite function, gets called when an item in the stack is
        # about to be overwritten.  This assignment replaces  the default
        # overwrite function set by the parent class initializer.
        self.undobuffer.overwrite = self.skeletonDestroy

        # Ensure that the passed-in obj really does start a new "family."
        skel.disconnect()

        # Ask the initial skel about any pre-existing boundaries.
        for (name, bdy) in skel.edgeboundaries.items():
            self.edgeboundaries[name] = \
              bdy.makeContextBoundary(self, name, skel)

        for (name, bdy) in skel.pointboundaries.items():
            self.pointboundaries[name] = \
              bdy.makeContextBoundary(self, name, skel)

        self.requestCallback("destroy pixel group", self.ms_grp_changed)
        self.requestCallback("changed pixel group", self.ms_grp_changed)
        self.requestCallback("changed pixel groups", self.ms_grps_changed)
        self.requestCallback('materials changed in microstructure',
                             self.materialsChanged)

    # Switchboard callback for "changed pixel group" or "destroy pixel
    # group".
    def ms_grp_changed(self, group, ms_name):
        skelobj=self.getObject()
        if skelobj and ms_name == skelobj.MS.name():
            switchboard.notify("skeleton homogeneity changed", self.path())

    # Switchboard callback for "changed pixel groups", indicating that
    # multiple pixel groups have changed but "changed pixel group" has
    # *not* been sent for them, so that setHomogeneityIndex() won't be
    # called too often.
    def ms_grps_changed(self, ms_name):
        skelobj=self.getObject()
        if skelobj and ms_name == skelobj.MS.name():
            switchboard.notify("skeleton homogeneity changed", self.path())

    def materialsChanged(self, ms): # switchboard "materials changed ..."
        if ms is self.parent.getObject():
            switchboard.notify("skeleton homogeneity changed", self.path())
            for mesh in self.getMeshes():
                mesh.refreshMaterials(self)

    # Comparison routine -- checks that the two skeletons have the
    # same element, segment, and node groups and group members, and
    # the same pinned nodes.  This function is in this context because
    # the skeletoncontext object is the one that knows about group
    # membership.  Returns 0 if comparison is successful, otherwise
    # returns a string explaining what happened.  Used only in the
    # regression test suite.
    def compare_groups(self, other):
        if self.elementgroups.allGroups() != other.elementgroups.allGroups():
            return "Element group names mismatch: %s != %s" % (
                self.elementgroups.allGroups(), other.elementgroups.allGroups())
        for g in self.elementgroups.allGroups():
            if [x.index for x in self.elementgroups.get_group(g)] != \
               [x.index for x in other.elementgroups.get_group(g)]:
                return "Element group membership mismatch."
        if (self.elementgroups.getAllMaterials() != 
            other.elementgroups.getAllMaterials()):
            return "Mismatch in Element group materials."
            
        if self.segmentgroups.allGroups() != other.segmentgroups.allGroups():
            return "Segment group names mismatch."
        for g in self.segmentgroups.allGroups():
            if [x.index for x in self.segmentgroups.get_group(g)] != \
               [x.index for x in other.segmentgroups.get_group(g)]:
                return "Segment group membership mismatch."

        if self.nodegroups.allGroups() != other.nodegroups.allGroups():
            return "Node group names mismatch."
        for g in self.nodegroups.allGroups():
            if [x.index for x in self.nodegroups.get_group(g)] != \
               [x.index for x in other.nodegroups.get_group(g)]:
                return "Node group membership mismatch."

        if self.pinnednodes.npinned() != other.pinnednodes.npinned():
            return "Pinned-node count mismatch."

        if [x.index for x in self.pinnednodes.retrieve()] != \
           [x.index for x in other.pinnednodes.retrieve()]:
            return "Pinned nodes mismatch."

        return 0


    def lockAndDelete(self):
        self.reserve()
        for mesh in self.getMeshes()[:]:
            mesh.lockAndDelete()
        try:
            self.begin_writing()
            try:
                skeletonContexts.remove(self.path())
            finally:
                self.end_writing()
        finally:
            self.cancel_reservation()
    
    # Remove must be sure to break circular references. TODO: Really?
    # The Python garbage collector does that automatically, as long as
    # the objects don't have __del__ methods.
    def remove(self):
        # WhoDoUndo.remove destroys all the objects in the undobuffer.
        whoville.WhoDoUndo.remove(self)

        self.nodeselection.destroy()
        self.segmentselection.destroy()
        self.elementselection.destroy()
        self.nodegroups.destroy()
        self.segmentgroups.destroy()
        self.elementgroups.destroy()
        self.pinnednodes.destroy()
        del self.nodeselection
        del self.segmentselection
        del self.elementselection
        del self.pinnednodes
        del self.nodegroups
        del self.elementgroups
        del self.segmentgroups

    def pushModification(self, skeleton):
        old = self.getObject()
        skeleton.activate()
        # Call the parent pushModification without emitting the "who
        # changed" switchboard signal.  "whodoundo push" *is* emitted,
        # though.
        whoville.WhoDoUndo.pushModification(self, skeleton, signal=0)
        ## parallel push is implicitly applied in the line above
        self.undobuffer[0].promoteTrackers(self)

        # TODO: The new skeleton-selectable indexing scheme does not
        # pay any attention to what the parallel code does -- it's
        # likely that the parallel code is multiply broken, so this
        # hasn't been examined in detail.
        self.next_indices = skeleton.getIndexBase()

        # Propagate the boundaries.  This must be done before the
        # boundaries are drawn, which is why the "who changed" signal
        # was suppressed.

#         b = old.edgeboundaries['bottom']
#         print >> sys.stderr, "Bottom boundary: ",b, id(b)
#         for s in b.edges:
#             print >> sys.stderr, "Edge: ", s, s.segment
#         print >> sys.stderr, "\n"

        for e in self.edgeboundaries.values():
            skeleton.mapBoundary(e, old) # Default direction is child-ward.
        for p in self.pointboundaries.values():
            skeleton.mapBoundary(p, old) # Default direction is child-ward.
            
#         b = old.edgeboundaries['bottom']
#         print >> sys.stderr, "\nBottom boundary: ",b, id(b)
#         for s in b.edges:
#             print >> sys.stderr, "Edge: ", s, s.segment
#         print >> sys.stderr, "\n"

        self.bdytimestamp.increment()

        # This call's activity used to be done by the "'who changed',
        # 'Skeleton'" switchboard signal, but this signal was getting
        # into a race condition with callbacks for "new who", leading
        # to inconsistent checkpointing.  We can do the direct call
        # here, because there's no GUI activity involved.  It's
        # encapsulated in a function, because skeletonIO needs to do
        # it also.
        self.pause_writing()
        try:
            self.updateGroupsAndSelections()
        finally:
            self.resume_writing()
       
        # Now emit the "who changed' signal.
        self.pushModificationSignal()
        
        switchboard.notify("new boundary configuration", self)
        self.unSyncMeshes()

    def unSyncMeshes(self):
        # Tell all Meshes that they're out of sync with the Skeleton.
        for meshctxt in self.getMeshes():
            meshctxt.skeletonChanged(self.getObject())

    def updateGroupsAndSelections(self):
        self.nodegroups.new_objects(self)
        self.segmentgroups.new_objects(self)
        self.elementgroups.new_objects(self)

        self.nodeselection.newSkeleton(self)
        self.segmentselection.newSkeleton(self)
        self.elementselection.newSkeleton(self)
    

    def undoModification(self):
        whoville.WhoDoUndo.undoModification(self)
        self.next_indices = self._obj.getIndexBase()
        self.unSyncMeshes()
        
    def redoModification(self):
        whoville.WhoDoUndo.redoModification(self)
        self.next_indices = self._obj.getIndexBase()
        self.unSyncMeshes()

    # Extra operations during WhoDoUndo undo and redo.  If either the
    # old object or the new one is a DeputySkeleton, the positions of
    # the nodes must be updated.  Also, the number of edges/nodes in
    # the current boundary can be changed.
    
    
    def undoHookFn(self, oldskel, newskel):
        newskel.activate()
        self.pause_writing()
        try:
            self.updateGroupsAndSelections()
        finally:
            self.resume_writing()
        self.pinnednodes.replace(oldskel, newskel)
        self.bdytimestamp.increment()
        switchboard.notify("new boundary configuration", self)

    def redoHookFn(self, oldskel, newskel):
        newskel.activate()
        self.pause_writing()
        try:
            self.updateGroupsAndSelections()
        finally:
            self.resume_writing()
        self.pinnednodes.replace(oldskel, newskel)
        self.bdytimestamp.increment()
        switchboard.notify("new boundary configuration", self)

    def promoteDeputyTrackers(self, deputyskeleton):
        # Called by DeputySkeleton.promoteTrackers, but not by
        # Skeleton.promoteTrackers, which are called by
        # SkeletonContext.pushModification.
        self.elementselection.promoteDeputyTrackers(deputyskeleton)
        self.nodeselection.promoteDeputyTrackers(deputyskeleton)
        self.segmentselection.promoteDeputyTrackers(deputyskeleton)
        self.nodegroups.promoteDeputyTracker(deputyskeleton)
        self.elementgroups.promoteDeputyTracker(deputyskeleton)
        self.segmentgroups.promoteDeputyTracker(deputyskeleton)
##        self.pinnednodes.promoteDeputyTrackers(deputyskeleton)
        
    # ## ### #### ##### ###### ####### ####### ###### ##### #### ### ## #

    # Boundary functions -- create, destroy, eventually edit.
    # To create a boundary, create it in the current skeleton, then
    # propagate it upward and downward.  Likewise to destroy.
    def createEdgeBoundary(self, name, segment_set, startnode,
                           exterior=None, autoselect=1):
        bdy = self.getObject().makeEdgeBoundary(name,
                                                segment_set, startnode,
                                                exterior)
        for mesh in self.getMeshes():
            mesh.newEdgeBoundary(name, bdy)

        context_bdy = bdy.makeContextBoundary(self, name, self.getObject())
        self.edgeboundaries[name] = context_bdy

        #Interface branch
        #TODO: Add skeleton boundary to list of interfaces somehow
        #interfacemsplugin=self.getMicrostructure().getPlugIn("Interfaces")
        
        # Propagation up and down.
        # Unfortunate nomenclature -- in the context, mapping "down"
        # is towards the children, which is the direction of
        # increasing index in the undobuffer, and is therefore towards
        # the top.
        current = self.getObject()
        children = self.undobuffer.getToTop()
        for c in withoutDeputies(children[1:]):
            c.mapBoundary(context_bdy, current,
                          direction=skeletonboundary.MAP_DOWN)
            current = c

        current = self.getObject()
        parents = self.undobuffer.getToBottom()
        for p in withoutDeputies(parents[1:]):
            p.mapBoundary(context_bdy, current,
                          direction=skeletonboundary.MAP_UP)
            current = p

        switchboard.notify("new boundary created", self)
        if autoselect:
            self.selectBoundary(name)
        self.bdytimestamp.increment()
        
    #Interface branch
    def createNonsequenceableEdgeBoundary(self, name, segment_set,
                                          direction_set,
                                          exterior=None, autoselect=1):
        bdy = self.getObject().makeNonsequenceableEdgeBoundary(name,
                                                               segment_set,
                                                               direction_set,
                                                               exterior)
        for mesh in self.getMeshes():
            mesh.newEdgeBoundary(name, bdy)

        context_bdy = bdy.makeContextBoundary(self, name, self.getObject())
        self.edgeboundaries[name] = context_bdy
        
        # Propagation up and down.
        # Unfortunate nomenclature -- in the context, mapping "down"
        # is towards the children, which is the direction of
        # increasing index in the undobuffer, and is therefore towards
        # the top.
        current = self.getObject()
        children = self.undobuffer.getToTop()
        for c in withoutDeputies(children[1:]):
            c.mapBoundary(context_bdy, current,
                          direction=skeletonboundary.MAP_DOWN)
            current = c

        current = self.getObject()
        parents = self.undobuffer.getToBottom()
        for p in withoutDeputies(parents[1:]):
            p.mapBoundary(context_bdy, current,
                          direction=skeletonboundary.MAP_UP)
            current = p

        switchboard.notify("new boundary created", self)
        if autoselect:
            self.selectBoundary(name)
        self.bdytimestamp.increment()


    def createPointBoundary(self, name, node_set,
                            exterior=None, autoselect=1):
        bdy = self.getObject().makePointBoundary(name, node_set, exterior)

        for mesh in self.getMeshes():
            mesh.newPointBoundary(name, bdy)

        context_bdy = bdy.makeContextBoundary(self, name, self.getObject())
        self.pointboundaries[name] = context_bdy
        
        # Propagation up and down.
        # See routine above for nomenclature lament.
        # DeputySkeleton.mapBoundary is a no-op.
        current = self.getObject()
        children = self.undobuffer.getToTop()
        for c in withoutDeputies(children[1:]):
            c.mapBoundary(context_bdy, current,
                          direction=skeletonboundary.MAP_DOWN)
            current = c

        current = self.getObject()
        parents = self.undobuffer.getToBottom()
        for p in withoutDeputies(parents[1:]):
            p.mapBoundary(context_bdy, current,
                          direction=skeletonboundary.MAP_UP)
            current = p

        switchboard.notify("new boundary created", self)
        if autoselect:
            self.selectBoundary(name)
        self.bdytimestamp.increment()

    # The edgeboundaries[name] or pointboundaries[name] objects here
    # are SkelContextBoundary objects -- their "remove" methods
    # remove the corresponding Skeleton[Point|Edge]Boundary objects
    # from the skeletons.
    def removeBoundary(self, name):
        # Actual removal from skeletons happens in the
        # SkelContext<type>Boundary's remove routine.
        for mesh in self.getMeshes():
            mesh.removeBoundary(name)
        if name in self.edgeboundaries:
            self.edgeboundaries[name].remove()
            del self.edgeboundaries[name]
        elif name in self.pointboundaries:
            self.pointboundaries[name].remove()
            del self.pointboundaries[name]
        else:
            raise ooferror.ErrUserError(
                "Cannot remove boundary %s, no such boundary." % name)
        if name == self.selectedBdyName:
            self.unselectBoundary()
        self.bdytimestamp.increment()
        switchboard.notify("boundary removed", self)

    def renameBoundary(self, oldname, newname):
        if oldname==newname:
            return

        if newname in self.allBoundaryNames():
            raise ooferror.ErrSetupError("Name %s is already in use." % newname)

        #Interface branch
        if config.dimension() == 2 and runtimeflags.surface_mode:
            if newname in self.allInterfaceNames():
                raise ooferror.ErrSetupError(
                    "Name %s is already in use as an interface name." % newname)

        if oldname in self.edgeboundaries:
            dict = self.edgeboundaries
        elif oldname in self.pointboundaries:
            dict = self.pointboundaries
        else: 
            raise ooferror.ErrPyProgrammingError(
                "Boundary name %s not found." % oldname)

        dict[newname]=dict[oldname]
        del dict[oldname]

        # SkelContextBoundary.rename calls Skeleton.renameBoundary
        dict[newname].rename(newname)

        # Maintain consistency in Meshes
        for mesh in self.getMeshes():
            mesh.renameBoundary(oldname, newname)

        switchboard.notify("boundary renamed", self)
        self.bdytimestamp.increment()
        self.selectBoundary(newname)

    # Retrieval routine -- returns the SkeletonContextBoundary object.
    def getBoundary(self, name):
        try:
            return self.edgeboundaries[name]
        except KeyError:
            return self.pointboundaries[name]

    # The selected boundary isn't actually used for anything directly,
    # but it's displayed in the GUI and its name is passed in as an
    # argument to commands that operate on boundaries.  
    def selectBoundary(self, bdyname):
        self.selectedBdyName = bdyname
        self.bdyselected.increment()    # timestamp
        switchboard.notify("boundary selected", self, bdyname)
        switchboard.notify('redraw')
    def unselectBoundary(self):
        if self.selectedBdyName is not None:
            self.selectedBdyName = None
            self.bdyselected.increment()
            switchboard.notify("boundary unselected", self)
            switchboard.notify('redraw')
    def getSelectedBoundaryName(self):
        return self.selectedBdyName
    def getSelectedBoundary(self):      # returns SkeletonContextBoundary object
        if self.selectedBdyName is not None:
            return self.getBoundary(self.selectedBdyName)
            

    # ## ### #### ##### ###### ####### ####### ###### ##### #### ### ## #

    # Routines that modify a boundary in place.  All of them exit via
    # the "bdyPropagate", which propagates the modified boundaries up
    # and down the stack.  All of these routines call
    # SkelContextBoundary objects which actually operate on the
    # sheriff of the current skeleton, not the current skeleton
    # itself.


    # Function to determine whether or not the requested modification
    # will result in a legal, sequence-able boundary.
    def try_appendSegstoBdy(self, name, seg_set):
        try:
            bdy = self.edgeboundaries[name]
        except KeyError:
            raise ooferror.ErrSetupError(
                "Boundary %s is not an edge boundary." % name)

        return bdy.try_append(seg_set)
    
        
    def appendSegstoBdy(self, name, seg_set):
        try:
            bdy = self.edgeboundaries[name]
        except KeyError:
            raise ooferror.ErrSetupError(
                "Boundary %s is not an edge boundary." % name)

        bdy.append(seg_set)

        self.bdyPropagate(name, bdy)
        self.bdytimestamp.increment()

    def reverseBoundary(self, name):
##         print "BEGIN skeletoncontext:reverseBoundary"
##         print self.edgeboundaries["bottom"].current_boundary().edges
        try:
            bdy = self.edgeboundaries[name] # SkelContextEdgeBoundary
        except KeyError:
            raise ooferror.ErrSetupError("Boundary %s is not an edge boundary."
                                         % name)
        bdy.reverse()
        self.bdyPropagate(name, bdy)
        self.bdytimestamp.increment()
##         print self.edgeboundaries["bottom"].current_boundary().edges
##         print "END skeletoncontext:reverseBoundary"


    def addNodestoBdy(self, name, node_list):
        try:
            bdy = self.pointboundaries[name]
        except KeyError:
            raise ooferror.ErrSetupError(
                "Boundary %s is not a point boundary." % name)

        bdy.append(node_list)

        self.bdyPropagate(name, bdy)
        self.bdytimestamp.increment()


    # Function to determine whether or not the requested modification
    # will result in a legal, sequence-able boundary.
    def try_removeSegsfromBdy(self, name, seg_set):
        try:
            bdy = self.edgeboundaries[name]
        except KeyError:
            raise ooferror.ErrSetupError(
                "Boundary %s is not an edge Boundary." % name)

        return bdy.try_delete(seg_set)
        
    # Function to actually do it.
    def removeSegsfromBdy(self, name, seg_set):
        try:
            bdy = self.edgeboundaries[name]
        except KeyError:
            raise ooferror.ErrSetupError(
                "Boundary %s is not an edge boundary." % name)

        bdy.delete(seg_set)
        
        self.bdyPropagate(name, bdy)
        self.bdytimestamp.increment()

        
    def removeNodesfromBdy(self, name, node_list):
        try:
            bdy = self.pointboundaries[name]
        except KeyError:
            raise ooferror.ErrSetupError(
                "Boundary %s is not a point boundary." % name)

        bdy.delete(node_list)

        self.bdyPropagate(name, bdy)
        self.bdytimestamp.increment()

    def bdyPropagate(self, name, contextbdy):
        # Replace the boundaries up and down the stack with a suitably
        # mapped version of the modified boundary.  Operate only
        # on sheriffs, and don't re-operate on the original object.

        # Then, ensure that the modifications get to the meshes --
        # in this case, we need to run over the whole stack, because
        # although deputy skeletons don't have boundaries, their
        # meshes nevertheless do.

        start = self.getObject().sheriffSkeleton() # Current sheriff
        children = self.undobuffer.getToTop()

        current = start
        for c in withoutDeputies(children[1:]):
            if not c is start:
                contextbdy.remove(c)
                contextbdy.map(current, c,
                               direction=skeletonboundary.MAP_DOWN)
                current = c

        current = start
        parents = self.undobuffer.getToBottom()
        for p in withoutDeputies(parents[1:]):
            if not p is start:
                contextbdy.remove(p)
                contextbdy.map(current, p, direction=skeletonboundary.MAP_UP)
                current = p

        # Update the boundaries in the Meshes to match the boundaries
        # in the Skeleton.
        for mesh in self.getMeshes():
            mesh.getObject().skeleton.pushBoundaryToMesh(mesh, name)

        switchboard.notify("new boundary configuration", self)


    # ## ### #### ##### ###### ####### ####### ###### ##### #### ### ## #

    def allEdgeBoundaryNames(self):
        return self.edgeboundaries.keys()
    
    def allBoundaryNames(self):
        return self.edgeboundaries.keys() + self.pointboundaries.keys()

    #Interface branch
    def allInterfaceNames(self):
        msobj=self.getMicrostructure()
        if runtimeflags.surface_mode:
            interfacemsplugin=msobj.getPlugIn("Interfaces")
            return interfacemsplugin.getInterfaceNames()
        else:
            return []
        
    def uniqueBoundaryName(self, name):
        if config.dimension() == 2:
            return utils.uniqueName(name, self.allBoundaryNames()+self.allInterfaceNames())
        if config.dimension() == 3:
            return utils.uniqueName(name, self.allBoundaryNames())

    # Get information about the named boundary, i.e. type, size, and
    # return it as a string, with newlines as appropriate.
    def boundaryInfo(self, boundaryname):
        outlist = []
        type = "Edge"
        bdy = None
        try:
            bdy = self.edgeboundaries[boundaryname]
            if bdy.sequenceableflag(self.getObject())==0:
                type+=", not sequenceable"
        except KeyError:
            type = "Point"
            try:
                bdy = self.pointboundaries[boundaryname]
            except KeyError:
                type = "Unknown"

        outlist.append("Type: %s" % type)

        if bdy:
            outlist.append("Size: %i" % bdy.size(self.getObject()))
        
        return string.join(outlist,"\n")
        
                
    #Called by C++ edgement function refreshInterfaceMaterial() (element.C)
    def getInterfaceMaterial(self, edgementname):
        if edgementname in self.allEdgeBoundaryNames():
            interfacematname=self.getBoundary(edgementname)._interfacematerial
        else:
            interfacemsplugin=self.getMicrostructure().getPlugIn("Interfaces")
            interfacematname=interfacemsplugin.getInterfaceMaterialName(edgementname)
        if interfacematname:
            return materialmanager.materialmanager[interfacematname].actual
        else:
            return None
                

    # ## ### #### ##### ###### ####### ####### ###### ##### #### ### ## #

    # This function is passed a reference to a skeleton that is about
    # to be overwritten in the stack.  The boundaries need to be
    # removed from the skeleton to break circular references between
    # the edges and segments, and all the selectables should unhook
    # themselves from their parents and/or children.
    def skeletonDestroy(self, skeleton):
        skeleton.destroy(self)

    # Copy over the group data from another skeletoncontext.
    def groupCopy(self, other):
        mygroups = [self.nodegroups, self.segmentgroups, self.elementgroups]
        othergroups = [other.nodegroups, other.segmentgroups,
                       other.elementgroups] 
        for (g, og) in map(None, mygroups, othergroups):
            g.nameCopy(og)

    # ## ### #### ##### ###### ####### ####### ###### ##### #### ### ## #

    # List retrievers, from here to the end of the undo buffer,
    # including (in both cases) the current skeleton.

    def getChildList(self):
        return self.undobuffer.getToTop()

    def getParentList(self):
        return self.undobuffer.getToBottom()

    # ## ### #### ##### ###### ####### ####### ###### ##### #### ### ## #    

    def getMicrostructure(self):
        return self.getObject().MS
    
##    def removeWho(self, whopath):
##        ## if whopath[-1] == self.getObject().MS.name():  # used to be this
##        if len(whopath)==1 and whopath[0]==self.getObject().MS.name():
##            # Our Microstructure has been removed.  Remove ourself.
##            skeletonContexts.remove(self.path())

    def getSelectionContext(self, mode):
        return mode.getSelectionContext(self)

    def getMeshes(self):
        from ooflib.engine import mesh # avoid import loop
        path = labeltree.makePath(self.path())
        if not path:
            # path can be None if we're still in the process o
            # building a new SkeletonContext.  In that case, there are
            # no Meshes.
            return []
        meshnames = mesh.meshes.keys(
            path, condition=lambda x: not isinstance(x, whoville.WhoProxy))
        return [mesh.meshes[path + name] for name in meshnames]
            
    def __repr__(self):
        return 'SkeletonContext("%s")' % self.name()

skeletonContexts = whoville.WhoDoUndoClass(
    'Skeleton',
    ordering=200,
    parentClass=microstructure.microStructures,
    instanceClass=SkeletonContext,
    proxyClasses=['<topmost>'])

utils.OOFdefine('skeletonContexts', skeletonContexts)

def getSkeleton(ms, name):
    # ms is a Microstructure.  Returns a SkeletonContext
    return skeletonContexts[[ms.name(), name]]

def extractSkeletonPath(somepath):
    #Calling labeltree.makePath may be a more formal way to do this.
    pathlist=string.split(somepath,":")
    if len(pathlist)<2:
        #Shouldn't happen
        return somepath
    return pathlist[0]+':'+pathlist[1]
