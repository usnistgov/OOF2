import tests
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 7.4000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Selection']).activate() # MenuItemLogger
checkpoint skeleton selection page grouplist Element
checkpoint page installed Skeleton Selection
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(474)
assert tests.sensitization0()

# Create a Microstructure
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 2.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
checkpoint page installed Microstructure
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('Dialog-Create Microstructure:width_in_pixels').set_text('100')
findWidget('Dialog-Create Microstructure:height_in_pixels').set_text('100')
findWidget('Dialog-Create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint pixel page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.New
event(Gdk.EventType.BUTTON_PRESS,x= 8.6000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Selection']).activate() # MenuItemLogger
checkpoint page installed Skeleton Selection
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.sensitization0()

# Open a graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
event(Gdk.EventType.BUTTON_PRESS,x= 4.5000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.New_Layer_Policy
findWidget('OOF2').resize(782, 545)

# Add a microstructure material display
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
findWidget('Dialog-New:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 1.3698630136986e-02)
findWidget('Dialog-New:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 5.4794520547945e-02)
findWidget('Dialog-New:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 1.6438356164384e-01)
findWidget('Dialog-New:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 3.0136986301370e-01)
findWidget('Dialog-New:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 4.9315068493151e-01)
findWidget('Dialog-New:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 5.7534246575342e-01)
findWidget('Dialog-New:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 5.8904109589041e-01)
findWidget('Dialog-New:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 5.7534246575342e-01)
findWidget('Dialog-New:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 5.6164383561644e-01)
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New

# Select a circle of pixels
event(Gdk.EventType.BUTTON_PRESS,x= 8.0000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
event(Gdk.EventType.BUTTON_PRESS,x= 4.5000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 0.16225, 0.8465, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.16225, 0.8465, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.16225, 0.843, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.16225, 0.843, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.16575, 0.8395, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.16575, 0.8395, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.16575, 0.836, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.16925, 0.829, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.17625, 0.822, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.18675, 0.8115, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.19375, 0.8045, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.20075, 0.794, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.20775, 0.787, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.21825, 0.7765, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.22175, 0.773, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.22875, 0.766, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.23575, 0.7625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.23925, 0.7625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.24625, 0.7555, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.25675, 0.752, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.26375, 0.7485, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.27075, 0.745, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.27425, 0.738, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28125, 0.731, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28475, 0.724, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28825, 0.7135, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29525, 0.71, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29525, 0.7065, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29875, 0.7065, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29875, 0.7065, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29875, 0.703, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29875, 0.7065, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29875, 0.7065, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29875, 0.7065, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29875, 0.71, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29875, 0.71, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29525, 0.7135, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29525, 0.7135, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29525, 0.7135, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29525, 0.717, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29525, 0.717, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29525, 0.717, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29525, 0.717, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29175, 0.7205, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29175, 0.7205, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29175, 0.724, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28825, 0.724, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28825, 0.7275, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28825, 0.7275, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28825, 0.7275, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28825, 0.7275, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28825, 0.731, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28825, 0.731, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28475, 0.731, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.28475, 0.731, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle

# Assign a material to the selected pixels
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 2.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:name').delete_text(0, 11)
findWidget('Dialog-New material:name').insert_text('s', 11)
findWidget('Dialog-New material:name').insert_text('t', 1)
findWidget('Dialog-New material:name').insert_text('u', 2)
findWidget('Dialog-New material:name').insert_text('f', 3)
findWidget('Dialog-New material:name').insert_text('f', 4)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material stuff to pixels
findWidget('Dialog-Assign material stuff to pixels').resize(235, 122)
findWidget('Dialog-Assign material stuff to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign

# Clear the pixel selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear

# Create a Skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 6.0000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:x_elements').set_text('')
findWidget('Dialog-New skeleton:x_elements').set_text('9')
findWidget('Dialog-New skeleton:y_elements').set_text('')
findWidget('Dialog-New skeleton:y_elements').set_text('9')
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page sensitized
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New
assert tests.sensitization1()

# Select 4 elements using the circle selector
event(Gdk.EventType.BUTTON_PRESS,x= 6.6000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(265)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.0000000000000e+01)
event(Gdk.EventType.BUTTON_PRESS,x= 1.0600000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 0.66275, 0.3355, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.66625, 0.3355, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.67675, 0.3285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.70825, 0.311, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73275, 0.3005, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73625, 0.2935, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73975, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.74675, 0.283, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.75725, 0.2725, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76775, 0.262, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.77125, 0.2515, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.77825, 0.234, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.78525, 0.22, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.78875, 0.2165, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.78875, 0.2165, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.78875, 0.2165, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.78875, 0.2165, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.78875, 0.213, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.79225, 0.2095, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.79225, 0.2095, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.79575, 0.206, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.79575, 0.206, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.79575, 0.206, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.79925, 0.206, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.79925, 0.206, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.79925, 0.206, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.79925, 0.206, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.79925, 0.206, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Circle
assert tests.sensitization2()
assert tests.selectionModeCheck('Elements')
assert tests.selectionSizeCheck(4)
assert tests.elementSelectionCheck([23, 24, 32, 33])

# put the selected elements in a group
event(Gdk.EventType.BUTTON_PRESS,x= 8.7000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Selection']).activate() # MenuItemLogger
checkpoint page installed Skeleton Selection
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new Element group
findWidget('Dialog-Create a new Element group').resize(192, 92)
findWidget('Dialog-Create a new Element group:name').insert_text('f', 3)
findWidget('Dialog-Create a new Element group:name').insert_text('o', 1)
findWidget('Dialog-Create a new Element group:name').insert_text('u', 2)
findWidget('Dialog-Create a new Element group:name').insert_text('r', 3)
findWidget('Dialog-Create a new Element group:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page grouplist Element
checkpoint OOF.ElementGroup.New_Group
checkpoint skeleton selection page groups sensitized Element
assert tests.sensitization3()
assert tests.groupCheck(['four (0 elements)'])

# Now put the elements in the group
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:Add').clicked()
checkpoint skeleton selection page grouplist Element
checkpoint OOF.ElementGroup.Add_to_Group
assert tests.sensitization4()
assert tests.groupCheck(['four (4 elements)'])
assert tests.selectionSizeCheck(4)
assert tests.elementSelectionCheck([23, 24, 32, 33])

# Undo the selection
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Undo
assert tests.sensitization5()
assert tests.selectionSizeCheck(0)
assert tests.elementSelectionCheck([])

# Redo the selection
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Redo').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Redo
assert tests.sensitization4()
assert tests.selectionSizeCheck(4)
assert tests.elementSelectionCheck([23, 24, 32, 33])

# Refine the selected elements
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 5.8000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Selected Elements']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(496)
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Bisection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 6.0000000000000e+01,y= 2.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:Bisection:rule_set').get_window())
checkpoint toplevel widget mapped chooserPopup-rule_set
findMenu(findWidget('chooserPopup-rule_set'), ['liberal']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-rule_set') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(498)
findWidget('OOF2:Skeleton Page:Pane:Modification:OK').clicked()
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Modify
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Skeleton Selection
assert tests.selectionSizeCheck(16)
assert tests.elementSelectionCheck([110, 111, 112, 113, 114, 115, 116, 117, 129, 130, 131, 132, 133, 134, 135, 136])
assert tests.sensitization4()

# Undo the selection
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Undo
assert tests.elementSelectionCheck([])
assert tests.selectionSizeCheck(0)
assert tests.sensitization5()

# Redo the selection
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Redo').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Redo
assert tests.sensitization4()
assert tests.selectionSizeCheck(16)
assert tests.groupCheck(['four (16 elements)'])
assert tests.elementSelectionCheck([110, 111, 112, 113, 114, 115, 116, 117, 129, 130, 131, 132, 133, 134, 135, 136])

# Undo the skleeton modification
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane:Modification:Undo').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Undo
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Skeleton Selection
assert tests.elementSelectionCheck([23, 24, 32, 33])
assert tests.groupCheck(['four (4 elements)'])
assert tests.selectionSizeCheck(4)

# Undo the selection
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Undo
assert tests.sensitization5()
assert tests.selectionSizeCheck(0)
assert tests.elementSelectionCheck([])
assert tests.groupCheck(['four (4 elements)'])

# Redo the Skeleton modification
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane:Modification:Redo').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Redo
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Skeleton Selection
assert tests.selectionSizeCheck(0)
assert tests.groupCheck(['four (16 elements)'])

# Redo the selection
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Redo').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Redo
assert tests.groupCheck(['four (16 elements)'])
assert tests.selectionSizeCheck(16)
assert tests.sensitization4()

# Select elements by material
event(Gdk.EventType.BUTTON_PRESS,x= 8.6000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select by Material']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 5.6000000000000e+01,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Material:material').get_window())
checkpoint toplevel widget mapped chooserPopup-material
findMenu(findWidget('chooserPopup-material'), ['stuff']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-material') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_by_Material
assert tests.elementSelectionCheck([164, 172, 173, 174, 181, 182, 183])
assert tests.selectionSizeCheck(7)
assert tests.sensitization4()

# Undo the selection
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Undo
assert tests.selectionSizeCheck(16)

# Select by homogeneity
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select by Homogeneity']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_by_Homogeneity
assert tests.sensitization6()
assert tests.elementSelectionCheck([163, 164, 165, 181, 183])
assert tests.selectionSizeCheck(5)

# Select by shape energy
event(Gdk.EventType.BUTTON_PRESS,x= 1.1800000000000e+02,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select by Shape Energy']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_by_Shape_Energy
assert tests.elementSelectionCheck([])
assert tests.selectionSizeCheck(0)
assert tests.sensitization7()

# Try that again with a nontrivial result
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:entry').set_text('0.')
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:entry').set_text('0.2')
widget_0=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:entry')
if widget_0: event(Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_by_Shape_Energy
assert tests.selectionSizeCheck(16)
assert tests.elementSelectionCheck([95, 97, 98, 100, 107, 109, 118, 120, 126, 128, 137, 139, 146, 148, 149, 151])
assert tests.sensitization6()

# Select iilegal elements
event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Illegal Elements']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_Illegal_Elements
assert tests.selectionSizeCheck(0)
assert tests.elementSelectionCheck([])

# Select a single node
findWidget('OOF2').resize(782, 545)
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('up', 0.44225, 0.4405, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('down', 0.44575, 0.4405, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.44575, 0.4405, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Circle
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Node').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
findGfxWindow('Graphics_1').simulateMouse('down', 0.43875, 0.444, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.43875, 0.444, 1, False, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
# Select elements from selected nodes
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select from Selected Nodes']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_from_Selected_Nodes
assert tests.elementSelectionCheck([125, 127, 128, 144, 145])
assert tests.selectionSizeCheck(5)

# Select elements from selected segments
# First select three segments
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint selection info updated Segment
checkpoint Graphics_1 Segment sensitized
findGfxWindow('Graphics_1').simulateMouse('down', 0.37575, 0.6645, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.37575, 0.6645, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.49125, 0.6575, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.49475, 0.6575, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.49475, 0.6575, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.50525, 0.787, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.50525, 0.7835, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.50525, 0.7835, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
# Select elements from segments
event(Gdk.EventType.BUTTON_PRESS,x= 1.1700000000000e+02,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select from Selected Segments']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_from_Selected_Segments
assert tests.selectionSizeCheck(5)
assert tests.elementSelectionCheck([157, 158, 166, 167, 176])

# expand the element selection
event(Gdk.EventType.BUTTON_PRESS,x= 9.9000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Expand Element Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Expand_Element_Selection
assert tests.selectionSizeCheck(20)
assert tests.elementSelectionCheck([143, 144, 145, 146, 147, 156, 157, 158, 159, 165, 166, 167, 168, 174, 175, 176, 177, 184, 185, 186])

# Select the element group
event(Gdk.EventType.BUTTON_PRESS,x= 8.7000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_Group
assert tests.elementSelectionCheck([110, 111, 112, 113, 114, 115, 116, 117, 129, 130, 131, 132, 133, 134, 135, 136])
assert tests.selectionSizeCheck(16)

# Select a circular region of elements
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Element').clicked()
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
findGfxWindow('Graphics_1').simulateMouse('down', 0.66625, 0.2725, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.66625, 0.2725, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.66625, 0.2725, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.66625, 0.269, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.66975, 0.269, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.66975, 0.2655, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.67325, 0.2585, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.67675, 0.248, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68375, 0.234, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68375, 0.227, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68375, 0.2235, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68375, 0.2165, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68375, 0.206, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68375, 0.1955, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68375, 0.1885, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68725, 0.1815, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68725, 0.1745, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.69075, 0.1675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.69075, 0.1605, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.69425, 0.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.69775, 0.143, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.69775, 0.1395, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.70125, 0.136, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.70125, 0.129, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.70475, 0.115, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.70125, 0.101, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.70125, 0.087, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.70125, 0.0765, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.70125, 0.0695, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.70125, 0.0625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.70825, 0.052, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.71175, 0.045, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.72225, 0.0345, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.72575, 0.0275, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.72925, 0.024, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.72925, 0.017, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73275, 0.01, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73275, -0.004, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73275, -0.018, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73625, -0.0285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73975, -0.0285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73975, -0.032, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73975, -0.0355, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73975, -0.039, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.74325, -0.0425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.74675, -0.0495, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.75025, -0.053, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.75375, -0.0635, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76075, -0.067, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76075, -0.074, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76075, -0.081, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76425, -0.088, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76425, -0.0915, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76075, -0.0985, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76075, -0.1055, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76075, -0.1055, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76075, -0.109, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76075, -0.116, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76425, -0.1195, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76425, -0.1265, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76775, -0.1335, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.77125, -0.144, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.77125, -0.1475, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.77125, -0.1545, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.77125, -0.1615, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.77125, -0.165, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.77125, -0.1685, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.77125, -0.172, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.77125, -0.172, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.77125, -0.172, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Circle
# Unselect the group
event(Gdk.EventType.BUTTON_PRESS,x= 7.8000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Unselect Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Unselect_Group
assert tests.elementSelectionCheck([84, 85, 86, 87, 88, 89, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 105, 106, 107, 108, 109, 118, 119, 120, 121, 125, 126, 127, 128, 137, 138, 139, 140, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 158, 159, 160, 161])
assert tests.selectionSizeCheck(47)

# Add the group to the selection
event(Gdk.EventType.BUTTON_PRESS,x= 5.4000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Add Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Add_Group
assert tests.elementSelectionCheck([84, 85, 86, 87, 88, 89, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 158, 159, 160, 161])
assert tests.selectionSizeCheck(63)

# Select a different circle, that partially intersects the group
findGfxWindow('Graphics_1').simulateMouse('up', 0.47725, 0.325, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('down', 0.33025, 0.332, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.33375, 0.332, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.33375, 0.332, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.34775, 0.332, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36525, 0.332, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.38275, 0.3285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.39675, 0.3285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.41075, 0.3285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.42475, 0.325, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.44225, 0.325, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.45275, 0.325, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.46325, 0.3215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.47375, 0.3215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.48775, 0.318, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.49825, 0.318, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.50875, 0.3145, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.51925, 0.311, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.52625, 0.311, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.53325, 0.3075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.54025, 0.3075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.54725, 0.3075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.55775, 0.304, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.56475, 0.3005, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.57175, 0.3005, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.58225, 0.297, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.58925, 0.297, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.59275, 0.297, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.59625, 0.297, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.60325, 0.297, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.61025, 0.297, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.61375, 0.297, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.62075, 0.2935, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.62425, 0.2935, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.63825, 0.2935, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.64525, 0.2935, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.64875, 0.2935, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.65575, 0.2935, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.67325, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68025, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68025, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68375, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68725, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68725, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.69075, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68725, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68725, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68375, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68375, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68025, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.67675, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.67675, 0.29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.67675, 0.29, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Circle
assert tests.selectionSizeCheck(30) # Get actual elements selected

# Select the intersection with the group
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Intersect Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Intersect_Group
assert tests.selectionSizeCheck(6)
assert tests.elementSelectionCheck([110, 112, 113, 129, 130, 132])

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
