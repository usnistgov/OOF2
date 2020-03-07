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
import Gtk
import math

# Collection of labelledsliders, passing through the value-changed
# callback.
class LabelledSliderSet:
    def __init__(self, label=[], min=None, max=None):
        debug.mainthreadTest()
        self.min = min or [0.0]*len(label)
        self.max = max or [1.0]*len(label)

        self.gtk = Gtk.Grid()
        self.sliders = []

        self.callback = None

        for i in range(len(label)):
            newlabel = Gtk.Label(label[i])
            self.gtk.attach(newlabel,0,1,i,i+1)

            newslider = labelledslider.FloatLabelledSlider(
                value=self.min[i], vmin=self.min[i], vmax=self.max[i],
                step=(self.max[i]-self.min[i])/100.0,
                callback=self.slider_callback, name=label[i] )
            
            self.gtk.attach(newslider.gtk, 1,2,i,i+1)
            self.sliders.append(newslider)

    def set_values(self, *values):
        debug.mainthreadTest()
        for i in range(len(values)):
            self.sliders[i].set_value(values[i])

    def get_values(self):
        debug.mainthreadTest()
        return map( lambda x: x.get_value(), self.sliders)

    def set_callback(self, func):
        self.callback = func

    # Callback gets called when any of the sliders changes value.
    # Arguments are the slider which changed value, and the new value.
    # Pass them on through.
    def slider_callback(self, slider, value):
        if self.callback:
            self.callback(slider, value)

class ColorBoxBase(object):
    def __init__(self, xsize=100, ysize=100):
        debug.mainthreadTest()
        self.gtk = Gtk.DrawingArea()
        self.gtk.set_size_request(xsize, ysize)
        self.gtk.connect("draw", self.drawCB)

# TwoColorBox divides its drawing area into two rectangles.  Initially
# both rectangles are filled with the color passed to set_color().  If
# a color is passed to change_color(), only the right hand rectangle
# is updated with the new color.

class TwoColorBox(ColorBoxBase):
    def set_color(self, bg):
        self.color0 = bg
        self.color1 = bg
    def change_color(self, fg):
        self.color1 = fg
    def drawCB(self, widget, ctxt):
        # ctxt is a Cairo context
        width = widget.get_allocated_width()
        halfwidth = width/2.
        height = widget.get_allocated_height()
        context.move_to(0, 0)
        context.line_to(halfwidth, 0)
        context.line_to(halfwidth, height)
        context.line_to(0, height)
        context.close_path()
        context.set_source_rgb(self.color0.getRed(), self.color0.getGreen(),
                               self.color0.getBlue())
        context.fill()
        context.move_to(halfwidth, 0)
        context.line_to(width, 0)
        context.line_to(width, height)
        context.line_to(halfwidth, height)
        context.close_path()
        context.set_source_rgb(self.color1.getRed(), self.color1.getGreen(),
                               self.color1.getBlue())
        context.fill()
        return False

# OneColorBox just displays a single color.  The whole box is redrawn
# when change_color() is called.
        
class OneColorBox(ColorBoxBase):
    def set_color(self, clr):
        self.color = clr
    def change_color(self, clr):
        self.color = clr
    def drawCB(self, widget, ctxt):
        width = widget.get_allocated_width()
        height = widget.get_allocated_height()
        context.set_source_rgb(self.color.getRed(), self.color.getGreen(),
                               self.color.getBlue())
        context.paint()

## TODO: The __init__s for all of these widgets are nearly identical.
## Can code be reused?

