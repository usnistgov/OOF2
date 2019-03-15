# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import switchboard
from ooflib.SWIG.orientationmap import orientmapdata
from ooflib.common import debug
from ooflib.common.IO import parameter
from ooflib.common.IO.GUI import fixedwidthtext
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import pixelinfoGUI
from ooflib.common.IO.GUI import pixelinfoGUIplugin
from ooflib.common.IO.GUI import tooltips
from ooflib.engine.IO import orientationmatrix
from ooflib.orientationmap import pixelinfoplugin
import gtk
import math

class OrientMapPixelInfoPlugIn(pixelinfoGUIplugin.PixelInfoGUIPlugIn):
    ordering = 4
    nrows = 1
    def __init__(self, toolbox, table, row):
        debug.mainthreadTest()
        pixelinfoGUIplugin.PixelInfoGUIPlugIn.__init__(self, toolbox)

        self.label = gtk.Label('orientation=')
        self.label.set_alignment(1.0, 0.5)
        table.attach(self.label, 0,1, row,row+1, xpadding=5, xoptions=gtk.FILL)

        self.vbox = gtk.VBox()
        self.param = parameter.ConvertibleRegisteredParameter(
            'dummy', orientationmatrix.Orientation)
        self.widget = self.param.makeWidget() # RegisteredClassFactory
        self.widget.makeReadOnly()
        self.text = gtk.Entry()
        self.text.set_editable(0)
        self.vbox.pack_start(self.text, expand=0, fill=0)
        self.current_mode = 'text'
        table.attach(self.vbox, 1,2, row,row+1,
                     xpadding=5, xoptions=gtk.EXPAND|gtk.FILL)
        self.sbcbs = [
            switchboard.requestCallbackMain(
                'materials changed in microstructure', self.materialchanged),
            switchboard.requestCallbackMain('OrientationMap changed',
                                            self.materialchanged),
            switchboard.requestCallbackMain('material changed',
                                            self.materialchanged),
            switchboard.requestCallbackMain('prop_added_to_material',
                                            self.materialchanged),
            switchboard.requestCallbackMain('prop_removed_from_material',
                                            self.materialchanged),
            switchboard.requestCallbackMain(self.widget, self.widgetcb)
            ]

        self.update(None)

    def set_mode(self, mode):
        if self.current_mode != mode:
            if mode == 'text':
                self.vbox.remove(self.widget.gtk)
                self.vbox.pack_start(self.text, expand=0, fill=0)
                self.text.show()
            elif mode == 'widget':
                self.vbox.remove(self.text)
                self.vbox.pack_start(self.widget.gtk, expand=0, fill=0)
                self.widget.show()
            self.current_mode = mode
                                                              
    def close(self):
        map(switchboard.removeCallback, self.sbcbs)
        pixelinfoGUIplugin.PixelInfoGUIPlugIn.close(self)

    def materialchanged(self, *args, **kwargs):
        # Generic switchboard callback, called when materials or
        # properties change, or materials are assigned to or removed
        # from pixels, or the material map changes in a
        # Microstructure.  We could check here to see if the change
        # affects the actual object that we're displaying, but it's
        # not worth the effort.
        self.update(self.toolbox.currentPixel())

    def update(self, where):
        debug.mainthreadTest()
        microstructure = self.toolbox.findMicrostructure()
        if microstructure and where is not None:
            orientsource = orientmapdata.getOrientationAtPoint(
                microstructure, where)
            if orientsource:
                orientation, source = orientsource
                # orientation is a COrientation instance.  It has to
                # be converted into an orientationmatrix.Orientation
                # object so that we can make (ab)use of the
                # ConvertibleRegisteredClass machinery.
                abg = orientation.abg()
                if self.param.value is not None:
                    klass = self.param.value.__class__
                    reg = self.param.value.getRegistration()
                else:
                    reg = orientationmatrix.Orientation.registry[0]
                    klass = reg.subclass
                base = orientationmatrix.Abg(
                    *[a*180./math.pi for a in (abg.alpha(), abg.beta(),
                                               abg.gamma())])
                newvalue = klass(*reg.from_base(None, base))
                self.param.value = newvalue
                self.widget.set(newvalue, interactive=False)
                self.set_mode("widget")
                self.label.set_text('Orientation=\n(%s)' % source)
            else:                       # orientsource is None
                self.text.set_text("<No Orientation>")
                self.set_mode("text")
                self.label.set_text('Orientation=')
        else:                      # microstructure is None or where is None
            self.text.set_text("<No Microstructure>")
            self.set_mode("text")
            self.label.set_text('Orientation=')

    def getOrientation(self):
        if self.current_mode == "widget":
            return self.widget.get_value()

    def widgetcb(self, *args, **kwargs):
        self.param.value = self.widget.get_value()

    def clear(self):
        debug.mainthreadTest()
        self.set_mode("text")
        self.text.set_text("---")

    def nonsense(self):
        debug.mainthreadTest()
        self.set_mode("text")
        self.text.set_text("???")
                
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class MisorientationPixelInfoPlugIn(pixelinfoGUIplugin.PixelInfoGUIPlugIn):
    ordering=5
    nrows = 4 # title, reference orientation + set button, lattice
              # widget, misorientation output
    def __init__(self, toolbox, table, row):
        debug.mainthreadTest()
        pixelinfoGUIplugin.PixelInfoGUIPlugIn.__init__(self, toolbox)
        self.refOrient = None   # the current reference orientation
        self.sbcbs = []         # switchboard callbacks

        title = gtk.Label("Misorientation")
        title.set_alignment(0.5, 0.5)
        table.attach(title, 1,2, row, row+1, xpadding=5, ypadding=2,
                     xoptions=gtk.FILL)

        label = gtk.Label("reference=")
        label.set_alignment(1.0, 0.5)
        table.attach(label, 0,1, row+1, row+2, xpadding=5, xoptions=gtk.FILL)

        frame = gtk.Frame()
        vbox = gtk.VBox()
        frame.add(vbox)
        table.attach(frame, 1,2, row+1,row+2, xpadding=5,
                     xoptions=gtk.EXPAND|gtk.FILL)

        # refBox holds either the RCF for the reference orientation,
        # or a gtk.Entry saying that the reference orientation isn't
        # set.  The only purpose of the box is to make it easy to swap
        # the RCF and the Entry.
        self.refBox = gtk.VBox()
        vbox.pack_start(self.refBox, fill=1, expand=0)
        
        refParam = self.getMenu().Set_Reference.get_arg("orientation")
        self.refWidget = refParam.makeWidget() # RegisteredClassFactory
        self.refWidget.makeReadOnly()

        self.refText = fixedwidthtext.FixedWidthTextView()
        self.refText.set_wrap_mode(gtk.WRAP_WORD)
        self.refText.set_editable(False)
        self.refText.set_cursor_visible(False)
        self.refText.get_buffer().set_text(
            'Select a pixel and click "Set Reference Orientation" to make it the reference.')
        self.refBox.pack_start(self.refText, expand=0, fill=0)

        # The "Set Reference" button copies the orientation from the
        # OrientMapPixelInfoPlugIn to the reference widget in this
        # plug-in.
        self.setButton = gtk.Button("Set Reference Orientation")
        gtklogger.setWidgetName(self.setButton, "Set")
        align = gtk.Alignment(xalign=0.5)
        align.add(self.setButton)
        vbox.pack_start(align, fill=0, expand=0)
        gtklogger.connect(self.setButton, 'clicked', self.setButtonCB)
        tooltips.set_tooltip_text(
            self.setButton,
            'Set the reference orientation to the'
            ' previously selected orientation.')

        label = gtk.Label("symmetry=")
        label.set_alignment(1.0, 0.5)
        table.attach(label, 0,1, row+2,row+3, xpadding=0, xoptions=gtk.FILL)
        symParam = self.getMenu().Set_Symmetry.get_arg('symmetry')
        self.symWidget = symParam.makeWidget()
        gtklogger.setWidgetName(self.symWidget.gtk, "Symmetry")
        table.attach(self.symWidget.gtk, 1,2, row+2,row+3, xpadding=5,
                     xoptions=gtk.EXPAND|gtk.FILL)

        label = gtk.Label("misorientation=")
        label.set_alignment(1.0, 0.5)
        table.attach(label, 0,1, row+3,row+4, xpadding=0, xoptions=gtk.FILL)
        self.misorientationText = gtk.Entry()
        self.misorientationText.set_editable(0)
        table.attach(self.misorientationText, 1,2, row+3,row+4,
                     xpadding=5, xoptions=gtk.EXPAND|gtk.FILL)
        self.sbcbs = [
            # Changing the lattice symmetry requires an immediate
            # update of the misorientation.  Connecting to the widget
            # via the switchboard catches all changes, not just
            # changes to the top chooser widget.
            switchboard.requestCallbackMain(self.symWidget, self.symChanged),
            # Messages indicating that the Microstructure has changed
            # in some possibly relevant way:
            switchboard.requestCallbackMain('OrientationMap changed',
                                            self.materialchanged),
            switchboard.requestCallbackMain(
                "materials changed in microstructure", self.materialchanged),
            switchboard.requestCallbackMain('material changed',
                                            self.materialchanged),
            switchboard.requestCallbackMain('prop_added_to_material',
                                            self.materialchanged),
            switchboard.requestCallbackMain('prop_removed_from_material',
                                            self.materialchanged),
            # Messages sent from the non-gui part of the toolbox:
            switchboard.requestCallbackMain("set reference orientation",
                                            self.setReference),
            switchboard.requestCallbackMain("set misorientation symmetry",
                                            self.setSymmetry)
            ]

        self.sensitize()

    def getNonGUIPlugIn(self):
        return self.getNonGUIToolbox().findPlugIn(
            pixelinfoplugin.MisorientationPlugIn)
    def getNonGUIToolbox(self):
        return self.toolbox.gfxwindow().getToolboxByName("Pixel_Info")
    def getMenu(self):
        return self.getNonGUIToolbox().menu.Misorientation

    def close(self):
        map(switchboard.removeCallback, self.sbcbs)
        pixelinfoGUIplugin.PixelInfoGUIPlugIn.close(self)

    def clear(self):
        self.getNonGUIPlugIn().clear()
        if self.refOrient is not None:
            self.refBox.remove(self.refWidget.gtk)
            self.refBox.pack_start(self.refText, expand=0, fill=0)
        self.refOrient = None
        self.updateMisorientation()
        
    def nonsense(self):
        self.updateMisorientation()

    def update(self, point):
        # This will do the right thing only if the
        # OrientMapPixelInfoPlugIn has been updated first, which is
        # will be if it was created first.
        self.updateMisorientation()

    def sensitize(self):
        self.setButton.set_sensitive(self.getOrientation() is not None)

    def setButtonCB(self, button):
        # gtk callback for "Set Reference Orientation" button
        menuitem = self.getMenu().Set_Reference
        menuitem.callWithDefaults(orientation=self.getOrientation())

    def setReference(self, gfxwindow):
        # switchboard callback for "set reference orientation"
        if gfxwindow is not self.toolbox.gfxwindow():
            return
        # If there was no reference orientation displayed before, we
        # have to install the orientation widget and remove the text widget.
        if self.refOrient is None:
            self.refBox.remove(self.refText)
            self.refBox.pack_start(self.refWidget.gtk, expand=0, fill=0)
        nonguitoolbox = self.getNonGUIToolbox()
        plugin = nonguitoolbox.findPlugIn(pixelinfoplugin.MisorientationPlugIn)
        self.refOrient = plugin.referenceOrientation
        self.refWidget.set(self.refOrient, interactive=False)
        assert self.refOrient is not None
        self.updateMisorientation()
            
    def updateMisorientation(self):
        orient = self.getOrientation()
        symmetry = self.getNonGUIPlugIn().symmetry
        if (orient is None or symmetry is None or self.refOrient is None):
            self.misorientationText.set_text('???')
        else:
            misorientation = orient.misorientation(self.refOrient,
                                                   symmetry.schoenflies())
            self.misorientationText.set_text(`misorientation`)
        self.sensitize()

    def getOrientation(self):
        # The orientation (the one that's being compared to the
        # reference orientation) is the one currently chosen in the
        # OrientMapPixelInfoPlugIn.
        oplugin = self.toolbox.findGUIPlugIn(OrientMapPixelInfoPlugIn)
        if oplugin is None:
            return
        return oplugin.getOrientation()

    def symChanged(self, interactive):
        # Switchboard callback for changes in the state of the
        # symmetry widget.

        # Checking 'interactive' here suppresses an infinite loop.
        # The menu item sets the value of the widget, which calls this
        # callback. 'interactive' is false if this callback is called
        # via that sequence.
        if interactive:
            menuitem = self.getMenu().Set_Symmetry
            menuitem.callWithDefaults(symmetry=self.symWidget.get_value())

    def setSymmetry(self, gfxwindow):
        # switchboard callback for "set misorientation symmetry",
        # which is issued by the menu command.
        if gfxwindow is not self.toolbox.gfxwindow():
            return
        self.symWidget.set(self.getNonGUIPlugIn().symmetry, interactive=False)
        self.updateMisorientation()
        
    def materialchanged(self, *args, **kwargs):
        debug.fmsg()
        self.updateMisorientation()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# The OrientMapPixelInfoPlugIn must be created before the
# MisorientationPixelInfoPlugIn in each graphics window, so it must be
# registered first here.

pixelinfoGUIplugin.registerPlugInClass(OrientMapPixelInfoPlugIn)
pixelinfoGUIplugin.registerPlugInClass(MisorientationPixelInfoPlugIn)
