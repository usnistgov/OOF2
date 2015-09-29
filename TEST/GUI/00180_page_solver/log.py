# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.19 $
# $Author: langer $
# $Date: 2010/12/02 21:09:28 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## Test the sensitization of the Solve button as a problem is
## constructed.

import tests

setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint page installed Solver
findWidget('OOF2').resize(550, 484)
findWidget('OOF2:Solver Page:VPane').set_position(152)
# Sensitization check.  Nothing defined.
assert tests.sensitive(False)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
checkpoint page installed Microstructure
findWidget('OOF2').resize(577, 484)
findWidget('OOF2:Microstructure Page:Pane').set_position(159)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(315, 163)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(164)
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint microstructure page sensitized
checkpoint meshable button set
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
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized
# checkpoint interface page updated
checkpoint OOF.Microstructure.New
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Solver
# Sensitization check.  MS defined.
assert tests.sensitive(False)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint page installed Materials
findWidget('OOF2').resize(685, 484)
findWidget('OOF2:Materials Page:Pane').set_position(274)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(301, 98)
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
findWidget('Dialog-Assign material material to pixels').resize(304, 106)
setComboBox(findWidget('Dialog-Assign material material to pixels:pixels'), '<every>')
findWidget('Dialog-Assign material material to pixels:gtk-ok').clicked()
checkpoint OOF.Material.Assign
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1,), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 0, 0))
checkpoint Materials page updated
checkpoint property selected
widget_0=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_0.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_0.window))
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 3), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 3, 0))
checkpoint Materials page updated
checkpoint property deselected
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
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(304)
findWidget('OOF2').resize(705, 484)
findWidget('OOF2:Skeleton Page:Pane').set_position(324)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(394, 198)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint OOF.Skeleton.New
checkpoint skeleton selection page updated
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint page installed Solver
# Sensitization check.  MS, material, & skeleton defined.
assert tests.sensitive(False)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
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
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Mesh.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint page installed Solver
# Sensitization check.  mesh defined.
assert tests.sensitive(False)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Fields & Equations')
checkpoint page installed Fields & Equations
findWidget('OOF2').resize(773, 484)
findWidget('OOF2:Fields & Equations Page:HPane').set_position(343)
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Field page sensitized
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement in-plane').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Mesh.Field.In_Plane
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
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Subproblem.Equation.Activate
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint page installed Solver
# Sensitization check.  fields & equations defined.
assert tests.sensitive(False)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((0,))
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(3)
tree.row_activated((0,), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(441, 218)
findWidget('Dialog-Specify Solver:gtk-ok').clicked()
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Subproblem.Set_Solver
# Sensitization check.  solver set. "Solve" should be sensitized
assert tests.sensitive(True)
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(191, 98)
findWidget('Dialog-Python_Log:filename').set_text('s')
findWidget('Dialog-Python_Log:filename').set_text('so')
findWidget('Dialog-Python_Log:filename').set_text('sol')
findWidget('Dialog-Python_Log:filename').set_text('solv')
findWidget('Dialog-Python_Log:filename').set_text('solve')
findWidget('Dialog-Python_Log:filename').set_text('solvet')
findWidget('Dialog-Python_Log:filename').set_text('solvete')
findWidget('Dialog-Python_Log:filename').set_text('solvetes')
findWidget('Dialog-Python_Log:filename').set_text('solvetest')
findWidget('Dialog-Python_Log:filename').set_text('solvetest.')
findWidget('Dialog-Python_Log:filename').set_text('solvetest.l')
findWidget('Dialog-Python_Log:filename').set_text('solvetest.lo')
findWidget('Dialog-Python_Log:filename').set_text('solvetest.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('solvetest.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
