checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
import tests
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials', 'Solving_Time_Dependent_Systems']).activate()
checkpoint toplevel widget mapped Solving Time Dependent Systems
findWidget('Solving Time Dependent Systems').resize(500, 314)
findWidget('OOF2').resize(782, 545)
findWidget('Solving Time Dependent Systems').resize(500, 326)
findWidget('Solving Time Dependent Systems:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 7.8000000000000e+01,y= 2.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
checkpoint page installed Microstructure
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('Dialog-Create Microstructure:widget_GTK_RESPONSE_OK').clicked()
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
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.New
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
findWidget('Solving Time Dependent Systems:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 5.2000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 1.4000000000000e+01,y= 2.3000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 2.7000000000000e+01,y= 4.3000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([1, 0, 0]))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 8.9000000000000e+01,y= 6.0000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
event(Gdk.EventType.BUTTON_RELEASE,x= 8.9000000000000e+01,y= 6.1000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic').resize(538, 330)
event(Gdk.EventType.BUTTON_PRESS,x= 5.0000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Bulk and Shear']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:Bulk and Shear:bulk').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:cijkl:Bulk and Shear:bulk').set_text('0.5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().unselect_all()
checkpoint Materials page updated
checkpoint property deselected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').collapse_row(Gtk.TreePath([1, 0]))
event(Gdk.EventType.BUTTON_RELEASE,x= 2.8000000000000e+01,y= 4.3000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 3]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 2.5000000000000e+01,y= 1.0200000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([1, 3, 0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 8.7000000000000e+01,y= 1.1800000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 3, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity').resize(192, 128)
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-9.')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-9')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-0')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-0.')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:gy').set_text('-0.3')
findWidget('Dialog-Parametrize Mechanical;ForceDensity;ConstantForceDensity:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.ForceDensity.ConstantForceDensity
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().unselect_all()
checkpoint Materials page updated
checkpoint property deselected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').collapse_row(Gtk.TreePath([1, 3]))
event(Gdk.EventType.BUTTON_RELEASE,x= 3.2000000000000e+01,y= 9.7000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 4]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 2.6000000000000e+01,y= 1.1600000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([1, 4, 0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 8.2000000000000e+01,y= 1.3600000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 4, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;MassDensity;ConstantMassDensity
findWidget('Dialog-Parametrize Mechanical;MassDensity;ConstantMassDensity').resize(192, 92)
findWidget('Dialog-Parametrize Mechanical;MassDensity;ConstantMassDensity:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.MassDensity.ConstantMassDensity
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 5]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 2.5000000000000e+01,y= 1.5100000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([1, 5, 0]))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 6.6000000000000e+01,y= 1.6900000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
event(Gdk.EventType.BUTTON_RELEASE,x= 6.8000000000000e+01,y= 1.6900000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
event(Gdk.EventType.BUTTON_RELEASE,x= 9.8000000000000e+01,y= 1.6900000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 5, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Viscosity;Isotropic
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic').resize(539, 330)
event(Gdk.EventType.BUTTON_PRESS,x= 1.0900000000000e+02,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Bulk and Shear']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gijkl:Bulk and Shear:bulk').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gijkl:Bulk and Shear:bulk').set_text('0.0')
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:gijkl:Bulk and Shear:bulk').set_text('0.07')
findWidget('Dialog-Parametrize Mechanical;Viscosity;Isotropic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Mechanical.Viscosity.Isotropic
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(235, 122)
event(Gdk.EventType.BUTTON_PRESS,x= 4.9000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('Dialog-Assign material material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['<every>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Material.Assign
findWidget('Solving Time Dependent Systems:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 7.3000000000000e+01,y= 2.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:x_elements').set_text('')
findWidget('Dialog-New skeleton:x_elements').set_text('8')
findWidget('Dialog-New skeleton:y_elements').set_text('')
findWidget('Dialog-New skeleton:y_elements').set_text('8')
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
event(Gdk.EventType.BUTTON_PRESS,x= 9.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
findWidget('Solving Time Dependent Systems:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 5.5000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
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
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Boundary Conditions
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 362)
event(Gdk.EventType.BUTTON_PRESS,x= 6.0000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
checkpoint toplevel widget mapped chooserPopup-boundary
findMenu(findWidget('chooserPopup-boundary'), ['bottom']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-boundary') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_APPLY').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
event(Gdk.EventType.BUTTON_PRESS,x= 5.9000000000000e+01,y= 0.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component').get_window())
checkpoint toplevel widget mapped chooserPopup-field_component
findMenu(findWidget('chooserPopup-field_component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field_component') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 5.0000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component').get_window())
checkpoint toplevel widget mapped chooserPopup-eqn_component
findWidget('chooserPopup-eqn_component').deactivate() # MenuLogger
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_APPLY').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_CANCEL').clicked()
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Scheduled Output
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('OOF2:Scheduled Output Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(206, 133)
findWidget('Dialog-Define a new Output:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.New
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('Solving Time Dependent Systems').resize(500, 350)
tree=findWidget('OOF2:Scheduled Output Page:list')
column = tree.get_column(2)
tree.row_activated(Gtk.TreePath([0]), column)
checkpoint toplevel widget mapped Dialog-Set an Output Schedule
findWidget('Dialog-Set an Output Schedule').resize(266, 211)
findWidget('Dialog-Set an Output Schedule:schedule:Periodic:interval').set_text('0.')
findWidget('Dialog-Set an Output Schedule:schedule:Periodic:interval').set_text('0.1')
findWidget('Dialog-Set an Output Schedule:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Schedule.Set
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('Solving Time Dependent Systems').resize(500, 362)
findWidget('OOF2:Scheduled Output Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(206, 133)
event(Gdk.EventType.BUTTON_PRESS,x= 9.2000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('Dialog-Define a new Output:output:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Boundary Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Define a new Output').resize(318, 236)
findWidget('Solving Time Dependent Systems').resize(500, 362)
findWidget('Dialog-Define a new Output:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.New
findWidget('OOF2:Scheduled Output Page:list').get_selection().select_path(Gtk.TreePath([0]))
findWidget('OOF2:Scheduled Output Page:CopySchedule').clicked()
checkpoint toplevel widget mapped Dialog-Copy an Output Schedule
findWidget('Dialog-Copy an Output Schedule').resize(223, 182)
event(Gdk.EventType.BUTTON_PRESS,x= 4.9000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-Copy an Output Schedule:target').get_window())
checkpoint toplevel widget mapped chooserPopup-target
findMenu(findWidget('chooserPopup-target'), ['Average Displacement on top']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-target') # MenuItemLogger
findWidget('Dialog-Copy an Output Schedule').resize(294, 182)
findWidget('Dialog-Copy an Output Schedule:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Schedule.Copy
findWidget('OOF2:Scheduled Output Page:list').get_selection().select_path(Gtk.TreePath([1]))
findWidget('OOF2:Scheduled Output Page:EditDestination').clicked()
checkpoint toplevel widget mapped Dialog-Set an Output Destination
findWidget('Dialog-Set an Output Destination').resize(235, 97)
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-Set an Output Destination:destination:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Output Stream']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Set an Output Destination').resize(259, 164)
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('d')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('di')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('dis')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('disp')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('disp.')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('disp.o')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('disp.ou')
findWidget('Dialog-Set an Output Destination:destination:Output Stream:filename').set_text('disp.out')
findWidget('Dialog-Set an Output Destination:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Destination.Set
findWidget('Solving Time Dependent Systems:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 7.5000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Analysis']).activate() # MenuItemLogger
checkpoint page installed Analysis
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Analysis Page:bottom').set_position(320)
findWidget('OOF2').resize(782, 601)
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Analysis Page:top:Output:Scalar:Parameters:component').get_window())
checkpoint toplevel widget mapped chooserPopup-component
findMenu(findWidget('chooserPopup-component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-component') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.5800000000000e+02,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Analysis Page:bottom:Operation:OperationRCF:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Average']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Analysis Page:bottom').set_position(296)
findWidget('OOF2:Analysis Page:Name:New').clicked()
checkpoint toplevel widget mapped Dialog-Name an analysis operation
findWidget('Dialog-Name an analysis operation').resize(192, 92)
findWidget('Dialog-Name an analysis operation:widget_GTK_RESPONSE_OK').clicked()
checkpoint named analysis chooser set
checkpoint OOF.Named_Analysis.Create
findWidget('Solving Time Dependent Systems:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 6.8000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Scheduled Output']).activate() # MenuItemLogger
checkpoint page installed Scheduled Output
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Scheduled Output Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Define a new Output
findWidget('Dialog-Define a new Output').resize(318, 236)
event(Gdk.EventType.BUTTON_PRESS,x= 1.4800000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-Define a new Output:output:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Named Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Define a new Output:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.New
findWidget('OOF2:Scheduled Output Page:list').get_selection().select_path(Gtk.TreePath([1]))
findWidget('OOF2:Scheduled Output Page:CopySchedule').clicked()
checkpoint toplevel widget mapped Dialog-Copy an Output Schedule
findWidget('Dialog-Copy an Output Schedule').resize(223, 182)
event(Gdk.EventType.BUTTON_PRESS,x= 4.8000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('Dialog-Copy an Output Schedule:target').get_window())
checkpoint toplevel widget mapped chooserPopup-target
findMenu(findWidget('chooserPopup-target'), ['analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-target') # MenuItemLogger
findWidget('Dialog-Copy an Output Schedule:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Schedule.Copy
findWidget('OOF2:Scheduled Output Page:list').get_selection().select_path(Gtk.TreePath([2]))
findWidget('OOF2:Scheduled Output Page:EditDestination').clicked()
checkpoint toplevel widget mapped Dialog-Set an Output Destination
findWidget('Dialog-Set an Output Destination').resize(259, 164)
findWidget('Dialog-Set an Output Destination:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Mesh.Scheduled_Output.Destination.Set
findWidget('Solving Time Dependent Systems:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 5.7000000000000e+01,y= 6.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Solver Page:VPane').set_position(198)
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('Solving Time Dependent Systems').resize(500, 578)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:Subproblems:Set').clicked()
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(414, 253)
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('Dialog-Specify Solver:solver_mode:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Advanced']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Specify Solver').resize(475, 490)
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 6.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-Specify Solver:solver_mode:Advanced:time_stepper:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Adaptive']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Specify Solver').resize(540, 723)
findWidget('Solving Time Dependent Systems').resize(500, 578)
event(Gdk.EventType.BUTTON_PRESS,x= 4.7000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-Specify Solver:solver_mode:Advanced:time_stepper:Adaptive:stepper:Two Step:singlestep:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['SS22']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Specify Solver').resize(664, 796)
findWidget('Solving Time Dependent Systems').resize(500, 578)
findWidget('Dialog-Specify Solver:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Subproblem.Set_Solver
findWidget('Solving Time Dependent Systems:Next').clicked()
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([0]), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(664, 796)
findWidget('Dialog-Specify Solver:widget_GTK_RESPONSE_CANCEL').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 6.8000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 7.3000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
tree=findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([0]), column)
checkpoint toplevel widget mapped Dialog-Specify Solver
findWidget('Dialog-Specify Solver').resize(664, 796)
findWidget('Dialog-Specify Solver:widget_GTK_RESPONSE_CANCEL').clicked()
findWidget('Solving Time Dependent Systems').resize(500, 578)
event(Gdk.EventType.BUTTON_PRESS,x= 7.4000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 8.4000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_hadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_hadjustment().set_value( 1.1000000000000e+01)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_hadjustment().set_value( 1.0000000000000e+01)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll').get_hadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([0]), column)
checkpoint toplevel widget mapped Dialog-Initialize field Displacement
findWidget('Dialog-Initialize field Displacement').resize(215, 170)
findWidget('Dialog-Initialize field Displacement:widget_GTK_RESPONSE_CANCEL').clicked()
tree=findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([0]), column)
checkpoint toplevel widget mapped Dialog-Initialize field Displacement
findWidget('Dialog-Initialize field Displacement').resize(215, 170)
event(Gdk.EventType.BUTTON_PRESS,x= 2.9000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-Initialize field Displacement:initializer:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['XYTFunction']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1&')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1&z')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1&')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1*')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1*x')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1*x*')
findWidget('Dialog-Initialize field Displacement:initializer:XYTFunction:fy').set_text('0.1*x*y')
findWidget('Dialog-Initialize field Displacement:widget_GTK_RESPONSE_OK').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.Set_Field_Initializer
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
findWidget('Solving Time Dependent Systems:Next').clicked()
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
event(Gdk.EventType.BUTTON_PRESS,x= 5.6000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
findWidget('Dialog-New').resize(467, 532)
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
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
checkpoint OOF.Graphics_1.Layer.New
findWidget('OOF2:Solver Page:VPane:FieldInit:Apply').clicked()
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().unselect_all()
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
findWidget('OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers').get_selection().select_path(Gtk.TreePath([0]))
 checkpoint OOF.Mesh.Apply_Field_Initializers
checkpoint Solver page sensitized
#checkpoint Solver page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 3.7800000000000e+02,y= 2.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
event(Gdk.EventType.BUTTON_PRESS,x= 3.7900000000000e+02,y= 2.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
event(Gdk.EventType.BUTTON_PRESS,x= 3.7900000000000e+02,y= 2.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
event(Gdk.EventType.BUTTON_PRESS,x= 3.6500000000000e+02,y= 2.8000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
event(Gdk.EventType.BUTTON_PRESS,x= 3.6600000000000e+02,y= 2.8000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([10]), column)
checkpoint toplevel widget mapped Dialog-Edit Graphics Layer
findWidget('Dialog-Edit Graphics Layer').resize(467, 484)
event(Gdk.EventType.BUTTON_PRESS,x= 7.7000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-Edit Graphics Layer:how:Element Edges:where:where_0').get_window())
checkpoint toplevel widget mapped chooserPopup-where_0
findMenu(findWidget('chooserPopup-where_0'), ['actual']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-where_0') # MenuItemLogger
findWidget('Dialog-Edit Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Edit
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(467, 484)
event(Gdk.EventType.BUTTON_PRESS,x= 4.8000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 1.5151515151515e-02)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 6.0606060606061e-02)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 1.4393939393939e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 1.8181818181818e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 2.5000000000000e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 2.9545454545455e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 3.2575757575758e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 3.3333333333333e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 3.4090909090909e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 3.5606060606061e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 3.7878787878788e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 4.3181818181818e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 4.9242424242424e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 5.6060606060606e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 6.0606060606061e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 6.3636363636364e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 6.5909090909091e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 6.7424242424242e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 6.8181818181818e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 6.8939393939394e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 7.0454545454545e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 7.2727272727273e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 7.4242424242424e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 7.6515151515152e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 7.5757575757576e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 7.5000000000000e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 7.4242424242424e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 7.2727272727273e-01)
findWidget('Dialog-New:how:Element Edges:color:TranslucentGray:gray:slider').get_adjustment().set_value( 7.1969696969697e-01)
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+01)
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
checkpoint OOF.Graphics_1.Layer.New
event(Gdk.EventType.BUTTON_PRESS,x= 1.7000000000000e+02,y= 8.0000000000000e+00,button=3,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
checkpoint toplevel widget mapped PopUp-0
findMenu(findWidget('PopUp-0'), ['Lower', 'To_Bottom']).activate() # MenuItemLogger
deactivatePopup('PopUp-0') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Lower.To_Bottom
findWidget('OOF2:Solver Page:end').set_text('6')
checkpoint Solver page sensitized
findWidget('Solving Time Dependent Systems').resize(500, 578)
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('Solving Time Dependent Systems').resize(500, 578)
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('Solving Time Dependent Systems:Next').clicked()
findWidget('Solving Time Dependent Systems').resize(500, 1082)
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
checkpoint OOF.Graphics_1.File.Close
