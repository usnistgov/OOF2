checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.9 $
# $Author: langer $
# $Date: 2010/12/25 01:40:40 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Check that the Subproblem list and buttons are working correctly.

import tests

findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
findWidget('OOF2').resize(577, 350)
findWidget('OOF2:Microstructure Page:Pane').set_position(159)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
checkpoint microstructure page sensitized
findWidget('Dialog-Create Microstructure').resize(315, 163)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(164)
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint active area status updated
checkpoint pixel page updated
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
findWidget('OOF2').resize(705, 424)
findWidget('OOF2:Skeleton Page:Pane').set_position(324)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(394, 198)
checkpoint skeleton page sensitized
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
checkpoint OOF.Skeleton.New
checkpoint skeleton selection page groups sensitized
checkpoint Solver page sensitized
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
checkpoint OOF.Mesh.New
checkpoint Solver page sensitized
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint page installed Solver
assert tests.listCheck("default")
checkpoint Solver page sensitized
assert tests.selection(None)
assert tests.unsolvable()
assert tests.sensitization0()
# Select subproblem
findWidget('OOF2').resize(705, 484)
findWidget('OOF2:Solver Page:VPane').set_position(152)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((0,))
assert tests.listCheck("default")
checkpoint Solver page sensitized
assert tests.selection(0)
assert tests.sensitization1()
# Deselect subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().unselect_all()
findWidget('OOF2:Solver Page:end').set_text('1')
checkpoint Solver page sensitized
checkpoint Solver page sensitized
assert tests.sensitization0()
# Reselect subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((0,))
checkpoint Solver page sensitized
assert tests.sensitization1()
# Add Solver
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(3)
tree.row_activated((0,), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(441, 218)
findWidget('Dialog-Specify Solver:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Subproblem.Set_Solver
checkpoint Solver page sensitized
assert tests.sensitization2()
# Remove solver
findWidget('OOF2:Solver Page:VPane:Subproblems:Remove').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Subproblem.Remove_Solver
checkpoint Solver page sensitized
assert tests.sensitization1()
assert tests.selection(0)
# Define second subproblem
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new subproblem
findWidget('Dialog-Create a new subproblem').resize(291, 102)
findWidget('Dialog-Create a new subproblem:name:Auto').clicked()
findWidget('Dialog-Create a new subproblem:name:Text').set_text('s')
findWidget('Dialog-Create a new subproblem:name:Text').set_text('su')
findWidget('Dialog-Create a new subproblem:name:Text').set_text('sub')
findWidget('Dialog-Create a new subproblem:name:Text').set_text('subp')
findWidget('Dialog-Create a new subproblem:name:Text').set_text('subpr')
findWidget('Dialog-Create a new subproblem:name:Text').set_text('subpro')
findWidget('Dialog-Create a new subproblem:name:Text').set_text('subprob')
findWidget('Dialog-Create a new subproblem:name:Text').set_text('subprob2')
findWidget('Dialog-Create a new subproblem:gtk-ok').clicked()
checkpoint mesh page subproblems sensitized
checkpoint OOF.Subproblem.New
checkpoint Solver page sensitized
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Solver
checkpoint Solver page sensitized
assert tests.listCheck("default", "subprob2")
assert tests.sensitization3()
assert tests.selection(0)
# Add Solver
findWidget('OOF2:Solver Page:VPane:Subproblems:Set').clicked()
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(441, 218)
findWidget('Dialog-Specify Solver:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Subproblem.Set_Solver
checkpoint Solver page sensitized
assert tests.sensitization4()
# Select second subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((1,))
checkpoint Solver page sensitized
assert tests.sensitization5()
assert tests.selection(1)
# Add solver
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 6.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:Subproblems:Set').clicked()
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(441, 218)
findWidget('Dialog-Specify Solver:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Subproblem.Set_Solver
checkpoint Solver page sensitized
assert tests.sensitization6()
# Remove second solver
findWidget('OOF2:Solver Page:VPane:Subproblems:Remove').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Subproblem.Remove_Solver
checkpoint Solver page sensitized
assert tests.sensitization5()
# Re-add second solver
findWidget('OOF2:Solver Page:VPane:Subproblems:Set').clicked()
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(441, 218)
findWidget('Dialog-Specify Solver:gtk-ok').clicked()
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
checkpoint Solver page sensitized
assert tests.sensitization6()
# Remove all solvers
findWidget('OOF2:Solver Page:VPane:Subproblems:RemoveAll').clicked()
checkpoint OOF.Mesh.Remove_All_Solvers
checkpoint Solver page sensitized
assert tests.sensitization7()
# Define third subproblem
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new subproblem
findWidget('Dialog-Create a new subproblem').resize(291, 102)
findWidget('Dialog-Create a new subproblem:name:Text').set_text('subprob')
findWidget('Dialog-Create a new subproblem:name:Text').set_text('subprob3')
findWidget('Dialog-Create a new subproblem:gtk-ok').clicked()
checkpoint mesh page subproblems sensitized
checkpoint OOF.Subproblem.New
checkpoint Solver page sensitized
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Solver
assert tests.listCheck("default", "subprob2", "subprob3")
checkpoint Solver page sensitized
assert tests.sensitization8()
assert tests.selection(1)
findWidget('OOF2').resize(705, 500)
findWidget('OOF2:Solver Page:VPane').set_position(160)
findWidget('OOF2').resize(708, 533)
findWidget('OOF2').resize(709, 568)
findWidget('OOF2').resize(709, 603)
findWidget('OOF2').resize(707, 629)
findWidget('OOF2').resize(706, 647)
findWidget('OOF2:Solver Page:VPane').set_position(234)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2').resize(705, 651)
findWidget('OOF2').resize(705, 654)
findWidget('OOF2').resize(705, 655)
findWidget('OOF2:Solver Page:VPane').set_position(238)
# Select third subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((2,))
assert tests.selection(2)
checkpoint Solver page sensitized
assert tests.sensitization7()
# Select first subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((0,))
checkpoint Solver page sensitized
assert tests.sensitization3()
assert tests.selection(0)
# Move 1st subproblem down in the list
findWidget('OOF2:Solver Page:VPane:Subproblems:Later').clicked()
checkpoint OOF.Mesh.ReorderSubproblems
assert tests.listCheck("subprob2", "default", "subprob3")
checkpoint Solver page sensitized
assert tests.sensitization8()
assert tests.selection(1)
# Move down again
findWidget('OOF2:Solver Page:VPane:Subproblems:Later').clicked()
checkpoint OOF.Mesh.ReorderSubproblems
assert tests.listCheck("subprob2", "subprob3", "default")
assert tests.sensitization7()
assert tests.selection(2)
# Move up
findWidget('OOF2:Solver Page:VPane:Subproblems:Earlier').clicked()
checkpoint OOF.Mesh.ReorderSubproblems
checkpoint Solver page sensitized
assert tests.listCheck("subprob2", "default", "subprob3")
checkpoint Solver page sensitized
assert tests.sensitization8()
assert tests.selection(1)
# Move up again
findWidget('OOF2:Solver Page:VPane:Subproblems:Earlier').clicked()
checkpoint OOF.Mesh.ReorderSubproblems
assert tests.listCheck("default", "subprob2", "subprob3")
checkpoint Solver page sensitized
assert tests.sensitization3()
assert tests.selection(0)
# Move to bottom
findWidget('OOF2:Solver Page:VPane:Subproblems:Last').clicked()
checkpoint OOF.Mesh.ReorderSubproblems
assert tests.listCheck("subprob2", "subprob3", "default")
checkpoint Solver page sensitized
assert tests.sensitization7()
assert tests.selection(2)
# Move to top
findWidget('OOF2:Solver Page:VPane:Subproblems:First').clicked()
checkpoint OOF.Mesh.ReorderSubproblems
assert tests.listCheck("default", "subprob2", "subprob3")
checkpoint Solver page sensitized
assert tests.sensitization3()
assert tests.selection(0)
# Select second subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((1,))
# Delete second subproblem
checkpoint Solver page sensitized
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:subprobChooserScroll:subprobChooser').get_selection().select_path((1,))
checkpoint mesh page subproblems sensitized
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(370, 93)
findWidget('Questioner:gtk-yes').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Delete
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Solver
checkpoint Solver page sensitized
assert tests.selection(None)
assert tests.sensitization0()
assert tests.listCheck("default", "subprob3")
# Select default subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((0,))
checkpoint Solver page sensitized
assert tests.sensitization3()
assert tests.selection(0)
# Delete third subproblem
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:subprobChooserScroll:subprobChooser').get_selection().select_path((1,))
checkpoint mesh page subproblems sensitized
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(370, 93)
findWidget('Questioner:gtk-yes').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Delete
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint page installed Solver
checkpoint Solver page sensitized
assert tests.sensitization1()
assert tests.listCheck("default")
assert tests.selection(0)
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(191, 98)
findWidget('Dialog-Python_Log:filename').set_text('s')
findWidget('Dialog-Python_Log:filename').set_text('su')
findWidget('Dialog-Python_Log:filename').set_text('sub')
findWidget('Dialog-Python_Log:filename').set_text('subp')
findWidget('Dialog-Python_Log:filename').set_text('subpr')
findWidget('Dialog-Python_Log:filename').set_text('subpro')
findWidget('Dialog-Python_Log:filename').set_text('subprob')
findWidget('Dialog-Python_Log:filename').set_text('subprobl')
findWidget('Dialog-Python_Log:filename').set_text('subproble')
findWidget('Dialog-Python_Log:filename').set_text('subproblem')
findWidget('Dialog-Python_Log:filename').set_text('subprobleml')
findWidget('Dialog-Python_Log:filename').set_text('subproblemli')
findWidget('Dialog-Python_Log:filename').set_text('subproblemlis')
findWidget('Dialog-Python_Log:filename').set_text('subproblemlist')
findWidget('Dialog-Python_Log:filename').set_text('subproblemlist.')
findWidget('Dialog-Python_Log:filename').set_text('subproblemlist.l')
findWidget('Dialog-Python_Log:filename').set_text('subproblemlist.lo')
findWidget('Dialog-Python_Log:filename').set_text('subproblemlist.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('subproblemlist.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
