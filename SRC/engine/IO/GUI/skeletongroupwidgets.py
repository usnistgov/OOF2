# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import utils
from ooflib.common.IO import placeholder
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import boundarybuilder
from ooflib.engine import boundarymodifier
from ooflib.engine import mesh
from ooflib.engine import skeletoncontext
from ooflib.engine.IO import skeletongroupparams
from ooflib.engine.IO.GUI import bdymodparamwidget

# Special widgets for the SkeletonGroup parameters.

# The "defaults" argument is used by the "Aggregate" widget, to
# provide a mechanism for picking sets of SkeletonSelectables which
# are not groups.  Currently only "<selection>" is available, but
# other examples could include "all", "none", and possibly others.

class SkeletonGroupWidget(parameterwidgets.ParameterWidget):
    def __init__(self, param, groups=[], defaults=utils.OrderedSet(),
                 scope=None, name=None, **kwargs):
        self.defaults = defaults
        self.widget = chooser.ChooserWidget(groups, self.selectCB,
                                            name=name, **kwargs)
        parameterwidgets.ParameterWidget.__init__(self, self.widget.gtk,
                                                  scope)
        self.skelmeshwidget = scope.findWidget(
            lambda w: (isinstance(w, whowidget.WhoWidget) and
                       (w.whoclass is skeletoncontext.skeletonContexts
                        or w.whoclass is mesh.meshes)))
        assert self.skelmeshwidget is not None
        self.sbcallbacks = [switchboard.requestCallbackMain(self.skelmeshwidget,
                                                            self.skelwidgetCB)]
        self.update()
        if param.value is not None:
            self.set_value(param.value)
        self.sbcallbacks += [
            switchboard.requestCallbackMain("groupset member added",
                                            self.grpCB),
            switchboard.requestCallbackMain("groupset member renamed",
                                            self.grpCB),
            switchboard.requestCallbackMain("groupset changed", self.grpCB)
            ]
        self.widgetChanged(self.widget.nChoices() > 0, interactive=False)

    def get_value(self):
        return self.widget.get_value()
    def set_value(self, groupname):
        self.widget.set_state(groupname)

    def selectCB(self, result):
        self.widgetChanged(self.widget.nChoices() > 0, interactive=True)

    def skelwidgetCB(self, interactive):
        self.update()
        self.widgetChanged(self.widget.nChoices() > 0, interactive)
    def grpCB(self, *args, **kwargs):
        self.update()
        self.widgetChanged(self.widget.nChoices() > 0, interactive=False)

    def getSkeleton(self):
        skelname = self.skelmeshwidget.get_value(depth=2)
        try:
            return skeletoncontext.skeletonContexts[skelname]
        except KeyError:
            return None

    def update(self):
        self.redraw(self.getSkeleton())

    def cleanUp(self):
        switchboard.removeCallbacks(self.sbcallbacks)
        parameterwidgets.ParameterWidget.cleanUp(self)

class SkeletonAggregateWidget(SkeletonGroupWidget):
    def get_value(self):
        rval = self.widget.get_value()
        return placeholder.getPlaceHolderFromString(rval)

    def set_value(self, aggregate):
        if aggregate == placeholder.selection:
            super(SkeletonAggregateWidget, self).set_value(aggregate.IDstring)
        else:
            super(SkeletonAggregateWidget, self).set_value(aggregate)
        
# Dictionary, indexed by widget class, of the function to use to
# get a segment set from the relevant aggregate name.
segmenter = {}

class NodeGroupWidget(SkeletonGroupWidget):
    def __init__(self, param, groups=[], scope=None, name=None, **kwargs):
        SkeletonGroupWidget.__init__(self, param, groups, scope=scope,
                                     name=name, **kwargs)

    def redraw(self, skeletoncontext):
        if skeletoncontext:
            self.widget.update(list(
                self.defaults.union(skeletoncontext.nodegroups.allGroups())))
        else:
            self.widget.update(list(self.defaults))

def _makeNodeGroupWidget(self, scope=None, **kwargs):
    # "self" is the param instance.
    return NodeGroupWidget(self, scope=scope, name=self.name, **kwargs)

skeletongroupparams.NodeGroupParameter.makeWidget = _makeNodeGroupWidget


class NodeAggregateWidget(SkeletonAggregateWidget, NodeGroupWidget):
    def __init__(self, param, groups=[], scope=None, name=None, **kwargs):
        SkeletonGroupWidget.__init__(
            self, param, groups,
            defaults=utils.OrderedSet(
                [placeholder.selection.IDstring]),
            scope=scope, name=name, **kwargs)
        
def _makeNodeAggregateWidget(self, scope=None, **kwargs):
    return NodeAggregateWidget(self, scope=scope, name=self.name, **kwargs)

