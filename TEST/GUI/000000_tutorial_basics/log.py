import tests
assert tests.existence()
assert tests.gui_open()
assert tests.mainPageCheck('Introduction')
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials', 'Basics']).activate()
checkpoint toplevel widget mapped Basics
findWidget('Basics').resize(500, 302)
findWidget('OOF2').resize(782, 545)
findWidget('Basics').resize(500, 302)
findWidget('Basics:Next').clicked()
assert tests.tutorialPageCheck(1)
findWidget('Basics').resize(500, 482)
findWidget('Basics:Next').clicked()
findWidget('Basics:Next').clicked()
findWidget('Basics:Next').clicked()
findWidget('Basics:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 7.5000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
assert tests.mainPageCheck('Microstructure')
assert tests.msPageSensitizationCheck0()
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('Basics:Next').clicked()
findWidget('Basics').resize(500, 518)
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
checkpoint active area status updated
checkpoint pixel page updated
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
checkpoint pixel page sensitized
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
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
assert tests.whoNameCheck('Microstructure', ['small.ppm'])
assert tests.chooserCheck('OOF2:Microstructure Page:Microstructure', ['small.ppm'])
assert tests.msPageSensitizationCheck1()
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Messages', 'Message_1']).activate()
findWidget('OOF2 Messages 1').resize(410, 130)
findWidget('Basics:Next').clicked()
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
assert tests.gfxWindowCheck(['Graphics_1'])
findWidget('Basics:Next').clicked()
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
event(Gdk.EventType.BUTTON_PRESS,x= 3.2000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Image']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 3.8000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New:what:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findWidget('chooserPopup-Microstructure').deactivate() # MenuLogger
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
findWidget('Basics:Next').clicked()
findWidget('Basics:Next').clicked()
findWidget('Basics:Next').clicked()
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Script']).activate()
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
findWidget('Error').resize(266, 210)
findWidget('Error:ViewTraceback').clicked()
findWidget('Error').resize(266, 258)
findWidget('Error:widget_GTK_RESPONSE_OK').clicked()
findWidget('Basics:Next').clicked()
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(336, 86)
findWidget('Questioner:Save').clicked()
checkpoint toplevel widget mapped Dialog-Save Log File
findWidget('Dialog-Save Log File').resize(192, 122)
findWidget('Dialog-Save Log File:widget_GTK_RESPONSE_CANCEL').clicked()
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
