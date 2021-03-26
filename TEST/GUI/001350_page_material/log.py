# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


import tests
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint pixel page sensitized
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 4.6000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 11)
findWidget('Dialog-Create new pixel group:name').insert_text('g', 11)
findWidget('Dialog-Create new pixel group:name').insert_text('r', 1)
findWidget('Dialog-Create new pixel group:name').insert_text('e', 2)
findWidget('Dialog-Create new pixel group:name').insert_text('e', 3)
findWidget('Dialog-Create new pixel group:name').insert_text('n', 4)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
event(Gdk.EventType.BUTTON_PRESS,x= 4.7000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Settings.Graphics_Defaults.New_Layer_Policy
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([13]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1').resize(800, 492)
event(Gdk.EventType.BUTTON_PRESS,x= 6.8000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Color']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 40.0875, 75.525, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 40.0875, 75.525, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Color
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['File', 'Close']).activate()
checkpoint OOF.Graphics_1.File.Close
event(Gdk.EventType.BUTTON_PRESS,x= 3.9000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(289)
assert tests.sensitization2()

# Create a material
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:name').delete_text(0, 11)
findWidget('Dialog-New material:name').insert_text('t', 11)
findWidget('Dialog-New material:name').insert_text('e', 1)
findWidget('Dialog-New material:name').insert_text('s', 2)
findWidget('Dialog-New material:name').insert_text('t', 3)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New
assert tests.sensitization3()
assert tests.materialListCheck('test')

# Clone a color property named green
event(Gdk.EventType.BUTTON_RELEASE,x= 3.3000000000000e+01,y= 5.0000000000000e+00,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 3.3000000000000e+01,y= 7.0000000000000e+00,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Color
findWidget('Dialog-Copy property Color').resize(192, 92)
findWidget('Dialog-Copy property Color:new_name').delete_text(0, 11)
findWidget('Dialog-Copy property Color:new_name').insert_text('g', 11)
findWidget('Dialog-Copy property Color:new_name').insert_text('r', 1)
findWidget('Dialog-Copy property Color:new_name').insert_text('e', 2)
findWidget('Dialog-Copy property Color:new_name').insert_text('e', 3)
findWidget('Dialog-Copy property Color:new_name').insert_text('n', 4)
findWidget('Dialog-Copy property Color:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([0]), open_all=False)
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy
assert tests.propertyTreeCheck('Color:green')

# parametrize the color property
event(Gdk.EventType.BUTTON_RELEASE,x= 6.8000000000000e+01,y= 2.7000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
event(Gdk.EventType.BUTTON_RELEASE,x= 6.8000000000000e+01,y= 2.8000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Color;green
findWidget('Dialog-Parametrize Color;green').resize(279, 206)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:gray:slider').get_adjustment().set_value( 1.3888888888889e-02)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:gray:slider').get_adjustment().set_value( 8.3333333333333e-02)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:gray:slider').get_adjustment().set_value( 1.9444444444444e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:gray:slider').get_adjustment().set_value( 2.6388888888889e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:gray:slider').get_adjustment().set_value( 3.3333333333333e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:gray:slider').get_adjustment().set_value( 4.0277777777778e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:gray:slider').get_adjustment().set_value( 4.1666666666667e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:gray:slider').get_adjustment().set_value( 4.4444444444444e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:gray:slider').get_adjustment().set_value( 4.7222222222222e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:gray:slider').get_adjustment().set_value( 4.8611111111111e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:gray:slider').get_adjustment().set_value( 5.0000000000000e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:gray:slider').get_adjustment().set_value( 5.1388888888889e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:alpha:slider').get_adjustment().set_value( 9.8611111111111e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:alpha:slider').get_adjustment().set_value( 9.5833333333333e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:alpha:slider').get_adjustment().set_value( 9.1666666666667e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:alpha:slider').get_adjustment().set_value( 8.7500000000000e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:alpha:slider').get_adjustment().set_value( 8.4722222222222e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:alpha:slider').get_adjustment().set_value( 8.3333333333333e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:alpha:slider').get_adjustment().set_value( 8.0555555555556e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:alpha:slider').get_adjustment().set_value( 7.9166666666667e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:alpha:slider').get_adjustment().set_value( 8.0555555555556e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:alpha:slider').get_adjustment().set_value( 8.1944444444444e-01)
findWidget('Dialog-Parametrize Color;green:color:TranslucentGray:alpha:slider').get_adjustment().set_value( 8.3333333333333e-01)
findWidget('Dialog-Parametrize Color;green:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Color.green

# add the property to the material
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
assert tests.materialPropertyListCheck('Color:green')
assert tests.sensitization4()

# parametrize the unnamed cubic thermal conductivity
event(Gdk.EventType.BUTTON_RELEASE,x= 6.0000000000000e+00,y= 6.3000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([2]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 8.0000000000000e+00,y= 6.1000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([2, 0]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 2.4000000000000e+01,y= 7.8000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([2, 0, 1]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 4.2000000000000e+01,y= 1.1500000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([2, 0, 1, 0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 9.8000000000000e+01,y= 1.3300000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([2, 0, 1, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic').resize(313, 184)
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0').set_text('')
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0').set_text('1')
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0').set_text('12')
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0').set_text('123')
widget_0=findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0')
if widget_0: wevent(widget_0, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Thermal.Conductivity.Anisotropic.Cubic

# add the unnamed cubic thermal conductivity to the material
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
assert tests.materialPropertyListCheck('Color:green', 'Thermal:Conductivity:Anisotropic:Cubic')
assert tests.sensitization5()

# unselect the property
event(Gdk.EventType.BUTTON_RELEASE,x= 8.5000000000000e+01,y= 1.3300000000000e+02,button=1,state=260,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
event(Gdk.EventType.BUTTON_RELEASE,x= 8.5000000000000e+01,y= 1.3300000000000e+02,button=1,state=260,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().unselect_all()
checkpoint Materials page updated
checkpoint property deselected
event(Gdk.EventType.BUTTON_RELEASE,x= 1.0900000000000e+02,y= 1.3500000000000e+02,button=1,state=272,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
assert tests.sensitization3()

# copy the material
findWidget('OOF2:Materials Page:Pane:Material:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Name for the new material.
findWidget('Dialog-Name for the new material.').resize(192, 92)
findWidget('Dialog-Name for the new material.:new_name').delete_text(0, 11)
findWidget('Dialog-Name for the new material.:new_name').insert_text('c', 11)
findWidget('Dialog-Name for the new material.:new_name').insert_text('p', 1)
findWidget('Dialog-Name for the new material.:new_name').delete_text(1, 2)
findWidget('Dialog-Name for the new material.:new_name').insert_text('o', 1)
findWidget('Dialog-Name for the new material.:new_name').insert_text('p', 2)
findWidget('Dialog-Name for the new material.:new_name').insert_text('y', 3)
findWidget('Dialog-Name for the new material.:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.Copy
assert tests.currentMaterialCheck('copy')
assert tests.materialListCheck('test', 'copy')
assert tests.currentPropertyCheck(None)

# Select a property of the copied material
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint property selected
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint property selected
checkpoint Materials page updated
assert tests.currentPropertyCheck('Thermal:Conductivity:Anisotropic:Cubic')
assert tests.sensitization5()

# Remove the property from the material
findWidget('OOF2:Materials Page:Pane:Material:RemoveProperty').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.Remove_property
assert tests.materialPropertyListCheck('Color:green')
assert tests.propertyTreeCheck('Thermal:Conductivity:Anisotropic:Cubic')
assert tests.materialPropertyCheck(None)

# go back to the first material
event(Gdk.EventType.BUTTON_PRESS,x= 6.8000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Materials Page:Pane:Material:MaterialList').get_window())
checkpoint toplevel widget mapped chooserPopup-MaterialList
findMenu(findWidget('chooserPopup-MaterialList'), ['test']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-MaterialList') # MenuItemLogger
checkpoint Materials page updated
assert tests.currentPropertyCheck('Thermal:Conductivity:Anisotropic:Cubic')
assert tests.materialPropertyListCheck('Color:green', 'Thermal:Conductivity:Anisotropic:Cubic')
assert tests.currentMaterialCheck('test')

# select the color property in the material
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint property selected
checkpoint Materials page updated
assert tests.currentPropertyCheck('Color:green')

# delete the property
findWidget('OOF2:Materials Page:Pane:Property:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(195, 86)
findWidget('Questioner:OK').clicked()
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().unselect_all()
checkpoint Materials page updated
checkpoint property deselected
checkpoint OOF.Property.Delete
assert tests.currentPropertyCheck(None)
assert tests.materialPropertyListCheck('Thermal:Conductivity:Anisotropic:Cubic')

# rename the material
findWidget('OOF2:Materials Page:Pane:Material:Rename').clicked()
checkpoint toplevel widget mapped Dialog-New name for the material.
findWidget('Dialog-New name for the material.').resize(192, 92)
findWidget('Dialog-New name for the material.:name').delete_text(0, 11)
findWidget('Dialog-New name for the material.:name').insert_text('m', 11)
findWidget('Dialog-New name for the material.:name').insert_text('a', 1)
findWidget('Dialog-New name for the material.:name').insert_text('t', 2)
findWidget('Dialog-New name for the material.:name').insert_text('e', 3)
findWidget('Dialog-New name for the material.:name').insert_text('r', 4)
findWidget('Dialog-New name for the material.:name').insert_text('i', 5)
findWidget('Dialog-New name for the material.:name').insert_text('a', 6)
findWidget('Dialog-New name for the material.:name').insert_text('l', 7)
findWidget('Dialog-New name for the material.:name').insert_text(' ', 8)
findWidget('Dialog-New name for the material.:name').insert_text('t', 9)
findWidget('Dialog-New name for the material.:name').insert_text('s', 10)
findWidget('Dialog-New name for the material.:name').insert_text('e', 11)
findWidget('Dialog-New name for the material.:name').insert_text('t', 12)
findWidget('Dialog-New name for the material.:name').delete_text(12, 13)
findWidget('Dialog-New name for the material.:name').delete_text(11, 12)
findWidget('Dialog-New name for the material.:name').delete_text(10, 11)
findWidget('Dialog-New name for the material.:name').insert_text('e', 10)
findWidget('Dialog-New name for the material.:name').insert_text('s', 11)
findWidget('Dialog-New name for the material.:name').insert_text('t', 12)
findWidget('Dialog-New name for the material.:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.Rename
assert tests.currentMaterialCheck('material test')
assert tests.materialPropertyListCheck('Thermal:Conductivity:Anisotropic:Cubic')
assert tests.currentPropertyCheck(None)

# create another material
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:name').insert_text('a', 0)
findWidget('Dialog-New material:name').insert_text('n', 1)
findWidget('Dialog-New material:name').insert_text('o', 2)
findWidget('Dialog-New material:name').insert_text('t', 3)
findWidget('Dialog-New material:name').insert_text('h', 4)
findWidget('Dialog-New material:name').insert_text('e', 5)
findWidget('Dialog-New material:name').insert_text('r', 6)
findWidget('Dialog-New material:name').insert_text(' ', 7)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New
assert tests.currentMaterialCheck('another test')
assert tests.materialPropertyListCheck()
assert tests.currentPropertyCheck(None)

# select the cubic thermal conductivity property again
event(Gdk.EventType.BUTTON_RELEASE,x= 1.0900000000000e+02,y= 1.1400000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([2, 0, 1, 0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 1.0400000000000e+02,y= 1.1600000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
assert tests.propertyTreeCheck('Thermal:Conductivity:Anisotropic:Cubic')

# parametrize it again, without changing anything
event(Gdk.EventType.BUTTON_RELEASE,x= 9.5000000000000e+01,y= 1.1400000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
event(Gdk.EventType.BUTTON_RELEASE,x= 9.5000000000000e+01,y= 1.1400000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
event(Gdk.EventType.BUTTON_RELEASE,x= 9.4000000000000e+01,y= 1.1400000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([2, 0, 1, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic').resize(313, 184)
widget_1=findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:kappa:0,0')
if widget_1: wevent(widget_1, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_1.get_window())
del widget_1
findWidget('Dialog-Parametrize Thermal;Conductivity;Anisotropic;Cubic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Thermal.Conductivity.Anisotropic.Cubic

# make a copy of the cubic property, with an illegal name
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic').resize(192, 92)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').delete_text(0, 5)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').insert_text('c', 11)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').insert_text('u', 1)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').insert_text('b', 2)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').insert_text('i', 3)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').insert_text('c', 4)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').insert_text(' ', 5)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').insert_text('c', 6)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').insert_text('o', 7)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').insert_text('p', 8)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').insert_text('y', 9)
assert tests.sensitizationCheck({'Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:widget_GTK_RESPONSE_OK': 0})
# fix the illegal name
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').delete_text(5, 6)
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:new_name').insert_text('_', 5)
assert tests.sensitizationCheck({'Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:widget_GTK_RESPONSE_OK': 1})
findWidget('Dialog-Copy property Thermal;Conductivity;Anisotropic;Cubic:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([2, 0, 1, 0]), open_all=False)
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy

# add the property to the material
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
assert tests.propertyTreeCheck('Thermal:Conductivity:Anisotropic:Cubic:cubic_copy')
assert tests.currentPropertyCheck('Thermal:Conductivity:Anisotropic:Cubic:cubic_copy')

# assign the material to a pixel group
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material another test to pixels
findWidget('Dialog-Assign material another test to pixels').resize(214, 122)
assert tests.chooserCheck('Dialog-Assign material another test to pixels:pixels', ['<selection>', '<every>', 'green'])

event(Gdk.EventType.BUTTON_PRESS,x= 4.4000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-Assign material another test to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['green']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material another test to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Material.Assign

# open a graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([13]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New

# query a green pixel
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Info']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(224)
findGfxWindow('Graphics_1').simulateMouse('down', 51.375, 82.875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 51.375, 82.875, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial('another test')

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 7.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 6.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.1300000000000e+02)

# remove the material from the pixels
findWidget('OOF2:Materials Page:Pane:Material:RemoveMaterial').clicked()
checkpoint toplevel widget mapped Dialog-Remove the assigned material from pixels
findWidget('Dialog-Remove the assigned material from pixels').resize(214, 122)
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-Remove the assigned material from pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['green']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Remove the assigned material from pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Remove
assert tests.checkTBMaterial()

# click on a couple other pixels
findGfxWindow('Graphics_1').simulateMouse('down', 31.95, 56.625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 31.95, 56.625, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial()

findGfxWindow('Graphics_1').simulateMouse('down', 87.075, 47.175, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 87.075, 47.175, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial()

# assign the material to every pixel
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material another test to pixels
findWidget('Dialog-Assign material another test to pixels').resize(213, 122)
event(Gdk.EventType.BUTTON_PRESS,x= 4.1000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('Dialog-Assign material another test to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['<every>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material another test to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign
assert tests.checkTBMaterial('another test')

# query some other pixels
findGfxWindow('Graphics_1').simulateMouse('down', 46.65, 79.725, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 46.65, 79.725, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial('another test')

findGfxWindow('Graphics_1').simulateMouse('down', 135.375, 9.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 135.375, 9.9, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial('another test')

findGfxWindow('Graphics_1').simulateMouse('down', 126.45, 60.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 126.45, 60.3, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial('another test')

# remove the material from the green pixels
findWidget('OOF2:Materials Page:Pane:Material:RemoveMaterial').clicked()
checkpoint toplevel widget mapped Dialog-Remove the assigned material from pixels
findWidget('Dialog-Remove the assigned material from pixels').resize(213, 122)
findWidget('Dialog-Remove the assigned material from pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Remove
assert tests.checkTBMaterial('another test')

findGfxWindow('Graphics_1').simulateMouse('down', 54, 64.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 54, 64.5, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial()

findGfxWindow('Graphics_1').simulateMouse('down', 109.125, 119.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 109.125, 119.1, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.checkTBMaterial('another test')

# save the material
findWidget('OOF2:Materials Page:Pane:Material:Save').clicked()
checkpoint toplevel widget mapped Dialog-Save Material "another test"
findWidget('Dialog-Save Material "another test"').resize(192, 152)
findWidget('Dialog-Save Material "another test":filename').set_text('m')
findWidget('Dialog-Save Material "another test":filename').set_text('ma')
findWidget('Dialog-Save Material "another test":filename').set_text('mat')
findWidget('Dialog-Save Material "another test":filename').set_text('mate')
findWidget('Dialog-Save Material "another test":filename').set_text('mater')
findWidget('Dialog-Save Material "another test":filename').set_text('materi')
findWidget('Dialog-Save Material "another test":filename').set_text('materia')
findWidget('Dialog-Save Material "another test":filename').set_text('material')
findWidget('Dialog-Save Material "another test":filename').set_text('material.')
findWidget('Dialog-Save Material "another test":filename').set_text('material.d')
findWidget('Dialog-Save Material "another test":filename').set_text('material.da')
findWidget('Dialog-Save Material "another test":filename').set_text('material.dat')
findWidget('Dialog-Save Material "another test":widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Materials
assert tests.filediff('material.dat')

# delete the microstructure
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(184, 86)
findWidget('Questioner:Yes').clicked()
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint pixel page updated
checkpoint active area status updated
checkpoint pixel page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.Delete
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
event(Gdk.EventType.BUTTON_PRESS,x= 1.0500000000000e+02,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
assert tests.sensitization0()

# delete the material
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(195, 86)
findWidget('Questioner:OK').clicked()
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Delete
event(Gdk.EventType.BUTTON_PRESS,x= 1.9700000000000e+02,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Materials Page:Pane:Material:MaterialList').get_window())
checkpoint toplevel widget mapped chooserPopup-MaterialList
findWidget('chooserPopup-MaterialList').deactivate() # MenuLogger
assert tests.chooserStateCheck('OOF2:Materials Page:Pane:Material:MaterialList', 'copy')
assert tests.propertyTreeCheck('Thermal:Conductivity:Anisotropic:Cubic:cubic_copy')

# delete another material
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(192, 86)
findWidget('Questioner:OK').clicked()
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Delete
assert tests.chooserStateCheck('OOF2:Materials Page:Pane:Material:MaterialList', 'material test')
assert tests.propertyTreeCheck('Thermal:Conductivity:Anisotropic:Cubic:cubic_copy')

# delete the last material
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(197, 86)
findWidget('Questioner:OK').clicked()
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Delete
assert tests.sensitization1()
assert tests.chooserCheck('OOF2:Materials Page:Pane:Material:MaterialList', [])
assert tests.checkTBMaterial("???")

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
findWidget('Dialog-Python_Log').resize(194, 122)
findWidget('Dialog-Python_Log:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff("session.log")
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
