# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Tests for the isotropic 4th rank tensor widget
import tests

checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer

# Make a material
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 5.0000000000000e+00)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 7.0000000000000e+00)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 1.3000000000000e+01)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 1.6000000000000e+01)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 1.8000000000000e+01)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 2.1000000000000e+01)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 2.4000000000000e+01)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 2.7000000000000e+01)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 3.0000000000000e+01)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 3.3000000000000e+01)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 3.5000000000000e+01)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 3.7000000000000e+01)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 3.9000000000000e+01)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 4.1000000000000e+01)
findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 4.3000000000000e+01)
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('OOF2').resize(782, 545)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New

# Copy the isotropic elasticity property
getTree("PropertyTree").simulateSelect(Gtk.TreePath([0]))
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 0, 0]))
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Isotropic
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic').resize(192, 92)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0, 0]), open_all=False)
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy

# Open the instance and check its parameters in the cij representation
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint CijIsoCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance').resize(538, 330)
assert tests.convertibleCij("Isotropic;instance", c11=1.0, c12=0.5, c13=0.5, c22=1.0, c23=0.5, c33=1.0, c44=0.25, c55=0.25, c66=0.25)

# Change c11
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:Cij:0,0').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:Cij:0,0').set_text('2')
widget_0=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:Cij:0,0')
if widget_0: wevent(widget_0, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
# Check that other input fields changed accordingly
assert tests.convertibleCij("Isotropic;instance", c11=2.0, c12=0.5, c13=0.5, c22=2.0, c23=0.5, c33=2.0, c44=0.75, c55=0.75, c66=0.75)

# Check sensitization
assert tests.sensitiveConvCij("Isotropic;instance", c11=1, c12=1, c44=1)

# Switch to Lame representation
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance').resize(538, 330)
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Lame']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
widget_2=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:Cij:0,0')
if widget_2: wevent(widget_2, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_2.get_window())
del widget_2
assert tests.other('Isotropic;instance', 'Lame', lmbda=0.5, mu=0.75)

# Switch to E & nu
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance').resize(538, 330)
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['E and nu']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.other('Isotropic;instance', 'E and nu', young=1.8, poisson=0.2)

# Switch to bulk and shear
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance').resize(538, 330)
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Bulk and Shear']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.other('Isotropic;instance', 'Bulk and Shear', bulk=1.0, shear=0.75)

# Change the bulk modulus
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:Bulk and Shear:bulk').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:Bulk and Shear:bulk').set_text('2')

# Now switch to E and nu (aka poisson)
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['E and nu']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.other('Isotropic;instance', 'E and nu', young=2.0, poisson=1./3.)

# Switch to Lame
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Lame']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.other('Isotropic;instance', 'Lame', lmbda=1.5, mu=0.75)

# Switch to Cij
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Cij']).activate() # MenuItemLogger
checkpoint CijIsoCijklWidget updated
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.convertibleCij('Isotropic;instance', c11=3.0, c12=1.5, c13=1.5, c22=3.0, c23=1.5, c33=3.0, c44=0.75, c55=0.75, c66=0.75)

# Switch back to E and nu
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance').resize(538, 330)
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['E and nu']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.other('Isotropic;instance', 'E and nu', young=2.0, poisson=1./3.)

# Set nu to an illegal value and try to switch to bulk & shear
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:E and nu:poisson').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:E and nu:poisson').set_text('0.5')
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Bulk and Shear']).activate() # MenuItemLogger
checkpoint toplevel widget mapped Warning
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Warning').resize(276, 68)
findWidget('Warning:widget_GTK_RESPONSE_OK').clicked()
assert tests.other('Isotropic;instance', 'Bulk and Shear', bulk=2.0, shear=0.75)

# Switch to Cij
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance').resize(538, 330)
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Cij']).activate() # MenuItemLogger
checkpoint CijIsoCijklWidget updated
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.convertibleCij('Isotropic;instance', c11=3.0, c12=1.5, c13=1.5, c22=3.0, c23=1.5, c33=3.0, c44=0.75, c55=0.75, c66=0.75)

