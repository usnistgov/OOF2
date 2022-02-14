# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common import debug
from ooflib.common import utils
from ooflib.common.IO.GUI import gtklogger
from gi.repository import Gtk
import sys

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Each LabelledSlider has a clipper that says what to do with values
# that are outside of the slider's range.  The default clipper just
# pegs the value to the beginning or end of the range.

# A clipper must have a __call__() method that returns an object with
# a clip() method.  __call__ takes two arguments, the min and max of
# the range.  clip() takes one argument, the value to be clipped.  It
# returns the value that should be used instead.

# The clipper can either be a single class that sets the range in its
# __init__ and has a clip method, or an instance of class whose
# __call__ method returns an instance of a second class that has a
# clip method.  See AngleClipper in common/IO/GUI/parameterwidgets.py
# for an example.

# This extra complexity is required because the LabelledSlider needs
# to be able to reset its range, which requires changing the range of
# the clipper.

## TODO: When the Gtk.Entry loses focus, should it clip?  Currently
## one can type an out of bounds value into the entry, and it isn't
## replaced with the clipped value until the parameterwidget is
## evaluated.

class DefaultClipper:
    def __init__(self, vmin, vmax):
        self.vmin = vmin
        self.vmax = vmax
    def clip(self, val):
        val = min(val, self.vmax)
        val = max(val, self.vmin)
        return val

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class LabelledSlider:
    def __init__(self, value=None, vmin=0, vmax=1, step=0.01, callback=None,
                 clipperclass=None,
                 name=None, immediate=True, logPaned=True,
                 **kwargs):
        # "callback" is called when the user moves the slider.  If
        # immediate==True, then the callback will be called when any
        # character is typed in the Entry.  If it's false, the
        # callback won't be called until the entry loses focus.

        # If logPaned is True, gtklogger will log changes in the
        # position of the GtkPaned that separates the slider from the
        # text area.  If multiple sliders' panes are synchronized,
        # logPaned should be True for just one of them.
        debug.mainthreadTest()
        self.immediate = immediate

        self.gtk = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL, **kwargs)
        if logPaned:
            gtklogger.connect_passive(self.gtk, 'notify::position')
        if value is None:
            value = vmin
        self.clipperclass = clipperclass or DefaultClipper
        self.clipper = self.clipperclass(vmin, vmax)
        if name is not None:
            gtklogger.setWidgetName(self.gtk, name)
        # TODO: Does setting page_size=0 cause problems for some gtk
        # themes, if the sliding part of the Gtk.Scale gets its size
        # from page_size?
        self.adjustment = Gtk.Adjustment(
            value=value, lower=vmin, upper=vmax,
            step_incr=step, # arrow keys move this far
            page_incr=step, # page up and page down keys move this far
            page_size=0)    # max slider value is upper-page_size
        self.slider = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL,
                                adjustment=self.adjustment)
        gtklogger.setWidgetName(self.slider, "slider")
        gtklogger.adoptGObject(self.adjustment, self.slider,
                              access_method=self.slider.get_adjustment)
        self.slider.set_size_request(100, -1)
        self.gtk.pack1(self.slider, resize=True, shrink=False)
        self.slider.set_draw_value(False)   # we'll display the value ourselves
        self.adjustmentsignal = gtklogger.connect(self.adjustment,
                                                  'value-changed',
                                                  self.text_from_slider)

        self.entry = Gtk.Entry()
        self.entry.set_margin_start(3)
        self.entry.set_margin_end(3)
        gtklogger.setWidgetName(self.entry, "entry")
        self.gtk.pack2(self.entry, resize=True, shrink=False)

        # Make sure that the Entry is big enough to hold the min and
        # max values, or at least 8 digits.
        width = max(len(repr(vmin)), len(repr(vmax)), 8)
        self.entry.set_width_chars(width)

        self.entrysignal = gtklogger.connect(self.entry, 'changed',
                                             self.entry_changed)
        self.set_value(value)
        self.callback = callback
        self.changed = False

        gtklogger.connect(self.entry, 'activate', self.slider_from_text)
        gtklogger.connect(self.entry, 'focus_out_event', self.entry_lost_focus)

    def set_sensitive(self, sensitivity):
        self.slider.set_sensitive(sensitivity)
        self.entry.set_sensitive(sensitivity)

    def set_value(self, value):
        # set_value is called by the API, not the GUI, so it should
        # never call the callback function.
        debug.mainthreadTest()
        self.changed = False
        value = self.clipper.clip(value)
        self.adjustmentsignal.block()
        self.entrysignal.block()
        try:
            self.slider.set_value(value)
            self.set_entry(value)
            self.inconsistent = False
        except:
            self.inconsistent = True
        finally:
            self.adjustmentsignal.unblock()
            self.entrysignal.unblock()
            
    def text_from_slider(self, obj):
        debug.mainthreadTest()
        val = self.slider.get_value()
        self.entrysignal.block()
        try:
            self.set_entry(val)
        finally:
            self.entrysignal.unblock()
        self.entry.set_position(0)
        self.changed = False
        if self.callback:
            self.callback(self, val)
    def slider_from_text(self, obj):    # callback for 'activate' from GtkEntry
        debug.mainthreadTest()
        try:
            v0 = self.get_value()
        except:
            # The value in the entry is illegal. Maybe the entry is
            # empty.  We need to call the callback anyway, in case
            # someone needs to know that the widget is in an
            # inconsistent state.
            if self.callback:
                self.inconsistent = True
                self.callback(self, None)
        else:
            self.changed = False
            self.inconsistent = False
            val = self.clipper.clip(v0)
            self.adjustmentsignal.block()
            try:
                self.adjustment.set_value(val)
            finally:
                self.adjustmentsignal.unblock()
            if self.callback:
                self.callback(self, val)
    def entry_lost_focus(self, obj, event):
        if self.changed:
            # get_value returns the current value of the entry, which
            # may be out of bounds if the user is fooling around.
            # set_value clips the value to the correct bounds and sets
            # both the entry and the slider.
            self.set_value(self.get_value())
            # self.slider_from_text(obj)
    def entry_changed(self, obj): # gtk callback for self.entry 'changed'
        if self.immediate:
            self.slider_from_text(obj)
        else:
            self.changed = True
    def parameterTableXRef(self, ptable, widgets):
        # Called after a LabelledSlider has been placed in a
        # ParameterTable.  All of the LabelledSliders in the table
        # should have their HPaned adjustments synchronized.
        self.syncsignals = [self.gtk.connect('notify', widget._syncothers)
                            for widget in widgets
                            if (isinstance(widget, LabelledSlider)
                                and widget is not self)]

    def _syncothers(self, pane, gparamspec):
        if gparamspec.name == 'position':
            pos = pane.get_property('position')
            for signal in self.syncsignals:
                self.gtk.handler_block(signal)
            self.gtk.set_position(pos)
            for signal in self.syncsignals:
                self.gtk.handler_unblock(signal)

    def setBounds(self, minval, maxval):
        val = self.adjustment.get_value()
        attop = (val == self.adjustment.get_upper())
        atbot = (val == self.adjustment.get_lower())
        self.adjustmentsignal.block()
        try:
            self.adjustment.set_lower(minval)
            self.adjustment.set_upper(maxval)
            self.clipper = self.clipperclass(minval, maxval)
            if attop:
                self.set_value(maxval)
            elif atbot:
                self.set_value(minval)
        finally:
            self.adjustmentsignal.unblock()

    def getBounds(self):
        return (self.adjustment.get_lower(), self.adjustment.get_upper())

    def consistent(self):
        # If the text in the entry has been deleted but slider hasn't
        # moved and no new text has been inserted, the widget is in an
        # inconsistent state and its value can't be evaluated.
        return not self.inconsistent
        

    ## TODO: Is there a Gtk3 version of Range.set_policy?
    # def set_policy(self, policy):
    #     # Set how often the callback is called in response to slider
    #     # motion.  policy should be gtk.UPDATE_CONTINUOUS,
    #     # gtk.UPDATE_DELAYED, or gtk.UPDATE_DISCONTINUOUS.
    #     self.slider.set_update_policy(policy)

    def set_tooltips(self, slider=None, entry=None):
        if slider:
            self.slider.set_tooltip_text(slider)
        if entry:
            self.entry.set_tooltip_text(entry)

    def dumpState(self, comment):
        print(comment, self.__class__.__name__, \
            "text=%s" % self.entry.get_text(), \
            "val=%s" % self.adjustment.get_value(), \
            "focus=%s" % self.entry.has_focus(), file=sys.stderr)

class FloatLabelledSlider(LabelledSlider):
    def set_digits(self, digits):
        # Sets number of digits after the decimal place.
        debug.mainthreadTest()
        self.slider.set_digits(digits)
    def set_entry(self, val):
        debug.mainthreadTest()
        self.entry.set_text(("%-8g" % val).rstrip())
    def get_value(self):
        debug.mainthreadTest()
        return self.clipper.clip(utils.OOFeval(self.entry.get_text()))


class IntLabelledSlider(LabelledSlider):
    def __init__(self, *args, **kwargs):
        LabelledSlider.__init__(self, *args, **kwargs)
        self.slider.set_digits(0)
    def set_entry(self, val):
        debug.mainthreadTest()
        self.entry.set_text("%d" % int(val))
    def get_value(self):
        debug.mainthreadTest()
        return self.clipper.clip(int(utils.OOFeval(self.entry.get_text())))
