checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.18 $
# $Author: langer $
# $Date: 2011/01/14 22:43:00 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests
findWidget('OOF2:Navigation:Next').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(150)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(314, 168)
findWidget('Dialog-Create Microstructure:name:Auto').clicked()
findWidget('Dialog-Create Microstructure:name:Text').set_text('t')
findWidget('Dialog-Create Microstructure:name:Text').set_text('te')
findWidget('Dialog-Create Microstructure:name:Text').set_text('tes')
findWidget('Dialog-Create Microstructure:name:Text').set_text('test')
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
checkpoint meshable button set
checkpoint meshable button set
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint microstructure page sensitized
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
checkpoint skeleton selection page updated
# checkpoint interface page updated
checkpoint OOF.Microstructure.New
checkpoint_count("meshable button set")
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
findWidget('Dialog-Create new pixel group:name:Auto').clicked()
findWidget('Dialog-Create new pixel group:name:Text').set_text('a')
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint_count("meshable button set")
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename pixelgroup a
findWidget('Dialog-Rename pixelgroup a').resize(194, 72)
findWidget('Dialog-Rename pixelgroup a:gtk-cancel').clicked()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
findWidget('Dialog-Create new pixel group:name:Text').set_text('')
findWidget('Dialog-Create new pixel group:name:Text').set_text('b')
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.New
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
findWidget('Dialog-Create new pixel group:name:Auto').clicked()
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.New
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll').get_vadjustment().set_value( 2.3000000000000e+01)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.New
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Meshable').clicked()
findWidget('OOF2 Messages 1').resize(547, 200)
checkpoint meshable button set
checkpoint_count("meshable button set") # unthreaded fails here
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Meshable
checkpoint_count("meshable button set") # threaded fails here
assert tests.meshableButtonState() == 0
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path((2,))
checkpoint meshable button set
checkpoint_count("meshable button set")
assert tests.treeViewColValues('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList',0) == ['a (0 pixels, meshable)', 'b (0 pixels, meshable)', 'pixelgroup (0 pixels, meshable)', 'pixelgroup<2> (0 pixels)']
assert tests.meshableButtonState() == 1
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path((3,))
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
assert tests.meshableButtonState() == 0
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path((1,))
checkpoint meshable button set
assert tests.meshableButtonState() == 1
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Meshable').clicked()
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Meshable
assert tests.meshableButtonState() == 0
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path((3,))
assert tests.meshableButtonState() == 0
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path((1,))
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
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
assert tests.sensitization1()

# Check that the pixel group list has the right items, and that
# nothing is selected.
assert tests.treeViewColValues('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList',0) == ['a (0 pixels, meshable)', 'pixelgroup (0 pixels, meshable)', 'pixelgroup<2> (0 pixels)']
assert findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().get_selected()[1] is None

