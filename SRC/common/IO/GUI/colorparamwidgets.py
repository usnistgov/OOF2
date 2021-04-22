# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


# Color selection widget, customized for rgb, hsv, and gray.
# The colors are a convertible class, meaning that they express
# a single object or value in one of several different representations,
# in this case, HSV, Gray, or RGB.  The different widgets allow the
# user to set the color according to a particular representation.

from ooflib.common import color
from ooflib.common import debug
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import labelledslider
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory
from gi.repository import Gtk
import math


class LabelledSliderSet(object):
    def __init__(self, label=[], min=None, max=None):
        debug.mainthreadTest()
        self.min = min or [0.0]*len(label)
        self.max = max or [1.0]*len(label)

        self.gtk = Gtk.Grid()
        self.sliders = []

        self.callback = None

        for i in range(len(label)):
            newlabel = Gtk.Label(label[i], halign=Gtk.Align.END)
            self.gtk.attach(newlabel,0,i, 1,1)

            newslider = labelledslider.FloatLabelledSlider(
                value=self.min[i], vmin=self.min[i], vmax=self.max[i],
                step=(self.max[i]-self.min[i])/100.0,
                callback=self.slider_callback, name=label[i],
                logpaned=(i==0), # only log the GtkPaned position for one slider
                hexpand=True, halign=Gtk.Align.FILL
            )
            
            self.gtk.attach(newslider.gtk, 1,i, 1,1)
            self.sliders.append(newslider)

        # (Ab)use the widget synchronization for ParameterTables to
        # keep the Paneds in the LabelledSliders in sync.  This is an
        # abuse because we're not actually using a ParameterTable
        # here.
        for slider in self.sliders:
            slider.parameterTableXRef(self, self.sliders)

    def set_values(self, *values):
        debug.mainthreadTest()
        for i in range(len(values)):
            self.sliders[i].set_value(values[i])

    def get_values(self):
        debug.mainthreadTest()
        return [x.get_value() for x in self.sliders]

    def set_callback(self, func):
        self.callback = func

    # Callback gets called when any of the sliders changes value.
    # Arguments are the slider which changed value, and the new value.
    # Pass them on through.
    def slider_callback(self, slider, value):
        if self.callback:
            self.callback(slider, value)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# TwoColorBox divides its drawing area into two rectangles.  Initially
# both rectangles are filled with the color passed to set_color().  If
# a color is passed to change_color(), only the right hand rectangle
# is updated with the new color.  Both rectangles are drawn on top of
# black and white triangles so that the opacity of the colors is
# apparent.

class TwoColorBox(object):
    def __init__(self, xsize=100, ysize=100):
        debug.mainthreadTest()
        self.gtk = Gtk.DrawingArea()
        self.gtk.set_size_request(xsize, ysize)
        self.gtk.connect("draw", self.drawCB)
    def set_color(self, bg):
        self.color0 = bg
        self.color1 = bg
    def change_color(self, fg):
        self.color1 = fg
        self.gtk.queue_draw()
    def drawCB(self, widget, context):
        # context is a Cairo::Context
        width = widget.get_allocated_width()
        halfwidth = width/2.
        height = widget.get_allocated_height()
        # Draw white and black triangles on the background.
        context.set_source_rgb(0, 0, 0)
        context.move_to(0, 0)
        context.line_to(halfwidth, 0)
        context.line_to(0, height)
        context.close_path()
        context.fill()
        context.move_to(halfwidth, 0)
        context.line_to(width, 0)
        context.line_to(halfwidth, height)
        context.close_path()
        context.fill()
        context.set_source_rgb(1, 1, 1)
        context.move_to(halfwidth, 0)
        context.line_to(halfwidth, height)
        context.line_to(0, height)
        context.close_path()
        context.fill()
        context.move_to(width, 0)
        context.line_to(width, height)
        context.line_to(halfwidth, height)
        context.close_path()
        context.fill()

        # Draw the old color in a rectangle on the left.
        context.move_to(0, 0)
        context.line_to(halfwidth, 0)
        context.line_to(halfwidth, height)
        context.line_to(0, height)
        context.close_path()
        context.set_source_rgba(self.color0.getRed(), self.color0.getGreen(),
                                self.color0.getBlue(), self.color0.getAlpha())
        context.fill()
        # Draw the new color in a rectangle on the right.
        context.move_to(halfwidth, 0)
        context.line_to(width, 0)
        context.line_to(width, height)
        context.line_to(halfwidth, height)
        context.close_path()
        context.set_source_rgba(self.color1.getRed(), self.color1.getGreen(),
                                self.color1.getBlue(), self.color1.getAlpha())
        context.fill()
        return False

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class ColorWidget(parameterwidgets.ParameterWidget):
    def __init__(self, params, old_base, scope=None, name=None):
        debug.mainthreadTest()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        parameterwidgets.ParameterWidget.__init__(self, vbox, scope, name)
        self.params = params

        self.sliders = LabelledSliderSet(self.slidernames,
                                         self.slidermins, self.slidermaxes)
        self.colorbox = TwoColorBox(160, 40)
        self.gtk.pack_start(self.sliders.gtk,
                            expand=True, fill=True, padding=0)
        self.gtk.pack_start(self.colorbox.gtk,
                            expand=False, fill=False, padding=0)
        if old_base:
            self.color = old_base
        else:
            self.color = color.black
        self.colorbox.set_color(self.color)

        self.set_values()       # Copies values from params to the sliders
        self.sliders.set_callback(self.sliderCB)
        self.widgetChanged(True, interactive=False)

    def sliderCB(self, slider, value):
        # Set the ColorBox from the sliders. The first arg is the
        # slider that changed, but we don't really need to know it.
        debug.mainthreadTest()
        # A labelled slider can be in an invalid state if its text has
        # been deleted, in which case get_values() will raise an
        # exception.
        try:
            values = self.sliders.get_values()
        except:
            self.widgetChanged(False, interactive=True)
        else:
            self.color = self.colorclass(*values)
            self.colorbox.change_color(self.color)
            self.widgetChanged(True, interactive=True)

    def set_values(self, values=None):
        # Set the sliders and the ColorBox from the parameters
        debug.mainthreadTest()
        vals = values or [p.value for p in self.params]
        self.sliders.set_values(*vals)
        self.color = self.colorclass(*vals)
        self.colorbox.change_color(self.color)
        self.widgetChanged(True, interactive=False)

    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()

