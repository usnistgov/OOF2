checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.19 $
# $Author: langer $
# $Date: 2011/01/14 22:43:06 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint page installed FE Mesh
assert tests.sensitization0()
findWidget('OOF2').resize(550, 373)
findWidget('OOF2:FE Mesh Page:Pane').set_position(308)
findMenu(findWidget('OOF2:MenuBar'), 'File:Load:Data').activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(191, 71)
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
findWidget('Dialog-Data:gtk-ok').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint microstructure page sensitized
checkpoint active area status updated
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
checkpoint skeleton selection page groups sensitized
checkpoint Solver page sensitized
# checkpoint interface page updated
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
findWidget('OOF2 Activity Viewer').resize(400, 300)
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
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
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
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
# Create a new Mesh
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(345, 210)
# New mesh dialog starts in a self-consistent state, so 'ok is sensitive.
assert tests.is_sensitive('Dialog-Create a new mesh:gtk-ok')
setComboBox(findWidget('Dialog-Create a new mesh:element_types:Map'), '2')
# After changing just one of the interpolation order widgets, the OK
# button should not be sensitive
assert not tests.is_sensitive('Dialog-Create a new mesh:gtk-ok')
# After changing the other one, the button is sensitive again.
setComboBox(findWidget('Dialog-Create a new mesh:element_types:Func'), '2')
assert tests.is_sensitive('Dialog-Create a new mesh:gtk-ok')
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
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.New
findWidget('OOF2').resize(562, 373)
findWidget('OOF2:FE Mesh Page:Pane').set_position(320)
assert tests.sensitization2()
assert tests.subproblemNameCheck('default')
assert tests.selectedSubproblem('default')

# Create a material and assign it to pixels so we can test a
# nontrivial subproblem
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2').resize(685, 373)
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
findWidget('Dialog-Assign material material to pixels').resize(690, 106)
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
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane').set_position(443)
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new subproblem
findWidget('Dialog-Create a new subproblem').resize(291, 102)
setComboBox(findWidget('Dialog-Create a new subproblem:subproblem:Chooser'), 'Material')
findWidget('Dialog-Create a new subproblem').resize(311, 129)
findWidget('Dialog-Create a new subproblem:gtk-ok').clicked()
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.New
assert tests.sensitization3()
assert tests.subproblemNameCheck('default', 'subproblem')
assert tests.selectedSubproblem('subproblem')

# create a subproblem from the union of the two existing ones
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new subproblem
findWidget('Dialog-Create a new subproblem').resize(311, 129)
setComboBox(findWidget('Dialog-Create a new subproblem:subproblem:Chooser'), 'Union')
findWidget('Dialog-Create a new subproblem').resize(330, 156)
setComboBox(findWidget('Dialog-Create a new subproblem:subproblem:Union:another'), 'subproblem')
findWidget('Dialog-Create a new subproblem:gtk-ok').clicked()
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:subprobChooserScroll').get_vadjustment().set_value( 4.0000000000000e+00)
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.New
# check that "subproblem<2>" is selected
assert tests.subproblemNameCheck('default', 'subproblem', 'subproblem<2>')
assert tests.selectedSubproblem('subproblem<2>')
assert tests.sensitization3()
findWidget('OOF2 Messages 1').resize(756, 200)
# reselect the default subproblem
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:subprobChooserScroll:subprobChooser').get_selection().select_path((0,))
checkpoint mesh page subproblems sensitized
assert tests.subproblemNameCheck('default', 'subproblem', 'subproblem<2>')
assert tests.selectedSubproblem('default')
assert tests.sensitization2()

# delete one of the subproblems that the union was built from
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:subprobChooserScroll:subprobChooser').get_selection().select_path((1,))
checkpoint mesh page subproblems sensitized
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(368, 93)
findWidget('Questioner:gtk-yes').clicked()
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
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:subprobChooserScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2:FE Mesh Page:Pane:Subproblems:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new subproblem
findWidget('Dialog-Create a new subproblem').resize(300, 156)
setComboBox(findWidget('Dialog-Create a new subproblem:subproblem:Chooser'), 'PixelGroup')
findWidget('Dialog-Create a new subproblem').resize(747, 156)
setComboBox(findWidget('Dialog-Create a new subproblem:subproblem:PixelGroup:group'), 'RGBColor(red=1.000000, green=1.000000, blue=0.752941)')
findWidget('Dialog-Create a new subproblem:gtk-ok').clicked()
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.New
# check subproblem list, selection, and sensitization
assert tests.sensitization3()
assert tests.subproblemNameCheck('default', 'subproblem')
assert tests.selectedSubproblem('subproblem')