# Params will be a list of floats, in r,g,b order corresponding
# to the registration parameters for RGBColor.
class RGBWidget(parameterwidgets.ParameterWidget):
    def __init__(self, params, old_base, colorbox_class, scope=None, name=None):
        debug.mainthreadTest()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        parameterwidgets.ParameterWidget.__init__(self, hbox, scope, name)
        self.params = params
        # VBox for the color patch.
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.colorbox = colorbox_class(160, 40)
        #
        self.gtk.pack_start(self.vbox, expand=False, fill=False, padding=0)
        #
        self.slider = LabelledSliderSet(["Red", "Green", "Blue"])
        self.vbox.pack_start(self.slider.gtk, expand=True, fill=True)
        self.vbox.pack_start(self.colorbox.gtk, expand=False, fill=False)
        #
        if old_base:
            self.color = old_base
        else:
            self.color = color.black
        self.colorbox.set_color(self.color)

        self.set_values()  # Copies values from params to the sliders.
        self.slider.set_callback(self.sliderCB)
        self.widgetChanged(1, interactive=0)

    def sliderCB(self, slider, value):
        # Set the ColorBox from the sliders
        debug.mainthreadTest()
        (r, g, b) = self.slider.get_values()
        self.color = color.RGBColor(r, g, b)
        self.colorbox.change_color(self.color)
        self.widgetChanged(1, interactive=1)

    def set_values(self, values=None):
        # Set the sliders and the ColorBox from the parameters
        debug.mainthreadTest()
        r, g, b = values or [p.value for p in self.params]
        self.slider.set_values(r, g, b)
        self.color = color.RGBColor(r, g, b)
        self.colorbox.change_color(self.color)
        self.widgetChanged(1, interactive=0)
        
    def get_values(self):
        self.params[0].value = self.color.getRed()
        self.params[1].value = self.color.getGreen()
        self.params[2].value = self.color.getBlue()
        # for p,v in map(None, self.params, self.values):
        #     p.value = v

    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()

class DiffRGBWidget(RGBWidget):
    def __init__(self,params,old_base,scope=None, name=None):
        RGBWidget.__init__(self, params, old_base, TwoColorBox, scope, name)

class NewRGBWidget(RGBWidget):
    def __init__(self, params, old_base, scope=None, name=None):
        RGBWidget.__init__(self, params, old_base, OneColorBox, scope, name)
        

regclassfactory.addWidget(color.ColorParameter, color.RGBColor, DiffRGBWidget)
regclassfactory.addWidget(color.NewColorParameter, color.RGBColor, NewRGBWidget)

class HSVWidget(parameterwidgets.ParameterWidget):
    def __init__(self, params, old_base, colorbox_class, scope=None, name=None):
        debug.mainthreadTest()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        parameterwidgets.ParameterWidget.__init__(self, hbox, scope, name)
        self.params = params
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.colorbox = colorbox_class(160,40)
        self.gtk.pack_start(self.vbox, expand=False, fill=False, padding=0)
        self.slider = LabelledSliderSet(["Hue","Saturation","Value"],
                                        max=[360.0, 1.0, 1.0])

        self.vbox.pack_start(self.slider.gtk, expand=False, fill=False,
                             padding=0)
        self.vbox.pack_start(self.colorbox.gtk, expand=False, fill=False,
                             padding=0)
        if old_base:
            self.color = old_base
        else:
            self.color = color.black
        self.colorbox.set_color(self.color)
        self.set_values()
        self.slider.set_callback(self.newhsv)
        self.widgetChanged(1, interactive=0)

    def newhsv(self, slider, value): # slider callback
        debug.mainthreadTest()
        h,s,v = self.slider.get_values()
        self.color = color.HSVColor(h,s,v)
        self.colorbox.change_color(self.color)
        
        # self.values = self.slider.get_values()
        # rgb = self.hsv2rgb(self.values)
        # self.gdkcol = self.gtk.get_colormap().alloc_color(
        #     int(65535*rgb[0]),
        #     int(65535*rgb[1]),
        #     int(65535*rgb[2]))
        # self.colorbox.set_foreground(self.gdkcol)
        self.widgetChanged(1, interactive=1)

    # Set slider values from the params.
    def set_values(self, values=None):
        debug.mainthreadTest()
        h,s,v = values or [p.value for p in self.params]
        self.color = color.HSVColor(h, s, v)
        self.slider.set_values(h, s, v)
        self.colorbox.change_color(self.color)
        self.widgetChanged(1, interactive=0)

    def get_values(self):
        self.params[0].value = self.color.hue
        self.params[1].value = self.color.saturation
        self.params[2].value = self.color.value
        # for p,v in map(None, self.params, self.values):
        #     p.value = v

    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()

    # def hsv2rgb(self,hsv):
    #     (h,s,v) = hsv
        
    #     if s==0.0:
    #         (r,g,b) = (v,v,v)
    #     else:
    #         h_sector = int(math.floor(h/60.0)) # Pick a sector, 0->5.
    #         h_fraction = (h/60.0)-h_sector
    #         #
    #         p = v*(1.0-s)
    #         q = v*(1.0-s*h_fraction)
    #         t = v*(1.0-s*(1.0-h_fraction))
    #         # If h=360.0, we can get artificial wrap-around -- catch it.
    #         if (h_sector == 0) or (h_sector == 6):
    #             (r,g,b) = (v,t,p)
    #         elif h_sector == 1:
    #             (r,g,b) = (q,v,p)
    #         elif h_sector == 2:
    #             (r,g,b) = (p,v,t)
    #         elif h_sector == 3:
    #             (r,g,b) = (p,q,v)
    #         elif h_sector == 4:
    #             (r,g,b) = (t,p,v)
    #         else:
    #             (r,g,b) = (v,p,q)
    #     return (r,g,b)


