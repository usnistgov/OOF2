# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)
event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
checkpoint page installed Microstructure
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('OOF2').resize(782, 545)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('Dialog-Create Microstructure:width_in_pixels').set_text('100')
findWidget('Dialog-Create Microstructure:height_in_pixels').set_text('100')
findWidget('Dialog-Create Microstructure:name').insert_text('m', 6)
findWidget('Dialog-Create Microstructure:name').insert_text('i', 1)
findWidget('Dialog-Create Microstructure:name').insert_text('c', 2)
findWidget('Dialog-Create Microstructure:name').insert_text('r', 3)
findWidget('Dialog-Create Microstructure:name').insert_text('o', 4)
findWidget('Dialog-Create Microstructure:name').insert_text('1', 5)
findWidget('Dialog-Create Microstructure:width').set_text('')
findWidget('Dialog-Create Microstructure:width').set_text('5')
findWidget('Dialog-Create Microstructure:height').set_text('')
findWidget('Dialog-Create Microstructure:height').set_text('5')
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
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.New
assert tests.sensitization1()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 11)
findWidget('Dialog-Create new pixel group:name').insert_text('a', 11)
findWidget('Dialog-Create new pixel group:name').insert_text('b', 1)
findWidget('Dialog-Create new pixel group:name').insert_text('d', 2)
findWidget('Dialog-Create new pixel group:name').insert_text('c', 3)
findWidget('Dialog-Create new pixel group:name').insert_text('d', 4)
findWidget('Dialog-Create new pixel group:name').insert_text('e', 5)
findWidget('Dialog-Create new pixel group:name').delete_text(2, 3)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set
#checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
assert tests.sensitization2()
assert tests.chooserListCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['abcde (0 pixels, meshable)'])
assert tests.meshableButtonState() == 1
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 5)
findWidget('Dialog-Create new pixel group:name').insert_text('f', 11)
findWidget('Dialog-Create new pixel group:name').insert_text('g', 1)
findWidget('Dialog-Create new pixel group:name').insert_text('h', 2)
findWidget('Dialog-Create new pixel group:name').insert_text('i', 3)
findWidget('Dialog-Create new pixel group:name').insert_text('j', 4)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
#checkpoint meshable button set
assert tests.sensitization2()
assert tests.chooserListCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['abcde (0 pixels, meshable)', 'fghij (0 pixels, meshable)'])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['fghij (0 pixels, meshable)'])
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['abcde (0 pixels, meshable)'])
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename pixelgroup abcde
findWidget('Dialog-Rename pixelgroup abcde').resize(192, 92)
findWidget('Dialog-Rename pixelgroup abcde:new_name').set_text('')
findWidget('Dialog-Rename pixelgroup abcde:new_name').set_text('k')
findWidget('Dialog-Rename pixelgroup abcde:new_name').set_text('kl')
findWidget('Dialog-Rename pixelgroup abcde:new_name').set_text('klm')
findWidget('Dialog-Rename pixelgroup abcde:new_name').set_text('klmn')
findWidget('Dialog-Rename pixelgroup abcde:new_name').set_text('klmno')
findWidget('Dialog-Rename pixelgroup abcde:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Rename
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.sensitization2()
assert tests.chooserListCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['fghij (0 pixels, meshable)', 'klmno (0 pixels, meshable)'])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['klmno (0 pixels, meshable)'])
assert tests.meshableButtonState() == 1
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Meshable').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Meshable
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['klmno (0 pixels)'])
assert tests.meshableButtonState() == 0
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
assert tests.chooserListCheck('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList', ['fghij (0 pixels, meshable)'])
assert tests.meshableButtonState() == 0
event(Gdk.EventType.BUTTON_PRESS,x= 7.4000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pixel Selection']).activate() # MenuItemLogger
checkpoint page installed Pixel Selection
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint pixel page updated
findWidget('OOF2:Pixel Selection Page:Pane').set_position(273)
checkpoint pixel page sensitized
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint OOF.PixelSelection.Invert
checkpoint pixel page updated
checkpoint pixel page sensitized
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Image
findWidget('OOF2:Image Page:Pane').set_position(546)
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Microstructure
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized

findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Stack:GroupListScroll:GroupList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint microstructure page sensitized
checkpoint_count("microstructure page sensitized")
assert tests.sensitization3()

findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint OOF.PixelGroup.AddSelection
assert tests.sensitization4()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Clear').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Clear
assert tests.sensitization3()
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
