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
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 4.1000000000000e+01,y= 2.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Settings.Graphics_Defaults.New_Layer_Policy
# Create a Microstructure and Skeleton
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('Dialog-Create Microstructure:widget_GTK_RESPONSE_OK').clicked()
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
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.New
event(Gdk.EventType.BUTTON_PRESS,x= 8.1000000000000e+01,y= 2.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:x_elements').set_text('')
findWidget('Dialog-New skeleton:x_elements').set_text('1')
findWidget('Dialog-New skeleton:x_elements').set_text('10')
findWidget('Dialog-New skeleton:y_elements').set_text('')
findWidget('Dialog-New skeleton:y_elements').set_text('1')
findWidget('Dialog-New skeleton:y_elements').set_text('10')
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.New
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
event(Gdk.EventType.BUTTON_PRESS,x= 3.6000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint skeleton selection page grouplist Element
checkpoint page installed Skeleton Selection
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(474)
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
assert tests.sensitization0()

# Switch to Node Mode
findWidget('OOF2:Skeleton Selection Page:Mode:Node').clicked()
checkpoint skeleton selection page grouplist Node
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
assert tests.sensitization0()
assert tests.nodeSelectionCheck([])
assert tests.selectionSizeCheck(0)

# Select some nodes via the graphics window
event(Gdk.EventType.BUTTON_PRESS,x= 6.9000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(265)
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Node').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.4000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 0.052967693, 0.9417731, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.052967693, 0.93826697, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.049461558, 0.92774856, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.045955422, 0.88918107, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.042449286, 0.80152767, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.035437015, 0.69283747, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.028424743, 0.63323316, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.031930879, 0.61219634, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.038943151, 0.60518407, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.070498372, 0.58414726, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.095041322, 0.57012271, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.13360882, 0.56311044, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.16516404, 0.55960431, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.20373153, 0.55609817, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.24931129, 0.54557976, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28437265, 0.54207363, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.30540947, 0.54207363, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.31592787, 0.54207363, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.33696469, 0.54207363, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.35449537, 0.54557976, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36150764, 0.5490859, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37202605, 0.55259204, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.38254445, 0.55259204, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.38605059, 0.55259204, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.38955672, 0.55259204, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.396569, 0.55259204, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.40007513, 0.55259204, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.40358127, 0.55609817, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.4070874, 0.55609817, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.4070874, 0.55609817, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.41059354, 0.55609817, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.43163035, 0.55259204, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.44916103, 0.5490859, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.46669171, 0.54207363, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.47019785, 0.54207363, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.46669171, 0.54207363, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.46669171, 0.54557976, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.46318557, 0.54557976, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.46318557, 0.54557976, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.46318557, 0.54557976, 1, False, False)
checkpoint Graphics_1 Node sensitized
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Rectangle
assert tests.selectionModeCheck('Nodes')
assert tests.selectionSizeCheck(16)
assert tests.nodeSelectionCheck([67, 68, 69, 70, 78, 79, 80, 81, 89, 90, 91, 92, 100, 101, 102, 103])

# Invert the selection
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Invert').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint Graphics_1 Node sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Invert
assert tests.selectionSizeCheck(105)
assert tests.sensitization1()

# Invert again
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Invert').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Invert
assert tests.selectionSizeCheck(16)
assert tests.nodeSelectionCheck([67, 68, 69, 70, 78, 79, 80, 81, 89, 90, 91, 92, 100, 101, 102, 103])
assert tests.sensitization1()

# create a node group
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new Node group
findWidget('Dialog-Create a new Node group').resize(192, 92)
findWidget('Dialog-Create a new Node group:name').delete_text(0, 11)
findWidget('Dialog-Create a new Node group:name').insert_text('n', 11)
findWidget('Dialog-Create a new Node group:name').insert_text('g', 1)
findWidget('Dialog-Create a new Node group:name').insert_text('r', 2)
findWidget('Dialog-Create a new Node group:name').insert_text('o', 3)
findWidget('Dialog-Create a new Node group:name').insert_text('p', 4)
findWidget('Dialog-Create a new Node group:name').insert_text('p', 5)
findWidget('Dialog-Create a new Node group:name').delete_text(5, 6)
findWidget('Dialog-Create a new Node group:name').delete_text(4, 5)
findWidget('Dialog-Create a new Node group:name').insert_text('o', 4)
findWidget('Dialog-Create a new Node group:name').insert_text('p', 5)
findWidget('Dialog-Create a new Node group:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page grouplist Node
checkpoint OOF.NodeGroup.New_Group
checkpoint skeleton selection page groups sensitized Node
assert tests.groupCheck(['ngroop (0 nodes)'])
assert tests.sensitization2()

# Add nodes to the group
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:Add').clicked()
checkpoint skeleton selection page grouplist Node
checkpoint skeleton selection page groups sensitized Node
checkpoint OOF.NodeGroup.Add_to_Group
assert tests.groupCheck(['ngroop (16 nodes)'])

# Select three segments
event(Gdk.EventType.BUTTON_PRESS,x= 1.1100000000000e+02,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findWidget('chooserPopup-RCFChooser').deactivate() # MenuLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.14763336, 0.70335587, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.14763336, 0.70335587, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.27736038, 0.71036814, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.27736038, 0.71036814, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.27736038, 0.71036814, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.36150764, 0.70335587, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.36150764, 0.70335587, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
# Select nodes from segments
event(Gdk.EventType.BUTTON_PRESS,x= 1.1300000000000e+02,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findWidget('chooserPopup-RCFChooser').deactivate() # MenuLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Select_from_Selected_Segments
assert tests.nodeSelectionCheck([78, 79, 80, 81])
assert tests.selectionSizeCheck(4)

# Remove nodes from the group
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:Remove').clicked()
checkpoint skeleton selection page grouplist Node
checkpoint skeleton selection page groups sensitized Node
checkpoint OOF.NodeGroup.Remove_from_Group
assert tests.groupCheck(['ngroop (12 nodes)'])

# Select the group
event(Gdk.EventType.BUTTON_PRESS,x= 9.5000000000000e+01,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Select_Group
assert tests.nodeSelectionCheck([67, 68, 69, 70, 89, 90, 91, 92, 100, 101, 102, 103])
assert tests.selectionSizeCheck(12)

# Clear the segment selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Clear').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Clear

# Select a rectangle of elements
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Element').clicked()
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
event(Gdk.EventType.BUTTON_PRESS,x= 6.6000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 0.37202605, 0.53506136, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37202605, 0.53506136, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37202605, 0.52804909, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36851991, 0.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36501377, 0.46493864, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36150764, 0.42987729, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36851991, 0.4018282, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.38955672, 0.38079138, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.42111195, 0.36326071, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.4456549, 0.34923616, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.46669171, 0.33871776, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.50876534, 0.32819935, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.55083897, 0.32819935, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.57538192, 0.32118708, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.603431, 0.31066867, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.63849236, 0.30015026, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68056599, 0.28612572, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.69809667, 0.27911345, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.71913348, 0.27210118, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.72614576, 0.26859504, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.72965189, 0.26859504, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.72965189, 0.26859504, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.72965189, 0.26859504, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73315803, 0.26508891, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.74718257, 0.26158277, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.74718257, 0.26158277, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.74718257, 0.26158277, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.74718257, 0.26508891, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.74718257, 0.26508891, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.74718257, 0.26508891, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.74718257, 0.26859504, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.74718257, 0.26859504, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Rectangle

# Select nodes from selected elements
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select from Selected Elements']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Select_from_Selected_Elements
assert tests.nodeSelectionCheck([37, 38, 39, 40, 48, 51, 59, 60, 61, 62])
assert tests.selectionSizeCheck(10)

# Select internal nodes only from the element selection
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:Select from Selected Elements:internal').clicked()
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:Select from Selected Elements:boundary').clicked()
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Select_from_Selected_Elements
assert tests.nodeSelectionCheck([49, 50])
assert tests.selectionSizeCheck(2)

# Select all node from the elements
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:Select from Selected Elements:boundary').clicked()
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Select_from_Selected_Elements
assert tests.nodeSelectionCheck([37, 38, 39, 40, 48, 49, 50, 51, 59, 60, 61, 62])
assert tests.selectionSizeCheck(12)

# Add a Microstructure Material display
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New Graphics Layer
findWidget('Dialog-New Graphics Layer').resize(395, 532)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 1.3698630136986e-02)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 8.2191780821918e-02)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 1.0958904109589e-01)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 1.5068493150685e-01)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 1.9178082191781e-01)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 2.0547945205479e-01)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 2.4657534246575e-01)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 2.6027397260274e-01)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 2.8767123287671e-01)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 3.1506849315068e-01)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 3.2876712328767e-01)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 3.4246575342466e-01)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 3.5616438356164e-01)
findWidget('Dialog-New Graphics Layer:how:Material:no_material:TranslucentGray:gray:slider').get_adjustment().set_value( 3.6986301369863e-01)
findWidget('Dialog-New Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New

# Select a bunch of pixels
event(Gdk.EventType.BUTTON_PRESS,x= 8.8000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 7.9000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 0.19671926, 0.79802154, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.20022539, 0.79802154, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.20373153, 0.79802154, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.21775607, 0.79100927, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.22476834, 0.78399699, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.23879289, 0.77347859, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.25281743, 0.76296018, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.27034811, 0.74893564, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.28086652, 0.73841723, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29489106, 0.72789882, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.30190333, 0.72088655, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.3089156, 0.71036814, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.31592787, 0.70335587, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.32644628, 0.69283747, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.33696469, 0.68231906, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.3474831, 0.67180065, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.35098923, 0.66478838, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.35449537, 0.66128224, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.3580015, 0.66128224, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.3580015, 0.65777611, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36150764, 0.65076384, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36501377, 0.64375157, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36851991, 0.64024543, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36851991, 0.63673929, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36851991, 0.63323316, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37202605, 0.63323316, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37202605, 0.63323316, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37202605, 0.62972702, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37202605, 0.62972702, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.62972702, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.62622089, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37903832, 0.62271475, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.38605059, 0.61920862, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.38955672, 0.61920862, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.38955672, 0.61570248, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.39306286, 0.61570248, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.39306286, 0.61219634, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.39306286, 0.61219634, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.39306286, 0.61219634, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.39306286, 0.60869021, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.396569, 0.60869021, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.396569, 0.60518407, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.396569, 0.60518407, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.396569, 0.60518407, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.396569, 0.60518407, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle

# Put the pixels in a group
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 7.5000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Node
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
assert tests.sensitization7()

event(Gdk.EventType.BUTTON_PRESS,x= 7.2000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton Selection

# Select internal boundaries
event(Gdk.EventType.BUTTON_PRESS,x= 1.2700000000000e+02,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Internal Boundaries']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Select_Internal_Boundaries
assert tests.nodeSelectionCheck([56, 57, 58, 66, 67, 69, 70, 81, 82, 93, 103, 104, 114])
assert tests.selectionSizeCheck(13)

# Make the pixel group unmeshable
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Meshable').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint OOF.PixelGroup.Meshable

# Select internal boundary nodes again (there aren't any)
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Skeleton Selection
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Select_Internal_Boundaries
assert tests.nodeSelectionCheck([])
assert tests.selectionSizeCheck(0)
assert tests.sensitization6()

# # Make the node group meshable again
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Meshable').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint OOF.PixelGroup.Meshable
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Skeleton Selection
# Reselect the internal boundaries
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Select_Internal_Boundaries
assert tests.nodeSelectionCheck([56, 57, 58, 66, 67, 69, 70, 81, 82, 93, 103, 104, 114])
assert tests.selectionSizeCheck(13)

# Expand the node selection
event(Gdk.EventType.BUTTON_PRESS,x= 1.0200000000000e+02,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Expand Node Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Expand_Node_Selection
assert tests.nodeSelectionCheck([44, 45, 46, 47, 48, 55, 56, 57, 58, 59, 60, 66, 67, 68, 69, 70, 71, 72, 77, 78, 79, 80, 81, 82, 83, 91, 92, 93, 94, 102, 103, 104, 105, 113, 114, 115, 116])
assert tests.selectionSizeCheck(37)

findWidget('OOF2').resize(782, 545)
# Undo the expansion
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
assert tests.nodeSelectionCheck([56, 57, 58, 66, 67, 69, 70, 81, 82, 93, 103, 104, 114])
assert tests.selectionSizeCheck(13)

# Expand by segments
event(Gdk.EventType.BUTTON_PRESS,x= 8.5000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:Expand Node Selection:criterion:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['By Segments']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Expand_Node_Selection
assert tests.nodeSelectionCheck([45, 46, 47, 55, 56, 57, 58, 59, 66, 67, 68, 69, 70, 71, 77, 78, 80, 81, 82, 83, 92, 93, 94, 102, 103, 104, 105, 113, 114, 115])
assert tests.selectionSizeCheck(30)

# undo
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
assert tests.nodeSelectionCheck([56, 57, 58, 66, 67, 69, 70, 81, 82, 93, 103, 104, 114])
assert tests.selectionSizeCheck(13)

# Undo all the way
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
assert tests.sensitization3()

findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
assert tests.sensitization4()
assert tests.selectionSizeCheck(0)
assert tests.nodeSelectionCheck([])

# Select a group
event(Gdk.EventType.BUTTON_PRESS,x= 7.9000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Select_Group
assert tests.nodeSelectionCheck([67, 68, 69, 70, 89, 90, 91, 92, 100, 101, 102, 103])
assert tests.selectionSizeCheck(12)

# Select a set of nodes that intersects the group's nodes nontrivially
event(Gdk.EventType.BUTTON_PRESS,x= 1.0200000000000e+02,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findWidget('chooserPopup-RCFChooser').deactivate() # MenuLogger
event(Gdk.EventType.BUTTON_PRESS,x= 6.3000000000000e+01,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(265)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.0000000000000e+01)
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Node').clicked()
checkpoint selection info updated Node
checkpoint Graphics_1 Node sensitized
findGfxWindow('Graphics_1').simulateMouse('down', -0.041697971, 0.85411971, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', -0.041697971, 0.85411971, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', -0.041697971, 0.85762585, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', -0.0346857, 0.85762585, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', -0.01014275, 0.85762585, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.035437015, 0.86463812, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.084522915, 0.86463812, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.14062109, 0.86463812, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.19321312, 0.85762585, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.22126221, 0.85411971, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.24229902, 0.84710744, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.27385424, 0.8330829, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.31242174, 0.80152767, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.33345855, 0.76997245, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.35098923, 0.73841723, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.35449537, 0.71738042, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.3580015, 0.69283747, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36501377, 0.67530679, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36851991, 0.65426997, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.62972702, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.61570248, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.5981718, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.58414726, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37202605, 0.56661658, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37202605, 0.55259204, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37202605, 0.54207363, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37202605, 0.53856749, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.53856749, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.53506136, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.53506136, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.53155522, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.53155522, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.52804909, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.52804909, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37553218, 0.52103681, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36851991, 0.51402454, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36501377, 0.50701227, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36150764, 0.49649386, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36150764, 0.49298773, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36150764, 0.48948159, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.36150764, 0.47896319, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.3580015, 0.47896319, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.3580015, 0.47545705, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.3580015, 0.47195091, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.3580015, 0.46844478, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.3580015, 0.46493864, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.3580015, 0.46844478, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.35449537, 0.46844478, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.35098923, 0.46844478, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.34397696, 0.46844478, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.34047082, 0.47195091, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.33345855, 0.47545705, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.32995242, 0.47545705, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.32995242, 0.47896319, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.32995242, 0.47896319, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.32995242, 0.47896319, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.34047082, 0.47896319, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.37202605, 0.47896319, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.396569, 0.47545705, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.40007513, 0.47896319, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.40358127, 0.47896319, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.41760581, 0.47896319, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.42461808, 0.47545705, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.42812422, 0.47545705, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.42812422, 0.47545705, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.43513649, 0.47545705, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.43864262, 0.47195091, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.44214876, 0.46844478, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.4456549, 0.46844478, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.4456549, 0.46844478, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.44916103, 0.46493864, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.45266717, 0.46493864, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.4561733, 0.46493864, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.4561733, 0.46493864, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.46318557, 0.46493864, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.48071625, 0.46493864, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.48772852, 0.46493864, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.4947408, 0.46493864, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.50876534, 0.46493864, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.51928375, 0.46143251, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.52629602, 0.46143251, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.53330829, 0.45792637, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.54032056, 0.45792637, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.5438267, 0.45442024, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.54733283, 0.45442024, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.54733283, 0.45442024, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.55083897, 0.45442024, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.55083897, 0.4509141, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.55083897, 0.4509141, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.55083897, 0.4509141, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.55083897, 0.4509141, 1, False, False)
checkpoint Graphics_1 Node sensitized
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Rectangle
assert tests.nodeSelectionCheck([55, 56, 57, 58, 59, 60, 66, 67, 68, 69, 70, 71, 77, 78, 79, 80, 81, 82, 88, 89, 90, 91, 92, 93])
assert tests.selectionSizeCheck(24)

# Add the group to the selection
event(Gdk.EventType.BUTTON_PRESS,x= 8.1000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Add Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Add_Group
assert tests.nodeSelectionCheck([55, 56, 57, 58, 59, 60, 66, 67, 68, 69, 70, 71, 77, 78, 79, 80, 81, 82, 88, 89, 90, 91, 92, 93, 100, 101, 102, 103])
assert tests.selectionSizeCheck(28)

# Unselect the group
event(Gdk.EventType.BUTTON_PRESS,x= 6.8000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Unselect Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Unselect_Group
assert tests.nodeSelectionCheck([55, 56, 57, 58, 59, 60, 66, 71, 77, 78, 79, 80, 81, 82, 88, 93])
assert tests.selectionSizeCheck(16)

# undo
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo
assert tests.nodeSelectionCheck([55, 56, 57, 58, 59, 60, 66, 67, 68, 69, 70, 71, 77, 78, 79, 80, 81, 82, 88, 89, 90, 91, 92, 93, 100, 101, 102, 103])
assert tests.selectionSizeCheck(28)
assert tests.sensitization3()

# undo again
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo

# uselect the group again, this time when not all group nodes are selected
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Unselect_Group
assert tests.nodeSelectionCheck([55, 56, 57, 58, 59, 60, 66, 71, 77, 78, 79, 80, 81, 82, 88, 93])
assert tests.selectionSizeCheck(16)

# undo
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Undo

# intersect with group
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Intersect Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Intersect_Group
assert tests.nodeSelectionCheck([67, 68, 69, 70, 89, 90, 91, 92])
assert tests.selectionSizeCheck(8)

# Remove nodes from group
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:Remove').clicked()
checkpoint skeleton selection page grouplist Node
checkpoint skeleton selection page groups sensitized Node
checkpoint OOF.NodeGroup.Remove_from_Group
assert tests.groupCheck(['ngroop (4 nodes)'])

# select the group again
event(Gdk.EventType.BUTTON_PRESS,x= 8.6000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint selection info updated Node
checkpoint Graphics_1 Node sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Select_Group
assert tests.nodeSelectionCheck([100, 101, 102, 103])
assert tests.selectionSizeCheck(4)

# Clear the group
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:Clear').clicked()
checkpoint skeleton selection page grouplist Node
checkpoint skeleton selection page groups sensitized Node
checkpoint OOF.NodeGroup.Clear_Group
assert tests.groupCheck(['ngroop (0 nodes)'])
assert tests.nodeSelectionCheck([100, 101, 102, 103])
assert tests.selectionSizeCheck(4)

# Delete the group
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:Delete').clicked()
checkpoint skeleton selection page grouplist Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint OOF.NodeGroup.Delete_Group
assert tests.groupCheck([])

# Clear the selection
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Clear').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Clear

# Create a new Skeleton with a different number of nodes
event(Gdk.EventType.BUTTON_PRESS,x= 5.5000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:x_elements').set_text('')
findWidget('Dialog-New skeleton:x_elements').set_text('9')
findWidget('Dialog-New skeleton:y_elements').set_text('')
findWidget('Dialog-New skeleton:y_elements').set_text('9')
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
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
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton Selection
assert tests.chooserCheck('OOF2:Skeleton Selection Page:Skeleton', ['skeleton', 'skeleton<2>'])
assert tests.chooserStateCheck('OOF2:Skeleton Selection Page:Skeleton', 'skeleton')

event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
checkpoint skeleton selection page grouplist Node
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Node
assert tests.groupCheck([])

# Make a group in the new skeleton
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new Node group
findWidget('Dialog-Create a new Node group').resize(192, 92)
findWidget('Dialog-Create a new Node group:name').insert_text('2', 6)
findWidget('Dialog-Create a new Node group:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page grouplist Node
checkpoint OOF.NodeGroup.New_Group
checkpoint skeleton selection page groups sensitized Node
assert tests.groupCheck(['ngroop2 (0 nodes)'])

# Invert the node selection
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Invert').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Invert
assert tests.selectionSizeCheck(100)

# Switch to the original Skeleton and check that the selection status updates properly
event(Gdk.EventType.BUTTON_PRESS,x= 8.2000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
checkpoint skeleton selection page grouplist Node
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
assert tests.selectionSizeCheck(0)

# Invert the node selection in the original skeleton
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Invert').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint Graphics_1 Node sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Invert
assert tests.selectionSizeCheck(121)

# Delete the current Skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 8.1000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(192, 86)
findWidget('Questioner:OK').clicked()
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
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
checkpoint Graphics_1 Node sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Node
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized Node
checkpoint Solver page sensitized
checkpoint skeleton page info updated
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint Field page sensitized
checkpoint skeleton page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.Delete
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton Selection
assert tests.selectionSizeCheck(100)
assert tests.groupCheck(['ngroop2 (0 nodes)'])

# Delete the other Skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 6.4000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(199, 86)
findWidget('Questioner:OK').clicked()
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Node sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Node
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.Delete
event(Gdk.EventType.BUTTON_PRESS,x= 4.9000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton Selection
assert tests.selectionSizeCheck(None)
assert tests.sensitization5()

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
