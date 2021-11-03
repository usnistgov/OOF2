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
from ooflib.common import runtimeflags
from ooflib.common.IO import mainmenu
from ooflib.common.IO import whoville
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import whowidget
import ooflib.common.microstructure

## TODO: This file has been converted to Gtk3 only superficially.  It
## may not work properly, since the interface code has never been
## completed.

from gi.repository import Gtk

class InterfacePage(oofGUI.MainPage):
    def __init__(self):
        self.built = False

        oofGUI.MainPage.__init__(
            self, name="Interfaces",
            ordering = 105,
            tip = "Create named one-dimensional interfaces.")

        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(mainbox)

        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            halign=Gtk.Align.CENTER, spacing=2)
        mainbox.pack_start(centerbox, expand=0, fill=0, padding=0)

        #skelwidget is really an mswidget
        self.skelwidget = whowidget.WhoWidget(
            whoville.getClass('Microstructure'), scope=self)
        switchboard.requestCallbackMain(self.skelwidget,
                                        self.widgetChanged)
        label = Gtk.Label('Microstructure=', halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=0, fill=0, padding=0)
        centerbox.pack_start(self.skelwidget.gtk[0],
                             expand=0, fill=0, padding=0)
        #We might want to include a skeleton in the widget, if an interface
        #is defined in terms of skeleton segments. For now the interface is
        #only associated with a microstructure
        # label = Gtk.Label('Skeleton=', halign=Gtk.Align.END)
        # centerbox.pack_start(label, expand=False, fill=False, padding=0)
        # centerbox.pack_start(self.skelwidget.gtk[1],
        #                      expand=True, fill=True, padding=0)

        mainpane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                             wide_handle=True)
        gtklogger.setWidgetName(mainpane, 'Pane')
        mainbox.pack_start(mainpane, expand=1, fill=1, padding=0)

        interfacelistframe = Gtk.Frame(label="Interfaces",
                                       shadow_type=Gtk.ShadowType.IN)
        gtklogger.setWidgetName(interfacelistframe, 'Interfaces')
        gtklogger.connect_passive(interfacelistframe, 'size-allocate')
        mainpane.pack1(interfacelistframe, resize=0, shrink=0)

        interfacelistbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                                    spacing=2)
        interfacelistframe.add(interfacelistbox)

        # List of all the named interfaces
        self.interfacelist = chooser.ScrolledChooserListWidget(
            callback=self.interfacelistCB,
##            dbcallback=self.modifyBoundaryCB,
            autoselect=0,
            name="InterfaceList"
            )
        interfacelistbox.pack_start(self.interfacelist.gtk,
                                    expand=1, fill=1, padding=0)

        interfacebuttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                                      homogeneous=1, spacing=2)
        interfacelistbox.pack_start(interfacebuttonbox,
                                    expand=0, fill=0, padding=0)

        # Buttons that actually do stuff.
        self.newbutton = Gtk.Button("New...")
        gtklogger.setWidgetName(self.newbutton, 'New')
        gtklogger.connect(self.newbutton, "clicked", self.newInterfaceCB)
        self.newbutton.set_tooltip_text(
            "Construct a new interface in the microstructure and associated meshes.")
        interfacebuttonbox.pack_start(self.newbutton,
                                      expand=1, fill=1, padding=0)

        self.renamebutton = Gtk.Button("Rename...")
        gtklogger.setWidgetName(self.renamebutton, 'Rename')
        gtklogger.connect(self.renamebutton, "clicked", self.renameInterfaceCB)
        self.renamebutton.set_tooltip_text("Rename the selected interface.")
        interfacebuttonbox.pack_start(self.renamebutton,
                                      expand=1, fill=1, padding=0)

        self.deletebutton = Gtk.Button("Delete")
        gtklogger.setWidgetName(self.deletebutton, 'Delete')
        gtklogger.connect(self.deletebutton, "clicked", self.deleteInterfaceCB)
        self.deletebutton.set_tooltip_text(
            "Delete the selected interface from the microstructure and associated meshes.")
        interfacebuttonbox.pack_start(self.deletebutton,
                                      expand=1, fill=1, padding=0)

        ########## Adding and removing interface materials
        materialbuttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                                    homogeneous=1, spacing=2)
        interfacelistbox.pack_start(materialbuttonbox,
                                    expand=0, fill=0, padding=0)
        self.assignmatbutton = Gtk.Button("Assign interface material...")
        gtklogger.setWidgetName(self.assignmatbutton, 'Assign material')
        gtklogger.connect(self.assignmatbutton, "clicked", self.assignmatCB)
        self.assignmatbutton.set_tooltip_text("Assign material to interface.")
        materialbuttonbox.pack_start(self.assignmatbutton,
                                     expand=1, fill=1, padding=0)

        self.removematbutton = Gtk.Button("Remove material")
        gtklogger.setWidgetName(self.removematbutton, 'Remove material')
        gtklogger.connect(self.removematbutton, "clicked", self.removematCB)
        self.removematbutton.set_tooltip_text("Remove material from interface.")
        materialbuttonbox.pack_start(self.removematbutton,
                                     expand=1, fill=1, padding=0)
        
        ####################################

        infoframe = Gtk.Frame(label="Interface details",
                              shadow_type=Gtk.ShadowType.IN)
        mainpane.pack2(infoframe, resize=1, shrink=1)

        infowindow = Gtk.ScrolledWindow(shadow_type=Gtk.ShadowType.IN)
        gtklogger.logScrollBars(infowindow, "InfoScroll")
        infoframe.add(infowindow)
        infowindow.set_policy(Gtk.PolicyType.AUTOMATIC,
                              Gtk.PolicyType.AUTOMATIC)
        
        self.infotext = Gtk.TextView(name="fixedfont",
                                     wrap_mode=Gtk.WrapMode.WORD,
                                     editable=False,
                                     left_margin=5, right_margin=5,
                                     top_margin=5, bottom_margin=5)
        gtklogger.setWidgetName(self.infotext, 'status')
        infowindow.add(self.infotext)

        self.built = True

        switchboard.requestCallbackMain("new interface created",
                                        self.newInterfaceUpdatePageCB)
        switchboard.requestCallbackMain("interface removed",
                                        self.newInterfaceUpdatePageCB)
        switchboard.requestCallbackMain("interface renamed",
                                        self.newInterfaceUpdatePageCB),
