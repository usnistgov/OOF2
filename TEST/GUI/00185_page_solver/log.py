# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.1 $
# $Author: langer $
# $Date: 2011/06/08 19:04:52 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import tests

setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
checkpoint page installed Microstructure
findWidget('OOF2').resize(577, 350)
findWidget('OOF2:Microstructure Page:Pane').set_position(159)
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(315, 161)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(164)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint active area status updated
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint named boundary analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint mesh bdy page updated
checkpoint meshable button set
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2').resize(685, 350)
findWidget('OOF2:Materials Page:Pane').set_position(274)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((0,))
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1,), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 0, 0))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
widget_0=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_0.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_0.window))
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(301, 96)
findWidget('Dialog-New material:gtk-ok').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(304, 104)
setComboBox(findWidget('Dialog-Assign material material to pixels:pixels'), '<every>')
findWidget('Dialog-Assign material material to pixels:gtk-ok').clicked()
checkpoint OOF.Material.Assign
findWidget('OOF2 Messages 1').resize(723, 200)
findWidget('OOF2 Messages 1').resize(731, 200)
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.9839513369337e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.9679026738675e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 3), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.9000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 3, 0))
checkpoint Materials page updated
checkpoint property deselected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.7000000000000e+01)
checkpoint Materials page updated
checkpoint property selected
widget_1=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_1.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_1.window))
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.7160486630663e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.3209732613251e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().unselect_all()
checkpoint Materials page updated
checkpoint property deselected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').collapse_row((1,))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((2,), open_all=False)
widget_2=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_2.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_2.window))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((2, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((2, 0, 0))
checkpoint Materials page updated
checkpoint property selected
widget_3=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_3.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_3.window))
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.9839513369337e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.9679026738675e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((2, 1), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.9000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((2, 1, 0))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
widget_4=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_4.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_4.window))
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 1.6000000000000e+01)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2').resize(705, 424)
findWidget('OOF2:Skeleton Page:Pane').set_position(324)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(394, 196)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint skeleton page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton selection page grouplist
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.New
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton Selection')
checkpoint skeleton selection page grouplist
checkpoint page installed Skeleton Selection
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(317)
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane').set_position(413)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(345, 208)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint mesh bdy page updated
checkpoint named boundary analysis chooser set
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Fields & Equations')
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2').resize(773, 424)
findWidget('OOF2:Fields & Equations Page:HPane').set_position(343)
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature in-plane').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Field.In_Plane
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement in-plane').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Field.In_Plane
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Heat_Eqn active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Force_Balance active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Activate

# Check that the right fields are listed in the Initialization pane.
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.checkInitializees("Temperature", "Displacement")

setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Boundary Conditions')
checkpoint page installed Boundary Conditions
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(441, 265)
setComboBox(findWidget('Dialog-New Boundary Condition:condition:Chooser'), 'Floating')
findWidget('Dialog-New Boundary Condition:name:Auto').clicked()
findWidget('Dialog-New Boundary Condition:name:Text').set_text('t')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('tl')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('tlo')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('tl')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('t')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('f')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('fl')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('flo')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('floa')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('float')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('floatt')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('floatte')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('floattem')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('floattemp')
findWidget('Dialog-New Boundary Condition:gtk-apply').clicked()
findWidget('OOF2 Messages 1').resize(795, 200)
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
findWidget('Dialog-New Boundary Condition:name:Text').set_text('floattem')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('floatte')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('floatt')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('float')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('floatd')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('floatdi')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('floatdis')
findWidget('Dialog-New Boundary Condition:name:Text').set_text('floatdisp')
setComboBox(findWidget('Dialog-New Boundary Condition:condition:Floating:field'), 'Displacement')
findWidget('Dialog-New Boundary Condition').resize(441, 277)
setComboBox(findWidget('Dialog-New Boundary Condition:condition:Floating:equation'), 'Force_Balance')
findWidget('Dialog-New Boundary Condition').resize(441, 289)
findWidget('Dialog-New Boundary Condition:gtk-ok').clicked()
checkpoint named analysis chooser set
checkpoint named analysis chooser set
findWidget('OOF2 Messages 1').resize(859, 200)
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.checkInitializees("Temperature","Displacement", "floattemp", "floatdisp")
findWidget('OOF2').resize(773, 488)
findWidget('OOF2:Solver Page:VPane').set_position(157)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.2651489979526e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.5302979959052e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 3.7954469938579e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 4.7000000000000e+01)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((0,))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(3)
tree.row_activated((0,), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(475, 185)
findWidget('Dialog-Specify Solver:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
# Static solver.   Check that fields can be initialized, but not time derivs.
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((3,))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Set').clicked()
checkpoint toplevel widget mapped Dialog-Initialize BC floatdisp
findWidget('Dialog-Initialize BC floatdisp').resize(263, 100)
# Check that value can be set but not time_derivative.
assert not tests.time_deriv_settable('floatdisp')
assert tests.value_settable('floatdisp')
# Check that initializer options are Minimum, Maximum, Average
assert tests.optionsCheck('floatdisp')
assert tests.checkInitializees("Temperature", "Displacement", "floattemp", "floatdisp")

findWidget('Dialog-Initialize BC floatdisp:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((3,))
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Set_BC_Initializer
# TODO: Check that floatdisp initializer is displayed correctly
# (min=0).  I don't know how to do this.
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((2,))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 4.6000000000000e+01)
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(1)
tree.row_activated((2,), column)
checkpoint toplevel widget mapped Dialog-Initialize BC floattemp
findWidget('Dialog-Initialize BC floattemp').resize(263, 100)
# Check that value can be set, but not time_derivative.
assert tests.value_settable('floattemp')
assert not tests.time_deriv_settable('floattemp')
# Check that correct initializers are listed.
assert tests.optionsCheck('floattemp')
findWidget('Dialog-Initialize BC floattemp:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((2,))
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Set_BC_Initializer
# TODO: Check that floattemp initializer is min=0. How?
# Switch to time dependent solver.
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(3)
tree.row_activated((0,), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(475, 185)
setComboBox(findWidget('Dialog-Specify Solver:solver_mode:Basic:time_stepper:Chooser'), 'Adaptive')
findWidget('Dialog-Specify Solver').resize(475, 231)
findWidget('Dialog-Specify Solver:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((3,))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
# Check that Displacement_t is now listed in the initialization pane
assert tests.checkInitializees("Temperature", "Displacement", "Displacement_t", 'floattemp', 'floatdisp')
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 5.8651489979526e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 7.0000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((4,))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(1)
tree.row_activated((4,), column)
checkpoint toplevel widget mapped Dialog-Initialize BC floatdisp
findWidget('Dialog-Initialize BC floatdisp').resize(323, 123)
# Check that time_derivative can be set for floatdisp bc
assert tests.time_deriv_settable('floatdisp')
assert tests.value_settable('floatdisp')
findWidget('Dialog-Initialize BC floatdisp:initializer:Minimum:time_derivative').set_text('0.')
findWidget('Dialog-Initialize BC floatdisp:initializer:Minimum:time_derivative').set_text('0.1')
findWidget('Dialog-Initialize BC floatdisp:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((4,))
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Set_BC_Initializer
# TODO: Check that initializer listed for floatdisp is min=0,
# time_derivative=0.1 How?
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((3,))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 6.9000000000000e+01)
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(1)
tree.row_activated((3,), column)
checkpoint toplevel widget mapped Dialog-Initialize BC floattemp
findWidget('Dialog-Initialize BC floattemp').resize(263, 100)
# Check that time_derivative isn't settable for floattemp.
assert not tests.time_deriv_settable('floattemp')
assert tests.value_settable('floattemp')
findWidget('Dialog-Initialize BC floattemp:initializer:Minimum:value').set_text('0.')
findWidget('Dialog-Initialize BC floattemp:initializer:Minimum:value').set_text('0.2')
findWidget('Dialog-Initialize BC floattemp:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((3,))
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Set_BC_Initializer
# TODO: Check that initializer for floattemp is min=0.2
findWidget('OOF2:Solver Page:VPane:FieldInit:Clear').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((3,))
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Clear_BC_Initializer
# TODO: Check that floattemp initializer has been cleared.
findWidget('OOF2:Solver Page:VPane:FieldInit:ClearAll').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Clear_Field_Initializers
# TODO: Check that all initializers have been cleared.

# Remove the mass density property.
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2').resize(685, 488)
findWidget('OOF2:Materials Page:Pane').set_position(274)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList').get_selection().select_path((1,))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0700000000000e+02)
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Material:RemoveProperty').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Material.Remove_property
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((3,))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(1)
tree.row_activated((3,), column)
checkpoint toplevel widget mapped Dialog-Initialize BC floatdisp
findWidget('Dialog-Initialize BC floatdisp').resize(263, 100)
# Check that the time derivative of floatdisp isn't settable.
assert not tests.time_deriv_settable('floatdisp')
assert tests.value_settable('floatdisp')
assert tests.checkInitializees('Temperature', 'Displacement', 'floattemp', 'floatdisp')
findWidget('Dialog-Initialize BC floatdisp:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((3,))
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Set_BC_Initializer
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(191, 96)
findWidget('Dialog-Python_Log:filename').set_text('t')
findWidget('Dialog-Python_Log:filename').set_text('td')
findWidget('Dialog-Python_Log:filename').set_text('tdb')
findWidget('Dialog-Python_Log:filename').set_text('tdbc')
findWidget('Dialog-Python_Log:filename').set_text('tdbc.')
findWidget('Dialog-Python_Log:filename').set_text('tdbc.l')
findWidget('Dialog-Python_Log:filename').set_text('tdbc.lo')
findWidget('Dialog-Python_Log:filename').set_text('tdbc.log')
findWidget('Dialog-Python_Log').resize(211, 96)
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('tdbc.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
