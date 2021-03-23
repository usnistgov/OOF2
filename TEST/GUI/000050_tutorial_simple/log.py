checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
import tests
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials', 'A_Simple_Example']).activate()
checkpoint toplevel widget mapped A Simple Example
findWidget('A Simple Example').resize(500, 300)
findWidget('OOF2').resize(782, 545)
findWidget('A Simple Example').resize(500, 300)
findWidget('A Simple Example:Next').clicked()
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
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
event(Gdk.EventType.BUTTON_PRESS,x= 9.6000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.New_Layer_Policy
findWidget('A Simple Example:Next').clicked()
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
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
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/c')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cy')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cya')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyal')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyall')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallo')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallow')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallow.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallow.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallow.pn')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallow.png')
findWidget('Dialog-Load Image and create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint pixel page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
findWidget('A Simple Example:Next').clicked()
findWidget('A Simple Example').resize(500, 302)
event(Gdk.EventType.BUTTON_PRESS,x= 9.4000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Image']).activate() # MenuItemLogger
checkpoint page installed Image
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
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
assert tests.checkGroupSizes()
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename pixelgroup #00ffff
findWidget('Dialog-Rename pixelgroup #00ffff').resize(192, 92)
findWidget('Dialog-Rename pixelgroup #00ffff:new_name').set_text('')
findWidget('Dialog-Rename pixelgroup #00ffff:new_name').set_text('c')
findWidget('Dialog-Rename pixelgroup #00ffff:new_name').set_text('cy')
findWidget('Dialog-Rename pixelgroup #00ffff:new_name').set_text('cya')
findWidget('Dialog-Rename pixelgroup #00ffff:new_name').set_text('cyan')
findWidget('Dialog-Rename pixelgroup #00ffff:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Rename
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename pixelgroup #ffff00
findWidget('Dialog-Rename pixelgroup #ffff00').resize(192, 92)
findWidget('Dialog-Rename pixelgroup #ffff00:new_name').set_text('')
findWidget('Dialog-Rename pixelgroup #ffff00:new_name').set_text('y')
findWidget('Dialog-Rename pixelgroup #ffff00:new_name').set_text('ye')
findWidget('Dialog-Rename pixelgroup #ffff00:new_name').set_text('yel')
findWidget('Dialog-Rename pixelgroup #ffff00:new_name').set_text('yell')
findWidget('Dialog-Rename pixelgroup #ffff00:new_name').set_text('yello')
findWidget('Dialog-Rename pixelgroup #ffff00:new_name').set_text('yellow')
findWidget('Dialog-Rename pixelgroup #ffff00:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Rename
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.checkNewGroupNames()
assert tests.treeViewColCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', 0, ['cyan (2160 pixels, meshable)', 'yellow (1440 pixels, meshable)'])
findWidget('A Simple Example:Next').clicked()
findWidget('A Simple Example').resize(500, 398)
event(Gdk.EventType.BUTTON_PRESS,x= 9.2000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.matlPageSensitizationCheck0()
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:name').delete_text(0, 11)
findWidget('Dialog-New material:name').insert_text('y', 11)
findWidget('Dialog-New material:name').insert_text('e', 1)
findWidget('Dialog-New material:name').insert_text('l', 2)
findWidget('Dialog-New material:name').insert_text('l', 3)
findWidget('Dialog-New material:name').insert_text('o', 4)
findWidget('Dialog-New material:name').insert_text('w', 5)
findWidget('Dialog-New material:name').insert_text('-', 6)
findWidget('Dialog-New material:name').insert_text('m', 7)
findWidget('Dialog-New material:name').insert_text('a', 8)
findWidget('Dialog-New material:name').insert_text('t', 9)
findWidget('Dialog-New material:name').insert_text('e', 10)
findWidget('Dialog-New material:name').insert_text('r', 11)
findWidget('Dialog-New material:name').insert_text('i', 12)
findWidget('Dialog-New material:name').insert_text('a', 13)
findWidget('Dialog-New material:name').insert_text('l', 14)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New
assert tests.chooserCheck('OOF2:Materials Page:Pane:Material:MaterialList', ['yellow-material'])
assert tests.matlPageSensitizationCheck1()
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:name').delete_text(0, 6)
findWidget('Dialog-New material:name').insert_text('c', 0)
findWidget('Dialog-New material:name').insert_text('y', 1)
findWidget('Dialog-New material:name').insert_text('a', 2)
findWidget('Dialog-New material:name').insert_text('n', 3)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New
assert tests.chooserCheck('OOF2:Materials Page:Pane:Material:MaterialList', [ 'cyan-material', 'yellow-material'])
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 1.3000000000000e+01,y= 2.5000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
event(Gdk.EventType.BUTTON_RELEASE,x= 2.8000000000000e+01,y= 4.3000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([1, 0, 0]))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
assert tests.matlPageSensitizationCheck2()
event(Gdk.EventType.BUTTON_RELEASE,x= 7.5000000000000e+01,y= 6.3000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Isotropic
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic').resize(192, 92)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').delete_text(0, 11)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('y', 11)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('e', 1)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('l', 2)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('l', 3)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('o', 4)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('w', 5)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('_', 6)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('e', 7)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('l', 8)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('a', 9)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('s', 10)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('t', 11)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('i', 12)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('c', 13)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('i', 14)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('t', 15)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('y', 16)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0, 0]), open_all=False)
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy
assert tests.matlPageSensitizationCheck3()
findWidget('A Simple Example:Next').clicked()
event(Gdk.EventType.BUTTON_RELEASE,x= 1.5000000000000e+02,y= 7.9000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity').resize(538, 330)
event(Gdk.EventType.BUTTON_PRESS,x= 1.5500000000000e+02,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['E and nu']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:E and nu:young').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:E and nu:young').set_text('1')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:E and nu:poisson').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:E and nu:poisson').set_text('0.3')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.yellow_elasticity
assert tests.selectedPropertyCheck('Mechanical:Elasticity:Isotropic:yellow_elasticity')
findWidget('A Simple Example:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.0900000000000e+02,y= 2.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Materials Page:Pane:Material:MaterialList').get_window())
checkpoint toplevel widget mapped chooserPopup-MaterialList
findMenu(findWidget('chooserPopup-MaterialList'), ['yellow-material']).activate() # MenuItemLogger
checkpoint Materials page updated
deactivatePopup('chooserPopup-MaterialList') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Add_property
assert tests.matlPageSensitizationCheck4()
assert tests.selectedMatlPropertyCheck('Mechanical:Elasticity:Isotropic:yellow_elasticity')
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Isotropic;yellow_elasticity
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;yellow_elasticity').resize(192, 92)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;yellow_elasticity:new_name').delete_text(0, 6)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;yellow_elasticity:new_name').insert_text('c', 0)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;yellow_elasticity:new_name').insert_text('y', 1)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;yellow_elasticity:new_name').insert_text('a', 2)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;yellow_elasticity:new_name').insert_text('n', 3)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;yellow_elasticity:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy
findWidget('A Simple Example:Next').clicked()
event(Gdk.EventType.BUTTON_RELEASE,x= 1.4700000000000e+02,y= 9.9000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
event(Gdk.EventType.BUTTON_RELEASE,x= 1.4700000000000e+02,y= 9.9000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
event(Gdk.EventType.BUTTON_RELEASE,x= 1.3400000000000e+02,y= 1.0000000000000e+02,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity').resize(217, 170)
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity:cijkl:E and nu:young').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity:cijkl:E and nu:young').set_text('0')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity:cijkl:E and nu:young').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity:cijkl:E and nu:young').set_text('0.5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.cyan_elasticity
assert tests.selectedPropertyCheck('Mechanical:Elasticity:Isotropic:cyan_elasticity')
findWidget('A Simple Example:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.0700000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Materials Page:Pane:Material:MaterialList').get_window())
checkpoint toplevel widget mapped chooserPopup-MaterialList
findMenu(findWidget('chooserPopup-MaterialList'), ['cyan-material']).activate() # MenuItemLogger
checkpoint Materials page updated
deactivatePopup('chooserPopup-MaterialList') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Add_property
assert tests.materialCheck('cyan-material', ['Mechanical:Elasticity:Isotropic:cyan_elasticity'])
assert tests.selectedMatlPropertyCheck('Mechanical:Elasticity:Isotropic:cyan_elasticity')
findWidget('OOF2:Materials Page:Pane:Material:RemoveProperty').clicked()
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Remove_property
assert tests.selectedMatlPropertyCheck(None)
assert tests.materialCheck('cyan-material', [])
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Add_property
assert tests.materialCheck('cyan-material', ['Mechanical:Elasticity:Isotropic:cyan_elasticity'])
assert tests.selectedMatlPropertyCheck('Mechanical:Elasticity:Isotropic:cyan_elasticity')
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 6.6000000000000e+01,y= 1.2000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Color
findWidget('Dialog-Copy property Color').resize(192, 92)
findWidget('Dialog-Copy property Color:new_name').delete_text(0, 15)
findWidget('Dialog-Copy property Color:new_name').insert_text('y', 11)
findWidget('Dialog-Copy property Color:new_name').insert_text('e', 1)
findWidget('Dialog-Copy property Color:new_name').insert_text('l', 2)
findWidget('Dialog-Copy property Color:new_name').insert_text('l', 3)
findWidget('Dialog-Copy property Color:new_name').insert_text('o', 4)
findWidget('Dialog-Copy property Color:new_name').insert_text('w', 5)
findWidget('Dialog-Copy property Color:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([0]), open_all=False)
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy
assert tests.selectedPropertyCheck('Color:yellow')
event(Gdk.EventType.BUTTON_RELEASE,x= 6.1000000000000e+01,y= 2.4000000000000e+01,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Color;yellow
findWidget('Dialog-Parametrize Color;yellow').resize(279, 206)
event(Gdk.EventType.BUTTON_PRESS,x= 4.5000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('Dialog-Parametrize Color;yellow:color:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['RGBAColor']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Parametrize Color;yellow').resize(280, 274)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:red:slider').get_adjustment().set_value( 2.7777777777778e-02)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:red:slider').get_adjustment().set_value( 1.2500000000000e-01)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:red:slider').get_adjustment().set_value( 2.7777777777778e-01)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:red:slider').get_adjustment().set_value( 6.2500000000000e-01)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:red:slider').get_adjustment().set_value( 9.5833333333333e-01)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:red:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:green:entry').set_text('0.')
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:green:entry').set_text('0.8')
widget_0=findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:green:entry')
if widget_0: wevent(widget_0, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
widget_1=findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:green:entry')
if widget_1: wevent(widget_1, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_1.get_window())
del widget_1
widget_2=findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:green:entry')
if widget_2: wevent(widget_2, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_2.get_window())
del widget_2
findWidget('Dialog-Parametrize Color;yellow:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Property.Parametrize.Color.yellow
event(Gdk.EventType.BUTTON_PRESS,x= 7.2000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Materials Page:Pane:Material:MaterialList').get_window())
checkpoint toplevel widget mapped chooserPopup-MaterialList
findMenu(findWidget('chooserPopup-MaterialList'), ['yellow-material']).activate() # MenuItemLogger
checkpoint Materials page updated
deactivatePopup('chooserPopup-MaterialList') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Add_property
assert tests.materialCheck('yellow-material',  ['Mechanical:Elasticity:Isotropic:yellow_elasticity', 'Color:yellow'])
assert tests.selectedMatlPropertyCheck('Color:yellow')
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([0]))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
event(Gdk.EventType.BUTTON_RELEASE,x= 3.4000000000000e+01,y= 4.0000000000000e+00,button=1,state=256,window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Color
findWidget('Dialog-Copy property Color').resize(192, 92)
findWidget('Dialog-Copy property Color:new_name').delete_text(0, 6)
findWidget('Dialog-Copy property Color:new_name').insert_text('b', 11)
findWidget('Dialog-Copy property Color:new_name').insert_text('l', 1)
findWidget('Dialog-Copy property Color:new_name').insert_text('l', 2)
findWidget('Dialog-Copy property Color:new_name').delete_text(2, 3)
findWidget('Dialog-Copy property Color:new_name').insert_text('u', 2)
findWidget('Dialog-Copy property Color:new_name').insert_text('e', 3)
findWidget('Dialog-Copy property Color:new_name').delete_text(3, 4)
findWidget('Dialog-Copy property Color:new_name').delete_text(2, 3)
findWidget('Dialog-Copy property Color:new_name').delete_text(1, 2)
findWidget('Dialog-Copy property Color:new_name').delete_text(0, 1)
findWidget('Dialog-Copy property Color:new_name').delete_text(0, 11)
findWidget('Dialog-Copy property Color:new_name').insert_text('c', 11)
findWidget('Dialog-Copy property Color:new_name').insert_text('y', 1)
findWidget('Dialog-Copy property Color:new_name').insert_text('a', 2)
findWidget('Dialog-Copy property Color:new_name').insert_text('n', 3)
findWidget('Dialog-Copy property Color:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Color;cyan
findWidget('Dialog-Parametrize Color;cyan').resize(279, 206)
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('Dialog-Parametrize Color;cyan:color:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['RGBAColor']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Parametrize Color;cyan').resize(280, 274)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:slider').get_adjustment().set_value( 5.5555555555556e-02)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:slider').get_adjustment().set_value( 2.2222222222222e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:slider').get_adjustment().set_value( 5.1388888888889e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:entry').set_text('0.')
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:entry').set_text('0.8')
widget_3=findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:entry')
if widget_3: wevent(widget_3, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_3.get_window())
del widget_3
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:slider').get_adjustment().set_value( 8.0555555555556e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:slider').get_adjustment().set_value( 9.4444444444444e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:entry').set_text('')
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:entry').set_text('/')
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:entry').set_text('')
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:entry').set_text('0')
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:entry').set_text('0.')
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:entry').set_text('0.8')
widget_4=findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:entry')
if widget_4: wevent(widget_4, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_4.get_window())
del widget_4
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:slider').get_adjustment().set_value( 9.8611111111111e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:slider').get_adjustment().set_value( 7.9166666666667e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:slider').get_adjustment().set_value( 6.3888888888889e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:slider').get_adjustment().set_value( 4.7222222222222e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:slider').get_adjustment().set_value( 2.6388888888889e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:slider').get_adjustment().set_value( 9.7222222222222e-02)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:red:slider').get_adjustment().set_value( 0.0000000000000e+00)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:blue:slider').get_adjustment().set_value( 8.3333333333333e-02)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:blue:slider').get_adjustment().set_value( 3.0555555555556e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:blue:slider').get_adjustment().set_value( 6.3888888888889e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:blue:slider').get_adjustment().set_value( 9.8611111111111e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:blue:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('Dialog-Parametrize Color;cyan:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Property.Parametrize.Color.cyan
event(Gdk.EventType.BUTTON_PRESS,x= 6.9000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Materials Page:Pane:Material:MaterialList').get_window())
checkpoint toplevel widget mapped chooserPopup-MaterialList
findMenu(findWidget('chooserPopup-MaterialList'), ['cyan-material']).activate() # MenuItemLogger
checkpoint Materials page updated
deactivatePopup('chooserPopup-MaterialList') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Add_property
assert tests.materialCheck('cyan-material',  ['Mechanical:Elasticity:Isotropic:cyan_elasticity', 'Color:cyan'])
assert tests.selectedMatlPropertyCheck('Color:cyan')
findWidget('A Simple Example:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 9.5000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Materials Page:Pane:Material:MaterialList').get_window())
checkpoint toplevel widget mapped chooserPopup-MaterialList
findMenu(findWidget('chooserPopup-MaterialList'), ['yellow-material']).activate() # MenuItemLogger
checkpoint Materials page updated
deactivatePopup('chooserPopup-MaterialList') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material yellow-material to pixels
findWidget('Dialog-Assign material yellow-material to pixels').resize(221, 122)
event(Gdk.EventType.BUTTON_PRESS,x= 7.3000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-Assign material yellow-material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['yellow']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material yellow-material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign
findWidget('A Simple Example:Next').clicked()
findWidget('A Simple Example').resize(500, 458)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
event(Gdk.EventType.BUTTON_PRESS,x= 1.3600000000000e+02,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:what:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findWidget('chooserPopup-Microstructure').deactivate() # MenuLogger
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
findWidget('A Simple Example:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 2.3000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', Gtk.TreePath(13))
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Hide
event(Gdk.EventType.BUTTON_PRESS,x= 2.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', Gtk.TreePath(13))
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Show
findWidget('A Simple Example:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 8.9000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Materials Page:Pane:Material:MaterialList').get_window())
checkpoint toplevel widget mapped chooserPopup-MaterialList
findMenu(findWidget('chooserPopup-MaterialList'), ['cyan-material']).activate() # MenuItemLogger
checkpoint Materials page updated
deactivatePopup('chooserPopup-MaterialList') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material cyan-material to pixels
findWidget('Dialog-Assign material cyan-material to pixels').resize(221, 122)
event(Gdk.EventType.BUTTON_PRESS,x= 5.7000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-Assign material cyan-material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['cyan']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material cyan-material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign
findWidget('A Simple Example:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
checkpoint page installed Skeleton
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
assert tests.skeletonPageSensitivityCheck0()
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
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint skeleton page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New
assert tests.skeletonPageSensitivityCheck1()
findWidget('A Simple Example:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 3.8000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Pane:Modification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Snap Nodes']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Page:Pane').set_position(437)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 3.0555555555556e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 3.6111111111111e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 5.4166666666667e-01)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 7.3611111111111e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 9.5833333333333e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Skeleton Page:Pane:Modification:OK').clicked()
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Modify
assert tests.skeletonPageSensitivityCheck2()
findWidget('A Simple Example:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 6.8000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
assert tests.meshPageSensitivityCheck0()
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(130)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(299, 244)
findWidget('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK').clicked()
checkpoint Graphics_1 Mesh Info cleared position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
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
assert tests.meshPageSensitivityCheck1()
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Navigation:Next').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint page installed Fields & Equations
assert tests.fieldPageSensitivityCheck0()
findWidget('OOF2:Fields & Equations Page:HPane').set_position(470)
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
assert tests.fieldPageSensitivityCheck1()
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
findWidget('A Simple Example:Next').clicked()
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
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Boundary Conditions
assert tests.bcPageSensitivityCheck0()
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 362)
event(Gdk.EventType.BUTTON_PRESS,x= 6.8000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
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
assert tests.bcPageSensitivityCheck1()
assert tests.treeViewColCheck('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList', 0, ['bc'])
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 362)
event(Gdk.EventType.BUTTON_PRESS,x= 3.2000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component').get_window())
checkpoint toplevel widget mapped chooserPopup-field_component
findMenu(findWidget('chooserPopup-field_component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field_component') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 3.8000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component').get_window())
checkpoint toplevel widget mapped chooserPopup-eqn_component
findMenu(findWidget('chooserPopup-eqn_component'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-eqn_component') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 8.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
checkpoint toplevel widget mapped chooserPopup-boundary
findMenu(findWidget('chooserPopup-boundary'), ['bottom']).activate() # MenuItemLogger
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
assert tests.treeViewColCheck('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList', 0, ['bc', 'bc<2>'])
assert tests.listViewSelectedRowNo('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList') == 1
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 362)
event(Gdk.EventType.BUTTON_PRESS,x= 4.5000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component').get_window())
checkpoint toplevel widget mapped chooserPopup-field_component
findMenu(findWidget('chooserPopup-field_component'), ['x']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-field_component') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 4.6000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component').get_window())
checkpoint toplevel widget mapped chooserPopup-eqn_component
findMenu(findWidget('chooserPopup-eqn_component'), ['x']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-eqn_component') # MenuItemLogger
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Constant Profile:value').set_text('')
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Constant Profile:value').set_text('1')
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Constant Profile:value').set_text('10')
event(Gdk.EventType.BUTTON_PRESS,x= 5.2000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary').get_window())
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
assert tests.treeViewColCheck('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList', 0, ['bc', 'bc<2>', 'bc<3>'])
assert tests.listViewSelectedRowNo('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList') == 2
findWidget('A Simple Example:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 7.6000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
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
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
findWidget('OOF2:Solver Page:end').set_text('0.0')
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Mesh.Solve
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.3092569869182e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.8092569869182e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.7092569869182e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.7092569869182e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.7000000000000e+01)
findWidget('OOF2 Graphics 1').resize(800, 518)
findWidget('OOF2 Graphics 1:Pane0').set_position(386)
findWidget('OOF2 Graphics 1').resize(800, 547)
findWidget('OOF2 Graphics 1:Pane0').set_position(415)
findWidget('OOF2 Graphics 1').resize(800, 577)
findWidget('OOF2 Graphics 1:Pane0').set_position(445)
findWidget('OOF2 Graphics 1').resize(800, 579)
findWidget('OOF2 Graphics 1:Pane0').set_position(447)
findWidget('OOF2 Graphics 1').resize(800, 580)
findWidget('OOF2 Graphics 1:Pane0').set_position(448)
findWidget('OOF2 Graphics 1').resize(800, 581)
findWidget('OOF2 Graphics 1:Pane0').set_position(449)
findWidget('OOF2 Graphics 1').resize(800, 583)
findWidget('OOF2 Graphics 1:Pane0').set_position(451)
findWidget('OOF2 Graphics 1').resize(800, 579)
findWidget('OOF2 Graphics 1:Pane0').set_position(383)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0').set_position(373)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0').set_position(364)
event(Gdk.EventType.BUTTON_PRESS,x= 4.0600000000000e+02,y= 3.0000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
checkpoint OOF.Graphics_1.Layer.Select
event(Gdk.EventType.BUTTON_PRESS,x= 4.0700000000000e+02,y= 3.0000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([10]), column)
checkpoint toplevel widget mapped Dialog-Edit Graphics Layer
findWidget('Dialog-Edit Graphics Layer').resize(467, 484)
event(Gdk.EventType.BUTTON_PRESS,x= 1.6000000000000e+02,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-Edit Graphics Layer:how:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Filled Contour']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Edit Graphics Layer').resize(483, 613)
findWidget('Dialog-Edit Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Edit
findWidget('A Simple Example:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 7.8000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Boundary Conditions']).activate() # MenuItemLogger
checkpoint page installed Boundary Conditions
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
tree=findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([2]), column)
checkpoint toplevel widget mapped Dialog-Edit Boundary Condition
findWidget('Dialog-Edit Boundary Condition').resize(353, 326)
event(Gdk.EventType.BUTTON_PRESS,x= 1.0100000000000e+02,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('Dialog-Edit Boundary Condition:condition:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Neumann']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Edit Boundary Condition').resize(353, 338)
findWidget('Dialog-Edit Boundary Condition:condition:Neumann:profile:p0:Constant Profile:value').set_text('0.01')
findWidget('Dialog-Edit Boundary Condition:condition:Neumann:profile:p0:Constant Profile:value').set_text('0.0')
findWidget('Dialog-Edit Boundary Condition:condition:Neumann:profile:p1:Constant Profile:value').set_text('0.01')
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
checkpoint OOF.Mesh.Boundary_Conditions.Edit
event(Gdk.EventType.BUTTON_PRESS,x= 8.2000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Solver']).activate() # MenuItemLogger
checkpoint Solver page sensitized
checkpoint page installed Solver
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
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
event(Gdk.EventType.BUTTON_PRESS,x= 1.2600000000000e+02,y= 5.8000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
event(Gdk.EventType.BUTTON_PRESS,x= 1.2500000000000e+02,y= 5.8000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
event(Gdk.EventType.BUTTON_PRESS,x= 1.2500000000000e+02,y= 5.8000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(2)
tree.row_activated(Gtk.TreePath([14]), column)
checkpoint toplevel widget mapped Dialog-Edit Graphics Layer
findWidget('Dialog-Edit Graphics Layer').resize(483, 613)
event(Gdk.EventType.BUTTON_PRESS,x= 1.2000000000000e+02,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('Dialog-Edit Graphics Layer:how:Filled Contour:where:where_0').get_window())
checkpoint toplevel widget mapped chooserPopup-where_0
findMenu(findWidget('chooserPopup-where_0'), ['actual']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-where_0') # MenuItemLogger
findWidget('Dialog-Edit Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Edit
findWidget('A Simple Example:Next').clicked()
findWidget('A Simple Example:Close').clicked()
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Python_Log']).activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(192, 122)
findWidget('Dialog-Python_Log:filename').set_text('s')
findWidget('Dialog-Python_Log:filename').set_text('se')
findWidget('Dialog-Python_Log:filename').set_text('ses')
findWidget('Dialog-Python_Log:filename').set_text('sess')
findWidget('Dialog-Python_Log:filename').set_text('sessi')
findWidget('Dialog-Python_Log:filename').set_text('sessin')
findWidget('Dialog-Python_Log:filename').set_text('sessino')
findWidget('Dialog-Python_Log:filename').set_text('sessino.')
findWidget('Dialog-Python_Log:filename').set_text('sessino')
findWidget('Dialog-Python_Log:filename').set_text('sessin')
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
