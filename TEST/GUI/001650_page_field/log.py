# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)
event(Gdk.EventType.BUTTON_PRESS,x= 4.5000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane').set_position(470)
findWidget('OOF2').resize(782, 545)
assert tests.sensitization0()

# load a Skeleton
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
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
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
assert tests.sensitization0()

# Create a mesh and check field page sensitization
findWidget('OOF2:Navigation:Prev').clicked()
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
findWidget('OOF2:Navigation:Next').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
assert tests.sensitization1()

# Define a field
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
assert tests.sensitization2()

# Define another field
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
assert tests.sensitization3()

# undefine the first field
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
checkpoint OOF.Subproblem.Field.Undefine
assert tests.sensitization4()

# undefine the second field
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
checkpoint OOF.Subproblem.Field.Undefine
assert tests.sensitization1()

# Refine the first field
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
assert tests.sensitization2()

# Create a new subproblem, switch between subproblems, and copy field
# and equation state between subproblems.

event(Gdk.EventType.BUTTON_PRESS,x= 4.5000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new subproblem
findWidget('Dialog-Create a new subproblem').resize(206, 133)
findWidget('Dialog-Create a new subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.New
findWidget('OOF2:Navigation:Next').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
assert tests.fieldButtonCheck(1, 0, 0)
assert tests.sensitization2()

event(Gdk.EventType.BUTTON_PRESS,x= 4.2000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:SubProblem').get_window())
checkpoint toplevel widget mapped chooserPopup-SubProblem
findMenu(findWidget('chooserPopup-SubProblem'), ['subproblem']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-SubProblem') # MenuItemLogger
checkpoint Field page sensitized
assert tests.sensitization1()
assert tests.fieldButtonCheck(0, 0, 0)

event(Gdk.EventType.BUTTON_PRESS,x= 5.2000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:SubProblem').get_window())
checkpoint toplevel widget mapped chooserPopup-SubProblem
findMenu(findWidget('chooserPopup-SubProblem'), ['default']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-SubProblem') # MenuItemLogger
checkpoint Field page sensitized
assert tests.sensitization2()
assert tests.fieldButtonCheck(1, 0, 0)

# Copy field and equation state
findWidget('OOF2:Fields & Equations Page:HPane:CopyField').clicked()
checkpoint toplevel widget mapped Dialog-Select a target Subproblem
findWidget('Dialog-Select a target Subproblem').resize(196, 182)
event(Gdk.EventType.BUTTON_PRESS,x= 7.8000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-Select a target Subproblem:target:SubProblem').get_window())
checkpoint toplevel widget mapped chooserPopup-SubProblem
findMenu(findWidget('chooserPopup-SubProblem'), ['subproblem']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-SubProblem') # MenuItemLogger
findWidget('Dialog-Select a target Subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Copy_Field_State
assert tests.sensitization2()
assert tests.fieldButtonCheck(1, 0, 0)

event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:SubProblem').get_window())
checkpoint toplevel widget mapped chooserPopup-SubProblem
findMenu(findWidget('chooserPopup-SubProblem'), ['subproblem']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-SubProblem') # MenuItemLogger
checkpoint Field page sensitized
assert tests.sensitization2()
assert tests.fieldButtonCheck(1, 0, 0)
assert tests.eqnButtonCheck(0)

# Activate an equation
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
assert tests.eqnButtonCheck(1)

event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:SubProblem').get_window())
checkpoint toplevel widget mapped chooserPopup-SubProblem
findMenu(findWidget('chooserPopup-SubProblem'), ['default']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-SubProblem') # MenuItemLogger
checkpoint Field page sensitized
assert tests.eqnButtonCheck(0)

event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:SubProblem').get_window())
checkpoint toplevel widget mapped chooserPopup-SubProblem
findMenu(findWidget('chooserPopup-SubProblem'), ['subproblem']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-SubProblem') # MenuItemLogger
checkpoint Field page sensitized
assert tests.eqnButtonCheck(1)

# Copy equation state
findWidget('OOF2:Fields & Equations Page:HPane:CopyEquation').clicked()
checkpoint toplevel widget mapped Dialog-Select a target subproblem
findWidget('Dialog-Select a target subproblem').resize(196, 182)
event(Gdk.EventType.BUTTON_PRESS,x= 9.2000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-Select a target subproblem:target:SubProblem').get_window())
checkpoint toplevel widget mapped chooserPopup-SubProblem
findMenu(findWidget('chooserPopup-SubProblem'), ['default']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-SubProblem') # MenuItemLogger
findWidget('Dialog-Select a target subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Copy_Equation_State
assert tests.eqnButtonCheck(1)

event(Gdk.EventType.BUTTON_PRESS,x= 4.8000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:SubProblem').get_window())
checkpoint toplevel widget mapped chooserPopup-SubProblem
findMenu(findWidget('chooserPopup-SubProblem'), ['default']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-SubProblem') # MenuItemLogger
checkpoint Field page sensitized
assert tests.eqnButtonCheck(1)

# Create a new Mesh, and switch back and forth between meshes checking
# that the page updates properly.
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
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
checkpoint OOF.Mesh.New
findWidget('OOF2:Navigation:Next').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
assert tests.sensitization2()
assert tests.fieldButtonCheck(1, 0, 0)
assert tests.eqnButtonCheck(1)

event(Gdk.EventType.BUTTON_PRESS,x= 6.4000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
checkpoint Field page sensitized
assert tests.sensitization1()
assert tests.fieldButtonCheck(0, 0, 0)
assert tests.eqnButtonCheck(0)

event(Gdk.EventType.BUTTON_PRESS,x= 6.4000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
checkpoint Field page sensitized
assert tests.sensitization2()
assert tests.fieldButtonCheck(1, 0, 0)
assert tests.eqnButtonCheck(1)

# Copy field state to the new mesh
findWidget('OOF2:Fields & Equations Page:HPane:CopyField').clicked()
checkpoint toplevel widget mapped Dialog-Select a target Subproblem
findWidget('Dialog-Select a target Subproblem').resize(196, 182)
event(Gdk.EventType.BUTTON_PRESS,x= 6.8000000000000e+01,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-Select a target Subproblem:target:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
findWidget('Dialog-Select a target Subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint OOF.Subproblem.Copy_Field_State
assert tests.sensitization2()
assert tests.fieldButtonCheck(1, 0, 0)
assert tests.eqnButtonCheck(1)

event(Gdk.EventType.BUTTON_PRESS,x= 2.6000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
checkpoint Field page sensitized
assert tests.sensitization2()
assert tests.fieldButtonCheck(1, 0, 0)
assert tests.eqnButtonCheck(0)

event(Gdk.EventType.BUTTON_PRESS,x= 4.6000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
checkpoint Field page sensitized
assert tests.sensitization2()
assert tests.fieldButtonCheck(1, 0, 0)
assert tests.eqnButtonCheck(1)

findWidget('OOF2:Fields & Equations Page:HPane:CopyEquation').clicked()
checkpoint toplevel widget mapped Dialog-Select a target subproblem
findWidget('Dialog-Select a target subproblem').resize(196, 182)
event(Gdk.EventType.BUTTON_PRESS,x= 9.4000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-Select a target subproblem:target:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
findWidget('Dialog-Select a target subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint OOF.Subproblem.Copy_Equation_State
assert tests.sensitization2()
assert tests.fieldButtonCheck(1, 0, 0)
assert tests.eqnButtonCheck(1)

event(Gdk.EventType.BUTTON_PRESS,x= 7.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Fields & Equations Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
checkpoint Field page sensitized
assert tests.sensitization2()
assert tests.fieldButtonCheck(1, 0, 0)
assert tests.eqnButtonCheck(1)

# Delete the new mesh
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(304, 86)
findWidget('Questioner:Yes').clicked()
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Mesh.Delete
findWidget('OOF2:Navigation:Next').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
assert tests.sensitization2()
assert tests.fieldButtonCheck(1, 0, 0)
assert tests.eqnButtonCheck(1)

# Delete a subproblem
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:subprobChooserScroll:subprobChooser').get_selection().select_path(Gtk.TreePath([1]))
checkpoint mesh page subproblems sensitized
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(343, 86)
findWidget('Questioner:Yes').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Delete
findWidget('OOF2:Navigation:Next').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
assert tests.sensitization2()
assert tests.fieldButtonCheck(1, 0, 0)
assert tests.eqnButtonCheck(1)

# Delete the mesh
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(283, 86)
findWidget('Questioner:Yes').clicked()
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Delete
findWidget('OOF2:Navigation:Next').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
assert tests.sensitization0()

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Python_Log']).activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(192, 122)
findWidget('Dialog-Python_Log:filename').set_text('d')
findWidget('Dialog-Python_Log:filename').set_text('dr')
findWidget('Dialog-Python_Log:filename').set_text('d')
findWidget('Dialog-Python_Log:filename').set_text('')
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
