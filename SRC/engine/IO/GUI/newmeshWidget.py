# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import switchboard
from ooflib.SWIG.engine import masterelement
from ooflib.SWIG.common import ooferror
from ooflib.common import debug
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.engine.IO import meshmenu

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Widget for the MasterElementTypesParameter, whose value is a list of
# MasterElement enumerators, one for each MasterElement topology.  The
# widget has a ChooserWidget for each element topology, and two extra
# Choosers for specifying the mapping order and interpolation order of
# the elements.  The Choosers for the elements only list those
# elements that have the desired orders.  This ensures that the user
# doesn't try to use linear triangles with quadratic quadrilaterals,
# for example.

class MasterElementTypesWidget(parameterwidgets.ParameterWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        frame = Gtk.Frame(shadow_type=Gtk.ShadowType.IN, **kwargs)
        self.table = None
        parameterwidgets.ParameterWidget.__init__(self, frame, scope, name=name)
        self.nclasses = 0    # number of enum classes (ie element topologies)
        self.classwidgets = []          # widgets for each enum class
        self.build()                    # construct widgets
        if not param.value:
            # Insert the choices in the choosers, if possible.
            ok = self.setChoices()
            self.widgetChanged(validity=ok, interactive=False)
        else:
            # Insert the choices in the choosers, and select the given value.
            self.set_value(param.value, interactive=False)

        self.sbcallback = switchboard.requestCallbackMain("new master element",
                                                          self.newElementCB)
    def cleanUp(self):
        debug.mainthreadTest()
        switchboard.removeCallback(self.sbcallback)
        parameterwidgets.ParameterWidget.cleanUp(self)
        del self.classwidgets
        del self.tablelabels
    def newElementCB(self):             # switchboard "new master element"
        self.build()
        
    def build(self):
        debug.mainthreadTest()
        elclasses = masterelement.getMasterElementEnumClasses()
        elgeometries = masterelement.getMasterElementGeometries()
        nclasses = len(elclasses)

        # Build the widgets, if necessary
        if self.table is None or nclasses != self.nclasses:
            self.nclasses = nclasses
            if self.table:
                self.table.destroy()
            self.tablelabels = []
            self.table = Gtk.Grid(margin=2, row_spacing=1, column_spacing=1)
            self.gtk.add(self.table)

            # Choosers for mapping and interpolation order
            self.mapchooser = chooser.ChooserWidget(
                [], callback=self.orderCB, name="Map",
                hexpand=True, halign=Gtk.Align.FILL)
            label = Gtk.Label(label='mapping order', halign=Gtk.Align.END)
            label.set_tooltip_text(
                'Polynomial order of the functions used to map master elements'
                ' to physical space.')
            self.tablelabels.append(label)
            self.table.attach(label, 0,0, 1,1)
            self.table.attach(self.mapchooser.gtk, 1,0, 1,1)

            self.funchooser = chooser.ChooserWidget(
                [], callback=self.orderCB, name="Func",
                hexpand=True, halign=Gtk.Align.FILL)
            label = Gtk.Label(label='interpolation order:',
                              halign=Gtk.Align.END)
            label.set_tooltip_text(
                'Polynomial order of the functions used to interpolate'
                ' within elements.')
            self.tablelabels.append(label)
            self.table.attach(label, 0,1, 1,1)
            self.table.attach(self.funchooser.gtk, 1,1, 1,1)

            # Choosers for each element geometry
            row = 2
            self.classwidgets = {}
            for geometry, elclass in zip(elgeometries, elclasses):
                label = Gtk.Label(label=repr(geometry)+'-cornered element:',
                                  halign=Gtk.Align.END)
                label.set_tooltip_text(
                        'Type of finite element to use for %d cornered'
                        ' Skeleton elements' % geometry)
                self.tablelabels.append(label)
                self.table.attach(label, 0,row, 1,1)
                ewidget = chooser.ChooserWidget(
                    [], name="%d-cornered"%geometry,
                    hexpand=True, halign=Gtk.Align.FILL)
                self.classwidgets[elclass] = ewidget
                self.table.attach(ewidget.gtk, 1,row, 1,1)
                row += 1

            # Find out which mapping and interpolation orders have to be listed.
            mapordset = set()
            funordset = set()

            for elclass in elclasses:
                for elname in elclass.names:
                    el = masterelement.getMasterElementFromEnum(elclass(elname))
                    mapordset.add(el.map_order())
                    funordset.add(el.fun_order())
            maporders = sorted(mapordset)
            funorders = sorted(funordset)
            # List the orders in the widgets
            self.mapchooser.update([repr(order) for order in maporders])
            self.funchooser.update([repr(order) for order in funorders])

    def setChoices(self, maporder=None, funorder=None):
        # Set the allowed values for the chooser for each geometry.
        # The allowed values are the element types with the current
        # mapping and interpolation orders.  The return value
        # indicates whether or not suitable element types were found
        # for each geometry.

        # Use the current interpolation orders or the ones from the
        # arguments.
        current_map = maporder or int(self.mapchooser.get_value())
        current_fun = funorder or int(self.funchooser.get_value())
        
        ok = True # Do all classes contain at least one suitable element type?
        elclasses = masterelement.getMasterElementEnumClasses()
        for elclass in elclasses:
            names = []
            for elname in elclass.names:
                el = masterelement.getMasterElementFromEnum(elclass(elname))
                if (el.map_order() == current_map and
                    el.fun_order() == current_fun):
                    names.append(el.name())
            ok = ok and bool(names)

            # classwidgets[elclass] is the chooser widget for the
            # geometry of the master elements in elclass.
            self.classwidgets[elclass].update(names, elclass.helpdict)
        return ok
        
    def orderCB(self, *args, **kwargs):
        # Mapping or interpolation order has been changed by the user.
        ok = self.setChoices()
        self.widgetChanged(validity=ok, interactive=True)

    def set_value(self, value, interactive):
        # value is a list of enums for master element types.  Check
        # that all of them have the same interpolation orders.
        maporder = funorder = None
        for val in value:
            el = masterelement.getMasterElementFromEnum(val)
            mo = el.map_order()
            fo = el.fun_order()
            if maporder is None:
                maporder = mo
                funorder = fo
            else:
                if mo != maporder or fo != funorder:
                    raise ooferror.PyErrUserError(
                        f"Inconsistent element types: {value}")
                    
        ok = self.setChoices(maporder, funorder)
        if not ok:
            self.widgetChanged(validity=False, interactive=interactive)
            return
        
        self.mapchooser.set_state(repr(maporder))
        self.funchooser.set_state(repr(funorder))

        # For each element type in value, set the corresponding
        # widget.
        for val in value:
            ewidget = self.classwidgets[val.__class__]
            ewidget.set_state(val.name)
            
        self.widgetChanged(validity=True, interactive=interactive)

    def show(self):
        debug.mainthreadTest()
        self.gtk.show()
        self.table.show()
        self.mapchooser.show()
        self.funchooser.show()
        for labelbox in self.tablelabels:
            labelbox.show_all()
        for ewidget in self.classwidgets.values():
            ewidget.show()

    def get_value(self):
        return [eclass(ewidget.get_value())
                for eclass, ewidget in self.classwidgets.items()]

def _MasterElementTypesParameter_makeWidget(self, scope=None, **kwargs):
    return MasterElementTypesWidget(self, scope, name=self.name, **kwargs)

meshmenu.MasterElementTypesParameter.makeWidget = \
                                   _MasterElementTypesParameter_makeWidget