class DiffHSVWidget(HSVWidget):
    def __init__(self,params,old_base,scope=None,name=None):
        HSVWidget.__init__(self, params, old_base, Colorbox, scope, name)

class NewHSVWidget(HSVWidget):
    def __init__(self,params,old_base,scope=None,name=None):
        HSVWidget.__init__(self, params, old_base, ColorBox, scope, name)

        
regclassfactory.addWidget(color.ColorParameter, color.HSVColor, DiffHSVWidget)
regclassfactory.addWidget(color.NewColorParameter, color.HSVColor, NewHSVWidget)

# Param will be a single Float parameter, corresponding to the
# registry for GrayColor.
class GrayWidget(parameterwidgets.ParameterWidget):
    def __init__(self,params,old_base,colorbox_class,scope=None,name=None):
        debug.mainthreadTest()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        parameterwidgets.ParameterWidget.__init__(self, hbox, scope, name)
        self.params = params
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.colorbox = colorbox_class(160,40)
        #
        self.gtk.pack_start(self.vbox, expand=False, fill=False, padding=0)
        #
        self.slider = LabelledSliderSet(["Gray"], min=[0.0],max=[1.0])
        #
        self.vbox.pack_start(self.slider.gtk, expand=False, fill=False,
                             padding=0)
        self.vbox.pack_start(self.colorbox.gtk, expand=False, fill=False,
                             padding=0)
        #
        if old_base:
            self.color = old_base
        else:
            self.color = color.black
        self.colorbox.set_color(self.color)
        self.set_values()
        self.slider.set_callback(self.newgray)
        self.widgetChanged(1, interactive=0)

    def set_values(self, values=None):
        debug.mainthreadTest()
        (g,) = values or [p.value for p in self.params]
        self.slider.set_values(g)
        self.color = color.Gray(g)
        self.colorbox.change_color(self.color)
        self.widgetChanged(1, interactive=0)
        
        # self.values = values or [p.value for p in self.params]
        # self.slider.set_values(self.values)
        # rgb = self.gray2rgb(self.values[0])
        # self.gdkcol = self.gtk.get_colormap().alloc_color(int(65535*rgb[0]),
        #                                                   int(65535*rgb[1]),
        #                                                   int(65535*rgb[2]))
        # self.colorbox.set_foreground(self.gdkcol)
        # self.widgetChanged(1, interactive=0)
        
    def get_values(self):
        assert isinstance(self.color, color.Gray)
        self.params[0].value = self.color.value

    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()
        
    def newgray(self, slider, value): # slider callback
        debug.mainthreadTest()
        self.color = color.Gray(value)
        self.colorbox.change_color(self.color)
        # self.values = [value]
        # rgb = self.gray2rgb(self.values[0])
        # self.gdkcol = self.gtk.get_colormap().alloc_color(int(65535*rgb[0]),
        #                                                   int(65535*rgb[1]),
        #                                                   int(65535*rgb[2]))
        # self.colorbox.set_foreground(self.gdkcol)
        self.widgetChanged(1, interactive=1)
        
    # def gray2rgb(self, gray):
    #     return (gray, gray, gray)

class DiffGrayWidget(GrayWidget):
    def __init__(self,params,old_base,scope=None,name=None):
        GrayWidget.__init__(self, params, old_base, Colorbox, scope, name)

class NewGrayWidget(GrayWidget):
    def __init__(self,params,old_base,scope=None,name=None):
        GrayWidget.__init__(self, params, old_base, ColorBox, scope, name)

regclassfactory.addWidget(color.ColorParameter, color.Gray, DiffGrayWidget)
regclassfactory.addWidget(color.NewColorParameter, color.Gray, NewGrayWidget)
