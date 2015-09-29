checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.23 $
# $Author: langer $
# $Date: 2011/01/14 22:43:04 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2').resize(593, 434)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
assert tests.sensitization0()
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(162)
findWidget('OOF2:Microstructure Page:NewFromFile').clicked()
checkpoint toplevel widget mapped Dialog-Load Image and create Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
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
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Auto').clicked()
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Text').set_text('t')
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Text').set_text('te')
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Text').set_text('tes')
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Text').set_text('test')
findWidget('Dialog-Load Image and create Microstructure:width:Auto').clicked()
findWidget('Dialog-Load Image and create Microstructure:width:Text').set_text('1')
findWidget('Dialog-Load Image and create Microstructure:height:Auto').clicked()
findWidget('Dialog-Load Image and create Microstructure:height:Text').set_text('1')
findWidget('Dialog-Load Image and create Microstructure:height:Text').set_text('1.')
findWidget('Dialog-Load Image and create Microstructure:height:Text').set_text('1.5')
findWidget('Dialog-Load Image and create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(165)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint active area status updated
checkpoint pixel page updated
checkpoint microstructure page sensitized
checkpoint mesh bdy page updated
checkpoint pixel page sensitized
checkpoint meshable button set
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint microstructure page sensitized
# checkpoint interface page updated
checkpoint OOF.Microstructure.Create_From_ImageFile
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Image')
checkpoint page installed Image
findWidget('OOF2:Image Page:Pane').set_position(380)
findWidget('OOF2:Image Page:Group').clicked()
checkpoint toplevel widget mapped Dialog-AutoGroup
findWidget('Dialog-AutoGroup').resize(211, 72)
findWidget('Dialog-AutoGroup:gtk-ok').clicked()
findWidget('OOF2 Activity Viewer').resize(400, 300)
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.Image.AutoGroup
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
checkpoint Move Node toolbox info updated
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1').resize(800, 400)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
assert tests.sensitization1()
assert tests.chooserCheck('OOF2:Skeleton Page:Microstructure', ['test'])
assert tests.chooserCheck('OOF2:Skeleton Page:Skeleton', [])
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(334, 152)
findWidget('Dialog-New skeleton:y_elements').set_text('')
findWidget('Dialog-New skeleton:y_elements').set_text('6')
findWidget('Dialog-New skeleton:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(549, 200)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page sensitized
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist
checkpoint Solver page sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
assert tests.sensitization2()
assert tests.chooserCheck('OOF2:Skeleton Page:Microstructure', ['test'])
assert tests.chooserCheck('OOF2:Skeleton Page:Skeleton', ['skeleton'])
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:Chooser'), 'Bisection')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:Bisection:rule_set'), 'liberal')
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 9.0476190476190e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 9.2063492063492e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 9.3650793650794e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 9.5238095238095e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 9.6825396825397e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 9.8412698412698e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Heterogeneous Elements:threshold:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 3.0128205128205e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 3.3974358974359e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 3.8461538461538e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 4.2307692307692e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 4.4230769230769e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 4.9358974358974e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.3461538461538e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.4102564102564e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.5384615384615e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.6025641025641e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.7307692307692e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.7948717948718e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 6.9230769230769e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 7.1794871794872e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 7.3717948717949e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 7.4358974358974e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 7.5000000000000e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 7.5641025641026e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:alpha:slider').get_adjustment().set_value( 7.4358974358974e-01)
findWidget('OOF2:Skeleton Page:Pane:Modification:OK').clicked()
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint skeleton page sensitized
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
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Modify
assert tests.sensitization3()
findWidget('OOF2:Skeleton Page:Pane:Modification:Undo').clicked()
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
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
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Undo
assert tests.sensitization4()
findWidget('OOF2:Skeleton Page:Pane:Modification:Redo').clicked()
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Redo
assert tests.sensitization3()
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Chooser'), 'Snap Nodes')
findWidget('OOF2:Skeleton Page:Pane').set_position(273)
findWidget('OOF2:Skeleton Page:Pane:Modification:OK').clicked()
findWidget('OOF2:Skeleton Page:Pane').set_position(273)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
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
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Modify
assert tests.sensitization5()
findWidget('OOF2:Skeleton Page:Pane:Modification:Prev').clicked()
assert tests.sensitization8()
assert tests.chooserStateCheck('OOF2:Skeleton Page:Pane:Modification:Method:Chooser', 'Refine')
findWidget('OOF2:Skeleton Page:Pane').set_position(249)
findWidget('OOF2:Skeleton Page:Pane:Modification:Next').clicked()
assert tests.sensitization5()
assert tests.chooserStateCheck('OOF2:Skeleton Page:Pane:Modification:Method:Chooser', 'Snap Nodes')
findWidget('OOF2:Skeleton Page:Pane').set_position(273)
findWidget('OOF2:Skeleton Page:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename skeleton
findWidget('Dialog-Rename skeleton').resize(194, 72)
findWidget('Dialog-Rename skeleton:name').set_text('')
findWidget('Dialog-Rename skeleton:name').set_text('b')
findWidget('Dialog-Rename skeleton:name').set_text('bo')
findWidget('Dialog-Rename skeleton:name').set_text('bon')
findWidget('Dialog-Rename skeleton:name').set_text('bone')
findWidget('Dialog-Rename skeleton:name').set_text('bones')
findWidget('Dialog-Rename skeleton:gtk-ok').clicked()
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint OOF.Skeleton.Rename
assert tests.chooserCheck('OOF2:Skeleton Page:Skeleton', ['bones'])
findWidget('OOF2:Skeleton Page:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy skeleton
findWidget('Dialog-Copy skeleton').resize(249, 72)
findWidget('Dialog-Copy skeleton:gtk-ok').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint skeleton page info updated
checkpoint OOF.Skeleton.Copy
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
assert tests.chooserCheck('OOF2:Skeleton Page:Skeleton', ['bones', 'skeleton'])
assert tests.chooserStateCheck('OOF2:Skeleton Page:Skeleton', 'skeleton')
assert tests.sensitization6()
setComboBox(findWidget('OOF2:Skeleton Page:Skeleton'), 'bones')
findWidget('OOF2:Skeleton Page:Pane:Modification:Undo').clicked()
findWidget('OOF2:Skeleton Page:Pane').set_position(273)
checkpoint skeleton page info updated
checkpoint skeleton page info updated
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint skeleton page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Undo
assert tests.sensitization7()
setComboBox(findWidget('OOF2:Skeleton Page:Skeleton'), 'skeleton')
findWidget('OOF2:Skeleton Page:Pane').set_position(273)
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
checkpoint skeleton page info updated
checkpoint skeleton page info updated
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-ok').clicked()
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.Delete
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Page:Pane').set_position(273)
assert tests.sensitization7()
assert tests.chooserCheck('OOF2:Skeleton Page:Skeleton', ['bones'])
findWidget('OOF2:Skeleton Page:Save').clicked()
checkpoint toplevel widget mapped Dialog-Save Skeleton "test;bones"
findWidget('Dialog-Save Skeleton "test;bones"').resize(194, 100)
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('b')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bo')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bon')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bons')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bon')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bone')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bones')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bones.')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bones.s')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bones.sk')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bones.ske')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bones.sk')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bones.s')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bones.')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bones.d')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bones.da')
findWidget('Dialog-Save Skeleton "test;bones":filename').set_text('bones.dat')
findWidget('Dialog-Save Skeleton "test;bones":gtk-ok').clicked()
checkpoint OOF.File.Save.Skeleton
assert tests.filediff('bones.dat')
findWidget('OOF2:Skeleton Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-ok').clicked()
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint Solver page sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.Delete
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Page:Pane').set_position(273)
assert tests.sensitization9()
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(334, 152)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Page:Pane').set_position(273)
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
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New
assert tests.chooserCheck('OOF2:Skeleton Page:Skeleton', ['skeleton'])
assert tests.sensitization6()
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(212)
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-yes').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Microstructure Page:Pane').set_position(212)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint active area status updated
checkpoint pixel page updated
checkpoint mesh bdy page updated
checkpoint pixel page sensitized
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint Solver page sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint Solver page sensitized
# checkpoint interface page updated
checkpoint OOF.Microstructure.Delete
findWidget('OOF2:Microstructure Page:Pane').set_position(162)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
assert tests.chooserCheck('OOF2:Skeleton Page:Microstructure', [])
assert tests.chooserCheck('OOF2:Skeleton Page:Skeleton', [])
assert tests.sensitization10()
findWidget('OOF2:Skeleton Page:Pane').set_position(273)
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(358, 94)
findWidget('Questioner:gtk-cancel').clicked()
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(194, 72)
findWidget('Dialog-Python_Log:filename').set_text('s')
findWidget('Dialog-Python_Log:filename').set_text('sk')
findWidget('Dialog-Python_Log:filename').set_text('ske')
findWidget('Dialog-Python_Log:filename').set_text('skel')
findWidget('Dialog-Python_Log:filename').set_text('skel.')
findWidget('Dialog-Python_Log:filename').set_text('skel.l')
findWidget('Dialog-Python_Log:filename').set_text('skel.lo')
findWidget('Dialog-Python_Log:filename').set_text('skel.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('skel.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint OOF.Graphics_1.File.Close