# create a new skeleton
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(304)
findWidget('OOF2').resize(705, 424)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane').set_position(324)
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(394, 198)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
checkpoint skeleton page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint OOF.Skeleton.New
checkpoint skeleton page sensitized
# switch to the new skeleton on the  mesh page.
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane').set_position(463)
setComboBox(findWidget('OOF2:FE Mesh Page:Skeleton'), 'skeleton<2>')
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
assert tests.sensitization1()
assert tests.subproblemNameCheck()
assert tests.selectedSubproblem(None)

# Create a new mesh for the new skeleton
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(345, 210)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
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
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Mesh.New
assert tests.sensitization2()
assert tests.subproblemNameCheck('default')
assert tests.selectedSubproblem('default')

# Switch back to first skeleton
setComboBox(findWidget('OOF2:FE Mesh Page:Skeleton'), 'skeleton')
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
# Check subp. list and sensitization
assert tests.sensitization2()
assert tests.subproblemNameCheck('default', 'subproblem')
assert tests.selectedSubproblem('default')

# Create a second mesh for the first skeleton
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(345, 210)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
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
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Mesh.New
# Check subp list and sensitization
assert tests.sensitization2()
assert tests.subproblemNameCheck('default')
assert tests.selectedSubproblem('default')

# Switch to second skeleton and delete it
setComboBox(findWidget('OOF2:FE Mesh Page:Skeleton'), 'skeleton<2>')
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
checkpoint skeleton page sensitized
findWidget('Questioner').resize(225, 93)
findWidget('Questioner:gtk-ok').clicked()
checkpoint skeleton page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
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
checkpoint OOF.Skeleton.Delete
checkpoint skeleton page sensitized
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint page installed FE Mesh
# Check that first skeleton is displayed with first mesh
assert tests.selectedSubproblem(None)
assert tests.subproblemNameCheck('default', 'subproblem')
assert tests.sensitization4()

# Switch to second mesh
setComboBox(findWidget('OOF2:FE Mesh Page:Mesh'), 'mesh<2>')
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
# Check second mesh's subproblems are now displayed.
assert tests.subproblemNameCheck('default')
assert tests.selectedSubproblem('default')
assert tests.sensitization2()

# Delete mesh
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(324, 93)
findWidget('Questioner:gtk-yes').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Mesh.Delete
# check subproblem list, no selection
assert tests.sensitization4()
assert tests.selectedSubproblem(None)
assert tests.subproblemNameCheck('default', 'subproblem')

# delete mesh
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(296, 93)
findWidget('Questioner:gtk-yes').clicked()
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
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Delete
# Check sensitization, empty subp list.
assert tests.sensitization1()
assert tests.selectedSubproblem(None)
assert tests.subproblemNameCheck()

findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(191, 98)
findWidget('Dialog-Python_Log:filename').set_text('m')
findWidget('Dialog-Python_Log:filename').set_text('me')
findWidget('Dialog-Python_Log:filename').set_text('mes')
findWidget('Dialog-Python_Log:filename').set_text('mesh')
findWidget('Dialog-Python_Log:filename').set_text('meshp')
findWidget('Dialog-Python_Log:filename').set_text('meshpa')
findWidget('Dialog-Python_Log:filename').set_text('meshpag')
findWidget('Dialog-Python_Log:filename').set_text('meshpage')
findWidget('Dialog-Python_Log:filename').set_text('meshpage.')
findWidget('Dialog-Python_Log:filename').set_text('meshpage.l')
findWidget('Dialog-Python_Log:filename').set_text('meshpage.lo')
findWidget('Dialog-Python_Log:filename').set_text('meshpage.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('meshpage.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
