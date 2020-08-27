import tests
assert tests.existence()
assert tests.gui_open()
assert tests.mainPageCheck('Introduction')
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 495)
findMenu(findWidget('OOF2:MenuBar'), 'Help:Tutorials').activate()
findMenu(findWidget('OOF2:MenuBar'), 'Help:Tutorials:Basics').activate()
checkpoint toplevel widget mapped Basics
assert tests.tutorialPageCheck(0)
findWidget('Basics').resize(500, 300)
findWidget('OOF2').resize(782, 529)
findWidget('Basics').resize(500, 300)
findWidget('Basics').resize(500, 310)
findWidget('Basics').resize(500, 320)
findWidget('Basics').resize(500, 328)
findWidget('Basics').resize(500, 347)
findWidget('Basics').resize(500, 371)
findWidget('Basics').resize(500, 400)
findWidget('Basics').resize(500, 417)
findWidget('Basics').resize(500, 452)
findWidget('Basics').resize(500, 469)
findWidget('Basics').resize(500, 520)
findWidget('Basics').resize(500, 559)
findWidget('Basics').resize(500, 571)
findWidget('Basics').resize(500, 605)
findWidget('Basics').resize(500, 616)
findWidget('Basics').resize(500, 641)
findWidget('Basics').resize(500, 648)
findWidget('Basics').resize(500, 663)
findWidget('Basics').resize(500, 666)
findWidget('Basics').resize(500, 676)
findWidget('Basics').resize(500, 679)
findWidget('Basics').resize(500, 694)
findWidget('Basics').resize(500, 696)
findWidget('Basics').resize(500, 699)
findWidget('Basics').resize(500, 700)
findWidget('Basics').resize(500, 703)
findWidget('Basics').resize(500, 705)
findWidget('Basics').resize(500, 712)
findWidget('Basics').resize(500, 714)
findWidget('Basics').resize(500, 717)
findWidget('Basics').resize(500, 716)
findWidget('Basics:Next').clicked()
assert tests.tutorialPageCheck(1)
findWidget('Basics:Next').clicked()
findWidget('Basics:Next').clicked()
findWidget('Basics:Next').clicked()
findWidget('Basics:Next').clicked()
widget_0 = findWidget('OOF2:Navigation:PageMenu')
widget_0.event(event(Gdk.EventType.BUTTON_PRESS,x= 1.0400000000000e+02,y= 2.5000000000000e+01,button=1,state=0,window=widget_0.get_window()))
del widget_0
checkpoint toplevel widget mapped chooserPopup-PageMenu
widget_1=findMenu(findWidget('chooserPopup-PageMenu'), 'Introduction')
widget_1.event(event(Gdk.EventType.ENTER_NOTIFY, window=widget_1.get_window()))
del widget_1
widget_2=findMenu(findWidget('chooserPopup-PageMenu'), 'Microstructure')
widget_2.event(event(Gdk.EventType.ENTER_NOTIFY, window=widget_2.get_window()))
del widget_2
findMenu(findWidget('chooserPopup-PageMenu'), 'Microstructure').activate()
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
assert tests.mainPageCheck('Microstructure')
assert tests.msPageSensitizationCheck0()
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('Basics:Next').clicked()
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
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/s')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/sm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/sma')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/smal')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small.pp')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/small.ppm')
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
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint Solver page sensitized
findWidget('OOF2').resize(782, 545)
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
# Image loaded
assert tests.whoNameCheck('Microstructure', ['small.ppm'])
assert tests.chooserCheck('OOF2:Microstructure Page:Microstructure', ['small.ppm'])
assert tests.msPageSensitizationCheck1()
# Test the testers.  The following three tests should report errors.
assert not tests.chooserCheck('OOF2:Microstructure Page:Microstructure', [])
assert not tests.chooserCheck('OOF2:Microstructure Page:Microstructure', ['smell.ppm'])
assert not tests.chooserCheck('OOF2:Microstructure Page:Microstructure', ['small.ppm', 'big.ppm'])
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Messages:Message_1').activate()
findWidget('OOF2 Messages 1').resize(410, 130)
findWidget('Basics:Next').clicked()
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
assert tests.gfxWindowCheck(['Graphics_1'])
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(671)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(669)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(211)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(658)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(208)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(656)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(207)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(651)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(206)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(649)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(205)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(648)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(646)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(204)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(647)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(648)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(205)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(653)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(206)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(654)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(662)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(209)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(663)
findWidget('Basics:Next').clicked()
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Activity_Viewer').activate()
checkpoint toplevel widget mapped OOF2 Activity Viewer
checkpoint OOF.Windows.Activity_Viewer
findWidget('OOF2 Activity Viewer').resize(400, 300)
findWidget('Basics:Next').clicked()
findWidget('Basics:Back').clicked()
widget_3 = findWidget('OOF2:Navigation:PageMenu')
widget_3.event(event(Gdk.EventType.BUTTON_PRESS,x= 1.1700000000000e+02,y= 1.9000000000000e+01,button=1,state=0,window=widget_3.get_window()))
del widget_3
checkpoint toplevel widget mapped chooserPopup-PageMenu
widget_4=findMenu(findWidget('chooserPopup-PageMenu'), 'Introduction')
widget_4.event(event(Gdk.EventType.ENTER_NOTIFY, window=widget_4.get_window()))
del widget_4
widget_5=findMenu(findWidget('chooserPopup-PageMenu'), 'Microstructure')
widget_5.event(event(Gdk.EventType.ENTER_NOTIFY, window=widget_5.get_window()))
del widget_5
widget_6=findMenu(findWidget('chooserPopup-PageMenu'), 'Image')
widget_6.event(event(Gdk.EventType.ENTER_NOTIFY, window=widget_6.get_window()))
del widget_6
findMenu(findWidget('chooserPopup-PageMenu'), 'Image').activate()
checkpoint page installed Image
findWidget('OOF2:Image Page:Pane').set_position(546)
findWidget('OOF2:Image Page:Group').clicked()
checkpoint toplevel widget mapped Dialog-AutoGroup
findWidget('Dialog-AutoGroup').resize(207, 92)
findWidget('Dialog-AutoGroup:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll').get_vadjustment().set_value( 9.0000000000000e+01)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll').get_vadjustment().set_value( 1.8000000000000e+01)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.Image.AutoGroup
assert tests.countMSGroups('small.ppm') == 8
findWidget('OOF2:Navigation:Prev').clicked()
assert tests.msPageSensitizationCheck2()
assert tests.treeViewLength('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList') == 8
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('Basics:Next').clicked()
findWidget('Basics:Next').clicked()
findMenu(findWidget('OOF2:MenuBar'), 'File:Load:Script').activate()
checkpoint toplevel widget mapped Dialog-Script
findWidget('Dialog-Script').resize(192, 92)
findWidget('Dialog-Script:filename').set_text('')
findWidget('Dialog-Script:filename').set_text('e')
findWidget('Dialog-Script:filename').set_text('ex')
findWidget('Dialog-Script:filename').set_text('exa')
findWidget('Dialog-Script:filename').set_text('exam')
findWidget('Dialog-Script:filename').set_text('examp')
findWidget('Dialog-Script:filename').set_text('exampl')
findWidget('Dialog-Script:filename').set_text('example')
findWidget('Dialog-Script:filename').set_text('examples')
findWidget('Dialog-Script:filename').set_text('examples/')
findWidget('Dialog-Script:filename').set_text('examples/e')
findWidget('Dialog-Script:filename').set_text('examples/er')
findWidget('Dialog-Script:filename').set_text('examples/err')
findWidget('Dialog-Script:filename').set_text('examples/erro')
findWidget('Dialog-Script:filename').set_text('examples/error')
findWidget('Dialog-Script:filename').set_text('examples/errorg')
findWidget('Dialog-Script:filename').set_text('examples/errorge')
findWidget('Dialog-Script:filename').set_text('examples/errorgen')
findWidget('Dialog-Script:filename').set_text('examples/errorgen.')
findWidget('Dialog-Script:filename').set_text('examples/errorgen.l')
findWidget('Dialog-Script:filename').set_text('examples/errorgen.lo')
findWidget('Dialog-Script:filename').set_text('examples/errorgen.log')
findWidget('Dialog-Script:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Load.Script
checkpoint toplevel widget mapped Error
findWidget('Error').resize(266, 150)
findWidget('Error').resize(266, 210)
findWidget('Error:ViewTraceback').clicked()
findWidget('Error').resize(266, 258)
findWidget('Error:ViewTraceback').clicked()
findWidget('Error:widget_GTK_RESPONSE_OK').clicked()
findWidget('Basics:Next').clicked()
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(192, 122)
findWidget('Dialog-Python_Log:filename').set_text('session.log')
widget_0 = findWidget('Dialog-Python_Log:mode')
widget_0.event(event(Gdk.EventType.BUTTON_PRESS,x= 5.9000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=widget_0.get_window()))
del widget_0
checkpoint toplevel widget mapped chooserPopup-mode
widget_1=findMenu(findWidget('chooserPopup-mode'), 'write')
widget_1.event(event(Gdk.EventType.ENTER_NOTIFY, window=widget_1.get_window()))
del widget_1
widget_2=findMenu(findWidget('chooserPopup-mode'), 'append')
widget_2.event(event(Gdk.EventType.ENTER_NOTIFY, window=widget_2.get_window()))
del widget_2
widget_3=findMenu(findWidget('chooserPopup-mode'), 'write')
widget_3.event(event(Gdk.EventType.ENTER_NOTIFY, window=widget_3.get_window()))
del widget_3
findMenu(findWidget('chooserPopup-mode'), 'write').activate()
findWidget('Dialog-Python_Log:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('session.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