skeletongroupparams.NodeAggregateParameter.makeWidget = _makeNodeAggregateWidget

segmenter[NodeAggregateWidget]=boundarybuilder.segments_from_node_aggregate

####

class SegmentGroupWidget(SkeletonGroupWidget):
    def __init__(self, param, groups=[], scope=None, name=None, **kwargs):
        SkeletonGroupWidget.__init__(self, param, groups, scope=scope,
                                     name=name, **kwargs)

    def redraw(self, skeletoncontext):
        if skeletoncontext:
            self.widget.update(list(
                self.defaults.union(skeletoncontext.segmentgroups.allGroups())))
        else:
            self.widget.update(list(self.defaults))

def _makeSegmentGroupWidget(self, scope=None, **kwargs):
    return SegmentGroupWidget(self, scope=scope, name=self.name, **kwargs)

skeletongroupparams.SegmentGroupParameter.makeWidget = _makeSegmentGroupWidget



class SegmentAggregateWidget(SkeletonAggregateWidget, SegmentGroupWidget):
    def __init__(self, param, groups=[], scope=None, name=None, **kwargs):
        SkeletonGroupWidget.__init__(
            self, param, groups,
            defaults=utils.OrderedSet(
                [placeholder.selection.IDstring]),
            scope=scope, name=name, **kwargs)
        
def _makeSegmentAggregateWidget(self, scope=None, **kwargs):
    return SegmentAggregateWidget(self, scope=scope, name=self.name, **kwargs)

skeletongroupparams.SegmentAggregateParameter.makeWidget = \
    _makeSegmentAggregateWidget

segmenter[SegmentAggregateWidget]=boundarybuilder.segments_from_seg_aggregate


# Special context-aware segment aggregate widget for use in boundary
# modifiers.  This widget can tell whether or not the intended
# modification to the current boundary of the current segment will
# result in a sequence-able segment set, and will only report itself
# as "valid" if this is true.  Note that it is necessary to actually
# attempt the operation, sequence-ability cannot be deduced from the
# segment aggregate alone -- it may "tee" into the boundary, creating
# a branch, and fail even though the aggregate itself can be
# sequenced, or it may consist of two separate branches at the two
# end-points of the boundary, and thus succeed even though the
# aggregate itself cannot be sequenced.
# 
# This widget lives in a modal dialog box, and is a subwidget for a
# parameter to the boundary modifier, so the only real "dynamism" is
# that the value of the widget itself (i.e. the aggregate selection)
# can change.  We can get the skeleton and the modifier at init-time.

class BdyModSegmentAggregateWidget(SegmentAggregateWidget, SegmentGroupWidget):
    def __init__(self, param, groups=[], scope=None, name=None, **kwargs):
        SkeletonGroupWidget.__init__(
            self, param, groups,
            defaults=utils.OrderedSet(
                [placeholder.selection.IDstring]),
            scope=scope, name=name, **kwargs)
        # self.skelwidget has been set by the parent.  The modifier
        # widget will not change during our lifetime, since changing
        # it causes a new aggregate widget to be created.
        self.modifierwidget = scope.findWidget(
            lambda w: isinstance(w, bdymodparamwidget.BoundaryModParamWidget))
        
        # The modifierwidget's scope's parent is the ParameterDialog
        # box, which has the boundary name.
        self.bdy_name = self.modifierwidget.scope.parent.boundaryname
        self.widgetChanged(self.local_validity(), interactive=False)
        
    def selectCB(self, gtkobj, result):
        self.widgetChanged(self.local_validity(), interactive=True)
        
    def local_validity(self):
        if (self.widget.nChoices()>0 and self.modifierwidget
            and self.skelmeshwidget):
            grp = self.get_value()
            mod_reg = self.modifierwidget.getRegistration()
            mod_obj = mod_reg(group=grp)
            skelctxt = skeletoncontext.skeletonContexts[
                self.skelmeshwidget.get_value(depth=2)]
            return mod_obj.attempt(skelctxt, self.bdy_name)

        

def _makeBMSegmentAggregateWidget(self, scope=None, **kwargs):
    return BdyModSegmentAggregateWidget(self, scope=scope, name=self.name,
                                        **kwargs)

boundarymodifier.BdyModSegmentAggregateParameter.makeWidget = \
                                               _makeBMSegmentAggregateWidget

segmenter[BdyModSegmentAggregateWidget] = \
                                 boundarybuilder.segments_from_seg_aggregate

####

class ElementGroupWidget(SkeletonGroupWidget):
    def __init__(self, param, groups=[], scope=None, name=None, **kwargs):
        SkeletonGroupWidget.__init__(self, param, groups,
                                     defaults=utils.OrderedSet(),
                                     scope=scope, name=name, **kwargs)

    def redraw(self, skeletoncontext):
        if skeletoncontext:
            self.widget.update(list(
                self.defaults.union(skeletoncontext.elementgroups.allGroups())))
        else:
            self.widget.update(list(self.defaults))

