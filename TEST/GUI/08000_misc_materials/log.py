checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.12 $
# $Author: gdogan $
# $Date: 2011/02/14 14:44:10 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Check that when materials are deleted entirely, or just removed from
# pixels, that the Solver page is sensitized correctly.

import tests

# Create a Microstructure
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
findWidget('OOF2').resize(579, 350)
findWidget('OOF2:Microstructure Page:Pane').set_position(158)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('Dialog-Create Microstructure').resize(314, 168)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane').set_position(161)
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint microstructure page sensitized
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint pixel page sensitized
checkpoint meshable button set
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

# Create a second Microstructure
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(314, 168)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint meshable button set
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
checkpoint OOF.Microstructure.New

# Create a Material
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2').resize(684, 350)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(249, 72)
findWidget('Dialog-New material:gtk-ok').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.New

# Add a Material Property (isotropic elasticity)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((0,))
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1,), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 0, 0))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
widget_0=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_0.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_0.window))
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Assign the material to all pixels in the first microstructure
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(292, 108)
findWidget('Dialog-Assign material material to pixels:gtk-ok').clicked()
checkpoint OOF.Material.Assign

# Create a second material
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(249, 72)
findWidget('Dialog-New material:gtk-ok').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.New

# Add a property to the second material
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
findWidget('OOF2:Materials Page:Pane').set_position(272)
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Assign the second material to pixels in the second microstructure
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material<2> to pixels
findWidget('Dialog-Assign material material<2> to pixels').resize(292, 108)
setComboBox(findWidget('Dialog-Assign material material<2> to pixels:microstructure:Microstructure'), 'microstructure<2>')
setComboBox(findWidget('Dialog-Assign material material<2> to pixels:pixels'), '<every>')
findWidget('Dialog-Assign material material<2> to pixels:gtk-ok').clicked()
checkpoint OOF.Material.Assign

# Assign the first material to pixels in the first microstructure (again!?)
findWidget('OOF2').resize(684, 350)
setComboBox(findWidget('OOF2:Materials Page:Pane:Material:MaterialList'), 'material')
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(292, 108)
setComboBox(findWidget('Dialog-Assign material material to pixels:microstructure:Microstructure'), 'microstructure')
setComboBox(findWidget('Dialog-Assign material material to pixels:pixels'), '<every>')
findWidget('Dialog-Assign material material to pixels:gtk-ok').clicked()
checkpoint OOF.Material.Assign

# Create a Skeleton on the second Microstructure
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2').resize(691, 434)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane').set_position(350)
findWidget('OOF2:Skeleton Page:Simple').clicked()
checkpoint toplevel widget mapped Dialog-Simple skeleton
checkpoint skeleton page sensitized
findWidget('Dialog-Simple skeleton').resize(389, 154)
findWidget('Dialog-Simple skeleton:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(473, 200)
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
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
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint OOF.Skeleton.Simple
checkpoint skeleton selection page updated
findWidget('OOF2:Skeleton Page:Pane').set_position(350)

# Create a Skeleton on the first Microstructure
setComboBox(findWidget('OOF2:Skeleton Page:Microstructure'), 'microstructure')
findWidget('OOF2:Skeleton Page:Pane').set_position(350)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(389, 202)
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
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.New

# Create a Mesh on the first Microstructure
findWidget('OOF2:Skeleton Page:Pane').set_position(350)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(331, 188)
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
checkpoint Solver page sensitized
checkpoint OOF.Mesh.New

# Create a Mesh on the second Microstructure
setComboBox(findWidget('OOF2:FE Mesh Page:Microstructure'), 'microstructure<2>')
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(331, 188)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
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
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Mesh.New

# Define Fields and activate Equations on the first Microstructure
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Fields & Equations')
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2').resize(716, 434)
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Undefine
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement in-plane').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Field.In_Plane

# Define Fields and activate Equations on the second Microstructure
setComboBox(findWidget('OOF2:Fields & Equations Page:Microstructure'), 'microstructure<2>')
checkpoint Field page sensitized
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Field page sensitized
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement in-plane').clicked()
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Mesh.Field.In_Plane
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Force_Balance active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint OOF.Subproblem.Equation.Activate
setComboBox(findWidget('OOF2:Fields & Equations Page:Microstructure'), 'microstructure')
checkpoint Field page sensitized
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Force_Balance active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Activate

# Set a Solver for the first Microstructure
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((0,))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:Subproblems:Set').clicked()
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(423, 212)
findWidget('Dialog-Specify Solver:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
assert tests.sensitive(1)

# Solve the first Microstructure
findWidget('OOF2:Solver Page:end').set_text('0')
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Solve
assert tests.sensitive(1)

# Set a Solver for the second Microstructure
setComboBox(findWidget('OOF2:Solver Page:Microstructure'), 'microstructure<2>')
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((0,))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:Subproblems:Set').clicked()
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(423, 212)
findWidget('Dialog-Specify Solver:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
assert tests.sensitive(1)

# Solve the second Microstructure
findWidget('OOF2:Solver Page:end').set_text('0')
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Solve
assert tests.sensitive(1)

# Delete the Material used in the first Microstructure
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-ok').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Material.Delete

# Switch to the Solver page and check the sensitization of the Solve
# button, which should be sensitized because the second Microstructure
# is selected.
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.sensitive(1)
# Switch to the first Microstructure and check that the Solve button
# is desensitized.
setComboBox(findWidget('OOF2:Solver Page:Microstructure'), 'microstructure')
checkpoint Solver page sensitized
assert tests.sensitive(0)

# Remove the second Material from the second Microstructure
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Material:RemoveMaterial').clicked()
checkpoint toplevel widget mapped Dialog-Remove the assigned material from pixels
findWidget('Dialog-Remove the assigned material from pixels').resize(292, 108)
setComboBox(findWidget('Dialog-Remove the assigned material from pixels:microstructure:Microstructure'), 'microstructure<2>')
setComboBox(findWidget('Dialog-Remove the assigned material from pixels:pixels'), '<every>')
findWidget('Dialog-Remove the assigned material from pixels:gtk-ok').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Material.Remove

# Switch to the Solver page and check that the Solve button is desensitized.
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint page installed Solver
assert tests.sensitive(0)

findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(194, 72)
findWidget('Dialog-Python_Log:filename').set_text('m')
findWidget('Dialog-Python_Log:filename').set_text('mi')
findWidget('Dialog-Python_Log:filename').set_text('mis')
findWidget('Dialog-Python_Log:filename').set_text('misc')
findWidget('Dialog-Python_Log:filename').set_text('miscm')
findWidget('Dialog-Python_Log:filename').set_text('miscma')
findWidget('Dialog-Python_Log:filename').set_text('miscmat')
findWidget('Dialog-Python_Log:filename').set_text('miscmat.')
findWidget('Dialog-Python_Log:filename').set_text('miscmat.l')
findWidget('Dialog-Python_Log:filename').set_text('miscmat.lo')
findWidget('Dialog-Python_Log:filename').set_text('miscmat.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('miscmat.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
