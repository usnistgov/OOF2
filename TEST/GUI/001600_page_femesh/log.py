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
findWidget('OOF2').resize(782, 511)
event(Gdk.EventType.BUTTON_PRESS,x= 1.0100000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(119)
findWidget('OOF2').resize(782, 545)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(130)
assert tests.sensitization0()

# Load a skeleton
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('e')
findWidget('Dialog-Data:filename').set_text('ex')
findWidget('Dialog-Data:filename').set_text('exa')
findWidget('Dialog-Data:filename').set_text('exam')
findWidget('Dialog-Data:filename').set_text('examp')
findWidget('Dialog-Data:filename').set_text('exampl')
findWidget('Dialog-Data:filename').set_text('example')
findWidget('Dialog-Data:filename').set_text('examples')
findWidget('Dialog-Data:filename').set_text('examples/')
findWidget('Dialog-Data:filename').set_text('examples/t')
findWidget('Dialog-Data:filename').set_text('examples/tr')
findWidget('Dialog-Data:filename').set_text('examples/tri')
findWidget('Dialog-Data:filename').set_text('examples/tria')
findWidget('Dialog-Data:filename').set_text('examples/trian')
findWidget('Dialog-Data:filename').set_text('examples/triang')
findWidget('Dialog-Data:filename').set_text('examples/triangl')
findWidget('Dialog-Data:filename').set_text('examples/triangle')
findWidget('Dialog-Data:filename').set_text('examples/triangle.')
findWidget('Dialog-Data:filename').set_text('examples/triangle.s')
findWidget('Dialog-Data:filename').set_text('examples/triangle.sk')
findWidget('Dialog-Data:filename').set_text('examples/triangle.ske')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skel')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skele')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skelet')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skeleto')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skeleton')
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
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Element
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
assert tests.sensitization1()

