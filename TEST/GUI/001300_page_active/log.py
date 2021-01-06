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
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
assert tests.activeAreaCheck(0)
assert tests.pixelSelectionCheck(0)
findWidget('OOF2').resize(782, 545)
# open a graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
event(Gdk.EventType.BUTTON_PRESS,x= 5.7000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Image']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
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
findWidget('OOF2 Graphics 1').resize(800, 492)
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 3.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Pixel Selection
findWidget('OOF2:Pixel Selection Page:Pane').set_position(273)
checkpoint pixel page updated
checkpoint pixel page sensitized
# Burn the green region and put pixels in a group

event(Gdk.EventType.BUTTON_PRESS,x= 8.7000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
event(Gdk.EventType.BUTTON_PRESS,x= 8.4000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Burn']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 47.9625, 79.725, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 47.9625, 79.725, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
event(Gdk.EventType.BUTTON_PRESS,x= 7.4000000000000e+01,y= 2.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
assert tests.pixelGroupSizeCheck('small.ppm', 'green', 4795)

# Burn the white region and put pixels in a group

findGfxWindow('Graphics_1').simulateMouse('up', 81.0375, 44.55, 1, False, False)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 5)
findWidget('Dialog-Create new pixel group:name').insert_text('w', 11)
findWidget('Dialog-Create new pixel group:name').insert_text('h', 1)
findWidget('Dialog-Create new pixel group:name').insert_text('i', 2)
findWidget('Dialog-Create new pixel group:name').insert_text('t', 3)
findWidget('Dialog-Create new pixel group:name').insert_text('e', 4)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
assert tests.pixelGroupSizeCheck('small.ppm', 'white', 4781)

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.9000000000000e+01)
# Select a circle centered on the image, containing about 7500 pixels

event(Gdk.EventType.BUTTON_PRESS,x= 1.0400000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 75.7875, 70.275, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 75.7875, 69.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.3625, 69.225, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.1375, 66.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.7625, 66.075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.8625, 65.025, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 91.0125, 63.975, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 95.2125, 62.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 99.9375, 60.825, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 103.6125, 59.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 107.8125, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 108.3375, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 109.3875, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 111.4875, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 112.5375, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.0625, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 114.6375, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 114.6375, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 114.6375, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 115.1625, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 115.1625, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 115.6875, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 115.6875, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 115.6875, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 115.6875, 58.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 116.2125, 58.725, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 116.2125, 58.725, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 116.7375, 58.725, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 116.7375, 59.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 117.2625, 59.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 117.2625, 59.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 117.7875, 59.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 117.7875, 59.25, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
# Activate the selection only

event(Gdk.EventType.BUTTON_PRESS,x= 8.3000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Active Area']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Active Area
findWidget('OOF2:Active Area Page:Pane').set_position(529)
event(Gdk.EventType.BUTTON_PRESS,x= 5.6000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Activate Selection Only']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint active area status updated
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Activate_Selection_Only
assert tests.pixelSelectionCheck(5925)
assert tests.activeAreaStatusCheck(5925, 22500)
assert tests.activeAreaCheck(5925)

# Store the active area as "circle"

findWidget('OOF2:Active Area Page:Pane:Store').clicked()
checkpoint toplevel widget mapped Dialog-Store the active area
findWidget('Dialog-Store the active area').resize(192, 92)
findWidget('Dialog-Store the active area:name').delete_text(0, 11)
findWidget('Dialog-Store the active area:name').insert_text('c', 11)
findWidget('Dialog-Store the active area:name').insert_text('i', 1)
findWidget('Dialog-Store the active area:name').insert_text('r', 2)
findWidget('Dialog-Store the active area:name').insert_text('c', 3)
findWidget('Dialog-Store the active area:name').insert_text('l', 4)
findWidget('Dialog-Store the active area:name').insert_text('e', 5)
findWidget('Dialog-Store the active area:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.ActiveArea.Store
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
# Burn the white pixels inside the circle

event(Gdk.EventType.BUTTON_PRESS,x= 1.3400000000000e+02,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Burn']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 88.9125, 63.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 88.9125, 63.45, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
findWidget('OOF2 Graphics 1').resize(800, 502)
findWidget('OOF2 Graphics 1:Pane0').set_position(370)
findWidget('OOF2 Graphics 1').resize(800, 524)
findWidget('OOF2 Graphics 1:Pane0').set_position(392)
findWidget('OOF2 Graphics 1').resize(800, 560)
findWidget('OOF2 Graphics 1:Pane0').set_position(428)
findWidget('OOF2 Graphics 1').resize(800, 572)
findWidget('OOF2 Graphics 1:Pane0').set_position(440)
findWidget('OOF2 Graphics 1').resize(800, 573)
findWidget('OOF2 Graphics 1:Pane0').set_position(441)
findWidget('OOF2 Graphics 1').resize(800, 581)
findWidget('OOF2 Graphics 1:Pane0').set_position(449)
findWidget('OOF2 Graphics 1').resize(800, 583)
findWidget('OOF2 Graphics 1:Pane0').set_position(451)
findWidget('OOF2 Graphics 1').resize(800, 582)
findWidget('OOF2 Graphics 1:Pane0').set_position(450)
findWidget('OOF2 Graphics 1').resize(800, 586)
findWidget('OOF2 Graphics 1:Pane0').set_position(454)
findWidget('OOF2 Graphics 1').resize(800, 588)
findWidget('OOF2 Graphics 1:Pane0').set_position(456)
findWidget('OOF2 Graphics 1').resize(800, 589)
findWidget('OOF2 Graphics 1:Pane0').set_position(457)
findWidget('OOF2 Graphics 1').resize(800, 591)
findWidget('OOF2 Graphics 1:Pane0').set_position(459)
findWidget('OOF2 Graphics 1').resize(800, 592)
findWidget('OOF2 Graphics 1:Pane0').set_position(460)
findWidget('OOF2 Graphics 1').resize(800, 593)
findWidget('OOF2 Graphics 1:Pane0').set_position(461)
assert tests.pixelSelectionCheck(1710)

# Override the active area
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Override
assert tests.activeAreaOverrideCheck(True)

# Repeat the selection and check that all white pixels are selected
event(Gdk.EventType.BUTTON_RELEASE,x= 4.9000000000000e+01,y= 2.0000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionCheck(4781)

# Turn off the active area override
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Override
assert tests.activeAreaOverrideCheck(False)

# Clear the pixel selection within the active area
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionCheck(3071)

findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Override
assert tests.activeAreaOverrideCheck(True)
assert tests.activeAreaStatusCheck(0, 22500, True)

# Clear the rest of the pixel selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionCheck(0)

# Turn off the active area override
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Override

# Activate all pixels
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 2.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Activate All']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Activate_All
assert tests.activeAreaStatusCheck(22500, 22500)
assert tests.activeAreaCheck(22500)

# Repeat the burn of the white pixels
event(Gdk.EventType.BUTTON_RELEASE,x= 3.7000000000000e+01,y= 1.7000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionCheck(4781)

# Activate the selection (white pixels)
event(Gdk.EventType.BUTTON_PRESS,x= 1.1400000000000e+02,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Activate Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Activate_Selection
assert tests.activeAreaCheck(22500)
assert tests.activeAreaStatusCheck(22500, 22500)

# Clear the selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionCheck(0)

# Select a different circle 
event(Gdk.EventType.BUTTON_PRESS,x= 1.0700000000000e+02,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.6000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 26.9625, 126.7125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.9625, 126.7125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.0125, 125.1375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 30.1125, 122.5125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 33.2625, 119.3625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 34.3125, 118.3125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 35.3625, 117.7875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 35.8875, 117.7875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 37.4625, 116.2125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 38.5125, 114.6375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 39.5625, 114.1125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 40.0875, 113.5875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.6625, 111.4875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.2375, 109.3875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.7625, 108.8625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 45.8625, 107.8125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.4375, 106.7625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.0625, 105.7125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.1625, 104.1375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 53.2125, 103.6125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 54.7875, 101.5125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.3625, 100.4625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.3625, 99.9375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.3625, 99.9375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.8875, 99.9375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 57.4125, 99.9375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 57.4125, 99.9375, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionCheck(3815)
assert tests.activeAreaStatusCheck(22500, 22500)

# Activate the new circle (This step does nothing, because the whole
# MS is active)

findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint active area status updated
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Activate_Selection
assert tests.activeAreaStatusCheck(22500, 22500)

# Restore the saved active area.
findWidget('OOF2:Active Area Page:Pane:Restore').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Restore
assert tests.activeAreaStatusCheck(5925, 22500)

assert tests.activeAreaCheck(5925)

# Activate the selection
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint active area status updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Activate_Selection
assert tests.activeAreaStatusCheck(9495, 22500)
assert tests.activeAreaCheck(9495)

# Clear the selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear

# Burn the white pixels again
event(Gdk.EventType.BUTTON_PRESS,x= 1.5500000000000e+02,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Burn']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 89.4375, 81.5625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 89.4375, 81.5625, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionCheck(2942)
assert tests.activeAreaCheck(9495)
assert tests.activeAreaStatusCheck(9495, 22500)

# Activate the pixels in the green group
event(Gdk.EventType.BUTTON_PRESS,x= 5.8000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Activate Pixel Group Only']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane').set_position(521)
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint active area status updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Activate_Pixel_Group_Only
assert tests.activeAreaStatusCheck(4795, 22500)
assert tests.activeAreaCheck(4795)

# Override the active area
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Override
assert tests.activeAreaOverrideCheck(True)

# Clear the selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionCheck(0)

# Turn off the override
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Override
assert tests.activeAreaOverrideCheck(False)

# Select yet another circle (about 1000 pixels, including the junction
# of the white veins where green, yellow, and dark blue grains nearly
# meet).
event(Gdk.EventType.BUTTON_PRESS,x= 1.4400000000000e+02,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.6000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 89.4375, 99.9375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.4375, 99.4125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.4375, 98.8875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 91.0125, 97.3125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 92.0625, 95.7375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 92.5875, 95.7375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 92.5875, 95.2125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.1125, 94.6875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.6375, 94.1625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 94.1625, 94.1625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 94.6875, 93.6375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 95.2125, 92.5875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 96.7875, 91.5375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 96.7875, 91.0125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 97.8375, 91.0125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 97.8375, 90.4875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 98.3625, 90.4875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 98.8875, 89.9625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 99.9375, 88.9125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 100.4625, 88.9125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 100.4625, 87.8625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 100.9875, 87.3375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 102.0375, 86.2875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 103.0875, 85.2375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 103.0875, 85.2375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 103.0875, 85.2375, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle

# Activate the white pixel group
event(Gdk.EventType.BUTTON_PRESS,x= 8.1000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Activate Pixel Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane').set_position(529)
event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:Activate Pixel Group:group').get_window())
checkpoint toplevel widget mapped chooserPopup-group
findMenu(findWidget('chooserPopup-group'), ['white']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-group') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Activate_Pixel_Group
assert tests.activeAreaStatusCheck(9576, 22500)
assert tests.activeAreaCheck(9576)

# Repeat the pixel selection.
event(Gdk.EventType.BUTTON_RELEASE,x= 5.5000000000000e+01,y= 1.8000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
event(Gdk.EventType.BUTTON_RELEASE,x= 5.7000000000000e+01,y= 1.7000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionCheck(732)

# Deactivate the selected pixels
event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Deactivate Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Deactivate_Selection
assert tests.activeAreaCheck(8844)
assert tests.activeAreaStatusCheck(8844, 22500)

# Clear the selection (should do nothing to the selection, as it's inactive)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionCheck(732)

# Burn white pixels in one of the veins below the third circle.  The
# burn should not extend into the veins to the right or left of the
# circle.
event(Gdk.EventType.BUTTON_PRESS,x= 1.4500000000000e+02,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Burn']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 89.4375, 46.9125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 89.4375, 46.9125, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionCheck(2951)

# Override the active area
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Override

# Clear the pixel selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionCheck(0)

# Turn off the override
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Override

# Deactivate the green group of pixels.  There will still be some
# white active pixels.
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Deactivate Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Deactivate_Group
assert tests.activeAreaStatusCheck(4264, 22500)
assert tests.activeAreaCheck(4264)

# Select another circle in the upper left corner
event(Gdk.EventType.BUTTON_PRESS,x= 1.1500000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.6000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 40.6125, 114.1125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.1375, 114.1125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.1375, 113.5875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.1875, 113.0625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.2375, 112.0125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 44.8125, 110.9625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.4375, 108.8625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.0625, 106.7625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 51.6375, 105.7125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.6875, 104.6625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 54.2625, 103.6125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.3625, 102.5625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.9875, 100.4625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.0375, 99.4125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 61.0875, 98.8875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 62.1375, 98.3625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 63.7125, 97.3125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 64.2375, 96.7875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 65.8125, 95.7375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 66.8625, 95.2125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 67.3875, 94.6875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 67.9125, 94.6875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 68.9625, 94.1625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 69.4875, 94.1625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 69.4875, 94.1625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 69.4875, 94.1625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 69.4875, 93.6375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 70.0125, 93.6375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 70.0125, 93.1125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 70.5375, 93.1125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 70.5375, 93.1125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 70.5375, 93.1125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.0625, 92.5875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.0625, 92.5875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.0625, 92.0625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.0625, 92.0625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.0625, 92.0625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.0625, 92.0625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 71.0625, 92.0625, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.activeAreaCheck(4264)
assert tests.activeAreaStatusCheck(4264, 22500)
assert tests.pixelSelectionCheck(1290)

# Expand the active area w/ radius 5.0
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Expand']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane:Modify:Method:Expand:radius').set_text('')
findWidget('OOF2:Active Area Page:Pane:Modify:Method:Expand:radius').set_text('5')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint active area status updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Expand
assert tests.activeAreaStatusCheck(8368, 22500)
assert tests.activeAreaCheck(8368)

# Repeat the pixel selection
event(Gdk.EventType.BUTTON_RELEASE,x= 5.2000000000000e+01,y= 2.5000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionCheck(2428)

# Shrink the active area w/ radius 1.0
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Shrink']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page updated
checkpoint active area status updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Shrink
assert tests.activeAreaStatusCheck(7622, 22500)
assert tests.activeAreaCheck(7622)

# Clear the selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionCheck(185)

# Repeat the pixel selection
event(Gdk.EventType.BUTTON_RELEASE,x= 5.2000000000000e+01,y= 1.9000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionCheck(2428)

# Restore the named active area
findWidget('OOF2:Active Area Page:Pane:Restore').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Restore

# Invert the active area
event(Gdk.EventType.BUTTON_PRESS,x= 7.7000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Invert']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Invert
assert tests.activeAreaCheck(16575)
assert tests.activeAreaStatusCheck(16575, 22500)

# Repeat the pixel selection 
event(Gdk.EventType.BUTTON_RELEASE,x= 6.0000000000000e+01,y= 1.6000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
event(Gdk.EventType.BUTTON_RELEASE,x= 5.3000000000000e+01,y= 1.7000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionCheck(3714)

# Restore the saved active area
findWidget('OOF2:Active Area Page:Pane:Restore').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Restore

# Copy the Microstructure
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy microstructure
findWidget('Dialog-Copy microstructure').resize(192, 92)
findWidget('Dialog-Copy microstructure:name').delete_text(0, 6)
findWidget('Dialog-Copy microstructure:name').insert_text('c', 11)
findWidget('Dialog-Copy microstructure:name').insert_text('o', 1)
findWidget('Dialog-Copy microstructure:name').insert_text('p', 2)
findWidget('Dialog-Copy microstructure:name').insert_text('i', 3)
findWidget('Dialog-Copy microstructure:name').insert_text('e', 4)
findWidget('Dialog-Copy microstructure:name').insert_text('d', 5)
findWidget('Dialog-Copy microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
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
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.Microstructure.Copy

# Check the active area in the copy
event(Gdk.EventType.BUTTON_PRESS,x= 8.5000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Active Area']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Active Area
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['copied']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
checkpoint active area status updated
assert tests.activeAreaStatusCheck(22500, 22500)
assert tests.activeAreaMSCheck('copied', 22500)
assert tests.activeAreaMSCheck('small.ppm', 5925)

# Copy the active area from the original microstrucure
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Copy']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Copy
assert tests.activeAreaStatusCheck(5925, 22500)
assert tests.activeAreaMSCheck('copied', 5925)

# Activate all pixels in the original
event(Gdk.EventType.BUTTON_PRESS,x= 5.7000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['small.ppm']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
checkpoint active area status updated
event(Gdk.EventType.BUTTON_PRESS,x= 4.0000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Activate All']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint active area status updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ActiveArea.Activate_All

# Switch back to the copy and check that not all pixels are activated
event(Gdk.EventType.BUTTON_PRESS,x= 4.8000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Active Area Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['copied']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
checkpoint active area status updated
assert tests.activeAreaStatusCheck(5925, 22500)

# Switch the graphics window display to the copied Microstructure
event(Gdk.EventType.BUTTON_PRESS,x= 3.4200000000000e+02,y= 3.5000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
event(Gdk.EventType.BUTTON_PRESS,x= 3.4600000000000e+02,y= 3.8000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
event(Gdk.EventType.BUTTON_PRESS,x= 3.4600000000000e+02,y= 3.8000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([13]), column)
checkpoint toplevel widget mapped Dialog-Edit Graphics Layer
findWidget('Dialog-Edit Graphics Layer').resize(203, 193)
event(Gdk.EventType.BUTTON_PRESS,x= 4.8000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-Edit Graphics Layer:what:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['copied']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
findWidget('Dialog-Edit Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Edit

# Repeat the selection
event(Gdk.EventType.BUTTON_RELEASE,x= 5.7000000000000e+01,y= 1.3000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionCheck(992, ms='copied')

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
checkpoint OOF.Graphics_1.File.Close
