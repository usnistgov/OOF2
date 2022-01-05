# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Tests for the cubic rank 4 tensor widgets

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)

findWidget('OOF2').resize(782, 511)
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2').resize(782, 545)
getTree("PropertyTree").simulateSelect(Gtk.TreePath([0]))
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0, 1]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())

# Select Cubic elasticity and copy it.
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 0, 1, 0]))
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Anisotropic;Cubic
findWidget('Dialog-Copy property Mechanical;Elasticity;Anisotropic;Cubic').resize(192, 92)
findWidget('Dialog-Copy property Mechanical;Elasticity;Anisotropic;Cubic:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0, 1, 0]), open_all=False)
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy

# Open the instance
findWidget('OOF2').resize(782, 545)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint CijCubicCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance').resize(538, 330)
assert tests.convertibleCij("Anisotropic;Cubic;instance", c11=1.0, c12=0.5, c13=0.5, c22=1.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)
assert tests.sensitiveConvCij("Anisotropic;Cubic;instance", c11=1, c12=1, c44=1)

# Change c11
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:Cij:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:Cij:0,0').set_text('2')
widget_0=weakRef(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:Cij:0,0'))
if widget_0(): wevent(widget_0(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0().get_window())
checkpoint CijCubicCijklWidget updated

# Click on C_12 and check that other C_ij update correctly
if widget_0(): wevent(widget_0(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0().get_window())
checkpoint CijCubicCijklWidget updated
widget_2=weakRef(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:Cij:0,1'))
if widget_2(): wevent(widget_2(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_2().get_window())
checkpoint CijCubicCijklWidget updated
assert tests.convertibleCij("Anisotropic;Cubic;instance", c11=2.0, c12=0.5, c13=0.5, c22=2.0, c23=0.5, c33=2.0, c44=0.25, c55=0.25, c66=0.25)

# Switch to Lame
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Lame']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
if widget_2(): wevent(widget_2(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_2().get_window())
assert tests.other("Anisotropic;Cubic;instance", "Lame", lmbda=0.5, mu=0.75, aniso=1./3.)

# Switch to E and nu
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['E and nu']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.other("Anisotropic;Cubic;instance", "E and nu", young=1.8, poisson=0.2, aniso=1./3.)

# Switch to bulk and shear
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Bulk and Shear']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.other("Anisotropic;Cubic;instance", "Bulk and Shear", bulk=1.0, shear=0.75, aniso=1./3.)

# Change anisotropy 
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:Bulk and Shear:aniso').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:Bulk and Shear:aniso').set_text('0.5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance').resize(538, 330)
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Cij']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
checkpoint CijCubicCijklWidget updated
assert tests.convertibleCij("Anisotropic;Cubic;instance", c11=2.0, c12=0.5, c13=0.5, c22=2.0, c23=0.5, c33=2.0, c44=0.375, c55=0.375, c66=0.375)

# Switch to Lame
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Lame']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.other("Anisotropic;Cubic;instance", "Lame", lmbda=0.5, mu=0.75, aniso=0.5)

# Switch to E and nu
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['E and nu']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.other("Anisotropic;Cubic;instance", "E and nu", young=1.8, poisson=0.2, aniso=0.5)

# Set nu to an illegal value
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:E and nu:poisson').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:E and nu:poisson').set_text('0.5')

# Switch to Lame and get warning message
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Lame']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
checkpoint toplevel widget mapped Warning
findWidget('Warning').resize(276, 68)
findWidget('Warning:widget_GTK_RESPONSE_OK').clicked()
assert tests.other("Anisotropic;Cubic;instance", "Lame", lmbda=0.5, mu=0.75, aniso=0.5)

# Switch back to E and nu and set illegal value again
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['E and nu']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:E and nu:poisson').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:E and nu:poisson').set_text('0.5')

# Switch to Cij and get error message
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Cij']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
checkpoint toplevel widget mapped Warning
findWidget('Warning').resize(276, 68)
findWidget('Warning:widget_GTK_RESPONSE_OK').clicked()
checkpoint CijCubicCijklWidget updated

# Switch back to E and nu, check for legal value, and save
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['E and nu']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.other("Anisotropic;Cubic;instance", "E and nu", young=1.8, poisson=0.2, aniso=0.5)

findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Cubic.instance

# Create Material and add instance to it
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Copy the instance to create instance_2
findWidget('OOF2').resize(782, 545)
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Anisotropic;Cubic;instance
findWidget('Dialog-Copy property Mechanical;Elasticity;Anisotropic;Cubic;instance').resize(192, 92)
findWidget('Dialog-Copy property Mechanical;Elasticity;Anisotropic;Cubic;instance:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy

# Open instance_2
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 0, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_2
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_2').resize(217, 206)
assert tests.other("Anisotropic;Cubic;instance_2", "E and nu", young=1.8, poisson=0.2, aniso=0.5)

# Switch to Cij
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_2:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_2:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Cij']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
checkpoint CijCubicCijklWidget updated
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_2').resize(538, 330)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_2:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Cubic.instance_2

# Add to Material
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Make a copy of instance_2
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Anisotropic;Cubic;instance_2
findWidget('Dialog-Copy property Mechanical;Elasticity;Anisotropic;Cubic;instance_2').resize(192, 92)
findWidget('Dialog-Copy property Mechanical;Elasticity;Anisotropic;Cubic;instance_2:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy

# Open instance_3
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1000000000000e+01)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 0, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint CijCubicCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_3
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_3').resize(538, 330)
assert tests.convertibleCij("Anisotropic;Cubic;instance_3", c11=2.0, c12=0.5, c13=0.5, c22=2.0, c23=0.5, c33=2.0, c44=0.375, c55=0.375, c66=0.375)

# Switch to Lame and change mu
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_3').resize(538, 330)
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_3:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_3:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Lame']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_3:cijkl:Lame:mu').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_3:cijkl:Lame:mu').set_text('0.5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_3:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Cubic.instance_3

# Add to material
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Copy instance_3
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Anisotropic;Cubic;instance_3
findWidget('Dialog-Copy property Mechanical;Elasticity;Anisotropic;Cubic;instance_3').resize(192, 92)
findWidget('Dialog-Copy property Mechanical;Elasticity;Anisotropic;Cubic;instance_3:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy

# Open instance_4 
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 0, 3]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_4
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_4').resize(209, 206)
assert tests.other('Anisotropic;Cubic;instance_4', 'Lame', lmbda=0.5, mu=0.5, aniso=0.5)

# Switch to bulk and shear
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_4:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_4:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Bulk and Shear']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger

# Change anisotropy
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_4:cijkl:Bulk and Shear:aniso').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_4:cijkl:Bulk and Shear:aniso').set_text('0.3')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_4:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Cubic.instance_4
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Save the material
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Materials']).activate()
checkpoint toplevel widget mapped Dialog-Materials
findWidget('Dialog-Materials').resize(192, 227)
findWidget('Dialog-Materials:filename').set_text('c')
findWidget('Dialog-Materials:filename').set_text('cu')
findWidget('Dialog-Materials:filename').set_text('cub')
findWidget('Dialog-Materials:filename').set_text('cubi')
findWidget('Dialog-Materials:filename').set_text('cubic')
findWidget('Dialog-Materials:filename').set_text('cubics')
findWidget('Dialog-Materials:filename').set_text('cubics.')
findWidget('Dialog-Materials:filename').set_text('cubics.d')
findWidget('Dialog-Materials:filename').set_text('cubics.da')
findWidget('Dialog-Materials:filename').set_text('cubics.dat')
findWidget('Dialog-Materials:materials').get_selection().unselect_all()
findWidget('Dialog-Materials:materials').get_selection().select_path(Gtk.TreePath([0]))
findWidget('Dialog-Materials:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Materials
assert tests.filediff('cubics.dat')

# Delete the Material
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(192, 86)
findWidget('Questioner:OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.Delete

# Delete the property instances
findWidget('OOF2:Materials Page:Pane:Property:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(402, 86)
findWidget('Questioner:OK').clicked()
getTree('PropertyTree').simulateUnselect()
checkpoint Materials page updated
checkpoint property deselected
checkpoint OOF.Property.Delete
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Cubic:instance_2')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(402, 86)
findWidget('Questioner:OK').clicked()
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Cubic:instance_3')
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Delete
findWidget('OOF2:Materials Page:Pane:Property:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(402, 86)
findWidget('Questioner:OK').clicked()
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Hexagonal')
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Delete
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Cubic:instance')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(389, 86)
findWidget('Questioner:OK').clicked()
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Anisotropic:Hexagonal')
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Delete

# Load the data file
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('c')
findWidget('Dialog-Data:filename').set_text('cu')
findWidget('Dialog-Data:filename').set_text('cub')
findWidget('Dialog-Data:filename').set_text('cubi')
findWidget('Dialog-Data:filename').set_text('cubis')
findWidget('Dialog-Data:filename').set_text('cubis.')
findWidget('Dialog-Data:filename').set_text('cubis.d')
findWidget('Dialog-Data:filename').set_text('cubis.da')
findWidget('Dialog-Data:filename').set_text('cubis.dat')
findWidget('Dialog-Data:filename').set_text('cubics.dat')
findWidget('Dialog-Data:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.File.Load.Data
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0, 1, 0]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())

# Open the cubic instances and check parameters
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 0, 1, 0, 0]))
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance').resize(217, 206)
assert tests.other('Anisotropic;Cubic;instance', 'E and nu', young=1.8, poisson=0.2, aniso=0.5)

findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance:widget_GTK_RESPONSE_CANCEL').clicked()
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 0, 1, 0, 1]))
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 0, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint CijCubicCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_2
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_2').resize(538, 330)
assert tests.convertibleCij('Anisotropic;Cubic;instance_2', c11=2.0, c12=0.5, c13=0.5, c22=2.0, c23=0.5, c33=2.0, c44=0.375, c55=0.375, c66=0.375)

findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_2:widget_GTK_RESPONSE_CANCEL').clicked()
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 0, 1, 0, 2]))
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 0, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_3
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_3').resize(209, 206)
assert tests.other('Anisotropic;Cubic;instance_3', 'Lame', lmbda=0.5, mu=0.5, aniso=0.5)

findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_3:widget_GTK_RESPONSE_CANCEL').clicked()
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 0, 1, 0, 3]))
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 1, 0, 3]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_4
findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_4').resize(206, 206)
assert tests.other('Anisotropic;Cubic;instance_4', 'Bulk and Shear', bulk=0.8333333333, shear=0.5, aniso=0.3)

findWidget('Dialog-Parametrize Mechanical;Elasticity;Anisotropic;Cubic;instance_4:widget_GTK_RESPONSE_CANCEL').clicked()
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Python_Log']).activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(192, 122)
findWidget('Dialog-Python_Log:filename').set_text('s')
findWidget('Dialog-Python_Log:filename').set_text('se')
findWidget('Dialog-Python_Log:filename').set_text('ses')
findWidget('Dialog-Python_Log:filename').set_text('sess')
findWidget('Dialog-Python_Log:filename').set_text('sessi')
findWidget('Dialog-Python_Log:filename').set_text('sessio')
findWidget('Dialog-Python_Log:filename').set_text('session')
findWidget('Dialog-Python_Log:filename').set_text('session.')
findWidget('Dialog-Python_Log:filename').set_text('session.l')
findWidget('Dialog-Python_Log:filename').set_text('session.lo')
findWidget('Dialog-Python_Log:filename').set_text('session.log')
findWidget('Dialog-Python_Log:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff("session.log")

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
