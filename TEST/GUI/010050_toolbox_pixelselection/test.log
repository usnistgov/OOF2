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
event(Gdk.EventType.BUTTON_PRESS,x= 2.9000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.New_Layer_Policy
findWidget('OOF2 Graphics 1').resize(800, 492)
# Go to the pixel selection toolbox
event(Gdk.EventType.BUTTON_PRESS,x= 9.1000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','No source!')
assert tests.sensitizationCheck({'Undo':False,'Redo':False,'Clear':False,'Invert':False,'Prev':False,'Repeat':False,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Create a Microstructure from an Image
event(Gdk.EventType.BUTTON_PRESS,x= 9.7000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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

# Check selection size
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','0 (0%)')
assert tests.sensitizationCheck({'Undo':False,'Redo':False,'Clear':False,'Invert':True,'Prev':False,'Repeat':False,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Click to select a pixel
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('down', 66.3375, 90.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 66.3375, 90.75, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','1 (0.00444444%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':False,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'--','ydown':'--','xup':'66.3375','yup':'90.75'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Select a different pixel
findGfxWindow('Graphics_1').simulateMouse('down', 133.5375, 12.525, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 133.5375, 12.525, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','1 (0.00444444%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'--','ydown':'--','xup':'133.537','yup':'12.525'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Shift-click to select an additional pixel
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('down', 50.5875, 114.9, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.5875, 114.9, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 50.5875, 114.9, 1, True, False)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','2 (0.00888889%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'--','ydown':'--','xup':'50.5875','yup':'114.9'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Brush selection
event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Brush']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','2 (0.00888889%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':False,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'--','ydown':'--','xup':'50.5875','yup':'114.9'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Set radius
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Circle:radius').set_text('')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Circle:radius').set_text('2')
# Make a squiggle
findGfxWindow('Graphics_1').simulateMouse('down', 53.7375, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 53.7375, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 54.7875, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.4625, 78.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 70.0125, 76.575, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.7625, 73.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 99.9375, 72.375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 112.5375, 70.275, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 117.2625, 69.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 117.2625, 69.225, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 117.2625, 69.225, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 117.7875, 69.225, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 117.7875, 69.225, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 117.7875, 68.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 117.7875, 68.7, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Brush
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','272 (1.20889%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'53.7375','ydown':'78.675','xup':'117.787','yup':'68.7'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Switch to square brush
event(Gdk.EventType.BUTTON_PRESS,x= 1.2800000000000e+02,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Square']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Square:size').set_text('')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Square:size').set_text('2')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Square:size').set_text('2.')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Brush:style:Square:size').set_text('2.0')
# Select some pixels
findGfxWindow('Graphics_1').simulateMouse('down', 41.1375, 71.325, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.1375, 71.325, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.1375, 70.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.1375, 69.225, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.1375, 66.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.1375, 63.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.6625, 59.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.2375, 56.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.4375, 54, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.1625, 52.425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.8375, 52.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.9875, 55.575, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 61.6125, 57.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 64.2375, 58.725, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 67.9125, 60.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 70.5375, 60.825, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.5875, 60.825, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 72.1125, 59.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 73.6875, 56.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 75.2625, 51.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 76.8375, 48.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.9875, 44.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.6125, 42.975, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.8625, 42.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 90.4875, 42.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.1125, 43.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 95.2125, 44.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 96.7875, 45.075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 97.8375, 46.125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 98.3625, 46.125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 98.3625, 46.125, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Brush
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 6.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.4000000000000e+01)
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','419 (1.86222%)')

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'41.1375','ydown':'71.325','xup':'98.3625','yup':'46.125'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Select a rectangle
event(Gdk.EventType.BUTTON_PRESS,x= 7.3000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('down', 41.1375, 101.775, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.1375, 101.775, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.1375, 101.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.7125, 99.675, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 46.9125, 97.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.3125, 92.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 66.3375, 87.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 74.7375, 83.925, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.0875, 80.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.3375, 78.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.1125, 75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 99.4125, 71.325, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 103.0875, 69.225, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 106.7625, 66.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 107.8125, 66.075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 108.3375, 65.025, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 109.3875, 63.975, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.4375, 62.925, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.9625, 62.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 112.5375, 61.875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 113.5875, 60.825, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 114.6375, 60.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 115.6875, 59.775, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 115.6875, 59.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 115.6875, 59.25, 1, False, False)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','3225 (14.3333%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'41.1375','ydown':'101.775','xup':'115.688','yup':'59.25'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Select a circle
event(Gdk.EventType.BUTTON_PRESS,x= 1.3400000000000e+02,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('down', 25.9125, 67.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.9125, 67.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.9125, 66.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.9625, 65.025, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.0125, 62.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 29.0625, 59.775, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 30.6375, 57.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 32.2125, 55.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 33.7875, 52.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 34.3125, 51.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 35.3625, 49.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 36.4125, 48.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 37.4625, 46.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 37.9875, 45.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 38.5125, 45.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 38.5125, 45.075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 39.0375, 44.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 39.5625, 44.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 39.5625, 44.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 39.5625, 44.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 39.5625, 44.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 39.5625, 44.55, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','2250 (10%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'25.9125','ydown':'67.65','xup':'39.5625','yup':'44.55'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Select an ellipse
event(Gdk.EventType.BUTTON_PRESS,x= 1.3600000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Ellipse']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 76.3125, 110.175, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 76.3125, 109.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 76.3125, 109.125, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.8875, 107.025, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.4625, 104.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 81.5625, 101.775, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.1875, 99.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.3375, 96, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 91.0125, 93.375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 95.2125, 91.275, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 102.0375, 89.175, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 106.2375, 87.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 108.3375, 87.075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.4375, 86.025, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 114.1125, 84.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 120.4125, 82.875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 124.6125, 80.775, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 128.2875, 79.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 131.9625, 78.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 134.5875, 77.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 136.1625, 76.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 138.7875, 74.475, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 140.8875, 72.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 142.9875, 71.325, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 143.5125, 70.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 143.5125, 70.8, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Ellipse
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','2085 (9.26667%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'76.3125','ydown':'110.175','xup':'143.512','yup':'70.8'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Select by color
event(Gdk.EventType.BUTTON_PRESS,x= 1.3500000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Color']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 45.3375, 84.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 45.3375, 84.45, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Color
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','4795 (21.3111%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'--','ydown':'--','xup':'45.3375','yup':'84.45'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Select by burning
event(Gdk.EventType.BUTTON_PRESS,x= 5.9000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findWidget('chooserPopup-TBChooser').deactivate() # MenuLogger
event(Gdk.EventType.BUTTON_PRESS,x= 9.1000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Burn']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 82.6125, 44.025, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 82.6125, 44.025, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','4781 (21.2489%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'--','ydown':'--','xup':'82.6125','yup':'44.025'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Undo
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','4795 (21.3111%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'--','ydown':'--','xup':'82.6125','yup':'44.025'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Undo again
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Undo
# Back to the ellipse selection
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','2085 (9.26667%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'--','ydown':'--','xup':'82.6125','yup':'44.025'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Clear
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','0 (0%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'--','ydown':'--','xup':'82.6125','yup':'44.025'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Mouse up coords are the same as the last click (burn)
# Redo the burn so that we can get nontrivial intersections for
# control clicks, etc. later
findGfxWindow('Graphics_1').simulateMouse('down', 91.0125, 45.075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 91.0125, 45.075, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','4781 (21.2489%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Circle mode
event(Gdk.EventType.BUTTON_PRESS,x= 1.1400000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.6000000000000e+01)

# Circle selection with the shift key depressed
findGfxWindow('Graphics_1').simulateMouse('down', 89.9625, 99.15, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.9625, 99.15, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 91.0125, 97.575, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.6375, 95.475, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 95.7375, 92.325, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 97.3125, 89.7, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 98.3625, 88.125, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 98.8875, 87.075, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 99.4125, 86.55, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 99.4125, 85.5, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 99.9375, 84.975, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 100.4625, 84.45, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 100.9875, 83.925, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 101.5125, 82.35, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 102.0375, 81.825, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 102.5625, 81.3, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 102.5625, 80.775, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 103.0875, 80.25, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 103.0875, 80.25, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 103.0875, 80.25, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 103.6125, 80.25, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 103.6125, 79.725, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 104.1375, 79.725, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 104.1375, 80.25, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 104.1375, 80.25, 1, True, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','5919 (26.3067%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'89.9625','ydown':'99.15','xup':'104.138','yup':'80.25'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# control-click the circle selection
findGfxWindow('Graphics_1').simulateMouse('down', 88.9125, 48.225, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 88.9125, 48.225, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 89.4375, 47.175, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 90.4875, 45.6, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 91.0125, 44.025, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 91.5375, 41.4, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 92.0625, 40.35, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 92.0625, 39.825, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 92.5875, 39.825, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 92.5875, 39.3, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 93.1125, 38.25, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 93.6375, 37.725, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 94.1625, 37.2, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 94.6875, 36.15, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 95.2125, 35.1, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 95.7375, 34.575, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 96.7875, 33, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 97.3125, 32.475, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 97.8375, 31.425, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 98.3625, 31.425, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 98.8875, 30.9, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 99.4125, 30.375, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 99.9375, 29.85, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 100.4625, 29.325, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 100.4625, 29.325, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 100.9875, 28.8, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 100.9875, 28.8, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 100.9875, 28.8, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 100.9875, 28.8, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 101.5125, 28.275, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 101.5125, 28.275, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 101.5125, 28.275, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 102.0375, 28.8, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 102.0375, 28.8, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 102.0375, 29.325, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 102.0375, 29.325, 1, False, True)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','6009 (26.7067%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'88.9125','ydown':'48.225','xup':'102.037','yup':'29.325'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Make the toolbox wider
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(261)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(269)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(270)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(285)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 1.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(287)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 8.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(301)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(341)

# Clear the selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','0 (0%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'88.9125','ydown':'48.225','xup':'102.037','yup':'29.325'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Repeat button (repeats the circle selection)
event(Gdk.EventType.BUTTON_RELEASE,x= 4.9000000000000e+01,y= 1.7000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','1668 (7.41333%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'88.9125','ydown':'48.225','xup':'102.037','yup':'29.325'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Choose the previous operation
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Prev').clicked()
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','1668 (7.41333%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':True}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'88.9125','ydown':'48.225','xup':'102.037','yup':'29.325'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# previous again
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Prev').clicked()
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','1668 (7.41333%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':True}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'89.9625','ydown':'99.15','xup':'104.138','yup':'80.25'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# repeat the operation
event(Gdk.EventType.BUTTON_RELEASE,x= 4.7000000000000e+01,y= 1.7000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','1758 (7.81333%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
# Same as 1st circle selection after burn
assert tests.gtkMultiTextCompare({'xdown':'89.9625','ydown':'99.15','xup':'104.138','yup':'80.25'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# previous again
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Prev').clicked()
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':True}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'88.9125','ydown':'48.225','xup':'102.037','yup':'29.325'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Next
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Next').clicked()
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'89.9625','ydown':'99.15','xup':'104.138','yup':'80.25'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Repeat.  This is the second circle selection after the burn
event(Gdk.EventType.BUTTON_RELEASE,x= 4.7000000000000e+01,y= 1.8000000000000e+01,button=1,state=256,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','1758 (7.81333%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'89.9625','ydown':'99.15','xup':'104.138','yup':'80.25'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Clear
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','0 (0%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'89.9625','ydown':'99.15','xup':'104.138','yup':'80.25'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Undo
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','1758 (7.81333%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'89.9625','ydown':'99.15','xup':'104.138','yup':'80.25'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Undo undone. (2x undo.  This is not the redo test.)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Undo
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','1758 (7.81333%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'89.9625','ydown':'99.15','xup':'104.138','yup':'80.25'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Redo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Redo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Redo
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','1758 (7.81333%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'89.9625','ydown':'99.15','xup':'104.138','yup':'80.25'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

# Invert
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Invert').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint pixel page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Invert
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','20742 (92.1867%)')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'89.9625','ydown':'99.15','xup':'104.138','yup':'80.25'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')

findWidget('OOF2 Graphics 1').resize(800, 492)
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

findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
