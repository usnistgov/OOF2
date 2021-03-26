# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Tests for the Boundary Analysis page

import tests
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 545)

# Create a Microstructure
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
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.New

# Create a Material with an elastic modulus and assign it to all pixels
event(Gdk.EventType.BUTTON_PRESS,x= 9.7000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New
getTree("PropertyTree").simulateSelect(Gtk.TreePath([0]))
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 9.0000000000000e+00,y= 2.8000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 3.1000000000000e+01,y= 4.3000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 0, 0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 8.2000000000000e+01,y= 6.0000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(235, 122)
event(Gdk.EventType.BUTTON_PRESS,x= 5.8000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-Assign material material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['<every>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Material.Assign

# Create a 10x10 Skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 8.0000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton page info updated
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.New
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton page info updated
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized

# Create a Mesh
event(Gdk.EventType.BUTTON_PRESS,x= 8.4000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(130)
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
checkpoint OOF.Mesh.New

# Go to the Boundary Analyis page
event(Gdk.EventType.BUTTON_PRESS,x= 5.8000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(256)
assert tests.goSensitive(0)
assert tests.bdyList("top", "bottom", "right", "left")

# Define some fields
event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane').set_position(470)
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
checkpoint OOF.Subproblem.Field.Define
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
checkpoint OOF.Subproblem.Field.Define

# Initialize the temperature field
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2:Solver Page:VPane').set_position(170)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Set').clicked()
checkpoint toplevel widget mapped Dialog-Initialize field Temperature
findWidget('Dialog-Initialize field Temperature').resize(232, 134)
event(Gdk.EventType.BUTTON_PRESS,x= 7.9000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-Initialize field Temperature:initializer:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['XYTFunction']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Initialize field Temperature').resize(245, 134)
findWidget('Dialog-Initialize field Temperature:initializer:XYTFunction:function').set_text('x')
findWidget('Dialog-Initialize field Temperature:initializer:XYTFunction:function').set_text('x*')
findWidget('Dialog-Initialize field Temperature:initializer:XYTFunction:function').set_text('x*y')
findWidget('Dialog-Initialize field Temperature:initializer:XYTFunction:function').set_text('x*y*')
findWidget('Dialog-Initialize field Temperature:initializer:XYTFunction:function').set_text('x*y*y')
findWidget('Dialog-Initialize field Temperature:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Set_Field_Initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Apply').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Apply_Field_Initializers

# Evaluate the average temperature on the boundaries
event(Gdk.EventType.BUTTON_PRESS,x= 8.1000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(211)
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([0]))
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().unselect_all()
assert tests.goSensitive(0)

findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([0]))
assert tests.goSensitive(1)

findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0.0, 0.5)

# bottom
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([1]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0.0, 0.0)

# left
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([3]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0.0, 0.0)

# right
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([2]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0.0, 0.335)

# Compute average displacement on the boundaries (they're all zero)
event(Gdk.EventType.BUTTON_PRESS,x= 4.6000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Analysis Page:Pane:BdyAnalyzerRCF:Average Field:field').get_window())
checkpoint toplevel widget mapped chooserPopup-field
findMenu(findWidget('chooserPopup-field'), ['Displacement']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field') # MenuItemLogger
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(208)
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([0]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0, 0, 0)

findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([1]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0, 0, 0)

findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([2]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0, 0, 0)

findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([3]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0, 0, 0)

# Activate the displacement field
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement in-plane').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Field.In_Plane

event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
assert tests.goSensitive(1)

# findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([0]))
# findWidget('OOF2:Boundary Analysis Page:Go').clicked()
# checkpoint OOF.Mesh.Boundary_Analysis.Analyze
# assert tests.msgFloat(0, 0, 0)

# findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([1]))
# findWidget('OOF2:Boundary Analysis Page:Go').clicked()
# checkpoint OOF.Mesh.Boundary_Analysis.Analyze
# assert tests.msgFloat(0, 0, 0)

# findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([2]))
# findWidget('OOF2:Boundary Analysis Page:Go').clicked()
# checkpoint OOF.Mesh.Boundary_Analysis.Analyze
# assert tests.msgFloat(0, 0, 0)

# findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([3]))
# findWidget('OOF2:Boundary Analysis Page:Go').clicked()
# checkpoint OOF.Mesh.Boundary_Analysis.Analyze
# assert tests.msgFloat(0, 0, 0)

# Assign boundary conditions
event(Gdk.EventType.BUTTON_PRESS,x= 1.3500000000000e+02,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Analysis Page:Pane:BdyAnalyzerRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Integrate Flux']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(258)
assert tests.goSensitive(0)

event(Gdk.EventType.BUTTON_PRESS,x= 7.4000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Force_Balance active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Activate
event(Gdk.EventType.BUTTON_PRESS,x= 8.2000000000000e+01,y= 2.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(250)
assert tests.goSensitive(1)

# Integrate stress fluxes (will all be zero)
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([0]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0, 0, 0)

findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([1]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0, 0, 0)

findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([2]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0, 0, 0)

findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([3]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0, 0, 0)

# Set boundary conditions on displacement
event(Gdk.EventType.BUTTON_PRESS,x= 4.1000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Boundary Conditions
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 346)
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field').get_window())
checkpoint toplevel widget mapped chooserPopup-field
findMenu(findWidget('chooserPopup-field'), ['Displacement']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field') # MenuItemLogger
findWidget('Dialog-New Boundary Condition').resize(353, 362)
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Continuum Profile']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Boundary Condition').resize(407, 434)
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('')
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('1')
event(Gdk.EventType.BUTTON_PRESS,x= 5.5000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
checkpoint toplevel widget mapped chooserPopup-boundary
findMenu(findWidget('chooserPopup-boundary'), ['left']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-boundary') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_APPLY').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
event(Gdk.EventType.BUTTON_PRESS,x= 5.1000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component').get_window())
checkpoint toplevel widget mapped chooserPopup-field_component
findMenu(findWidget('chooserPopup-field_component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field_component') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 5.8000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component').get_window())
checkpoint toplevel widget mapped chooserPopup-eqn_component
findMenu(findWidget('chooserPopup-eqn_component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-eqn_component') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_APPLY').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
event(Gdk.EventType.BUTTON_PRESS,x= 7.8000000000000e+01,y= 6.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
checkpoint toplevel widget mapped chooserPopup-boundary
findMenu(findWidget('chooserPopup-boundary'), ['right']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-boundary') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_APPLY').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
event(Gdk.EventType.BUTTON_PRESS,x= 7.5000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component').get_window())
checkpoint toplevel widget mapped chooserPopup-eqn_component
findMenu(findWidget('chooserPopup-eqn_component'), ['x']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-eqn_component') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 6.9000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component').get_window())
checkpoint toplevel widget mapped chooserPopup-field_component
findMenu(findWidget('chooserPopup-field_component'), ['x']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field_component') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('')
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('0')
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('0.')
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('0.1')
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New

# Solve
event(Gdk.EventType.BUTTON_PRESS,x= 7.9000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([0]), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(414, 253)
findWidget('Dialog-Specify Solver:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:end').set_text('0.0')
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Solve
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Settings.Graphics_Defaults.New_Layer_Policy
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
findWidget('OOF2 Graphics 1').resize(800, 492)

# Oops.  Fix the boundary conditions
event(Gdk.EventType.BUTTON_PRESS,x= 5.1000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Boundary Conditions
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([0]))
tree=findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([0]), column)
checkpoint toplevel widget mapped Dialog-Edit Boundary Condition
findWidget('Dialog-Edit Boundary Condition').resize(407, 398)
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('0')
findWidget('Dialog-Edit Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
tree=findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([1]), column)
checkpoint toplevel widget mapped Dialog-Edit Boundary Condition
findWidget('Dialog-Edit Boundary Condition').resize(407, 398)
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Edit
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('0')
findWidget('Dialog-Edit Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Edit
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([2]))
tree=findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([2]), column)
checkpoint toplevel widget mapped Dialog-Edit Boundary Condition
findWidget('Dialog-Edit Boundary Condition').resize(407, 398)
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('0')
findWidget('Dialog-Edit Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Edit

# Re-solve
event(Gdk.EventType.BUTTON_PRESS,x= 1.1800000000000e+02,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Solve
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer:Zoom:Fill').clicked()
checkpoint OOF.Graphics_1.Settings.Zoom.Fill_Window

# Integrate the flux again
event(Gdk.EventType.BUTTON_PRESS,x= 8.0000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([0]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
findWidget('OOF2 Graphics 1').resize(800, 492)
assert tests.msgFloat(0.0, 0.0, 0.00620165904187)
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([1]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0.0, 0.0, -0.00620165904187)
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([2]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0.0, 0.0878255288986, 0.0)
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([3]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0.0, -0.0878255288986, 0.0)

# Change poisson's ratio to 0
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
event(Gdk.EventType.BUTTON_RELEASE,x= 1.0400000000000e+02,y= 6.2000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic').resize(538, 330)
event(Gdk.EventType.BUTTON_PRESS,x= 1.1900000000000e+02,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['E and nu']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:E and nu:poisson').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:E and nu:poisson').set_text('0.0')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic

# Solve again
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Solve

# Check integrated fluxes again
event(Gdk.EventType.BUTTON_PRESS,x= 7.5000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([0]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0, 0, 0)

findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([3]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0, -0.06666666666666736, 0)

findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([2]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0, 0.066666666666669996, 0)

findWidget('OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([1]))
findWidget('OOF2:Boundary Analysis Page:Go').clicked()
checkpoint OOF.Mesh.Boundary_Analysis.Analyze
assert tests.msgFloat(0, 0, 0)

# Undefine the fields
event(Gdk.EventType.BUTTON_PRESS,x= 5.2000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
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
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Subproblem.Field.Undefine
event(Gdk.EventType.BUTTON_PRESS,x= 6.9000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
assert tests.goSensitive(1)

# Deactivate the equation
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Force_Balance active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Deactivate
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint mesh bdy page updated
checkpoint page installed Boundary Analysis
findWidget('OOF2:Boundary Analysis Page:Pane').set_position(258)
assert tests.goSensitive(0)

# Delete the mesh
event(Gdk.EventType.BUTTON_PRESS,x= 1.0200000000000e+02,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(277, 86)
findWidget('Questioner:Yes').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint Graphics_1 Mesh Info cleared position
checkpoint Graphics_1 Mesh Info sensitized
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
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Delete

findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Boundary Analysis
checkpoint mesh bdy page updated
assert tests.bdyList()
assert tests.goSensitive(0)

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
assert tests.filediff("session.log")

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
