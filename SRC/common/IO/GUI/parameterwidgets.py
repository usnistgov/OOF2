# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# GTK widgets for inputting Parameter objects.

from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import primitives
from ooflib.common import strfunction
from ooflib.common import utils
from ooflib.common.IO import automatic
from ooflib.common.IO import parameter
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import widgetscope

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import math
import string
import sys

from ooflib.common.utils import stringlstrip

# The python2 version of this file used FloatType, IntType, etc, via
# "from types import *".  Rather than change all of them by hand, we
# just define the old names here:
FloatType = float
IntType = int
ListType = list
TupleType = tuple
StringType = str

############################

class ParameterWidget:
    def __init__(self, gtk, scope=None, name=None, expandable=False,
                 compact=False):
        debug.mainthreadTest()
        self.gtk = gtk                  # base of gtk widget heirarchy
        self.scope = scope              # WidgetScope containing this widget
        self._valid = 0
        # expandable is used when the widget appears in a
        # ParameterTable to indicate if the widget should adjust its
        # y-dimension when the table is resized.  
        self.expandable = expandable
        # compact is used when a smaller form of a widget is desired,
        # such as in a dense table.  Not all widgets have compact
        # forms. Only a few of them need it, so I didn't go
        # back and add it to them all.  If it's necessary to implement
        # a compact form for a new ParameterWidget, make sure to give
        # the Parameter's makeWidget method an optional 'compact'
        # argument with default value False.
        self.compact = compact

        if scope:
            scope.addWidget(self)
        self.gtk.connect('destroy', self.destroyCB)
        if name:
            gtklogger.setWidgetName(self.gtk, name)

    # Widgets that contain other widgets must redefine show().  show()
    # must call the show() function of each of the subwidgets, instead
    # of just calling gtk.show_all().  This is because the subwidgets
    # might have parts that shouldn't be shown in all contexts.
    def show(self):
        debug.mainthreadTest()
        self.gtk.show_all()

    # Widget destruction.  Destruction is initiated either when
    # external code calls ParameterWidget.destroy(), or when the gtk
    # widget is destroyed by gtk.  ParameterWidget.cleanUp() can be
    # redefined in derived classes if there's other stuff to be done.
    # The derived classes must then be sure to call the base class
    # cleanUp function.
    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()
    def destroyCB(self, *args):
        self.gtk = None
        self.cleanUp()
    def cleanUp(self):                  # redefine in derived classes
        if self.scope:
            self.scope.removeWidget(self)
            self.scope = None

    # Widget subclasses should call widgetChanged whenever their value
    # changes.  widgetChanged issues a switchboard call when the
    # validity changes.  The "interactive" flag is used to indicate
    # non-programmatic changes -- some widgets need to do extra
    # consistency work in that case, or suppress callback loops.
    def widgetChanged(self, validity, interactive):
        if self._valid and not validity:
            self._valid = 0
            switchboard.notify(('validity', self), 0)
        elif not self._valid and validity:
            self._valid = 1
            switchboard.notify(('validity', self), 1)
        switchboard.notify(self, interactive)
    def isValid(self):
        return self._valid
    def __repr__(self):
        return self.__class__.__name__

    # Widgets in a ParameterTable may want to synchronize themselves
    # in some way.  This function is called on all widgets in a
    # ParameterTable after they've all been added.  The arguments are
    # the ParameterTable and the widgets it contains.
    def parameterTableXRef(self, ptable, widgets):
        pass

    # For debugging. Redefine in derived classes to print more useful info.
    def dumpState(self, comment):
        print(comment, "(%s)" % self.__class__.__name__, file=sys.stderr)

# GenericWidget is a base class for several other widgets.  It can
# also be created as an instance itself, but currently this is not
# done.
class GenericWidget(ParameterWidget):
    def __init__(self, param, scope=None, name=None, compact=False,
                 value=None,    # init. to this instead of param.value
                 **kwargs):
        # It's possible that param.value can't be evaluate when the
        # widget is constructed because its resolution depends on the
        # state of other widgets that may not exist yet.  In that
        # case, pass an initial value for the widget in the 'value'
        # arg, to be used instead of param.value.
        debug.mainthreadTest()
        widget = Gtk.Entry(**kwargs)
        widget.set_width_chars(10)
        ParameterWidget.__init__(self, widget, scope=scope, name=name,
                                 compact=compact)
        self.signal = gtklogger.connect(widget, 'changed', self.changedCB)
        val = value or param.value
        self.set_value(val)
        self.widgetChanged(self.validValue(val), interactive=0)
    def get_value(self):
        debug.mainthreadTest()
        text = self.gtk.get_text().lstrip()
        # Derived classes should redefine get_value() to do something
        # sensible, if possible, when there is no input.  They should
        # return None only if the input is invalid (which may or may
        # not be the same as having no input).
        if text:
            return utils.OOFeval(self.gtk.get_text())
        return None
    def set_value(self, newvalue):
        debug.mainthreadTest()
        valuestr = repr(newvalue)
        self.signal.block()
        self.gtk.set_text(valuestr)
        self.signal.unblock()
        self.gtk.set_position(0) # makes most significant digit visible
    def changedCB(self, gtkobj):
        debug.mainthreadTest()
        self.widgetChanged(self.validValue(self.gtk.get_text()), interactive=1)
    def validValue(self, value):
        # Redefine this in derived classes if necessary.  The argument
        # to validValue is the raw string returned from the widget.
        # It will be run through 'eval' before being used, so the
        # checking here shouldn't be too strict.  In most cases it's
        # sufficient to check that the string isn't empty.  ACTUALLY,
        # validValue is also called from the widget constructor, where
        # the value passed is *not* the raw string.  So validValue()
        # must accept either a raw string or an instance of the class
        # that the widget represents.  TODO LATER: This is rather
        # ugly, particularly in the subclasses.  This function should
        # either do the oofeval if it gets a string, or be broken up
        # into "validStringValue" and "validParameterValue" or
        # something similar.
        return value is not None and stringlstrip(value) != ""

    # GenericWidgets are sometimes included in other widgets with fake
    # parameters, which may need control over the emission of the
    # 'changed' signal.  (See matrixparamwidgets.py, for example.)
    # The need for these functions indicates that widgets *shouldn't*
    # be nested like this.  OTOH, blocking and unblocking are
    # cumulative, so a signal that's been blocked twice needs to be
    # unblocked twice before it's active again, which makes nesting
    # safe(r).
    def block_signal(self):
        debug.mainthreadTest()
        self.signal.block()
    def unblock_signal(self):
        debug.mainthreadTest()
        self.signal.unblock()

