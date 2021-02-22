# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests
tbox="OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Info"

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)

# Open a graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2').resize(782, 545)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
wevent(findWidget('Dialog-New_Layer_Policy:policy'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.New_Layer_Policy
findWidget('OOF2 Graphics 1').resize(800, 492)

# Open the pixel info toolbox
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Info']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(224)
assert tests.gtkMultiTextCompare({'X':'','Y':'','Image':'','Text 1':'','Text 2':'','Text 3':'','MSText':'(No microstructure)','material':''},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':False},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkTextviewCompare(tbox+":MSScroll:Group view","")

# Create a microstructure from an image
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
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
findWidget('Dialog-Load Image and create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Microstructure.Create_From_ImageFile
assert tests.gtkMultiTextCompare({'X':'','Y':'','Image':'???','Text 1':'???','Text 2':'???','Text 3':'???','MSText':'???','material':'???'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':False},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','')

# Click on  a pixel
findGfxWindow('Graphics_1').simulateMouse('down', 44.025, 68.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 44.025, 68.7, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.gtkMultiTextCompare({'X':'44','Y':'68','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'<No material>'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','')
assert tests.gtkMultiFloatCompare({'Text 1':0.0,'Text 2':0.9882352941,'Text 3':0.0},tbox)

# Click on another pixel
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('down', 132.225, 87.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 132.225, 87.6, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.gtkMultiTextCompare({'X':'132','Y':'87','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'<No material>'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkMultiFloatCompare({'Text 1':0.0,'Text 2':0.0,'Text 3':0.97254901},tbox)
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','')

# Click on another pixel again
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('down', 114.9, 135.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 114.9, 135.9, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.gtkMultiTextCompare({'X':'114','Y':'135','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'<No material>'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkMultiFloatCompare({'Text 1':0.97254901,'Text 2':0.9882352941,'Text 3':0.0},tbox)
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','')

# Select some pixels
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Burn']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 92.5875, 127.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 92.5875, 127.5, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn

# Make a pixel group and put the pixels in it
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 11)
findWidget('Dialog-Create new pixel group:name').insert_text('y', 11)
findWidget('Dialog-Create new pixel group:name').insert_text('e', 1)
findWidget('Dialog-Create new pixel group:name').insert_text('l', 2)
findWidget('Dialog-Create new pixel group:name').insert_text('l', 3)
findWidget('Dialog-Create new pixel group:name').insert_text('o', 4)
findWidget('Dialog-Create new pixel group:name').insert_text('w', 5)
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
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Info']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(224)
# Selected pixel was part of set added to group "yellow".
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','yellow')

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 5.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 7.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2800000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.9000000000000e+02)

# Burn more pixels
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 5.6000000000000e+01)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
findGfxWindow('Graphics_1').simulateMouse('down', 23.2875, 84.975, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 23.2875, 84.975, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn

# Create a group and add pixels
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 6)
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
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection

# Clear the pixel selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear

# Check that creating the green pixel group hasn't changed the info toolbox
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Info']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(224)
assert tests.gtkMultiTextCompare({'X':'114','Y':'135','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'<No material>'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkMultiFloatCompare({'Text 1':0.97254902,'Text 2':0.9882353,'Text 3':0.0},tbox)
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','yellow')

# Rename the yellow pixel group
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename pixelgroup yellow
findWidget('Dialog-Rename pixelgroup yellow').resize(192, 92)
findWidget('Dialog-Rename pixelgroup yellow:new_name').set_text('')
findWidget('Dialog-Rename pixelgroup yellow:new_name').set_text('o')
findWidget('Dialog-Rename pixelgroup yellow:new_name').set_text('ow')
findWidget('Dialog-Rename pixelgroup yellow:new_name').set_text('owl')
findWidget('Dialog-Rename pixelgroup yellow:new_name').set_text('owl ')
findWidget('Dialog-Rename pixelgroup yellow:new_name').set_text('owl l')
findWidget('Dialog-Rename pixelgroup yellow:new_name').set_text('owl ly')
findWidget('Dialog-Rename pixelgroup yellow:new_name').set_text('owl lye')
findWidget('Dialog-Rename pixelgroup yellow:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Rename
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.gtkMultiTextCompare({'X':'114','Y':'135','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'<No material>'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkMultiFloatCompare({'Text 1':0.97254902,'Text 2':0.9882353,'Text 3':0.0},tbox)
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','owl lye')

wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:global_flammability:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 5.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.9000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 5.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 4.3134023981909e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.2407018520074e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.3624527503150e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.6592094819793e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.1115264358657e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 6.9995800083999e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 4.0505856576758e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.0738251951406e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 8.7484250944981e-01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.5918148925900e-01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.2386023223729e-02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 0.0000000000000e+00)
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.6000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 62.6625, 124.875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 62.6625, 124.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 61.6125, 121.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.0375, 113.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.0375, 108.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 61.0875, 104.925, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 62.1375, 100.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 63.1875, 97.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 67.9125, 93.375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.5875, 91.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.8875, 88.125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.6625, 84.975, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.9625, 82.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 97.3125, 81.825, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 100.9875, 81.825, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 107.8125, 80.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.9625, 79.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 112.0125, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 112.5375, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.0625, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.5875, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.5875, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.5875, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 114.1125, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.5875, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.5875, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.5875, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.0625, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 113.0625, 78.675, 1, False, False)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle

# Put the selection in a group named "test"
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 5)
findWidget('Dialog-Create new pixel group:name').insert_text('t', 11)
findWidget('Dialog-Create new pixel group:name').insert_text('e', 1)
findWidget('Dialog-Create new pixel group:name').insert_text('r', 2)
findWidget('Dialog-Create new pixel group:name').insert_text('s', 3)
findWidget('Dialog-Create new pixel group:name').insert_text('t', 4)
findWidget('Dialog-Create new pixel group:name').delete_text(4, 5)
findWidget('Dialog-Create new pixel group:name').delete_text(3, 4)
findWidget('Dialog-Create new pixel group:name').insert_text('s', 3)
findWidget('Dialog-Create new pixel group:name').insert_text('t', 4)
findWidget('Dialog-Create new pixel group:name').delete_text(2, 3)
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
assert tests.gtkMultiTextCompare({'X':'114','Y':'135','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'<No material>'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkMultiFloatCompare({'Text 1':0.97254902,'Text 2':0.9882353,'Text 3':0.0},tbox)
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','owl lye')

# Click on a pixel that's just in the green group
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Info']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 9.375, 75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 9.375, 75, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(224)
assert tests.gtkMultiTextCompare({'X':'9','Y':'75','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'<No material>'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkMultiFloatCompare({'Text 1':0.0,'Text 2':0.9882353,'Text 3':0.0},tbox)
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','green')

# Click on a pixel that's in green and in test
findGfxWindow('Graphics_1').simulateMouse('down', 77.625, 92.325, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 77.625, 92.325, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.6210144887378e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.9510144887378e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.0410144887378e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.5200000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.9000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.5110144887378e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.5010144887378e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.1510144887378e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.9910144887378e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.9101448873780e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 0.0000000000000e+00)
assert tests.gtkMultiTextCompare({'X':'77','Y':'92','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'<No material>'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkMultiFloatCompare({'Text 1':0.0,'Text 2':0.9882353,'Text 3':0.0},tbox)
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','green\ntest')

# Delete the green group
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(184, 86)
findWidget('Questioner:Yes').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.Delete
assert tests.gtkMultiTextCompare({'X':'77','Y':'92','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'<No material>'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkMultiFloatCompare({'Text 1':0.0,'Text 2':0.9882353,'Text 3':0.0},tbox)
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','test')

# Edit the position of the queried pixel
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 8.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Info:X').set_text('')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Info:X').set_text('1')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Info:X').set_text('10')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Info:X').set_text('100')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 8.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Info:Y').set_text('')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Info:Y').set_text('1')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Info:Y').set_text('10')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Info:Y').set_text('100')
# Typed in coordinates -- "Update" button should be sensitive now.
assert tests.sensitizationCheck({'Update':True,'Clear':True},tbox)

# Update
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 8.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 7.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Info:Update').clicked()
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
assert tests.gtkMultiTextCompare({'X':'100','Y':'100','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'<No material>'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkMultiFloatCompare({'Text 1':0.97254901960784312,'Text 2':0.9882353,'Text 3':0.97254901960784312},tbox)
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','test')

# Clear the toolbox
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(300)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Info:Clear').clicked()
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Clear
assert tests.gtkMultiTextCompare({'X':'','Y':'','Image':'???','Text 1':'???','Text 2':'???','Text 3':'???','MSText':'???','material':'???'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':False},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','')

# Click on a new pixel
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('down', 84.975, 112.275, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 84.975, 112.275, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.1077844311377e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 4.2155688622754e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 6.3233532934132e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 8.4311377245509e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.0538922155689e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.4754491017964e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.8970059880240e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.5293413173653e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.9508982035928e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.5832335329341e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 4.0047904191617e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 4.6371257485030e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 5.0586826347305e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 5.9017964071856e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 6.7449101796407e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 8.2203592814371e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 9.0634730538922e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 9.6958083832335e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.0538922155689e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.1171257485030e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.1592814371257e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.1803592814371e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2225149700599e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2435928143713e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2646706586826e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2857485029940e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.3068263473054e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.3279041916168e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.3489820359281e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.3700598802395e+02)
assert tests.gtkMultiTextCompare({'X':'84','Y':'112','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'<No material>'},tbox)
# FIX X and Y
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkMultiFloatCompare({'Text 1':0.97254902,'Text 2':0.9882353,'Text 3':0.0},tbox)
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','owl lye\ntest')

# Create a material and assign it to the yellow pixels
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:name').delete_text(0, 11)
findWidget('Dialog-New material:name').insert_text('s', 11)
findWidget('Dialog-New material:name').insert_text('t', 1)
findWidget('Dialog-New material:name').insert_text('f', 2)
findWidget('Dialog-New material:name').delete_text(2, 3)
findWidget('Dialog-New material:name').insert_text('u', 2)
findWidget('Dialog-New material:name').insert_text('f', 3)
findWidget('Dialog-New material:name').insert_text('f', 4)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material stuff to pixels
findWidget('Dialog-Assign material stuff to pixels').resize(214, 122)
wevent(findWidget('Dialog-Assign material stuff to pixels:pixels'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Assign material stuff to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['owl lye']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material stuff to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign
# New material added to pixels, should show up now.
assert tests.gtkMultiTextCompare({'X':'84','Y':'112','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'stuff'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkMultiFloatCompare({'Text 1':0.97254902,'Text 2':0.9882353,'Text 3':0.0},tbox)

# Click on a white pixel
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('down', 74.475, 104.925, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 74.475, 104.925, 1, False, False)
checkpoint Graphics_1 Pixel Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Info.Query
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.3600598802395e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2700598802395e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 8.4005988023952e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 0.0000000000000e+00)
assert tests.gtkMultiTextCompare({'X':'74','Y':'104','Image':'small.ppm:small.ppm','MSText':'small.ppm','material':'<No material>'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkMultiFloatCompare({'Text 1':0.97254902,'Text 2':0.9882353,'Text 3':0.97254901960784312},tbox)

# Delete the graphics layer
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([13]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 8.4260648142593e-01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.4074251850074e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.7500149997000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.9259348144593e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.9907435182408e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.9988433563134e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'Delete']).activate()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Delete
assert tests.gtkMultiTextCompare({'X':'74','Y':'104','Image':'???','Text 1':'???','Text 2':'???','Text 3':'???','MSText':'???','material':'???'},tbox)
assert tests.sensitizationCheck({'Update':False,'Clear':True},tbox)
assert findWidget(tbox+':RGB selector').get_active()
assert tests.gtkTextviewCompare(tbox+':MSScroll:Group view','')

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