# Create a Mesh
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(299, 244)
# New mesh dialog starts in a self-consistent state, so 'ok is sensitive.
assert tests.is_sensitive('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK')
event(Gdk.EventType.BUTTON_PRESS,x= 5.1000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-Create a new mesh:element_types:Map').get_window())
checkpoint toplevel widget mapped chooserPopup-Map
findMenu(findWidget('chooserPopup-Map'), ['2']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Map') # MenuItemLogger
# After changing just one of the interpolation order widgets, the OK
# button should not be sensitive
assert not tests.is_sensitive('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK')

# After changing the other one, the button is sensitive again.
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-Create a new mesh:element_types:Func').get_window())
checkpoint toplevel widget mapped chooserPopup-Func
findMenu(findWidget('chooserPopup-Func'), ['2']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Func') # MenuItemLogger
assert tests.is_sensitive('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK')

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
assert tests.sensitization2()
assert tests.subproblemNameCheck('default')
assert tests.selectedSubproblem('default')

# Create a material and assign it to pixels so we can test a
# nontrivial subproblem

event(Gdk.EventType.BUTTON_PRESS,x= 8.6000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
findWidget('Dialog-Assign material material to pixels').resize(221, 122)
event(Gdk.EventType.BUTTON_PRESS,x= 4.8000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('Dialog-Assign material material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['<every>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Material.Assign
# Create a subproblem
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
event(Gdk.EventType.BUTTON_PRESS,x= 6.0000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-Create a new subproblem:subproblem:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Material']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Create a new subproblem').resize(257, 164)
findWidget('Dialog-Create a new subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.New
assert tests.sensitization3()
assert tests.subproblemNameCheck('default', 'subproblem')
assert tests.selectedSubproblem('subproblem')

# create a subproblem from the union of the two existing ones
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new subproblem
findWidget('Dialog-Create a new subproblem').resize(257, 164)
event(Gdk.EventType.BUTTON_PRESS,x= 4.8000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('Dialog-Create a new subproblem:subproblem:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Union']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Create a new subproblem').resize(257, 194)
event(Gdk.EventType.BUTTON_PRESS,x= 3.7000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-Create a new subproblem:subproblem:Union:another').get_window())
checkpoint toplevel widget mapped chooserPopup-another
findMenu(findWidget('chooserPopup-another'), ['subproblem']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-another') # MenuItemLogger
findWidget('Dialog-Create a new subproblem').resize(275, 194)
findWidget('Dialog-Create a new subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.New
# check that "subproblem<2>" is selected
assert tests.subproblemNameCheck('default', 'subproblem', 'subproblem<2>')
assert tests.selectedSubproblem('subproblem<2>')
assert tests.sensitization3()

# reselect the default subproblem
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:subprobChooserScroll:subprobChooser').get_selection().select_path(Gtk.TreePath([0]))
checkpoint mesh page subproblems sensitized
assert tests.subproblemNameCheck('default', 'subproblem', 'subproblem<2>')
assert tests.selectedSubproblem('default')
assert tests.sensitization2()

# delete one of the subproblems that the union was built from
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:subprobChooserScroll:subprobChooser').get_selection().select_path(Gtk.TreePath([1]))
checkpoint mesh page subproblems sensitized
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(323, 86)
findWidget('Questioner:Yes').clicked()
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Delete
# check that only the original default subproblem is left, and that
# it's selected
assert tests.sensitization2()
assert tests.subproblemNameCheck('default')
assert tests.selectedSubproblem('default')

# create a subproblem from a pixel group
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new subproblem
findWidget('Dialog-Create a new subproblem').resize(249, 194)
event(Gdk.EventType.BUTTON_PRESS,x= 4.7000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('Dialog-Create a new subproblem:subproblem:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['PixelGroup']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Create a new subproblem').resize(520, 194)
event(Gdk.EventType.BUTTON_PRESS,x= 6.9000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-Create a new subproblem:subproblem:PixelGroup:group').get_window())
checkpoint toplevel widget mapped chooserPopup-group
findMenu(findWidget('chooserPopup-group'), ['RGBColor(red=1.000000, green=1.000000, blue=0.752941)']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-group') # MenuItemLogger
findWidget('Dialog-Create a new subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.New
# check subproblem list, selection, and sensitization
assert tests.sensitization3()
assert tests.subproblemNameCheck('default', 'subproblem')
assert tests.selectedSubproblem('subproblem')

# create a new skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
checkpoint skeleton page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton page info updated
checkpoint OOF.Skeleton.New
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
# # switch to the new skeleton on the  mesh page.

event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 2.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
event(Gdk.EventType.BUTTON_PRESS,x= 8.4000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:FE Mesh Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
assert tests.sensitization1()
assert tests.subproblemNameCheck()
assert tests.selectedSubproblem(None)

# Create a new mesh for the new skeleton
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
assert tests.sensitization2()
assert tests.subproblemNameCheck('default')
assert tests.selectedSubproblem('default')

# Switch back to first skeleton
event(Gdk.EventType.BUTTON_PRESS,x= 5.4000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:FE Mesh Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
# Check subp. list and sensitization
assert tests.sensitization2()
assert tests.subproblemNameCheck('default', 'subproblem')
assert tests.selectedSubproblem('default')

# Create a second mesh for the first skeleton
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
# Check subp list and sensitization
assert tests.sensitization2()
assert tests.subproblemNameCheck('default')
assert tests.selectedSubproblem('default')

# Check that mesh chooser is set to "mesh<2>"
assert tests.chooserStateCheck('OOF2:FE Mesh Page:Mesh', 'mesh<2>')

# Switch to second skeleton and delete it
event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:FE Mesh Page:Skeleton').get_window())
checkpoint toplevel widget mapped chooserPopup-Skeleton
findMenu(findWidget('chooserPopup-Skeleton'), ['skeleton<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Skeleton') # MenuItemLogger
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 1.0100000000000e+02,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(199, 86)
findWidget('Questioner:OK').clicked()
checkpoint skeleton page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint OOF.Skeleton.Delete
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
# # Check that first skeleton is displayed with first mesh
assert tests.selectedSubproblem(None)
assert tests.subproblemNameCheck('default', 'subproblem')
assert tests.sensitization4()

# # Switch to second mesh

event(Gdk.EventType.BUTTON_PRESS,x= 7.8000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:FE Mesh Page:Mesh').get_window())
checkpoint toplevel widget mapped chooserPopup-Mesh
findMenu(findWidget('chooserPopup-Mesh'), ['mesh<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Mesh') # MenuItemLogger
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
# # Check second mesh's subproblems are now displayed.
assert tests.subproblemNameCheck('default')
assert tests.selectedSubproblem('default')
assert tests.sensitization2()

# # Delete mesh

findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(284, 86)
findWidget('Questioner:Yes').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Mesh.Delete
# # check subproblem list, no selection
assert tests.sensitization4()
assert tests.selectedSubproblem(None)
assert tests.subproblemNameCheck('default', 'subproblem')

# # delete mesh

findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(263, 86)
findWidget('Questioner:Yes').clicked()
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
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
# # Check sensitization, empty subp list.
assert tests.sensitization1()
assert tests.selectedSubproblem(None)
assert tests.subproblemNameCheck()

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
assert tests.filediff("session.log")
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
