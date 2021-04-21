# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Test that the On/Off (EnableDisable) button on the boundary
# condition page works properly.
# This was test 00179_page_bc before the gtk3 upgrade.

import tests
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
checkpoint Materials page updated
checkpoint Materials page updated
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
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
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
checkpoint OOF.File.LoadStartUp.Data
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Materials page updated
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
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
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
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
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
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint OOF.File.LoadStartUp.Data
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer

# Load a couple of meshes from a data file via command line args. See
# the args file in the test directory.
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)
findWidget('OOF2').resize(782, 545)
findWidget('OOF2').resize(782, 545)

event(Gdk.EventType.BUTTON_PRESS,x= 1.0600000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
checkpoint page installed Boundary Conditions
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert not tests.bcDisabled(0)
assert not tests.bcDisabled(2)

findCellRenderer(findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList'), col=0, rend=0).emit('toggled', Gtk.TreePath(2))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Disable
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([2]))
assert not tests.bcDisabled(0)
assert tests.bcDisabled(2)

event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Conditions Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['el_shape.png']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([0]))
findCellRenderer(findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList'), col=0, rend=0).emit('toggled', Gtk.TreePath(0))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Disable
assert tests.bcDisabled(0)

event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Boundary Conditions Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['cyallow.png']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
findCellRenderer(findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList'), col=0, rend=0).emit('toggled', Gtk.TreePath(2))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Enable
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([2]))
assert not tests.bcDisabled(0)
assert not tests.bcDisabled(2)

# Deactivate the equation on the cyallow microstructure
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane').set_position(470)
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Force_Balance active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Deactivate
# Go back to the boundary condition page
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Boundary Conditions
assert not tests.bcDisabled(0)
assert not tests.bcDisabled(1)
assert not tests.bcDisabled(2)

findCellRenderer(findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList'), col=0, rend=0).emit('toggled', Gtk.TreePath(2))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Disable
assert not tests.bcDisabled(0)
assert not tests.bcDisabled(1)
assert tests.bcDisabled(2)

findCellRenderer(findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList'), col=0, rend=0).emit('toggled', Gtk.TreePath(2))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Enable
assert not tests.bcDisabled(0)
assert not tests.bcDisabled(1)
assert not tests.bcDisabled(2)

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
