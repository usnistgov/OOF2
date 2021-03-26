# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## TODO: After loading a script that uses a secret Property, the "Add
## Property" button doesn't sensitize correctly.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.engine import material
from ooflib.common import debug
from ooflib.common import microstructure
from ooflib.common import runtimeflags
from ooflib.common.IO import mainmenu
from ooflib.common.IO import reporter
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gfxLabelTree
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import materialmanager
from ooflib.engine import propertyregistration

AllProperties = propertyregistration.AllProperties

#Interface branch
from ooflib.engine.IO import interfaceparameters

from gi.repository import Gtk
import types, string

OOF = mainmenu.OOF

class MaterialsPage(oofGUI.MainPage):
    def __init__(self):
        self.built = False
        oofGUI.MainPage.__init__(self, name="Materials", ordering=100,
                                 tip='Define Materials')
        # Pane has Properties on left, Materials on right.
        pane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                         wide_handle=True)
        gtklogger.setWidgetName(pane, 'Pane')
        self.gtk.add(pane)

        self.propertypane = PropertyPane(self)
        self.materialpane = MaterialPane(self)
        pane.pack1(self.propertypane.gtk, resize=False, shrink=False)
        pane.pack2(self.materialpane.gtk, resize=True, shrink=False)
        gtklogger.connect_passive(pane, 'notify::position')

        self.built = True

    def installed(self):
        self.sensitize()

    def currentMaterialName(self):
        return self.materialpane.currentMaterialName()
    def currentMaterial(self):
        return self.materialpane.currentMaterial()

    # Returns a tuple, (name, property-registration-object)
    def current_property(self):
        return self.propertypane.current_property
    
    def current_property_name(self):
        prop = self.current_property()
        if prop:
            return prop[0]
        return None
    
    def sensitize(self):
        # When recording, this is called twice after each
        # TreeSelectionLogger changed signal.  When replaying, it's
        # called just once.
        if self.sensitizable():
            self.propertypane.do_sensitize()
            self.materialpane.do_sensitize()
            gtklogger.checkpoint("Materials page updated")

########################################################################
########################################################################

