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
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import pixelinfoGUI
from ooflib.common.IO.GUI import pixelinfoGUIplugin
from ooflib.engine.IO import orientationmatrix
from ooflib.orientationmap import pixelinfoplugin

from ooflib.common.runtimeflags import digits

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import math

class OrientMapPixelInfoPlugIn(pixelinfoGUIplugin.PixelInfoGUIPlugIn):
    ordering = 4
    nrows = 1
    def __init__(self, toolbox, table, row):
        debug.mainthreadTest()
        pixelinfoGUIplugin.PixelInfoGUIPlugIn.__init__(self, toolbox)

        self.label = Gtk.Label(label='orientation=', halign=Gtk.Align.END)
        table.attach(self.label, 0,row, 1,1)

        self.stack = Gtk.Stack(homogeneous=False)
        gtklogger.setWidgetName(self.stack, "orientation")

        self.param = parameter.ConvertibleRegisteredParameter(
            'dummy', orientationmatrix.Orientation)
        self.widget = self.param.makeWidget() # RegisteredClassFactory
        self.widget.makeReadOnly()
        self.stack.add_named(self.widget.gtk, "widget")
        self.text = Gtk.Entry(editable=False, hexpand=True)
        gtklogger.setWidgetName(self.text, "text")
        self.stack.add_named(self.text, "text")
        self.stack.set_visible_child_name("text")

        table.attach(self.stack, 1,row,1,1)
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
        self.stack.set_visible_child_name(mode)

    def get_mode(self):
        return self.stack.get_visible_child_name()
                                                              
    def close(self):
        switchboard.removeCallbacks(self.sbcbs)
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
                newvalue = klass(*reg.from_base(base))
                self.param.value = newvalue
                self.widget.set(newvalue, interactive=False)
                self.set_mode("widget")
                self.label.set_text('Orientation=\n(%s)' % source)
            else:                       # orientsource is None
                self.text.set_text("<No Orientation>")
                self.set_mode("text")
                self.label.set_text('Orientation=')
        else:                      # microstructure is None or where is None
            self.text.set_text("---")
            self.set_mode("text")
            self.label.set_text('Orientation=')

    def getOrientation(self):
        if self.get_mode() == "widget":
            return self.widget.get_value()

    def getLocation(self):
        return self.toolbox.currentPixel()
    
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

        title = Gtk.Label(label="Misorientation", halign=Gtk.Align.FILL)
        table.attach(title, 1,row, 1,1)

        label = Gtk.Label(label="reference=", halign=Gtk.Align.END)
        table.attach(label, 0,row+1, 1,1)

        frame = Gtk.Frame()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, margin=2)
        frame.add(vbox)
        table.attach(frame, 1,row+1, 1,1)

        # The stack displays either the RCF for the reference
        # orientation, or a gtk.Entry saying that the reference
        # orientation isn't set.
        self.stack = Gtk.Stack(homogeneous=False)
        gtklogger.setWidgetName(self.stack, 'reference')
        vbox.pack_start(self.stack, fill=True, expand=False, padding=0)
        
        refBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.stack.add_named(refBox, 'refwidget')
        refParam = self.getMenu().Set_Reference.get_arg("orientation")

        self.refWidget = refParam.makeWidget() # RegisteredClassFactory
        self.refWidget.makeReadOnly()

        # A table displaying the x, y coords of the reference point.
        # TODO: Should the coordinates be editable directly?  It would
        # require a separate button to indicate that the user is done
        # editing.
        self.refPointTable = Gtk.Grid(margin_start=2, margin_end=2,
                                      column_spacing=1, row_spacing=1,
                                      hexpand=True)
        gtklogger.setWidgetName(self.refPointTable, 'point')

        xlabel = Gtk.Label(label="x=", halign=Gtk.Align.END)
        self.refPointTable.attach(xlabel, 0,0, 1,1)

        self.xtext = Gtk.Entry(editable=False)
        gtklogger.setWidgetName(self.xtext, 'X')
        self.refPointTable.attach(self.xtext, 1,0, 1,1)

        ylabel = Gtk.Label(label="y=", halign=Gtk.Align.END)
        self.refPointTable.attach(ylabel, 0,1, 1,1)
        
        self.ytext = Gtk.Entry(editable=False)
        gtklogger.setWidgetName(self.ytext, 'Y')
        self.refPointTable.attach(self.ytext, 1,1, 1,1)

        refBox.pack_start(self.refWidget.gtk,
                          expand=False, fill=False, padding=0)
        refBox.pack_start(self.refPointTable,
                          expand=True, fill=True, padding=0)
        
        # Text displayed instead of the reference orientation and
        # location when no reference has been selected.

        refText = Gtk.TextView(name="fixedfont",
                               left_margin=5, right_margin=5,
                               top_margin=5, bottom_margin=5,
                               wrap_mode=Gtk.WrapMode.WORD,
                               editable=False, cursor_visible=False)
        gtklogger.setWidgetName(refText, 'text')
        self.refTextFrame = Gtk.Frame(margin=2)
        self.refTextFrame.add(refText)
        refText.get_buffer().set_text(
            'Select a pixel and click "Set Reference Point"'
            ' to make it the reference.')
        self.stack.add_named(self.refTextFrame, "reftext")

        # The "Set Reference" button copies the orientation from the
        # OrientMapPixelInfoPlugIn to the reference widget in this
        # plug-in.
        self.setRefButton = Gtk.Button(label="Set Reference Point",
                                    halign=Gtk.Align.CENTER)
        gtklogger.setWidgetName(self.setRefButton, "setref")
        vbox.pack_start(self.setRefButton, fill=False, expand=False, padding=0)
        gtklogger.connect(self.setRefButton, 'clicked', self.setRefButtonCB)
        self.setRefButton.set_tooltip_text(
            'Set the reference orientation to the'
            ' previously selected orientation.')

        label = Gtk.Label(label="symmetry=", halign=Gtk.Align.END)
        table.attach(label, 0,row+2, 1,1)
        symParam = self.getMenu().Set_Symmetry.get_arg('symmetry')
        symbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        gtklogger.setWidgetName(symbox, 'symmetry')
        self.symtext = Gtk.Entry(editable=False)
        gtklogger.setWidgetName(self.symtext, 'text')
        symbox.pack_start(self.symtext, expand=True, fill=True, padding=0)
        self.setSymButton = Gtk.Button(label="Set")
        gtklogger.setWidgetName(self.setSymButton, "set")
        gtklogger.connect(self.setSymButton, 'clicked', self.setSymmetryCB)
        symbox.pack_start(self.setSymButton,
                          expand=False, fill=False, padding=0)
        table.attach(symbox, 1,row+2, 1,1)

        label = Gtk.Label(label="misorientation=", halign=Gtk.Align.END)
        table.attach(label, 0,row+3, 1,1)
        self.misorientationText = Gtk.Entry(editable=False, hexpand=True)
        gtklogger.setWidgetName(self.misorientationText, 'misorientation')
        table.attach(self.misorientationText, 1,row+3, 1,1)
        self.sbcbs = [
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

        self.stack.set_visible_child_name("reftext")
        self.setSymmetry(self.toolbox.gfxwindow())
        self.sensitize()

    def getNonGUIPlugIn(self):
        return self.getNonGUIToolbox().findPlugIn(
            pixelinfoplugin.MisorientationPlugIn)
    def getNonGUIToolbox(self):
        return self.toolbox.gfxwindow().getToolboxByName("Pixel_Info")
    def getMenu(self):
        return self.getNonGUIToolbox().menu.Misorientation

    def close(self):
        switchboard.removeCallbacks(self.sbcbs)
        pixelinfoGUIplugin.PixelInfoGUIPlugIn.close(self)

    def clear(self):
        self.getNonGUIPlugIn().clear()
        self.stack.set_visible_child_name("reftext")
        self.refOrient = None
        self.updateMisorientation()
        
    def nonsense(self):
        self.updateMisorientation()

    def update(self, point):
        # This will do the right thing only if the
        # OrientMapPixelInfoPlugIn has been updated first,
        # which it will be if it was created first.
        self.updateMisorientation()
        self.sensitize()

    def sensitize(self):
        self.setRefButton.set_sensitive(
            self.getOrientPlugInData()[0] is not None)

    def setRefButtonCB(self, button):
        # gtk callback for "Set Reference Orientation" button
        menuitem = self.getMenu().Set_Reference
        orientation, location = self.getOrientPlugInData()
        menuitem.callWithDefaults(point=location, orientation=orientation)

    def setReference(self, gfxwindow):
        # switchboard callback for "set reference orientation"
        if gfxwindow is not self.toolbox.gfxwindow():
            return
        nonguitoolbox = self.getNonGUIToolbox()
        plugin = nonguitoolbox.findPlugIn(pixelinfoplugin.MisorientationPlugIn)
        self.refOrient = plugin.referenceOrientation
        self.refPoint = plugin.referencePoint
        self.refWidget.set(self.refOrient, interactive=False)
        self.xtext.set_text(f"{self.refPoint.x:.{digits()}g}")
        self.ytext.set_text(f"{self.refPoint.y:.{digits()}g}")
        self.stack.set_visible_child_name("refwidget")
        assert self.refOrient is not None
        self.updateMisorientation()
            
    def updateMisorientation(self):
        orient, location = self.getOrientPlugInData()
        symmetry = self.getNonGUIPlugIn().symmetry
        if (orient is None or symmetry is None or self.refOrient is None):
            self.misorientationText.set_text('???')
        else:
            misorientation = orient.misorientation(self.refOrient,
                                                   symmetry.schoenflies())
            self.misorientationText.set_text(f"{misorientation:.{digits()}f}")
        self.sensitize()

    def getOrientPlugInData(self):
        # The orientation (the one that's being compared to the
        # reference orientation) is the one currently chosen in the
        # OrientMapPixelInfoPlugIn.
        oplugin = self.toolbox.findGUIPlugIn(OrientMapPixelInfoPlugIn)
        if oplugin is None:
            return
        return oplugin.getOrientation(), oplugin.getLocation()

    def setSymmetryCB(self, button):
        menuitem = self.getMenu().Set_Symmetry
        if parameterwidgets.getParameters(
                menuitem.get_arg('symmetry'),
                parentwindow=self.toolbox.gtk.get_toplevel(),
                title="Set lattice symmetry for misorientation calculation"):
            menuitem.callWithDefaults()
                                        

    def setSymmetry(self, gfxwindow):
        # switchboard callback for "set misorientation symmetry",
        # which is issued by the menu command.
        if gfxwindow is not self.toolbox.gfxwindow():
            return
        val = self.getNonGUIPlugIn().symmetry
        assert val is not None
        self.symtext.set_text(val.displayname())
        self.updateMisorientation()
        
    def materialchanged(self, *args, **kwargs):
        self.updateMisorientation()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# The OrientMapPixelInfoPlugIn must be created before the
# MisorientationPixelInfoPlugIn in each graphics window, so it must be
# registered first here.

pixelinfoGUIplugin.registerPlugInClass(OrientMapPixelInfoPlugIn)
pixelinfoGUIplugin.registerPlugInClass(MisorientationPixelInfoPlugIn)
