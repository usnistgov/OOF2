# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Check that the Subproblem list and buttons are working correctly.

import tests
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)

findWidget('OOF2').resize(782, 545)
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
checkpoint mesh bdy page updated
checkpoint pixel page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
checkpoint skeleton page info updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 4.5000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
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
event(Gdk.EventType.BUTTON_PRESS,x= 7.4000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Solver Page:VPane').set_position(170)
assert tests.listCheck("default")

assert tests.selection(None)
assert tests.unsolvable()
assert tests.sensitization0()

# Select subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
assert tests.listCheck("default")

assert tests.selection(0)
assert tests.sensitization1()

# Deselect subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().unselect_all()
checkpoint Solver page sensitized
assert tests.sensitization0()

# Reselect subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
assert tests.sensitization1()

# Add Solver
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
assert tests.sensitization2()

# Remove solver
findWidget('OOF2:Solver Page:VPane:Subproblems:Remove').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Remove_Solver
assert tests.sensitization1()
assert tests.selection(0)

# Define second subproblem
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new subproblem
findWidget('Dialog-Create a new subproblem').resize(206, 133)
findWidget('Dialog-Create a new subproblem:name').delete_text(0, 11)
findWidget('Dialog-Create a new subproblem:name').insert_text('s', 11)
findWidget('Dialog-Create a new subproblem:name').insert_text('u', 1)
findWidget('Dialog-Create a new subproblem:name').insert_text('b', 2)
findWidget('Dialog-Create a new subproblem:name').insert_text('p', 3)
findWidget('Dialog-Create a new subproblem:name').insert_text('r', 4)
findWidget('Dialog-Create a new subproblem:name').insert_text('o', 5)
findWidget('Dialog-Create a new subproblem:name').insert_text('b', 6)
findWidget('Dialog-Create a new subproblem:name').insert_text('2', 7)
findWidget('Dialog-Create a new subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.New
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.listCheck("default", "subprob2")
assert tests.sensitization3()
assert tests.selection(0)

# Add Solver
findWidget('OOF2:Solver Page:VPane:Subproblems:Set').clicked()
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(414, 253)
findWidget('Dialog-Specify Solver:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
assert tests.sensitization4()

# Select second subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint Solver page sensitized
assert tests.sensitization5()
assert tests.selection(1)

# Add solver
findWidget('OOF2:Solver Page:VPane:Subproblems:Set').clicked()
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(414, 253)
findWidget('Dialog-Specify Solver:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
assert tests.sensitization6()

# Remove second solver
findWidget('OOF2:Solver Page:VPane:Subproblems:Remove').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Remove_Solver
assert tests.sensitization5()

# Re-add second solver
findWidget('OOF2:Solver Page:VPane:Subproblems:Set').clicked()
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(414, 253)
findWidget('Dialog-Specify Solver:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
assert tests.sensitization6()

# Remove all solvers
findWidget('OOF2:Solver Page:VPane:Subproblems:RemoveAll').clicked()
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Remove_All_Solvers
assert tests.sensitization7()

# Define third subproblem
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new subproblem
findWidget('Dialog-Create a new subproblem').resize(206, 133)
findWidget('Dialog-Create a new subproblem:name').delete_text(7, 8)
findWidget('Dialog-Create a new subproblem:name').insert_text('3', 7)
findWidget('Dialog-Create a new subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.New
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.listCheck("default", "subprob2", "subprob3")
assert tests.sensitization8()
assert tests.selection(1)

# Select third subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 2.0000000000000e+01)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([2]))
checkpoint Solver page sensitized
assert tests.selection(2)
assert tests.sensitization7()

# Select first subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 1.9112155731228e+01)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
assert tests.sensitization3()
assert tests.selection(0)

# Move 1st subproblem down in the list
findWidget('OOF2:Solver Page:VPane:Subproblems:Later').clicked()
checkpoint Solver page sensitized
checkpoint OOF.Mesh.ReorderSubproblems
assert tests.listCheck("subprob2", "default", "subprob3")
assert tests.sensitization8()
assert tests.selection(1)

# Move down again
findWidget('OOF2:Solver Page:VPane:Subproblems:Later').clicked()
checkpoint Solver page sensitized
checkpoint OOF.Mesh.ReorderSubproblems
assert tests.listCheck("subprob2", "subprob3", "default")
assert tests.sensitization7()
assert tests.selection(2)

# Move up
findWidget('OOF2:Solver Page:VPane:Subproblems:Earlier').clicked()
checkpoint Solver page sensitized
checkpoint OOF.Mesh.ReorderSubproblems
assert tests.listCheck("subprob2", "default", "subprob3")
assert tests.sensitization8()
assert tests.selection(1)

# Move up again
findWidget('OOF2:Solver Page:VPane:Subproblems:Earlier').clicked()
checkpoint Solver page sensitized
checkpoint OOF.Mesh.ReorderSubproblems
assert tests.listCheck("default", "subprob2", "subprob3")
assert tests.sensitization3()
assert tests.selection(0)

# Move to bottom
findWidget('OOF2:Solver Page:VPane:Subproblems:Last').clicked()
checkpoint Solver page sensitized
checkpoint OOF.Mesh.ReorderSubproblems
assert tests.listCheck("subprob2", "subprob3", "default")
assert tests.sensitization7()
assert tests.selection(2)

# Move to top
findWidget('OOF2:Solver Page:VPane:Subproblems:First').clicked()
checkpoint Solver page sensitized
checkpoint OOF.Mesh.ReorderSubproblems
assert tests.listCheck("default", "subprob2", "subprob3")
assert tests.sensitization3()
assert tests.selection(0)

# Select second subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint Solver page sensitized

# Delete second subproblem
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2').resize(782, 545)
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:subprobChooserScroll:subprobChooser').get_selection().select_path(Gtk.TreePath([1]))
checkpoint mesh page subproblems sensitized
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(323, 86)
findWidget('Questioner:Yes').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Delete
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.selection(None)
assert tests.sensitization0()
assert tests.listCheck("default", "subprob3")

# Select default subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
assert tests.sensitization3()
assert tests.selection(0)

# Delete third subproblem
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:subprobChooserScroll:subprobChooser').get_selection().select_path(Gtk.TreePath([1]))
checkpoint mesh page subproblems sensitized
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(323, 86)
findWidget('Questioner:Yes').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Delete
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.sensitization1()
assert tests.listCheck("default")
assert tests.selection(0)

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