class PropertyPane:
    def __init__(self, parent):
        debug.mainthreadTest()
        self.parent = parent
        # Property selection state lives here.  When not None,
        # current_property is a tuple, (name, propertyregistration).
        # current_property mirrors the selection state of the
        # GfxLabelTree self.propertytree.
        self.current_property = None

        self.gtk = Gtk.Frame(
            label='Property', shadow_type=Gtk.ShadowType.IN,
            margin_start=2, margin_end=gtkutils.handle_padding,
            margin_top=2, margin_bottom=2)
        gtklogger.setWidgetName(self.gtk, 'Property')
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                       margin=2)
        
        self.gtk.add(vbox)

        # Button box above the Property Tree
        buttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                            margin=2)
        vbox.pack_start(buttonbox, expand=False, fill=False, padding=0)

        self.copybutton = gtkutils.StockButton('edit-copy-symbolic', 'Copy...')
        gtklogger.setWidgetName(self.copybutton, 'Copy')
        gtklogger.connect(self.copybutton, 'clicked', self.on_copy_property)
        self.copybutton.set_tooltip_text(
            'Create a named copy of the currently selected property')
        buttonbox.pack_start(self.copybutton,
                             expand=True, fill=False, padding=0)

        self.parambutton = gtkutils.StockButton('document-edit-symbolic',
                                                'Parametrize...')
        gtklogger.setWidgetName(self.parambutton, 'Parametrize')
        gtklogger.connect(self.parambutton, 'clicked', self.parametrize)
        self.parambutton.set_tooltip_text(
            "Set parameters for the currently selected Property.")
        buttonbox.pack_start(self.parambutton,
                             expand=True, fill=False, padding=0)

        self.deletebutton = gtkutils.StockButton('edit-delete-symbolic',
                                                 'Delete')
        gtklogger.setWidgetName(self.deletebutton, 'Delete')
        gtklogger.connect(self.deletebutton, 'clicked', self.GUIdelete)
        self.deletebutton.set_tooltip_text(
            "Delete the currently selected Property.")
        buttonbox.pack_start(self.deletebutton,
                             expand=True, fill=False, padding=0)

        # Scrolling window containing the Property Tree
        scroll = Gtk.ScrolledWindow(shadow_type=Gtk.ShadowType.IN,
                                    margin=2)
        gtklogger.logScrollBars(scroll, "PropertyScroll")
        vbox.pack_start(scroll, expand=True, fill=True, padding=0)
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC,
                          Gtk.PolicyType.AUTOMATIC)
        self.propertytree = gfxLabelTree.GfxLabelTree(AllProperties.data,
                                                      "PropertyTree",
                                                      expand=None,
                                                      callback=self.proptreeCB)
        self.propertytree.setRightClickCB(self.parametrize)
        scroll.add(self.propertytree.gtk)


        # The Load button.
        self.loadbutton = gtkutils.StockButton("go-next-symbolic",
                                               "Add Property to Material",
                                               reverse=True,
                                               halign=Gtk.Align.CENTER,
                                               margin=3)
        gtklogger.setWidgetName(self.loadbutton, 'Add')
        vbox.pack_start(self.loadbutton, expand=False, fill=False, padding=0)
        self.loadbutton.set_tooltip_text(
            "Load the currently selected property into the current material.")
        gtklogger.connect(self.loadbutton, 'clicked',self.on_prop_load)

        # Utility callbacks.
        self.propertytree.gtk.connect("destroy", self.on_destroy)

        switchboard.requestCallbackMain("new property", self.newPropCB)

    def sensitize(self, *args):
        self.parent.sensitize()
    def do_sensitize(self):
        debug.mainthreadTest()
        sensitivity = self.current_property is not None
        deletable = sensitivity and hasattr(self.current_property[1], "parent")
        
        self.copybutton.set_sensitive(sensitivity)
        self.parambutton.set_sensitive(sensitivity)
        self.deletebutton.set_sensitive(deletable)

        matselected = self.parent.currentMaterialName() is not None

        #Interface branch
        currentmat=self.parent.currentMaterial()
        
        if runtimeflags.surface_mode:
            isInterfaceMat=(currentmat is not None and
                            currentmat.type()==material.MATERIALTYPE_INTERFACE)
        else:
            isInterfaceMat=False
            
        isInterfaceProp=(sensitivity and 
                         self.current_property[1].interfaceCompatibility() != 
                         interfaceparameters.COMPATIBILITY_BULK_ONLY)
        isBulkMat=(currentmat is not None and 
                   currentmat.type()==material.MATERIALTYPE_BULK)
        isBulkProp= (sensitivity and 
                     self.current_property[1].interfaceCompatibility() !=
                     interfaceparameters.COMPATIBILITY_INTERFACE_ONLY)
        #Check if the currently selected property node and the current
        #material are compatible
        matpropcompatible = ((isBulkMat and isBulkProp) or
                             (isInterfaceMat and isInterfaceProp))
        self.loadbutton.set_sensitive(sensitivity and matselected and
                                      matpropcompatible)

        if sensitivity:
            mainmenu.OOF.File.Save.Property.enable()
        else:
            mainmenu.OOF.File.Save.Property.disable()
        

    # Although the "Add Property to Material" button is in the
    # Property pane, adding a property is a material-menu operation.
    def on_prop_load(self,button):      # gtk callback
        propname = self.current_property[0]
        mat = self.parent.currentMaterial()
        OOF.Material.Add_property(name=mat.name(), property=propname)
        self.parent.materialpane.select_property(propname)

    #######################################################################
    #
    
    # Master property selection and deselection routines, called
    # in response to both materialsPane and propertyPane selection events.

    def select_property(self, name):
        debug.mainthreadTest()
        treenode = AllProperties.data[name]
        self.propertytree.blockSignals()
        if treenode.object is not None:
            self.propertytree.expandToPath(name)
            self.propertytree.selectObject(treenode.object)
            self.current_property = (name, treenode.object)
        else:
            self.propertytree.deselect()
            self.current_property = None
        self.propertytree.unblockSignals()
        self.sensitize()
        gtklogger.checkpoint("property selected")
        
    def deselect_property(self, name):
        debug.mainthreadTest()
        if self.current_property: # and self.propertytree:
            assert self.current_property[0] == name
            self.propertytree.blockSignals()
            self.propertytree.deselect()
            self.propertytree.unblockSignals()
            self.current_property = None
            self.sensitize()
            gtklogger.checkpoint("property deselected")
        else:
            raise ooferror.ErrPyProgrammingError("Inconsistent selection state")
        
    def proptreeCB(self, signal, treenode): # GfxLabelTree callback
        prop_name = treenode.path()
        if signal == "select":
            # MaterialPane.select_property must be called first, or
            # else when select_property calls sensitize, the Remove
            # Property from Material button will be sensitized
            # incorrectly.
            self.parent.materialpane.select_property(prop_name)
            self.select_property(prop_name)
        elif signal == "deselect":
            self.parent.materialpane.deselect_property(prop_name)
            self.deselect_property(prop_name)
        elif signal == "doubleclick":
            self.select_property(prop_name)
            self.parametrize()
            
    def newPropCB(self, propertyregistration): # switchboard 'new property'
        propname = propertyregistration.name()
        self.select_property(propname)
        self.parent.materialpane.select_property(propname)

    ####################################################################
    
    # Callback for the parametrize button, brings up a dialog box to
    # fill in the parameters of the currently-selected property.
    def parametrize(self, gtkobj=None):
        if self.current_property:
            reg = self.current_property[1]
            if reg is not None:
                # Get the associated LabelTree node.
                ltn = AllProperties.data.reverse_dict[reg]
                menuitem = ltn.menus[AllProperties.parametrizekey]
                # Copy parameters out of the PropertyRegistration, not
                # the menu item. 
                params = [p for p in reg.params if p.name != 'name']
                if parameterwidgets.getParameters(
                        title='Parametrize '+self.current_property[0],
                        parentwindow=self.parent.gtk.get_toplevel(),
                        *params):
                    menuitem.callParamList(params)
            else:                       # should never happen
                reporter.report("Property is not parametrizable.")
        else:                           # should never happen
            reporter.report("No property selected.")
            
    def on_destroy(self,gtk):
        self.gtktree = None
        
    def on_copy_property(self, button): # gtk callback
        menuitem = OOF.Property.Copy
        newnameparam = menuitem.get_arg('new_name')
        if parameterwidgets.getParameters(
                newnameparam,
                parentwindow=self.parent.gtk.get_toplevel(),
                title='Copy property ' + self.current_property[0]):
            if newnameparam.nontrivial():
                menuitem.callWithDefaults(property=self.current_property[0])

    def GUIdelete(self, gtk):
        if reporter.query("Delete property %s?" % self.current_property[0],
                          "OK", "Cancel", default="OK",
                          parentwindow=self.parent.gtk.get_toplevel()) == "OK":
            OOF.Property.Delete(property=self.current_property[0])

