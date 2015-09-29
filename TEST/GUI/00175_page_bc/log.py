checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.14 $
# $Author: langer $
# $Date: 2011/01/14 22:43:08 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Boundary Conditions')
assert tests.sensitization0()
findMenu(findWidget('OOF2:MenuBar'), 'File:Load:Data').activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(194, 72)
findWidget('Dialog-Data:filename').set_text('e')
findWidget('Dialog-Data:filename').set_text('ex')
findWidget('Dialog-Data:filename').set_text('exa')
findWidget('Dialog-Data:filename').set_text('exam')
findWidget('Dialog-Data:filename').set_text('examp')
findWidget('Dialog-Data:filename').set_text('exampl')
findWidget('Dialog-Data:filename').set_text('example')
findWidget('Dialog-Data:filename').set_text('examples')
findWidget('Dialog-Data:filename').set_text('examples/')
findWidget('Dialog-Data:filename').set_text('examples/e')
findWidget('Dialog-Data:filename').set_text('examples/el')
findWidget('Dialog-Data:filename').set_text('examples/el_')
findWidget('Dialog-Data:filename').set_text('examples/el_s')
findWidget('Dialog-Data:filename').set_text('examples/el_sh')
findWidget('Dialog-Data:filename').set_text('examples/el_sha')
findWidget('Dialog-Data:filename').set_text('examples/el_shap')
findWidget('Dialog-Data:filename').set_text('examples/el_shape')
findWidget('Dialog-Data:filename').set_text('examples/el_shape.')
findWidget('Dialog-Data:filename').set_text('examples/el_shape.m')
findWidget('Dialog-Data:filename').set_text('examples/el_shape.me')
findWidget('Dialog-Data:filename').set_text('examples/el_shape.mes')
findWidget('Dialog-Data:filename').set_text('examples/el_shape.mesh')
findWidget('Dialog-Data:gtk-ok').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint meshable button set
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
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
findWidget('OOF2 Activity Viewer').resize(400, 300)
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
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
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.File.Load.Data
findWidget('OOF2 Activity Viewer').resize(400, 300)
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path((0,))
assert tests.sensitization1()
assert tests.bcNameCheck('bc', 'bc<2>', 'bc<3>', 'bc<4>', 'bc<5>')
assert tests.bcSelectCheck('bc')
findWidget('OOF2:Boundary Conditions Page:Condition:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename the boundary condition "bc"
findWidget('Dialog-Rename the boundary condition "bc"').resize(194, 72)
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('l')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('le')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('lef')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('left')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('left-')
findWidget('Dialog-Rename the boundary condition "bc":name').set_text('left-x')
findWidget('Dialog-Rename the boundary condition "bc":gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(553, 200)
checkpoint OOF.Mesh.Boundary_Conditions.Rename
assert tests.bcNameCheck
assert tests.bcSelectCheck('left-x')
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path((0,))
findWidget('OOF2:Boundary Conditions Page:Condition:Edit').clicked()
checkpoint toplevel widget mapped Dialog-Edit Boundary Condition
findWidget('Dialog-Edit Boundary Condition').resize(399, 276)
setComboBox(findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Chooser'), 'Continuum Profile')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('y')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('y*')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('y*0')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('y*0.')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('y*0.0')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('y*0.01')
findWidget('Dialog-Edit Boundary Condition:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(797, 200)
checkpoint OOF.Mesh.Boundary_Conditions.Edit
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<4>', 'bc<5>', 'left-x')
assert tests.sensitization1()
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path((2,))
assert tests.sensitization1()
findWidget('OOF2:Boundary Conditions Page:Condition:Delete').clicked()
checkpoint OOF.Mesh.Boundary_Conditions.Delete
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
assert tests.sensitization2()
findWidget('OOF2:Navigation:Prev').clicked()
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
findWidget('OOF2').resize(550, 482)
findWidget('OOF2:FE Mesh Page:Pane').set_position(131)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(331, 188)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
findWidget('OOF2:FE Mesh Page:Pane').set_position(131)
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
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
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Mesh.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Boundary Conditions')
setComboBox(findWidget('OOF2:Boundary Conditions Page:Mesh'), 'mesh')
findWidget('OOF2').resize(550, 482)
assert tests.chooserStateCheck('OOF2:Boundary Conditions Page:Mesh', 'mesh')
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path((0,))
setComboBox(findWidget('OOF2:Boundary Conditions Page:Mesh'), 'mesh<2>')
setComboBox(findWidget('OOF2:Boundary Conditions Page:Mesh'), 'mesh')
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path((2,))
assert tests.sensitization1()
findWidget('OOF2:Boundary Conditions Page:Condition:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Choose a name and boundary.
findWidget('Dialog-Choose a name and boundary.').resize(273, 188)
setComboBox(findWidget('Dialog-Choose a name and boundary.:mesh:Mesh'), 'mesh<2>')
findWidget('Dialog-Choose a name and boundary.:gtk-ok').clicked()
checkpoint OOF.Mesh.Boundary_Conditions.Copy
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
setComboBox(findWidget('OOF2:Boundary Conditions Page:Mesh'), 'mesh<2>')
assert tests.bcNameCheck('bc')
assert tests.bcSelectCheck(None)
assert tests.sensitization3()
setComboBox(findWidget('OOF2:Boundary Conditions Page:Mesh'), 'mesh')
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
assert tests.bcSelectCheck(None)
assert tests.sensitization2()
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path((0,))
assert tests.sensitization1()
findWidget('OOF2:Boundary Conditions Page:Condition:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Choose a name and boundary.
findWidget('Dialog-Choose a name and boundary.').resize(273, 188)
findWidget('Dialog-Choose a name and boundary.:name:Auto').clicked()
findWidget('Dialog-Choose a name and boundary.:name:Text').set_text('r')
findWidget('Dialog-Choose a name and boundary.:name:Text').set_text('re')
findWidget('Dialog-Choose a name and boundary.:name:Text').set_text('ren')
findWidget('Dialog-Choose a name and boundary.:name:Text').set_text('rena')
findWidget('Dialog-Choose a name and boundary.:name:Text').set_text('renam')
findWidget('Dialog-Choose a name and boundary.:name:Text').set_text('rename')
findWidget('Dialog-Choose a name and boundary.:name:Text').set_text('renamed')
findWidget('Dialog-Choose a name and boundary.:gtk-ok').clicked()
checkpoint OOF.Mesh.Boundary_Conditions.Copy
setComboBox(findWidget('OOF2:Boundary Conditions Page:Mesh'), 'mesh<2>')
assert tests.bcNameCheck('bc', 'renamed')
assert tests.bcSelectCheck(None)
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path((0,))
findWidget('OOF2:Boundary Conditions Page:Condition:Delete').clicked()
checkpoint OOF.Mesh.Boundary_Conditions.Delete
assert tests.bcNameCheck('renamed')
assert tests.bcSelectCheck(None)
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path((0,))
findWidget('OOF2:Boundary Conditions Page:Condition:Delete').clicked()
checkpoint OOF.Mesh.Boundary_Conditions.Delete
assert tests.bcNameCheck()
assert tests.sensitization0()
setComboBox(findWidget('OOF2:Boundary Conditions Page:Mesh'), 'mesh')
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
assert tests.sensitization2()
findWidget('OOF2:Boundary Conditions Page:Condition:CopyAll').clicked()
checkpoint toplevel widget mapped Dialog-Choose the target mesh.
findWidget('Dialog-Choose the target mesh.').resize(199, 136)
setComboBox(findWidget('Dialog-Choose the target mesh.:mesh:Mesh'), 'mesh<2>')
findWidget('Dialog-Choose the target mesh.:gtk-ok').clicked()
checkpoint OOF.Mesh.Boundary_Conditions.Copy_All
setComboBox(findWidget('OOF2:Boundary Conditions Page:Mesh'), 'mesh<2>')
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
assert tests.bcSelectCheck(None)
assert tests.sensitization3()
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
findWidget('OOF2:FE Mesh Page:Pane').set_position(131)
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(328, 94)
findWidget('Questioner:gtk-yes').clicked()
findWidget('OOF2:FE Mesh Page:Pane').set_position(131)
checkpoint mesh page subproblems sensitized
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Mesh.Delete
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Boundary Conditions')
assert tests.chooserCheck('OOF2:Boundary Conditions Page:Mesh', ['mesh'])
findWidget('OOF2').resize(550, 482)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
findWidget('OOF2:FE Mesh Page:Pane').set_position(131)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(331, 188)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
findWidget('OOF2:FE Mesh Page:Pane').set_position(131)
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
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
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Mesh.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Boundary Conditions')
assert tests.chooserCheck('OOF2:Boundary Conditions Page:Mesh', ['mesh', 'mesh<2>'])
assert tests.chooserStateCheck('OOF2:Boundary Conditions Page:Mesh', 'mesh')
setComboBox(findWidget('OOF2:Boundary Conditions Page:Mesh'), 'mesh<2>')
assert tests.sensitization7()
setComboBox(findWidget('OOF2:Boundary Conditions Page:Mesh'), 'mesh')
assert tests.sensitization8()
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
findWidget('OOF2:FE Mesh Page:Pane').set_position(131)
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(328, 94)
findWidget('Questioner:gtk-yes').clicked()
findWidget('OOF2:FE Mesh Page:Pane').set_position(131)
checkpoint mesh page subproblems sensitized
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Mesh.Delete
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Boundary Conditions')
assert tests.chooserCheck('OOF2:Boundary Conditions Page:Mesh', ['mesh'])
assert tests.sensitization4()
assert tests.bcNameCheck('bc<2>', 'bc<3>', 'bc<5>', 'left-x')
assert tests.bcSelectCheck(None)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
findWidget('OOF2').resize(593, 482)
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-ok').clicked()
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
checkpoint OOF.Skeleton.Delete
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Boundary Conditions')
assert tests.sensitization9()
assert tests.bcNameCheck()
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(194, 72)
findWidget('Dialog-Python_Log:filename').set_text('b')
findWidget('Dialog-Python_Log:filename').set_text('bc')
findWidget('Dialog-Python_Log:filename').set_text('bcp')
findWidget('Dialog-Python_Log:filename').set_text('bcpa')
findWidget('Dialog-Python_Log:filename').set_text('bcpag')
findWidget('Dialog-Python_Log:filename').set_text('bcpage')
findWidget('Dialog-Python_Log:filename').set_text('bcpage.')
findWidget('Dialog-Python_Log:filename').set_text('bcpage.l')
findWidget('Dialog-Python_Log:filename').set_text('bcpage.lo')
findWidget('Dialog-Python_Log:filename').set_text('bcpage.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('bcpage.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
