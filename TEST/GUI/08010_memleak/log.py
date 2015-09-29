# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.10 $
# $Author: langer $
# $Date: 2010/12/27 07:24:50 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import tests

findWidget('OOF2:Navigation:Next').clicked()
findWidget('OOF2').resize(585, 350)
findWidget('OOF2:Microstructure Page:Pane').set_position(161)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(316, 163)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(166)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
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
checkpoint OOF.Microstructure.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
findWidget('OOF2:Skeleton Page:Pane').set_position(227)
findWidget('OOF2').resize(712, 424)
findWidget('OOF2:Skeleton Page:Pane').set_position(354)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(397, 198)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(542, 200)
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint mesh bdy page updated
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
checkpoint skeleton selection page updated
checkpoint OOF.Skeleton.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
findWidget('OOF2:FE Mesh Page:Pane').set_position(418)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(338, 210)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
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
findWidget('OOF2:Navigation:Next').clicked()
findWidget('OOF2:Fields & Equations Page:HPane').set_position(129)
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature defined').clicked()
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Temperature active').clicked()
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Heat_Eqn active').clicked()
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Subproblem.Equation.Activate
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Boundary Conditions')
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(408, 267)
findWidget('Dialog-New Boundary Condition:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(799, 200)
checkpoint OOF.Mesh.Boundary_Conditions.New
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(408, 267)
setComboBox(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary'), 'bottom')
setComboBox(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Chooser'), 'Constant Profile')
findWidget('Dialog-New Boundary Condition').resize(408, 271)
findWidget('Dialog-New Boundary Condition:gtk-ok').clicked()
checkpoint OOF.Mesh.Boundary_Conditions.New
findWidget('OOF2').resize(712, 424)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(315, 93)
findWidget('Questioner:gtk-yes').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Mesh.Delete
assert tests.objectInventory(microstructures=1, nodes=25, elements=16, meshes=0)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(198, 93)
findWidget('Questioner:gtk-ok').clicked()
checkpoint skeleton page sensitized
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
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
checkpoint OOF.Skeleton.Delete
assert tests.objectInventory(microstructures=1, nodes=0, elements=0, meshes=0)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
findWidget('OOF2:Microstructure Page:Pane').set_position(203)
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(219, 93)
findWidget('Questioner:gtk-yes').clicked()
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
# checkpoint interface page updated
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint OOF.Microstructure.Delete
assert tests.objectInventory(microstructures=0, nodes=0, elements=0, meshes=0)
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
checkpoint Move Node toolbox info updated
findWidget('OOF2 Graphics 1:Pane0').set_position(285)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(691)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1').resize(800, 400)
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(714)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(316, 163)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(203)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
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
# checkpoint interface page updated
checkpoint OOF.Microstructure.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(397, 198)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint mesh bdy page updated
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
checkpoint skeleton selection page updated
checkpoint OOF.Skeleton.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(338, 210)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
checkpoint toplevel widget mapped Warning
findWidget('Warning').resize(383, 82)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2 Activity Viewer').resize(400, 300)
findWidget('Warning:OK').clicked()
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
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
findWidget('OOF2:Materials Page:Pane').set_position(278)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(302, 98)
findWidget('Dialog-New material:gtk-ok').clicked()
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(276, 106)
setComboBox(findWidget('Dialog-Assign material material to pixels:pixels'), '<every>')
findWidget('Dialog-Assign material material to pixels:gtk-ok').clicked()
checkpoint OOF.Material.Assign
findWidget('OOF2 Graphics 1').resize(800, 400)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
findWidget('OOF2:FE Mesh Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(315, 93)
findWidget('Questioner:gtk-yes').clicked()
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint mesh page subproblems sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Mesh.Delete
assert tests.objectInventory(microstructures=1, nodes=25, elements=16, meshes=0)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(198, 93)
findWidget('Questioner:gtk-ok').clicked()
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
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
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
checkpoint OOF.Skeleton.Delete
assert tests.objectInventory(microstructures=1, nodes=0, elements=0, meshes=0)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(219, 93)
findWidget('Questioner:gtk-yes').clicked()
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
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
# checkpoint interface page updated
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint OOF.Microstructure.Delete
assert tests.objectInventory(microstructures=0, nodes=0, elements=0, meshes=0)
widget_0=findWidget('OOF2 Graphics 1')
handled_0=widget_0.event(event(gtk.gdk.DELETE,window=widget_0.window))
postpone if not handled_0: widget_0.destroy()
checkpoint OOF.Graphics_1.File.Close
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(316, 163)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(203)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
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
# checkpoint interface page updated
checkpoint OOF.Microstructure.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(276, 106)
setComboBox(findWidget('Dialog-Assign material material to pixels:pixels'), '<every>')
findWidget('Dialog-Assign material material to pixels:gtk-ok').clicked()
checkpoint OOF.Material.Assign
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(397, 198)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint mesh bdy page updated
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
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(397, 198)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Skeleton.New
checkpoint skeleton page sensitized
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(338, 210)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
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
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(338, 210)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
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
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
checkpoint Move Node toolbox info updated
findWidget('OOF2 Graphics 1:Pane0').set_position(285)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(691)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1').resize(800, 400)
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(714)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1').resize(800, 400)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'Layer:New').activate()
checkpoint layereditor layerset changed
checkpoint toplevel widget mapped OOF2 Graphics Layer Editor
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.New
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:category'), 'Mesh')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
findWidget('OOF2 Graphics Layer Editor:NewLayer').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.New
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:category'), 'Mesh')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:object:Skeleton'), 'skeleton<2>')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:New').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Mesh mesh
findWidget('Dialog-New Display Method for Mesh mesh').resize(350, 227)
findWidget('Dialog-New Display Method for Mesh mesh:gtk-ok').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Add_Method
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:object:Mesh'), 'mesh<2>')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:New').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Mesh mesh<2>
findWidget('Dialog-New Display Method for Mesh mesh<2>').resize(350, 227)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:width:slider').get_adjustment().set_value( 1.1627906976744e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:width:slider').get_adjustment().set_value( 3.4883720930233e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:width:slider').get_adjustment().set_value( 9.3023255813953e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:width:slider').get_adjustment().set_value( 1.7441860465116e+00)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:width:slider').get_adjustment().set_value( 2.3255813953488e+00)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:width:slider').get_adjustment().set_value( 2.9069767441860e+00)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:width:slider').get_adjustment().set_value( 3.1395348837209e+00)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:width:slider').get_adjustment().set_value( 3.2558139534884e+00)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:width:slider').get_adjustment().set_value( 3.3720930232558e+00)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:width:slider').get_adjustment().set_value( 3.4883720930233e+00)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:width:slider').get_adjustment().set_value( 3.7209302325581e+00)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:width:slider').get_adjustment().set_value( 3.8372093023256e+00)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 1.5873015873016e-02)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 4.7619047619048e-02)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 1.4285714285714e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 2.2222222222222e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.3333333333333e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 4.1269841269841e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 4.9206349206349e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 5.7142857142857e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 6.0317460317460e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 6.1904761904762e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 6.5079365079365e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 7.1428571428571e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 7.4603174603175e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 7.6190476190476e-01)
findWidget('Dialog-New Display Method for Mesh mesh<2>:gtk-ok').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Add_Method
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(219, 93)
findWidget('Questioner:gtk-yes').clicked()
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint mesh page subproblems sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
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
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
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
checkpoint layer editor updated
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint OOF.Microstructure.Delete
assert tests.objectInventory(microstructures=0, nodes=0, elements=0, meshes=0)
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(356, 93)
findWidget('Questioner:gtk-delete').clicked()
checkpoint OOF.ActivityViewer.File.Close
checkpoint OOF.Graphics_1.File.Close
