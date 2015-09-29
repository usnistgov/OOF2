checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.15 $
# $Author: langer $
# $Date: 2010/12/27 07:24:48 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(150)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.sensitization0()
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(314, 168)
findWidget('Dialog-Create Microstructure:name:Auto').clicked()
findWidget('Dialog-Create Microstructure:name:Text').set_text('m')
findWidget('Dialog-Create Microstructure:name:Text').set_text('mi')
findWidget('Dialog-Create Microstructure:name:Text').set_text('mic')
findWidget('Dialog-Create Microstructure:name:Text').set_text('micr')
findWidget('Dialog-Create Microstructure:name:Text').set_text('micro')
findWidget('Dialog-Create Microstructure:name:Text').set_text('micro1')
findWidget('Dialog-Create Microstructure:width').set_text('')
findWidget('Dialog-Create Microstructure:width').set_text('5')
findWidget('Dialog-Create Microstructure:height').set_text('')
findWidget('Dialog-Create Microstructure:height').set_text('5')
findWidget('Dialog-Create Microstructure:width_in_pixels').set_text('')
findWidget('Dialog-Create Microstructure:width_in_pixels').set_text('1')
findWidget('Dialog-Create Microstructure:width_in_pixels').set_text('10')
findWidget('Dialog-Create Microstructure:width_in_pixels').set_text('100')
findWidget('Dialog-Create Microstructure:height_in_pixels').set_text('')
findWidget('Dialog-Create Microstructure:height_in_pixels').set_text('1')
findWidget('Dialog-Create Microstructure:height_in_pixels').set_text('10')
findWidget('Dialog-Create Microstructure:height_in_pixels').set_text('100')
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint Solver page sensitized
checkpoint skeleton selection page updated
# checkpoint interface page updated
checkpoint OOF.Microstructure.New
assert tests.sensitization1()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
findWidget('Dialog-Create new pixel group:name:Auto').clicked()
findWidget('Dialog-Create new pixel group:name:Text').set_text('a')
findWidget('Dialog-Create new pixel group:name:Text').set_text('ab')
findWidget('Dialog-Create new pixel group:name:Text').set_text('abc')
findWidget('Dialog-Create new pixel group:name:Text').set_text('abcd')
findWidget('Dialog-Create new pixel group:name:Text').set_text('abcde')
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.sensitization2()
assert tests.chooserCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', ['abcde (0 pixels, meshable)'])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', ['abcde (0 pixels, meshable)'])
assert tests.meshableButtonState() == 1
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
findWidget('Dialog-Create new pixel group:name:Text').set_text('')
findWidget('Dialog-Create new pixel group:name:Text').set_text('f')
findWidget('Dialog-Create new pixel group:name:Text').set_text('fg')
findWidget('Dialog-Create new pixel group:name:Text').set_text('fgh')
findWidget('Dialog-Create new pixel group:name:Text').set_text('fghi')
findWidget('Dialog-Create new pixel group:name:Text').set_text('fghij')
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.New
assert tests.sensitization2()
assert tests.chooserCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', ['abcde (0 pixels, meshable)', 'fghij (0 pixels, meshable)'])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', ['fghij (0 pixels, meshable)'])
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path((0,))
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', ['abcde (0 pixels, meshable)'])
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename pixelgroup abcde
findWidget('Dialog-Rename pixelgroup abcde').resize(194, 72)
findWidget('Dialog-Rename pixelgroup abcde:new_name').set_text('')
findWidget('Dialog-Rename pixelgroup abcde:new_name').set_text('k')
findWidget('Dialog-Rename pixelgroup abcde:new_name').set_text('kl')
checkpoint microstructure page sensitized
findWidget('Dialog-Rename pixelgroup abcde:new_name').set_text('klm')
findWidget('Dialog-Rename pixelgroup abcde:new_name').set_text('klmn')
findWidget('Dialog-Rename pixelgroup abcde:new_name').set_text('klmno')
findWidget('Dialog-Rename pixelgroup abcde:gtk-ok').clicked()
checkpoint meshable button set
# checkpoint interface page updated
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Rename
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.sensitization2()
assert tests.chooserCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', ['fghij (0 pixels, meshable)', 'klmno (0 pixels, meshable)'])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', ['klmno (0 pixels, meshable)'])
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Meshable').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Meshable
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', ['klmno (0 pixels)'])
assert tests.meshableButtonState() == 0
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-yes').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Delete
checkpoint microstructure page sensitized
assert tests.chooserCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', ['fghij (0 pixels, meshable)'])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', ['fghij (0 pixels, meshable)'])
assert tests.meshableButtonState() == 1
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Pixel Selection')
checkpoint page installed Pixel Selection
findWidget('OOF2:Pixel Selection Page:Pane').set_position(281)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint OOF.PixelSelection.Invert
checkpoint pixel page updated
findWidget('OOF2:Pixel Selection Page:Pane').set_position(281)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
checkpoint page installed Microstructure
assert tests.sensitization3()
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.AddSelection
assert tests.sensitization4()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Clear').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Clear
assert tests.sensitization3()
findWidget('OOF2:Microstructure Page:Save').clicked()
checkpoint toplevel widget mapped Dialog-Save Microstructure "micro1"
findWidget('Dialog-Save Microstructure "micro1"').resize(194, 100)
findWidget('Dialog-Save Microstructure "micro1":filename').set_text('m')
findWidget('Dialog-Save Microstructure "micro1":filename').set_text('mi')
findWidget('Dialog-Save Microstructure "micro1":filename').set_text('mic')
findWidget('Dialog-Save Microstructure "micro1":filename').set_text('micr')
findWidget('Dialog-Save Microstructure "micro1":filename').set_text('micro')
findWidget('Dialog-Save Microstructure "micro1":filename').set_text('micro.')
findWidget('Dialog-Save Microstructure "micro1":filename').set_text('micro.d')
findWidget('Dialog-Save Microstructure "micro1":filename').set_text('micro.da')
findWidget('Dialog-Save Microstructure "micro1":filename').set_text('micro.dat')
findWidget('Dialog-Save Microstructure "micro1":gtk-ok').clicked()
checkpoint OOF.File.Save.Microstructure
assert tests.filediff('micro.dat')
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-yes').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(150)
checkpoint pixel page updated
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint Solver page sensitized
checkpoint skeleton selection page updated
# checkpoint interface page updated
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint microstructure page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.Delete
assert tests.sensitization0()
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(194, 72)
findWidget('Dialog-Python_Log:filename').set_text('m')
findWidget('Dialog-Python_Log:filename').set_text('mi')
findWidget('Dialog-Python_Log:filename').set_text('mic')
findWidget('Dialog-Python_Log:filename').set_text('micr')
findWidget('Dialog-Python_Log:filename').set_text('micro')
findWidget('Dialog-Python_Log:filename').set_text('micro.')
findWidget('Dialog-Python_Log:filename').set_text('micro.l')
findWidget('Dialog-Python_Log:filename').set_text('micro.lo')
findWidget('Dialog-Python_Log:filename').set_text('micro.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
checkpoint_count("microstructure page sensitized")
assert tests.filediff('micro.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