##        switchboard.requestCallbackMain("remove_material",self.del_mat)
        #TODO: Enable something like this later?
##        switchboard.requestCallbackMain(("new who", "Microstructure"),
##                                        self.newMicrostructureCB)

        self.selectsignals = [
            switchboard.requestCallbackMain("interface selected",
                                            self.interfaceSelectedCB),
            switchboard.requestCallbackMain("interface unselected",
                                            self.interfaceUnselectedCB)
            ]

    def installed(self):
        self.updateInfo()
        self.sensitize()

    def sensitize(self):
        debug.mainthreadTest()
        buttons_alive = self.interfacelist.has_selection()
        self.newbutton.set_sensitive(self.skelwidget.get_value(depth=1)
                                     is not None)
        self.renamebutton.set_sensitive(buttons_alive)
        self.deletebutton.set_sensitive(buttons_alive)
        self.assignmatbutton.set_sensitive(buttons_alive)
        self.removematbutton.set_sensitive(buttons_alive)

    def newInterfaceCB(self,gtkobj):
        #self.skelwidget.get_value() returns the skeletonpath,
        #e.g. "msname:skelname". Pass depth=1 to get "msname"
        msname=self.skelwidget.get_value(depth=1)
        menuitem=mainmenu.OOF.Microstructure.Interface.New
        params = filter(lambda x: x.name != 'microstructure', menuitem.params)
        if parameterwidgets.getParameters(
                title="Create interface in microstructure %s" % msname,
                parentwindow=self.gtk.get_toplevel(),
                scope=self, *params):
            menuitem.callWithDefaults(microstructure=msname)

    def renameInterfaceCB(self,gtkobj):
        menuitem = mainmenu.OOF.Microstructure.Interface.Rename
        newname = menuitem.get_arg('name')
        oldname = self.interfacelist.get_value()
        newname.set(oldname)
        if parameterwidgets.getParameters(
                newname,
                parentwindow=self.gtk.get_toplevel(),
                title="New name for this interface"):
            menuitem.callWithDefaults(
                microstructure=self.skelwidget.get_value(depth=1),
                interface=self.interfacelist.get_value())

    def deleteInterfaceCB(self,gtkobj):
        menuitem = mainmenu.OOF.Microstructure.Interface.Delete
        menuitem(microstructure=self.skelwidget.get_value(depth=1),
                 interface=self.interfacelist.get_value())

    def assignmatCB(self,gtkobj):
        menuitem = mainmenu.OOF.Material.Interface.Assign
        matparam=menuitem.get_arg('material')
        interfacename=self.interfacelist.get_value()
        if parameterwidgets.getParameters(
                matparam,
                parentwindow=self.gtk.get_toplevel(),
                title="Assign material to interface %s" % interfacename):
            menuitem.callWithDefaults(
                microstructure=self.skelwidget.get_value(depth=1),
                interfaces=[interfacename],
                skeleton=None)

    def removematCB(self,gtkobj):
        menuitem = mainmenu.OOF.Material.Interface.Remove
        #The material parameter is used only to group the list of interfaces
        #in the parameter dialog.
        menuitem(microstructure=self.skelwidget.get_value(depth=1),
                 #material=,
                 interfaces=[self.interfacelist.get_value()])

    def interfacelistCB(self, someobj, interactive):
        # ChooserListWidget callback
        if self.built and interactive:
            msname = self.skelwidget.get_value(depth=1)
            if msname:
                interfacename = self.interfacelist.get_value()
                msobj = ooflib.common.microstructure.microStructures[msname].getObject()
                interfacemsplugin=msobj.getPlugIn("Interfaces")
                if interfacename:
                    interfacemsplugin.selectInterface(interfacename)
                else:
                    interfacemsplugin.unselectInterface()
            self.sensitize()
            self.updateInfo()
            gtklogger.checkpoint("interface page updated")