########################################################################
########################################################################

class MaterialPane:
    def __init__(self, parent):
        debug.mainthreadTest()
        self.parent = parent

        self.gtk = Gtk.Frame(
            label='Material', shadow_type=Gtk.ShadowType.IN,
            margin_start=gtkutils.handle_padding, margin_end=2,
            margin_top=2, margin_bottom=2)
        gtklogger.setWidgetName(self.gtk, 'Material')
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                       margin=2)
        self.gtk.add(vbox)

        buttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            spacing=2, margin=2)
        vbox.pack_start(buttonbox, expand=False, fill=False, padding=0)

        self.newmaterial = gtkutils.StockButton('document-new-symbolic',
                                                'New...')
        gtklogger.setWidgetName(self.newmaterial, 'New')
        buttonbox.pack_start(self.newmaterial,
                             expand=True, fill=False, padding=0)
        self.newmaterial.set_tooltip_text('Create a new Material.')
        gtklogger.connect(self.newmaterial, "clicked", self.on_newmaterial)

        self.renamematerial = gtkutils.StockButton('document-edit-symbolic',
                                                   'Rename...')
        gtklogger.setWidgetName(self.renamematerial,'Rename')
        buttonbox.pack_start(self.renamematerial,
                             expand=True, fill=False, padding=0)
        self.renamematerial.set_tooltip_text('Rename this material.')
        gtklogger.connect(self.renamematerial, "clicked", self.on_rename)
        
        self.copymaterial = gtkutils.StockButton('edit-copy-symbolic',
                                                 'Copy...')
        gtklogger.setWidgetName(self.copymaterial, 'Copy')
        buttonbox.pack_start(self.copymaterial,
                             expand=True, fill=False, padding=0)
        self.copymaterial.set_tooltip_text('Create a copy of this material.')
        gtklogger.connect(self.copymaterial, "clicked", self.on_copy)

        self.deletebutton = gtkutils.StockButton('edit-delete-symbolic',
                                                 'Delete')
        gtklogger.setWidgetName(self.deletebutton, 'Delete')
        buttonbox.pack_start(self.deletebutton,
                             expand=True, fill=False, padding=0)
        self.deletebutton.set_tooltip_text('Delete this material.')
        gtklogger.connect(self.deletebutton, "clicked", self.on_delete)

        self.savebutton = gtkutils.StockButton('document-save-symbolic',
                                               'Save...')
        gtklogger.setWidgetName(self.savebutton, 'Save')
        buttonbox.pack_start(self.savebutton,
                             expand=True, fill=False, padding=0)
        self.savebutton.set_tooltip_text('Save this material in a file.')
        gtklogger.connect(self.savebutton, 'clicked', self.on_save)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        vbox.pack_start(hbox, expand=False, fill=False, padding=0)
        
        self.materialName = chooser.ChooserWidget(
            materialmanager.getMaterialNames(),
            callback=self.newMatSelection,
            update_callback=self.newMatSelection,
            name="MaterialList",
            border_width=2)
        hbox.pack_start(Gtk.Label("Material:"),
                        expand=False, fill=False, padding=0)
        hbox.pack_start(self.materialName.gtk,
                        expand=True, fill=True, padding=0)
        self.materialName.gtk.set_tooltip_text('Choose a Material to edit.')

        # The list of Properties belonging to a Material
        self.matproplist = chooser.ScrolledChooserListWidget(
            callback=self.matproplistCB, autoselect=False, name="PropertyList",
            border_width=2)
        vbox.pack_start(self.matproplist.gtk, expand=True, fill=True, padding=0)

        self.removebutton = Gtk.Button('Remove Property from Material',
                                       border_width=2)
        gtklogger.setWidgetName(self.removebutton, "RemoveProperty")
        vbox.pack_start(self.removebutton, expand=False, fill=False, padding=0)
        self.removebutton.set_tooltip_text(
            'Remove the currently selected property from this material.')
        gtklogger.connect(self.removebutton, "clicked", self.on_remove)

        # The buttons for assigning and removing materials from pixels
        # are in a Grid because if we ever get around to finishing the
        # interface materials, the buttons for adding and removing
        # material from interfaces will appear in the second row of
        # the grid.

        assigngrid = Gtk.Grid(halign=Gtk.Align.CENTER,
                              column_homogeneous=True)
        vbox.pack_start(assigngrid, expand=False, fill=False, padding=0)
        
        # Assign materials to pixels
        self.assignbutton = Gtk.Button('Assign to Pixels...',
                                       hexpand=True,
                                       border_width=2)
        gtklogger.setWidgetName(self.assignbutton, "Assign")
        self.assignbutton.set_tooltip_text(
            'Assign the currently selected Material to pixels'
            ' in a Microstructure.')
        gtklogger.connect(self.assignbutton, 'clicked', self.on_assignment)
        assigngrid.attach(self.assignbutton, 0,0, 1,1)
        
        # Remove materials from pixels
        self.removematbutton = Gtk.Button('Remove from Pixels...',
                                          hexpand=True,
                                          border_width=2)
        gtklogger.setWidgetName(self.removematbutton, "RemoveMaterial")
        self.removematbutton.set_tooltip_text(
            'Remove all Materials from pixels in a Microstructure.')
        gtklogger.connect(self.removematbutton, 'clicked',
                          self.on_MS_remove_material)
        assigngrid.attach(self.removematbutton, 1,0, 1,1)

        if runtimeflags.surface_mode:
            # Assign material to interface
            self.assigninterfacebutton = Gtk.Button('Assign to interface...',
                                                    hexpand=True,
                                                    border_width=2)
            gtklogger.setWidgetName(self.assigninterfacebutton,
                                    "AssignInterface")
            self.assigninterfacebutton.set_tooltip_text(
                'Assign the currently selected Material to an interface'
                ' in a Microstructure.')
            gtklogger.connect(self.assigninterfacebutton, 'clicked',
                              self.on_interface_assign)
        
            # Remove material from interface
            self.removeinterfacebutton = Gtk.Button('Remove from interface...',
                                                    hexpand=True,
                                                    border_width=2)
            gtklogger.setWidgetName(self.removeinterfacebutton,
                                    "RemoveInterface")
            self.removeinterfacebutton.set_tooltip_text(
                'Remove Material from an interface in a Microstructure.')
            gtklogger.connect(self.removeinterfacebutton, 'clicked',
                              self.on_interface_remove)

            assigngrid.attach(self.assigninterfacebutton, 1,0, 1,1)
            assigngrid.attach(self.removeinterfacebutton, 1,1, 1,1)
        
        # End of surface-mode block.


        self.updatePropList()
        self.gtk.show_all()

        # Switchboard callbacks.
        switchboard.requestCallbackMain("new_material", self.new_mat)
        switchboard.requestCallbackMain("remove_material", self.del_mat)
        switchboard.requestCallbackMain("prop_added_to_material",
                                        self.prop_added)
        switchboard.requestCallbackMain("prop_removed_from_material",
                                        self.prop_removed)
        switchboard.requestCallbackMain(('new who', 'Microstructure'),
                                        self.sensitize)
        switchboard.requestCallbackMain(('remove who', 'Microstructure'),
                                        self.sensitize)

    def currentMaterialName(self):
        return self.materialName.get_value()
    def currentMaterial(self):
        name = self.currentMaterialName()
        if name:
            return materialmanager.getMaterial(name)
    def currentPropertyName(self):
        return self.matproplist.get_value()
    def currentProperty(self):
        name = self.currentPropertyName()
        if name:
            return AllProperties[name]

    def updatePropList(self):
        matl = self.currentMaterial()
        if matl is not None:
            props = matl.properties()
            self.matproplist.update([prop.name() for prop in props])
            self.matproplist.set_selection(self.parent.current_property_name())
        else:
            self.matproplist.update([])

    def select_property(self, propname):
        debug.mainthreadTest()
        self.matproplist.suppress_signals()
        self.matproplist.set_selection(propname)
        self.matproplist.allow_signals()

    def deselect_property(self, propname):
        debug.mainthreadTest()
        self.matproplist.suppress_signals()
        self.matproplist.set_selection(None)
        self.matproplist.allow_signals()

    #########

    def on_newmaterial(self, button):   # gtk callback
        menuitem = OOF.Material.New
        if parameterwidgets.getParameters(
                title='New material',
                parentwindow=self.parent.gtk.get_toplevel(),
                *menuitem.params):
            if menuitem.get_arg('name').nontrivial():
                menuitem.callWithDefaults()

    def on_delete(self, button):        # gtk callback
        name = self.currentMaterialName()
        if name is not None:
            if reporter.query(
                    "Delete material %s?" % name,
                    'OK', 'Cancel', default='OK',
                    parentwindow=self.parent.gtk.get_toplevel()) == 'OK':
                OOF.Material.Delete(name=name)
            
    def new_mat(self, name):            # switchboard "new_material"
        names = materialmanager.getMaterialNames()
        self.parent.suppressSensitization(True)
        try:
            self.materialName.update(names)
            self.materialName.set_state(name)
            self.updatePropList()
        finally:
            self.parent.suppressSensitization(False)
        self.sensitize()

    def del_mat(self, material):        # switchboard "remove_material"
        self.parent.suppressSensitization(True)
        try:
            self.materialName.update(materialmanager.getMaterialNames())
            self.updatePropList()
        finally:
            self.parent.suppressSensitization(False)
        self.sensitize()

    def on_rename(self, button):     # gtk callback
        oldname = self.currentMaterialName()
        if oldname is not None:
            menuitem = OOF.Material.Rename
            newnameparam = menuitem.get_arg("name")
            if parameterwidgets.getParameters(
                    newnameparam,
                    parentwindow=self.parent.gtk.get_toplevel(),
                    title="New name for the material."):
                if newnameparam.nontrivial():
                    menuitem.callWithDefaults(material=oldname)
            

    def on_copy(self, button):          # gtk callback
        oldname = self.currentMaterialName()
        if oldname is not None:
            menuitem = OOF.Material.Copy
            newnameparam = menuitem.get_arg('new_name')
            if parameterwidgets.getParameters(
                    newnameparam,
                    parentwindow=self.parent.gtk.get_toplevel(),
                    title="Name for the new material."):
                if newnameparam.nontrivial():
                    menuitem.callWithDefaults(name=oldname)

    def on_remove(self, button):        # gtk callback
        name = self.currentMaterialName()
        if name is not None:
            propname = self.currentPropertyName()
            if propname is not None:
                OOF.Material.Remove_property(name=name, property=propname)

    def on_assignment(self, button):    # gtk callback
        menuitem = OOF.Material.Assign
        params = filter(lambda x: x.name != 'material', menuitem.params)
        materialname = self.currentMaterialName()
        if parameterwidgets.getParameters(
                parentwindow=self.parent.gtk.get_toplevel(),
                title="Assign material %s to pixels" % materialname, *params):
            menuitem.callWithDefaults(material=materialname)

    def on_MS_remove_material(self, button): # gtk callback
        menuitem = OOF.Material.Remove
        if parameterwidgets.getParameters(
                parentwindow=self.parent.gtk.get_toplevel(),
                title='Remove the assigned material from pixels',
                *menuitem.params):
            menuitem.callWithDefaults()

    #Interface branch
    def on_interface_assign(self, button):
        menuitem=OOF.Material.Interface.Assign
        params = filter(lambda x: x.name != 'material', menuitem.params)
        materialname = self.currentMaterialName()
        if parameterwidgets.getParameters(
                parentwindow=self.parent.gtk.get_toplevel(),
                title="Assign material %s to an interface" % materialname,
                *params):
            menuitem.callWithDefaults(material=materialname)
    def on_interface_remove(self, button):
        menuitem = OOF.Material.Interface.Remove
        if parameterwidgets.getParameters(
                parentwindow=self.parent.gtk.get_toplevel(),
                title='Remove the assigned material from interface',
                *menuitem.params):
            menuitem.callWithDefaults()

    def on_save(self, button):          # gtk callback
        # Save a single material
        menuitem = OOF.File.Save.Materials
        materialname = self.currentMaterialName()
        params = filter(lambda x: x.name != "materials", menuitem.params)
        if parameterwidgets.getParameters(
                parentwindow=self.parent.gtk.get_toplevel(),
                title='Save Material "%s"' % materialname,
                ident='SaveMat',
                *params):
            menuitem.callWithDefaults(materials=[materialname])
        
    #########

    # switchboard "prop_added_to_material".
    def prop_added(self, material, property):
        if self.currentMaterialName() == material:
            self.parent.suppressSensitization(True)
            try:
                self.updatePropList()
                self.select_property(property)
                self.parent.propertypane.select_property(property)
            finally:
                self.parent.suppressSensitization(False)
        self.sensitize()

    # switchboard "prop_removed_from_material"
    def prop_removed(self, material, name, property):
        if self.currentMaterialName() == material.name:
            self.parent.suppressSensitization(True)
            try:
                self.updatePropList()
            finally:
                self.parent.suppressSensitization(False)
            self.sensitize()

    def sensitize(self, *args):
        self.parent.sensitize()
    def do_sensitize(self, *args):
        debug.mainthreadTest()
        mat_selected = self.currentMaterialName() is not None
        self.renamematerial.set_sensitive(mat_selected)
        self.copymaterial.set_sensitive(mat_selected)
        self.deletebutton.set_sensitive(mat_selected)
        self.savebutton.set_sensitive(mat_selected)

        nmicros = microstructure.microStructures.nActual()
        self.assignbutton.set_sensitive(
            mat_selected and nmicros > 0 and
            self.currentMaterial() is not None and
            self.currentMaterial().type() == material.MATERIALTYPE_BULK)
        self.removematbutton.set_sensitive(nmicros > 0)

        self.removebutton.set_sensitive(self.currentPropertyName() is not None)

        #Interface branch
