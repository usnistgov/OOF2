import tests
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 545)
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials', 'Nonrectangular_Domain']).activate()
checkpoint toplevel widget mapped Nonrectangular Domain
findWidget('Nonrectangular Domain').resize(500, 300)
findWidget('Nonrectangular Domain:Next').clicked()
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
event(Gdk.EventType.BUTTON_PRESS,x= 7.2000000000000e+01,y= 2.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.New_Layer_Policy
event(Gdk.EventType.BUTTON_PRESS,x= 9.3000000000000e+01,y= 2.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:NewFromFile').clicked()
checkpoint toplevel widget mapped Dialog-Load Image and create Microstructure
findWidget('Dialog-Load Image and create Microstructure').resize(237, 200)
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('e')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('ex')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('exa')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('exam')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examp')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('exampl')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('example')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/e')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_s')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_sh')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_shi')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_shia')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_shi')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_sh')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_sha')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_shap')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_shape')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_shape.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_shape.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_shape.pn')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/el_shape.png')
findWidget('Dialog-Load Image and create Microstructure:widget_GTK_RESPONSE_OK').clicked()
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
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Microstructure.Create_From_ImageFile
findWidget('Nonrectangular Domain:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 9.1000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Image']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Image
findWidget('OOF2:Image Page:Pane').set_position(546)
findWidget('OOF2:Image Page:Group').clicked()
checkpoint toplevel widget mapped Dialog-AutoGroup
findWidget('Dialog-AutoGroup').resize(207, 92)
findWidget('Dialog-AutoGroup:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.Image.AutoGroup
event(Gdk.EventType.BUTTON_PRESS,x= 8.2000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('Nonrectangular Domain:Next').clicked()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename pixelgroup #00ff00
findWidget('Dialog-Rename pixelgroup #00ff00').resize(192, 92)
findWidget('Dialog-Rename pixelgroup #00ff00:new_name').set_text('')
findWidget('Dialog-Rename pixelgroup #00ff00:new_name').set_text('g')
findWidget('Dialog-Rename pixelgroup #00ff00:new_name').set_text('gr')
findWidget('Dialog-Rename pixelgroup #00ff00:new_name').set_text('gre')
findWidget('Dialog-Rename pixelgroup #00ff00:new_name').set_text('gree')
findWidget('Dialog-Rename pixelgroup #00ff00:new_name').set_text('green')
findWidget('Dialog-Rename pixelgroup #00ff00').resize(192, 92)
findWidget('Dialog-Rename pixelgroup #00ff00:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Rename
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('Nonrectangular Domain:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 6.4000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:name').delete_text(0, 11)
findWidget('Dialog-New material:name').insert_text('g', 11)
findWidget('Dialog-New material:name').insert_text('r', 1)
findWidget('Dialog-New material:name').insert_text('e', 2)
findWidget('Dialog-New material:name').insert_text('e', 3)
findWidget('Dialog-New material:name').insert_text('n', 4)
findWidget('Dialog-New material:name').insert_text('_', 5)
findWidget('Dialog-New material:name').insert_text('m', 6)
findWidget('Dialog-New material:name').delete_text(6, 7)
findWidget('Dialog-New material:name').delete_text(5, 6)
findWidget('Dialog-New material:name').insert_text('-', 5)
findWidget('Dialog-New material:name').insert_text('m', 6)
findWidget('Dialog-New material:name').insert_text('a', 7)
findWidget('Dialog-New material:name').insert_text('t', 8)
findWidget('Dialog-New material:name').insert_text('e', 9)
findWidget('Dialog-New material:name').insert_text('r', 10)
findWidget('Dialog-New material:name').insert_text('i', 11)
findWidget('Dialog-New material:name').insert_text('a', 12)
findWidget('Dialog-New material:name').insert_text('l', 13)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.New
findWidget('Nonrectangular Domain:Next').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 1.7000000000000e+01,y= 2.3000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 1.7000000000000e+01,y= 3.2000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 3.2000000000000e+01,y= 4.5000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([1, 0, 0]))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 9.1000000000000e+01,y= 6.3000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Isotropic
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic').resize(192, 92)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').delete_text(0, 11)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('g', 11)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('r', 1)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('e', 2)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('e', 3)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('n', 4)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('_', 5)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('e', 6)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('l', 7)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('e', 8)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('a', 9)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('s', 10)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').delete_text(10, 11)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').delete_text(9, 10)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').delete_text(8, 9)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('a', 8)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('s', 9)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('t', 10)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('i', 11)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('c', 12)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('i', 13)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('t', 14)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('y', 15)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0, 0]), open_all=False)
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy
findWidget('Nonrectangular Domain:Next').clicked()
event(Gdk.EventType.BUTTON_RELEASE,x= 1.0500000000000e+02,y= 8.2000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;green_elasticity
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;green_elasticity').resize(538, 330)
event(Gdk.EventType.BUTTON_PRESS,x= 1.9100000000000e+02,y= 1.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;green_elasticity:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['E and nu']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;green_elasticity:cijkl:E and nu:young').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;green_elasticity:cijkl:E and nu:young').set_text('1')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;green_elasticity:cijkl:E and nu:young').set_text('1.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;green_elasticity:cijkl:E and nu:young').set_text('1.0')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;green_elasticity:cijkl:E and nu:poisson').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;green_elasticity:cijkl:E and nu:poisson').set_text('0.3')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;green_elasticity:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.green_elasticity
findWidget('Nonrectangular Domain:Next').clicked()
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Add_property
findWidget('Nonrectangular Domain:Next').clicked()
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material green-material to pixels
findWidget('Dialog-Assign material green-material to pixels').resize(231, 122)
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-Assign material green-material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['green']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material green-material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign
findWidget('Nonrectangular Domain:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
findWidget('Dialog-New skeleton:x_elements').set_text('')
findWidget('Dialog-New skeleton:x_elements').set_text('2')
findWidget('Dialog-New skeleton:x_elements').set_text('20')
findWidget('Dialog-New skeleton:y_elements').set_text('')
findWidget('Dialog-New skeleton:y_elements').set_text('2')
findWidget('Dialog-New skeleton:y_elements').set_text('20')
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
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
checkpoint skeleton selection page grouplist Element
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New
findWidget('Nonrectangular Domain:Next').clicked()
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('Nonrectangular Domain:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 2.4000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Boundaries']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton Boundaries
assert tests.skeletonBdySensitizationCheck0()
findWidget('OOF2:Skeleton Boundaries Page:Pane').set_position(379)
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
assert tests.skeletonBdySensitizationCheck1()
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 2.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(265)
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint selection info updated Element
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
event(Gdk.EventType.BUTTON_PRESS,x= 1.0200000000000e+02,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.4000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 3.09, 9.76, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.09, 9.76, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.125, 9.795, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.125, 9.795, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.16, 9.83, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.265, 9.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.37, 9.935, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.545, 10.075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.615, 10.145, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.65, 10.18, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.72, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.79, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 4, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 4.245, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 4.385, 10.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 4.525, 10.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 4.665, 10.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 4.945, 10.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 5.155, 10.285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 5.295, 10.285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 5.4, 10.32, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 5.54, 10.355, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 5.75, 10.39, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 5.925, 10.425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 6.1, 10.425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 6.275, 10.425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 6.485, 10.425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 6.555, 10.425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 6.695, 10.46, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 6.905, 10.46, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.08, 10.46, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.255, 10.425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.36, 10.425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.465, 10.39, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.605, 10.39, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.78, 10.355, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.955, 10.355, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.06, 10.32, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.165, 10.285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.27, 10.285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.41, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.725, 10.145, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.9, 10.11, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.075, 10.11, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.18, 10.075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.25, 10.075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.355, 10.075, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.495, 10.11, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.635, 10.11, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.74, 10.11, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.915, 10.145, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.09, 10.145, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.16, 10.145, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.195, 10.18, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.23, 10.18, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.265, 10.18, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.265, 10.18, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.3, 10.18, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.3, 10.18, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.37, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.405, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.405, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.44, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.44, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.475, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 10.475, 10.215, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Rectangle
assert tests.skeletonSelectionTBSizeCheck('OOF2 Graphics 1', 'Segment', 13)
assert tests.skeletonBdySizeCheck('el_shape.png:skeleton', 'top', 20)
event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Single_Segment']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 3.125, 10.04, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.125, 10.005, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 3.125, 10.005, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
assert tests.skeletonSelectionTBSizeCheck('OOF2 Graphics 1', 'Segment', 14)
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Modify').clicked()
checkpoint toplevel widget mapped Dialog-Boundary modifier
findWidget('Dialog-Boundary modifier').resize(244, 128)
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-Boundary modifier:modifier:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Remove segments']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Boundary modifier:widget_GTK_RESPONSE_OK').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Modify
assert tests.chooserListStateCheck('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList', ['top'])
assert tests.skeletonBdySizeCheck('el_shape.png:skeleton', 'top', 6)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'List_All_Layers']).activate()
checkpoint OOF.Graphics_1.Settings.List_All_Layers
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.9000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 7.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 7.1000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 7.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 8.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.1500000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.4600000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.4700000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.4800000000000e+02)
event(Gdk.EventType.BUTTON_PRESS,x= 3.8500000000000e+02,y= 3.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([8]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.4841981187680e+02)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.4997461067577e+02)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.5054579599361e+02)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.5099802488666e+02)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.5134518707718e+02)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.5160117228739e+02)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.5177987023953e+02)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.5189517065585e+02)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.5196096325859e+02)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.5199113776997e+02)
event(Gdk.EventType.BUTTON_PRESS,x= 3.8500000000000e+02,y= 3.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([8]), column)
checkpoint toplevel widget mapped Dialog-Edit Graphics Layer
findWidget('Dialog-Edit Graphics Layer').resize(383, 520)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.5200000000000e+02)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 1.4193548387097e+01)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 1.3225806451613e+01)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 1.2580645161290e+01)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 1.1612903225806e+01)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 1.0322580645161e+01)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 8.7096774193548e+00)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 8.0645161290323e+00)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 7.7419354838710e+00)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 7.0967741935484e+00)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 6.7741935483871e+00)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 6.4516129032258e+00)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 5.8064516129032e+00)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 5.4838709677419e+00)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 5.1612903225806e+00)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 4.8387096774194e+00)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 5.1612903225806e+00)
findWidget('Dialog-Edit Graphics Layer:how:Selected Boundary:arrowsize:slider').get_adjustment().set_value( 5.4838709677419e+00)
findWidget('Dialog-Edit Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.7600000000000e+02)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Edit
findWidget('OOF2 Messages 1').resize(771, 177)
findWidget('Nonrectangular Domain:Next').clicked()
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList').get_selection().select_path(Gtk.TreePath([2]))
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
event(Gdk.EventType.BUTTON_PRESS,x= 1.3000000000000e+02,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 9.703125, 2.83, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.703125, 2.83, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.808125, 2.83, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.983125, 2.865, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.158125, 3.005, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.298125, 3.285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.368125, 3.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.508125, 3.985, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.613125, 4.475, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.613125, 5.07, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.508125, 5.77, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.403125, 6.26, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.298125, 6.645, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.263125, 6.96, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.193125, 7.24, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.123125, 7.485, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.123125, 7.835, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.123125, 8.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.123125, 8.535, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.088125, 8.92, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.018125, 9.235, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.983125, 9.515, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.018125, 9.76, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.018125, 9.97, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.018125, 10.11, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.053125, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.088125, 10.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.088125, 10.285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.088125, 10.32, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.123125, 10.355, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.158125, 10.39, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.158125, 10.425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.158125, 10.425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.158125, 10.425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.158125, 10.355, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.158125, 10.32, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.193125, 10.285, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.193125, 10.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.193125, 10.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.193125, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.193125, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.193125, 10.215, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 10.193125, 10.215, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Rectangle
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:Modify').clicked()
checkpoint toplevel widget mapped Dialog-Boundary modifier
findWidget('Dialog-Boundary modifier').resize(244, 128)
findWidget('Dialog-Boundary modifier:widget_GTK_RESPONSE_OK').clicked()
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Modify
findWidget('Nonrectangular Domain:Next').clicked()
findWidget('Nonrectangular Domain').resize(500, 326)
event(Gdk.EventType.BUTTON_PRESS,x= 5.2000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
event(Gdk.EventType.BUTTON_PRESS,x= 4.7000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('Dialog-Create a new mesh:element_types:Map').get_window())
checkpoint toplevel widget mapped chooserPopup-Map
findMenu(findWidget('chooserPopup-Map'), ['2']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Map') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 5.4000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-Create a new mesh:element_types:Func').get_window())
checkpoint toplevel widget mapped chooserPopup-Func
findMenu(findWidget('chooserPopup-Func'), ['2']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Func') # MenuItemLogger
findWidget('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+01)
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
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Segment sensitized
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
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'List_All_Layers']).activate()
checkpoint OOF.Graphics_1.Settings.List_All_Layers
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.9000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.7000000000000e+01)
event(Gdk.EventType.BUTTON_PRESS,x= 2.4000000000000e+01,y= 2.7000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', Gtk.TreePath(11))
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([11]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.2000000000000e+01)
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Hide
findWidget('Nonrectangular Domain:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 7.3000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Fields & Equations']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
findWidget('OOF2:Fields & Equations Page:HPane').set_position(470)
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
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
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement in-plane').clicked()
checkpoint Solver page sensitized
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
checkpoint OOF.Mesh.Field.In_Plane
findWidget('OOF2:Fields & Equations Page:HPane:Equations:Force_Balance active').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
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
findWidget('Nonrectangular Domain:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 5.8000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Boundary Conditions
findWidget('Nonrectangular Domain:Next').clicked()
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 362)
event(Gdk.EventType.BUTTON_PRESS,x= 3.6000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
checkpoint toplevel widget mapped chooserPopup-boundary
findMenu(findWidget('chooserPopup-boundary'), ['left']).activate() # MenuItemLogger
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
checkpoint OOF.Mesh.Boundary_Conditions.New
findWidget('Nonrectangular Domain:Next').clicked()
findWidget('Nonrectangular Domain:Back').clicked()
findWidget('Nonrectangular Domain:Back').clicked()
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 362)
event(Gdk.EventType.BUTTON_PRESS,x= 5.2000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component').get_window())
checkpoint toplevel widget mapped chooserPopup-field_component
findMenu(findWidget('chooserPopup-field_component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field_component') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 5.8000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component').get_window())
checkpoint toplevel widget mapped chooserPopup-eqn_component
findMenu(findWidget('chooserPopup-eqn_component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-eqn_component') # MenuItemLogger
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
checkpoint OOF.Mesh.Boundary_Conditions.New
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component').get_window())
checkpoint toplevel widget mapped chooserPopup-field_component
findMenu(findWidget('chooserPopup-field_component'), ['x']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field_component') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 2.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component').get_window())
checkpoint toplevel widget mapped chooserPopup-eqn_component
findMenu(findWidget('chooserPopup-eqn_component'), ['x']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-eqn_component') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
checkpoint toplevel widget mapped chooserPopup-boundary
findMenu(findWidget('chooserPopup-boundary'), ['top']).activate() # MenuItemLogger
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
checkpoint OOF.Mesh.Boundary_Conditions.New
event(Gdk.EventType.BUTTON_PRESS,x= 3.9000000000000e+01,y= 6.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component').get_window())
checkpoint toplevel widget mapped chooserPopup-field_component
findMenu(findWidget('chooserPopup-field_component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field_component') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 3.6000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component').get_window())
checkpoint toplevel widget mapped chooserPopup-eqn_component
findMenu(findWidget('chooserPopup-eqn_component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-eqn_component') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 3.8000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
checkpoint toplevel widget mapped chooserPopup-boundary
findWidget('chooserPopup-boundary').deactivate() # MenuLogger
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
checkpoint OOF.Mesh.Boundary_Conditions.New
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Constant Profile:value').set_text('')
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Constant Profile:value').set_text('-')
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Constant Profile:value').set_text('-2')
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
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
checkpoint OOF.Mesh.Boundary_Conditions.New
findWidget('Nonrectangular Domain:Jump').clicked()
findWidget('Nonrectangular Domain:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 8.6000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
findWidget('OOF2:Solver Page:VPane').set_position(170)
findWidget('OOF2:Solver Page:VPane:Subproblems:SubproblemScroll:SubproblemList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:VPane:Subproblems:Set').clicked()
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
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:end').set_text('0.0')
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
findWidget('Dialog-Python_Log:filename').set_text('sessin')
findWidget('Dialog-Python_Log:filename').set_text('sessi')
findWidget('Dialog-Python_Log:filename').set_text('sessio')
findWidget('Dialog-Python_Log:filename').set_text('session')
findWidget('Dialog-Python_Log:filename').set_text('session.')
findWidget('Dialog-Python_Log:filename').set_text('session.l')
findWidget('Dialog-Python_Log:filename').set_text('session.lo')
findWidget('Dialog-Python_Log:filename').set_text('session.log')
findWidget('Dialog-Python_Log:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('session.log')
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
