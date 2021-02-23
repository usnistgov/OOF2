# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Node mode test in the Skeleton Selection toolbox

import tests
tbox="OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection"
elbox=tbox+":Element"
ndbox=tbox+":Node"
sgbox=tbox+":Segment"

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)
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
findWidget('OOF2').resize(782, 545)
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('e')
findWidget('Dialog-Data:filename').set_text('ex')
findWidget('Dialog-Data:filename').set_text('exa')
findWidget('Dialog-Data:filename').set_text('exam')
findWidget('Dialog-Data:filename').set_text('examp')
findWidget('Dialog-Data:filename').set_text('exampl')
findWidget('Dialog-Data:filename').set_text('example')
findWidget('Dialog-Data:filename').set_text('examples')
findWidget('Dialog-Data:filename').set_text('examples/')
findWidget('Dialog-Data:filename').set_text('examples/t')
findWidget('Dialog-Data:filename').set_text('examples/tr')
findWidget('Dialog-Data:filename').set_text('examples/tri')
findWidget('Dialog-Data:filename').set_text('examples/tria')
findWidget('Dialog-Data:filename').set_text('examples/trian')
findWidget('Dialog-Data:filename').set_text('examples/triang')
findWidget('Dialog-Data:filename').set_text('examples/triangl')
findWidget('Dialog-Data:filename').set_text('examples/triangle')
findWidget('Dialog-Data:filename').set_text('examples/triangle.')
findWidget('Dialog-Data:filename').set_text('examples/triangle.s')
findWidget('Dialog-Data:filename').set_text('examples/triangle.sk')
findWidget('Dialog-Data:filename').set_text('examples/triangle.ske')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skel')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skele')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skelet')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skeleto')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skeleton')
findWidget('Dialog-Data:widget_GTK_RESPONSE_OK').clicked()
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
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint OOF.File.Load.Data

wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(265)
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
# Switch to node mode
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Node').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'', 'ydown':'', 'xup':'', 'yup':''}, ndbox)
assert tests.sensitizationCheck({'Undo':False,'Redo':False,'Clear':False,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':False,'Repeat':False,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","0 (0%)")

# Select a single node
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('down', 11.675, 88.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 11.675, 88.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 11.675, 88.5, 1, False, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'11.675', 'yup':'88.5'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':False,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","1 (1.33333%)")

# Select a rectangle of nodes
findWidget('OOF2 Graphics 1').resize(800, 492)
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findWidget('chooserPopup-TBChooser').deactivate() # MenuLogger
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.4000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 7.825, 68.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.825, 68.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.825, 68.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.825, 67.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.825, 65.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.825, 62.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.825, 58.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.825, 54.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.825, 51.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.825, 47.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.825, 45.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.825, 43.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.175, 41.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.525, 40.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.225, 39.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.975, 37.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 12.725, 36.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 15.875, 35.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 19.375, 33.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 23.925, 32.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 31.975, 31.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.825, 30.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 49.475, 29, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 53.325, 27.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.825, 26.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 63.475, 25.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.525, 24.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 76.075, 24.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.475, 24.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78.525, 24.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.275, 24.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.425, 24.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 24.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.275, 24.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 24.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 24.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 24.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 25.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 25.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 25.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 25.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 25.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 26.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 26.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 26.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 27.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 27.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 27.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 28.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 28.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.975, 28.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.975, 28.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.975, 28.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.975, 28.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.975, 28.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.975, 28.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.975, 26.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.975, 24.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 22.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.275, 21.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 20.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 20.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 19.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 18.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.575, 18.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.575, 18.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.575, 18.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.575, 18.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.575, 18.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.575, 18.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 18.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 19.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 19.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 19.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 19.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 19.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 19.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 19.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 20.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.275, 20.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.275, 20.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.275, 20.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.275, 20.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.275, 20.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.275, 20.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 87.275, 20.95, 1, False, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Rectangle
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'7.825', 'ydown':'68.2', 'xup':'87.275', 'yup':'20.95'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","21 (28%)")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 1.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 1.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
# Select a circle
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.4000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 44.225, 56.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 44.225, 56.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.175, 56.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.475, 56.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.425, 56.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 40.025, 55.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 38.275, 55.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 36.875, 55.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 34.425, 55.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 31.625, 54.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 29.175, 54.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 27.775, 53.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.675, 53.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 24.275, 53.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 23.575, 53.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 22.875, 52.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 22.525, 52.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 21.825, 52.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 21.475, 52.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 21.125, 52.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 21.125, 52.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 20.775, 52.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 20.775, 52.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 20.425, 51.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 20.075, 51.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 20.075, 51.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 20.075, 51.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 19.725, 51.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 19.025, 51.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 18.675, 51.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 18.325, 51.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 18.325, 51.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 17.975, 51.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 17.975, 51.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 17.975, 51.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 17.975, 51.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 17.975, 51.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 17.975, 51.05, 1, False, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Circle
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'44.225', 'ydown':'56.65', 'xup':'17.975', 'yup':'51.05'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","12 (16%)")

# Select an ellipse
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Ellipse']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('down', 2.575, 85.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.575, 85.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.925, 84.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.975, 82.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 6.775, 80.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 11.675, 75.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 15.875, 71.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 19.725, 67.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 27.075, 62.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 34.075, 60.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 40.025, 58.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 45.975, 57.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.875, 56.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.775, 55.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 59.975, 54.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 66.625, 53.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 72.925, 52.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78.525, 51.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.025, 51.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.825, 50.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.275, 50, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 90.775, 48.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.575, 48.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 48.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 47.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 47.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 47.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 46.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 94.275, 45.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 94.275, 44.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 94.275, 43.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 94.275, 43.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 42.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 41.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 40.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 40.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 40.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 40.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 40.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 41.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 41.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.925, 41.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 93.925, 41.25, 1, False, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Ellipse
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'2.575', 'ydown':'85.35', 'xup':'93.925', 'yup':'41.25'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","15 (20%)")

# Clear the selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Clear').clicked()
checkpoint selection info updated Node
checkpoint Graphics_1 Node sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Clear
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'2.575', 'ydown':'85.35', 'xup':'93.925', 'yup':'41.25'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","0 (0%)")

# Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Undo').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Undo
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'2.575', 'ydown':'85.35', 'xup':'93.925', 'yup':'41.25'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","15 (20%)")

# Undo again
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Undo').clicked()
checkpoint selection info updated Node
checkpoint Graphics_1 Node sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Undo
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'2.575', 'ydown':'85.35', 'xup':'93.925', 'yup':'41.25'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","12 (16%)")

# Redo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Redo').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Redo
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'2.575', 'ydown':'85.35', 'xup':'93.925', 'yup':'41.25'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","15 (20%)")

# Invert
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Invert').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Invert
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'2.575', 'ydown':'85.35', 'xup':'93.925', 'yup':'41.25'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","60 (80%)")

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