# Commented out while interfaces are unimplemented.
#         self.assigninterfacebutton.set_sensitive(
#             mat_selected and
#             nmicros > 0 and
#             self.currentMaterial().type()==
#             material.MATERIALTYPE_INTERFACE)
#         self.removeinterfacebutton.set_sensitive(nmicros > 0)

    ##############

    # Callback for the material chooser
    def newMatSelection(self, name):
        self.parent.suppressSensitization(True)
        try:
            self.updatePropList()
        finally:
            self.parent.suppressSensitization(False)
        self.sensitize()

    # Callback for the property list
    def matproplistCB(self, prop, interactive):
        if self.parent.built:
            if interactive:
                propname = self.currentPropertyName()
                self.parent.suppressSensitization(True)
                try:
                    self.parent.propertypane.select_property(propname)
                finally:
                    self.parent.suppressSensitization(False)
            self.sensitize()
        


        
# Create the page
materialspage = MaterialsPage()

#####################################

# GUI callbacks for the save-property menu item in the main FILE menu.

# Save the current property, if selected, etc.
def _save_prop(menuitem):
    global materialspage
    propname = materialspage.current_property_name()
    if propname:
        params = filter(lambda x: x.name!="property", menuitem.params)
        if parameterwidgets.getParameters(ident='PropMenu',
                                          title='Save Property',
                                          parentwindow=oofGUI.gui.gtk,
                                          *params):
            menuitem.callWithDefaults(property=propname)
    else:
        reporter.report("No property selected for saving.")

mainmenu.OOF.File.Save.Property.add_gui_callback(_save_prop)
