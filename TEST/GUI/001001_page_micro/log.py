# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
# No Microstructure defined
assert tests.sensitization0()
assert tests.stackStateTest("message", "No Microstructure defined!")
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('OOF2').resize(782, 545)
findWidget('Dialog-Create Microstructure:name').delete_text(0, 11)
findWidget('Dialog-Create Microstructure:name').insert_text('t', 11)
findWidget('Dialog-Create Microstructure:name').insert_text('e', 1)
findWidget('Dialog-Create Microstructure:name').insert_text('s', 2)
findWidget('Dialog-Create Microstructure:name').insert_text('t', 3)
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
# Microstructure defined, but no groups
assert tests.sensitization1()
assert tests.meshableButtonState(0)
assert tests.stackStateTest("message", "No pixel groups defined!")
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 11)
findWidget('Dialog-Create new pixel group:name').insert_text('a', 11)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set
# Microstructure with one group
assert tests.sensitization2()
assert tests.meshableButtonState(1)
assert tests.chooserListCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['a (0 pixels, meshable)'])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['a (0 pixels, meshable)'])
assert tests.stackStateTest("list")
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 1)
findWidget('Dialog-Create new pixel group:name').insert_text('b', 11)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
# Microstructure with two groups
assert tests.sensitization2()
assert tests.meshableButtonState(1)
assert tests.chooserListCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['a (0 pixels, meshable)', 'b (0 pixels, meshable)'])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['b (0 pixels, meshable)'])
assert tests.meshableButtonState(1)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 1)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
assert tests.sensitization2()
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['pixelgroup (0 pixels, meshable)'])
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
# ... four groups
assert tests.sensitization2()
assert tests.meshableButtonState(1)
assert tests.chooserListCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['a (0 pixels, meshable)', 'b (0 pixels, meshable)', 'pixelgroup (0 pixels, meshable)', 'pixelgroup<2> (0 pixels, meshable)'])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['pixelgroup<2> (0 pixels, meshable)'])
assert tests.meshableButtonState(1)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Meshable').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Meshable
# not meshable
assert tests.sensitization2()
assert tests.chooserListCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['a (0 pixels, meshable)', 'b (0 pixels, meshable)', 'pixelgroup (0 pixels, meshable)', 'pixelgroup<2> (0 pixels)'])
assert tests.meshableButtonState(0)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.meshableButtonState(1)
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['b (0 pixels, meshable)'])
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Meshable').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Meshable
assert tests.meshableButtonState(0)
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['b (0 pixels)'])
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.meshableButtonState(1)
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['a (0 pixels, meshable)'])
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.meshableButtonState(0)
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['b (0 pixels)'])
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([2]))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.meshableButtonState(1)
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['pixelgroup (0 pixels, meshable)'])
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([3]))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.meshableButtonState(0)
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['pixelgroup<2> (0 pixels)'])

findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['b (0 pixels)'])
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(184, 86)
findWidget('Questioner:Yes').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.Delete
checkpoint microstructure page sensitized
checkpoint meshable button set
# Group deleted. No group selected.
assert tests.sensitization1()
assert tests.chooserListCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['a (0 pixels, meshable)', 'pixelgroup (0 pixels, meshable)', 'pixelgroup<2> (0 pixels)'])
event(Gdk.EventType.BUTTON_PRESS,x= 7.9000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Pixel Selection
findWidget('OOF2:Pixel Selection Page:Pane').set_position(273)
checkpoint pixel page updated
checkpoint pixel page sensitized
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint OOF.PixelSelection.Invert
checkpoint pixel page updated
checkpoint pixel page sensitized
findWidget('OOF2:Navigation:PrevHist').clicked()
checkpoint page installed Microstructure
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
assert tests.sensitization1()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([1]))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.sensitization3()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.AddSelection
# Non-empty pixel group
assert tests.sensitization4()
assert tests.chooserListCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['a (0 pixels, meshable)', 'pixelgroup (100 pixels, meshable)', 'pixelgroup<2> (0 pixels)'])
assert tests.meshableButtonState(1)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Remove').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.RemoveSelection
assert tests.sensitization5()
assert tests.chooserListCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['a (0 pixels, meshable)', 'pixelgroup (0 pixels, meshable)', 'pixelgroup<2> (0 pixels)'])
assert tests.meshableButtonState(1)
# Load a Microstructure containing an image
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
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
assert tests.sensitization6()
assert tests.stackStateTest("message", "No pixel groups defined!")
assert tests.chooserCheck('OOF2:Microstructure Page:Microstructure', ['test', 'small.ppm'])
assert tests.chooserStateCheck('OOF2:Microstructure Page:Microstructure', 'small.ppm')
findWidget('OOF2:Microstructure Page:NewFromImage').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure from Image
findWidget('Dialog-Create Microstructure from Image').resize(192, 230)
event(Gdk.EventType.BUTTON_PRESS,x= 7.7000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('Dialog-Create Microstructure from Image:image:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['small.ppm']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
event(Gdk.EventType.KEY_PRESS, keyval=Gdk.keyval_from_name('2'), state=0, window=findWidget('Dialog-Create Microstructure from Image:image:Microstructure').get_window())
findWidget('Dialog-Create Microstructure from Image:name').insert_text('2', 6)
findWidget('Dialog-Create Microstructure from Image:name').insert_text('s', 1)
findWidget('Dialog-Create Microstructure from Image:name').insert_text('m', 2)
findWidget('Dialog-Create Microstructure from Image:name').insert_text('a', 3)
findWidget('Dialog-Create Microstructure from Image:name').insert_text('l', 4)
findWidget('Dialog-Create Microstructure from Image:name').insert_text('l', 5)
findWidget('Dialog-Create Microstructure from Image:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
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
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_Image
assert tests.sensitization6()
assert tests.stackStateTest("message", "No pixel groups defined!")
assert tests.chooserCheck("OOF2:Microstructure Page:Microstructure", ['test', 'small.ppm', '2small'])
assert tests.chooserStateCheck("OOF2:Microstructure Page:Microstructure", '2small')
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(184, 86)
findWidget('Questioner:Yes').clicked()
checkpoint microstructure page sensitized
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
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.Delete
assert tests.sensitization7()
assert tests.stackStateTest("list")
assert tests.chooserCheck("OOF2:Microstructure Page:Microstructure", ['test', 'small.ppm'])
assert tests.chooserStateCheck("OOF2:Microstructure Page:Microstructure", 'test')
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(184, 86)
findWidget('Questioner:Yes').clicked()
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
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.Delete
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
