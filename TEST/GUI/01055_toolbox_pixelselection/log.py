checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.16 $
# $Author: langer $
# $Date: 2011/01/14 22:43:11 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests, os
findWidget('OOF2 Messages 1').resize(630, 200)
findWidget('OOF2').resize(550, 350)
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1:Pane0').set_position(280)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 1:Pane0').set_position(280)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
findWidget('OOF2 Graphics 1:Pane0').set_position(280)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(280)
findWidget('OOF2 Graphics 1').resize(800, 400)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
findWidget('OOF2:Microstructure Page:Pane').set_position(151)
findWidget('OOF2:Microstructure Page:NewFromFile').clicked()
checkpoint toplevel widget mapped Dialog-Load Image and create Microstructure
findWidget('Dialog-Load Image and create Microstructure').resize(346, 140)
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
findWidget('OOF2 Graphics 1:Pane0').set_position(280)
findWidget('OOF2:Microstructure Page:Pane').set_position(155)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint active area status updated
checkpoint pixel page updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0').set_position(280)
checkpoint OOF.Microstructure.Create_From_ImageFile
findWidget('OOF2:Microstructure Page:Pane').set_position(155)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(280)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), 'Pixel Selection')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(280)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(280)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 3.6500000000000e+01,y=-9.9911764705882e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 3.6500000000000e+01,y=-9.9911764705882e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findWidget('OOF2 Graphics 1:Pane0').set_position(280)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 5.9147058823529e+01,y=-6.8205882352941e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 5.9147058823529e+01,y=-6.8205882352941e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findWidget('OOF2 Graphics 1:Pane0').set_position(280)
# *Second* pixel selection, check texts.
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','1')
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'--','ydown':'--','xup':'59.1471','yup':'68.2059'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
findWidget('OOF2 Graphics 1').resize(800, 406)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(286)
findWidget('OOF2 Graphics 1').resize(800, 408)
findWidget('OOF2 Graphics 1').resize(800, 414)
findWidget('OOF2 Graphics 1').resize(800, 417)
findWidget('OOF2 Graphics 1').resize(800, 419)
findWidget('OOF2 Graphics 1').resize(800, 422)
findWidget('OOF2 Graphics 1').resize(800, 424)
findWidget('OOF2 Graphics 1').resize(800, 426)
findWidget('OOF2 Graphics 1').resize(800, 428)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(308)
findWidget('OOF2 Graphics 1').resize(800, 431)
findWidget('OOF2 Graphics 1').resize(800, 433)
findWidget('OOF2 Graphics 1').resize(800, 435)
findWidget('OOF2 Graphics 1').resize(800, 438)
findWidget('OOF2 Graphics 1').resize(800, 441)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(321)
findWidget('OOF2 Graphics 1').resize(800, 446)
findWidget('OOF2 Graphics 1').resize(800, 448)
findWidget('OOF2 Graphics 1').resize(800, 449)
findWidget('OOF2 Graphics 1').resize(800, 450)
findWidget('OOF2 Graphics 1').resize(800, 451)
findWidget('OOF2 Graphics 1').resize(800, 452)
findWidget('OOF2 Graphics 1').resize(800, 453)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(333)
findWidget('OOF2 Graphics 1').resize(800, 454)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(334)
findWidget('OOF2 Graphics 1').resize(800, 457)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(337)
findWidget('OOF2 Graphics 1').resize(800, 458)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(338)
findWidget('OOF2 Graphics 1').resize(800, 459)
findWidget('OOF2 Graphics 1').resize(800, 461)
findWidget('OOF2 Graphics 1').resize(800, 463)
findWidget('OOF2 Graphics 1').resize(800, 464)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(344)
findWidget('OOF2 Graphics 1').resize(800, 465)
findWidget('OOF2 Graphics 1').resize(800, 466)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(346)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(345)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(327)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(309)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(299)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(716)
findWidget('OOF2 Graphics 1:Pane0').set_position(294)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((13,))
checkpoint OOF.Graphics_1.Layer.Select
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'Layer:Delete').activate()
findWidget('OOF2 Graphics 1:Pane0').set_position(294)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.Graphics_1.Layer.Delete
# Test that the box was cleared appropriately.
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size','No source!')
assert tests.sensitizationCheck({'Undo':False,'Redo':False,'Clear':False,'Invert':False,'Prev':True,'Repeat':True,'Next':False}, 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
assert tests.gtkMultiTextCompare({'xdown':'--','ydown':'--','xup':'59.1471','yup':'68.2059'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection')
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(194, 71)
findWidget('Dialog-Python_Log:filename').set_text('p')
findWidget('Dialog-Python_Log:filename').set_text('pi')
findWidget('Dialog-Python_Log:filename').set_text('pix')
findWidget('Dialog-Python_Log:filename').set_text('pixe')
findWidget('Dialog-Python_Log:filename').set_text('pixel')
findWidget('Dialog-Python_Log:filename').set_text('pixels')
findWidget('Dialog-Python_Log:filename').set_text('pixelse')
findWidget('Dialog-Python_Log:filename').set_text('pixelsel')
findWidget('Dialog-Python_Log:filename').set_text('pixelselt')
findWidget('Dialog-Python_Log:filename').set_text('pixelseltb')
findWidget('Dialog-Python_Log:filename').set_text('pixelseltb.')
findWidget('Dialog-Python_Log:filename').set_text('pixelseltb.l')
findWidget('Dialog-Python_Log:filename').set_text('pixelseltb.lo')
findWidget('Dialog-Python_Log:filename').set_text('pixelseltb.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('pixelseltb.log')
os.remove('pixelseltb.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
