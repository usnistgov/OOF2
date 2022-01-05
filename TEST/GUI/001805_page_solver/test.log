 # -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Test the handling of time dependent boundary conditions in the Solver page.

# TODO: Check the contents of the Initialization GtkTreeView.  I don't
# know how to verify that a given row and column of a tree view
# contains a given string.

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 6.3000000000000e+01,y= 2.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
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
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.New
event(Gdk.EventType.BUTTON_PRESS,x= 3.5000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(235, 122)
event(Gdk.EventType.BUTTON_PRESS,x= 5.4000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-Assign material material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['<every>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Material.Assign
getTree("PropertyTree").simulateSelect(Gtk.TreePath([0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 1.4000000000000e+01,y= 2.8000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 1.1000000000000e+01,y= 2.8000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 2.8000000000000e+01,y= 4.7000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 0, 0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 8.1000000000000e+01,y= 6.6000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 4]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 2.7000000000000e+01,y= 1.7000000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([1, 4, 0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 8.1000000000000e+01,y= 1.8600000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([2]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 1.0000000000000e+01,y= 2.4300000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([2, 0]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 3.2000000000000e+01,y= 2.6200000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([2, 0, 0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 8.4000000000000e+01,y= 2.8600000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([2, 1]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 2.5000000000000e+01,y= 3.1700000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree("PropertyTree").simulateSelect(Gtk.TreePath([2, 1, 0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 9.6000000000000e+01,y= 3.3500000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
event(Gdk.EventType.BUTTON_PRESS,x= 9.6000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
event(Gdk.EventType.BUTTON_PRESS,x= 4.7000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature in-plane').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Field.In_Plane
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
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Heat_Eqn active').clicked()
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

# Check that the right fields are listed in the Initialization pane.
event(Gdk.EventType.BUTTON_PRESS,x= 7.2000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2:Solver Page:VPane').set_position(170)
assert tests.checkInitializees("Temperature", "Displacement")

event(Gdk.EventType.BUTTON_PRESS,x= 5.4000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Boundary Conditions
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 330)
event(Gdk.EventType.BUTTON_PRESS,x= 7.9000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Floating']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:name').insert_text('f', 9)
findWidget('Dialog-New Boundary Condition:name').insert_text('l', 1)
findWidget('Dialog-New Boundary Condition:name').insert_text('o', 2)
findWidget('Dialog-New Boundary Condition:name').insert_text('a', 3)
findWidget('Dialog-New Boundary Condition:name').insert_text('t', 4)
findWidget('Dialog-New Boundary Condition:name').insert_text('t', 5)
findWidget('Dialog-New Boundary Condition:name').insert_text('e', 6)
findWidget('Dialog-New Boundary Condition:name').insert_text('m', 7)
findWidget('Dialog-New Boundary Condition:name').insert_text('p', 8)
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_APPLY').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
findWidget('Dialog-New Boundary Condition:name').delete_text(8, 9)
findWidget('Dialog-New Boundary Condition:name').delete_text(7, 8)
findWidget('Dialog-New Boundary Condition:name').delete_text(6, 7)
findWidget('Dialog-New Boundary Condition:name').delete_text(5, 6)
findWidget('Dialog-New Boundary Condition:name').insert_text('d', 5)
findWidget('Dialog-New Boundary Condition:name').insert_text('i', 6)
findWidget('Dialog-New Boundary Condition:name').insert_text('s', 7)
findWidget('Dialog-New Boundary Condition:name').insert_text('p', 8)
event(Gdk.EventType.BUTTON_PRESS,x= 7.3000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Floating:field').get_window())
checkpoint toplevel widget mapped chooserPopup-field
findMenu(findWidget('chooserPopup-field'), ['Displacement']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field') # MenuItemLogger
findWidget('Dialog-New Boundary Condition').resize(353, 346)
event(Gdk.EventType.BUTTON_PRESS,x= 7.5000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Floating:equation').get_window())
checkpoint toplevel widget mapped chooserPopup-equation
findMenu(findWidget('chooserPopup-equation'), ['Force_Balance']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-equation') # MenuItemLogger
findWidget('Dialog-New Boundary Condition').resize(353, 362)
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
event(Gdk.EventType.BUTTON_PRESS,x= 6.6000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.checkInitializees("Temperature","Displacement", "floattemp", "floatdisp")

# Static solver
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

# Check that fields can be initialized, but not time derivs.
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.6000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path(Gtk.TreePath([3]))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Set').clicked()
checkpoint toplevel widget mapped Dialog-Initialize BC floatdisp
findWidget('Dialog-Initialize BC floatdisp').resize(232, 134)
# Check that value can be set but not time_derivative.
assert not tests.time_deriv_settable('floatdisp')
assert tests.value_settable('floatdisp')
# Check that initializer options are Minimum, Maximum, Average
assert tests.optionsCheck('floatdisp')
assert tests.checkInitializees("Temperature", "Displacement", "floattemp", "floatdisp")

findWidget('Dialog-Initialize BC floatdisp:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Set_BC_Initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 8.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 9.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.4000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.6000000000000e+01)
# Check that floatdisp initializer is displayed correctly (min=0).

# Set the temperature initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path(Gtk.TreePath([2]))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(1)
tree.row_activated(Gtk.TreePath([2]), column)
checkpoint toplevel widget mapped Dialog-Initialize BC floattemp
findWidget('Dialog-Initialize BC floattemp').resize(232, 134)
# Check that value can be set, but not time_derivative.
assert tests.value_settable('floattemp')
assert not tests.time_deriv_settable('floattemp')
# Check that correct initializers are listed.
assert tests.optionsCheck('floattemp')

findWidget('Dialog-Initialize BC floattemp:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Set_BC_Initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 8.0000000000000e+00)
# Check that floattemp initializer is min=0.

# Switch to time dependent solver.
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([0]), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(414, 253)
event(Gdk.EventType.BUTTON_PRESS,x= 4.3000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-Specify Solver:solver_mode:Basic:time_stepper:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Adaptive']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Specify Solver').resize(414, 326)
findWidget('Dialog-Specify Solver:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
# Check that Displacement_t is now listed in the initialization pane
assert tests.checkInitializees("Temperature", "Displacement", "Displacement_t", 'floattemp', 'floatdisp')

# Check that time_derivative can be set for floatdisp bc
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 9.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.2000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 3.5000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 3.6000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 3.7000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 4.4000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path(Gtk.TreePath([4]))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(1)
tree.row_activated(Gtk.TreePath([4]), column)
checkpoint toplevel widget mapped Dialog-Initialize BC floatdisp
findWidget('Dialog-Initialize BC floatdisp').resize(284, 170)
assert tests.time_deriv_settable('floatdisp')
assert tests.value_settable('floatdisp')

findWidget('Dialog-Initialize BC floatdisp:initializer:Minimum:time_derivative').set_text('0.')
findWidget('Dialog-Initialize BC floatdisp:initializer:Minimum:time_derivative').set_text('0.1')
findWidget('Dialog-Initialize BC floatdisp:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Set_BC_Initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 8.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 9.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.4000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 4.4000000000000e+01)
# Check that initializer listed for floatdisp is min=0, time_derivative=0.1

# Check that time_derivative isn't settable for floattemp.
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path(Gtk.TreePath([3]))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(1)
tree.row_activated(Gtk.TreePath([3]), column)
checkpoint toplevel widget mapped Dialog-Initialize BC floattemp
findWidget('Dialog-Initialize BC floattemp').resize(232, 134)
assert not tests.time_deriv_settable('floattemp')
assert tests.value_settable('floattemp')

findWidget('Dialog-Initialize BC floattemp:initializer:Minimum:value').set_text('0.')
findWidget('Dialog-Initialize BC floattemp:initializer:Minimum:value').set_text('0.2')
findWidget('Dialog-Initialize BC floattemp:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Set_BC_Initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 8.0000000000000e+00)
# Check that initializer for floattemp is min=0.2

# Clear the floattemp bc initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 9.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 3.4000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 4.4000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Clear').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Clear_BC_Initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 8.0000000000000e+00)
# Check that floattemp initializer has been cleared.

# Clear all initializers
findWidget('OOF2:Solver Page:VPane:FieldInit:ClearAll').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Clear_Field_Initializers
# Check that all initializers have been cleared.

# Remove the mass density property.
event(Gdk.EventType.BUTTON_PRESS,x= 7.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint property selected
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Material:RemoveProperty').clicked()
checkpoint Materials page updated
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Material.Remove_property
event(Gdk.EventType.BUTTON_PRESS,x= 5.0000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver

# Check that the time derivative of floatdisp isn't settable.
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 9.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.4000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.6000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path(Gtk.TreePath([3]))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Set').clicked()
checkpoint toplevel widget mapped Dialog-Initialize BC floatdisp
findWidget('Dialog-Initialize BC floatdisp').resize(232, 134)
assert not tests.time_deriv_settable('floatdisp')
assert tests.value_settable('floatdisp')
assert tests.checkInitializees('Temperature', 'Displacement', 'floattemp', 'floatdisp')

findWidget('Dialog-Initialize BC floatdisp:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Set_BC_Initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 8.0000000000000e+00)
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
assert tests.filediff('session.log')

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
