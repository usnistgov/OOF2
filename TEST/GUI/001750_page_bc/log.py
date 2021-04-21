# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
checkpoint page installed Boundary Conditions
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.sensitization0()

# Load a Mesh
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('examples/el_shape.mesh')
findWidget('Dialog-Data:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
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
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page sensitized
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
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.File.Load.Data

# Select the first bc
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([0]))
assert tests.sensitization1()
assert tests.bcNameCheck('bc', 'bc<2>', 'bc<3>', 'bc<4>', 'bc<5>')
assert tests.bcSelectCheck('bc')

# Rename
findWidget('OOF2:Boundary Conditions Page:Condition:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename the boundary condition "bc"
findWidget('Dialog-Rename the boundary condition "bc"').resize(192, 92)
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('l')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('le')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('lev')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('le')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('lef')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('left')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('left-')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('left-x')
findWidget('Dialog-Rename the boundary condition "bc":widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Boundary_Conditions.Rename
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<4>', 'bc<5>', 'left-x')
assert tests.bcSelectCheck('left-x')

# Select bc<2> and edit it
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([0]))
findWidget('OOF2:Boundary Conditions Page:Condition:Edit').clicked()
checkpoint toplevel widget mapped Dialog-Edit Boundary Condition
findWidget('Dialog-Edit Boundary Condition').resize(353, 326)
event(Gdk.EventType.BUTTON_PRESS,x= 7.7000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Continuum Profile']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Edit Boundary Condition').resize(407, 398)
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('y')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('y*')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('y*0')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('y*0.')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('y*0.0')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('y*0.01')
findWidget('Dialog-Edit Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Edit
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<4>', 'bc<5>', 'left-x')
assert tests.sensitization1()

# Select and delete bc<4>
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([2]))
findWidget('OOF2:Boundary Conditions Page:Condition:Delete').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Delete
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
assert tests.sensitization2()

# Create a new Mesh
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane').set_position(470)
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint mesh page sensitized
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
event(Gdk.EventType.BUTTON_PRESS,x= 7.4000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
checkpoint page installed Boundary Conditions
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.chooserStateCheck('OOF2:Boundary Conditions Page:Mesh', 'mesh')

# switch to the new mesh
event(Gdk.EventType.BUTTON_PRESS,x= 3.4000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Conditions Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
assert tests.bcNameCheck()
assert tests.sensitization0()   # no field or eqn defined, so New isn't active

# switch back to the first mesh
event(Gdk.EventType.BUTTON_PRESS,x= 3.9000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Conditions Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
# select bc<5>
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([2]))
assert tests.sensitization1()

# Copy the bc
findWidget('OOF2:Boundary Conditions Page:Condition:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Choose a name and boundary.
findWidget('Dialog-Choose a name and boundary.').resize(205, 218)
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-Choose a name and boundary.:mesh:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
findWidget('Dialog-Choose a name and boundary.:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Copy
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')

# Switch to the new mesh
event(Gdk.EventType.BUTTON_PRESS,x= 4.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Conditions Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
assert tests.bcNameCheck('bc')
assert tests.bcSelectCheck(None)
assert tests.sensitization3()

# switch back to the original mesh
event(Gdk.EventType.BUTTON_PRESS,x= 3.6000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Boundary Conditions Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
assert tests.bcSelectCheck(None)
assert tests.sensitization2()

# Select bc<2>
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([0]))
assert tests.sensitization1()

# Copy the bc to the other mesh with a new name
findWidget('OOF2:Boundary Conditions Page:Condition:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Choose a name and boundary.
findWidget('Dialog-Choose a name and boundary.').resize(205, 218)
findWidget('Dialog-Choose a name and boundary.:name').delete_text(0, 11)
findWidget('Dialog-Choose a name and boundary.:name').insert_text('r', 11)
findWidget('Dialog-Choose a name and boundary.:name').insert_text('e', 1)
findWidget('Dialog-Choose a name and boundary.:name').insert_text('n', 2)
findWidget('Dialog-Choose a name and boundary.:name').insert_text('a', 3)
findWidget('Dialog-Choose a name and boundary.:name').insert_text('m', 4)
findWidget('Dialog-Choose a name and boundary.:name').insert_text('e', 5)
findWidget('Dialog-Choose a name and boundary.:name').insert_text('d', 6)
findWidget('Dialog-Choose a name and boundary.:name').insert_text('d', 7)
findWidget('Dialog-Choose a name and boundary.:name').delete_text(7, 8)
findWidget('Dialog-Choose a name and boundary.:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Copy
event(Gdk.EventType.BUTTON_PRESS,x= 4.3000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Conditions Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
assert tests.bcNameCheck('bc', 'renamed')
assert tests.bcSelectCheck(None)

# Select the first bc in the new mesh
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([0]))
# Delete it
findWidget('OOF2:Boundary Conditions Page:Condition:Delete').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Delete
assert tests.bcNameCheck('renamed')
assert tests.bcSelectCheck(None)

# Select and delete the other bc
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([0]))
findWidget('OOF2:Boundary Conditions Page:Condition:Delete').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Delete
assert tests.bcNameCheck()
assert tests.sensitization0()

# switch back to the original mesh
event(Gdk.EventType.BUTTON_PRESS,x= 5.2000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Conditions Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
assert tests.sensitization2()

# Copy all bcs to the other mesh
findWidget('OOF2:Boundary Conditions Page:Condition:CopyAll').clicked()
checkpoint toplevel widget mapped Dialog-Choose the target mesh.
findWidget('Dialog-Choose the target mesh.').resize(192, 152)
event(Gdk.EventType.BUTTON_PRESS,x= 8.9000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-Choose the target mesh.:mesh:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
findWidget('Dialog-Choose the target mesh.:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Copy_All
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
assert tests.bcSelectCheck(None)
assert tests.sensitization2()

event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Boundary Conditions Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
assert tests.bcSelectCheck(None)
assert tests.sensitization3()

# Delete the new mesh
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Conditions Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findWidget('chooserPopup-Mesh').deactivate() # MenuLogger
event(Gdk.EventType.BUTTON_PRESS,x= 4.6000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(293, 86)
findWidget('Questioner:Yes').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Mesh.Delete
event(Gdk.EventType.BUTTON_PRESS,x= 9.4000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
checkpoint page installed Boundary Conditions
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
assert tests.bcSelectCheck(None)
assert tests.sensitization2()

# Create a new mesh again
event(Gdk.EventType.BUTTON_PRESS,x= 5.7000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
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
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Boundary Conditions
assert tests.chooserCheck('OOF2:Boundary Conditions Page:Mesh', ['mesh', 'mesh<2>'])
assert tests.chooserStateCheck('OOF2:Boundary Conditions Page:Mesh', 'mesh')

event(Gdk.EventType.BUTTON_PRESS,x= 5.7000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Conditions Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
assert tests.sensitization0()

event(Gdk.EventType.BUTTON_PRESS,x= 5.1000000000000e+01,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Boundary Conditions Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
assert tests.sensitization2()

# Delete the new mesh
findWidget('OOF2:Navigation:NextHist').clicked()
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(293, 86)
findWidget('Questioner:Yes').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Mesh.Delete
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Boundary Conditions
assert tests.chooserCheck('OOF2:Boundary Conditions Page:Mesh', ['mesh'])
assert tests.sensitization2()
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
assert tests.bcSelectCheck(None)

# Delete the Skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 4.4000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint skeleton page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(192, 86)
findWidget('Questioner:OK').clicked()
checkpoint skeleton page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.Delete
event(Gdk.EventType.BUTTON_PRESS,x= 5.4000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
checkpoint page installed Boundary Conditions
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.sensitization0()
assert tests.bcNameCheck()

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
