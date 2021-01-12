checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
import tests
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)
# Go to the Skeleton Boundary Page
findWidget('OOF2').resize(782, 511)
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Boundaries']).activate() # MenuItemLogger
checkpoint page installed Skeleton Boundaries
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Boundaries Page:Pane').set_position(379)
findWidget('OOF2').resize(782, 545)
assert tests.sensitization0()
assert tests.bdyStatusEmpty()
assert tests.bdyNames([])

# Load a Skeleton
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('examples/two_circles.skeleton')
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
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
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
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
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
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
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
assert tests.bdyNames(['top', 'right', 'bottom', 'left', None, 'topleft', 'bottomleft', 'topright', 'bottomright'])
assert tests.selectedBdy(None)
assert tests.sensitization1()

# Open a graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
event(Gdk.EventType.BUTTON_PRESS,x= 3.1000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
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
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2').resize(782, 545)
# Select the top boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
assert tests.bdyStatusCheck('top', 'Edge', 10)

# Select the right boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
assert tests.bdyStatusCheck('right', 'Edge', 14)

# Select the bottom boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([2]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
assert tests.bdyStatusCheck('bottom', 'Edge', 12)

# # Select the left boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([3]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
assert tests.bdyStatusCheck('left', 'Edge', 12)

# ... topleft
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([5]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
assert tests.bdyStatusCheck('topleft', 'Point', 1)

# ... bottomleft
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([6]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
assert tests.bdyStatusCheck('bottomleft', 'Point', 1)

# .. bottomright
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([8]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
assert tests.bdyStatusCheck('bottomright', 'Point', 1)

findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([6]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
assert tests.bdyStatusCheck('bottomleft', 'Point', 1)

# Select the elements in the yellow circle.
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(265)
event(Gdk.EventType.BUTTON_PRESS,x= 7.9000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['ByDominantPixel']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.4000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 26.41875, 42.34375, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 26.41875, 42.34375, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.ByDominantPixel
# Create a new boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(313, 194)
assert tests.newBdyOK(False)
assert tests.directionCheck('segments', ['No edge sequence'])

event(Gdk.EventType.BUTTON_PRESS,x= 1.4600000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary:constructor:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Edge boundary from elements']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.newBdyOK(True)
assert tests.directionCheck('elements', ['Clockwise', 'Counterclockwise'])

findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Construct
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary', None, 'topleft', 'bottomleft', 'topright', 'bottomright'])

# Create an element group from the red elements
event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Selection']).activate() # MenuItemLogger
checkpoint skeleton selection page grouplist Element
checkpoint page installed Skeleton Selection
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(474)
findGfxWindow('Graphics_1').simulateMouse('down', 66.275, 62.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 66.275, 62.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 66.275, 62.6, 1, False, False)
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
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new Element group
findWidget('Dialog-Create a new Element group').resize(192, 92)
findWidget('Dialog-Create a new Element group:name').delete_text(0, 11)
findWidget('Dialog-Create a new Element group:name').insert_text('r', 11)
findWidget('Dialog-Create a new Element group:name').insert_text('e', 1)
findWidget('Dialog-Create a new Element group:name').insert_text('d', 2)
findWidget('Dialog-Create a new Element group:name').insert_text(' ', 3)
findWidget('Dialog-Create a new Element group:name').insert_text('s', 4)
findWidget('Dialog-Create a new Element group:name').insert_text('p', 5)
findWidget('Dialog-Create a new Element group:name').insert_text('o', 6)
findWidget('Dialog-Create a new Element group:name').insert_text('t', 7)
findWidget('Dialog-Create a new Element group:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page grouplist Element
checkpoint OOF.ElementGroup.New_Group
checkpoint skeleton selection page groups sensitized Element
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:Add').clicked()
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.ElementGroup.Add_to_Group
# Go back to the Skeleton boundary page
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Skeleton Boundaries
# Create a boundary from the group
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(302, 194)
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary:constructor:Edge boundary from elements:group').get_window())
checkpoint toplevel widget mapped chooserPopup-group
findMenu(findWidget('chooserPopup-group'), ['red spot']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-group') # MenuItemLogger
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Construct
assert tests.bdyStatusCheck('boundary<2>', 'Edge', 38)
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary', 'boundary<2>', None, 'topleft', 'bottomleft', 'topright', 'bottomright'])

# Zoom in and select a single segment from the yellow circle's boundary
event(Gdk.EventType.KEY_PRESS, keyval=Gdk.keyval_from_name('plus'), state=5, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser').get_window())
event(Gdk.EventType.BUTTON_PRESS,x= 8.5000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Viewer']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer:Zoom:In').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.0000000000000e+01)
checkpoint OOF.Graphics_1.Settings.Zoom.In
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 7.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer:Zoom:In').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.3700000000000e+02)
checkpoint OOF.Graphics_1.Settings.Zoom.In
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.8700000000000e+02)
event(Gdk.EventType.BUTTON_PRESS,x= 5.6000000000000e+01,y= 6.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(265)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
findGfxWindow('Graphics_1').simulateMouse('down', 39.188889, 49.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 39.188889, 49.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 39.344444, 49.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 39.344444, 49.3, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
# Select the yellow boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([4]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
# Remove the segment from the boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Modify').clicked()
checkpoint toplevel widget mapped Dialog-Boundary modifier
findWidget('Dialog-Boundary modifier').resize(244, 128)
event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-Boundary modifier:modifier:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Remove segments']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Boundary modifier:widget_GTK_RESPONSE_OK').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Modify
assert tests.bdyStatusCheck('boundary', 'Edge', 30)

# Select some segments that join the two circles.
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Clear').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Clear
findGfxWindow('Graphics_1').simulateMouse('down', 38.255556, 51.788889, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 38.255556, 51.788889, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 40.433333, 52.722222, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 40.433333, 52.722222, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 42.611111, 54.277778, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 42.611111, 54.277778, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 44.322222, 56.766667, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 44.322222, 56.766667, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment

# Add the segments to the yellow boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Modify').clicked()
checkpoint toplevel widget mapped Dialog-Boundary modifier
findWidget('Dialog-Boundary modifier').resize(244, 128)
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-Boundary modifier:modifier:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Add segments']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Boundary modifier:widget_GTK_RESPONSE_OK').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Modify
# Go to the Skeleton selection page and select the segments in hte red boundary
event(Gdk.EventType.BUTTON_PRESS,x= 4.7000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Selection']).activate() # MenuItemLogger
checkpoint page installed Skeleton Selection
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Mode:Segment').clicked()
checkpoint skeleton selection page grouplist Segment
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint skeleton selection page updated
event(Gdk.EventType.BUTTON_PRESS,x= 1.0000000000000e+02,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:SegmentAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Named Boundary']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:SegmentAction:Select Named Boundary:boundary').get_window())
checkpoint toplevel widget mapped chooserPopup-boundary
findMenu(findWidget('chooserPopup-boundary'), ['boundary<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-boundary') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:SegmentHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint Graphics_1 Segment sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.SegmentSelection.Select_Named_Boundary
# Go back to the skeleton bdy page
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Skeleton Boundaries
assert tests.sensitization2()
assert tests.bdyStatusCheck('boundary', 'Edge', 34)

# Try to add the selected segments to the first boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Modify').clicked()
checkpoint toplevel widget mapped Dialog-Boundary modifier
findWidget('Dialog-Boundary modifier').resize(244, 128)
assert tests.modifyBdyOK(False)

findWidget('Dialog-Boundary modifier:widget_GTK_RESPONSE_CANCEL').clicked()
# Unselect one segment from the red boundary, making the resulting selected set simply connected
findGfxWindow('Graphics_1').simulateMouse('down', 47.122222, 55.522222, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 47.277778, 55.522222, 1, False, True)
checkpoint Graphics_1 Segment sensitized
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
# Try to add the selected segments to the boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Modify').clicked()
checkpoint toplevel widget mapped Dialog-Boundary modifier
findWidget('Dialog-Boundary modifier').resize(244, 128)
assert tests.modifyBdyOK(True)

findWidget('Dialog-Boundary modifier:widget_GTK_RESPONSE_OK').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Modify
# Check sizes
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([5]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
assert tests.bdyStatusCheck('boundary<2>', 'Edge', 38)

findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([4]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
assert tests.bdyStatusCheck('boundary', 'Edge', 71)

# Delete boundary<2>
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([5]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Delete').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint OOF.Skeleton.Boundary.Delete
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary', None,                       'topleft', 'bottomleft', 'topright', 'bottomright'])
assert tests.selectedBdy(None)

# Reselect the extended boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([4]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
# Select segments that will close it
findGfxWindow('Graphics_1').simulateMouse('up', 47.588889, 52.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('down', 47.744444, 52.411111, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.744444, 52.255556, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 47.744444, 52.255556, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint skeleton selection page updated
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 45.877778, 50.388889, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 45.877778, 50.388889, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 44.322222, 48.833333, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 44.322222, 48.677778, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 44.166667, 48.522222, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 44.166667, 48.522222, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint Graphics_1 Segment sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 43.233333, 48.055556, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.233333, 48.055556, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 43.233333, 48.055556, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint skeleton selection page updated
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
# Add the segments to the boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Modify').clicked()
checkpoint toplevel widget mapped Dialog-Boundary modifier
findWidget('Dialog-Boundary modifier').resize(244, 128)
assert tests.modifyBdyOK(True)

findWidget('Dialog-Boundary modifier:widget_GTK_RESPONSE_OK').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Modify
assert tests.bdyStatusCheck('boundary', 'Edge', 75)

# Reverse the boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Modify').clicked()
checkpoint toplevel widget mapped Dialog-Boundary modifier
findWidget('Dialog-Boundary modifier').resize(244, 128)
event(Gdk.EventType.BUTTON_PRESS,x= 7.7000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('Dialog-Boundary modifier:modifier:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Reverse direction']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.modifyBdyOK(True)

findWidget('Dialog-Boundary modifier:widget_GTK_RESPONSE_OK').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Modify
assert tests.bdyStatusCheck('boundary', 'Edge', 75)

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.8750000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.9196428571429e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 2.8794642857143e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.5937500000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.7500000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.3835714285714e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.2172619047619e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.9800000000000e+02)

# Select a line of nodes
findWidget('OOF2 Graphics 1').resize(809, 492)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(681)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(269)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.9300000000000e+02)
findWidget('OOF2 Graphics 1').resize(924, 492)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(796)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(315)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.2400000000000e+02)
findWidget('OOF2 Graphics 1').resize(1049, 500)
findWidget('OOF2 Graphics 1:Pane0').set_position(368)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(921)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(365)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.4900000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.6700000000000e+02)
findWidget('OOF2 Graphics 1').resize(1052, 500)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(924)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(366)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.4700000000000e+02)
findWidget('OOF2 Graphics 1').resize(1051, 500)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(923)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Node').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
event(Gdk.EventType.BUTTON_PRESS,x= 8.1000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 42.922222, 16.477778, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.922222, 16.322222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.922222, 16.166667, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.922222, 15.855556, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.922222, 15.388889, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 42.922222, 14.922222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.077778, 14.766667, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.233333, 14.611111, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.855556, 14.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 44.633333, 14.144444, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 45.1, 13.988889, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 46.188889, 13.833333, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.588889, 13.677778, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 48.677778, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.388889, 13.366667, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 51.477778, 13.211111, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.722222, 13.211111, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.766667, 13.211111, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 59.1, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.655556, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 63.3, 13.055556, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 67.344444, 13.055556, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 69.833333, 13.055556, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 71.7, 13.055556, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 73.411111, 13.211111, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 75.9, 13.366667, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.455556, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78.388889, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.166667, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.633333, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.633333, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.633333, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.788889, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.788889, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 79.944444, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.255556, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.411111, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.877778, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 81.344444, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 81.966667, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.588889, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.366667, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.833333, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.144444, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.455556, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.611111, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.766667, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.611111, 13.522222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.455556, 13.366667, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 84.455556, 13.366667, 1, False, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Rectangle
event(Gdk.EventType.KEY_PRESS, keyval=Gdk.keyval_from_name('grave'), state=268435472, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:RCFChooser').get_window())
# DELETE PREVIOUS EVENT
findWidget('OOF2 Graphics 1').resize(1051, 500)
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(302, 194)
event(Gdk.EventType.BUTTON_PRESS,x= 9.2000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary:constructor:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Edge boundary from nodes']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Boundary:name').delete_text(0, 11)
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
checkpoint OOF.Skeleton.Boundary.Construct
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary',                       'interior', None, 'topleft', 'bottomleft', 'topright',                       'bottomright'])
assert tests.bdyStatusCheck('interior', 'Edge', 14)

# Select more nodes, making a non-sequenceable branched shape
findGfxWindow('Graphics_1').simulateMouse('up', 55.988889, 17.877778, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('down', 55.988889, 17.877778, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 55.988889, 17.877778, 1, True, False)
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint Graphics_1 Node sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Rectangle
event(Gdk.EventType.BUTTON_PRESS,x= 1.8800000000000e+02,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Single_Node']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 55.522222, 18.344444, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 55.522222, 18.344444, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 55.522222, 18.344444, 1, False, True)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
findGfxWindow('Graphics_1').simulateMouse('down', 56.455556, 21.455556, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 56.611111, 21.455556, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 56.611111, 21.455556, 1, False, True)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
findGfxWindow('Graphics_1').simulateMouse('down', 58.633333, 25.966667, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 58.633333, 25.811111, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 58.633333, 25.811111, 1, False, True)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
# Try to create a boundary from the non-sequenceable nodes
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(313, 194)
assert tests.newBdyOK(False)
assert tests.directionCheck('nodes', ['No edge sequence'])

findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_CANCEL').clicked()
# Undo the selection and make a different sort of non-sequenceable set
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Undo').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Undo').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Undo').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Undo
findGfxWindow('Graphics_1').simulateMouse('down', 80.722222, 17.722222, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 80.722222, 17.722222, 1, True, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
findGfxWindow('Graphics_1').simulateMouse('down', 83.211111, 17.566667, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 83.211111, 17.566667, 1, True, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
# Try to make a boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(313, 194)
assert tests.newBdyOK(False)
assert tests.directionCheck('nodes', ['No edge sequence'])

findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_CANCEL').clicked()
# Undo the latest selections and select nodes that aren't connected to the rest of the selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Undo').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Undo').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Undo
findGfxWindow('Graphics_1').simulateMouse('up', 90.055556, 25.5, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('down', 89.744444, 25.811111, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 89.744444, 25.811111, 1, True, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(313, 194)
assert tests.newBdyOK(False)
assert tests.directionCheck('nodes', ['No edge sequence'])

# Select nodes that connect the isolated node to the rest sequenceably.
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_CANCEL').clicked()
findGfxWindow('Graphics_1').simulateMouse('down', 82.9, 25.188889, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 82.9, 25.188889, 1, True, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
findGfxWindow('Graphics_1').simulateMouse('down', 84.766667, 21.144444, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.766667, 20.988889, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 84.766667, 20.988889, 1, True, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
findGfxWindow('Graphics_1').simulateMouse('down', 83.055556, 19.744444, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 83.055556, 19.433333, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 83.055556, 19.433333, 1, True, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
findGfxWindow('Graphics_1').simulateMouse('down', 82.744444, 17.722222, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.744444, 17.722222, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 82.744444, 17.722222, 1, True, False)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(286, 194)
assert tests.newBdyOK(True)
assert tests.directionCheck('nodes', ['Left to right', 'Right to left', 'Top to bottom', 'Bottom to top'])

findWidget('Dialog-New Boundary').resize(286, 194)
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Construct
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary',                       'interior', 'interior<2>', None, 'topleft',                       'bottomleft', 'topright', 'bottomright'])
assert tests.selectedBdy('interior<2>')

# Delete the new boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Delete').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint OOF.Skeleton.Boundary.Delete
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary',                       'interior', None, 'topleft', 'bottomleft', 'topright',                       'bottomright'])
assert tests.selectedBdy(None)

# Create a point boundary from the selected nodes
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(286, 194)
event(Gdk.EventType.BUTTON_PRESS,x= 6.3000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-New Boundary:constructor:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Point boundary from nodes']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Construct
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary',                       'interior', None, 'topleft', 'bottomleft', 'topright',                       'bottomright', 'interior<2>'])
assert tests.selectedBdy('interior<2>')
assert tests.bdyStatusCheck('interior<2>', 'Point', 20)

# Delete the point boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Delete').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint OOF.Skeleton.Boundary.Delete
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary',                       'interior', None, 'topleft', 'bottomleft', 'topright',                       'bottomright'])
assert tests.selectedBdy(None)

# Unselect two nodes
findGfxWindow('Graphics_1').simulateMouse('up', 83.522222, 17.411111, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('down', 83.366667, 17.566667, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 83.366667, 17.411111, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 83.366667, 17.411111, 1, False, True)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
findGfxWindow('Graphics_1').simulateMouse('down', 82.9, 15.388889, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('move', 82.9, 15.233333, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 82.9, 15.233333, 1, False, True)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
# Create a point boundary from disconnected nodes
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(286, 164)
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Construct
assert tests.bdyStatusCheck('interior<2>', 'Point', 18)

# Delete the new boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Delete').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint OOF.Skeleton.Boundary.Delete
# Select a bunch of segments
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
event(Gdk.EventType.BUTTON_PRESS,x= 1.4200000000000e+02,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Circle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('up', 58.322222, 19.433333, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('down', 49.766667, 29.544444, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 49.766667, 29.544444, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 49.766667, 29.544444, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 49.922222, 29.233333, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.233333, 29.077778, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.388889, 28.922222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.544444, 28.766667, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.855556, 28.455556, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 51.166667, 28.144444, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 51.633333, 27.677778, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.411111, 27.055556, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 53.033333, 26.433333, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 53.655556, 25.966667, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 54.433333, 25.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.055556, 24.877778, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.988889, 24.255556, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.611111, 23.633333, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.766667, 23.322222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 57.077778, 23.011111, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 57.544444, 22.855556, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 57.7, 22.544444, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.011111, 22.388889, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.011111, 22.388889, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.011111, 22.233333, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.011111, 22.233333, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.011111, 22.233333, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.166667, 22.077778, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.166667, 22.077778, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.166667, 22.077778, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.166667, 22.077778, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.166667, 22.077778, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.322222, 21.922222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.477778, 21.922222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.477778, 21.922222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.477778, 21.922222, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.633333, 21.766667, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.633333, 21.766667, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 58.633333, 21.766667, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page updated
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Circle
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(286, 164)
event(Gdk.EventType.BUTTON_PRESS,x= 1.0400000000000e+02,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary:constructor:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Edge boundary from segments']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Boundary').resize(313, 194)
# Check that OK is not active
event(Gdk.EventType.BUTTON_PRESS,x= 1.2600000000000e+02,y= 5.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-New Boundary:constructor:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Point boundary from segments']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Construct
assert tests.bdyStatusCheck('interior<2>', 'Point', 32)
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary',                       'interior', None, 'topleft', 'bottomleft', 'topright',                       'bottomright', 'interior<2>'])
assert tests.selectedBdy('interior<2>')

findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Delete').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint OOF.Skeleton.Boundary.Delete
# Try to create a point boundary from elements although no elements are selected
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(305, 164)
event(Gdk.EventType.BUTTON_PRESS,x= 5.6000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-New Boundary:constructor:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Point boundary from elements']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Construct
# FIX THE COMMENT there were elements selected
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.6482840236686e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 2.6927810650888e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.6938461538462e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.3463905325444e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.1075147928994e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 9.5550295857988e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 9.7721893491124e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 9.9893491124260e+01)
assert tests.bdyStatusCheck('interior<2>', 'Point', 38)

findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Delete').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint OOF.Skeleton.Boundary.Delete
# Create a point boundary from an element group
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(302, 164)
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary:constructor:Point boundary from elements:group').get_window())
checkpoint toplevel widget mapped chooserPopup-group
findMenu(findWidget('chooserPopup-group'), ['red spot']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-group') # MenuItemLogger
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Construct
assert tests.bdyStatusCheck('interior<2>', 'Point', 38)

# Rename a boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Rename').clicked()
checkpoint toplevel widget mapped Dialog-New name for this boundary
findWidget('Dialog-New name for this boundary').resize(192, 92)
findWidget('Dialog-New name for this boundary:name').set_text('')
findWidget('Dialog-New name for this boundary:name').set_text('b')
findWidget('Dialog-New name for this boundary:name').set_text('bi')
findWidget('Dialog-New name for this boundary:name').set_text('big')
findWidget('Dialog-New name for this boundary:name').set_text('big ')
findWidget('Dialog-New name for this boundary:name').set_text('big r')
findWidget('Dialog-New name for this boundary:name').set_text('big re')
findWidget('Dialog-New name for this boundary:name').set_text('big red')
findWidget('Dialog-New name for this boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Rename
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary',                       'interior', None, 'topleft', 'bottomleft', 'topright',                       'bottomright', 'big red'])
assert tests.selectedBdy('big red')
assert tests.bdyStatusCheck('big red', 'Point', 38)

# Create a new Skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 5.4000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
checkpoint skeleton page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint skeleton selection page updated
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
event(Gdk.EventType.BUTTON_PRESS,x= 8.3000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Boundaries']).activate() # MenuItemLogger
checkpoint page installed Skeleton Boundaries
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary',                        'interior', None, 'topleft', 'bottomleft', 'topright',                       'bottomright', 'big red'])
assert tests.selectedBdy('big red')

# Switch to the new Skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Boundaries Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
checkpoint boundary page updated
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
assert tests.bdyNames(['top', 'bottom', 'right', 'left', None, 'topleft',                       'bottomleft', 'topright', 'bottomright'])
assert tests.selectedBdy(None)
assert tests.bdyStatusNoBdy()

# Switch back to the old Skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 4.5000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Boundaries Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
checkpoint boundary page updated
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary', 'interior', None, 'topleft', 'bottomleft', 'topright', 'bottomright', 'big red'])
assert tests.selectedBdy('big red')

# Delete a pre-defined boundary
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([7]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
assert tests.bdyStatusCheck('topleft', 'Point', 1)

findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Delete').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint boundary page updated
checkpoint OOF.Skeleton.Boundary.Delete
assert tests.bdyStatusNoBdy()
assert tests.bdyNames(['top', 'right', 'bottom', 'left', 'boundary', 'interior', None, 'bottomleft', 'topright', 'bottomright', 'big red'])

findWidget('OOF2').resize(782, 545)
# Delete the first skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 8.6000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 6.3000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Skeleton').get_window())
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
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
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
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Segment
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized Segment
checkpoint Solver page sensitized
checkpoint skeleton page info updated
checkpoint skeleton selection page groups sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint skeleton selection page updated
checkpoint Field page sensitized
checkpoint skeleton page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.Delete
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Boundaries']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton Boundaries
assert tests.bdyNames(['top', 'bottom', 'right', 'left', None, 'topleft',                       'bottomleft', 'topright', 'bottomright'])
assert tests.selectedBdy(None)
assert tests.bdyStatusNoBdy()

# Delete the new skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 1.6000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Segment
checkpoint skeleton selection page selection sensitized Segment
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Segment
checkpoint skeleton selection page groups sensitized Segment
checkpoint skeleton page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.Delete
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 2.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Boundaries']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton Boundaries
assert tests.bdyNames([])
assert tests.bdyStatusEmpty()
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
assert tests.filediff("session.log")

findGfxWindow('Graphics_1').simulateMouse('up', 39.208333, 81.791667, 1, False, False)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
