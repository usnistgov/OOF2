# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Element mode test in the Skeleton Selection toolbox

import tests
tbox="OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection"
elbox=tbox+":Element"
ndbox=tbox+":Node"
sgbox=tbox+":Segment"

checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2').resize(782, 545)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
wevent(findWidget('Dialog-New_Layer_Policy:policy'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.New_Layer_Policy
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(265)
# Graphics window up and toolbox selected.  Check displays.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'', 'ydown':'', 'xup':'', 'yup':''}, elbox)
assert tests.sensitizationCheck({'Undo':False,'Redo':False,'Clear':False,'Invert':False},elbox)
assert tests.sensitizationCheck({'Prev':False,'Repeat':False,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","No Skeleton!")

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
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
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
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
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
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
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
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
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
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
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

# Skeleton loaded up, recheck displays.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'', 'ydown':'', 'xup':'', 'yup':''}, elbox)
assert tests.sensitizationCheck({'Undo':False,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':False,'Repeat':False,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","0 (0%)")

# Single element selection.
findGfxWindow('Graphics_1').simulateMouse('down', 21.125, 59.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 21.125, 59.1, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Single_Element
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'21.125', 'yup':'59.1'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':False,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","1 (1.5625%)")

# Select a rectangle of elements
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.4000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 9.925, 78.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.925, 78.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.275, 78.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.275, 78, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 12.375, 75.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 14.475, 73.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 17.275, 69.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 20.075, 66.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 23.575, 62.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 27.775, 58.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 31.975, 55.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 38.275, 52.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 44.925, 49.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 51.575, 46.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.225, 44.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 67.675, 41.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 74.675, 38.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.975, 37.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.125, 36.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.525, 36, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.875, 36, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.875, 36, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.525, 36, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.475, 35.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.125, 35.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.125, 35.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.775, 34.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.075, 34.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.725, 34.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.725, 34.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.375, 34.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.025, 33.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.025, 33.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 82.025, 33.9, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated Element
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Rectangle
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'9.925', 'ydown':'78.35', 'xup':'82.025', 'yup':'33.9'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","15 (23.4375%)")

# Select a circle of elements
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('up', 25.675, 75.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('down', 25.325, 77.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.325, 77.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.325, 76.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.325, 76.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.325, 76.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.325, 75.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.325, 75.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.325, 74.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.325, 74.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.325, 73.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.325, 73.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.675, 72.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.675, 71.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.675, 71, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 25.675, 70.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.025, 69.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.025, 68.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.025, 67.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.025, 67.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.025, 66.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.375, 65.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.375, 64, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.725, 63.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.725, 62.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.725, 61.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.725, 61.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 27.075, 61.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 27.075, 60.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 27.425, 59.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 27.775, 59.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 27.775, 59.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 27.775, 59.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.125, 59.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.125, 58.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.125, 58.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.475, 58.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.475, 58.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.475, 58.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.825, 58.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.825, 58.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.825, 58.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 29.175, 58.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 29.175, 58.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 29.175, 58.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 29.525, 57.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 29.525, 57.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 29.875, 57.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 29.875, 57.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 29.875, 57.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 29.875, 57.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 30.225, 57.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 30.225, 57, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 30.225, 57, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 30.225, 57, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 30.225, 57, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 30.575, 56.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 30.575, 56.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 30.575, 56.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 30.575, 56.65, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Circle
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'25.325', 'ydown':'77.3', 'xup':'30.575', 'yup':'56.65'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","4 (6.25%)")

# Select an ellipse
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Ellipse']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 16.925, 57, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 16.925, 57, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 17.625, 56.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 20.775, 55.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 30.575, 53.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.425, 51.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 45.275, 49.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 46.675, 48.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 49.125, 46.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.275, 44.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 57.175, 41.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 64.875, 35.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 70.825, 29.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 72.925, 26.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 76.075, 25.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.225, 23.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.625, 22.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.725, 20.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.775, 19.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.775, 19.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.775, 19.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.125, 19.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.825, 19.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.575, 18.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.275, 17.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 16.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.975, 16.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.325, 16.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.325, 16.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.325, 15.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.325, 15.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.325, 15.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.675, 15.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.675, 15.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.675, 15.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.025, 15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.025, 15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.375, 14.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.375, 14.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.375, 14.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.725, 14.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.725, 13.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 90.425, 13.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 90.425, 13.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 90.775, 13.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 90.775, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 90.775, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 90.775, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 91.125, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 91.125, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 91.125, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 91.475, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 91.475, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 92.175, 12.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 92.175, 12.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 92.525, 12.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 92.525, 12.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 92.525, 12.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.225, 12.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 95.325, 12.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 95.325, 12.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 95.325, 12.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 95.325, 12.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 95.325, 11.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 94.975, 11.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 94.625, 11.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 94.275, 11.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 94.275, 11.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 94.275, 11.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 94.275, 11.85, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Ellipse
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'16.925', 'ydown':'57', 'xup':'94.275', 'yup':'11.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","8 (12.5%)")

# Select by dominant pixel
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['ByDominantPixel']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 49.475, 67.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 49.475, 67.85, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.ByDominantPixel
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'49.475', 'yup':'67.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)

# Clear the selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Clear').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Clear
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'49.475', 'yup':'67.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","0 (0%)")

# Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Undo').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Undo
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'49.475', 'yup':'67.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","18 (28.125%)")

# Undo again
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Undo').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Undo
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'49.475', 'yup':'67.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","8 (12.5%)")

# Redo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Redo').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Redo
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'49.475', 'yup':'67.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","18 (28.125%)")

# Invert
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Invert').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Invert
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'49.475', 'yup':'67.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","46 (71.875%)")

# Clear
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Clear').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Clear
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'49.475', 'yup':'67.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","0 (0%)")

# History previous
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Prev').clicked()
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'16.925', 'ydown':'57', 'xup':'94.275', 'yup':'11.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':True},elbox)
assert tests.gtkTextCompare(elbox+":size","0 (0%)")

# Previous again
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Prev').clicked()
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'25.325', 'ydown':'77.3', 'xup':'30.575', 'yup':'56.65'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':True},elbox)
assert tests.gtkTextCompare(elbox+":size","0 (0%)")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Prev').clicked()
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'9.925', 'ydown':'78.35', 'xup':'82.025', 'yup':'33.9'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':True},elbox)
assert tests.gtkTextCompare(elbox+":size","0 (0%)")

# Repeat rectangle selection from history gizmo
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Repeat'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Repeat').clicked()
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Rectangle
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2').resize(782, 545)
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'9.925', 'ydown':'78.35', 'xup':'82.025', 'yup':'33.9'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","15 (23.4375%)")

# Previous again.

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Prev').clicked()
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'49.475', 'yup':'67.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':True},elbox)
assert tests.gtkTextCompare(elbox+":size","15 (23.4375%)")

# Previous some more.

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Prev').clicked()
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'16.925', 'ydown':'57', 'xup':'94.275', 'yup':'11.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':True},elbox)

# Next!
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Next').clicked()
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'49.475', 'yup':'67.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':True},elbox)
assert tests.gtkTextCompare(elbox+":size","15 (23.4375%)")

# Repeat dominant pixel selection
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Repeat'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Repeat').get_window())
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Repeat').clicked()
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.ByDominantPixel
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'49.475', 'yup':'67.85'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","18 (28.125%)")

# Remove Skeleton display layer
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.0000000000000e+00)
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=3, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
checkpoint toplevel widget mapped PopUp-0
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
checkpoint OOF.Graphics_1.Layer.Select
findMenu(findWidget('PopUp-0'), ['Delete']).activate() # MenuItemLogger
deactivatePopup('PopUp-0') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Delete
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'49.475', 'yup':'67.85'}, elbox)
assert tests.sensitizationCheck({'Undo':False,'Redo':False,'Clear':False,'Invert':False},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","No Skeleton!")

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
checkpoint OOF.Graphics_1.File.Close
