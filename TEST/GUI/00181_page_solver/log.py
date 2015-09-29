checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.24 $
# $Author: langer $
# $Date: 2011/04/29 20:25:56 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Load a Mesh from a file.  Check that making the problem unsolvable
# in various ways desensitizes the Solve button and sets the status
# correctly.

import tests

checkpoint microstructure page sensitized
checkpoint active area status updated
checkpoint pixel page updated
checkpoint microstructure page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
# checkpoint interface page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint Solver page sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
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
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
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
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.File.LoadStartUp.Data
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2').resize(582, 484)
findWidget('OOF2:Solver Page:VPane').set_position(152)
assert tests.solvable()
checkpoint_count("Solver page sensitized")

# Remove solver
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((0,))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 3.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:Subproblems:Remove').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Remove_Solver
assert tests.unsolvable()
checkpoint_count("Solver page sensitized")

# Restore solver
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 3.0000000000000e+00)
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(3)
tree.row_activated((0,), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(441, 218)
findWidget('Dialog-Specify Solver:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
#checkpoint Solver page sensitized
assert tests.solvable()
checkpoint_count("Solver page sensitized")

# Toggle solvability
findCellRenderer(findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList'), col=1, rend=0).emit('toggled', '0')
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Disable_Solution
assert tests.unsolvable()
checkpoint_count("Solver page sensitized")

# Toggle again
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 3.0000000000000e+00)
findCellRenderer(findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList'), col=1, rend=0).emit('toggled', '0')
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Enable_Solution
assert tests.solvable()
checkpoint_count("Solver page sensitized")

# Deactivate field
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Fields & Equations')
checkpoint page installed Fields & Equations
findWidget('OOF2').resize(773, 484)
findWidget('OOF2:Fields & Equations Page:HPane').set_position(343)
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Deactivate
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.unsolvable()
findWidget('OOF2:Solver Page:status').clicked()
assert tests.details("There are no active fields.\n")
checkpoint_count("Solver page sensitized")

# Reactivate field
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.solvable()
findWidget('OOF2:Solver Page:status').clicked()
assert tests.details("Unsolved: Field activated.\n")
checkpoint_count("Solver page sensitized")

# undefine field
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Undefine
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.unsolvable()
findWidget('OOF2:Solver Page:status').clicked()
assert tests.details("There are no active fields.\n")

# Redefine and activate field
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define
checkpoint_count("Solver page sensitized")
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.solvable()
checkpoint_count("Solver page sensitized")

# Deactivate equation
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Force_Balance active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Deactivate
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.unsolvable()
findWidget('OOF2:Solver Page:status').clicked()
assert tests.details("There are too few active equations (3) or too many active fields (5).\n")

# Deactivate other equation
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Force_Balance active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Plane_Stress active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Deactivate
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.unsolvable()
checkpoint_count("Solver page sensitized")
findWidget('OOF2:Solver Page:status').clicked()
assert tests.details("There are too few active equations (2) or too many active fields (5).\n")

# Reactivate equations
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Introduction
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Plane_Stress active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Activate
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.solvable()

# Remove modulus from Material
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(274)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList').get_selection().select_path((0,))
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1,), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Material:RemoveProperty').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint OOF.Material.Remove_property
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Fields & Equations
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.unsolvable()
findWidget('OOF2:Solver Page:status').clicked()
assert tests.details("Equation 'Force_Balance' has no flux contributions\n   Equation 'Plane_Stress' has no flux contributions\n")

# Restore modulus to Material
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.solvable()
findWidget('OOF2:Solver Page:status').clicked()
assert tests.details("Unsolved: Material properties changed.\n")
checkpoint_count("Solver page sensitized")

# Remove material from pixels
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane:Material:RemoveMaterial').clicked()
checkpoint toplevel widget mapped Dialog-Remove the assigned material from pixels
findWidget('Dialog-Remove the assigned material from pixels').resize(304, 106)
setComboBox(findWidget('Dialog-Remove the assigned material from pixels:pixels'), '<every>')
findWidget('Dialog-Remove the assigned material from pixels:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Material.Remove
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.unsolvable()
findWidget('OOF2:Solver Page:status').clicked()
assert tests.details("Equation 'Force_Balance' has no flux contributions\n   Equation 'Plane_Stress' has no flux contributions\n")

# Restore material to pixels
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(304, 106)
setComboBox(findWidget('Dialog-Assign material material to pixels:pixels'), '<every>')
findWidget('Dialog-Assign material material to pixels:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Material.Assign
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.solvable()
findWidget('OOF2:Solver Page:status').clicked()
# Check details
assert tests.details("Unsolved: Materials changed.\n")

# Switch to a time-dependent solver
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(3)
tree.row_activated((0,), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(475, 187)
setComboBox(findWidget('Dialog-Specify Solver:solver_mode:Basic:time_stepper:Chooser'), 'Adaptive')
findWidget('Dialog-Specify Solver').resize(475, 233)
findWidget('Dialog-Specify Solver:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
assert tests.unsolvable()
findWidget('OOF2:Solver Page:status').clicked()
assert tests.details("Unsolved: Solver changed\n")

# Enter the end time
findWidget('OOF2:Solver Page:end').set_text('1')
checkpoint Solver page sensitized
assert tests.solvable()

# Remove mass density from material
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList').get_selection().select_path((0,))
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 3), open_all=False)
findWidget('OOF2:Materials Page:Pane:Material:RemoveProperty').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Material.Remove_property
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.solvable()
findWidget('OOF2:Solver Page:status').clicked()
assert tests.details("Unsolved: Material properties changed.\n")

# Restore mass density
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.solvable()
findWidget('OOF2:Solver Page:status').clicked()
assert tests.details("Unsolved: Material properties changed.\n")
checkpoint_count("Solver page sensitized")
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(191, 98)
findWidget('Dialog-Python_Log:filename').set_text('s')
findWidget('Dialog-Python_Log:filename').set_text('so')
findWidget('Dialog-Python_Log:filename').set_text('sol')
findWidget('Dialog-Python_Log:filename').set_text('solv')
findWidget('Dialog-Python_Log:filename').set_text('solve')
findWidget('Dialog-Python_Log:filename').set_text('solver')
findWidget('Dialog-Python_Log:filename').set_text('solverp')
findWidget('Dialog-Python_Log:filename').set_text('solverpa')
findWidget('Dialog-Python_Log:filename').set_text('solverpag')
findWidget('Dialog-Python_Log:filename').set_text('solverpage')
findWidget('Dialog-Python_Log:filename').set_text('solverpage.')
findWidget('Dialog-Python_Log:filename').set_text('solverpage.l')
findWidget('Dialog-Python_Log:filename').set_text('solverpage.lo')
findWidget('Dialog-Python_Log:filename').set_text('solverpage.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
