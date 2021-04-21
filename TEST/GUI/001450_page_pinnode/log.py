# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

## TODO GTK3: Why are some assert statements commented out?

import tests

checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer

# Load a Skeleton
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('OOF2').resize(782, 545)
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
findWidget('Dialog-Data:filename').set_text('examples/tw')
findWidget('Dialog-Data:filename').set_text('examples/two')
findWidget('Dialog-Data:filename').set_text('examples/two_')
findWidget('Dialog-Data:filename').set_text('examples/two_c')
findWidget('Dialog-Data:filename').set_text('examples/two_ci')
findWidget('Dialog-Data:filename').set_text('examples/two_cir')
findWidget('Dialog-Data:filename').set_text('examples/two_circ')
findWidget('Dialog-Data:filename').set_text('examples/two_circl')
findWidget('Dialog-Data:filename').set_text('examples/two_circle')
findWidget('Dialog-Data:filename').set_text('examples/two_circles')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.s')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.sk')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.ske')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.skel')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.skele')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.skelet')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.skeleto')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.skeleton')
findWidget('Dialog-Data:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
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
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pin Nodes']).activate() # MenuItemLogger
checkpoint page installed Pin Nodes
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Pin Nodes Page:Pane').set_position(549)
# assert tests.sensitization1()

# Open a graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
event(Gdk.EventType.BUTTON_PRESS,x= 3.8000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Settings.Graphics_Defaults.New_Layer_Policy
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint OOF.Graphics_1.Layer.Select
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
findWidget('OOF2 Graphics 1').resize(800, 492)
# assert tests.pinnedNodesCheck(0)

findWidget('OOF2:Pin Nodes Page:Pane:Modify:Invert').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Invert
# assert tests.pinnedNodesCheck(617)
assert tests.sensitization2()

# Unpin all nodes
findWidget('OOF2:Pin Nodes Page:Pane:Modify:Unpin All').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.UnpinAll
# assert tests.pinnedNodesCheck(0)
assert tests.sensitization3()

# Undo
findWidget('OOF2:Pin Nodes Page:Pane:Modify:Undo').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Undo
# assert tests.pinnedNodesCheck(617)
assert tests.sensitization4()

# Undo again
findWidget('OOF2:Pin Nodes Page:Pane:Modify:Undo').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Undo
# assert tests.pinnedNodesCheck(0)
assert tests.sensitization5()

# Redo
findWidget('OOF2:Pin Nodes Page:Pane:Modify:Redo').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Redo
# assert tests.pinnedNodesCheck(617)
assert tests.sensitization4()

# Pin internal boundary nodes
event(Gdk.EventType.BUTTON_PRESS,x= 6.6000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pin Nodes Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Pin Internal Boundary Nodes']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pin Nodes Page:Pane').set_position(508)
findWidget('OOF2:Pin Nodes Page:Pane:Modify:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Pin_Internal_Boundary_Nodes
# assert tests.pinnedNodesCheck(617)

# Unpin all, *then* pin internal boundary nodes.
findWidget('OOF2:Pin Nodes Page:Pane:Modify:Unpin All').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.UnpinAll
# assert tests.pinnedNodesCheck(0)

findWidget('OOF2:Pin Nodes Page:Pane:Modify:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Pin_Internal_Boundary_Nodes
# assert tests.pinnedNodesCheck(106)

findWidget('OOF2:Pin Nodes Page:Pane:Modify:Undo').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Undo
# assert tests.pinnedNodesCheck(0)

findWidget('OOF2:Pin Nodes Page:Pane:Modify:Redo').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Redo
# assert tests.pinnedNodesCheck(106)

# Select some nodes, then unpin them.
event(Gdk.EventType.BUTTON_PRESS,x= 1.1600000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pin Nodes Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['UnPin Node Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pin Nodes Page:Pane').set_position(544)
event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Selection']).activate() # MenuItemLogger
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(265)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Node').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.4000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 45.275, 87.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 45.275, 87.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 44.925, 87.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 44.225, 82.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.175, 78.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.825, 74.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.475, 71.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.475, 67.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.125, 64.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.475, 62.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.175, 60.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 45.275, 58.05, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 46.325, 56.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 49.125, 53.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.275, 51.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.075, 49.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.775, 48.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.475, 47.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 57.175, 46.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 57.875, 46.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 59.975, 44.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 61.725, 43.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 64.525, 42.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 69.075, 40.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.875, 40.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 74.325, 40.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 75.375, 40.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 75.725, 40.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 76.425, 40.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.825, 40.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.925, 40.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.025, 40.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.375, 41.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.725, 41.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.425, 41.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.125, 41.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.175, 41.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.875, 41.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 86.925, 41.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.975, 40.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.325, 40.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.325, 41.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.325, 41.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.675, 41.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.675, 41.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.675, 41.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.675, 41.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.675, 42.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.675, 42.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.675, 42.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 88.675, 42.3, 1, False, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Rectangle
findWidget('OOF2:Pin Nodes Page:Pane:Modify:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.UnPin_Node_Selection
# assert tests.pinnedNodesCheck(71)

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Clear').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Clear
# Reselect and repin the nodes
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Undo').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Undo
event(Gdk.EventType.BUTTON_PRESS,x= 9.1000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pin Nodes Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Pin Node Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pin Nodes Page:Pane').set_position(549)
findWidget('OOF2:Pin Nodes Page:Pane:Modify:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Pin_Node_Selection
# assert tests.pinnedNodesCheck(212)

# Clear the node selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Clear').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Clear
# Unpin all nodes
findWidget('OOF2:Pin Nodes Page:Pane:Modify:Unpin All').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.UnpinAll
# assert tests.pinnedNodesCheck(0)

# Select a single segment
findGfxWindow('Graphics_1').simulateMouse('down', 36.875, 91.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 36.875, 91.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 36.875, 90.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 36.875, 90.95, 1, False, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Rectangle
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
findGfxWindow('Graphics_1').simulateMouse('down', 34.425, 90.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 34.425, 90.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 34.425, 90.6, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
# Pin the nodes of the selected segment
event(Gdk.EventType.BUTTON_PRESS,x= 9.6000000000000e+01,y= 6.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Pin Nodes Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Pin Selected Segments']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pin Nodes Page:Pane').set_position(537)
findWidget('OOF2:Pin Nodes Page:Pane:Modify:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Pin_Selected_Segments
# assert tests.pinnedNodesCheck(2)

# Select an element
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Element').clicked()
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
findGfxWindow('Graphics_1').simulateMouse('down', 3.625, 87.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.625, 87.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.975, 87.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.975, 87.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 3.975, 87.45, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Single_Element
# Pin the nodes of the element
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pin Nodes Page:Pane:Modify:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Pin Selected Elements']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pin Nodes Page:Pane').set_position(541)
findWidget('OOF2:Pin Nodes Page:Pane:Modify:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Pin_Selected_Elements
# assert tests.pinnedNodesCheck(6)

findWidget('OOF2:Pin Nodes Page:Pane:Modify:Invert').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Invert
# assert tests.pinnedNodesCheck(611)

# delete the skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 8.9000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint skeleton page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(192, 86)
findWidget('Questioner:OK').clicked()
checkpoint skeleton page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
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
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.Delete
# Create a new skeleton
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
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
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New
event(Gdk.EventType.BUTTON_PRESS,x= 7.3000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pin Nodes']).activate() # MenuItemLogger
checkpoint page installed Pin Nodes
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger

# Create another new skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 8.3000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint skeleton page sensitized
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New

# Pin all nodes in the new skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 6.9000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pin Nodes']).activate() # MenuItemLogger
checkpoint page installed Pin Nodes
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.sensitization1()
findWidget('OOF2:Pin Nodes Page:Pane:Modify:Invert').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.PinNodes.Invert
assert tests.chooserStateCheck('OOF2:Pin Nodes Page:Skeleton', 'skeleton')
assert tests.chooserCheck('OOF2:Pin Nodes Page:Skeleton', ['skeleton', 'skeleton<2>'])
assert tests.pinnedNodesCheck(25)

# Switch to the other skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 5.5000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pin Nodes Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger

# Delete the second skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 8.6000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint skeleton page sensitized
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(199, 86)
findWidget('Questioner:OK').clicked()
checkpoint skeleton page sensitized
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
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.Delete
event(Gdk.EventType.BUTTON_PRESS,x= 7.4000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pin Nodes']).activate() # MenuItemLogger
checkpoint page installed Pin Nodes
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.pinnedNodesCheck(25)
assert tests.sensitization2()

event(Gdk.EventType.BUTTON_PRESS,x= 7.4000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint skeleton page sensitized
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
# Delete the remaining skeleton
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(192, 86)
findWidget('Questioner:OK').clicked()
checkpoint skeleton page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
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
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.Delete
event(Gdk.EventType.BUTTON_PRESS,x= 4.3000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pin Nodes']).activate() # MenuItemLogger
checkpoint page installed Pin Nodes
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.chooserCheck('OOF2:Pin Nodes Page:Skeleton', [])
assert tests.sensitization0()

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
