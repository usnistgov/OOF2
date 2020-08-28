import tests
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 495)
findMenu(findWidget('OOF2:MenuBar'), 'Help:Tutorials').activate()
findMenu(findWidget('OOF2:MenuBar'), 'Help:Tutorials:A_Simple_Example').activate()
checkpoint toplevel widget mapped A Simple Example
findWidget('A Simple Example').resize(500, 300)
findWidget('OOF2').resize(782, 529)
findWidget('A Simple Example').resize(500, 300)
findWidget('OOF2').resize(782, 529)
findWidget('A Simple Example:Next').clicked()
findWidget('A Simple Example:Next').clicked()
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
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
checkpoint named analysis chooser set
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
checkpoint pixel page sensitized
checkpoint named boundary analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
findWidget('OOF2').resize(782, 545)
findWidget('A Simple Example:Back').clicked()
findWidget('A Simple Example:Back').clicked()
findWidget('A Simple Example:Next').clicked()
findWidget('A Simple Example:Next').clicked()
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([13]))
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
checkpoint OOF.Graphics_1.Layer.Select
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Navigation:Next').clicked()
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
checkpoint skeleton selection page groups sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.Image.AutoGroup
assert tests.checkGroupSizes()
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Image
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename pixelgroup #00ffff
findWidget('Dialog-Rename pixelgroup #00ffff').resize(192, 92)
findWidget('Dialog-Rename pixelgroup #00ffff:new_name').set_text('')
findWidget('Dialog-Rename pixelgroup #00ffff:new_name').set_text('c')
findWidget('Dialog-Rename pixelgroup #00ffff:new_name').set_text('cy')
findWidget('Dialog-Rename pixelgroup #00ffff:new_name').set_text('cya')
findWidget('Dialog-Rename pixelgroup #00ffff:new_name').set_text('cyab')
findWidget('Dialog-Rename pixelgroup #00ffff:new_name').set_text('cya')
findWidget('Dialog-Rename pixelgroup #00ffff:new_name').set_text('cyan')
findWidget('Dialog-Rename pixelgroup #00ffff:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Rename
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([0]))
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
assert tests.checkNewGroupNames()
assert tests.treeViewColCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', 0, ['cyan (2160 pixels, meshable)', 'yellow (1440 pixels, meshable)'])
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('A Simple Example:Next').clicked()
widget_0 = findWidget('OOF2:Navigation:PageMenu')
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=widget_0.get_window())
del widget_0
checkpoint toplevel widget mapped chooserPopup-PageMenu
widget_1=findMenu(findWidget('chooserPopup-PageMenu'), 'Image')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_1.get_window())
del widget_1
widget_2=findMenu(findWidget('chooserPopup-PageMenu'), 'Pixel Selection')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_2.get_window())
del widget_2
widget_3=findMenu(findWidget('chooserPopup-PageMenu'), 'Active Area')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_3.get_window())
del widget_3
widget_4=findMenu(findWidget('chooserPopup-PageMenu'), 'Materials')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_4.get_window())
del widget_4
findMenu(findWidget('chooserPopup-PageMenu'), 'Materials').activate()
checkpoint Materials page updated
checkpoint page installed Materials
assert tests.matlPageSensitizationCheck0()
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('A Simple Example:TutorialScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('A Simple Example:TutorialScroll').get_vadjustment().set_value( 2.8000000000000e+01)
findWidget('A Simple Example:TutorialScroll').get_vadjustment().set_value( 8.5000000000000e+01)
findWidget('A Simple Example:TutorialScroll').get_vadjustment().set_value( 1.0200000000000e+02)
findWidget('A Simple Example:TutorialScroll').get_vadjustment().set_value( 1.0116646530963e+02)
findWidget('A Simple Example:TutorialScroll').get_vadjustment().set_value( 1.0016646530963e+02)
findWidget('A Simple Example:TutorialScroll').get_vadjustment().set_value( 8.7166465309633e+01)
findWidget('A Simple Example:TutorialScroll').get_vadjustment().set_value( 5.6166465309633e+01)
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
findWidget('Dialog-New material:name').insert_text('o', 15)
findWidget('Dialog-New material:name').delete_text(15, 16)
findWidget('Dialog-New material:name').delete_text(14, 15)
findWidget('Dialog-New material:name').insert_text('a', 14)
findWidget('Dialog-New material:name').delete_text(14, 15)
findWidget('Dialog-New material:name').insert_text('l', 14)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.New
assert tests.chooserCheck('OOF2:Materials Page:Pane:Material:MaterialList', ['yellow-material'])
assert tests.matlPageSensitizationCheck1()
findWidget('A Simple Example:TutorialScroll').get_vadjustment().set_value( 5.7166465309633e+01)
findWidget('A Simple Example:TutorialScroll').get_vadjustment().set_value( 9.0166465309633e+01)
findWidget('A Simple Example:TutorialScroll').get_vadjustment().set_value( 1.0200000000000e+02)
findWidget('A Simple Example:Next').clicked()
findWidget('A Simple Example').resize(500, 308)
findWidget('A Simple Example').resize(500, 314)
findWidget('A Simple Example').resize(500, 316)
findWidget('A Simple Example').resize(500, 323)
findWidget('A Simple Example').resize(500, 331)
findWidget('A Simple Example').resize(500, 339)
findWidget('A Simple Example').resize(500, 344)
findWidget('A Simple Example').resize(500, 354)
findWidget('A Simple Example').resize(500, 364)
findWidget('A Simple Example').resize(500, 368)
findWidget('A Simple Example').resize(500, 380)
findWidget('A Simple Example').resize(500, 388)
findWidget('A Simple Example').resize(500, 391)
findWidget('A Simple Example').resize(500, 395)
findWidget('A Simple Example').resize(500, 400)
findWidget('A Simple Example').resize(500, 410)
findWidget('A Simple Example').resize(500, 414)
findWidget('A Simple Example').resize(500, 419)
findWidget('A Simple Example').resize(500, 421)
findWidget('A Simple Example').resize(500, 426)
findWidget('A Simple Example').resize(500, 428)
findWidget('A Simple Example').resize(500, 432)
findWidget('A Simple Example').resize(500, 434)
findWidget('A Simple Example').resize(500, 433)
findWidget('A Simple Example').resize(500, 436)
findWidget('A Simple Example').resize(500, 435)
findWidget('A Simple Example').resize(500, 438)
findWidget('A Simple Example').resize(500, 439)
findWidget('A Simple Example').resize(500, 438)
findWidget('A Simple Example').resize(500, 437)
findWidget('A Simple Example').resize(500, 436)
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
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.New
assert tests.chooserCheck('OOF2:Materials Page:Pane:Material:MaterialList', ['cyan-material', 'yellow-material'])
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
widget_5 = findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
event(Gdk.EventType.BUTTON_RELEASE,x= 1.3000000000000e+01,y= 2.4000000000000e+01,button=1,state=256,window=widget_5.get_window())
del widget_5
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
widget_6 = findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
event(Gdk.EventType.BUTTON_RELEASE,x= 2.9000000000000e+01,y= 4.6000000000000e+01,button=1,state=256,window=widget_6.get_window())
del widget_6
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([1, 0, 0]))
checkpoint Materials page updated
checkpoint property selected
assert tests.matlPageSensitizationCheck2()
widget_7 = findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
event(Gdk.EventType.BUTTON_RELEASE,x= 7.7000000000000e+01,y= 6.4000000000000e+01,button=1,state=256,window=widget_7.get_window())
del widget_7
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
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity').resize(538, 330)
widget_8 = findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:Chooser')
event(Gdk.EventType.BUTTON_PRESS,x= 1.5900000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=widget_8.get_window())
del widget_8
checkpoint toplevel widget mapped chooserPopup-Chooser
widget_9=findMenu(findWidget('chooserPopup-Chooser'), 'Cij')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_9.get_window())
del widget_9
widget_10=findMenu(findWidget('chooserPopup-Chooser'), 'Lame')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_10.get_window())
del widget_10
widget_11=findMenu(findWidget('chooserPopup-Chooser'), 'E and nu')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_11.get_window())
del widget_11
findMenu(findWidget('chooserPopup-Chooser'), 'E and nu').activate()
widget_12=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:Cij:0,0')
if widget_12: event(Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_12.get_window())
del widget_12
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:E and nu:young').set_text('')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:E and nu:young').set_text('1')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:E and nu:young').set_text('1.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:E and nu:young').set_text('1.0')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:E and nu:poisson').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:cijkl:E and nu:poisson').set_text('0.3')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;yellow_elasticity:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.yellow_elasticity
assert tests.selectedPropertyCheck('Mechanical:Elasticity:Isotropic:yellow_elasticity')
findWidget('A Simple Example:Next').clicked()
widget_13 = findWidget('OOF2:Materials Page:Pane:Material:MaterialList')
event(Gdk.EventType.BUTTON_PRESS,x= 8.9000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=widget_13.get_window())
del widget_13
checkpoint toplevel widget mapped chooserPopup-MaterialList
widget_14=findMenu(findWidget('chooserPopup-MaterialList'), 'cyan-material')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_14.get_window())
del widget_14
widget_15=findMenu(findWidget('chooserPopup-MaterialList'), 'yellow-material')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_15.get_window())
del widget_15
findMenu(findWidget('chooserPopup-MaterialList'), 'yellow-material').activate()
checkpoint Materials page updated
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Add_property
assert tests.matlPageSensitizationCheck4()
assert tests.selectedMatlPropertyCheck('Mechanical:Elasticity:Isotropic:yellow_elasticity')
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path(Gtk.TreePath([1, 0, 0]))
checkpoint Materials page updated
checkpoint property deselected
checkpoint Materials page updated
checkpoint property selected
widget_16 = findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
event(Gdk.EventType.BUTTON_RELEASE,x= 8.0000000000000e+01,y= 6.1000000000000e+01,button=1,state=256,window=widget_16.get_window())
del widget_16
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Isotropic
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic').resize(192, 92)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').delete_text(0, 6)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('c', 0)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('y', 1)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('a', 2)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('n', 3)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy
findWidget('A Simple Example:Next').clicked()
widget_17 = findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
event(Gdk.EventType.BUTTON_RELEASE,x= 1.1900000000000e+02,y= 1.0300000000000e+02,button=1,state=256,window=widget_17.get_window())
del widget_17
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([1, 0, 0, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity').resize(538, 330)
widget_18 = findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity:cijkl:Chooser')
event(Gdk.EventType.BUTTON_PRESS,x= 1.3800000000000e+02,y= 1.1000000000000e+01,button=1,state=0,window=widget_18.get_window())
del widget_18
checkpoint toplevel widget mapped chooserPopup-Chooser
widget_19=findMenu(findWidget('chooserPopup-Chooser'), 'Cij')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_19.get_window())
del widget_19
widget_20=findMenu(findWidget('chooserPopup-Chooser'), 'Lame')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_20.get_window())
del widget_20
widget_21=findMenu(findWidget('chooserPopup-Chooser'), 'E and nu')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_21.get_window())
del widget_21
findMenu(findWidget('chooserPopup-Chooser'), 'E and nu').activate()
widget_22=findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity:cijkl:Cij:0,0')
if widget_22: event(Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_22.get_window())
del widget_22
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity:cijkl:E and nu:young').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity:cijkl:E and nu:young').set_text('0.5')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity:cijkl:E and nu:poisson').set_text('0.')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity:cijkl:E and nu:poisson').set_text('0.3')
findWidget('Dialog-Parametrize Mechanical;Elasticity;Isotropic;cyan_elasticity:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.cyan_elasticity
assert tests.selectedPropertyCheck('Mechanical:Elasticity:Isotropic:cyan_elasticity')
findWidget('A Simple Example:Next').clicked()
widget_23 = findWidget('OOF2:Materials Page:Pane:Material:MaterialList')
event(Gdk.EventType.BUTTON_PRESS,x= 6.9000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=widget_23.get_window())
del widget_23
checkpoint toplevel widget mapped chooserPopup-MaterialList
widget_24=findMenu(findWidget('chooserPopup-MaterialList'), 'cyan-material')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_24.get_window())
del widget_24
findMenu(findWidget('chooserPopup-MaterialList'), 'cyan-material').activate()
checkpoint Materials page updated
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
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
widget_25 = findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
event(Gdk.EventType.BUTTON_RELEASE,x= 5.6000000000000e+01,y= 1.2000000000000e+01,button=1,state=256,window=widget_25.get_window())
del widget_25
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
widget_26 = findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
event(Gdk.EventType.BUTTON_RELEASE,x= 6.2000000000000e+01,y= 2.4000000000000e+01,button=1,state=256,window=widget_26.get_window())
del widget_26
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Color;yellow
findWidget('Dialog-Parametrize Color;yellow').resize(279, 206)
widget_27 = findWidget('Dialog-Parametrize Color;yellow:color:Chooser')
event(Gdk.EventType.BUTTON_PRESS,x= 6.3000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=widget_27.get_window())
del widget_27
checkpoint toplevel widget mapped chooserPopup-Chooser
widget_28=findMenu(findWidget('chooserPopup-Chooser'), 'RGBAColor')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_28.get_window())
del widget_28
findMenu(findWidget('chooserPopup-Chooser'), 'RGBAColor').activate()
widget_29=findWidget('Dialog-Parametrize Color;yellow:color:TranslucentGray:gray:entry')
if widget_29: event(Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_29.get_window())
del widget_29
findWidget('Dialog-Parametrize Color;yellow').resize(280, 274)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:red:slider').get_adjustment().set_value( 9.7222222222222e-02)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:red:slider').get_adjustment().set_value( 2.6388888888889e-01)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:red:slider').get_adjustment().set_value( 4.7222222222222e-01)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:red:slider').get_adjustment().set_value( 6.8055555555556e-01)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:red:slider').get_adjustment().set_value( 9.3055555555556e-01)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:red:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:green:entry').set_text('0.')
findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:green:entry').set_text('0.8')
widget_30=findWidget('Dialog-Parametrize Color;yellow:color:RGBAColor:green:entry')
if widget_30: event(Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_30.get_window())
del widget_30
findWidget('Dialog-Parametrize Color;yellow:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Property.Parametrize.Color.yellow
widget_31 = findWidget('OOF2:Materials Page:Pane:Material:MaterialList')
event(Gdk.EventType.BUTTON_PRESS,x= 5.8000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=widget_31.get_window())
del widget_31
checkpoint toplevel widget mapped chooserPopup-MaterialList
widget_32=findMenu(findWidget('chooserPopup-MaterialList'), 'cyan-material')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_32.get_window())
del widget_32
widget_33=findMenu(findWidget('chooserPopup-MaterialList'), 'yellow-material')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_33.get_window())
del widget_33
findMenu(findWidget('chooserPopup-MaterialList'), 'yellow-material').activate()
checkpoint Materials page updated
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
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
widget_34 = findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
event(Gdk.EventType.BUTTON_RELEASE,x= 5.2000000000000e+01,y= 8.0000000000000e+00,button=1,state=256,window=widget_34.get_window())
del widget_34
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Color
findWidget('Dialog-Copy property Color').resize(192, 92)
findWidget('Dialog-Copy property Color:new_name').delete_text(0, 6)
findWidget('Dialog-Copy property Color:new_name').insert_text('c', 11)
findWidget('Dialog-Copy property Color:new_name').insert_text('a', 1)
findWidget('Dialog-Copy property Color:new_name').insert_text('y', 2)
findWidget('Dialog-Copy property Color:new_name').insert_text('n', 3)
findWidget('Dialog-Copy property Color:new_name').delete_text(3, 4)
findWidget('Dialog-Copy property Color:new_name').delete_text(2, 3)
findWidget('Dialog-Copy property Color:new_name').delete_text(1, 2)
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
widget_35 = findWidget('Dialog-Parametrize Color;cyan:color:Chooser')
event(Gdk.EventType.BUTTON_PRESS,x= 7.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=widget_35.get_window())
del widget_35
checkpoint toplevel widget mapped chooserPopup-Chooser
widget_36=findMenu(findWidget('chooserPopup-Chooser'), 'RGBAColor')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_36.get_window())
del widget_36
findMenu(findWidget('chooserPopup-Chooser'), 'RGBAColor').activate()
widget_37=findWidget('Dialog-Parametrize Color;cyan:color:TranslucentGray:gray:entry')
if widget_37: event(Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_37.get_window())
del widget_37
findWidget('Dialog-Parametrize Color;cyan').resize(280, 274)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:entry').set_text('0.')
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:entry').set_text('0.8')
widget_38=findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:green:entry')
if widget_38: event(Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_38.get_window())
del widget_38
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:blue:slider').get_adjustment().set_value( 9.7222222222222e-02)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:blue:slider').get_adjustment().set_value( 2.6388888888889e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:blue:slider').get_adjustment().set_value( 5.0000000000000e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:blue:slider').get_adjustment().set_value( 8.6111111111111e-01)
findWidget('Dialog-Parametrize Color;cyan:color:RGBAColor:blue:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('Dialog-Parametrize Color;cyan:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Property.Parametrize.Color.cyan
widget_39 = findWidget('OOF2:Materials Page:Pane:Material:MaterialList')
event(Gdk.EventType.BUTTON_PRESS,x= 9.8000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=widget_39.get_window())
del widget_39
checkpoint toplevel widget mapped chooserPopup-MaterialList
widget_40=findMenu(findWidget('chooserPopup-MaterialList'), 'cyan-material')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_40.get_window())
del widget_40
findMenu(findWidget('chooserPopup-MaterialList'), 'cyan-material').activate()
checkpoint Materials page updated
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint property selected
checkpoint Materials page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Add_property
assert tests.materialCheck('cyan-material',  ['Mechanical:Elasticity:Isotropic:cyan_elasticity', 'Color:cyan'])
assert tests.selectedMatlPropertyCheck('Color:cyan')
findWidget('A Simple Example:Next').clicked()
widget_41 = findWidget('OOF2:Materials Page:Pane:Material:MaterialList')
event(Gdk.EventType.BUTTON_PRESS,x= 1.1500000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=widget_41.get_window())
del widget_41
checkpoint toplevel widget mapped chooserPopup-MaterialList
widget_42=findMenu(findWidget('chooserPopup-MaterialList'), 'cyan-material')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_42.get_window())
del widget_42
widget_43=findMenu(findWidget('chooserPopup-MaterialList'), 'yellow-material')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_43.get_window())
del widget_43
findMenu(findWidget('chooserPopup-MaterialList'), 'yellow-material').activate()
checkpoint Materials page updated
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material yellow-material to pixels
findWidget('Dialog-Assign material yellow-material to pixels').resize(221, 122)
widget_44 = findWidget('Dialog-Assign material yellow-material to pixels:pixels')
event(Gdk.EventType.BUTTON_PRESS,x= 7.9000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=widget_44.get_window())
del widget_44
checkpoint toplevel widget mapped chooserPopup-pixels
widget_45=findMenu(findWidget('chooserPopup-pixels'), '<selection>')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_45.get_window())
del widget_45
widget_46=findMenu(findWidget('chooserPopup-pixels'), '<every>')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_46.get_window())
del widget_46
widget_47=findMenu(findWidget('chooserPopup-pixels'), 'cyan')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_47.get_window())
del widget_47
widget_48=findMenu(findWidget('chooserPopup-pixels'), 'yellow')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_48.get_window())
del widget_48
findMenu(findWidget('chooserPopup-pixels'), 'yellow').activate()
findWidget('Dialog-Assign material yellow-material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign
findWidget('A Simple Example:Next').clicked()
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'Layer:New').activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(203, 193)
widget_49 = findWidget('Dialog-New:category')
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=widget_49.get_window())
del widget_49
checkpoint toplevel widget mapped chooserPopup-category
widget_50=findMenu(findWidget('chooserPopup-category'), 'Image')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_50.get_window())
del widget_50
widget_51=findMenu(findWidget('chooserPopup-category'), 'Microstructure')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_51.get_window())
del widget_51
findMenu(findWidget('chooserPopup-category'), 'Microstructure').activate()
findWidget('Dialog-New').resize(395, 532)
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
findWidget('A Simple Example:Next').clicked()
widget_52 = findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
event(Gdk.EventType.BUTTON_PRESS,x= 1.9000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=widget_52.get_window())
del widget_52
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
widget_53 = findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
event(Gdk.EventType.BUTTON_PRESS,x= 1.9000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=widget_53.get_window())
del widget_53
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
widget_54 = findWidget('OOF2:Materials Page:Pane:Material:MaterialList')
event(Gdk.EventType.BUTTON_PRESS,x= 5.1000000000000e+01,y= 2.2000000000000e+01,button=1,state=0,window=widget_54.get_window())
del widget_54
checkpoint toplevel widget mapped chooserPopup-MaterialList
widget_55=findMenu(findWidget('chooserPopup-MaterialList'), 'cyan-material')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_55.get_window())
del widget_55
findMenu(findWidget('chooserPopup-MaterialList'), 'cyan-material').activate()
checkpoint Materials page updated
checkpoint Materials page updated
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material cyan-material to pixels
findWidget('Dialog-Assign material cyan-material to pixels').resize(221, 122)
widget_56 = findWidget('Dialog-Assign material cyan-material to pixels:pixels')
event(Gdk.EventType.BUTTON_PRESS,x= 5.5000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=widget_56.get_window())
del widget_56
checkpoint toplevel widget mapped chooserPopup-pixels
widget_57=findMenu(findWidget('chooserPopup-pixels'), '<selection>')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_57.get_window())
del widget_57
widget_58=findMenu(findWidget('chooserPopup-pixels'), '<every>')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_58.get_window())
del widget_58
widget_59=findMenu(findWidget('chooserPopup-pixels'), 'cyan')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_59.get_window())
del widget_59
findMenu(findWidget('chooserPopup-pixels'), 'cyan').activate()
findWidget('Dialog-Assign material cyan-material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign
findWidget('A Simple Example:Next').clicked()
widget_60 = findWidget('OOF2:Navigation:PageMenu')
event(Gdk.EventType.BUTTON_PRESS,x= 1.0100000000000e+02,y= 2.1000000000000e+01,button=1,state=0,window=widget_60.get_window())
del widget_60
checkpoint toplevel widget mapped chooserPopup-PageMenu
widget_61=findMenu(findWidget('chooserPopup-PageMenu'), 'Introduction')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_61.get_window())
del widget_61
widget_62=findMenu(findWidget('chooserPopup-PageMenu'), 'Microstructure')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_62.get_window())
del widget_62
widget_63=findMenu(findWidget('chooserPopup-PageMenu'), 'Image')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_63.get_window())
del widget_63
widget_64=findMenu(findWidget('chooserPopup-PageMenu'), 'Pixel Selection')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_64.get_window())
del widget_64
widget_65=findMenu(findWidget('chooserPopup-PageMenu'), 'Active Area')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_65.get_window())
del widget_65
widget_66=findMenu(findWidget('chooserPopup-PageMenu'), 'Materials')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_66.get_window())
del widget_66
widget_67=findMenu(findWidget('chooserPopup-PageMenu'), 'Skeleton')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_67.get_window())
del widget_67
findMenu(findWidget('chooserPopup-PageMenu'), 'Skeleton').activate()
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
assert tests.skeletonPageSensitivityCheck0()
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page sensitized
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
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
checkpoint named boundary analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized
checkpoint Solver page sensitized
checkpoint skeleton page info updated
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New
assert tests.skeletonPageSensitivityCheck1()
findWidget('A Simple Example:Next').clicked()
widget_68 = findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Chooser')
event(Gdk.EventType.BUTTON_PRESS,x= 1.7400000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=widget_68.get_window())
del widget_68
checkpoint toplevel widget mapped chooserPopup-Chooser
widget_69=findMenu(findWidget('chooserPopup-Chooser'), 'Refine')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_69.get_window())
del widget_69
widget_70=findMenu(findWidget('chooserPopup-Chooser'), 'Relax')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_70.get_window())
del widget_70
widget_71=findMenu(findWidget('chooserPopup-Chooser'), 'Snap Nodes')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_71.get_window())
del widget_71
widget_72=findMenu(findWidget('chooserPopup-Chooser'), 'Split Quads')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_72.get_window())
del widget_72
widget_73=findMenu(findWidget('chooserPopup-Chooser'), 'Snap Nodes')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_73.get_window())
del widget_73
findMenu(findWidget('chooserPopup-Chooser'), 'Snap Nodes').activate()
findWidget('OOF2:Skeleton Page:Pane').set_position(437)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 2.9166666666667e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 3.4722222222222e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 3.7500000000000e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 4.3055555555556e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 5.1388888888889e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 6.2500000000000e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 7.5000000000000e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 9.1666666666667e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Snap Nodes:criterion:Average Energy:alpha:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Skeleton Page:Pane:Modification:OK').clicked()
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Modify
assert tests.skeletonPageSensitivityCheck2()
findWidget('A Simple Example:Next').clicked()
widget_74 = findWidget('OOF2:Navigation:PageMenu')
event(Gdk.EventType.BUTTON_PRESS,x= 3.7000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=widget_74.get_window())
del widget_74
checkpoint toplevel widget mapped chooserPopup-PageMenu
widget_75=findMenu(findWidget('chooserPopup-PageMenu'), 'Introduction')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_75.get_window())
del widget_75
widget_76=findMenu(findWidget('chooserPopup-PageMenu'), 'Microstructure')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_76.get_window())
del widget_76
widget_77=findMenu(findWidget('chooserPopup-PageMenu'), 'Image')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_77.get_window())
del widget_77
widget_78=findMenu(findWidget('chooserPopup-PageMenu'), 'Pixel Selection')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_78.get_window())
del widget_78
widget_79=findMenu(findWidget('chooserPopup-PageMenu'), 'Active Area')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_79.get_window())
del widget_79
widget_80=findMenu(findWidget('chooserPopup-PageMenu'), 'Materials')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_80.get_window())
del widget_80
widget_81=findMenu(findWidget('chooserPopup-PageMenu'), 'Skeleton')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_81.get_window())
del widget_81
widget_82=findMenu(findWidget('chooserPopup-PageMenu'), 'Pin Nodes')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_82.get_window())
del widget_82
widget_83=findMenu(findWidget('chooserPopup-PageMenu'), 'Skeleton Selection')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_83.get_window())
del widget_83
widget_84=findMenu(findWidget('chooserPopup-PageMenu'), 'Skeleton Boundaries')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_84.get_window())
del widget_84
widget_85=findMenu(findWidget('chooserPopup-PageMenu'), 'FE Mesh')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_85.get_window())
del widget_85
findMenu(findWidget('chooserPopup-PageMenu'), 'FE Mesh').activate()
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
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
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint named boundary analysis chooser set
checkpoint named boundary analysis chooser set
checkpoint mesh bdy page updated
checkpoint named boundary analysis chooser set
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
checkpoint_count("Field page sensitized")
assert tests.fieldPageSensitivityCheck0()
findWidget('OOF2:Fields & Equations Page:HPane').set_position(470)
findWidget('OOF2:Fields & Equations Page:HPane:Fields:Displacement defined').clicked()
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint named boundary analysis chooser set
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
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint named boundary analysis chooser set
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
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint named boundary analysis chooser set
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
checkpoint Field page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint named boundary analysis chooser set
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
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 362)
findWidget('Dialog-New Boundary Condition:name').delete_text(0, 11)
findWidget('Dialog-New Boundary Condition:name').insert_text('a', 11)
findWidget('Dialog-New Boundary Condition:name').insert_text('b', 1)
findWidget('Dialog-New Boundary Condition:name').insert_text('c', 2)
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
assert tests.bcPageSensitivityCheck1()
assert tests.treeViewColCheck('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList', 0, ['abc'])
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 362)
widget_86 = findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component')
event(Gdk.EventType.BUTTON_PRESS,x= 2.5000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=widget_86.get_window())
del widget_86
checkpoint toplevel widget mapped chooserPopup-field_component
widget_87=findMenu(findWidget('chooserPopup-field_component'), 'x')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_87.get_window())
del widget_87
widget_88=findMenu(findWidget('chooserPopup-field_component'), 'y')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_88.get_window())
del widget_88
findMenu(findWidget('chooserPopup-field_component'), 'y').activate()
widget_89 = findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component')
event(Gdk.EventType.BUTTON_PRESS,x= 3.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=widget_89.get_window())
del widget_89
checkpoint toplevel widget mapped chooserPopup-eqn_component
widget_90=findMenu(findWidget('chooserPopup-eqn_component'), 'x')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_90.get_window())
del widget_90
widget_91=findMenu(findWidget('chooserPopup-eqn_component'), 'y')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_91.get_window())
del widget_91
findMenu(findWidget('chooserPopup-eqn_component'), 'y').activate()
widget_92 = findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary')
event(Gdk.EventType.BUTTON_PRESS,x= 7.4000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=widget_92.get_window())
del widget_92
checkpoint toplevel widget mapped chooserPopup-boundary
widget_93=findMenu(findWidget('chooserPopup-boundary'), 'top')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_93.get_window())
del widget_93
widget_94=findMenu(findWidget('chooserPopup-boundary'), 'bottom')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_94.get_window())
del widget_94
widget_95=findMenu(findWidget('chooserPopup-boundary'), 'right')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_95.get_window())
del widget_95
widget_96=findMenu(findWidget('chooserPopup-boundary'), 'bottom')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_96.get_window())
del widget_96
findMenu(findWidget('chooserPopup-boundary'), 'bottom').activate()
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
assert tests.treeViewColCheck('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList', 0, ['abc', 'abc<2>'])
assert tests.listViewSelectedRowNo('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList') == 1
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Boundary Conditions Page:Condition:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary Condition
findWidget('Dialog-New Boundary Condition').resize(353, 362)
widget_97 = findWidget('Dialog-New Boundary Condition:condition:Dirichlet:field_component')
event(Gdk.EventType.BUTTON_PRESS,x= 3.6000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=widget_97.get_window())
del widget_97
checkpoint toplevel widget mapped chooserPopup-field_component
widget_98=findMenu(findWidget('chooserPopup-field_component'), 'x')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_98.get_window())
del widget_98
findMenu(findWidget('chooserPopup-field_component'), 'x').activate()
widget_99 = findWidget('Dialog-New Boundary Condition:condition:Dirichlet:eqn_component')
event(Gdk.EventType.BUTTON_PRESS,x= 4.3000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=widget_99.get_window())
del widget_99
checkpoint toplevel widget mapped chooserPopup-eqn_component
widget_100=findMenu(findWidget('chooserPopup-eqn_component'), 'x')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_100.get_window())
del widget_100
findMenu(findWidget('chooserPopup-eqn_component'), 'x').activate()
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Constant Profile:value').set_text('.0')
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Constant Profile:value').set_text('1.0')
findWidget('Dialog-New Boundary Condition:condition:Dirichlet:profile:Constant Profile:value').set_text('10.0')
widget_101 = findWidget('Dialog-New Boundary Condition:condition:Dirichlet:boundary')
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=widget_101.get_window())
del widget_101
checkpoint toplevel widget mapped chooserPopup-boundary
widget_102=findMenu(findWidget('chooserPopup-boundary'), 'top')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_102.get_window())
del widget_102
widget_103=findMenu(findWidget('chooserPopup-boundary'), 'bottom')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_103.get_window())
del widget_103
widget_104=findMenu(findWidget('chooserPopup-boundary'), 'right')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_104.get_window())
del widget_104
findMenu(findWidget('chooserPopup-boundary'), 'right').activate()
findWidget('Dialog-New Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint OOF.Mesh.Boundary_Conditions.New
assert tests.treeViewColCheck('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList', 0, ['abc', 'abc<2>', 'abc<3>'])
assert tests.listViewSelectedRowNo('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList') == 2
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Scheduled Output
findWidget('OOF2:Navigation:Next').clicked()
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
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2:Solver Page:solve').clicked()
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint toplevel widget mapped Warning
findWidget('Warning').resize(395, 68)
findWidget('Warning:widget_GTK_RESPONSE_OK').clicked()
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
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Scheduled Output
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Boundary Conditions
findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList').get_selection().select_path(Gtk.TreePath([0]))
tree=findWidget('OOF2:Boundary Conditions Page:Condition:BCScroll:BCList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([0]), column)
checkpoint toplevel widget mapped Dialog-Edit Boundary Condition
findWidget('Dialog-Edit Boundary Condition').resize(353, 326)
widget_105 = findWidget('Dialog-Edit Boundary Condition:condition:Dirichlet:boundary')
event(Gdk.EventType.BUTTON_PRESS,x= 4.4000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=widget_105.get_window())
del widget_105
checkpoint toplevel widget mapped chooserPopup-boundary
widget_106=findMenu(findWidget('chooserPopup-boundary'), 'top')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_106.get_window())
del widget_106
widget_107=findMenu(findWidget('chooserPopup-boundary'), 'bottom')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_107.get_window())
del widget_107
widget_108=findMenu(findWidget('chooserPopup-boundary'), 'right')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_108.get_window())
del widget_108
widget_109=findMenu(findWidget('chooserPopup-boundary'), 'left')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_109.get_window())
del widget_109
findMenu(findWidget('chooserPopup-boundary'), 'left').activate()
findWidget('Dialog-Edit Boundary Condition:widget_GTK_RESPONSE_OK').clicked()
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint named boundary analysis chooser set
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint OOF.Mesh.Boundary_Conditions.Edit
widget_110 = findWidget('OOF2:Navigation:PageMenu')
event(Gdk.EventType.BUTTON_PRESS,x= 9.0000000000000e+01,y= 2.2000000000000e+01,button=1,state=0,window=widget_110.get_window())
del widget_110
checkpoint toplevel widget mapped chooserPopup-PageMenu
widget_111=findMenu(findWidget('chooserPopup-PageMenu'), 'Introduction')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_111.get_window())
del widget_111
widget_112=findMenu(findWidget('chooserPopup-PageMenu'), 'Microstructure')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_112.get_window())
del widget_112
widget_113=findMenu(findWidget('chooserPopup-PageMenu'), 'Image')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_113.get_window())
del widget_113
widget_114=findMenu(findWidget('chooserPopup-PageMenu'), 'Pixel Selection')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_114.get_window())
del widget_114
widget_115=findMenu(findWidget('chooserPopup-PageMenu'), 'Active Area')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_115.get_window())
del widget_115
widget_116=findMenu(findWidget('chooserPopup-PageMenu'), 'Materials')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_116.get_window())
del widget_116
widget_117=findMenu(findWidget('chooserPopup-PageMenu'), 'Skeleton')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_117.get_window())
del widget_117
widget_118=findMenu(findWidget('chooserPopup-PageMenu'), 'Pin Nodes')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_118.get_window())
del widget_118
widget_119=findMenu(findWidget('chooserPopup-PageMenu'), 'Skeleton Selection')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_119.get_window())
del widget_119
widget_120=findMenu(findWidget('chooserPopup-PageMenu'), 'Skeleton Boundaries')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_120.get_window())
del widget_120
widget_121=findMenu(findWidget('chooserPopup-PageMenu'), 'FE Mesh')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_121.get_window())
del widget_121
widget_122=findMenu(findWidget('chooserPopup-PageMenu'), 'Fields & Equations')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_122.get_window())
del widget_122
widget_123=findMenu(findWidget('chooserPopup-PageMenu'), 'Boundary Conditions')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_123.get_window())
del widget_123
widget_124=findMenu(findWidget('chooserPopup-PageMenu'), 'Scheduled Output')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_124.get_window())
del widget_124
widget_125=findMenu(findWidget('chooserPopup-PageMenu'), 'Solver')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_125.get_window())
del widget_125
findMenu(findWidget('chooserPopup-PageMenu'), 'Solver').activate()
checkpoint Solver page sensitized
checkpoint page installed Solver
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
findWidget('A Simple Example:Next').clicked()
findWidget('A Simple Example:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.1000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.3000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 5.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.7111388830316e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.6111388830316e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.5111388830316e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.0111388830316e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 3.4111388830316e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
widget_126 = findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
event(Gdk.EventType.BUTTON_PRESS,x= 3.6400000000000e+02,y= 3.1000000000000e+01,button=1,state=0,window=widget_126.get_window())
del widget_126
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
widget_127 = findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
event(Gdk.EventType.BUTTON_PRESS,x= 3.6400000000000e+02,y= 3.1000000000000e+01,button=1,state=0,window=widget_127.get_window())
del widget_127
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([10]), column)
checkpoint toplevel widget mapped Dialog-Edit Graphics Layer
findWidget('Dialog-Edit Graphics Layer').resize(395, 532)
checkpoint OOF.Graphics_1.Layer.Select
widget_128=findWidget('Dialog-Edit Graphics Layer:how:Material:no_material:TranslucentGray:gray:entry')
if widget_128: event(Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_128.get_window())
del widget_128
findWidget('Dialog-Edit Graphics Layer:widget_GTK_RESPONSE_CANCEL').clicked()
widget_129 = findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
event(Gdk.EventType.BUTTON_PRESS,x= 3.8800000000000e+02,y= 3.1000000000000e+01,button=1,state=0,window=widget_129.get_window())
del widget_129
widget_130 = findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
event(Gdk.EventType.BUTTON_PRESS,x= 3.8800000000000e+02,y= 3.1000000000000e+01,button=1,state=0,window=widget_130.get_window())
del widget_130
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated(Gtk.TreePath([10]), column)
checkpoint toplevel widget mapped Dialog-Edit Graphics Layer
findWidget('Dialog-Edit Graphics Layer').resize(467, 484)
widget_131 = findWidget('Dialog-Edit Graphics Layer:how:Chooser')
event(Gdk.EventType.BUTTON_PRESS,x= 2.1700000000000e+02,y= 1.6000000000000e+01,button=1,state=0,window=widget_131.get_window())
del widget_131
checkpoint toplevel widget mapped chooserPopup-Chooser
widget_132=findMenu(findWidget('chooserPopup-Chooser'), 'Element Edges')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_132.get_window())
del widget_132
widget_133=findMenu(findWidget('chooserPopup-Chooser'), 'Material Color')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_133.get_window())
del widget_133
widget_134=findMenu(findWidget('chooserPopup-Chooser'), 'Perimeter')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_134.get_window())
del widget_134
widget_135=findMenu(findWidget('chooserPopup-Chooser'), 'Solid Fill')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_135.get_window())
del widget_135
widget_136=findMenu(findWidget('chooserPopup-Chooser'), 'Contour Line')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_136.get_window())
del widget_136
widget_137=findMenu(findWidget('chooserPopup-Chooser'), 'Filled Contour')
event(Gdk.EventType.ENTER_NOTIFY, window=widget_137.get_window())
del widget_137
findMenu(findWidget('chooserPopup-Chooser'), 'Filled Contour').activate()
findWidget('Dialog-Edit Graphics Layer').resize(483, 613)
findWidget('Dialog-Edit Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.8000000000000e+01)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Edit
findWidget('A Simple Example:Close').clicked()
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
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
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint OOF.Graphics_1.File.Close