##    def newMicrostructureCB(self, msname): # sb ("new who", "Microstructure")
##        if not self.currentSkeletonContext():
##            self.skelwidget.set_value(msname)

    def widgetChanged(self, interactive): # sb callback from skelwidget
        self.updateInterfaceList()
        self.updateInfo()
        self.sensitize()
        gtklogger.checkpoint("interface page updated")

    def newInterfaceUpdatePageCB(self,ms):
        #TODO: Check ms with skelwidget?
        self.updateInterfaceList()
        self.updateInfo()
        self.sensitize()
        gtklogger.checkpoint("interface page updated")

    def updateInterfaceList(self):
        msname=self.skelwidget.get_value(depth=1)
        if msname:
            msobj = ooflib.common.microstructure.microStructures[msname].getObject()
            interfacemsplugin=msobj.getPlugIn("Interfaces")
            interfacenames=interfacemsplugin.getInterfaceNames()
            self.interfacelist.update(interfacenames)
            #Isn't this work done by "interface selected/unselected" callbacks?
            #Update: If you switch microstructures, this is needed.
            selinterfacename = interfacemsplugin.getSelectedInterfaceName()
            if selinterfacename:
                self.interfacelist.set_selection(selinterfacename)
        else:
            self.interfacelist.update([])

    def updateInfo(self):
        debug.mainthreadTest()
        msname=self.skelwidget.get_value(depth=1)
        if msname:
            msobj = ooflib.common.microstructure.microStructures[msname].getObject()
            interfacemsplugin=msobj.getPlugIn("Interfaces")
            interfacename = self.interfacelist.get_value()
            if interfacename is not None:
                textdetails = interfacemsplugin.interfaceInfo(interfacename)
                self.infotext.get_buffer().set_text(
                    "Interface %s:\n%s" % (interfacename, textdetails))
            else:
                self.infotext.get_buffer().set_text("No interface selected.")
        else:
            self.infotext.get_buffer().set_text("No microstructure selected.")

    def interfaceSelectedCB(self, ms, interfacename): # sb "boundary selected"
        if self.skelwidget.get_value(depth=1)==ms.name():
            self.inhibitSignals() #Dunno what this does
            self.interfacelist.set_selection(interfacename)
            self.uninhibitSignals() #Dunno what this does
            self.updateInfo()
            self.sensitize()
            gtklogger.checkpoint("interface page updated")
    def interfaceUnselectedCB(self, ms): # sb "interface unselected"
        if self.skelwidget.get_value(depth=1)==ms.name():
            self.inhibitSignals()
            self.interfacelist.set_selection(None)
            self.uninhibitSignals()
            self.updateInfo()
            self.sensitize()
            gtklogger.checkpoint("interface page updated")
    def inhibitSignals(self):
        debug.mainthreadTest()
        for sig in self.selectsignals:
            sig.block()
    def uninhibitSignals(self):
        debug.mainthreadTest()
        for sig in self.selectsignals:
            sig.unblock()

    #A material has been deleted in the materials page. Update this page.
    #If the material is a bulk material, it may cause the demise
    #of one or more named interfaces.
##    def del_mat(self, material):        # switchboard "remove_material"
##        self.updateInterfaceList()
##        self.updateInfo()
##        self.sensitize()
##        gtklogger.checkpoint("interface page updated")

if runtimeflags.surface_mode:
    ifcp = InterfacePage()
