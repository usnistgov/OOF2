import tests
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials', 'Microstructure']).activate()
checkpoint toplevel widget mapped Microstructure
findWidget('Microstructure').resize(500, 300)
findWidget('OOF2').resize(782, 545)
findWidget('Microstructure').resize(500, 300)
findWidget('Microstructure:Next').clicked()
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
findWidget('Microstructure:Next').clicked()
findWidget('Microstructure:Next').clicked()
findWidget('Microstructure').resize(500, 326)
event(Gdk.EventType.BUTTON_PRESS,x= 8.2000000000000e+01,y= 2.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
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
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_m')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_ms')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_msa')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_msal')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_msa')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_ms')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_m')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_s')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_sm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_sma')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_smal')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.pg')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.pgm')
findWidget('Dialog-Load Image and create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint active area status updated
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
checkpoint pixel page updated
checkpoint mesh bdy page updated
checkpoint pixel page sensitized
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
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
findWidget('Microstructure:Next').clicked()
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.0200000000000e+02,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Image']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Image
findWidget('OOF2:Image Page:Pane').set_position(546)
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 9.9000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Normalize']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Normalize
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.0700000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Contrast']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Contrast
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Contrast
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Contrast
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 5.6000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('Microstructure:Next').clicked()
findGfxWindow('Graphics_1').simulateMouse('down', 33.73775, 56.966, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 33.73775, 56.6475, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('up', 33.73775, 56.6475, 1, 0, 0)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 1)
findWidget('Microstructure:Next').clicked()
findGfxWindow('Graphics_1').simulateMouse('down', 36.92275, 54.418, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 36.92275, 54.418, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('up', 36.92275, 54.418, 1, 1, 0)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 2)
findGfxWindow('Graphics_1').simulateMouse('down', 35.64875, 50.596, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 35.64875, 50.596, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('up', 35.64875, 50.596, 1, 1, 0)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 3)
findGfxWindow('Graphics_1').simulateMouse('down', 40.42625, 53.4625, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('up', 40.42625, 53.4625, 1, 0, 1)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 4)
findGfxWindow('Graphics_1').simulateMouse('down', 40.74475, 53.144, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('up', 40.74475, 53.144, 1, 0, 1)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 3)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Undo
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 4)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Redo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Redo
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 3)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Redo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Redo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Invert').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Invert
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 8368)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint pixel page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 0)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'In']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 6.1000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 7.4000000000000e+01)
checkpoint OOF.Graphics_1.Settings.Zoom.In
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'Out']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 0.0000000000000e+00)
checkpoint OOF.Graphics_1.Settings.Zoom.Out
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'In']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 6.1000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 7.5000000000000e+01)
checkpoint OOF.Graphics_1.Settings.Zoom.In
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'Out']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 0.0000000000000e+00)
checkpoint OOF.Graphics_1.Settings.Zoom.Out
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'Fill_Window']).activate()
checkpoint OOF.Graphics_1.Settings.Zoom.Fill_Window
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.2800000000000e+02,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 8.89475, 75.1205, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 8.89475, 74.802, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 9.21325, 73.528, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 9.85025, 69.706, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 13.99075, 64.61, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 22.59025, 62.3805, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 35.01175, 58.877, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 45.84075, 56.966, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 53.48475, 55.692, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 54.44025, 55.692, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 54.75875, 55.692, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 55.07725, 55.692, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 55.07725, 55.692, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('up', 55.07725, 55.692, 1, 0, 0)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 1008)
event(Gdk.EventType.BUTTON_PRESS,x= 1.0500000000000e+02,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Ellipse']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 25.13825, 63.0175, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 25.45675, 62.699, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 26.09375, 62.062, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 26.41225, 59.8325, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 30.87125, 57.2845, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 34.37475, 55.692, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 37.55975, 53.4625, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 41.38175, 51.5515, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 46.15925, 50.2775, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 51.89225, 48.685, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 56.35125, 47.411, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 62.72125, 45.8185, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 66.22475, 45.5, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 71.95775, 44.863, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 74.50575, 44.226, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 75.14275, 44.226, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 76.41675, 44.226, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 76.73525, 44.226, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('up', 76.73525, 44.226, 1, 0, 1)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Ellipse
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 1381)
event(Gdk.EventType.BUTTON_PRESS,x= 1.1900000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 55.39575, 43.589, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 55.39575, 43.589, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 55.71425, 43.2705, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 56.66975, 42.315, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 57.30675, 41.678, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 57.94375, 41.041, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 58.89925, 39.767, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 60.17325, 38.8115, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 62.08425, 36.9005, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 63.03975, 35.6265, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 63.99525, 34.3525, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 64.95075, 33.397, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 65.26925, 32.76, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 65.58775, 32.4415, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 65.90625, 32.123, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 66.54325, 31.486, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 66.86175, 31.1675, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 67.18025, 31.1675, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 67.18025, 31.1675, 1, 0, 1)
findGfxWindow('Graphics_1').simulateMouse('up', 67.18025, 31.1675, 1, 0, 1)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 1585)
findGfxWindow('Graphics_1').simulateMouse('down', 56.66975, 32.76, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 56.66975, 32.76, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 56.66975, 32.4415, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 57.30675, 31.8045, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 57.62525, 31.1675, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 58.58075, 29.8935, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 59.21775, 28.938, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 59.53625, 28.6195, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 59.53625, 28.301, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 60.17325, 27.3455, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 60.81025, 26.7085, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 61.44725, 25.753, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 62.08425, 24.7975, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 63.03975, 23.842, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 63.67675, 23.205, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 63.67675, 22.568, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 64.95075, 21.6125, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 65.90625, 20.9755, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 65.90625, 20.657, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 65.90625, 20.3385, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 65.90625, 20.3385, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 66.22475, 20.02, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 66.22475, 20.02, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 66.54325, 19.7015, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 66.54325, 19.7015, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 66.54325, 19.7015, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 66.54325, 19.383, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('move', 66.54325, 19.383, 1, 1, 1)
findGfxWindow('Graphics_1').simulateMouse('up', 66.54325, 19.383, 1, 1, 1)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 453)
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.1800000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Brush']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Circle:radius').set_text('')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Circle:radius').set_text('5')
findGfxWindow('Graphics_1').simulateMouse('down', 16.53875, 68.1135, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 16.85725, 68.1135, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 17.81275, 68.432, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 20.36075, 68.7505, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 26.09375, 69.069, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 29.91575, 68.7505, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 33.73775, 67.4765, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 38.83375, 64.9285, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 45.20375, 62.3805, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 46.47775, 61.1065, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 47.43325, 59.8325, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 49.34425, 57.2845, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 49.98125, 56.329, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 49.98125, 55.3735, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 50.29975, 54.0995, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 50.61825, 53.144, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 50.93675, 52.507, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 51.25525, 52.1885, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 51.57375, 52.1885, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 51.57375, 52.1885, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('up', 51.57375, 52.1885, 1, 0, 0)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Brush
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 499)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.1000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.8787576237703e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 0)
findWidget('Microstructure:Next').clicked()
findWidget('Microstructure').resize(500, 338)
event(Gdk.EventType.BUTTON_PRESS,x= 9.1000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Color']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
event(Gdk.EventType.BUTTON_PRESS,x= 1.1600000000000e+02,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['DeltaGray']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 6.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 7.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry').set_text('0.')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry').set_text('0.4')
findGfxWindow('Graphics_1').simulateMouse('down', 72.27625, 60.151, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('up', 72.27625, 60.151, 1, 0, 0)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 5799)
widget_0=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry')
if widget_0: event(Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Color
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 5799)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 9.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Invert').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Invert
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 2573)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 9.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 8.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.1000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
event(Gdk.EventType.BUTTON_PRESS,x= 7.7000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Brush']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Circle:radius').set_text('')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Circle:radius').set_text('3')
findGfxWindow('Graphics_1').simulateMouse('down', 39.47075, 25.753, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 39.78925, 25.753, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 39.78925, 25.753, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 39.78925, 25.753, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 40.42625, 25.753, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 40.74475, 25.4345, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 41.06325, 25.4345, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 41.70025, 25.4345, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 41.70025, 25.4345, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 42.33725, 25.116, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 42.65575, 25.116, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 42.97425, 24.7975, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 43.61125, 24.7975, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 44.24825, 24.479, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 44.88525, 24.479, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 45.20375, 24.479, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 46.15925, 24.1605, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 46.79625, 23.842, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 47.11475, 23.842, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 48.07025, 23.205, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 48.70725, 23.205, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 49.34425, 22.8865, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 49.66275, 22.8865, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 50.29975, 22.568, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 50.93675, 22.2495, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 51.57375, 22.2495, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 52.52925, 21.931, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 53.48475, 21.6125, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 53.80325, 21.6125, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 53.80325, 21.6125, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 54.12175, 21.294, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 54.44025, 21.294, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 54.75875, 21.294, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 54.44025, 20.9755, 1, 1, 0)
findGfxWindow('Graphics_1').simulateMouse('up', 54.44025, 20.9755, 1, 1, 0)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Brush
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 2647)
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 9.1000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
assert tests.newPixelGroupSensitizationCheck0()
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 11)
findWidget('Dialog-Create new pixel group:name').insert_text('w', 11)
assert tests.newPixelGroupSensitizationCheck1()
findWidget('Dialog-Create new pixel group:name').insert_text('h', 1)
findWidget('Dialog-Create new pixel group:name').insert_text('i', 2)
findWidget('Dialog-Create new pixel group:name').insert_text('t', 3)
findWidget('Dialog-Create new pixel group:name').insert_text('e', 4)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.chooserListStateCheck("OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList", ['white (0 pixels, meshable)'])
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 2647)
checkpoint OOF.PixelGroup.AddSelection
## The gtk2 version says that the number of pixels in a group depends
## on the ImageMagick version, so these tests are unreliable.
assert tests.chooserListStateCheck("OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList", ['white (2647 pixels, meshable)'])
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
event(Gdk.EventType.BUTTON_PRESS,x= 1.3300000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Burn']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
findGfxWindow('Graphics_1').simulateMouse('down', 18.44975, 49.0035, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 18.44975, 49.0035, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('up', 18.44975, 49.0035, 1, 0, 0)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 1259)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 5.6000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('up', 83.10525, 57.2845, 1, 1, 0)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 2670)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionTBSizeCheck("OOF2 Graphics 1", 0)
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Image']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Image
findWidget('OOF2:Image Page:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy Image
findWidget('Dialog-Copy Image').resize(317, 134)
findWidget('Dialog-Copy Image:widget_GTK_RESPONSE_OK').clicked()
checkpoint microstructure page sensitized
checkpoint OOF.Image.Copy
findWidget('Microstructure:Next').clicked()
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
event(Gdk.EventType.BUTTON_PRESS,x= 8.1000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Image']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.1500000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:what:Image').get_window())
checkpoint toplevel widget mapped chooserPopup-Image
findMenu(findWidget('chooserPopup-Image'), ['K1_small.pgm<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Image') # MenuItemLogger
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 8.7000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Image').get_window())
checkpoint toplevel widget mapped chooserPopup-Image
findMenu(findWidget('chooserPopup-Image'), ['K1_small.pgm']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Image') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:Undo').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Undo
findWidget('OOF2:Image Page:Pane:Undo').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Undo
findWidget('OOF2:Image Page:Pane:Undo').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Undo
findWidget('OOF2:Image Page:Pane:Undo').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Undo
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 2.1600000000000e+02,y= 1.3000000000000e+01,button=3,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
checkpoint toplevel widget mapped PopUp-0
findMenu(findWidget('PopUp-0'), ['Lower', 'One_Level']).activate() # MenuItemLogger
deactivatePopup('PopUp-0') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Lower.One_Level
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:slider').get_adjustment().set_value( 1.0000000000000e+00)
event(Gdk.EventType.BUTTON_PRESS,x= 8.1000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findWidget('chooserPopup-TBChooser').deactivate() # MenuLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 0.0000000000000e+00)
event(Gdk.EventType.BUTTON_PRESS,x= 8.7000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Color']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 7.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry').set_text('0.')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry').set_text('0.0')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry').set_text('0.05')
findGfxWindow('Graphics_1').simulateMouse('down', 76.09825, 60.788, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 76.41675, 60.788, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 76.73525, 60.788, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 76.73525, 60.788, 1, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('up', 76.73525, 60.788, 1, 0, 0)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
assert tests.pixelSelectionTBSizeCheck("OOF2 Graphics 1", 4122)
widget_1=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry')
if widget_1: event(Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_1.get_window())
del widget_1
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Color
assert tests.pixelSelectionTBSizeCheck("OOF2 Graphics 1", 4122)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 7.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 9.1000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 9.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.5756154210084e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
event(Gdk.EventType.BUTTON_PRESS,x= 1.3200000000000e+02,y= 3.6000000000000e+01,button=3,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
checkpoint toplevel widget mapped PopUp-1
findMenu(findWidget('PopUp-1'), ['Raise', 'One_Level']).activate() # MenuItemLogger
deactivatePopup('PopUp-1') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Raise.One_Level
event(Gdk.EventType.BUTTON_RELEASE,x= 4.0000000000000e+01,y= 2.1000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Color
assert tests.pixelSelectionTBSizeCheck("OOF2 Graphics 1", 4916)
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 8.8000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Pixel Selection
findWidget('OOF2:Pixel Selection Page:Pane').set_position(273)
checkpoint pixel page updated
checkpoint pixel page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 1.6900000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.3800000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Select Group:group').get_window())
checkpoint toplevel widget mapped chooserPopup-group
findWidget('chooserPopup-group').deactivate() # MenuLogger
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Select_Group
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 2.1200000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Invert']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Invert
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.1000000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 5)
findWidget('Dialog-Create new pixel group:name').insert_text('b', 11)
findWidget('Dialog-Create new pixel group:name').insert_text('l', 1)
findWidget('Dialog-Create new pixel group:name').insert_text('a', 2)
findWidget('Dialog-Create new pixel group:name').insert_text('c', 3)
findWidget('Dialog-Create new pixel group:name').insert_text('k', 4)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint OOF.PixelGroup.New
assert tests.treeViewColCheck("OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList", 0, ['black (0 pixels, meshable)', 'white (2647 pixels, meshable)'])
findWidget('Microstructure:Next').clicked()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
assert tests.treeViewColCheck("OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList", 0, ['black (5725 pixels, meshable)', 'white (2647 pixels, meshable)'])
findWidget('Microstructure:Next').clicked()
findWidget('Microstructure').resize(500, 458)
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Microstructure']).activate()
checkpoint toplevel widget mapped Dialog-Microstructure
findWidget('Dialog-Microstructure').resize(235, 188)
findWidget('Dialog-Microstructure:filename').set_text('m')
findWidget('Dialog-Microstructure:filename').set_text('mi')
findWidget('Dialog-Microstructure:filename').set_text('mic')
findWidget('Dialog-Microstructure:filename').set_text('micr')
findWidget('Dialog-Microstructure:filename').set_text('micro')
findWidget('Dialog-Microstructure:filename').set_text('micros')
findWidget('Dialog-Microstructure:filename').set_text('microst')
findWidget('Dialog-Microstructure:filename').set_text('microstr')
findWidget('Dialog-Microstructure:filename').set_text('microstru')
findWidget('Dialog-Microstructure:filename').set_text('microstruc')
findWidget('Dialog-Microstructure:filename').set_text('microstruct')
findWidget('Dialog-Microstructure:filename').set_text('microstructu')
findWidget('Dialog-Microstructure:filename').set_text('microstructur')
findWidget('Dialog-Microstructure:filename').set_text('microstructure')
findWidget('Dialog-Microstructure:filename').set_text('microstructure.')
findWidget('Dialog-Microstructure:filename').set_text('microstructure.a')
findWidget('Dialog-Microstructure:filename').set_text('microstructure.')
findWidget('Dialog-Microstructure:filename').set_text('microstructure.d')
findWidget('Dialog-Microstructure:filename').set_text('microstructure.da')
findWidget('Dialog-Microstructure:filename').set_text('microstructure.dat')
findWidget('Dialog-Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Microstructure
assert tests.filediff('microstructure.dat')
findWidget('Microstructure:Next').clicked()
findWidget('Microstructure:Close').clicked()
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
assert tests.filediff('session.log')
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
