# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 545)

# Create a Microstructure
event(Gdk.EventType.BUTTON_PRESS,x= 8.1000000000000e+01,y= 2.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
checkpoint page installed Microstructure
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
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
checkpoint pixel page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
checkpoint OOF.Microstructure.New
# Create a Material
event(Gdk.EventType.BUTTON_PRESS,x= 5.2000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(235, 122)
event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-Assign material material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['<every>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Material.Assign
# Create a 10x10 Skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 7.7000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
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
checkpoint skeleton selection page grouplist Element
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.New
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
# Create a 7x7 Skeleton with triangular elements
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:x_elements').set_text('')
findWidget('Dialog-New skeleton:x_elements').set_text('7')
findWidget('Dialog-New skeleton:y_elements').set_text('')
findWidget('Dialog-New skeleton:y_elements').set_text('7')
event(Gdk.EventType.BUTTON_PRESS,x= 6.0000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-New skeleton:skeleton_geometry:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['TriSkeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New skeleton').resize(381, 284)
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint skeleton page info updated
checkpoint OOF.Skeleton.New
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
# Open a graphics window
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
# Display the 7x7 Skeleton
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New Graphics Layer
findWidget('Dialog-New Graphics Layer').resize(395, 532)
event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-New Graphics Layer:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 8.3000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Graphics Layer:what:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
findWidget('Dialog-New Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
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
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
# Select a bunch of segments
findWidget('OOF2 Graphics 1').resize(800, 492)
event(Gdk.EventType.BUTTON_PRESS,x= 3.2000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(265)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
# Select a diagonal line of segments from the top left to bottom right
findGfxWindow('Graphics_1').simulateMouse('down', 0.059979965, 0.9417731, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.059979965, 0.9417731, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.19470323, 0.80529677, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.19470323, 0.80529677, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.19820937, 0.80179063, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.2017155, 0.7982845, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.2017155, 0.7982845, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.34196093, 0.66505134, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.34196093, 0.66505134, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.34546707, 0.66505134, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.34546707, 0.6615452, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.34546707, 0.6615452, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.48220636, 0.5142875, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.48220636, 0.51078137, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.48921863, 0.50727523, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.48921863, 0.50727523, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.64348861, 0.35300526, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.64348861, 0.34949912, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.65050088, 0.34599299, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.65050088, 0.34599299, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.7802279, 0.21626597, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.7802279, 0.21275983, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.78373403, 0.20925369, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.79074631, 0.20574756, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.79074631, 0.20574756, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.95904082, 0.044465314, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.95904082, 0.044465314, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.96254696, 0.044465314, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.96605309, 0.044465314, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.96605309, 0.044465314, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
# Construct an edge boundary from the segments
findWidget('OOF2 Graphics 1').resize(800, 492)
event(Gdk.EventType.BUTTON_PRESS,x= 8.5000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Boundaries']).activate() # MenuItemLogger
checkpoint page installed Skeleton Boundaries
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Boundaries Page:Pane').set_position(379)
event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Boundaries Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
checkpoint boundary page updated
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(306, 194)
findWidget('Dialog-New Boundary:name').delete_text(0, 11)
findWidget('Dialog-New Boundary:name').insert_text('d', 11)
findWidget('Dialog-New Boundary:name').insert_text('i', 1)
findWidget('Dialog-New Boundary:name').insert_text('a', 2)
findWidget('Dialog-New Boundary:name').insert_text('g', 3)
findWidget('Dialog-New Boundary:name').insert_text('o', 4)
findWidget('Dialog-New Boundary:name').insert_text('n', 5)
findWidget('Dialog-New Boundary:name').insert_text('a', 6)
findWidget('Dialog-New Boundary:name').insert_text('l', 7)
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Construct
# Create a Mesh for each Skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 8.7000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(130)
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:FE Mesh Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(299, 244)
findWidget('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.New
event(Gdk.EventType.BUTTON_PRESS,x= 8.4000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:FE Mesh Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(299, 244)
findWidget('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.New
# Define temperature field and heat equation on skeleton 2's mesh
event(Gdk.EventType.BUTTON_PRESS,x= 8.0000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Fields & Equations Page:HPane').set_position(470)
event(Gdk.EventType.BUTTON_PRESS,x= 6.0000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
checkpoint Field page sensitized
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Field page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Heat_Eqn active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint OOF.Subproblem.Equation.Activate
# Define temperature field and heat equation on skeleton 1's mesh,
# plus displacement and force balance
event(Gdk.EventType.BUTTON_PRESS,x= 5.9000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
checkpoint Field page sensitized
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Heat_Eqn active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Force_Balance active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Activate
# Go to the Boundary Analysis page.
event(Gdk.EventType.BUTTON_PRESS,x= 6.8000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Analysis']).activate() # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(211)
event(Gdk.EventType.BUTTON_PRESS,x= 5.8000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Analysis Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
assert tests.bdyList('top', 'bottom', 'right', 'left')
assert tests.goSensitive(0)

event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Analysis Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
assert tests.bdyList('top', 'bottom', 'right', 'diagonal', 'left')
assert tests.goSensitive(0)

# Select the diagonal bdy
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([3]))
assert tests.goSensitive(1)

# Switch to the skeleton with no diagonal bdy
event(Gdk.EventType.BUTTON_PRESS,x= 8.4000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Analysis Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
assert tests.bdyList('top', 'bottom', 'right', 'left')
assert tests.goSensitive(0)

# Choose the displacement field output
event(Gdk.EventType.BUTTON_PRESS,x= 7.5000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Boundary Analysis Page:Pane:BdyAnalyzerRCF:Average Field:field').get_window())
checkpoint toplevel widget mapped chooserPopup-field
findMenu(findWidget('chooserPopup-field'), ['Displacement']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field') # MenuItemLogger
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(208)
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([3]))
assert tests.goSensitive(1)

# Switch to the mesh with no displacement field
event(Gdk.EventType.BUTTON_PRESS,x= 5.6000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Analysis Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(211)
assert tests.goSensitive(1)

# Select the diagonal boundary
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([3]))
assert tests.goSensitive(1)

# Switch back to the mesh with no diagonal boundary
event(Gdk.EventType.BUTTON_PRESS,x= 5.0000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Analysis Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
assert tests.goSensitive(0)

# Switch back to displacement w/out selecting a boundary
event(Gdk.EventType.BUTTON_PRESS,x= 1.2500000000000e+02,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Analysis Page:Pane:BdyAnalyzerRCF:Average Field:field').get_window())
checkpoint toplevel widget mapped chooserPopup-field
findMenu(findWidget('chooserPopup-field'), ['Displacement']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field') # MenuItemLogger
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(208)
# Swich to the Skeleton with no displacement
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Analysis Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(211)
assert tests.goSensitive(0)

# Delete the diagonal boundary
event(Gdk.EventType.BUTTON_PRESS,x= 6.4000000000000e+01,y= 2.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Boundaries']).activate() # MenuItemLogger
checkpoint page installed Skeleton Boundaries
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Delete').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh page sensitized
checkpoint OOF.Skeleton.Boundary.Delete
# Back to the Boundary Analysis page
event(Gdk.EventType.BUTTON_PRESS,x= 8.4000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Analysis']).activate() # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.bdyList('top', 'bottom', 'right', 'left')
assert tests.goSensitive(0)

# Delete the mesh from skeleton<2>
event(Gdk.EventType.BUTTON_PRESS,x= 8.3000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(297, 86)
findWidget('Questioner:Yes').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint selection info updated Node
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Mesh.Delete
# Check the Boundary Analysis page
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(256)
assert tests.bdyList()
assert tests.goSensitive(0)

event(Gdk.EventType.BUTTON_PRESS,x= 5.2000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Analysis Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(211)
assert tests.bdyList('top', 'bottom', 'right', 'left')
assert tests.goSensitive(0)

# Switch the display to the other skeleton
findWidget('OOF2 Graphics 1').resize(800, 492)
event(Gdk.EventType.BUTTON_PRESS,x= 2.0200000000000e+02,y= 2.7000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
event(Gdk.EventType.BUTTON_PRESS,x= 2.0200000000000e+02,y= 2.7000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(2)
tree.row_activated(Gtk.TreePath([10]), column)
checkpoint toplevel widget mapped Dialog-Edit Graphics Layer
findWidget('Dialog-Edit Graphics Layer').resize(359, 380)
event(Gdk.EventType.BUTTON_PRESS,x= 9.8000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-Edit Graphics Layer:what:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
findWidget('Dialog-Edit Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
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
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Edit
# Select some internal segments
event(Gdk.EventType.BUTTON_PRESS,x= 9.4000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.4000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 0.049461558, 0.65076384, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.049461558, 0.6472577, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.049461558, 0.64024543, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.052967693, 0.62972702, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.056473829, 0.61920862, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.070498372, 0.60869021, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.084522915, 0.60167794, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.10906587, 0.59466566, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.13010268, 0.59115953, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.15464563, 0.58765339, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.18970699, 0.58064112, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.25632357, 0.57362885, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.31592787, 0.55960431, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.38955672, 0.54207363, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.42111195, 0.53856749, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.4561733, 0.53506136, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.4947408, 0.53506136, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.52629602, 0.53506136, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.56486351, 0.53155522, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.603431, 0.53155522, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.63148009, 0.53506136, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.6525169, 0.53856749, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68407213, 0.53856749, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.70861508, 0.53856749, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.73315803, 0.54207363, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.76471325, 0.54557976, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.80328074, 0.54557976, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.83483596, 0.5490859, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.85937891, 0.5490859, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.88041573, 0.55259204, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.89444027, 0.55259204, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.90846481, 0.55609817, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.92248936, 0.55960431, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.93300776, 0.56311044, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.9365139, 0.56311044, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.94703231, 0.55960431, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.95053844, 0.55960431, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.95404458, 0.55960431, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.95404458, 0.55609817, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.95404458, 0.55609817, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.95404458, 0.55609817, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.95404458, 0.55259204, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.95404458, 0.55259204, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Rectangle
# Create a boundary from the selected segments
event(Gdk.EventType.BUTTON_PRESS,x= 7.9000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Boundaries']).activate() # MenuItemLogger
checkpoint page installed Skeleton Boundaries
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 4.7000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Boundaries Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
checkpoint boundary page updated
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(306, 194)
findWidget('Dialog-New Boundary:name').delete_text(0, 8)
findWidget('Dialog-New Boundary:name').insert_text('i', 11)
findWidget('Dialog-New Boundary:name').insert_text('n', 1)
findWidget('Dialog-New Boundary:name').insert_text('t', 2)
findWidget('Dialog-New Boundary:name').insert_text('e', 3)
findWidget('Dialog-New Boundary:name').insert_text('r', 4)
findWidget('Dialog-New Boundary:name').insert_text('i', 5)
findWidget('Dialog-New Boundary:name').insert_text('o', 6)
findWidget('Dialog-New Boundary:name').insert_text('r', 7)
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.Boundary.Construct
# Back to the Bdy Anal. page
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Analysis']).activate() # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.bdyList('top', 'bottom', 'right', 'left', 'interior')
assert tests.goSensitive(0)

findWidget('OOF2').resize(782, 545)

## Test that double-clicking a boundary name doesn't do anything when
## the boundary operation chooser is invalid.  If this test fails, the
## program won't exit properly.

event(Gdk.EventType.BUTTON_PRESS,x= 8.8000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations

# The Fields and Equations page is insensitive because the mesh needs
# to be rebuilt.  This isn't really the right scope to check it, but
# it's convenient.  It should have been done in the field page tests.
assert tests.fieldPageInsensitive()

event(Gdk.EventType.BUTTON_PRESS,x= 9.6000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
event(Gdk.EventType.BUTTON_PRESS,x= 8.2000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:FE Mesh Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
findWidget('OOF2:FE Mesh Page:Pane:ElementOps:OK').clicked()
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Mesh.Modify
event(Gdk.EventType.BUTTON_PRESS,x= 8.7000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
assert tests.fieldPageSensitive()

# Undefine the fields so that the boundary analysis has nothing to work on
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Subproblem.Field.Undefine
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Subproblem.Field.Undefine
event(Gdk.EventType.BUTTON_PRESS,x= 7.7000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis

# Double-clicking on a boundary name should now do nothing.
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([2]))
tree=findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([2]), column)

# Comparing the log file verifies that nothing happened.
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
