# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# This script checks for errors that occurred when solving adjacent
# subproblems and with creating new subproblems when a graphics window
# was open.  There are almost no explicit tests in the script.  If it
# finishes without hanging or crashing, it passes.

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
checkpoint OOF.Microstructure.Create_From_ImageFile
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)

# Autogroup the image
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Image']).activate() # MenuItemLogger
checkpoint page installed Image
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Image Page:Pane').set_position(546)
findWidget('OOF2').resize(782, 545)
findWidget('OOF2:Image Page:Group').clicked()
checkpoint toplevel widget mapped Dialog-AutoGroup
findWidget('Dialog-AutoGroup').resize(207, 92)
findWidget('Dialog-AutoGroup:widget_GTK_RESPONSE_OK').clicked()
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.Image.AutoGroup

# Create a new material
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New

# Add an isotropic elasticity property
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Color')
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Isotropic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Assign the material to all pixels
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(221, 122)
wevent(findWidget('Dialog-Assign material material to pixels:pixels'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Assign material material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['<every>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Material.Assign

# Set the new layer policy to Single
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
wevent(findWidget('Dialog-New_Layer_Policy:policy'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Settings.Graphics_Defaults.New_Layer_Policy

# Open a graphics window
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint OOF.Graphics_1.Layer.Select
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([13]))
findWidget('OOF2 Graphics 1').resize(800, 492)

# Create a Skeleton
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page sensitized
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New

# Create a Mesh
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(130)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(299, 244)
findWidget('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK').clicked()
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info cleared position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
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
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.New

# Create a pixel group subproblem, group='#00ffff'
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new subproblem
findWidget('Dialog-Create a new subproblem').resize(206, 133)
wevent(findWidget('Dialog-Create a new subproblem:subproblem:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Create a new subproblem:subproblem:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['PixelGroup']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Create a new subproblem').resize(236, 164)
findWidget('Dialog-Create a new subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.New

# Define and activate displacement on the subproblem.
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Fields & Equations Page:HPane').set_position(470)
wevent(findWidget('OOF2:Fields & Equations Page:SubProblem'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Fields & Equations Page:SubProblem').get_window())
checkpoint toplevel widget mapped chooserPopup-SubProblem
findMenu(findWidget('chooserPopup-SubProblem'), ['subproblem']).activate() # MenuItemLogger
checkpoint Field page sensitized
deactivatePopup('chooserPopup-SubProblem') # MenuItemLogger
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Subproblem.Field.Define
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Field.Activate

# Activate the force balance and plane stress equations on the subproblem
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Force_Balance active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Activate
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Plane_Stress active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Equation.Activate

# Create boundary condition: left, x, continuum profile, all 0s
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
checkpoint page installed Boundary Conditions
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 362)
wevent(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Continuum Profile']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Boundary Condition').resize(407, 434)
wevent(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
checkpoint toplevel widget mapped chooserPopup-boundary
findMenu(findWidget('chooserPopup-boundary'), ['left']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-boundary') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_APPLY').clicked()
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New

# Create boundary condition: right, x, continuum profile, all 0s
wevent(findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
checkpoint toplevel widget mapped chooserPopup-boundary
findMenu(findWidget('chooserPopup-boundary'), ['right']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-boundary') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New

# Disable the default subproblem
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Solver Page:VPane').set_position(170)
findCellRenderer(findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList'), col=1, rend=0).emit('toggled', Gtk.TreePath(0))
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Disable_Solution
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized

# Set the basic static solver for the "subproblem" subproblem
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(2)
tree.row_activated(Gtk.TreePath([1]), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(414, 253)
findWidget('Dialog-Specify Solver:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver

# Set end time to  0
findWidget('OOF2:Solver Page:end').set_text('0')
checkpoint Solver page sensitized

# Solve 1 subproblem with trivial bcs
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Solve
findWidget('OOF2:Solver Page:end').set_text('0.0')

# Edit bc<2> (right) changing value to 10
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
checkpoint page installed Boundary Conditions
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
tree=findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([1]), column)
checkpoint toplevel widget mapped Dialog-Edit Boundary Condition
findWidget('Dialog-Edit Boundary Condition').resize(407, 398)
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('1')
findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:profile:Continuum Profile:function').set_text('10')
findWidget('Dialog-Edit Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Edit

# Create a second subproblem using the same pixel group
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:FE Mesh Page:Pane:leftpane:Subproblems:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new subproblem
findWidget('Dialog-Create a new subproblem').resize(236, 164)
findWidget('Dialog-Create a new subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.New

# Copy field state from the first subproblem to the second
findWidget('OOF2:Navigation:Next').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane:CopyField').clicked()
checkpoint toplevel widget mapped Dialog-Select a target Subproblem
findWidget('Dialog-Select a target Subproblem').resize(197, 182)
wevent(findWidget('Dialog-Select a target Subproblem:target:SubProblem'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Select a target Subproblem:target:SubProblem').get_window())
checkpoint toplevel widget mapped chooserPopup-SubProblem
findMenu(findWidget('chooserPopup-SubProblem'), ['subproblem<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-SubProblem') # MenuItemLogger
findWidget('Dialog-Select a target Subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Subproblem.Copy_Field_State

# Copy equation state from the first subproblem to the second
findWidget('OOF2:Fields & Equations Page:HPane:CopyEquation').clicked()
checkpoint toplevel widget mapped Dialog-Select a target subproblem
findWidget('Dialog-Select a target subproblem').resize(197, 182)
wevent(findWidget('Dialog-Select a target subproblem:target:SubProblem'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Select a target subproblem:target:SubProblem').get_window())
checkpoint toplevel widget mapped chooserPopup-SubProblem
findMenu(findWidget('chooserPopup-SubProblem'), ['subproblem<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-SubProblem') # MenuItemLogger
findWidget('Dialog-Select a target subproblem:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Copy_Equation_State

# Switch to the second subproblem
wevent(findWidget('OOF2:Fields & Equations Page:SubProblem'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Fields & Equations Page:SubProblem').get_window())
checkpoint toplevel widget mapped chooserPopup-SubProblem
findMenu(findWidget('chooserPopup-SubProblem'), ['subproblem<2>']).activate() # MenuItemLogger
checkpoint Field page sensitized
deactivatePopup('chooserPopup-SubProblem') # MenuItemLogger

# Go to the solver page
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger

# Disable solution of the first subproblem
findCellRenderer(findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList'), col=1, rend=0).emit('toggled', Gtk.TreePath(1))
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Disable_Solution

# Specify a solver for the second subproblem (basic static)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 9.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 1.2000000000000e+01)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 1.6000000000000e+01)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_vadjustment().set_value( 2.0000000000000e+01)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([2]))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([2]), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(414, 253)
findWidget('Dialog-Specify Solver:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver

# Solve second subproblem with nontrivial bcs
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Solve

# Enable solution of first subproblem and disable the second
findCellRenderer(findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList'), col=1, rend=0).emit('toggled', Gtk.TreePath(1))
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Enable_Solution
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint Solver page sensitized
findCellRenderer(findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList'), col=1, rend=0).emit('toggled', Gtk.TreePath(2))
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Disable_Solution
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([2]))
checkpoint Solver page sensitized

# Solve first subproblem again, with nontrivial bcs
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Solve
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
assert tests.filediff('session.log')

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