class RGBWidget(ColorWidget):
    colorclass = color.RGBColor
    slidernames = ["red", "green", "blue"]
    slidermins = [0.0]*3
    slidermaxes = [1.0]*3
    def get_values(self):
        self.params[0].value = self.color.red
        self.params[1].value = self.color.green
        self.params[2].value = self.color.blue

class RGBAWidget(ColorWidget):
    colorclass = color.RGBAColor
    slidernames = ["red", "green", "blue", "alpha"]
    slidermins = [0.0]*4
    slidermaxes = [1.0]*4
    def get_values(self):
        self.params[0].value = self.color.red
        self.params[1].value = self.color.green
        self.params[2].value = self.color.blue
        self.params[3].value = self.color.alpha

class HSVWidget(ColorWidget):
    colorclass = color.HSVColor
    slidernames = ["hue", "saturation", "value"]
    slidermins = [0.0]*3
    slidermaxes = [360., 1.0, 1.0]
    def get_values(self):
        self.params[0].value = self.color.hue
        self.params[1].value = self.color.saturation
        self.params[2].value = self.color.value

class HSVAWidget(ColorWidget):
    colorclass = color.HSVAColor
    slidernames = ["hue", "saturation", "value", "alpha"]
    slidermins = [0.0]*4
    slidermaxes = [360., 1.0, 1.0, 1.0]
    def get_values(self):
        self.params[0].value = self.color.hue
        self.params[1].value = self.color.saturation
        self.params[2].value = self.color.value
        self.params[3].value = self.color.alpha

class GrayWidget(ColorWidget):
    colorclass = color.Gray
    slidernames = ["gray"]
    slidermins = [0.0]
    slidermaxes = [1.0]
    def get_values(self):
        self.params[0].value = self.color.value

class TransGrayWidget(ColorWidget):
    colorclass = color.TranslucentGray
    slidernames = ["gray", "alpha"]
    slidermins = [0.0, 0.0]
    slidermaxes = [1.0, 1.0]
    def get_values(self):
        self.params[0].value = self.color.value
        self.params[1].value = self.color.alpha


regclassfactory.addWidget(
    color.OpaqueColorParameter, color.RGBColor, RGBWidget)
regclassfactory.addWidget(
    color.TranslucentColorParameter, color.RGBAColor, RGBAWidget)
regclassfactory.addWidget(
    color.OpaqueColorParameter, color.HSVColor, HSVWidget)
regclassfactory.addWidget(
    color.TranslucentColorParameter, color.HSVAColor, HSVAWidget)
regclassfactory.addWidget(
    color.OpaqueColorParameter, color.Gray, GrayWidget)
regclassfactory.addWidget(
    color.TranslucentColorParameter, color.TranslucentGray, TransGrayWidget)
