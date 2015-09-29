checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.12 $
# $Author: langer $
# $Date: 2010/12/26 05:03:22 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2').resize(550, 484)
findWidget('OOF2:Solver Page:VPane').set_position(152)
assert tests.sensitization0()
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
checkpoint page installed Microstructure
findWidget('OOF2').resize(577, 484)
findWidget('OOF2:Microstructure Page:Pane').set_position(159)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
checkpoint microstructure page sensitized
findWidget('Dialog-Create Microstructure').resize(315, 163)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(164)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint microstructure page sensitized
checkpoint mesh bdy page updated
checkpoint pixel page sensitized
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
# checkpoint interface page updated
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2').resize(705, 484)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane').set_position(324)
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
checkpoint skeleton page sensitized
findWidget('Dialog-New skeleton').resize(394, 198)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
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
checkpoint skeleton page info updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.New
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
findWidget('OOF2:FE Mesh Page:Pane').set_position(463)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(345, 210)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
checkpoint mesh bdy page updated
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
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.sensitization0()
assert tests.listCheck()
assert tests.selection(None)
# Define a field
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Fields & Equations')
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2').resize(773, 484)
findWidget('OOF2:Fields & Equations Page:HPane').set_position(343)
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.sensitization0()
assert tests.selection(None)
assert tests.listCheck('Temperature', 'Temperature_z')
# Select a field
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
assert tests.sensitization1()
assert tests.selection(0)
# Unselect the field
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
assert tests.sensitization0()
assert tests.selection(None)
# Reselect field
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
assert tests.sensitization1()
assert tests.selection(0)
# Assign initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Set').clicked()
checkpoint toplevel widget mapped Dialog-Initialize field Temperature
findWidget('Dialog-Initialize field Temperature').resize(263, 102)
findWidget('Dialog-Initialize field Temperature:initializer:Constant:value').set_text('')
findWidget('Dialog-Initialize field Temperature:initializer:Constant:value').set_text('1')
findWidget('Dialog-Initialize field Temperature:initializer:Constant:value').set_text('12')
findWidget('Dialog-Initialize field Temperature:initializer:Constant:value').set_text('123')
findWidget('Dialog-Initialize field Temperature:initializer:Constant:value').set_text('1233')
findWidget('Dialog-Initialize field Temperature:initializer:Constant:value').set_text('123')
findWidget('Dialog-Initialize field Temperature:gtk-ok').clicked()
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Set_Field_Initializer
checkpoint Solver page sensitized
assert tests.sensitization2()
assert tests.selection(0)
# Remove initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Clear').clicked()
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Clear_Field_Initializer
checkpoint Solver page sensitized
assert tests.sensitization1()
assert tests.selection(0)
# Reassign initializer
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(1)
tree.row_activated((0,), column)
checkpoint toplevel widget mapped Dialog-Initialize field Temperature
findWidget('Dialog-Initialize field Temperature').resize(263, 102)
findWidget('Dialog-Initialize field Temperature:gtk-ok').clicked()
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Set_Field_Initializer
checkpoint Solver page sensitized
assert tests.sensitization2()
assert tests.selection(0)
# Assign second initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((1,))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 6.0000000000000e+00)
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(1)
tree.row_activated((1,), column)
checkpoint toplevel widget mapped Dialog-Initialize field Temperature_z
findWidget('Dialog-Initialize field Temperature_z').resize(263, 102)
setComboBox(findWidget('Dialog-Initialize field Temperature_z:initializer:Chooser'), 'XYTFunction')
findWidget('Dialog-Initialize field Temperature_z').resize(281, 102)
findWidget('Dialog-Initialize field Temperature_z:initializer:XYTFunction:function').set_text('x')
findWidget('Dialog-Initialize field Temperature_z:initializer:XYTFunction:function').set_text('x+')
findWidget('Dialog-Initialize field Temperature_z:initializer:XYTFunction:function').set_text('x+y')
findWidget('Dialog-Initialize field Temperature_z:gtk-ok').clicked()
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((1,))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Set_Field_Initializer
checkpoint Solver page sensitized
assert tests.sensitization2()
assert tests.selection(1)
# Remove first initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Clear').clicked()
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Clear_Field_Initializer
checkpoint Solver page sensitized
assert tests.sensitization3()
assert tests.selection(0)
# Remove all initializers
findWidget('OOF2:Solver Page:VPane:FieldInit:ClearAll').clicked()
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Clear_Field_Initializers
checkpoint Solver page sensitized
assert tests.sensitization1()
assert tests.selection(0)
# Define another field
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Fields & Equations')
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define
checkpoint Solver page sensitized
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement in-plane').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Field.In_Plane
checkpoint Solver page sensitized
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint page installed Solver
checkpoint Solver page sensitized
assert tests.sensitization1()
assert tests.listCheck("Temperature", "Temperature_z", "Displacement")
assert tests.selection(0)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.7058823529412e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 3.4117647058824e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 5.1176470588235e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 6.8235294117647e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 8.5294117647059e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.0235294117647e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.1941176470588e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.3647058823529e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.5352941176471e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.7058823529412e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.8764705882353e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.0470588235294e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.2176470588235e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.3882352941176e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.5588235294118e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.7294117647059e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.9000000000000e+01)
# Select new field
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((2,))
checkpoint Solver page sensitized
assert tests.sensitization1()
assert tests.selection(2)
# Initialize second field
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(1)
tree.row_activated((2,), column)
checkpoint toplevel widget mapped Dialog-Initialize field Displacement
findWidget('Dialog-Initialize field Displacement').resize(243, 125)
findWidget('Dialog-Initialize field Displacement:initializer:Constant:cx').set_text('')
findWidget('Dialog-Initialize field Displacement:initializer:Constant:cx').set_text('1')
findWidget('Dialog-Initialize field Displacement:initializer:Constant:cy').set_text('')
findWidget('Dialog-Initialize field Displacement:initializer:Constant:cy').set_text('2')
findWidget('Dialog-Initialize field Displacement:gtk-ok').clicked()
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((2,))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Set_Field_Initializer
checkpoint Solver page sensitized
assert tests.sensitization2()
assert tests.selection(2)
# Apply initializers.  There are no explicit tests here, other the
# checkpoint that confirms that the command has completed, and the log
# file test at the end that checks that the arguments were obtained
# correctly.
findWidget('OOF2:Solver Page:VPane:FieldInit:Apply').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Apply_Field_Initializers
checkpoint Solver page sensitized
# Apply at time.  There are no explicit tests here either.
findWidget('OOF2:Solver Page:VPane:FieldInit:ApplyAt').clicked()
checkpoint toplevel widget mapped Dialog-Initialize Fields at Time
findWidget('Dialog-Initialize Fields at Time').resize(190, 71)
findWidget('Dialog-Initialize Fields at Time:time').set_text('')
findWidget('Dialog-Initialize Fields at Time:time').set_text('1')
findWidget('Dialog-Initialize Fields at Time:time').set_text('12')
findWidget('Dialog-Initialize Fields at Time:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Apply_Field_Initializers_at_Time
checkpoint Solver page sensitized
# Check that mesh time is 12
assert tests.sensitization2()
assert tests.checkTime(12.0)
# Create second mesh
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane').set_position(531)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(345, 210)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
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
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Mesh.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint page installed Solver
checkpoint Solver page sensitized
assert tests.sensitization2()
assert tests.listCheck("Temperature", "Temperature_z", "Displacement")
# Switch to second mesh
setComboBox(findWidget('OOF2:Solver Page:Mesh'), 'mesh<2>')
checkpoint Solver page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 0.0000000000000e+00)
assert tests.sensitization0()
assert tests.listCheck()
# Switch back to first mesh
setComboBox(findWidget('OOF2:Solver Page:Mesh'), 'mesh')
checkpoint Solver page sensitized
assert tests.sensitization4()
assert tests.listCheck("Temperature", "Temperature_z", "Displacement")
# Copy initializers to second mesh
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.7058823529412e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 3.4117647058824e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 5.1176470588235e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 6.8235294117647e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 8.5294117647059e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.0235294117647e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.1941176470588e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.3647058823529e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.5352941176471e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.7058823529412e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 1.8764705882353e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.0470588235294e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.2176470588235e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.3882352941176e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.5588235294118e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.7294117647059e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 2.9000000000000e+01)
findWidget('OOF2:Solver Page:VPane:FieldInit:CopyInit').clicked()
checkpoint toplevel widget mapped Dialog-Select a target Mesh
findWidget('Dialog-Select a target Mesh').resize(251, 133)
setComboBox(findWidget('Dialog-Select a target Mesh:target:Mesh'), 'mesh<2>')
findWidget('Dialog-Select a target Mesh:gtk-ok').clicked()
checkpoint OOF.Mesh.Copy_Field_Initializers
# Switch to second mesh
setComboBox(findWidget('OOF2:Solver Page:Mesh'), 'mesh<2>')
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 0.0000000000000e+00)
# Nothing should have happened, since fields aren't defined.
assert tests.sensitization0()
assert tests.listCheck()
# Define only one field (T) on second mesh.
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Boundary Conditions')
checkpoint page installed Boundary Conditions
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Fields & Equations')
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2').resize(803, 484)
findWidget('OOF2:Fields & Equations Page:HPane').set_position(357)
setComboBox(findWidget('OOF2:Fields & Equations Page:Mesh'), 'mesh<2>')
checkpoint Field page sensitized
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.sensitization0()
assert tests.listCheck("Temperature", "Temperature_z")
# Switch to first mesh
setComboBox(findWidget('OOF2:Solver Page:Mesh'), 'mesh')
checkpoint Solver page sensitized
assert tests.sensitization4()
assert tests.listCheck("Temperature", "Temperature_z", "Displacement")
# Define initializer for T
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(1)
tree.row_activated((0,), column)
checkpoint toplevel widget mapped Dialog-Initialize field Temperature
findWidget('Dialog-Initialize field Temperature').resize(263, 102)
findWidget('Dialog-Initialize field Temperature:gtk-ok').clicked()
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Set_Field_Initializer
checkpoint Solver page sensitized
assert tests.sensitization2()
# Copy initializers to second mesh
findWidget('OOF2:Solver Page:VPane:FieldInit:CopyInit').clicked()
checkpoint toplevel widget mapped Dialog-Select a target Mesh
findWidget('Dialog-Select a target Mesh').resize(251, 133)
setComboBox(findWidget('Dialog-Select a target Mesh:target:Mesh'), 'mesh<2>')
findWidget('Dialog-Select a target Mesh:gtk-ok').clicked()
checkpoint OOF.Mesh.Copy_Field_Initializers
assert tests.sensitization2()
assert tests.listCheck("Temperature", "Temperature_z", "Displacement")
# Switch to second mesh
setComboBox(findWidget('OOF2:Solver Page:Mesh'), 'mesh<2>')
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
assert tests.sensitization2()
assert tests.listCheck("Temperature", "Temperature_z")
# Undefine field on second mesh
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Fields & Equations')
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Undefine
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.sensitization0()
assert tests.listCheck()
# Switch to first mesh
setComboBox(findWidget('OOF2:Solver Page:Mesh'), 'mesh')
checkpoint Solver page sensitized
assert tests.sensitization4()
assert tests.listCheck("Temperature", "Temperature_z", "Displacement")
# Switch back to second mesh, then delete it.
setComboBox(findWidget('OOF2:Solver Page:Mesh'), 'mesh<2>')
checkpoint Solver page sensitized
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane').set_position(561)
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(340, 93)
findWidget('Questioner:gtk-yes').clicked()
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Delete
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.sensitization4()
assert tests.listCheck("Temperature", "Temperature_z", "Displacement")
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(191, 98)
findWidget('Dialog-Python_Log:filename').set_text('i')
findWidget('Dialog-Python_Log:filename').set_text('in')
findWidget('Dialog-Python_Log:filename').set_text('ini')
findWidget('Dialog-Python_Log:filename').set_text('init')
findWidget('Dialog-Python_Log:filename').set_text('initt')
findWidget('Dialog-Python_Log:filename').set_text('initte')
findWidget('Dialog-Python_Log:filename').set_text('inittes')
findWidget('Dialog-Python_Log:filename').set_text('inittest')
findWidget('Dialog-Python_Log:filename').set_text('inittest.')
findWidget('Dialog-Python_Log:filename').set_text('inittest.l')
findWidget('Dialog-Python_Log:filename').set_text('inittest.lo')
findWidget('Dialog-Python_Log:filename').set_text('inittest.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('inittest.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
