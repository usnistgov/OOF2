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
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
findWidget('OOF2').resize(782, 545)
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
wevent(findWidget('Dialog-New_Layer_Policy:policy'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.New_Layer_Policy
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Move Nodes']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Move Nodes sensitized
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(240)
assert tests.sensitivityCheck0()
assert tests.textCompare('---', '---', '---', '---')
assert tests.mouseMode()

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
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
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
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
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
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
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
assert tests.sensitivityCheck0()
assert tests.textCompare('---', '---', '---', '---')
assert tests.mouseMode()

# Move node with mouse
findGfxWindow('Graphics_1').simulateMouse('down', 87.45, 88.15, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox node changed
checkpoint Move Node toolbox down event
assert tests.floatCompare(87.45, 88.15, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 87.45, 88.15, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
## TODO: Why with no motion yet has the shape energy changed?
assert tests.floatCompare(87.45, 88.15, 0.01088, 0) # ????
findGfxWindow('Graphics_1').simulateMouse('move', 87.45, 87.8, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.floatCompare(87.45, 87.8, 0.002368, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 87.8, 87.1, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 88.15, 86.75, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 88.85, 86.05, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 88.85, 85.7, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 89.2, 85.7, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 89.2, 85.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 89.2, 85.35, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 89.2, 85.35, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 89.2, 85.35, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 89.2, 85.35, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 89.9, 84.65, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 89.9, 83.95, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 90.25, 83.95, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 90.25, 83.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 90.25, 83.6, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 90.25, 83.6, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 90.25, 83.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 90.6, 83.6, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 90.6, 83.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 90.6, 83.6, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
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
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode
checkpoint Move Node toolbox up event
assert tests.floatCompare(90.6, 83.6, 0.6327, 0)
assert tests.sensitivityCheck1()

# Another mouse move
findGfxWindow('Graphics_1').simulateMouse('down', 74.5, 88.85, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox node changed
checkpoint Move Node toolbox down event
assert tests.floatCompare(74.5, 88.85, 0, 0)
findGfxWindow('Graphics_1').simulateMouse('move', 74.5, 88.5, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.floatCompare(74.5, 88.5, 0.005999, 0.001435)
findGfxWindow('Graphics_1').simulateMouse('move', 74.5, 88.5, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 74.85, 87.45, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 74.85, 87.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 74.85, 86.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 74.85, 86.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 74.85, 85.7, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 74.85, 85.7, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 74.85, 85.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 75.2, 85.7, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 75.55, 85.35, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 75.55, 85, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 76.25, 85, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 76.6, 85, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 76.6, 85, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 76.95, 84.65, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 76.95, 84.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 76.95, 84.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 76.95, 83.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 76.95, 83.6, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 77.3, 83.6, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 77.3, 83.25, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 77.65, 83.25, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 77.65, 83.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.65, 83.25, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 77.65, 83.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.65, 83.25, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 77.65, 83.25, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 77.65, 83.25, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 77.65, 83.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78, 82.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78, 82.9, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 78, 82.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78, 82.55, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 78, 82.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78, 82.55, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 78, 82.55, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 78, 82.55, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 78.35, 82.2, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 78.35, 82.2, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 78.35, 82.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 78.35, 82.2, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
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
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode
checkpoint Move Node toolbox up event
assert tests.sensitivityCheck1()
assert tests.floatCompare(78.35, 82.2, 0.3644, -0.007744)

# Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Undo').clicked()
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
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Undo
assert tests.sensitivityCheck2()

# Undo again
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Undo').clicked()
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
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Undo
assert tests.sensitivityCheck3()

# Redo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Redo').clicked()
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
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Redo
assert tests.sensitivityCheck2()

# Redo again
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Redo').clicked()
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
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Redo
assert tests.sensitivityCheck1()

# Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Undo').clicked()
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
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Undo
assert tests.sensitivityCheck2()

# Undo again
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Undo').clicked()
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
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Undo
assert tests.sensitivityCheck3()

# Switch to keyboard mode
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:MoveWith:Keyboard').clicked()
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
assert tests.keyboardMode()
assert tests.sensitivityCheck3()

# Click on a node
findGfxWindow('Graphics_1').simulateMouse('down', 13.25, 12.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 13.25, 12.2, 1, False, False)
checkpoint contourmap info updated for Graphics_1
checkpoint Move Node toolbox node changed
checkpoint Graphics_1 Move Nodes sensitized
checkpoint OOF.Graphics_1.Toolbox.Move_Nodes.SelectNode
checkpoint Move Node toolbox up event
assert tests.sensitivityCheck4()
assert tests.floatCompare(12.5, 12.5, 0.3644, -0.007744)

# Edit the position
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:x').set_text('2.5')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:x').set_text('.5')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:x').set_text('1.5')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:x').set_text('15.5')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Move').clicked()
checkpoint Move Node toolbox info updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
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
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode
assert tests.sensitivityCheck5()
assert tests.floatCompare(15.5, 12.5, 0.2238, 0)

# Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Undo').clicked()
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
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Undo
assert tests.sensitivityCheck4()

# Select a different node
findGfxWindow('Graphics_1').simulateMouse('up', 12.2, 25.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('down', 12.2, 25.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 12.2, 25.5, 1, False, False)
checkpoint contourmap info updated for Graphics_1
checkpoint Move Node toolbox node changed
checkpoint Graphics_1 Move Nodes sensitized
checkpoint OOF.Graphics_1.Toolbox.Move_Nodes.SelectNode
checkpoint Move Node toolbox up event

# Edit its y position
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:y').set_text('')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:y').set_text('3')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:y').set_text('30')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Move').clicked()
checkpoint Move Node toolbox info updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
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
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode
assert tests.sensitivityCheck5()
assert tests.floatCompare(12.5, 30, 0.4065, 0.193)

# Try an illegal move
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:y').set_text('300')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:y').set_text('3000')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Move').clicked()
checkpoint Move Node toolbox info updated
assert tests.sensitivityCheck5()
assert tests.xyshCompare(12.5, 30, '---', '---')
assert tests.nIllegalElements() == 0

# Allow an illegal move
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:AllowIllegal').clicked()
checkpoint OOF.Graphics_1.Toolbox.Move_Nodes.AllowIllegal
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:y').set_text('0')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:y').set_text('60')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Move').clicked()
checkpoint Move Node toolbox info updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
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
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode
assert tests.sensitivityCheck5()
assert tests.xyshCompare(12.5, 60, '---', '---')
assert tests.messageCompare("2 illegal elements in the skeleton.\n")
assert tests.nIllegalElements() == 2

# Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Undo').clicked()
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
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Undo
assert tests.nIllegalElements() == 0
assert tests.sensitivityCheck6()

# Switch back to Mouse mode

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:MoveWith:Mouse').clicked()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
assert tests.textCompare('---', '---', '---', '---')
assert tests.sensitivityCheck2()

# Make an illegal move
findGfxWindow('Graphics_1').simulateMouse('down', 12.2, 88.15, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox node changed
checkpoint Move Node toolbox down event
assert tests.messageCompare("")
findGfxWindow('Graphics_1').simulateMouse('move', 12.2, 88.15, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 12.2, 88.15, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 12.55, 88.15, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 15.7, 86.05, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 18.15, 83.95, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("")
findGfxWindow('Graphics_1').simulateMouse('move', 20.95, 79.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 21.65, 77.65, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("Illegal node position!")
findGfxWindow('Graphics_1').simulateMouse('move', 21.65, 76.6, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("Illegal node position!")
findGfxWindow('Graphics_1').simulateMouse('move', 22, 75.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 22, 75.55, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("Illegal node position!")
findGfxWindow('Graphics_1').simulateMouse('move', 22, 74.85, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 22, 74.15, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 22.35, 72.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 22.35, 72.05, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 22.35, 71.7, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("Illegal node position!")
findGfxWindow('Graphics_1').simulateMouse('move', 22.35, 71, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 22.35, 70.65, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 22.35, 70.65, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 22.35, 69.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 22.7, 69.6, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 22.7, 69.25, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 22.7, 68.9, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 22.7, 68.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 22.7, 68.9, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 22.7, 68.9, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("Illegal node position!")
findGfxWindow('Graphics_1').simulateMouse('move', 22.7, 68.9, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('up', 22.7, 68.9, 1, False, False)
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
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
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode
checkpoint Move Node toolbox up event
assert tests.xyshCompare(22.7, 68.9, '---', '---')

assert tests.messageCompare("2 illegal elements in the skeleton.\n")
assert tests.sensitivityCheck1()

# Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:Undo').clicked()
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
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Undo
assert tests.xyshCompare(22.7, 68.9, '---', '---')

# Make a forbidden illegal move with the mouse
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Move Nodes:AllowIllegal').clicked()
checkpoint OOF.Graphics_1.Toolbox.Move_Nodes.AllowIllegal
findGfxWindow('Graphics_1').simulateMouse('down', 61.55, 21.65, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox node changed
checkpoint Move Node toolbox down event
findGfxWindow('Graphics_1').simulateMouse('move', 61.55, 21.65, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 61.55, 21.65, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 61.55, 21.3, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("")
findGfxWindow('Graphics_1').simulateMouse('move', 60.15, 20.95, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 59.45, 20.6, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 57.7, 19.9, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 56.65, 19.55, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("")
findGfxWindow('Graphics_1').simulateMouse('move', 54.55, 18.5, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("Illegal node position!")
findGfxWindow('Graphics_1').simulateMouse('move', 51.05, 17.1, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("Illegal node position!")
findGfxWindow('Graphics_1').simulateMouse('move', 49.65, 16.4, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("Illegal node position!")
findGfxWindow('Graphics_1').simulateMouse('move', 47.55, 15, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 45.8, 13.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.65, 11.15, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("Illegal node position!")
findGfxWindow('Graphics_1').simulateMouse('move', 39.85, 7.3, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 39.15, 5.2, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 38.8, 3.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 38.8, 3.8, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 38.8, 3.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 38.45, 3.45, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 38.45, 3.45, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 38.45, 3.45, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 38.45, 3.45, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 38.45, 3.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 38.45, 3.1, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 38.45, 3.1, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 38.45, 3.1, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 38.1, 3.1, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 38.1, 3.1, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 38.1, 3.1, 1, False, False)
checkpoint Move Node toolbox info updated
checkpoint Move Node toolbox move event
assert tests.messageCompare("Illegal node position!")
findGfxWindow('Graphics_1').simulateMouse('up', 38.1, 3.1, 1, False, False)
checkpoint Move Node toolbox up event
# Displayed x and y snap back to original values when forbidden move
# is finished.
assert tests.xyshCompare(62.5, 21, '---', '---')

# Delete the skeleton display layer
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.0000000000000e+00)
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=3, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
checkpoint toplevel widget mapped PopUp-0
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
checkpoint OOF.Graphics_1.Layer.Select
findMenu(findWidget('PopUp-0'), ['Delete']).activate() # MenuItemLogger
deactivatePopup('PopUp-0') # MenuItemLogger
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
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Delete
assert tests.sensitivityCheck0()
assert tests.textCompare('---', '---', '---', '---')
assert tests.messageCompare("")

findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 1.0000000000000e+00)
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

findWidget('OOF2:Introduction Page:Scroll').get_vadjustment().set_value( 0.0000000000000e+00)
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
