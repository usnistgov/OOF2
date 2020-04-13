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
from ooflib.common import labeltree
from ooflib.common import utils
from ooflib.common.IO import whoville
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import boundarybuilder
from ooflib.engine import skeletoncontext
from ooflib.engine.IO import boundarymenu

from gi.repository import Gtk

# TODO: Display interface material, if any.

class SkeletonBoundaryPage(oofGUI.MainPage):
    def __init__(self):
        self.built = False
        oofGUI.MainPage.__init__(self, name="Skeleton Boundaries",
                                 ordering = 150,
                                 tip = "Create and orient boundaries.")

        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(mainbox)

        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            halign=Gtk.Align.CENTER, spacing=2)
        mainbox.pack_start(centerbox, expand=False, fill=False, padding=0)
        
        self.skelwidget = whowidget.WhoWidget(whoville.getClass('Skeleton'),
                                              scope=self)
        switchboard.requestCallbackMain(self.skelwidget,
                                        self.widgetChanged)
        label = Gtk.Label('Microstructure=', halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.skelwidget.gtk[0],
                             expand=False, fill=False, padding=0)
        label = Gtk.Label('Skeleton=', halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.skelwidget.gtk[1],
                             expand=False, fill=False, padding=0)

        mainpane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                             wide_handle=True)
        gtklogger.setWidgetName(mainpane, 'Pane')
        mainbox.pack_start(mainpane, expand=True, fill=True, padding=0)
        gtklogger.connect_passive(mainpane, 'notify::position')

        boundarylistframe = Gtk.Frame(label="Boundaries",
                                      shadow_type=Gtk.ShadowType.IN)
        gtklogger.setWidgetName(boundarylistframe, 'Boundaries')
        mainpane.pack1(boundarylistframe, resize=False, shrink=False)

        boundarylistbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                                  spacing=2)
        boundarylistframe.add(boundarylistbox)

        # List of all the boundaries.
        self.boundarylist = chooser.ScrolledChooserListWidget(
            callback=self.boundarylistCB,
            dbcallback=self.modifyBoundaryCB,
            autoselect=0,
            name="BoundaryList",
            separator_func=self.chooserSepFunc)
        boundarylistbox.pack_start(self.boundarylist.gtk,
                                   expand=True, fill=True, padding=0)

        boundarybuttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                                    homogeneous=True, spacing=2)
        boundarylistbox.pack_start(boundarybuttonbox,
                                   expand=False, fill=False, padding=0)

        # Buttons that actually do stuff.
        self.newbutton = Gtk.Button("New...")
        gtklogger.setWidgetName(self.newbutton, 'New')
        gtklogger.connect(self.newbutton, "clicked", self.newBoundaryCB)
        self.newbutton.set_tooltip_text(
            "Construct a new boundary in the skeleton and associated meshes.")
        boundarybuttonbox.pack_start(self.newbutton,
                                     expand=True, fill=True, padding=0)

        self.editbutton = Gtk.Button("Modify...")
        gtklogger.setWidgetName(self.editbutton, 'Modify')
        gtklogger.connect(self.editbutton, "clicked", self.modifyBoundaryCB)
        self.editbutton.set_tooltip_text(
            "Modify the attributes of the selected boundary.")
        boundarybuttonbox.pack_start(self.editbutton,
                                     expand=True, fill=True, padding=0)
        
        self.renamebutton = Gtk.Button("Rename...")
        gtklogger.setWidgetName(self.renamebutton, 'Rename')
        gtklogger.connect(self.renamebutton, "clicked", self.renameBoundaryCB)
        self.renamebutton.set_tooltip_text("Rename the selected boundary.")
        boundarybuttonbox.pack_start(self.renamebutton,
                                     expand=True, fill=True, padding=0)

        self.deletebutton = Gtk.Button("Delete")
        gtklogger.setWidgetName(self.deletebutton, 'Delete')
        gtklogger.connect(self.deletebutton, "clicked", self.deleteBoundaryCB)
        self.deletebutton.set_tooltip_text(
            "Delete the selected boundary from the skeleton"
            " and associated meshes.")
        boundarybuttonbox.pack_start(self.deletebutton,
                                     expand=True, fill=True, padding=0)
        
        # TODO LATER: Copying could be added here -- the scenario is
        # that a user may want to make a copy of a boundary, and then
        # edit one of the copies.  Currently boundary editing is
        # primitive (one can only add/remove components), but when
        # visual pointy-clicky boundary editing is added, copying will
        # make sense.

        infoframe = Gtk.Frame(label="Boundary data",
                              shadow_type=Gtk.ShadowType.IN)
        mainpane.pack2(infoframe, resize=True, shrink=True)

        infowindow = Gtk.ScrolledWindow(shadow_type=Gtk.ShadowType.IN)
        gtklogger.logScrollBars(infowindow, "InfoScroll")
        infoframe.add(infowindow)
        infowindow.set_policy(Gtk.PolicyType.AUTOMATIC,
                              Gtk.PolicyType.AUTOMATIC)
        
        self.infotext = Gtk.TextView(name="fixedfont", editable=False,
                                     wrap_mode=Gtk.WrapMode.WORD)
        gtklogger.setWidgetName(self.infotext, 'status')
        infowindow.add(self.infotext)

        self.built = True
        
        # Catches push events *after* the boundaries have been
        # propagated, and also undo/redo events.  "who changed" is
        # too early.
        switchboard.requestCallbackMain("new boundary configuration",
                                        self.newBdyConfigCB)
        switchboard.requestCallbackMain("new boundary created",
                                        self.newBdyCB)
        switchboard.requestCallbackMain("boundary removed",
                                        self.newBdyCB)
        switchboard.requestCallbackMain("boundary renamed",
                                        self.newBdyCB),
        switchboard.requestCallbackMain(("new who", "Microstructure"),
                                        self.newMicrostructureCB)
        self.selectsignals = [
            switchboard.requestCallbackMain("boundary selected",
                                            self.bdySelectedCB),
            switchboard.requestCallbackMain("boundary unselected",
                                            self.bdyUnselectedCB)
            ]

    def installed(self):
        self.updateInfo()
        self.sensitize()
        
    def currentSkeletonContext(self):
        try:
            return skeletoncontext.skeletonContexts[self.skelwidget.get_value()]
        except KeyError:
            return None

    def widgetChanged(self, interactive): # sb callback from skelwidget
        self.updateBdyList()
        self.updateInfo()
        self.sensitize()
        gtklogger.checkpoint("boundary page updated")

    # A separator is inserted in the list of boundary names between
    # the edge boundaries and the point boundaries.  (The separator is
    # a meta-boundary!)  This is done by including a string unlikely
    # to be a boundary name in the list of names sent to the
    # ChooserListWidget, and giving the widget a separator_func that
    # looks for the string.
    ## TODO GTK3: Does the proxy have to be a string?  It would be
    ## more elegant to create an object for that purpose.  Then there
    ## would be no chance of a conflict with boundary name.
    
    separator_proxy = "a string unlikely to be a boundary name"

    def updateBdyList(self):
        skelctxt = self.currentSkeletonContext()
        if skelctxt:
            names = skelctxt.edgeboundaries.keys() + [self.separator_proxy] \
                    + skelctxt.pointboundaries.keys()
            self.boundarylist.update(names)
            # If we've just switched Skeletons, we need make sure that
            # the selected bdy in our list is the same as the one
            # selected in the Skeleton. This is important because it's
            # also displayed on the canvas.
            selbdyname = skelctxt.getSelectedBoundaryName()
            if selbdyname:
                self.boundarylist.set_selection(selbdyname)
        else:
            self.boundarylist.update([])

    def chooserSepFunc(self, model, iter):
        # See comment about separators above.
        return model[iter][0] == self.separator_proxy
        
    def sensitize(self):
        debug.mainthreadTest()
        buttons_alive = self.boundarylist.has_selection()
        self.editbutton.set_sensitive(buttons_alive)
        self.renamebutton.set_sensitive(buttons_alive)
        self.deletebutton.set_sensitive(buttons_alive)
        self.newbutton.set_sensitive(self.currentSkeletonContext() is not None)

    def updateInfo(self):
        debug.mainthreadTest()
        skelctxt = self.currentSkeletonContext()
        if skelctxt is not None:
            bdyname = self.boundarylist.get_value()
            if bdyname is not None:
                bdytext = skelctxt.boundaryInfo(bdyname)
                self.infotext.get_buffer().set_text(
                    "Boundary %s:\n%s" % (bdyname, bdytext))
            else:
                self.infotext.get_buffer().set_text("No boundary selected.")
        else:
            self.infotext.get_buffer().set_text("No skeleton selected.")

    def newMicrostructureCB(self, msname): # sb ("new who", "Microstructure")
        if not self.currentSkeletonContext():
            self.skelwidget.set_value(msname)
            
    def newBdyConfigCB(self, skelctxt): # sb "new boundary configuration"
        if skelctxt is self.currentSkeletonContext():
            self.sensitize()
            self.updateBdyList()
            self.updateInfo()
            gtklogger.checkpoint("boundary page updated")
                    

    def newBdyCB(self, skelctxt):       # sb bdy creation, removal, or renaming
        if skelctxt is self.currentSkeletonContext():
            self.updateBdyList()
            self.updateInfo()
            self.sensitize()
            gtklogger.checkpoint("boundary page updated")

    def bdySelectedCB(self, skelctxt, name): # sb "boundary selected"
        if skelctxt is self.currentSkeletonContext():
            self.inhibitSignals()
            self.boundarylist.set_selection(name)
            self.uninhibitSignals()
            self.updateInfo()
            self.sensitize()
            gtklogger.checkpoint("boundary page updated")
    def bdyUnselectedCB(self, skelctxt): # sb "boundary unselected"
        if skelctxt is self.currentSkeletonContext():
            self.inhibitSignals()
            self.boundarylist.set_selection(None)
            self.uninhibitSignals()
            self.updateInfo()
            self.sensitize()
            gtklogger.checkpoint("boundary page updated")
    def inhibitSignals(self):
        debug.mainthreadTest()
        for sig in self.selectsignals:
            sig.block()
    def uninhibitSignals(self):
        debug.mainthreadTest()
        for sig in self.selectsignals:
            sig.unblock()

    def boundarylistCB(self, bdyobj, interactive): # ChooserListWidget callback
        if self.built and interactive:
            skelctxt = self.currentSkeletonContext()
            if skelctxt:
                bdyname = self.boundarylist.get_value()
                if bdyname:
                    skelctxt.selectBoundary(bdyname)
                else:
                    skelctxt.unselectBoundary()
            self.sensitize()
            self.updateInfo()
            gtklogger.checkpoint("boundary page updated")

    # Context-sensitivity is built in to the DirectorWidget.
    def newBoundaryCB(self, gtkobj):    # button callback
        menuitem = boundarymenu.boundarymenu.Construct
        nameparam =  menuitem.get_arg('name')
        builderparam = menuitem.get_arg('constructor')
        if parameterwidgets.getParameters(
            nameparam, builderparam, title="New Boundary",scope=self):
            menuitem.callWithDefaults(skeleton=self.skelwidget.get_value())
    
    def modifyBoundaryCB(self, *args): # button callback
        # The parameter widget needs to know what types of modifiers to
        # present -- this can be passed through via the "parameter",
        # which should have its ".modifiertype" attribute set to the
        # same as the current boundary object.

        menuitem = boundarymenu.boundarymenu.Modify
        modparam = menuitem.get_arg('modifier')

        skelctxt = skeletoncontext.skeletonContexts[
            self.skelwidget.get_value()]
        bdyobj = skelctxt.getBoundary(self.boundarylist.get_value())

        # Hang the extra data we need on the parameter dialog box --
        # it's a widgetscope, so the enclosed widgets can navigate to
        # it easily, and it has the same lifetime as the data in
        # question.  The price of this is that we have to do the
        # dialog operations ourselves.

        dialog_extra = {'modifiertype' : bdyobj.modifiertype,
                       'boundaryname' : self.boundarylist.get_value() }
        
        
        if parameterwidgets.getParameters(
            modparam, title="Boundary modifier", scope=self,
            dialog_data=dialog_extra):
            menuitem.callWithDefaults(skeleton=self.skelwidget.get_value(),
                                      boundary=self.boundarylist.get_value())

    def renameBoundaryCB(self, gtkobj): # button callback
        menuitem = boundarymenu.boundarymenu.Rename
        newname = menuitem.get_arg('name')
        oldname = self.boundarylist.get_value()
        newname.set(oldname)
        if parameterwidgets.getParameters(
            newname, title="New name for this boundary"):
            menuitem.callWithDefaults(
                skeleton=self.skelwidget.get_value(),
                boundary=self.boundarylist.get_value())

    def deleteBoundaryCB(self, gtkobj): # button callback
        menuitem = boundarymenu.boundarymenu.Delete
        menuitem(skeleton=self.skelwidget.get_value(),
                 boundary=self.boundarylist.get_value())

        
    
sbp = SkeletonBoundaryPage()
