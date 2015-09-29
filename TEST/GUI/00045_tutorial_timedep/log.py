checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.20 $
# $Author: langer $
# $Date: 2011/03/09 22:19:08 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

findMenu(findWidget('OOF2:MenuBar'), 'Help:Tutorials').activate()
findMenu(findWidget('OOF2:MenuBar'), 'Help:Tutorials:Solving_Time_Dependent_Systems').activate()
checkpoint toplevel widget mapped Solving Time Dependent Systems
findWidget('Solving Time Dependent Systems').resize(500, 300)
# Tutorial page 1
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.5925925925926e+00)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 3.1851851851852e+00)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.4333333333333e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 2.8666666666667e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 3.9814814814815e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 5.0962962962963e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 5.7333333333333e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 6.5296296296296e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 7.4851851851852e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 8.6000000000000e+01)
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 2
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
checkpoint page installed Microstructure
findWidget('OOF2').resize(577, 350)
findWidget('OOF2:Microstructure Page:Pane').set_position(159)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('Dialog-Create Microstructure').resize(315, 163)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(164)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint microstructure page sensitized
checkpoint active area status updated
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint pixel page sensitized
checkpoint mesh bdy page updated
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
checkpoint skeleton selection page groups sensitized
checkpoint Solver page sensitized
checkpoint skeleton selection page updated
checkpoint OOF.Microstructure.New
# checkpoint interface page updated
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 3
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2').resize(685, 350)
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
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1,), open_all=False)
widget_0=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_0.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_0.window))
widget_1=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_1.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_1.window))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 0, 0))
checkpoint Materials page updated
checkpoint property selected
widget_2=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_2.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_2.window))
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic').resize(469, 236)
setComboBox(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:Chooser'), 'Bulk and Shear')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:Bulk and Shear:bulk').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:Bulk and Shear:bulk').set_text('0.5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().unselect_all()
checkpoint Materials page updated
checkpoint property deselected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').collapse_row((1, 0))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 2), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 2, 0))
checkpoint Materials page updated
checkpoint property selected
widget_3=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_3.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_3.window))
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity').resize(190, 94)
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-9.')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-9.-')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-9.-0')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-9.-0.')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-9.-0.3')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-9-0.3')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('--0.3')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-0.3')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.ForceDensity.ConstantForceDensity
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 0, 0))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
widget_4=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_4.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_4.window))
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().unselect_all()
checkpoint Materials page updated
checkpoint property deselected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').collapse_row((1, 0))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').collapse_row((1, 2))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 3), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 3, 0))
checkpoint Materials page updated
checkpoint property selected
widget_5=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_5.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_5.window))
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;MassDensity;ConstantMassDensity
findWidget('Dialog-Parametrize Mechanical;MassDensity;ConstantMassDensity').resize(190, 71)
findWidget('Dialog-Parametrize Mechanical;MassDensity;ConstantMassDensity:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.MassDensity.ConstantMassDensity
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.7313432835821e+00)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 3.4626865671642e+00)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 6.9253731343284e+00)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.0388059701493e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.5582089552239e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 2.2507462686567e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 3.1164179104478e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 3.8089552238806e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 4.5014925373134e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 5.0208955223881e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 5.5402985074627e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 6.0597014925373e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 6.2328358208955e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 6.5791044776119e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 6.9253731343284e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 7.2716417910448e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 7.6179104477612e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 7.9641791044776e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 8.1373134328358e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 8.3104477611940e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 8.4835820895522e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().unselect_all()
checkpoint Materials page updated
checkpoint property deselected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').collapse_row((1, 3))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.9717345240052e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.9434690480103e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.9152035720155e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1886938096021e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 4), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 4, 0))
checkpoint Materials page updated
checkpoint property selected
widget_6=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_6.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_6.window))
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Viscosity;Isotropic
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic').resize(470, 236)
setComboBox(findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gijkl:Chooser'), 'Bulk and Shear')
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gijkl:Bulk and Shear:bulk').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gijkl:Bulk and Shear:bulk').set_text('0.0')
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gijkl:Bulk and Shear:bulk').set_text('0.07')
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gtk-ok').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Viscosity.Isotropic
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 1.6000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(304, 106)
setComboBox(findWidget('Dialog-Assign material material to pixels:pixels'), '<every>')
findWidget('Dialog-Assign material material to pixels:gtk-ok').clicked()
checkpoint OOF.Material.Assign
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 4
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2').resize(705, 424)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane').set_position(324)
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
checkpoint skeleton page sensitized
findWidget('Dialog-New skeleton').resize(394, 198)
findWidget('Dialog-New skeleton:x_elements').set_text('')
findWidget('Dialog-New skeleton:x_elements').set_text('8')
findWidget('Dialog-New skeleton:y_elements').set_text('')
findWidget('Dialog-New skeleton:y_elements').set_text('8')
findWidget('Dialog-New skeleton:gtk-ok').clicked()
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint skeleton page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
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
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.New
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
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
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
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
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 5
findWidget('Solving Time Dependent Systems').resize(500, 300)
findWidget('OOF2:Navigation:Next').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2').resize(773, 424)
findWidget('OOF2:Fields & Equations Page:HPane').set_position(343)
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement in-plane').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
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
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Activate
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 6
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Boundary Conditions
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(441, 291)
setComboBox(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary'), 'bottom')
findWidget('Dialog-New Boundary Condition:gtk-apply').clicked()
findWidget('OOF2 Messages 1').resize(860, 200)
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
setComboBox(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component'), 'y')
setComboBox(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component'), 'y')
findWidget('Dialog-New Boundary Condition:gtk-ok').clicked()
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 7
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Scheduled Output
findWidget('OOF2:Scheduled Output Page:HPane0').set_position(357)
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2').set_position(158)
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL').set_position(14)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 2.1460674157303e+00)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 4.2921348314607e+00)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 6.4382022471910e+00)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 8.5842696629213e+00)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.0730337078652e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.2876404494382e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.5022471910112e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.7168539325843e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.9314606741573e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 2.1460674157303e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 2.3606741573034e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 2.5752808988764e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 2.7898876404494e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 3.0044943820225e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 3.2191011235955e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 3.4337078651685e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 3.6483146067416e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 3.8629213483146e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 4.2921348314607e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 4.5067415730337e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 4.9359550561798e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 5.1505617977528e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 5.3651685393258e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 5.7943820224719e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 6.0089887640449e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 6.4382022471910e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 6.8674157303371e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 7.0820224719101e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 7.2966292134831e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 7.5112359550562e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 7.7258426966292e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 7.9404494382022e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 8.1550561797753e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 8.5842696629213e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 9.0134831460674e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 9.4426966292135e+01)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.0086516853933e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.0515730337079e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.0944943820225e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.1374157303371e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.1803370786517e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.2447191011236e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.2876404494382e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.3305617977528e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.3520224719101e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.3734831460674e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.4164044943820e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.4378651685393e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.4593258426966e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.5022471910112e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.5237078651685e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.5451685393258e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.5666292134831e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.5880898876404e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.6095505617978e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.6310112359551e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.6524719101124e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.6739325842697e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.6953932584270e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.7168539325843e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.7383146067416e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.7597752808989e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.7812359550562e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.8026966292135e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.8241573033708e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.8456179775281e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.8670786516854e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.8885393258427e+02)
findWidget('Solving Time Dependent Systems:TutorialScroll').get_vadjustment().set_value( 1.9100000000000e+02)
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 8
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:Output:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(314, 102)
findWidget('Dialog-Define a new Output:gtk-ok').clicked()
checkpoint OOF.Mesh.Scheduled_Output.New
findWidget('OOF2:Scheduled Output Page:HPane0').set_position(364)
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2').set_position(156)
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL').set_position(25)
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('Solving Time Dependent Systems').resize(500, 300)
# Tutorial page 9
findWidget('Solving Time Dependent Systems').resize(501, 312)
findWidget('Solving Time Dependent Systems').resize(502, 333)
findWidget('Solving Time Dependent Systems').resize(503, 366)
findWidget('Solving Time Dependent Systems').resize(501, 447)
findWidget('Solving Time Dependent Systems').resize(498, 504)
findWidget('Solving Time Dependent Systems').resize(487, 604)
findWidget('Solving Time Dependent Systems').resize(486, 619)
findWidget('Solving Time Dependent Systems').resize(486, 621)
findWidget('Solving Time Dependent Systems').resize(486, 622)
findWidget('Solving Time Dependent Systems').resize(486, 623)
findWidget('Solving Time Dependent Systems').resize(487, 624)
findWidget('Solving Time Dependent Systems').resize(487, 626)
findWidget('Solving Time Dependent Systems').resize(487, 628)
findWidget('Solving Time Dependent Systems').resize(488, 628)
findWidget('Solving Time Dependent Systems').resize(489, 628)
findWidget('Solving Time Dependent Systems').resize(489, 627)
findWidget('Solving Time Dependent Systems').resize(490, 626)
findWidget('Solving Time Dependent Systems').resize(491, 626)
findWidget('Solving Time Dependent Systems').resize(492, 626)
findWidget('Solving Time Dependent Systems').resize(492, 625)
findWidget('Solving Time Dependent Systems').resize(493, 625)
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Schedule:New').clicked()
checkpoint toplevel widget mapped Dialog-Set an Output Schedule
findWidget('Dialog-Set an Output Schedule').resize(306, 156)
findWidget('Dialog-Set an Output Schedule:schedule:Periodic:interval').set_text('0.01')
findWidget('Dialog-Set an Output Schedule:schedule:Periodic:interval').set_text('0.1')
findWidget('Dialog-Set an Output Schedule:gtk-ok').clicked()
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:enable').get_selection().unselect_all()
checkpoint OOF.Mesh.Scheduled_Output.Schedule.Set
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:Output:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(314, 102)
findWidget('Dialog-Define a new Output:gtk-cancel').clicked()
# Tutorial page 10
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:Output:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(314, 102)
setComboBox(findWidget('Dialog-Define a new Output:output:Chooser'), 'Boundary Analysis')
findWidget('Dialog-Define a new Output').resize(393, 187)
findWidget('Dialog-Define a new Output:gtk-ok').clicked()
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:enable').get_selection().unselect_all()
checkpoint OOF.Mesh.Scheduled_Output.New
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Schedule:list').get_selection().select_path((0,))
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Schedule:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy an Output Schedule
findWidget('Dialog-Copy an Output Schedule').resize(411, 160)
setComboBox(findWidget('Dialog-Copy an Output Schedule:target'), 'Average Displacement on top')
findWidget('Dialog-Copy an Output Schedule:gtk-ok').clicked()
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:enable').get_selection().unselect_all()
checkpoint OOF.Mesh.Scheduled_Output.Schedule.Copy
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Schedule:list').get_selection().select_path((1,))
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Destination:Set').clicked()
checkpoint toplevel widget mapped Dialog-Set an Output Destination
findWidget('Dialog-Set an Output Destination').resize(293, 79)
setComboBox(findWidget('Dialog-Set an Output Destination:destination:Chooser'), 'Output Stream')
findWidget('Dialog-Set an Output Destination').resize(300, 129)
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('t')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('td')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('td.')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('td.o')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('td.ou')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('td.out')
findWidget('Dialog-Set an Output Destination').resize(320, 129)
findWidget('Dialog-Set an Output Destination:gtk-ok').clicked()
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:enable').get_selection().unselect_all()
checkpoint OOF.Mesh.Scheduled_Output.Destination.Set
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 11
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Analysis')
checkpoint page installed Analysis
findWidget('OOF2:Analysis Page:bottom').set_position(402)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.4090909090909e+00)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.8181818181818e+00)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 7.2272727272727e+00)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 1.2045454545455e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 1.4454545454545e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 1.6863636363636e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 1.9272727272727e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.1681818181818e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.4090909090909e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.6500000000000e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 2.8909090909091e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 3.1318181818182e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 3.3727272727273e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 3.6136363636364e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 3.8545454545455e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.0954545454545e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.3363636363636e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 4.8181818181818e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 5.0590909090909e+01)
findWidget('OOF2:Analysis Page:top:Output').get_vadjustment().set_value( 5.3000000000000e+01)
setComboBox(findWidget('OOF2:Analysis Page:top:Output:Scalar:Parameters:component'), 'y')
checkpoint named analysis chooser set
setComboBox(findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:Chooser'), 'Average')
checkpoint named analysis chooser set
checkpoint named analysis chooser set
findWidget('OOF2:Analysis Page:bottom').set_position(375)

widget_0 = findWidget('OOF2:Analysis Page:Name:Operations')
widget_0.event(event(gtk.gdk.BUTTON_PRESS,x= 1.5000000000000e+02,y= 1.1000000000000e+01,button=1,state=0,window=widget_0.window))
checkpoint toplevel widget mapped NamedOpsMenu
findWidget('NamedOpsMenu').deactivate()
findMenu(findWidget('NamedOpsMenu'), 'Create').activate()
checkpoint toplevel widget mapped Dialog-Name an analysis operation
findWidget('Dialog-Name an analysis operation').resize(252, 69)
findWidget('Dialog-Name an analysis operation:name:Auto').clicked()
findWidget('Dialog-Name an analysis operation:name:Text').set_text('a')
findWidget('Dialog-Name an analysis operation:name:Text').set_text('av')
findWidget('Dialog-Name an analysis operation:name:Text').set_text('avg')
findWidget('Dialog-Name an analysis operation:name:Text').set_text('avg-')
findWidget('Dialog-Name an analysis operation:name:Text').set_text('avg-y')
findWidget('Dialog-Name an analysis operation:gtk-ok').clicked()
checkpoint named analysis chooser set
checkpoint OOF.Named_Analysis.Create

findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 12
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Scheduled Output
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:Output:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(393, 187)
setComboBox(findWidget('Dialog-Define a new Output:output:Chooser'), 'Named Analysis')
findWidget('Dialog-Define a new Output:gtk-ok').clicked()
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:enable').get_selection().unselect_all()
checkpoint OOF.Mesh.Scheduled_Output.New
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Schedule:list').get_selection().select_path((1,))
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Schedule:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy an Output Schedule
findWidget('Dialog-Copy an Output Schedule').resize(411, 160)
setComboBox(findWidget('Dialog-Copy an Output Schedule:target'), 'avg-y')
findWidget('Dialog-Copy an Output Schedule:gtk-ok').clicked()
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:enable').get_selection().unselect_all()
checkpoint OOF.Mesh.Scheduled_Output.Schedule.Copy
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Destination:list').get_selection().select_path((2,))
findWidget('OOF2:Scheduled Output Page:HPane0:HPane2:Destination:Set').clicked()
checkpoint toplevel widget mapped Dialog-Set an Output Destination
findWidget('Dialog-Set an Output Destination').resize(320, 129)
findWidget('Dialog-Set an Output Destination:gtk-ok').clicked()
findWidget('OOF2:Scheduled Output Page:HPane0:HPaneL:enable').get_selection().unselect_all()
checkpoint OOF.Mesh.Scheduled_Output.Destination.Set
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 13
findWidget('OOF2:Navigation:Next').clicked()
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2').resize(773, 484)
findWidget('OOF2:Solver Page:VPane').set_position(152)
findWidget('Solving Time Dependent Systems').resize(493, 625)
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 14
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path((0,))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:Subproblems:Set').clicked()
checkpoint toplevel widget mapped Dialog-Specify Solver

findWidget('Dialog-Specify Solver').resize(475, 187)
setComboBox(findWidget('Dialog-Specify Solver:solver_mode:Chooser'), 'Advanced')
findWidget('Dialog-Specify Solver').resize(498, 357)
setComboBox(findWidget('Dialog-Specify Solver:solver_mode:Advanced:time_stepper:Chooser'), 'Adaptive')
findWidget('Dialog-Specify Solver').resize(728, 496)
setComboBox(findWidget('Dialog-Specify Solver:solver_mode:Advanced:time_stepper:Adaptive:errorscaling:Chooser'), 'Absolute')
setComboBox(findWidget('Dialog-Specify Solver:solver_mode:Advanced:time_stepper:Adaptive:stepper:Two Step:singlestep:Chooser'), 'SS22')
findWidget('Dialog-Specify Solver').resize(733, 542)
findWidget('Dialog-Specify Solver:solver_mode:Advanced:time_stepper:Adaptive:stepper:Two Step:singlestep:SS22:theta2:entry').set_text('0.')
findWidget('Dialog-Specify Solver:solver_mode:Advanced:time_stepper:Adaptive:stepper:Two Step:singlestep:SS22:theta2:entry').set_text('0.5')
widget_0=findWidget('Dialog-Specify Solver:solver_mode:Advanced:time_stepper:Adaptive:stepper:Two Step:singlestep:SS22:theta2:entry')
widget_0.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_0.window))
widget_1=findWidget('Dialog-Specify Solver:solver_mode:Advanced:time_stepper:Adaptive:stepper:Two Step:singlestep:SS22:theta2:entry')
widget_1.event(event(gtk.gdk.FOCUS_CHANGE, in_=0, window=widget_1.window))
# findWidget('Dialog-Specify Solver').resize(370, 218)
# setComboBox(findWidget('Dialog-Specify Solver:time_stepping:Chooser'), 'Adaptive')
# findWidget('Dialog-Specify Solver').resize(600, 357)
# setComboBox(findWidget('Dialog-Specify Solver:time_stepping:Adaptive:stepper:Two Step:singlestep:Chooser'), 'SS22')
# findWidget('Dialog-Specify Solver').resize(605, 403)
findWidget('Dialog-Specify Solver:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 15
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Set').clicked()
checkpoint toplevel widget mapped Dialog-Initialize field Displacement
findWidget('Dialog-Initialize field Displacement').resize(243, 125)
setComboBox(findWidget('Dialog-Initialize field Displacement:initializer:Chooser'), 'XYTFunction')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1*')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1*x')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1*x*')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1*x*y')
findWidget('Dialog-Initialize field Displacement:gtk-ok').clicked()
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((0,))
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Set_Field_Initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((1,))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll').get_vadjustment().set_value( 6.0000000000000e+00)
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(1)
tree.row_activated((1,), column)
checkpoint toplevel widget mapped Dialog-Initialize field Displacement_t
findWidget('Dialog-Initialize field Displacement_t').resize(243, 125)
findWidget('Dialog-Initialize field Displacement_t:gtk-ok').clicked()
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Set_Field_Initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path((1,))
checkpoint Solver page sensitized
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 16
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0').set_position(285)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(692)
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(715)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2:Solver Page:VPane:FieldInit:Apply').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Apply_Field_Initializers
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.1696070952851e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.3392141905703e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.5088212858554e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.6784283811406e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 5.8000000000000e+01)
widget_7 = findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
widget_7.event(event(gtk.gdk.BUTTON_PRESS,x= 2.1900000000000e+02,y= 2.1000000000000e+01,button=1,state=0,window=widget_7.window))
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((11,))
checkpoint OOF.Graphics_1.Layer.Select
widget_8 = findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
widget_8.event(event(gtk.gdk.BUTTON_PRESS,x= 2.1900000000000e+02,y= 2.1000000000000e+01,button=1,state=0,window=widget_8.window))
widget_9 = findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
widget_9.event(event(gtk.gdk.BUTTON_PRESS,x= 2.1900000000000e+02,y= 2.1000000000000e+01,button=1,state=0,window=widget_9.window))
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((11,), column)
checkpoint layereditor layerset changed
checkpoint toplevel widget mapped OOF2 Graphics Layer Editor
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:Edit').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Skeleton skeleton
findWidget('Dialog-New Display Method for Skeleton skeleton').resize(358, 196)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 1.0000000000000e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 2.0000000000000e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.0000000000000e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 7.9365079365079e-02)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 1.4285714285714e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 2.0634920634921e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 2.6984126984127e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.1746031746032e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 3.8095238095238e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 4.1269841269841e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 4.6031746031746e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 4.9206349206349e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 5.0793650793651e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 5.2380952380952e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 5.0793650793651e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 4.9206349206349e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 4.7619047619048e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 4.9206349206349e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 5.0793650793651e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 5.2380952380952e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 5.3968253968254e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 5.5555555555556e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:method:Element Edges:color:Gray:Gray:slider').get_adjustment().set_value( 5.7142857142857e-01)
findWidget('Dialog-New Display Method for Skeleton skeleton:gtk-ok').clicked()
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Replace_Method
widget_10=findWidget('OOF2 Graphics Layer Editor')
handled_0=widget_10.event(event(gtk.gdk.DELETE,window=widget_10.window))
postpone if not handled_0: widget_10.destroy()
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 17
findWidget('OOF2:Solver Page:end').set_text('')
findWidget('OOF2:Solver Page:end').set_text('6')
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Solve
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 18
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'File:Animate').activate()
checkpoint toplevel widget mapped Dialog-Animate
findWidget('Dialog-Animate').resize(390, 278)
findWidget('Dialog-Animate:gtk-ok').clicked()
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.File.Animate
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 19
findWidget('Solving Time Dependent Systems:Next').clicked()
# Tutorial page 20
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.9000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList').get_selection().select_path((2,))
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 3), open_all=False)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll:PropertyList').get_selection().select_path((3,))
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Viscosity;Isotropic
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic').resize(236, 125)
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gijkl:Bulk and Shear:shear').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gijkl:Bulk and Shear:shear').set_text('0.0')
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gijkl:Bulk and Shear:shear').set_text('0.01')
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gtk-ok').clicked()
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint named analysis chooser set
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Property.Parametrize.Mechanical.Viscosity.Isotropic
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Solver')
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2:Solver Page:VPane:FieldInit:ApplyAt').clicked()
checkpoint toplevel widget mapped Dialog-Initialize Fields at Time
findWidget('Dialog-Initialize Fields at Time').resize(190, 71)
findWidget('Dialog-Initialize Fields at Time:gtk-ok').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Apply_Field_Initializers_at_Time
findWidget('OOF2:Solver Page:end').set_text('0')
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:end').set_text('60')
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:end').set_text('6/0')
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:end').set_text('60')
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:end').set_text('6.0')
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Solve
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'File:Animate').activate()
checkpoint toplevel widget mapped Dialog-Animate
findWidget('Dialog-Animate').resize(390, 278)
findWidget('Dialog-Animate:gtk-ok').clicked()
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Mesh Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.File.Animate
findWidget('Solving Time Dependent Systems:Next').clicked()
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(191, 98)
findWidget('Dialog-Python_Log:filename').set_text('t')
findWidget('Dialog-Python_Log:filename').set_text('td')
findWidget('Dialog-Python_Log:filename').set_text('td.')
findWidget('Dialog-Python_Log:filename').set_text('td.l')
findWidget('Dialog-Python_Log:filename').set_text('td.lo')
findWidget('Dialog-Python_Log:filename').set_text('td.log')
findWidget('Dialog-Python_Log').resize(211, 98)
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.floatFileDiff2("td.log")
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint OOF.Graphics_1.File.Close