def _makeElementGroupWidget(self, scope=None, **kwargs):
    return ElementGroupWidget(self, scope=scope, name=self.name, **kwargs)

skeletongroupparams.ElementGroupParameter.makeWidget = _makeElementGroupWidget

class ElementAggregateWidget(SkeletonAggregateWidget, ElementGroupWidget):
    def __init__(self, param, groups=[], scope=None, name=None, **kwargs):
        SkeletonGroupWidget.__init__(
            self, param, groups,
            defaults=utils.OrderedSet(
                [placeholder.selection.IDstring]),
            scope=scope, name=name, **kwargs)
        

def _makeElementAggregateWidget(self, scope=None, **kwargs):
    return ElementAggregateWidget(self, scope=scope, name=self.name, **kwargs)

skeletongroupparams.ElementAggregateParameter.makeWidget = \
    _makeElementAggregateWidget

segmenter[ElementAggregateWidget]=boundarybuilder.segments_from_el_aggregate

# ## ### #### ##### ###### ####### ######## ####### ###### ##### #### ### ## #


# Scope-aware widget for picking the boundary from the local skeleton
# context.

class SkeletonBoundaryWidgetBase(parameterwidgets.ParameterWidget):
    def __init__(self, param, boundaries=[], scope=None, name=None, **kwargs):
        self.widget = chooser.ChooserWidget(boundaries, self.selectCB,
                                            name=name, **kwargs)
        parameterwidgets.ParameterWidget.__init__(self, self.widget.gtk, scope)
        self.skelwidget = scope.findWidget(
            lambda w: isinstance(w, whowidget.WhoWidget)
            and (w.whoclass is skeletoncontext.skeletonContexts))
        self.update()

        self.sbcallbacks = [
            switchboard.requestCallbackMain(self.skelwidget,
                                            self.skelwidgetCB),
            switchboard.requestCallbackMain("new boundary configuration",
                                            self.update),
            switchboard.requestCallbackMain("new boundary created",
                                            self.update),
            switchboard.requestCallbackMain("boundary removed",
                                            self.update),
            switchboard.requestCallbackMain("boundary renamed",
                                            self.update)
            ]
        if param.value is not None:
            self.widget.set_state(param.value)
        self.widgetChanged(self.widget.nChoices() > 0, interactive=False)

    def get_value(self):
        return self.widget.get_value()
    def selectCB(self, result):
        self.widgetChanged(self.widget.nChoices() > 0, interactive=True)
    def skelwidgetCB(self, interactive):
        self.update()
        self.widgetChanged(self.widget.nChoices() > 0, interactive)

    def update(self, *args, **kwargs):
        try:
            skel = skeletoncontext.skeletonContexts[self.skelwidget.get_value()]
        except KeyError:
            skel = None

        self.redraw(skel)

    def redraw(self, skel):
        if skel:
            self.widget.update(self.names(skel))
        else:
            self.widget.update([])

    def cleanUp(self):
        switchboard.removeCallbacks(self.sbcallbacks)
        parameterwidgets.ParameterWidget.cleanUp(self)


class SkeletonBoundaryWidget(SkeletonBoundaryWidgetBase):
    def names(self, skel):
        return skel.allBoundaryNames()
        
def _makeSkeletonBoundaryWidget(self, scope=None, **kwargs):
    return SkeletonBoundaryWidget(self, scope=scope, name=self.name, **kwargs)

skeletongroupparams.SkeletonBoundaryParameter.makeWidget = \
                                                _makeSkeletonBoundaryWidget


class SkeletonEdgeBoundaryWidget(SkeletonBoundaryWidgetBase):
    def names(self, skel):
        return list(skel.edgeboundaries.keys())
        
def _makeSkeletonEdgeBoundaryWidget(self, scope=None, **kwargs):
    return SkeletonEdgeBoundaryWidget(self, scope=scope, name=self.name,
                                      **kwargs)

skeletongroupparams.SkeletonEdgeBoundaryParameter.makeWidget = \
                                                _makeSkeletonEdgeBoundaryWidget


class SkeletonPointBoundaryWidget(SkeletonBoundaryWidgetBase):
    def names(self, skel):
        return list(skel.pointboundaries.keys())
        
def _makeSkeletonPointBoundaryWidget(self, scope=None, **kwargs):
    return SkeletonPointBoundaryWidget(self, scope=scope, name=self.name,
                                       **kwargs)

skeletongroupparams.SkeletonPointBoundaryParameter.makeWidget = \
                                                _makeSkeletonPointBoundaryWidget


