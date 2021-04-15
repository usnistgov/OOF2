# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import ooferror
from ooflib.common import debug
from ooflib.common.IO.GUI import gtklogger
from gi.repository import Gtk
from gi.repository import Pango


# A gtk.Button containing an image from the given stock item, (eg,
# gtk.STOCK_OK) and optional text.  If 'reverse' is true, the text
# will precede the image.

# For gtk3, stock_id is the name of a named icon. The possible names
# can be found with
#  it = Gtk.IconTheme()
#  it.list_icons()
# The button text needs to be provided with labelstr, if desired.
# gtk2 provided it automatically.

## TODO?: Many of the icons come in two flavors, "xxx" and
## "xxx-symbolic".  We could make using the symbolic versions an
## option. StockButton could check for the existence of the preferred
## version and fall back to the other version if the preferred one was
## not available.  Then we could delete the "-symbolic" everywhere
## that we spell it out in the code.

class StockButton(Gtk.Button):
    def __init__(self, icon_name, labelstr=None, reverse=False, markup=False,
                 align=None, **kwargs):
        assert isinstance(align, (type(None), Gtk.Align))
        debug.mainthreadTest()
        if debug.debug():
            it = Gtk.IconTheme()
            if not icon_name in it.list_icons():
                raise ooferror.ErrPyProgrammingError(
                    "Bad icon name: " + icon_name)

        if align is None:
            align = Gtk.Align.CENTER
        Gtk.Button.__init__(self, **kwargs)
        image = Gtk.Image.new_from_icon_name(icon_name, Gtk.IconSize.BUTTON)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.markup = markup
        self.reverse = reverse
        if reverse:
            if labelstr:
                if markup:
                    self.label = Gtk.Label(halign=align)
                    self.label.set_markup(labelstr + ' ')
                else:
                    self.label = Gtk.Label(labelstr + ' ')
                hbox.pack_start(self.label, expand=True, fill=True, padding=0)
            hbox.pack_start(image, expand=False, fill=False, padding=0)
        else:                       # not reverse
            hbox.pack_start(image, expand=False, fill=False, padding=0)
            if labelstr:
                if markup:
                    self.label = Gtk.Label(halign=align)
                    self.label.set_markup(' ' + labelstr)
                else:
                    self.label = Gtk.Label(' ' + labelstr)
                hbox.pack_start(self.label, expand=True, fill=True, padding=0)
        self.add(hbox)

    def relabel(self, labelstr):
        if self.markup:
            if self.reverse:
                self.label.set_markup(labelstr + ' ')
            else:
                self.label.set_markup(' ' + labelstr)
        else:
            if self.reverse:
                self.label.set_text(labelstr + ' ')
            else:
                self.label.set_text(' ' + labelstr)
                        
def prevButton(**kwargs):
    debug.mainthreadTest()
    button = StockButton('go-previous-symbolic', 'Prev', **kwargs)
    gtklogger.setWidgetName(button, "Prev")
    return button

def nextButton(**kwargs):
    debug.mainthreadTest()
    button = StockButton('go-next-symbolic', 'Next', reverse=True, **kwargs)
    gtklogger.setWidgetName(button, "Next")
    return button

#####################

# Find and return a gtk widget of type 'widgetclass' in the widget
# hierarchy rooted at 'root' (which must be a gtk widget).

def findChild(widgetclass, root):
    debug.mainthreadTest()
    if isinstance(root, Gtk.Container):
        for child in root.get_children():
            if isinstance(child, widgetclass):
                return child
            descendant = findChild(widgetclass, child)
            if descendant:
                return descendant

# findChildren is just like findChild, but it returns all matching
# child widgets.

def findChildren(widgetclasses, root):
    debug.mainthreadTest()
    kids = []
    if isinstance(root, Gtk.Container):
        for child in root.get_children():
            for widgetclass in widgetclasses:
                if isinstance(child, widgetclass):
                    kids.append(child)
                    break
            kids.extend(findChildren(widgetclasses, child))
    return kids

########################

# extra space around Paned handles because they're not visible enough
handle_padding = 5   

########################

# Global CSS styles.

# addStyle might be called before the GUI is started, before the
# styles can be applied.  So it stores the styles that have been
# assigned too early and oofGUI.__init__ applies them after the main
# window has been created.

# See https://developer.gnome.org/gtk3/stable/chap-css-overview.html

styleStrings = []

def addStyle(stylestring):
    if not guitop.top():
        styleStrings.append(stylestring)
    else:
        guitop.top().addStyle(stylestring)