# Add this property to the material
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance').resize(538, 330)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.instance
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Make a copy of the isotropic elasticity instance
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Isotropic;instance
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;instance').resize(192, 92)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;instance:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy

# Parametrize instance_2
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint CijIsoCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_2
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_2').resize(538, 330)
assert tests.convertibleCij('Isotropic;instance_2', c11=3.0, c12=1.5, c13=1.5, c22=3.0, c23=1.5, c33=3.0, c44=0.75, c55=0.75, c66=0.75)

# Switch to Lame
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_2').resize(538, 330)
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_2:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_2:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Lame']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.other('Isotropic;instance_2', 'Lame', lmbda=1.5, mu=0.75)

# Change lmbda
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_2').resize(538, 330)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_2:cijkl:Lame:lmbda').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_2:cijkl:Lame:lmbda').set_text('3')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_2:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.instance_2

# Add instance_2 to material
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Make a copy, instance_3
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Isotropic;instance_2
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;instance_2').resize(192, 92)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;instance_2:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy
# Open instance_3

findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3').resize(209, 170)
assert tests.other('Isotropic;instance_3', 'Lame', lmbda=3.0, mu=0.75)

# Switch to E and nu
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['E and nu']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3').resize(217, 170)
assert tests.other('Isotropic;instance_3', 'E and nu', young=2.1, poisson=0.4)

# Set poisson illegally but don't try to convert it.  Just save. No
# error message is generated.
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:cijkl:E and nu:poisson').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:cijkl:E and nu:poisson').set_text('0.5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.instance_3

# Now re-open the illegal property -- get error message
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Warning
findWidget('Warning').resize(276, 68)
findWidget('Warning:widget_GTK_RESPONSE_OK').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3').resize(217, 170)
assert tests.other('Isotropic;instance_3', 'E and nu', young=2.1, poisson=0.5)

# Fix illegal value
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:cijkl:E and nu:poisson').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:cijkl:E and nu:poisson').set_text('0.4')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.instance_3

# Add property to material
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Reopen instance_3
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.0000000000000e+00)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3').resize(217, 170)

# Check unmodified parameters
assert tests.other('Isotropic;instance_3', 'E and nu', young=2.1, poisson=0.4)

# Choose illegal poisson.  Get an error message because the property
# is in a material.
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:cijkl:E and nu:poisson').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:cijkl:E and nu:poisson').set_text('0.5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.instance_3
checkpoint toplevel widget mapped Error
findWidget('Error').resize(266, 162)
findWidget('Error:widget_GTK_RESPONSE_OK').clicked()

# Remove illegal property from material
findWidget('OOF2:Materials Page:Pane:Material:RemoveProperty').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.Remove_property

# Open the illegal property -- get error message
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Warning
findWidget('Warning').resize(276, 68)
findWidget('Warning:widget_GTK_RESPONSE_OK').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3').resize(217, 170)
assert tests.other('Isotropic;instance_3', 'E and nu', young=2.1, poisson=0.5)

# Close illegal property -- no error message bc it's not in a material
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.instance_3

# Add illegal property to the material -- get error message
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint OOF.Material.Add_property
checkpoint toplevel widget mapped Error
findWidget('Error').resize(266, 162)
findWidget('Error:widget_GTK_RESPONSE_OK').clicked()

# Open illegal property -- get error message
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Warning
findWidget('Warning').resize(276, 68)
findWidget('Warning:widget_GTK_RESPONSE_OK').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3').resize(217, 170)
assert tests.other('Isotropic;instance_3', 'E and nu', young=2.1, poisson=0.5)

# Make the illegal property legal again
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:cijkl:E and nu:poisson').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:cijkl:E and nu:poisson').set_text('0.4')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.instance_3

# Add the legal property to the material -- no error message
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Make another copy, instance_4
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Isotropic;instance_3
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;instance_3').resize(192, 92)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;instance_3:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy

