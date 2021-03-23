import tests
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials', 'Microstructure']).activate()
checkpoint toplevel widget mapped Microstructure
findWidget('Microstructure').resize(500, 300)
findWidget('OOF2').resize(782, 545)
findWidget('Microstructure').resize(500, 300)
findWidget('Microstructure:Next').clicked()
findWidget('Microstructure').resize(500, 362)
event(Gdk.EventType.BUTTON_PRESS,x= 9.3000000000000e+01,y= 2.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
checkpoint page installed Microstructure
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
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
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1')
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
checkpoint pixel page updated
checkpoint active area status updated
checkpoint pixel page sensitized
checkpoint mesh bdy page updated
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
findWidget('Microstructure:Next').clicked()
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
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
event(Gdk.EventType.BUTTON_PRESS,x= 8.7000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:category').get_window())
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
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 8.5000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Image']).activate() # MenuItemLogger
checkpoint page installed Image
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Image Page:Pane').set_position(546)
findWidget('Microstructure:Next').clicked()
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 4.7000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Normalize']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Normalize
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Contrast']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2').resize(782, 545)
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
event(Gdk.EventType.BUTTON_PRESS,x= 8.3000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
findWidget('Microstructure:Next').clicked()
findGfxWindow('Graphics_1').simulateMouse('down', 65.90625, 54.7365, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 65.90625, 54.7365, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 65.90625, 54.7365, 1, False, False)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 1)
findWidget('Microstructure:Next').clicked()
findGfxWindow('Graphics_1').simulateMouse('down', 72.59475, 53.781, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 73.55025, 53.781, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 73.55025, 53.781, 1, False, True)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 2)
findGfxWindow('Graphics_1').simulateMouse('down', 74.82425, 60.4695, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 75.14275, 60.4695, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 75.14275, 60.4695, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 75.46125, 60.4695, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 75.46125, 60.4695, 1, False, True)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 3)
findGfxWindow('Graphics_1').simulateMouse('down', 67.49875, 61.1065, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 67.49875, 61.1065, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 67.81725, 60.788, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 67.81725, 60.788, 1, False, True)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 4)
findGfxWindow('Graphics_1').simulateMouse('down', 67.18025, 60.151, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 67.18025, 60.151, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 67.18025, 60.151, 1, False, True)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 3)
findGfxWindow('Graphics_1').simulateMouse('down', 68.45425, 60.788, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 68.45425, 60.788, 1, False, True)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 4)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Undo
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 3)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Redo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Redo
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 4)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Invert').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Invert
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 8368)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
findWidget('Microstructure:Next').clicked()
findGfxWindow('Graphics_1').simulateMouse('down', 70.68375, 49.322, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 70.68375, 49.322, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 70.68375, 49.322, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 1)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'In']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 6.1000000000000e+01)
checkpoint OOF.Graphics_1.Settings.Zoom.In
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 7.4000000000000e+01)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'In']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.9000000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.8500000000000e+02)
checkpoint OOF.Graphics_1.Settings.Zoom.In
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'Out']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 6.1000000000000e+01)
checkpoint OOF.Graphics_1.Settings.Zoom.Out
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.5000000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 7.3000000000000e+01)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'Fill_Window']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 0.0000000000000e+00)
checkpoint OOF.Graphics_1.Settings.Zoom.Fill_Window
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 0.0000000000000e+00)
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.6100000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 18.13125, 70.343, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 18.13125, 70.343, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 18.13125, 69.3875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 17.49425, 66.521, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 17.17575, 62.3805, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 16.85725, 58.24, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 17.17575, 56.329, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 18.13125, 55.055, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 20.04225, 53.781, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 22.59025, 52.8255, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.73075, 52.1885, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 33.73775, 50.9145, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 37.87825, 50.596, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.33725, 49.6405, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 46.15925, 49.322, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.75175, 49.322, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 49.66275, 49.0035, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.93675, 49.0035, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.52925, 48.685, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 54.75875, 48.3665, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.03275, 48.048, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.35125, 48.048, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.35125, 48.048, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.35125, 48.048, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.35125, 48.048, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.03275, 48.048, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.39575, 48.048, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 55.39575, 48.048, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 874)
event(Gdk.EventType.BUTTON_PRESS,x= 8.5000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 60.49175, 60.788, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.81025, 60.788, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.81025, 60.788, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 61.76575, 59.8325, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 63.67675, 58.5585, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 66.22475, 56.966, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 68.77275, 55.055, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 70.68375, 53.144, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 74.18725, 51.5515, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.37225, 50.2775, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.28325, 49.322, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.60175, 49.322, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.60175, 49.322, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.23875, 48.685, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.87575, 48.3665, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.87575, 48.048, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.87575, 48.048, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.87575, 48.048, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.87575, 48.3665, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.87575, 48.685, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.87575, 49.0035, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.87575, 49.0035, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.87575, 49.322, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.55725, 49.6405, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.55725, 50.2775, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.55725, 50.2775, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.55725, 50.596, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.23875, 50.596, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.23875, 50.596, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.60175, 51.233, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.28325, 51.233, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.28325, 51.233, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78.96475, 51.5515, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78.64625, 51.5515, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 78.64625, 51.5515, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 1842)
event(Gdk.EventType.BUTTON_PRESS,x= 1.3500000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Ellipse']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 23.54575, 66.8395, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 23.86425, 66.8395, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 27.04925, 65.884, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 33.10075, 64.2915, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 40.10775, 62.699, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 45.52225, 61.425, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 49.98125, 60.4695, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 52.84775, 59.8325, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 55.07725, 59.514, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 57.62525, 58.877, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 58.58075, 58.5585, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 59.53625, 58.24, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 61.44725, 57.603, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 63.03975, 56.966, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 64.63225, 56.6475, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 66.54325, 55.692, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 68.77275, 55.055, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 70.68375, 54.0995, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 71.95775, 53.4625, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 72.59475, 53.144, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 72.91325, 52.8255, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 72.91325, 52.507, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 73.23175, 52.507, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 73.55025, 52.1885, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 73.86875, 51.5515, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 74.18725, 51.233, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 74.50575, 50.9145, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 74.50575, 50.9145, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 74.82425, 50.596, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 74.82425, 50.2775, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 75.14275, 49.6405, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 75.14275, 49.0035, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 75.14275, 48.3665, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 75.14275, 48.048, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 75.14275, 48.048, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('move', 75.14275, 48.048, 1, True, True)
findGfxWindow('Graphics_1').simulateMouse('up', 75.14275, 48.048, 1, True, True)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Ellipse
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 766)
findGfxWindow('Graphics_1').simulateMouse('down', 39.78925, 60.4695, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 40.10775, 60.151, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 41.06325, 59.514, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 43.29275, 57.603, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 46.47775, 55.055, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 49.66275, 51.87, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 52.52925, 49.0035, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 54.75875, 46.4555, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 56.03275, 43.9075, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 56.66975, 41.041, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 56.98825, 38.1745, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 56.98825, 35.6265, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 56.98825, 33.397, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 57.62525, 30.849, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 58.26225, 28.6195, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 58.26225, 27.027, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 58.26225, 25.4345, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 58.26225, 24.7975, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 58.26225, 24.479, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 58.26225, 23.205, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 58.58075, 22.2495, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 58.89925, 21.6125, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 58.89925, 20.3385, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 59.85475, 17.7905, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 59.85475, 17.1535, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 59.85475, 17.1535, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 59.85475, 16.5165, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 59.85475, 16.5165, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 59.85475, 16.5165, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 59.85475, 16.198, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 59.85475, 15.8795, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 59.85475, 15.8795, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 59.85475, 15.8795, 1, False, True)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Ellipse
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 1153)
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.4100000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Brush']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Circle:radius').set_text('')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Circle:radius').set_text('5')
findGfxWindow('Graphics_1').simulateMouse('down', 8.89475, 62.699, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.89475, 62.699, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.89475, 62.699, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.85025, 63.336, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.48725, 63.973, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 13.99075, 65.5655, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 16.85725, 66.521, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 21.63475, 67.4765, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.00475, 67.4765, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 34.37475, 66.521, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 37.55975, 64.61, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 39.78925, 61.7435, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.33725, 55.692, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.97425, 50.9145, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.33725, 43.2705, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.01875, 37.219, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.33725, 30.5305, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 45.84075, 24.1605, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.61825, 19.383, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.71425, 16.198, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 64.63225, 13.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 69.72825, 13.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.00225, 13.9685, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 72.27625, 14.287, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 74.18725, 15.2425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 76.41675, 19.0645, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78.00925, 22.8865, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.28325, 27.9825, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.92025, 31.1675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.92025, 33.397, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.55725, 35.945, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.55725, 40.404, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.23875, 41.3595, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 80.23875, 41.3595, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Brush
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 1405)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 0)
event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Color']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.0900000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['DeltaGray']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 6.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:slider').get_adjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:slider').get_adjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:slider').get_adjustment().set_value( 4.1666666666667e-02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:slider').get_adjustment().set_value( 1.3888888888889e-01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:slider').get_adjustment().set_value( 3.1944444444444e-01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:slider').get_adjustment().set_value( 5.9722222222222e-01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:slider').get_adjustment().set_value( 9.3055555555556e-01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 7.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry').set_text('')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry').set_text('0')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry').set_text('0.')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry').set_text('0.4')
findGfxWindow('Graphics_1').simulateMouse('down', 21.31625, 48.3665, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 21.31625, 48.3665, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Color
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 5799)
widget_0=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry')
if widget_0: wevent(widget_0, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 9.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Invert').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Invert
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 2573)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 9.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 9.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 8.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Brush']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Circle:radius').set_text('')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Circle:radius').set_text('3')
findGfxWindow('Graphics_1').simulateMouse('down', 38.19675, 25.753, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 38.51525, 25.753, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 38.83375, 25.753, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 39.47075, 25.753, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 40.74475, 25.753, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.01875, 25.753, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.97425, 25.753, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.61125, 25.4345, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 45.20375, 25.116, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 46.79625, 24.7975, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.75175, 24.479, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 48.07025, 24.1605, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 49.34425, 23.842, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 49.98125, 23.5235, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.61825, 23.205, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.61825, 23.205, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.93675, 23.205, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 51.25525, 22.8865, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 51.89225, 22.568, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.84775, 22.2495, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 53.48475, 21.931, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 53.48475, 21.931, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Brush
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 2649)
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 7.2000000000000e+01,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
checkpoint page installed Microstructure
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
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
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.chooserListStateCheck("OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList", ['white (0 pixels, meshable)'])
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
## The gtk2 version says that the number of pixels in a group depends
## on the ImageMagick version, so these tests are unreliable.
assert tests.chooserListStateCheck("OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList", ['white (2649 pixels, meshable)'])
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 2649)
findWidget('OOF2 Messages 1').resize(410, 130)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.0000000000000e+00)
findWidget('Microstructure').resize(500, 362)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 0)
event(Gdk.EventType.BUTTON_PRESS,x= 9.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Burn']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 28.00475, 51.5515, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 28.00475, 51.5515, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 1259)
findGfxWindow('Graphics_1').simulateMouse('down', 79.60175, 61.425, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.60175, 61.425, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.92025, 61.425, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.23875, 61.1065, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 80.23875, 61.1065, 1, True, False)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 2670)
findGfxWindow('Graphics_1').simulateMouse('down', 82.78675, 24.7975, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 82.78675, 24.7975, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 3717)
findWidget('Microstructure:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 0)
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Image']).activate() # MenuItemLogger
checkpoint page installed Image
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Image Page:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy Image
findWidget('Dialog-Copy Image').resize(317, 134)
findWidget('Dialog-Copy Image:widget_GTK_RESPONSE_OK').clicked()
checkpoint microstructure page sensitized
checkpoint OOF.Image.Copy
findWidget('Microstructure:Next').clicked()
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(229, 193)
event(Gdk.EventType.BUTTON_PRESS,x= 7.8000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:what:Image').get_window())
checkpoint toplevel widget mapped chooserPopup-Image
findMenu(findWidget('chooserPopup-Image'), ['K1_small.pgm<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Image') # MenuItemLogger
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
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.6221461632542e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.0000000000000e+02,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Image').get_window())
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
event(Gdk.EventType.BUTTON_PRESS,x= 4.1700000000000e+02,y= 6.0000000000000e+00,button=3,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
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
event(Gdk.EventType.BUTTON_PRESS,x= 1.1300000000000e+02,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Color']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 7.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry').set_text('0.')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry').set_text('0.0')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry').set_text('0.05')
findGfxWindow('Graphics_1').simulateMouse('down', 76.73525, 62.3805, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 76.73525, 62.3805, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
widget_1=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Color:range:DeltaGray:delta_gray:entry')
if widget_1: wevent(widget_1, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_1.get_window())
del widget_1
 checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Color
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 4341)
event(Gdk.EventType.BUTTON_PRESS,x= 1.6100000000000e+02,y= 3.2000000000000e+01,button=3,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
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
event(Gdk.EventType.BUTTON_RELEASE,x= 6.0000000000000e+01,y= 2.3000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Color
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 4843)
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 8.1000000000000e+01,y= 2.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pixel Selection']).activate() # MenuItemLogger
checkpoint page installed Pixel Selection
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint pixel page updated
findWidget('OOF2:Pixel Selection Page:Pane').set_position(273)
checkpoint pixel page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 8.6000000000000e+01,y= 2.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Select_Group
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 2649)
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.3600000000000e+02,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
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
assert tests.pixelSelectionTBSizeCheck('OOF2 Graphics 1', 5723)
findWidget('Microstructure:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.0100000000000e+02,y= 2.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
checkpoint page installed Microstructure
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
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
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
assert tests.treeViewColCheck("OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList", 0, ['black (0 pixels, meshable)', 'white (2649 pixels, meshable)'])
findWidget('Microstructure:Next').clicked()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
assert tests.treeViewColCheck("OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList", 0, ['black (5723 pixels, meshable)', 'white (2649 pixels, meshable)'])
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
findWidget('Dialog-Microstructure:filename').set_text('microstructure.d')
findWidget('Dialog-Microstructure:filename').set_text('microstructure.da')
findWidget('Dialog-Microstructure:filename').set_text('microstructure.dat')
findWidget('Dialog-Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Microstructure
assert tests.filediff('microstructure.dat')
findWidget('Microstructure:Next').clicked()
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
assert tests.filediff('session.log')
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
