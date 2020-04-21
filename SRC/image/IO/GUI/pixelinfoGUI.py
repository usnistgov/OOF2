# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
if config.dimension() == 2:
    from ooflib.SWIG.image import oofimage
elif config.dimension() == 3:
    from ooflib.SWIG.image import oofimage3d as oofimage
from ooflib.common import color
from ooflib.common import debug
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import pixelinfoGUIplugin
from gi.repository import Gtk

class ImagePlugIn(pixelinfoGUIplugin.PixelInfoGUIPlugIn):
    ordering = 1
    nrows = 5
    def __init__(self, toolbox, grid, row):
        debug.mainthreadTest()
        pixelinfoGUIplugin.PixelInfoGUIPlugIn.__init__(self, toolbox)

        # Colorv is set by "update" and "nonsense", it can be None (no
        # color), -1 (Nonsense), or a color.Color object.
        # Statefulness is needed to remain consistent when a user
        # switches from RGB to HSV or vice versa.
        self.colorv = None
        
        label = Gtk.Label('image=', halign=Gtk.Align.END, hexpand=False)
        grid.attach(label, 0,row, 1,1)
        self.imagetext = Gtk.Entry(editable=False, hexpand=True,
                                   halign=Gtk.Align.FILL)
        self.imagetext.set_width_chars(12)
        gtklogger.setWidgetName(self.imagetext, "Image")
        grid.attach(self.imagetext, 1,row, 1,1)

        selectorbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                              halign=Gtk.Align.START,
                              spacing=2)
        self.rgb_selector = Gtk.RadioButton("RGB")
        self.rgb_selector.set_tooltip_text(
            "View color values in Red-Green-Blue format.")
        selectorbox.add(self.rgb_selector)
        self.hsv_selector = Gtk.RadioButton("HSV", group=self.rgb_selector)
        self.hsv_selector.set_tooltip_text(
            "View color values in Hue-Saturation-Value format.")
        selectorbox.add(self.hsv_selector)
        self.rgb_selector.set_active(True) # Default.
        gtklogger.setWidgetName(self.rgb_selector, "RGB selector")
        gtklogger.setWidgetName(self.hsv_selector, "HSV selector")
        gtklogger.connect(self.rgb_selector, "clicked", self.selector_cb)
        gtklogger.connect(self.hsv_selector, "clicked", self.selector_cb)
        grid.attach(selectorbox, 1,row+1, 1,1)
        
        self.label1 = Gtk.Label('red=', halign=Gtk.Align.END)
        grid.attach(self.label1, 0,row+2, 1,1)
        self.text1 = Gtk.Entry(editable=False)
        gtklogger.setWidgetName(self.text1,'Text 1')
        self.text1.set_width_chars(10)
        grid.attach(self.text1, 1,row+2, 1,1)

        self.label2 = Gtk.Label('green=', halign=Gtk.Align.END)
        grid.attach(self.label2, 0,row+3,1,1)
        self.text2 = Gtk.Entry(editable=False)
        gtklogger.setWidgetName(self.text2,'Text 2')
        self.text2.set_width_chars(10)
        grid.attach(self.text2, 1,row+3, 1,1)

        self.label3 = Gtk.Label('blue=', halign=Gtk.Align.END)
        grid.attach(self.label3, 0,row+4, 1,1)
        self.text3 = Gtk.Entry(editable=False)
        gtklogger.setWidgetName(self.text3,'Text 3')
        self.text3.set_width_chars(10)
        grid.attach(self.text3, 1,row+4, 1,1)

        self.sbcallbacks = [
            switchboard.requestCallbackMain('modified image',
                                            self.image_changed)
            ]

    def close(self):
        map(switchboard.removeCallback, self.sbcallbacks)

    def update(self, where):
        debug.mainthreadTest()
        # If the topmost Image in the display is obscured by a
        # Microstructure, then Image data is not displayed in the
        # toolbox.  This is because it wouldn't be clear which Image
        # the data is from, if the Microstructure has more than one
        # Image or if the Image is from a different Microstructure.
        image = self.toolbox.gfxwindow().topmost('Image', 'Microstructure')
        if config.dimension() == 2:
            imagetype = oofimage.OOFImagePtr
        elif config.dimension() == 3:
            imagetype = oofimage.OOFImage3D
        if isinstance(image, imagetype) and where is not None:
            self.colorv = image[where]
            imagecontext = self.toolbox.gfxwindow().topwho('Image')
            self.imagetext.set_text(imagecontext.path())
        else:
            self.colorv = None
            self.imagetext.set_text('(No image)')
        self.color_display()

    # GTK callback for selection toggles.
    def selector_cb(self, gtkobj):
        # activations are always paired with deactivations, so one can
        # be ignored.
        if gtkobj.get_active():
            self.color_display()

    def clear(self):
        self.colorv = None
        self.imagetext.set_text("")
        self.color_display()

    def color_display(self):
        debug.mainthreadTest()
        # First do labels, then do colors.
        if self.rgb_selector.get_active():
            self.label1.set_text("red=")
            self.label2.set_text("green=")
            self.label3.set_text("blue=")
        else:
            self.label1.set_text("hue=")
            self.label2.set_text("saturation=")
            self.label3.set_text("value=")

        if self.colorv == -1:
            return
            
        if self.colorv is not None:
            (c1,c2,c3) = (self.colorv.getRed(),
                          self.colorv.getGreen(),
                          self.colorv.getBlue())
            if not self.rgb_selector.get_active():
                (c1,c2,c3) = color.hsv_from_rgb(c1,c2,c3)
            self.text1.set_text(`c1`)
            self.text2.set_text(`c2`)
            self.text3.set_text(`c3`)
            
        else:
            self.text1.set_text("")
            self.text2.set_text("")
            self.text3.set_text("")

    
    def image_changed(self, modifier, image):
        self.update(self.toolbox.currentPixel())

    def nonsense(self):
        debug.mainthreadTest()
        self.colorv = -1
        debug.mainthreadTest()
        self.imagetext.set_text('???')
        self.text1.set_text('???')
        self.text2.set_text('???')
        self.text3.set_text('???')


pixelinfoGUIplugin.registerPlugInClass(ImagePlugIn)