# Open instance_4
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6000000000000e+01)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 3]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_4
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_4').resize(217, 170)
assert tests.other('Isotropic;instance_4', 'E and nu', young=2.1, poisson=0.4)

# Change to bulk & shear
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_4:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_4:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Bulk and Shear']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
# Change shear modulus

findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_4:cijkl:Bulk and Shear:shear').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_4:cijkl:Bulk and Shear:shear').set_text('1')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_4:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.instance_4

# Add instance_4 to the material.  The material now contains an
# isotropic elasticity property in each tensor representation.
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Save materials to a file
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Materials']).activate()
checkpoint toplevel widget mapped Dialog-Materials
findWidget('Dialog-Materials').resize(192, 227)
findWidget('Dialog-Materials:filename').set_text('i')
findWidget('Dialog-Materials:filename').set_text('is')
findWidget('Dialog-Materials:filename').set_text('iso')
findWidget('Dialog-Materials:filename').set_text('isom')
findWidget('Dialog-Materials:filename').set_text('isoma')
findWidget('Dialog-Materials:filename').set_text('isomat')
findWidget('Dialog-Materials:filename').set_text('isomat.')
findWidget('Dialog-Materials:filename').set_text('isomat.d')
findWidget('Dialog-Materials:filename').set_text('isomat.da')
findWidget('Dialog-Materials:filename').set_text('isomat.dat')
findWidget('Dialog-Materials:materials').get_selection().unselect_all()
findWidget('Dialog-Materials:materials').get_selection().select_path(Gtk.TreePath([0]))
findWidget('Dialog-Materials:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Materials
assert tests.filediff('isomat.dat')

# Delete material
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(192, 86)
findWidget('Questioner:OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.Delete

# Load material from file
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('i')
findWidget('Dialog-Data:filename').set_text('is')
findWidget('Dialog-Data:filename').set_text('ism')
findWidget('Dialog-Data:filename').set_text('isma')
findWidget('Dialog-Data:filename').set_text('ismat')
findWidget('Dialog-Data:filename').set_text('ismat.')
findWidget('Dialog-Data:filename').set_text('ismat.d')
findWidget('Dialog-Data:filename').set_text('ismat.da')
findWidget('Dialog-Data:filename').set_text('ismat.dat')
findWidget('Dialog-Data:filename').set_text('isomat.dat')
findWidget('Dialog-Data:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.File.Load.Data

# Open isotropic elasticity instance to check its values
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 0, 0, 0]))
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint CijIsoCijklWidget updated
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance').resize(538, 330)
assert tests.convertibleCij('Isotropic;instance', c11=3.0, c12=1.5, c13=1.5, c22=3.0, c23=1.5, c33=3.0, c44=0.75, c55=0.75, c66=0.75)

# Close instance
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance').resize(538, 330)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance:widget_GTK_RESPONSE_CANCEL').clicked()

# Open and check instance_2
findWidget('OOF2').resize(782, 545)
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 0, 0, 1]))
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_2
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_2').resize(209, 170)
assert tests.other('Isotropic;instance_2', 'Lame', lmbda=3.0, mu=0.75)

findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_2:widget_GTK_RESPONSE_CANCEL').clicked()

# Open and check instance_3
findWidget('OOF2').resize(782, 545)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList').get_selection().select_path(Gtk.TreePath([2]))
checkpoint property selected
checkpoint Materials page updated
tree=findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([2]), column)
tree=findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([2]), column)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3').resize(217, 170)
assert tests.other('Isotropic;instance_3', 'E and nu', young=2.1, poisson=0.4)

findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_3:widget_GTK_RESPONSE_CANCEL').clicked()

# Open and check instance_4
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 0, 0, 3]))
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_4
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_4').resize(206, 170)
assert tests.other('Isotropic;instance_4', 'Bulk and Shear', bulk=3.5, shear=1.0)

findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;instance_4:widget_GTK_RESPONSE_CANCEL').clicked()
findWidget('OOF2').resize(782, 545)
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
