# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Check that the correct widgets are appearing in the mesh data viewer window

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)
# Create and solve a simple elasticity problem
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('OOF2').resize(782, 545)
findWidget('Dialog-Create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
checkpoint OOF.Microstructure.New
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
checkpoint skeleton page sensitized
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
checkpoint skeleton page info updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.New
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([1, 0, 0]))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic').resize(538, 330)
wevent(findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['E and nu']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:E and nu:young').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:E and nu:young').set_text('1')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:E and nu:young').set_text('10')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(235, 122)
wevent(findWidget('Dialog-Assign material material to pixels:pixels'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Assign material material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['<every>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Material.Assign
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
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
findWidget('OOF2:Fields & Equations Page:HPane').set_position(470)
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
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement in-plane').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Field.In_Plane
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Force_Balance active').clicked()
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
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Boundary Conditions
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 362)
wevent(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
checkpoint toplevel widget mapped chooserPopup-boundary
findMenu(findWidget('chooserPopup-boundary'), ['bottomleft']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-boundary') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_APPLY').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
wevent(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component').get_window())
checkpoint toplevel widget mapped chooserPopup-field_component
findMenu(findWidget('chooserPopup-field_component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field_component') # MenuItemLogger
wevent(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component').get_window())
checkpoint toplevel widget mapped chooserPopup-eqn_component
findMenu(findWidget('chooserPopup-eqn_component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-eqn_component') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_APPLY').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Constant Profile:value').set_text('0.')
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Constant Profile:value').set_text('0.1')
wevent(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
checkpoint toplevel widget mapped chooserPopup-boundary
findMenu(findWidget('chooserPopup-boundary'), ['topright']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-boundary') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_APPLY').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
wevent(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component').get_window())
checkpoint toplevel widget mapped chooserPopup-field_component
findMenu(findWidget('chooserPopup-field_component'), ['x']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field_component') # MenuItemLogger
wevent(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component').get_window())
checkpoint toplevel widget mapped chooserPopup-eqn_component
findMenu(findWidget('chooserPopup-eqn_component'), ['x']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-eqn_component') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2:Solver Page:VPane').set_position(170)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
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
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:end').set_text('0.0')
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Solve
findWidget('OOF2').resize(782, 545)
# Open a graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
wevent(findWidget('Dialog-New_Layer_Policy:policy'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Settings.Graphics_Defaults.New_Layer_Policy
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1').resize(800, 492)
# Open the mesh info toolbox
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Mesh Info']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(227)
# Open a data viewer
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:NewDataViewer').clicked()
checkpoint Mesh_Data_1 time updated
checkpoint Mesh_Data_1 mesh updated
checkpoint toplevel widget mapped Mesh Data 1
findWidget('Mesh Data 1').resize(278, 372)
checkpoint Mesh_Data_1 data updated
findWidget('Mesh Data 1').resize(278, 372)
assert tests.dataWidgets()

# Select Strain
wevent(findWidget('Mesh Data 1:ViewSource:output:output_0'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Mesh Data 1:ViewSource:output:output_0').get_window())
checkpoint toplevel widget mapped chooserPopup-output_0
findMenu(findWidget('chooserPopup-output_0'), ['Strain']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-output_0') # MenuItemLogger
findWidget('Mesh Data 1').resize(296, 383)
checkpoint Mesh_Data_1 data updated
assert tests.dataWidgets()

# Click on the canvas
findGfxWindow('Graphics_1').simulateMouse('down', 0.9684573, 0.97038567, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.9684573, 0.97038567, 1, False, False)
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint Mesh_Data_1 position updated
checkpoint Mesh_Data_1 data updated
findWidget('Mesh Data 1').resize(543, 503)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryElement
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 9.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.1000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
assert tests.dataWidgets('xy', 'xz', 'yz', 'zz', 'yy', 'xx')

# DELETE ABOVE SCROLL EVENTS
# Change from Value to Invariant
wevent(findWidget('Mesh Data 1:ViewSource:output:output_1'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Mesh Data 1:ViewSource:output:output_1').get_window())
checkpoint toplevel widget mapped chooserPopup-output_1
findMenu(findWidget('chooserPopup-output_1'), ['Invariant']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-output_1') # MenuItemLogger
findWidget('Mesh Data 1').resize(543, 544)
checkpoint Mesh_Data_1 data updated
assert tests.dataWidgets('generic')

# Change to Elastic Strain
wevent(findWidget('Mesh Data 1:ViewSource:output:Parameters:type:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Mesh Data 1:ViewSource:output:Parameters:type:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Elastic Strain']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
checkpoint Mesh_Data_1 data updated
checkpoint Mesh_Data_1 data updated
assert tests.dataWidgets('generic')

# Click on a different element
findGfxWindow('Graphics_1').simulateMouse('down', 0.66213499, 0.93210744, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.66213499, 0.93210744, 1, False, False)
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint Mesh_Data_1 position updated
checkpoint Mesh_Data_1 data updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryElement
assert tests.dataWidgets('generic')

# Delete the Mesh layer
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=3, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
checkpoint toplevel widget mapped PopUp-0
findMenu(findWidget('PopUp-0'), ['Delete']).activate() # MenuItemLogger
deactivatePopup('PopUp-0') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint Graphics_1 Mesh Info cleared position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Mesh_Data_1 time updated
checkpoint Mesh_Data_1 mesh updated
checkpoint Mesh_Data_1 data updated
checkpoint Mesh_Data_1 data updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Delete
assert tests.dataWidgets()

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
checkpoint OOF.Graphics_1.File.Close