assert tests.meshableButtonState() == 0
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path((0,))
findWidget('OOF2:Navigation:Next').clicked()
findWidget('OOF2').resize(593, 350)
findWidget('OOF2:Image Page:Pane').set_position(380)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Pixel Selection')
findWidget('OOF2:Pixel Selection Page:Pane').set_position(324)
checkpoint microstructure page sensitized
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelSelection.Invert
checkpoint pixel page updated
findWidget('OOF2:Pixel Selection Page:Pane').set_position(324)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
assert tests.sensitization2()
assert tests.meshableButtonState() == 1
findWidget('OOF2:Microstructure Page:Pane').set_position(212)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path((1,))
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.AddSelection
assert tests.sensitization3()
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Remove').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.RemoveSelection
assert tests.sensitization2()
findWidget('OOF2:Microstructure Page:NewFromFile').clicked()
checkpoint toplevel widget mapped Dialog-Load Image and create Microstructure
findWidget('Dialog-Load Image and create Microstructure').resize(342, 144)
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
findWidget('Dialog-Load Image and create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(165)
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
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
checkpoint skeleton selection page updated
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
assert tests.sensitization4()
assert tests.chooserCheck('OOF2:Microstructure Page:Microstructure', ['test', 'small.ppm'])
assert tests.chooserStateCheck('OOF2:Microstructure Page:Microstructure', 'small.ppm')
assert tests.chooserCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', [])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', [])
setComboBox(findWidget('OOF2:Microstructure Page:Microstructure'), 'test')
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
assert tests.sensitization5()
assert tests.chooserCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', ['a (0 pixels, meshable)', 'pixelgroup (0 pixels, meshable)', 'pixelgroup<2> (0 pixels)'])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', [])
findWidget('OOF2:Microstructure Page:Pane').set_position(212)
setComboBox(findWidget('OOF2:Microstructure Page:Microstructure'), 'small.ppm')
findWidget('OOF2:Microstructure Page:Pane').set_position(165)
findWidget('OOF2:Microstructure Page:NewFromImage').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure from Image
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('Dialog-Create Microstructure from Image').resize(253, 180)
setComboBox(findWidget('Dialog-Create Microstructure from Image:image:Microstructure'), 'small.ppm')
findWidget('Dialog-Create Microstructure from Image:name:Auto').clicked()
findWidget('Dialog-Create Microstructure from Image:name:Text').set_text('2')
findWidget('Dialog-Create Microstructure from Image:name:Text').set_text('2s')
findWidget('Dialog-Create Microstructure from Image:name:Text').set_text('2sm')
findWidget('Dialog-Create Microstructure from Image:name:Text').set_text('2sma')
findWidget('Dialog-Create Microstructure from Image:name:Text').set_text('2smal')
findWidget('Dialog-Create Microstructure from Image:name:Text').set_text('2small')
findWidget('Dialog-Create Microstructure from Image:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(165)
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
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
checkpoint skeleton selection page updated
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_Image
assert tests.sensitization4()
assert tests.chooserCheck('OOF2:Microstructure Page:Microstructure', ['test', 'small.ppm', '2small'])
assert tests.chooserStateCheck('OOF2:Microstructure Page:Microstructure', '2small')
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-yes').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(165)
findWidget('OOF2:Microstructure Page:Pane').set_position(212)
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
checkpoint skeleton selection page updated
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Delete
assert tests.chooserCheck('OOF2:Microstructure Page:Microstructure', ['test', 'small.ppm'])
assert tests.chooserStateCheck('OOF2:Microstructure Page:Microstructure', 'test')
assert tests.sensitization4()
assert tests.chooserCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', ['a (0 pixels, meshable)', 'pixelgroup (0 pixels, meshable)', 'pixelgroup<2> (0 pixels)'])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', [])
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-yes').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(165)
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
checkpoint skeleton selection page updated
# checkpoint interface page updated
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Delete
assert tests.sensitization4()
assert tests.chooserCheck('OOF2:Microstructure Page:Microstructure', ['small.ppm'])
assert tests.chooserStateCheck('OOF2:Microstructure Page:Microstructure', 'small.ppm')
assert tests.chooserCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', [])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', [])
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-yes').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(165)
checkpoint microstructure page sensitized
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
checkpoint skeleton selection page updated
# checkpoint interface page updated
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Delete
assert tests.sensitization6()
assert tests.chooserCheck('OOF2:Microstructure Page:Microstructure', [])
assert tests.chooserCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', [])
assert tests.chooserListStateCheck('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList', [])
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(194, 72)
findWidget('Dialog-Python_Log:filename').set_text('m')
findWidget('Dialog-Python_Log:filename').set_text('mi')
findWidget('Dialog-Python_Log:filename').set_text('mic')
findWidget('Dialog-Python_Log:filename').set_text('micr')
findWidget('Dialog-Python_Log:filename').set_text('micro')
findWidget('Dialog-Python_Log:filename').set_text('micro2')
findWidget('Dialog-Python_Log:filename').set_text('micro2.')
findWidget('Dialog-Python_Log:filename').set_text('micro2.l')
findWidget('Dialog-Python_Log:filename').set_text('micro2.lo')
findWidget('Dialog-Python_Log:filename').set_text('micro2.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('micro2.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
