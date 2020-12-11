import tests
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 9.7000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
# check that nothing is sensitized
assert tests.sensitization0()

# create a microstructure 'micro1' from an image file
findWidget('OOF2:Microstructure Page:NewFromFile').clicked()
checkpoint toplevel widget mapped Dialog-Load Image and create Microstructure
findWidget('Dialog-Load Image and create Microstructure').resize(237, 200)
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('e')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('ex')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('exa')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('exam')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examp')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('exampl')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('example')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/s')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/sm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/sma')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/smal')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small.pp')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small.ppm')
findWidget('Dialog-Load Image and create Microstructure:microstructure_name').insert_text('m', 5)
findWidget('Dialog-Load Image and create Microstructure:microstructure_name').insert_text('i', 1)
findWidget('Dialog-Load Image and create Microstructure:microstructure_name').insert_text('c', 2)
findWidget('Dialog-Load Image and create Microstructure:microstructure_name').insert_text('r', 3)
findWidget('Dialog-Load Image and create Microstructure:microstructure_name').insert_text('o', 4)
findWidget('Dialog-Load Image and create Microstructure:microstructure_name').insert_text('1', 5)
findWidget('Dialog-Load Image and create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
# check that the new group button is sensitized
assert tests.sensitization1()

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
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.New_Layer_Policy
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
event(Gdk.EventType.BUTTON_PRESS,x= 5.6000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:category').get_window())
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

# load a second image, creating microstructure micro2
findWidget('OOF2:Microstructure Page:NewFromFile').clicked()
checkpoint toplevel widget mapped Dialog-Load Image and create Microstructure
findWidget('Dialog-Load Image and create Microstructure').resize(237, 200)
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/.ppm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/t.ppm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/tr.ppm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/tri.ppm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/tria.ppm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/trian.ppm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triang.ppm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triangl.ppm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triangle.ppm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triangle.pp')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triangle.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triangle.pn')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triangle.png')
findWidget('Dialog-Load Image and create Microstructure:microstructure_name').delete_text(5, 6)
findWidget('Dialog-Load Image and create Microstructure:microstructure_name').insert_text('2', 5)
findWidget('Dialog-Load Image and create Microstructure:widget_GTK_RESPONSE_OK').clicked()
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
checkpoint contourmap info updated for Graphics_1
# check that the microstructure page sensitization hasn't changed
assert tests.sensitization1()

# check that micro2 is selected
assert tests.microstructureCheck('micro2')

# open the pixel selection toolbox
checkpoint OOF.Microstructure.Create_From_ImageFile
event(Gdk.EventType.BUTTON_PRESS,x= 6.9000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
# choose the circle selector
event(Gdk.EventType.BUTTON_PRESS,x= 4.3000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)

# select pixels in micro1
findGfxWindow('Graphics_1').simulateMouse('down', 61.6125, 98.625, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 61.6125, 98.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 62.1375, 97.575, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 65.8125, 94.425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 70.0125, 90.225, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 74.2125, 86.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 76.3125, 83.925, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.3625, 82.875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.8875, 81.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78.4125, 80.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.4625, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.9875, 77.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 81.0375, 76.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 81.5625, 76.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 81.5625, 76.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 81.5625, 76.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 81.5625, 76.05, 1, False, False)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized

# Just selecting pixels doesn't change the sensitization, because no
# groups have been made (and micro2 is selected)
assert tests.sensitization1()

# make a group in micro2
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set

# A group has been created in micro2, but no pixels are selected
assert tests.sensitization2()
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (0 pixels, meshable)')

# switch to micro1
event(Gdk.EventType.BUTTON_PRESS,x= 5.2000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Microstructure Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['micro1']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
checkpoint meshable button set
checkpoint microstructure page sensitized
# check that sensitization is correct for a micro. with no groups
assert tests.sensitization1()
assert tests.meshableCheck(0)

# create groups in micro1
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
assert tests.sensitization3()
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (0 pixels, meshable)')

# add pixels to the group
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
assert tests.sensitization4()
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2848 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (2848 pixels, meshable)')

# select more pixels
checkpoint OOF.PixelGroup.AddSelection
findGfxWindow('Graphics_1').simulateMouse('down', 82.6125, 57.675, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.6125, 57.675, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.1375, 57.675, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.2375, 56.1, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.9125, 54, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 95.2125, 49.8, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 99.9375, 45.075, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 103.6125, 40.35, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 108.8625, 34.575, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.0625, 29.85, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 115.6875, 27.225, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 117.2625, 26.175, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 119.8875, 24.6, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 121.9875, 23.55, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 122.5125, 23.55, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 122.5125, 23.55, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 122.5125, 23.55, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 121.9875, 24.075, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 121.4625, 24.6, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 121.4625, 25.125, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 121.4625, 25.125, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 120.9375, 25.65, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 120.9375, 25.65, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 120.9375, 25.65, 1, True, False)
checkpoint microstructure page sensitized

# create a new pixel group
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2848 pixels, meshable)', 'pixelgroup<2> (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (0 pixels, meshable)')
assert tests.sensitization3()

findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2848 pixels, meshable)', 'pixelgroup<2> (9216 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (9216 pixels, meshable)')
assert tests.sensitization4()

# undo the pixel selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.9000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 1.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Undo
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2848 pixels, meshable)', 'pixelgroup<2> (9216 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (9216 pixels, meshable)')
assert tests.sensitization4()

# select the other group
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2848 pixels, meshable)', 'pixelgroup<2> (9216 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (2848 pixels, meshable)')
assert tests.sensitization4()

# go back to the first group
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2848 pixels, meshable)', 'pixelgroup<2> (9216 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (9216 pixels, meshable)')
assert tests.sensitization4()

# remove some pixels from a group
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Remove').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.RemoveSelection
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2848 pixels, meshable)', 'pixelgroup<2> (6368 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (6368 pixels, meshable)')
assert tests.sensitization4()


# # actually, we wanted to remove all the pixels from a group, so select
# the pixels in the group first.
event(Gdk.EventType.BUTTON_PRESS,x= 6.9000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Pixel Selection
findWidget('OOF2:Pixel Selection Page:Pane').set_position(273)
checkpoint pixel page updated
checkpoint pixel page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 8.9000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.0100000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Select Group:group').get_window())
checkpoint toplevel widget mapped chooserPopup-group
findMenu(findWidget('chooserPopup-group'), ['pixelgroup<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-group') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Select_Group

# now remove the pixels again
event(Gdk.EventType.BUTTON_PRESS,x= 3.1000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Remove').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.RemoveSelection
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2848 pixels, meshable)',                                  'pixelgroup<2> (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (0 pixels, meshable)')
assert tests.sensitization3()

# add a second image layer for micro2
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(203, 193)
event(Gdk.EventType.BUTTON_PRESS,x= 6.0000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:what:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['micro2']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New

# select pixels in micro2
findGfxWindow('Graphics_1').simulateMouse('up', 44.8125, 50.85, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
findGfxWindow('Graphics_1').simulateMouse('down', 44.2875, 50.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 49.0125, 47.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.0625, 45.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.5875, 45.075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.5875, 44.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 51.1125, 44.025, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 51.6375, 43.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.1625, 42.975, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.1625, 42.975, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.1625, 42.975, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.1625, 42.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.6875, 42.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.6875, 41.925, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 53.2125, 41.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 53.7375, 40.875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 53.7375, 40.875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 54.2625, 40.875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 54.2625, 40.875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 54.7875, 40.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 54.7875, 40.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.3125, 39.825, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.3125, 39.825, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.8375, 39.825, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.3125, 39.825, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 55.3125, 39.825, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1

# switch to micro2 in the microstructure page
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
event(Gdk.EventType.BUTTON_PRESS,x= 3.7000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Microstructure Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['micro2']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (0 pixels, meshable)')
assert tests.sensitization3()

# add pixels
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (762 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (762 pixels, meshable)')
assert tests.sensitization4()

# select more pixels
findGfxWindow('Graphics_1').simulateMouse('down', 71.0625, 24.6, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.5875, 24.075, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 72.1125, 24.075, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 73.1625, 23.025, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 74.2125, 22.5, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 75.2625, 21.975, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 75.7875, 20.925, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 76.8375, 19.875, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78.4125, 18.825, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.4625, 18.3, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 81.0375, 17.25, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 81.5625, 16.725, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 81.5625, 16.725, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.0875, 16.2, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.6125, 15.675, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.6625, 15.15, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.2375, 14.625, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.2375, 14.625, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.2375, 14.1, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.7625, 14.1, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.7625, 14.1, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.2875, 14.1, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.2875, 14.1, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.2875, 13.575, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 86.2875, 13.575, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (762 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (762 pixels, meshable)')
assert tests.sensitization4()

# clear the pixel selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (762 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (762 pixels, meshable)')
assert tests.sensitization5()

# select more pixels
findGfxWindow('Graphics_1').simulateMouse('down', 82.6125, 90.225, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.6125, 90.225, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.6125, 89.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.1375, 89.175, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.7125, 88.125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.2875, 87.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.3375, 87.075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.3875, 86.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.4375, 86.025, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 90.4875, 85.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 91.5375, 84.975, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 92.5875, 84.975, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 94.6875, 83.925, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 96.7875, 83.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 98.8875, 82.875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 100.4625, 81.825, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 103.0875, 81.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 104.6625, 81.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 106.2375, 80.775, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 107.8125, 80.775, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 109.9125, 80.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 111.4875, 79.725, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 112.5375, 79.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.0625, 79.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.0625, 79.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.5875, 79.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.5875, 79.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.5875, 79.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 113.5875, 79.2, 1, False, False)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle

# create a new pixel group in micro2
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (762 pixels, meshable)',                                  'pixelgroup<2> (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (0 pixels, meshable)')
assert tests.sensitization3()

findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (762 pixels, meshable)', 'pixelgroup<2> (1879 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (1879 pixels, meshable)')
assert tests.sensitization4()

# click the meshable button
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Meshable').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Meshable
assert tests.meshableCheck(0)
assert tests.selectedGroupCheck('pixelgroup<2> (1879 pixels)')

# Select a different group
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (762 pixels, meshable)', 'pixelgroup<2> (1879 pixels)')
assert tests.selectedGroupCheck('pixelgroup (762 pixels, meshable)')
assert tests.sensitization4()

# switch to micro1
event(Gdk.EventType.BUTTON_PRESS,x= 5.7000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Microstructure Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['micro1']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
checkpoint meshable button set
checkpoint microstructure page sensitized
assert tests.meshableCheck(1)

# switch to micro2
event(Gdk.EventType.BUTTON_PRESS,x= 3.8000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Microstructure Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['micro2']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
checkpoint meshable button set
checkpoint microstructure page sensitized
assert tests.meshableCheck(1)

# select the unmeshable group
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.meshableCheck(0)

# delete micro2
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(184, 86)
findWidget('Questioner:Yes').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
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
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
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
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.Delete
# deleted micro2, switched back to micro1
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2848 pixels, meshable)', 'pixelgroup<2> (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (0 pixels, meshable)')
assert tests.sensitization3()
assert tests.microstructureCheck('micro1')

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