#########################

# StringParameter widget is almost a GenericWidget.
# It removes leading spaces from the result.

class StringWidget(GenericWidget):
    def get_value(self):
        debug.mainthreadTest()
        return self.gtk.get_text().lstrip()
    def set_value(self, value):
        debug.mainthreadTest()
        self.block_signal()
        if isinstance(value, StringType) and stringlstrip(value) != "":
            self.gtk.set_text(value)
            self.widgetChanged(1, interactive=0)
        else:
            self.gtk.set_text("")
            self.widgetChanged(0, interactive=0)
        self.unblock_signal()

def _StringParameter_makeWidget(self, scope=None, **kwargs):
    return StringWidget(self, scope=scope, name=self.name, **kwargs)

parameter.StringParameter.makeWidget = _StringParameter_makeWidget

class RestrictedStringWidget(StringWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        self.prog = param.prog  # compiled regular expression
        StringWidget.__init__(self, param, scope, name, **kwargs)
    def validValue(self, value):
        if self.prog.match(value):
            return StringWidget.validValue(self, value)
        return False

def _RSParam_makeWidget(self, scope=None, **kwargs):
    return RestrictedStringWidget(self, scope=scope,name=self.name, **kwargs)

parameter.RestrictedStringParameter.makeWidget = _RSParam_makeWidget
        
#########################

# If the user doesn't type anything in an AutoWidget, it displays
# self.autotext and its value is automatic.automatic.  The autotext is
# displayed in a distinctive style.  When the user types anything, the
# autotext is deleted and the style is changed back to the normal
# Gtk.Entry style.  When the user deletes everything in the Entry, the
# autotext and its style are restored.

# Style for displaying the autotext.  It should look different from
# what the user types.  It should *not* set the color unless we first
# check the theme's background color to make sure that the text is
# visible.
gtkutils.addStyle("entry.automatic { font-style: italic; }")

# This changes the text color for automatic widgets with keyboard focus:
#   gtkutils.addStyle("entry.automatic:focus { color: blue; }")
# BUT if we want to change the colors, we'd have to base the new colors on
# the colors for the current theme, which can be retrieved from the
# widget's StyleContext, eg:
#   widget.get_style_context().get_color(Gtk.StateFlags.NORMAL)
#   widget.get_style_context().get_background_color(Gtk.StateFlags.NORMAL)
# We'd also need to make sure to update the colors if the user changes
# the theme.  Gtk3 doesn't provide a good way to do this, since
# changing colors and such violates the spirit of CSS.

# We want to add a handler for the Gtk.Entry's 'insert_text' signal,
# but there's a bug in Gtk with regard to in/out parameters in python
# signal handlers, such as the 'position' parameter for the
# insert_text handler.  This can be avoided by deriving a new class
# from Gtk.Entry instead of using a handler.  See
# https://stackoverflow.com/questions/38815694/gtk-3-position-attribute-on-insert-text-signal-from-gtk-entry-is-always-0
# That site also 'explains' that it's necessary to derive the new
# class from both Gtk.Entry and Gtk.Editable, even though Gtk.Entry is
# itself derived from Gtk.Editable.

from ooflib.common.IO.GUI.gtklogger import findLogger, signalLogger

class AutomaticEntry(Gtk.Entry, Gtk.Editable):
    def __init__(self, *args, **kwargs):
        Gtk.Entry.__init__(self, *args, **kwargs)
        # super(AutomaticEntry, self).__init__(args, kwargs)
    def setAutoWidget(self, autowidget):
        # autowidget is the ParameterWidget that is using this
        # AutomaticEntry.
        self.autowidget = autowidget
        self.logger = gtklogger.findLogger(self)
    def do_insert_text(self, new_text, length, position):
        # If we used gtklogger to connect to the 'insert_text' signal,
        # it would call signalLogger() like this at about this point
        # in the proceedings:
        if isinstance(self.get_toplevel(), Gtk.Window):
            gtklogger.signalLogger(self, 'insert_text', self.logger,
                                   new_text, length, position)
        # Code that would be in the 'insert_text' handler if there
        # were one:
        if self.autowidget.automatic:
            self.autowidget.enterManualMode()
            self.get_buffer().set_text(new_text, len(new_text))
            newpos = len(new_text)
        else:
            # Code that is presumably in the base class do_insert_text()
            # method:
            self.get_buffer().insert_text(position, new_text, length)
            newpos = length + position
        # More code that should be in the 'insert_text' handler:
        self.autowidget.widgetChanged(
            self.autowidget.validValue(self.get_buffer().get_text()), True)
        return newpos

class AutoWidget(ParameterWidget):
    def __init__(self, param, scope=None, name=None,
                 compact=False,
                 value=None,
                 autotext=None, # text to display in automatic mode
                 **kwargs):
        debug.mainthreadTest()
        self.autotext = autotext or "<automatic>"
        self.stylecontext = None
        widget = AutomaticEntry(**kwargs)
        widget.setAutoWidget(self)
        widget.set_width_chars(10)
        ParameterWidget.__init__(self, widget, scope=scope, name=name,
                                 compact=compact)
        # We don't need to connect to the 'changed' signal because
        # we're handling 'insert_text' (sort of) and 'delete_text'.
        self.deleteSignal = gtklogger.connect(self.gtk, 'delete_text',
                                              self.deleteTextCB)

        val = value or param.value
        # Initialize self.automatic to the wrong value so that
        # set_value() will switch into the correct mode.
        self.automatic = val is not automatic.automatic
        self.set_value(val)
        self.widgetChanged(self.validValue(val), interactive=False)

    def set_value(self, newvalue):
        # If newvalue is not a string, the derived class might need to
        # override this method.  The derived class method should call
        # the base class method, passing a string or
        # automatic.automatic as newvalue.
        self.deleteSignal.block()
        try:
            if newvalue is automatic.automatic:
                if not self.automatic:
                    self.enterAutoMode()
            else:
                if self.automatic:
                    self.enterManualMode()
                if isinstance(newvalue, StringType):
                    self.gtk.set_text(newvalue)
                else:
                    self.gtk.set_text(repr(newvalue))
        finally:
            self.deleteSignal.unblock()
        self.widgetChanged(1, interactive=0)
        

    def deleteTextCB(self, gtkobj, start_pos, end_pos):
        # In automatic mode, deletion does nothing.
        if self.automatic:
            self.gtk.stop_emission_by_name("delete_text")
            return
        # In manual mode, deleting the last character switches to
        # automatic mode.
        if start_pos == 0 and (end_pos == -1 or
                               end_pos == self.gtk.get_text_length()):
            self.deleteSignal.block()
            try:
                self.enterAutoMode()
            finally:
                self.deleteSignal.unblock()
        else:
            # Just a normal deletion.
            self.gtk.get_buffer().delete_text(start_pos, end_pos-start_pos)

        self.gtk.stop_emission_by_name("delete_text")
        self.widgetChanged(self.validValue(self.get_value()),
                           interactive=True)
                
    def get_value(self):
        if self.automatic:
            return automatic.automatic
        return self.gtk.get_text()

    def validValue(self, value):
        # See comment in GenericWidget.validValue.
        return (value is automatic.automatic or
                (isinstance(value, StringType) and stringlstrip(value) != ""))

    def enterAutoMode(self):
        self.automatic = True
        self.gtk.get_style_context().add_class("automatic")
        # Don't use AutomaticEntry.set_text() here, because it will
        # call AutomaticEntry.do_insert_text() and switch back to
        # manual mode.
        self.gtk.get_buffer().set_text(self.autotext, len(self.autotext))
        self.gtk.set_position(-1)
        self.gtk.select_region(0, -1)

    def enterManualMode(self):
        self.automatic = False
        self.gtk.get_style_context().remove_class("automatic")


class AutoNameWidget(AutoWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        AutoWidget.__init__(self, param, scope=scope, name=name,
                            value=automatic.automatic,
                            **kwargs)
        # Avoid querying param.value here, as it will trigger the
        # autoname resolution process if the parameter is an
        # AutomaticNameParameter or ContextualNameParameter, and the
        # resolution may not be possible if the widget is just now
        # being constructed and the other widgets that it depends on
        # don't yet have values.
        if param.automatic():
            self.set_value(automatic.automatic)
            self.widgetChanged(1, interactive=0)
        else:
            self.set_value(param.truevalue)
            self.widgetChanged(self.validValue(param.truevalue), interactive=0)

def _AutoNameParameter_makeWidget(self, scope, **kwargs):
    return AutoNameWidget(self, scope=scope, name=self.name, **kwargs)
parameter.AutomaticNameParameter.makeWidget = _AutoNameParameter_makeWidget


class RestrictedAutoNameWidget(AutoNameWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        self.prog = param.prog  # compiled regular expression
        AutoNameWidget.__init__(self, param, scope, name)
    def validValue(self, value):
        if value is automatic.automatic:
            return True
        return (isinstance(value, StringType) and utils.stringstrip(value) != ""
                and self.prog.match(value))

def _RestrictedAutoNameParam_makeWidget(self, scope, **kwargs):
    return RestrictedAutoNameWidget(self, scope=scope, name=self.name, **kwargs)
parameter.RestrictedAutomaticNameParameter.makeWidget = \
                                         _RestrictedAutoNameParam_makeWidget
#########################

# Allows a value of "automatic", or an integer.
class AutoNumberWidget(AutoWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        AutoWidget.__init__(self, param, scope=scope, name=name, **kwargs)
        self.set_value(param.value)
        self.widgetChanged(1, interactive=0)

    # The AutoWidget get_value returns automatic or a string, or none.
    # If we get a string, evaluate it and return the result.
    def get_value(self):
        v = AutoWidget.get_value(self)
        if v==automatic.automatic:
            return v
        return utils.OOFeval(v)
        

def _AutoNumberWidget_makeWidget(self, scope, **kwargs):
    return AutoNumberWidget(self, scope=scope, name=self.name, **kwargs)

parameter.AutoIntParameter.makeWidget = _AutoNumberWidget_makeWidget

parameter.AutoNumericParameter.makeWidget = _AutoNumberWidget_makeWidget
    

#########################

class BooleanWidget(ParameterWidget):
    def __init__(self, param, scope=None, name=None, compact=False, **kwargs):
        debug.mainthreadTest()
        quargs = kwargs.copy()
        if param.value:
            labelstr = 'true'
        else:
            labelstr = 'false'
        if not compact:
            self.button = Gtk.CheckButton(label=labelstr)
        else:
            quargs.setdefault('halign', Gtk.Align.CENTER)
            quargs.setdefault('hexpand', True)
            quargs.setdefault('shadow_type', Gtk.ShadowType.NONE)
            self.button = Gtk.CheckButton()
        ParameterWidget.__init__(self, Gtk.Frame(**quargs), scope=scope,
                                 compact=compact)
        self.gtk.add(self.button)
        # name is assigned to the button, not the frame, because it's
        # the button that gets connected.
        gtklogger.setWidgetName(self.button, name)
        self.signal = gtklogger.connect(self.button, 'clicked', self.buttonCB)
        self.set_value(param.value)
    def get_value(self):
        debug.mainthreadTest()
        return self.button.get_active()
    def set_value(self, newvalue):
        debug.mainthreadTest()
        self.signal.block()
        if newvalue:
            self.button.set_active(1)
        else:
            self.button.set_active(0)
        self.signal.unblock()
        self.widgetChanged(1, interactive=0)
    def buttonCB(self, obj):
        debug.mainthreadTest()
        if not self.compact:
            if self.button.get_active():
                self.button.set_label('true')
            else:
                self.button.set_label('false')
        self.widgetChanged(1, interactive=1)
    def block_signal(self):
        debug.mainthreadTest()
        self.signal.block()
    def unblock_signal(self):
        debug.mainthreadTest()
        self.signal.unblock()

def _Boolean_makeWidget(self, scope, compact=False, **kwargs):
    return BooleanWidget(self, scope=scope, name=self.name, compact=compact,
                         **kwargs)
parameter.BooleanParameter.makeWidget = _Boolean_makeWidget

##########################

from ooflib.common.IO.GUI import labelledslider

# The order of the base classes for IntRangeWidget and
# FloatRangeWidget is important.  All of the base classes define
# parameterTableXRef, but the one in ParameterWidget is just a stub.

class IntRangeWidget(labelledslider.IntLabelledSlider, ParameterWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        if param.value is not None:
            val = param.value
        else:
            val = param.range[0]
        labelledslider.IntLabelledSlider.__init__(
            self, val,
            vmin=param.range[0], vmax=param.range[1], step=1,
            callback=self.sliderCB, **kwargs)
        ParameterWidget.__init__(self, self.gtk, scope=scope, name=name)
        self.widgetChanged(self.consistent(), interactive=0)
    def sliderCB(self, slider, val):
        debug.mainthreadTest()
        self.widgetChanged(self.consistent(), interactive=1)

def _IntRange_makeWidget(self, scope, **kwargs):
    return IntRangeWidget(self, scope=scope, name=self.name, **kwargs)

parameter.IntRangeParameter.makeWidget = _IntRange_makeWidget


class FloatRangeWidget(labelledslider.FloatLabelledSlider, ParameterWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        if param.value is not None:
            val = param.value
        else:
            val = param.range[0]
        labelledslider.FloatLabelledSlider.__init__(
            self, val,
            vmin=param.range[0], vmax=param.range[1], step=param.range[2],
            callback=self.sliderCB, **kwargs)
        ParameterWidget.__init__(self, self.gtk, scope=scope, name=name)
        self.widgetChanged(self.consistent(), interactive=0)
    ## FloatRangeWidget uses LabelledSlider's get_value()
    def sliderCB(self, slider, val):
        debug.mainthreadTest()
        self.widgetChanged(self.consistent(), interactive=1)

def _FloatRange_makeWidget(self, scope=None, **kwargs):
    return FloatRangeWidget(self, scope=scope, name=self.name, **kwargs)
parameter.FloatRangeParameter.makeWidget = _FloatRange_makeWidget

########

# The AngleRangeWidget is used to set an angle variable.  If the
# allowed range of the variable covers a full circle, values outside
# of the nominal range should be mapped back inside it by adding or
# subtracting multiples of 2*pi or 360, instead of clipping to the
# numerical limits of the range.  The clipper used by the
# LabelledSlider needs to know if the range is given in degrees or
# radians, so we need an extra class to store the units.

class _AngleClipper:
    def __init__(self, vmin, vmax, circle):
        self.vmin = vmin
        self.vmax = vmax
        self.circle = circle    # either 360 or 2*pi
    def clip(self, val):
        if self.vmin > val:
            n = math.ceil((self.vmin - val)/self.circle)
            val += n*self.circle
        elif val > self.vmax:
            n = math.ceil((val - self.vmax)/self.circle)
            val -= n*self.circle
        if val < self.vmin or val > self.vmax:
            raise ValueError("Parameter value out of range: val=" + repr(val)
                             + " range=[" + repr(self.vmin) + ", " + repr(self.vmax)
                             + "]")
        return val

class _ClipperFactory:
    def __init__(self, circle):
        self.circle = circle    # either 360 or 2*pi
    def __call__(self, vmin, vmax):
        return _AngleClipper(vmin, vmax, self.circle)

class AngleRangeWidget(labelledslider.FloatLabelledSlider, ParameterWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        if param.value is not None:
            val = param.value
        else:
            val = param.range[0]
        labelledslider.FloatLabelledSlider.__init__(
            self, val,
            vmin=param.range[0],
            vmax=param.range[1],
            step=param.range[2],
            callback=self.sliderCB,
            clipperclass=_ClipperFactory(param.circle),
            **kwargs)
        ParameterWidget.__init__(self, self.gtk, scope=scope, name=name)
        self.widgetChanged(1, interactive=0)
        
    def sliderCB(self, slider, val):
        self.widgetChanged(1, interactive=1)

def _AngleRange_makeWidget(self, scope, **kwargs):
    return AngleRangeWidget(self, scope=scope, name=self.name, **kwargs)

parameter.AngleRangeParameter.makeWidget = _AngleRange_makeWidget
        

##############################################

class FloatWidget(GenericWidget):
    def __init__(self, param, scope=None, name=None, compact=False, **kwargs):
        GenericWidget.__init__(self, param=param, scope=scope, name=name,
                               compact=compact, **kwargs)
        if compact:
            self.gtk.set_width_chars(8)
    def get_value(self):
        x = GenericWidget.get_value(self)
        if x is not None:
            # This doesn't have to convert the data to a Float,
            # because the GenericWidget eval's its input.
            return x
        return 0.0
    def validValue(self, val):
        try:
            if isinstance(val, StringType):
                return isinstance(1.0*utils.OOFeval(val), FloatType)
            else:
                return isinstance(val, (FloatType, IntType))
        except:
            return False
    def set_value(self, newvalue):
        GenericWidget.set_value(self, 1.0*newvalue)

def _FloatParameter_makeWidget(self, scope=None, compact=False, **kwargs):
    return FloatWidget(self, scope=scope, name=self.name, compact=compact,
                       **kwargs)
parameter.FloatParameter.makeWidget = _FloatParameter_makeWidget

class PositiveFloatWidget(FloatWidget):
    def validValue(self, val):
        debug.fmsg("val=", val, type(val))
        try:
            if isinstance(val, StringType):
                fval = 1.0*utils.OOFeval(val)
                return isinstance(fval, FloatType) and fval > 0.0
            else:
                return isinstance(val, (FloatType, IntType)) and val > 0.0
        except:
            return False

def _PositiveFloatParameter_makeWidget(self, scope=None, **kwargs):
    return PositiveFloatWidget(self, scope=scope, name=self.name, **kwargs)
parameter.PositiveFloatParameter.makeWidget = _PositiveFloatParameter_makeWidget

class ListOfFloatsWidget(GenericWidget):
    # See comments in FloatWidget
    def get_value(self):
        x = GenericWidget.get_value(self)
        if x is not None:
            return x
        return []
    def validValue(self, *args):
        return 1

def _ListOfFloatsParameter_makeWidget(self, scope=None, **kwargs):
    return ListOfFloatsWidget(self, scope=scope, name=self.name, **kwargs)
parameter.ListOfFloatsParameter.makeWidget = _ListOfFloatsParameter_makeWidget

#########################

class IntWidget(GenericWidget):
    def __init__(self, param, scope=None, name=None, compact=False, **kwargs):
        GenericWidget.__init__(self, param=param, scope=scope, name=name,
                               compact=compact, **kwargs)
        if compact:
            self.gtk.set_width_chars(8)
    # See comments in FloatWidget
    def get_value(self):
        x = GenericWidget.get_value(self)
        if x is not None:
            return x
        return 0
    def validValue(self, val):
        try:
            if isinstance(val, StringType):
                return isinstance(utils.OOFeval(val), IntType)
            else:
                return isinstance(val, IntType)
        except:
            return False
def _IntParameter_makeWidget(self, scope=None, **kwargs):
    return IntWidget(self, scope=scope, name=self.name, **kwargs)

parameter.IntParameter.makeWidget = _IntParameter_makeWidget

class PositiveIntWidget(IntWidget):
    def validValue(self, val):
        try:
            if isinstance(val, StringType):
                ival = utils.OOFeval(val)
                return isinstance(ival, IntType) and ival > 0
            else:
                return isinstance(val, IntType) and val > 0
        except:
            return False

def _PositiveIntParameter_makeWidget(self, scope=None, **kwargs):
    return PositiveIntWidget(self, scope=scope, name=self.name, **kwargs)
parameter.PositiveIntParameter.makeWidget = _PositiveIntParameter_makeWidget

#######################

class XYStrFunctionWidget(GenericWidget):
    def get_value(self):
        debug.mainthreadTest()
        return strfunction.XYStrFunction(self.gtk.get_text().lstrip())
    def set_value(self, newvalue):
        debug.mainthreadTest()
        self.block_signal()
        if newvalue is not None:
            self.gtk.set_text(newvalue.funcstr)
        else:
            self.gtk.set_text('')
        self.unblock_signal()
    def validValue(self, value):
        if isinstance(value, StringType):
            try:
                fn = strfunction.XYStrFunction(value)
                return True
            except:
                return False
        return isinstance(value, strfunction.XYStrFunction)
            
def _XYStrFunctionParameter_makeWidget(self, scope=None, **kwargs):
    return XYStrFunctionWidget(self, scope=scope, name=self.name, **kwargs)
        
strfunction.XYStrFunctionParameter.makeWidget = \
                                              _XYStrFunctionParameter_makeWidget

class XYTStrFunctionWidget(GenericWidget):
    def get_value(self):
        debug.mainthreadTest()
        return strfunction.XYTStrFunction(self.gtk.get_text().lstrip())
    def set_value(self, newvalue):
        debug.mainthreadTest()
        self.block_signal()
        if newvalue is not None:
            self.gtk.set_text(newvalue.funcstr)
        else:
            self.gtk.set_text('')
        self.unblock_signal()
    def validValue(self, value):
        if isinstance(value, StringType):
            try:
                fn = strfunction.XYTStrFunction(value)
                return True
            except:
                return False
        return isinstance(value, strfunction.XYTStrFunction)
            
def _XYTStrFunctionParameter_makeWidget(self, scope=None, **kwargs):
    return XYTStrFunctionWidget(self, scope=scope, name=self.name, **kwargs)
        
strfunction.XYTStrFunctionParameter.makeWidget = \
                                           _XYTStrFunctionParameter_makeWidget

############################################

class ParameterTable(ParameterWidget, widgetscope.WidgetScope):
    # A table of Parameter Widgets
    def __init__(self, params, scope=None, name=None, showLabels=True, data={},
                 **kwargs):
        debug.mainthreadTest()
        widgetscope.WidgetScope.__init__(self, scope)
        for key, value in data.items():
            self.setData(key, value)
        self.params = params            # list of Parameters
        if self.params:
            quargs = kwargs.copy()
            quargs.setdefault('margin', 2)
            quargs.setdefault('row_spacing', 2)
            quargs.setdefault('column_spacing', 2)
            base = Gtk.Grid(**quargs)
        else:
            # There are no parameters.  The 'table' needs to be a
            # wiget but it should take up no space, so don't pass any
            # kwargs to it, since they might set margins.
            base = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, vexpand=False)
            base.set_size_request(-1, 0) # overkill
        ParameterWidget.__init__(self, base, scope, name)
        self.showLabels = showLabels
        self.labels = []
        self.widgets = []
        self.sbcallbacks = []           # switchboard callbacks
        self.subscopes = []             # Widgetscopes for ParameterGroups
        self.set_values()
        self.show()

    def set_values(self):
        self.labels = []
        for widget in self.widgets:
            widget.destroy()
        self.widgets = []
        self.validities = [0]*len(self.params)
        self.destroySubScopes()
        self.makeWidgets()
        self.show()
        self.signal(interactive=False)

    def makeWidgets(self):
        debug.mainthreadTest()
        subscopedict = {}
        self.expandable = False
        for i, param in enumerate(self.params):
            if param.group is None:
                scope = self
            else:
                # Get or make a WidgetScope for this ParameterGroup
                try:
                    scope = subscopedict[param.group]
                except KeyError:
                    scope = widgetscope.WidgetScope(self)
                    self.subscopes.append(scope)
                    subscopedict[param.group] = scope
            self.makeSingleWidget(param, i, scope)
        # Allow widgets to synchronize themselves, if they so desire.
        for widget in self.widgets:
            widget.parameterTableXRef(self, self.widgets)

    def makeSingleWidget(self, param, tablepos, scope):
        debug.mainthreadTest()
        
        widget = param.makeWidget(scope=scope, halign=Gtk.Align.FILL,
                                  hexpand=True, margin_start=2, margin_end=2)
        self.widgets.append(widget)

        self.sbcallbacks += [
            switchboard.requestCallbackMain(('validity', widget), self.vcheck,
                                            tablepos),
            switchboard.requestCallbackMain(widget, self.widgetChangeCB)
            ]
        self.validities[tablepos] = widget.isValid()
        
        label = Gtk.Label(label=param.name + ' =', halign=Gtk.Align.END,
                          hexpand=False, margin_start=5)
        self.labels.append(label)
        if param.tip:
            label.set_tooltip_text(param.tip)
        if widget.expandable:
            widget.gtk.set_vexpand(True)
            widget.gtk.set_valign(Gtk.Align.FILL)
            label.set_vexpand(True)
            label.set_valign(Gtk.Align.FILL)
            self.expandable = True
        if self.showLabels:
            self.gtk.attach(label, 0,tablepos, 1,1)
        self.gtk.attach(widget.gtk, 1,tablepos, 1,1)
        
    def get_values(self):
        debug.mainthreadTest()
        exceptions = []
        for param, widget in zip(self.params, self.widgets):
            # Get as many values as possible, even if setting some of them
            # causes errors.
            try:
                val = widget.get_value()
                param.value = val
            except Exception as exception:
                exceptions.append(exception)
        if exceptions:
            debug.fmsg("exceptions[0] ->%s<-", exceptions[0])
            raise exceptions[0]
    def vcheck(self, widgetnumber, validity):
        # callback for ('validity', widget).  This just stores the
        # validity value.  The subsequent widget changed switchboard
        # call actually broadcasts the new validity by calling
        # widgetChanged.
        self.validities[widgetnumber] = validity
    def widgetChangeCB(self, interactive):
        self.signal(interactive)
    def signal(self, interactive):
        for v in self.validities:
            if not v:
                self.widgetChanged(False, interactive)
                return
        self.widgetChanged(True, interactive)
    def dumpValidity(self):
        debug.fmsg(list(zip([p.name for p in self.params], self.validities)))
    def dumpValues(self):
        debug.fmsg(*["%s=%s" % (p.name, p.value) for p in self.params])
    def dumpState(self, comment):
        for widget in self.widgets:
            try:
                widget.dumpState("   " + comment)
            except AttributeError:
                pass
    def show(self):
        # Don't simply run self.gtk.show_all(), because it might show
        # too much of some child widgets.
        debug.mainthreadTest()
        for widget in self.widgets:
            widget.show()
        for label in self.labels:
            label.show_all()
        self.gtk.show()
    def cleanUp(self):
        # Make sure we don't have any circular references...
        switchboard.removeCallbacks(self.sbcallbacks)
        self.params = []
        self.widgets = []
        ParameterWidget.cleanUp(self)
        self.destroyScope()
        self.destroySubScopes()
    def destroySubScopes(self):
        for scope in self.subscopes:
            scope.destroyScope()
        self.subscopes = []


class HierParameterTable(ParameterTable):
    # ParameterTable that takes a hierarchical list of Parameters, and
    # puts them in a table with WidgetScopes defined for each level of
    # the hierarchy.  The hierarchical list is just a list of lists of
    # lists of Parameters, with arbitrarily deep nesting.
    ## TODO: Is this necessary, now that ParameterGroups can be nested?
    def __init__(self, params, scope=None, **kwargs):
        self.paramhier = params
        ParameterTable.__init__(self, utils.flatten_all(params), scope,
                                **kwargs)
    def makeWidgets(self):
        debug.mainthreadTest()
        tablepos = 0
        self._doMakeWidgets(self, tablepos, self.paramhier)
    def _doMakeWidgets(self, scope, tablepos, phier):
        for obj in phier:  
            if isinstance(obj, parameter.Parameter):
                self.makeSingleWidget(obj, tablepos, scope)
                tablepos += 1
            else:                       # obj is a hierarchical list of params
                # Only thing to phier is phier itself...
                subscope = widgetscope.WidgetScope(scope)
                tablepos = self._doMakeWidgets(subscope, tablepos, obj)
        return tablepos
                
#####################################################################

# Modal dialog for setting Parameters

class ParameterDialog(widgetscope.WidgetScope):
    def __init__(self, *parameters, **kwargs):
        debug.mainthreadTest()
        # A title for the dialog box can be specified by a REQUIRED
        # 'title' keyword argument.  A WidgetScope can be specified
        # with a 'scope' keyword.  If a parent window is specified
        # with the 'parentwindow' argument, the dialog will be brought
        # up as a transient window for it.

        parentwindow = kwargs['parentwindow'] # required!
        assert isinstance(parentwindow, Gtk.Window)

        scope = kwargs.get('scope', None)
        widgetscope.WidgetScope.__init__(self, scope)

        try:
            data_dict = kwargs['dialog_data']
        except KeyError:
            pass
        else:
            self.__dict__.update(data_dict)

        try:
            scopedata = kwargs['data']
        except KeyError:
            pass
        else:
            for key,value in scopedata.items():
                self.setData(key, value)
            
        self.parameters = parameters
        self.dialog = gtklogger.Dialog(modal=True,
                                       transient_for=parentwindow,
                                       border_width=3)
        # Window.set_keep_above is not guaranteed to work, but it won't hurt.
        # https://developer.gnome.org/gtk3/stable/GtkWindow.html#gtk-window-set-keep-above
        self.dialog.set_keep_above(True) 
        
        try:
            title = kwargs['title']
        except KeyError:
            raise ooferror.PyErrPyProgrammingError("Untitled dialog!")
        gtklogger.newTopLevelWidget(self.dialog, 'Dialog-'+kwargs['title'])
        self.dialog.set_title(title)

        # The gtk2 version had code here that put an hbox containing
        # the dialog's title at the top of the dialog's content area.
        # But show_all was never called on it, so it never appeared.
        # Apparently it wasn't necessary.

        # Create buttons in the action area.  This can be overridden
        # in derived classes.
        self._button_hook()

        self.table = ParameterTable(parameters, scope=self, hexpand=True,
                                    halign=Gtk.Align.FILL)
        self.sbcallback = switchboard.requestCallbackMain(
            ('validity', self.table),
            self.validityCB)
        vbox = self.dialog.get_content_area()
        vbox.pack_start(self.table.gtk, expand=self.table.expandable,
                        fill=True, padding=5)
        self.response = None
        self.sensitize()

    # _button_hook installs OK and Cancel buttons.  Override in
    # derived classes if other buttons are needed in the dialog's
    # action area.
    def _button_hook(self):
        debug.mainthreadTest()
        okbutton = gtkutils.StockButton('gtk-ok', 'OK')
        self.dialog.add_action_widget(
            okbutton,
            Gtk.ResponseType.OK)
        ## TODO: The following three lines sometimes seem to suffice
        ## to connect the Enter key with the OK button, as long as
        ## button.set_receives_default(False) is called for any
        ## buttons in the content area and the content area contains
        ## no Gtk.Entrys. Sometimes it generates
        ##  Gtk-CRITICAL: gtk_widget_grab_default: assertion 'gtk_widget_get_can_default (widget)' failed
        ## Obviously we don't understand how to do this properly.
        okbutton.set_can_default(True)
        okbutton.set_receives_default(True)
        okbutton.grab_default()
        
        self.dialog.add_action_widget(
            gtkutils.StockButton('gtk-cancel', 'Cancel'),
            Gtk.ResponseType.CANCEL)
 
    def run(self):
        debug.mainthreadTest()
        self.table.show()
        # TODO: Dialog.show_all() is unsafe if some of the widgets
        # have subwidgets that aren't ready to be shown.  We used to
        # use dialog.get_action_area().show_all(), but get_action_area
        # is deprecated in Gtk+3.  Maybe we need to keep track of the
        # widgets in the action area and show them
        # individually. Probably the better solution is to make sure
        # that all widgets can tolerate show_all(), by adding and
        # removing subwidgets instead of showing and hiding them.
        self.dialog.show_all()
        return self.dialog.run()        # shows dialog & makes it modal
    def close(self):
        debug.mainthreadTest()
        switchboard.removeCallback(self.sbcallback)
        self.dialog.destroy()
        self.destroyScope()
    def get_values(self):
        self.table.get_values()
    def validityCB(self, validity):     # sb callback from ParameterTable
        self.sensitize()
    def sensitize(self):
        debug.mainthreadTest()
        self.dialog.set_response_sensitive(Gtk.ResponseType.OK,
                                           self.table.isValid())
    def hide(self):
        debug.mainthreadTest()
        self.dialog.hide()

def getParameters(*params, **kwargs):
    # Given a bunch of Parameters, create a dialog box for setting
    # them.  If the function returns 1, then the parameters have been
    # set and their values can be extracted by the calling routine.
    # kwargs can contain 'title', 'scope', and 'data' arguments.
    # 'data' is a dict of values to be stored as the dialog's
    # widgetscope's data.  See WidgetScope.setData.
    dialog = ParameterDialog(*params, **kwargs)

    result = dialog.run()
    
    if result in (Gtk.ResponseType.CANCEL,
                  Gtk.ResponseType.DELETE_EVENT,
                  Gtk.ResponseType.NONE):
        dialog.close()
        return None
    try:
        dialog.get_values()
        return 1
    finally:
        dialog.close()


def getParameterValues(*params, **kwargs):
    # This version of getParameters extracts and returns the Parameter
    # values, or returns None if they haven't been set. kwargs can
    # contain 'title' and 'scope' arguments.
    if getParameters(*params, **kwargs):
        return [p.value for p in params]

#####################################################################

class PersistentParameterDialog(ParameterDialog):
    # OK = 1
    # APPLY = 2
    # CANCEL = 3
    def _button_hook(self):
        debug.mainthreadTest()
        okbutton = gtkutils.StockButton('gtk-ok', 'OK')
        self.dialog.add_action_widget(
            okbutton,
            Gtk.ResponseType.OK)
        # See comment in ParameterDialog._button_hook
        okbutton.set_can_default(True)
        okbutton.set_receives_default(True)
        okbutton.grab_default()

        self.dialog.add_action_widget(
            gtkutils.StockButton('gtk-apply', 'Apply'),
            Gtk.ResponseType.APPLY)
        self.dialog.add_action_widget(
            gtkutils.StockButton('gtk-cancel', 'Cancel'),
            Gtk.ResponseType.CANCEL)
        self.dialog.set_default_response(Gtk.ResponseType.OK)
        
    def sensitize(self):
        debug.mainthreadTest()
        ParameterDialog.sensitize(self)
        self.dialog.set_response_sensitive(Gtk.ResponseType.APPLY,
                                           self.table.isValid())

# This function passes the params and kwargs on to a persistent
# parameter dialog box, which it leaves up until it gets OK or some
# cancellation event.  Any affirmative event (OK or APPLY) cause the
# passed-in menu item to be run with the provided defaults, via
# menuitem.callWithDefaults(**defaults).  OK events close the dialog,
# APPLY events cause the dialog to persist.
def persistentMenuitemDialog(menuitem, defaults,
                             *params, **kwargs):
    rerun = True
    count = 0
    dialog = PersistentParameterDialog(*params, **kwargs)
    while rerun:
        result = dialog.run()
        if result in (Gtk.ResponseType.CANCEL,
                      Gtk.ResponseType.DELETE_EVENT,
                      Gtk.ResponseType.NONE):
            rerun = False
        elif result==Gtk.ResponseType.OK:
            try:
                dialog.get_values()
            finally:
                rerun = False
            menuitem.callWithDefaults(**defaults)
            count += 1
        else: #  result==Gtk.ResponseType.APPLY
            dialog.get_values()
            menuitem.callWithDefaults(**defaults)
            count += 1
    dialog.close()
    
    return count

def transientMenuItemDialog(menuitem, defaults, parentwindow,
                            *params, **kwargs):
    dialog = ParameterDialog(parentwindow=parentwindow, *params, **kwargs)
    result = dialog.run()
    if result == Gtk.ResponseType.OK:
        dialog.get_values()
        menuitem.callWithDefaults(**defaults)
    dialog.close()

#####################################################################

from ooflib.common.IO.GUI import chooser

# Widget base class for subclasses of the Enum class.
class EnumWidget(ParameterWidget):
    def __init__(self, enumclass, param, scope=None, name=None, **kwargs):
        self.enumclass = enumclass
        nameset = list(self.enumclass.names)
        self.widget = chooser.ChooserWidget(nameset, self.selection,
                                            helpdict=self.enumclass.helpdict,
                                            name=name, **kwargs)
        if param.value is not None:
            self.set_value(param.value)
        else:
            self.set_value(enumclass(enumclass.names[0]))
        self.sbcallback = switchboard.requestCallbackMain(enumclass,
                                                          self.update)
        ParameterWidget.__init__(self, self.widget.gtk, scope=scope)
        self.widgetChanged(len(nameset) > 0, interactive=0)
    def update(self):
        self.widget.update(list(self.enumclass.names), self.enumclass.helpdict)
        self.widgetChanged(len(self.enumclass.names) > 0, interactive=0)
    def selection(self, name):
        self.value = self.enumclass(name)
        self.widgetChanged(validity=1, interactive=1)
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
        self.widget.set_state(value.name)
    def cleanUp(self):
        switchboard.removeCallback(self.sbcallback)
        ParameterWidget.cleanUp(self)
    
def _EnumParameter_makeWidget(self, scope=None, **kwargs):
    return EnumWidget(self.enumclass, self, scope=scope, name=self.name,
                      **kwargs)

enum.EnumParameter.makeWidget = _EnumParameter_makeWidget


#######################################################################

# ValueSetParameter is valid if it's a nontrivial string, or if
# it's a positive integer, or if it's a tuple of things that can
# be converted to floats.
class ValueSetParameterWidget(GenericWidget):
    def validValue(self, value):
        if value is None:
            return 0
        if isinstance(value, StringType):
            if stringlstrip(value)=="":
                return 0
            return 1 # Nontrival strings are OK.
        
        if isinstance(value, IntType) and value>0:
            return 1 # Ints greater than zero are OK.

        if isinstance(value, TupleType):
            for v in value:
                try:
                    x = float(v)
                except ValueError:
                    return 0
            return 1


def _makeVSPWidget(self, scope=None, **kwargs):
    return ValueSetParameterWidget(self, scope=scope, name=self.name, **kwargs)

parameter.ValueSetParameter.makeWidget = _makeVSPWidget

class AutomaticValueSetParameterWidget(AutoWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        AutoWidget.__init__(self, param, scope=scope, name=name, **kwargs)
        self.set_value(param.value)

    def validValue(self, value):
        if value is None:
            return 0
        if isinstance(value, StringType):
            if stringlstrip(value)=="":
                return 0
            return 1
        
        if isinstance(value, IntType) and value>0:
            return 1

        if value == automatic.automatic:
            return 1

        if isinstance(value, TupleType):
            for v in value:
                try:
                    x = float(v)
                except ValueError:
                    return 0
            return 1

    # Similarly to the AutoNumber widget, if we don't get automatic,
    # we should evaluate our text-string to get a result.
    def get_value(self):
        v = AutoWidget.get_value(self)
        if v==automatic.automatic:
            return v
        return utils.OOFeval(v)

def _makeAVSPWidget(self, scope=None, **kwargs):
    return AutomaticValueSetParameterWidget(self, scope=scope, name=self.name,
                                            **kwargs)

parameter.AutomaticValueSetParameter.makeWidget = _makeAVSPWidget

#######################################################################

class PointWidget(ParameterWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        debug.mainthreadTest()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                       **kwargs)
        xlabel = Gtk.Label(label="x:", halign=Gtk.Align.END)
        self.xwidget = FloatWidget(parameter.FloatParameter('Tweedledum', 0),
                                   name="X")
        ylabel = Gtk.Label(label="y:", halign=Gtk.Align.END)
        self.ywidget = FloatWidget(parameter.FloatParameter('Tweedledee', 0),
                                   name="Y")
        hbox.pack_start(xlabel, expand=False, fill=False, padding=0)
        hbox.pack_start(self.xwidget.gtk, expand=True, fill=True, padding=0)
        hbox.pack_start(ylabel, expand=False, fill=False, padding=0)
        hbox.pack_start(self.ywidget.gtk, expand=True, fill=True, padding=0)
        self.sbcallbacks=[
            switchboard.requestCallbackMain(self.xwidget,
                                            self.widgetChangeCB),
            switchboard.requestCallbackMain(self.ywidget,
                                            self.widgetChangeCB)
            ]
        ParameterWidget.__init__(self, hbox, scope=scope, name=name)
        self.set_value(param.value)
        self.widgetChanged(self.xwidget.isValid() and self.ywidget.isValid(),
                           interactive=0)
    def set_value(self, point):
        self.xwidget.set_value(point.x)
        self.ywidget.set_value(point.y)
    def get_value(self):
        return primitives.Point(self.xwidget.get_value(),
                                self.ywidget.get_value())
    def widgetChangeCB(self, interactive):
        self.widgetChanged(self.xwidget.isValid() and self.ywidget.isValid(),
                           interactive)
    def cleanUp(self):
        switchboard.removeCallbacks(self.sbcallbacks)
        ParameterWidget.cleanUp(self)

def _PointParameter_makeWidget(self, scope=None, **kwargs):
    return PointWidget(self, scope=scope, name=self.name, **kwargs)

primitives.PointParameter.makeWidget = _PointParameter_makeWidget
 
