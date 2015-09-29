checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.20 $
# $Author: langer $
# $Date: 2011/01/14 22:43:13 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests, os
tbox="OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection"
elbox=tbox+":Element"
ndbox=tbox+":Node"
sgbox=tbox+":Segment"

findWidget('OOF2').resize(550, 350)
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
checkpoint Move Node toolbox info updated
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(706)
findWidget('OOF2 Graphics 1:Pane0').set_position(284)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(706)
findWidget('OOF2 Graphics 1:Pane0').set_position(284)
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(706)
findWidget('OOF2 Graphics 1:Pane0').set_position(284)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(284)
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2 Graphics 1').resize(800, 418)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(302)
findWidget('OOF2 Graphics 1').resize(800, 430)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(314)
findWidget('OOF2 Graphics 1').resize(800, 448)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(332)
findWidget('OOF2 Graphics 1').resize(800, 470)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(354)
findWidget('OOF2 Graphics 1').resize(800, 494)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(378)
findWidget('OOF2 Graphics 1').resize(800, 516)
findWidget('OOF2 Graphics 1').resize(800, 532)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(416)
findWidget('OOF2 Graphics 1').resize(800, 542)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(426)
findWidget('OOF2 Graphics 1').resize(800, 545)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(429)
findWidget('OOF2 Graphics 1').resize(800, 553)
findWidget('OOF2 Graphics 1').resize(800, 563)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(447)
findWidget('OOF2 Graphics 1').resize(800, 573)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(457)
findWidget('OOF2 Graphics 1').resize(800, 581)
findWidget('OOF2 Graphics 1').resize(800, 583)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(467)
findWidget('OOF2 Graphics 1').resize(800, 584)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(468)
findWidget('OOF2 Graphics 1').resize(800, 583)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(467)
findWidget('OOF2 Graphics 1').resize(800, 582)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(466)
findWidget('OOF2 Graphics 1').resize(800, 581)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(465)
findWidget('OOF2 Graphics 1').resize(800, 580)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(464)
findWidget('OOF2 Graphics 1').resize(800, 579)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(463)
findWidget('OOF2 Graphics 1').resize(800, 578)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(462)
findWidget('OOF2 Graphics 1').resize(800, 577)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(461)
findWidget('OOF2 Graphics 1').resize(800, 576)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(460)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(459)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(458)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(456)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(454)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(446)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(438)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(432)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(426)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(423)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(420)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(410)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(402)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(396)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(394)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(393)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(392)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(391)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(392)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(393)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), 'Skeleton Selection')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(256)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(723)
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Graphics window up and toolbox selected.  Check displays.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'', 'ydown':'', 'xup':'', 'yup':''}, elbox)
assert tests.sensitizationCheck({'Undo':False,'Redo':False,'Clear':False,'Invert':False},elbox)
assert tests.sensitizationCheck({'Prev':False,'Repeat':False,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","No Skeleton!")

findMenu(findWidget('OOF2:MenuBar'), 'File:Load:Data').activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(194, 69)
findWidget('Dialog-Data:filename').set_text('e')
findWidget('Dialog-Data:filename').set_text('ex')
findWidget('Dialog-Data:filename').set_text('exa')
findWidget('Dialog-Data:filename').set_text('exam')
findWidget('Dialog-Data:filename').set_text('examp')
findWidget('Dialog-Data:filename').set_text('exampl')
findWidget('Dialog-Data:filename').set_text('example')
findWidget('Dialog-Data:filename').set_text('examples')
findWidget('Dialog-Data:filename').set_text('examples/')
findWidget('Dialog-Data:filename').set_text('examples/t')
findWidget('Dialog-Data:filename').set_text('examples/tr')
findWidget('Dialog-Data:filename').set_text('examples/tri')
findWidget('Dialog-Data:filename').set_text('examples/tria')
findWidget('Dialog-Data:filename').set_text('examples/trian')
findWidget('Dialog-Data:filename').set_text('examples/triang')
findWidget('Dialog-Data:filename').set_text('examples/triangl')
findWidget('Dialog-Data:filename').set_text('examples/triangle')
findWidget('Dialog-Data:filename').set_text('examples/triangle.')
findWidget('Dialog-Data:filename').set_text('examples/triangle.s')
findWidget('Dialog-Data:filename').set_text('examples/triangle.sk')
findWidget('Dialog-Data:filename').set_text('examples/triangle.ske')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skel')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skele')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skelet')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skeleto')
findWidget('Dialog-Data:filename').set_text('examples/triangle.skeleton')
findWidget('Dialog-Data:gtk-ok').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint active area status updated
checkpoint pixel page updated
checkpoint mesh bdy page updated
checkpoint meshable button set
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
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint Solver page sensitized
# checkpoint interface page updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
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
checkpoint skeleton selection page selection sensitized
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Move Nodes sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
findWidget('OOF2 Activity Viewer').resize(400, 300)
checkpoint boundary page updated
checkpoint mesh bdy page updated
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint OOF.File.Load.Data

# Skeleton loaded up, recheck displays.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'', 'ydown':'', 'xup':'', 'yup':''}, elbox)
assert tests.sensitizationCheck({'Undo':False,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':False,'Repeat':False,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","0")

canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 2.5027027027027e+01,y=-6.0108108108108e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 2.5027027027027e+01,y=-6.0108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint selection info updated
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Single_Element
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Single element selection.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'25.027', 'yup':'60.1081'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':False,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","1")

setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:Chooser'), 'Rectangle')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.0162162162162e+01,y=-8.0621621621622e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.8648648648649e+00,y=-8.0621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.8648648648649e+00,y=-8.0324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.8648648648649e+00,y=-8.0027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.0459459459459e+01,y=-7.9729729729730e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.2837837837838e+01,y=-7.7945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.7594594594595e+01,y=-7.3189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.4729729729730e+01,y=-6.7243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.3054054054054e+01,y=-6.0702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.0783783783784e+01,y=-5.4756756756757e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7324324324324e+01,y=-5.0594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3270270270270e+01,y=-4.7621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.8621621621622e+01,y=-4.5243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4567567567568e+01,y=-4.2864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9918918918919e+01,y=-4.1675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.4081081081081e+01,y=-4.0486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7648648648649e+01,y=-4.0486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.0027027027027e+01,y=-4.0486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.1810810810811e+01,y=-3.9891891891892e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3594594594595e+01,y=-4.1081081081081e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5378378378378e+01,y=-3.8702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7162162162162e+01,y=-3.6918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8351351351351e+01,y=-3.5729729729730e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8351351351351e+01,y=-3.5135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8648648648649e+01,y=-3.5135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8648648648649e+01,y=-3.4837837837838e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8648648648649e+01,y=-3.4540540540541e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8648648648649e+01,y=-3.3945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8945945945946e+01,y=-3.3351351351351e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8945945945946e+01,y=-3.2459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.9243243243243e+01,y=-3.2162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.9243243243243e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8945945945946e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8648648648649e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8351351351351e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7756756756757e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7459459459459e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7162162162162e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6864864864865e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6567567567568e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6270270270270e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5972972972973e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5675675675676e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5378378378378e+01,y=-3.1270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5081081081081e+01,y=-3.1270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4783783783784e+01,y=-3.1270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4486486486486e+01,y=-3.1270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 8.4486486486486e+01,y=-3.1270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Rectangle
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Rectangle selection of elements.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'10.1622', 'ydown':'80.6216', 'xup':'84.4865', 'yup':'31.2703'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","15")

setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:Chooser'), 'Circle')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 2.7702702702703e+01,y=-7.7945945945946e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.0081081081081e+01,y=-7.7351351351351e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.1864864864865e+01,y=-7.6162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.4837837837838e+01,y=-7.4378378378378e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.7810810810811e+01,y=-7.2000000000000e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.0189189189189e+01,y=-7.0216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.1972972972973e+01,y=-6.8432432432432e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.3756756756757e+01,y=-6.6054054054054e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6135135135135e+01,y=-6.2486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9702702702703e+01,y=-5.7135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4459459459459e+01,y=-5.1189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.9216216216216e+01,y=-4.5837837837838e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2783783783784e+01,y=-4.1081081081081e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.5162162162162e+01,y=-3.6918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6351351351351e+01,y=-3.4540540540541e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6945945945946e+01,y=-3.2756756756757e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7243243243243e+01,y=-3.2459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7243243243243e+01,y=-3.2162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7540540540541e+01,y=-3.1864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7540540540541e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6351351351351e+01,y=-3.5135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6054054054054e+01,y=-3.5432432432432e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.5756756756757e+01,y=-3.6027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4567567567568e+01,y=-3.7216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3378378378378e+01,y=-3.8405405405405e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1594594594595e+01,y=-4.0189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.0405405405405e+01,y=-4.2567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.9216216216216e+01,y=-4.4945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.7432432432432e+01,y=-4.7324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.6243243243243e+01,y=-4.9702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5054054054054e+01,y=-5.1486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3864864864865e+01,y=-5.3270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3270270270270e+01,y=-5.5054054054054e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2972972972973e+01,y=-5.5351351351351e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2675675675676e+01,y=-5.5648648648649e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2675675675676e+01,y=-5.5945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2675675675676e+01,y=-5.6243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2675675675676e+01,y=-5.6540540540541e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2378378378378e+01,y=-5.7135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1783783783784e+01,y=-5.9513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0594594594595e+01,y=-6.0702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0594594594595e+01,y=-6.1297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0297297297297e+01,y=-6.1297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0000000000000e+01,y=-6.1297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0000000000000e+01,y=-6.1594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0297297297297e+01,y=-6.1594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0000000000000e+01,y=-6.1891891891892e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9702702702703e+01,y=-6.1891891891892e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9405405405405e+01,y=-6.2189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9108108108108e+01,y=-6.2189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9108108108108e+01,y=-6.2486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.8513513513514e+01,y=-6.2486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.8216216216216e+01,y=-6.2783783783784e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7918918918919e+01,y=-6.3081081081081e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7621621621622e+01,y=-6.3081081081081e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7621621621622e+01,y=-6.3378378378378e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7324324324324e+01,y=-6.3378378378378e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7027027027027e+01,y=-6.3378378378378e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6729729729730e+01,y=-6.3675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6432432432432e+01,y=-6.3972972972973e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6135135135135e+01,y=-6.3972972972973e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6135135135135e+01,y=-6.4270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5837837837838e+01,y=-6.4270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5837837837838e+01,y=-6.4567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5837837837838e+01,y=-6.4864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5243243243243e+01,y=-6.4864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.4945945945946e+01,y=-6.4864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 4.4945945945946e+01,y=-6.4864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page groups sensitized
checkpoint selection info updated
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Circle

# Circle selection of elements.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'27.7027', 'ydown':'77.9459', 'xup':'44.9459', 'yup':'64.8649'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","3")

setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:Chooser'), 'Ellipse')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 2.2648648648649e+01,y=-5.8027027027027e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.2648648648649e+01,y=-5.7729729729730e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.2648648648649e+01,y=-5.7432432432432e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.2945945945946e+01,y=-5.7135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.4729729729730e+01,y=-5.5945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.6513513513514e+01,y=-5.4162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.8297297297297e+01,y=-5.2378378378378e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.0081081081081e+01,y=-5.1189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.2459459459459e+01,y=-5.0000000000000e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.3648648648649e+01,y=-4.8810810810811e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.6027027027027e+01,y=-4.7621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.9594594594595e+01,y=-4.5837837837838e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.3756756756757e+01,y=-4.3459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7918918918919e+01,y=-4.1081081081081e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1486486486486e+01,y=-3.9297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3270270270270e+01,y=-3.8108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3864864864865e+01,y=-3.7810810810811e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4162162162162e+01,y=-3.7810810810811e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4162162162162e+01,y=-3.7513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4162162162162e+01,y=-3.7216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4459459459459e+01,y=-3.7216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5351351351351e+01,y=-3.7216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.8324324324324e+01,y=-3.6027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1891891891892e+01,y=-3.4837837837838e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7243243243243e+01,y=-3.2459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.3189189189189e+01,y=-3.0081081081081e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.8540540540541e+01,y=-2.7702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3891891891892e+01,y=-2.5324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8054054054054e+01,y=-2.3540540540541e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.2216216216216e+01,y=-2.1756756756757e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4594594594595e+01,y=-2.0567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.6378378378378e+01,y=-1.9972972972973e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.6972972972973e+01,y=-1.9675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.7270270270270e+01,y=-1.9675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.7270270270270e+01,y=-1.8783783783784e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.7270270270270e+01,y=-1.8486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.7567567567568e+01,y=-1.8189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.7567567567568e+01,y=-1.7891891891892e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.7567567567568e+01,y=-1.7594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.7567567567568e+01,y=-1.7000000000000e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.7567567567568e+01,y=-1.6702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.7567567567568e+01,y=-1.6405405405405e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.7270270270270e+01,y=-1.6108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.6675675675676e+01,y=-1.5810810810811e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.6378378378378e+01,y=-1.5810810810811e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5783783783784e+01,y=-1.5513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5486486486486e+01,y=-1.5513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5486486486486e+01,y=-1.5216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5189189189189e+01,y=-1.5216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4891891891892e+01,y=-1.5216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4891891891892e+01,y=-1.4918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4891891891892e+01,y=-1.4621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5189189189189e+01,y=-1.4324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5189189189189e+01,y=-1.4027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5189189189189e+01,y=-1.3432432432432e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5189189189189e+01,y=-1.3135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5189189189189e+01,y=-1.2837837837838e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5189189189189e+01,y=-1.2540540540541e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5783783783784e+01,y=-1.0756756756757e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5783783783784e+01,y=-1.0459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5783783783784e+01,y=-1.0162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5783783783784e+01,y=-9.8648648648649e+00,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5783783783784e+01,y=-9.5675675675676e+00,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 9.5783783783784e+01,y=-9.5675675675676e+00,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Ellipse
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Ellipse selection of elements.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'22.6486', 'ydown':'58.027', 'xup':'95.7838', 'yup':'9.56757'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","9")

setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:Chooser'), 'ByDominantPixel')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 4.4945945945946e+01,y=-6.9918918918919e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 4.4945945945946e+01,y=-6.9918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.ByDominantPixel
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Dominant pixel selection of elements.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'44.9459', 'yup':'69.9189'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","18")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Clear').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Clear

# Element selection cleared.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'44.9459', 'yup':'69.9189'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","0")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Node').clicked()
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Node sensitized

# Node mode selected.
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'', 'ydown':'', 'xup':'', 'yup':''}, ndbox)
assert tests.sensitizationCheck({'Undo':False,'Redo':False,'Clear':False,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':False,'Repeat':False,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","0")

canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.6108108108108e+01,y=-8.4783783783784e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 1.6108108108108e+01,y=-8.4783783783784e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Single node selection completed.
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'16.1081', 'yup':'84.7838'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':False,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","1")

setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:Chooser'), 'Rectangle')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.1648648648649e+01,y=-6.9621621621622e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 1.1648648648649e+01,y=-6.9621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Rectangle

# Trivial clutzy rectangle selection made -- probably not worth testing.

canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.0459459459459e+01,y=-6.9621621621622e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 1.0459459459459e+01,y=-6.9621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Rectangle

# What do you know, there were *two* ham-handed selections.

canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.0459459459459e+01,y=-6.9621621621622e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.2837837837838e+01,y=-6.7243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.5216216216216e+01,y=-6.5459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.8189189189189e+01,y=-6.3081081081081e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.1162162162162e+01,y=-6.0108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.4135135135135e+01,y=-5.7135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.7702702702703e+01,y=-5.4162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.3054054054054e+01,y=-5.1189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.9000000000000e+01,y=-4.7621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5540540540541e+01,y=-4.3459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2675675675676e+01,y=-3.8108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.0405405405405e+01,y=-3.3351351351351e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4567567567568e+01,y=-3.0378378378378e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8135135135135e+01,y=-2.8594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.1702702702703e+01,y=-2.8594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.5270270270270e+01,y=-2.8594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.5864864864865e+01,y=-2.6810810810811e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.6162162162162e+01,y=-2.6513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.6459459459459e+01,y=-2.5918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.6756756756757e+01,y=-2.5621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7054054054054e+01,y=-2.5324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7351351351351e+01,y=-2.5027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7648648648649e+01,y=-2.5027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.8243243243243e+01,y=-2.4729729729730e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.9432432432432e+01,y=-2.3540540540541e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.0027027027027e+01,y=-2.3243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.0324324324324e+01,y=-2.2945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.0621621621622e+01,y=-2.2648648648649e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.0918918918919e+01,y=-2.2054054054054e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.1216216216216e+01,y=-2.1459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.1513513513514e+01,y=-2.1162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.1810810810811e+01,y=-2.0864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.2108108108108e+01,y=-2.0864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.2702702702703e+01,y=-2.1162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3297297297297e+01,y=-2.1162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3891891891892e+01,y=-2.1459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5675675675676e+01,y=-2.2054054054054e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7459459459459e+01,y=-2.2648648648649e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8054054054054e+01,y=-2.2945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8351351351351e+01,y=-2.3243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8648648648649e+01,y=-2.3243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8351351351351e+01,y=-2.3243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8054054054054e+01,y=-2.3243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7756756756757e+01,y=-2.2945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7459459459459e+01,y=-2.2648648648649e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7459459459459e+01,y=-2.2351351351351e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7162162162162e+01,y=-2.2351351351351e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6864864864865e+01,y=-2.2351351351351e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6864864864865e+01,y=-2.2054054054054e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6567567567568e+01,y=-2.2054054054054e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6567567567568e+01,y=-2.1756756756757e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6270270270270e+01,y=-2.1459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5972972972973e+01,y=-2.1162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5972972972973e+01,y=-2.0864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6270270270270e+01,y=-2.0864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6567567567568e+01,y=-2.0864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6864864864865e+01,y=-2.0864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 8.6864864864865e+01,y=-2.0864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Rectangle
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Nontrivial rectangle selection completed.
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'10.4595', 'ydown':'69.6216', 'xup':'86.8649', 'yup':'20.8649'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","22")

setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:Chooser'), 'Circle')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 4.3756756756757e+01,y=-5.8621621621622e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5540540540541e+01,y=-5.7432432432432e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6135135135135e+01,y=-5.7432432432432e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6729729729730e+01,y=-5.7135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7324324324324e+01,y=-5.6837837837838e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9108108108108e+01,y=-5.6243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0891891891892e+01,y=-5.5054054054054e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1486486486486e+01,y=-5.4756756756757e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1783783783784e+01,y=-5.4459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1783783783784e+01,y=-5.4162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2081081081081e+01,y=-5.4162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2081081081081e+01,y=-5.3567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2378378378378e+01,y=-5.3270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2972972972973e+01,y=-5.1486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2972972972973e+01,y=-5.1189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2972972972973e+01,y=-5.0891891891892e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3270270270270e+01,y=-5.0891891891892e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3270270270270e+01,y=-5.0594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3567567567568e+01,y=-5.0297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3864864864865e+01,y=-5.0000000000000e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4162162162162e+01,y=-4.9702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4459459459459e+01,y=-4.9405405405405e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4756756756757e+01,y=-4.9108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5054054054054e+01,y=-4.8513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5351351351351e+01,y=-4.8216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5648648648649e+01,y=-4.7918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5945945945946e+01,y=-4.7621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.6540540540541e+01,y=-4.7324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.6837837837838e+01,y=-4.6729729729730e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.8027027027027e+01,y=-4.5540540540541e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.9216216216216e+01,y=-4.4351351351351e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.0405405405405e+01,y=-4.3162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1594594594595e+01,y=-4.1972972972973e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1891891891892e+01,y=-4.1675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2189189189189e+01,y=-4.1675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2486486486486e+01,y=-4.1675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2783783783784e+01,y=-4.1675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3081081081081e+01,y=-4.1675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3378378378378e+01,y=-4.1675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 6.3378378378378e+01,y=-4.1675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint Graphics_1 Node sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Circle

# Circle selection completed.
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'43.7568', 'ydown':'58.6216', 'xup':'63.3784', 'yup':'41.6757'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","11")

setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Method:Chooser'), 'Ellipse')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.0459459459459e+01,y=-8.2702702702703e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1054054054054e+01,y=-8.2702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.2837837837838e+01,y=-8.2108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.5216216216216e+01,y=-8.0918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.8189189189189e+01,y=-7.9729729729730e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.2351351351351e+01,y=-7.7945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.7108108108108e+01,y=-7.5567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.1864864864865e+01,y=-7.1405405405405e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.7810810810811e+01,y=-6.4864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.3756756756757e+01,y=-5.7729729729730e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9108108108108e+01,y=-5.2972972972973e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3270270270270e+01,y=-4.8810810810811e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.6243243243243e+01,y=-4.5243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.8621621621622e+01,y=-4.3459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1000000000000e+01,y=-4.1081081081081e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2189189189189e+01,y=-3.9297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2486486486486e+01,y=-3.8702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2783783783784e+01,y=-3.8108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3081081081081e+01,y=-3.8108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3378378378378e+01,y=-3.8108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4270270270270e+01,y=-3.8108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4567567567568e+01,y=-3.8108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4864864864865e+01,y=-3.8108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.5162162162162e+01,y=-3.8108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.5459459459459e+01,y=-3.8108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.5756756756757e+01,y=-3.8405405405405e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6054054054054e+01,y=-3.8702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6351351351351e+01,y=-3.8702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6648648648649e+01,y=-3.9000000000000e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6945945945946e+01,y=-3.9000000000000e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7243243243243e+01,y=-3.9297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7540540540541e+01,y=-3.9594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8135135135135e+01,y=-3.9891891891892e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8432432432432e+01,y=-4.0189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8729729729730e+01,y=-4.0486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9027027027027e+01,y=-4.0783783783784e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9621621621622e+01,y=-4.1081081081081e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.0216216216216e+01,y=-4.1378378378378e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.0513513513514e+01,y=-4.1675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.0810810810811e+01,y=-4.1972972972973e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.1108108108108e+01,y=-4.2270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.1405405405405e+01,y=-4.2567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.2000000000000e+01,y=-4.4351351351351e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.3189189189189e+01,y=-4.6729729729730e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.5567567567568e+01,y=-4.9108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.5864864864865e+01,y=-4.9108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.6162162162162e+01,y=-4.9108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.6459459459459e+01,y=-4.9108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7054054054054e+01,y=-4.9108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7351351351351e+01,y=-4.8810810810811e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7648648648649e+01,y=-4.8513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7945945945946e+01,y=-4.8216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.8243243243243e+01,y=-4.8216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.8540540540541e+01,y=-4.8216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.8837837837838e+01,y=-4.8216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.9135135135135e+01,y=-4.8216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.9432432432432e+01,y=-4.8216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.9729729729730e+01,y=-4.8216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.0027027027027e+01,y=-4.8216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.0324324324324e+01,y=-4.8216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.0621621621622e+01,y=-4.7918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.1216216216216e+01,y=-4.7621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.1513513513514e+01,y=-4.7324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.1810810810811e+01,y=-4.7324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.2108108108108e+01,y=-4.7027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.2702702702703e+01,y=-4.7027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3297297297297e+01,y=-4.7027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3891891891892e+01,y=-4.7027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4189189189189e+01,y=-4.7027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4783783783784e+01,y=-4.7027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5081081081081e+01,y=-4.7027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5378378378378e+01,y=-4.7027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5675675675676e+01,y=-4.7027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5972972972973e+01,y=-4.7324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6270270270270e+01,y=-4.7621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 8.6270270270270e+01,y=-4.7621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Ellipse
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Ellipse selection completed.
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'10.4595', 'ydown':'82.7027', 'xup':'86.2703', 'yup':'47.6216'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","11")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Node').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Node sensitized
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Clear').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Switched to segment mode, then back to node mode, cleared node selection.
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'10.4595', 'ydown':'82.7027', 'xup':'86.2703', 'yup':'47.6216'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","0")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint selection info updated
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated

# Segment mode, this time for real.
assert not findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'', 'ydown':'', 'xup':'', 'yup':''}, sgbox)
assert tests.sensitizationCheck({'Undo':False,'Redo':False,'Clear':False,'Invert':True},sgbox)
assert tests.sensitizationCheck({'Prev':False,'Repeat':False,'Next':False},sgbox)
assert tests.gtkTextCompare(sgbox+":size","0")

canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 2.1162162162162e+01,y=-7.2297297297297e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 2.1162162162162e+01,y=-7.2297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Single segment selection completed.
assert not findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'21.1622', 'yup':'72.2973'}, sgbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},sgbox)
assert tests.sensitizationCheck({'Prev':False,'Repeat':True,'Next':False},sgbox)
assert tests.gtkTextCompare(sgbox+":size","1")

setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Method:Chooser'), 'Rectangle')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 9.2702702702703e+00,y=-7.9432432432432e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1648648648649e+01,y=-7.9432432432432e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.5216216216216e+01,y=-7.8837837837838e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.8783783783784e+01,y=-7.7648648648649e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.2351351351351e+01,y=-7.5864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.6513513513514e+01,y=-7.4675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.0675675675676e+01,y=-7.2297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.4243243243243e+01,y=-6.9918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.8405405405405e+01,y=-6.6945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.2567567567568e+01,y=-6.2783783783784e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7918918918919e+01,y=-5.8027027027027e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4459459459459e+01,y=-5.2675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1594594594595e+01,y=-4.7324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9324324324324e+01,y=-4.1378378378378e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.5864864864865e+01,y=-3.6621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.0621621621622e+01,y=-3.3054054054054e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4189189189189e+01,y=-3.1864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4486486486486e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4783783783784e+01,y=-3.1270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5081081081081e+01,y=-3.1270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5675675675676e+01,y=-3.1270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5972972972973e+01,y=-3.1270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6567567567568e+01,y=-3.1270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6864864864865e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7162162162162e+01,y=-3.1864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7459459459459e+01,y=-3.1864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7756756756757e+01,y=-3.2162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7756756756757e+01,y=-3.2459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8054054054054e+01,y=-3.2459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8351351351351e+01,y=-3.2756756756757e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8648648648649e+01,y=-3.3054054054054e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8945945945946e+01,y=-3.3351351351351e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.9243243243243e+01,y=-3.3648648648649e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.9540540540541e+01,y=-3.3945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.9837837837838e+01,y=-3.3945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.9837837837838e+01,y=-3.4243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.0135135135135e+01,y=-3.4243243243243e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.0729729729730e+01,y=-3.4540540540541e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.1027027027027e+01,y=-3.4837837837838e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.1324324324324e+01,y=-3.5135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.1621621621622e+01,y=-3.5135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.1918918918919e+01,y=-3.5135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.1918918918919e+01,y=-3.5432432432432e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.3108108108108e+01,y=-3.6621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.3405405405405e+01,y=-3.6918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.3702702702703e+01,y=-3.7216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4000000000000e+01,y=-3.7810810810811e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4297297297297e+01,y=-3.8108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4297297297297e+01,y=-3.8405405405405e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4297297297297e+01,y=-3.8702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4297297297297e+01,y=-3.9000000000000e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4594594594595e+01,y=-3.9297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4891891891892e+01,y=-3.9891891891892e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5189189189189e+01,y=-3.9891891891892e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5189189189189e+01,y=-4.0189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5486486486486e+01,y=-4.0189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5783783783784e+01,y=-4.0189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.6081081081081e+01,y=-4.0486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.6378378378378e+01,y=-4.0486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 9.6378378378378e+01,y=-4.0486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Rectangle

# Rectangle segment selection completed.
assert not findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'9.27027', 'ydown':'79.4324', 'xup':'96.3784', 'yup':'40.4865'}, sgbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},sgbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},sgbox)
assert tests.gtkTextCompare(sgbox+":size","28")

setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Method:Chooser'), 'Circle')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 5.0891891891892e+01,y=-5.1486486486486e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0891891891892e+01,y=-5.0594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0891891891892e+01,y=-4.8216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2081081081081e+01,y=-4.5837837837838e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3270270270270e+01,y=-4.3459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4459459459459e+01,y=-4.2270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5648648648649e+01,y=-4.1081081081081e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.6837837837838e+01,y=-3.9297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.7432432432432e+01,y=-3.7513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.8621621621622e+01,y=-3.5729729729730e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.9810810810811e+01,y=-3.3351351351351e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.0405405405405e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1594594594595e+01,y=-3.0378378378378e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1594594594595e+01,y=-3.0081081081081e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1891891891892e+01,y=-2.9783783783784e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1891891891892e+01,y=-2.9486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1891891891892e+01,y=-2.9189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2189189189189e+01,y=-2.8891891891892e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2486486486486e+01,y=-2.8594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2783783783784e+01,y=-2.8297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3378378378378e+01,y=-2.8000000000000e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3675675675676e+01,y=-2.7702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3972972972973e+01,y=-2.7405405405405e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4270270270270e+01,y=-2.6810810810811e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4567567567568e+01,y=-2.6513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.5756756756757e+01,y=-2.4729729729730e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6054054054054e+01,y=-2.4135135135135e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6351351351351e+01,y=-2.3837837837838e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6351351351351e+01,y=-2.3540540540541e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6648648648649e+01,y=-2.3540540540541e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7837837837838e+01,y=-2.2351351351351e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8135135135135e+01,y=-2.2054054054054e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8432432432432e+01,y=-2.1756756756757e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8729729729730e+01,y=-2.1459459459459e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8729729729730e+01,y=-2.1162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9027027027027e+01,y=-2.0864864864865e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9027027027027e+01,y=-2.0567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9027027027027e+01,y=-2.0270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9027027027027e+01,y=-1.9972972972973e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9324324324324e+01,y=-1.9972972972973e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9621621621622e+01,y=-1.9972972972973e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9621621621622e+01,y=-1.9675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 6.9621621621622e+01,y=-1.9675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Circle

# Circle segment selection completed.
assert not findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'50.8919', 'ydown':'51.4865', 'xup':'69.6216', 'yup':'19.6757'}, sgbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},sgbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},sgbox)
assert tests.gtkTextCompare(sgbox+":size","37")

setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Method:Chooser'), 'Ellipse')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 2.2648648648649e+01,y=-6.4567567567568e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.3540540540541e+01,y=-6.4567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.4135135135135e+01,y=-6.4270270270270e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.5918918918919e+01,y=-6.3675675675676e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.8297297297297e+01,y=-6.3081081081081e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.0675675675676e+01,y=-6.2486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.3054054054054e+01,y=-6.1297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.5432432432432e+01,y=-5.9513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.7810810810811e+01,y=-5.7729729729730e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.9594594594595e+01,y=-5.5945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.1378378378378e+01,y=-5.4162162162162e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.3162162162162e+01,y=-5.2378378378378e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.4945945945946e+01,y=-5.1783783783784e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5243243243243e+01,y=-5.1486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5540540540541e+01,y=-5.1486486486486e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5837837837838e+01,y=-5.1189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6135135135135e+01,y=-5.0891891891892e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7918918918919e+01,y=-5.0297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9108108108108e+01,y=-4.9108108108108e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1486486486486e+01,y=-4.7324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3864864864865e+01,y=-4.4945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.6243243243243e+01,y=-4.1972972972973e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.8621621621622e+01,y=-3.9594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1000000000000e+01,y=-3.7810810810811e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2189189189189e+01,y=-3.6621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2486486486486e+01,y=-3.6324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2783783783784e+01,y=-3.6324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3675675675676e+01,y=-3.6324324324324e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.5459459459459e+01,y=-3.5729729729730e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8432432432432e+01,y=-3.3945945945946e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.3189189189189e+01,y=-3.1567567567568e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.5567567567568e+01,y=-3.0972972972973e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7351351351351e+01,y=-3.0378378378378e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.9135135135135e+01,y=-2.9783783783784e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.0918918918919e+01,y=-2.9189189189189e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.2702702702703e+01,y=-2.8594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3297297297297e+01,y=-2.8594594594595e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3891891891892e+01,y=-2.8297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4189189189189e+01,y=-2.8297297297297e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4783783783784e+01,y=-2.8000000000000e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5378378378378e+01,y=-2.7702702702703e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5972972972973e+01,y=-2.7405405405405e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7756756756757e+01,y=-2.6810810810811e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8351351351351e+01,y=-2.6513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8945945945946e+01,y=-2.6513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.9540540540541e+01,y=-2.6513513513514e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.0135135135135e+01,y=-2.6216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.0432432432432e+01,y=-2.6216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.0729729729730e+01,y=-2.6216216216216e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.1027027027027e+01,y=-2.5918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.1324324324324e+01,y=-2.5918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.1621621621622e+01,y=-2.5918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.1918918918919e+01,y=-2.5918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.2216216216216e+01,y=-2.5918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.2513513513514e+01,y=-2.5918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.2810810810811e+01,y=-2.5918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.3108108108108e+01,y=-2.5918918918919e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.3108108108108e+01,y=-2.5621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.3405405405405e+01,y=-2.5621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 9.3405405405405e+01,y=-2.5621621621622e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Ellipse
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Segment ellipse selection completed.
assert not findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'22.6486', 'ydown':'64.5676', 'xup':'93.4054', 'yup':'25.6216'}, sgbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},sgbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},sgbox)
assert tests.gtkTextCompare(sgbox+":size","14")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Clear').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Segment selection cleared.
assert not findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'22.6486', 'ydown':'64.5676', 'xup':'93.4054', 'yup':'25.6216'}, sgbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},sgbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},sgbox)
assert tests.gtkTextCompare(sgbox+":size","0")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Undo').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Undo
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Selection undone.
assert not findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'22.6486', 'ydown':'64.5676', 'xup':'93.4054', 'yup':'25.6216'}, sgbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},sgbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},sgbox)
assert tests.gtkTextCompare(sgbox+":size","14")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Undo').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Undo
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Undone again.
assert not findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'22.6486', 'ydown':'64.5676', 'xup':'93.4054', 'yup':'25.6216'}, sgbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},sgbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},sgbox)
assert tests.gtkTextCompare(sgbox+":size","37")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Redo').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Redo
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Redone.
assert not findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'22.6486', 'ydown':'64.5676', 'xup':'93.4054', 'yup':'25.6216'}, sgbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},sgbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},sgbox)
assert tests.gtkTextCompare(sgbox+":size","14")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Invert').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Invert
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Inverted.
assert not findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'22.6486', 'ydown':'64.5676', 'xup':'93.4054', 'yup':'25.6216'}, sgbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},sgbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},sgbox)
assert tests.gtkTextCompare(sgbox+":size","124")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Clear').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Cleared.
assert not findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'22.6486', 'ydown':'64.5676', 'xup':'93.4054', 'yup':'25.6216'}, sgbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},sgbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},sgbox)
assert tests.gtkTextCompare(sgbox+":size","0")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Node').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated

# Node mode...
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'10.4595', 'ydown':'82.7027', 'xup':'86.2703', 'yup':'47.6216'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","0")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Undo').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Undo
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Node selection undone.
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'10.4595', 'ydown':'82.7027', 'xup':'86.2703', 'yup':'47.6216'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","11")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Undo').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
checkpoint selection info updated
checkpoint Graphics_1 Node sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Undo

# Undone again.
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'10.4595', 'ydown':'82.7027', 'xup':'86.2703', 'yup':'47.6216'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","11")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Redo').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Redo
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Redone.
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'10.4595', 'ydown':'82.7027', 'xup':'86.2703', 'yup':'47.6216'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","11")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Invert').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Invert
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Inverted.
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'10.4595', 'ydown':'82.7027', 'xup':'86.2703', 'yup':'47.6216'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","64")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Clear').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Cleared.
assert not findWidget(tbox+":Select:Element").get_active()
assert findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'10.4595', 'ydown':'82.7027', 'xup':'86.2703', 'yup':'47.6216'}, ndbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},ndbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},ndbox)
assert tests.gtkTextCompare(ndbox+":size","0")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Element').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated

# Element mode.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'44.9459', 'yup':'69.9189'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","0")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Undo').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Undo

# Element selection undone.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'44.9459', 'yup':'69.9189'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","18")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Undo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Undo
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Undone again.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'44.9459', 'yup':'69.9189'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","9")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Redo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Redo
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Redone.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'44.9459', 'yup':'69.9189'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':True,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","18")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Invert').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Invert
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Inverted.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'44.9459', 'yup':'69.9189'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","46")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Clear').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Cleared.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'44.9459', 'yup':'69.9189'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","0")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Prev').clicked()

# History previous.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'22.6486', 'ydown':'58.027', 'xup':'95.7838', 'yup':'9.56757'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':True},elbox)
assert tests.gtkTextCompare(elbox+":size","0")


findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Prev').clicked()

# Histroy previous previous.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'27.7027', 'ydown':'77.9459', 'xup':'44.9459', 'yup':'64.8649'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':True},elbox)
assert tests.gtkTextCompare(elbox+":size","0")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Prev').clicked()

# History previous previous previous.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'10.1622', 'ydown':'80.6216', 'xup':'84.4865', 'yup':'31.2703'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':False,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':True},elbox)
assert tests.gtkTextCompare(elbox+":size","0")

widget_0 = findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Repeat')
widget_0.event(event(gtk.gdk.BUTTON_RELEASE,x= 5.3000000000000e+01,y= 8.0000000000000e+00,state=256,window=widget_0.window))
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Repeat').clicked()
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Rectangle
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Rectangle operatoin repeated from history gizmo.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'10.1622', 'ydown':'80.6216', 'xup':'84.4865', 'yup':'31.2703'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","15")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Prev').clicked()

# Previous again.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'44.9459', 'yup':'69.9189'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':True},elbox)
assert tests.gtkTextCompare(elbox+":size","15")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Prev').clicked()

# Previous some more.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'22.6486', 'ydown':'58.027', 'xup':'95.7838', 'yup':'9.56757'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':True},elbox)
assert tests.gtkTextCompare(elbox+":size","15")

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Next').clicked()

# Next!
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'44.9459', 'yup':'69.9189'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':True},elbox)
assert tests.gtkTextCompare(elbox+":size","15")

widget_1 = findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Repeat')
widget_1.event(event(gtk.gdk.BUTTON_RELEASE,x= 4.4000000000000e+01,y= 9.0000000000000e+00,state=256,window=widget_1.window))
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Repeat').clicked()
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.ByDominantPixel
findWidget('OOF2 Graphics 1:Pane0').set_position(395)

# Dominant pixel selection repeated.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'44.9459', 'yup':'69.9189'}, elbox)
assert tests.sensitizationCheck({'Undo':True,'Redo':False,'Clear':True,'Invert':True},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","18")

findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((10,))
checkpoint OOF.Graphics_1.Layer.Select
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'Layer:Delete').activate()
findWidget('OOF2 Graphics 1:Pane0').set_position(395)
checkpoint contourmap info updated for Graphics_1
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Delete

# Skeleton display layer removed.
assert findWidget(tbox+":Select:Element").get_active()
assert not findWidget(tbox+":Select:Node").get_active()
assert not findWidget(tbox+":Select:Segment").get_active()
assert tests.gtkMultiTextCompare({'xdown':'--', 'ydown':'--', 'xup':'44.9459', 'yup':'69.9189'}, elbox)
assert tests.sensitizationCheck({'Undo':False,'Redo':False,'Clear':False,'Invert':False},elbox)
assert tests.sensitizationCheck({'Prev':True,'Repeat':True,'Next':False},elbox)
assert tests.gtkTextCompare(elbox+":size","No Skeleton!")

findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(194, 69)
findWidget('Dialog-Python_Log:filename').set_text('s')
findWidget('Dialog-Python_Log:filename').set_text('sk')
findWidget('Dialog-Python_Log:filename').set_text('ske')
findWidget('Dialog-Python_Log:filename').set_text('skel')
findWidget('Dialog-Python_Log:filename').set_text('skels')
findWidget('Dialog-Python_Log:filename').set_text('skelse')
findWidget('Dialog-Python_Log:filename').set_text('skelsel')
findWidget('Dialog-Python_Log:filename').set_text('skelselt')
findWidget('Dialog-Python_Log:filename').set_text('skelselto')
findWidget('Dialog-Python_Log:filename').set_text('skelselt')
findWidget('Dialog-Python_Log:filename').set_text('skelseltb')
findWidget('Dialog-Python_Log:filename').set_text('skelseltbo')
findWidget('Dialog-Python_Log:filename').set_text('skelseltbox')
findWidget('Dialog-Python_Log:filename').set_text('skelseltbox.')
findWidget('Dialog-Python_Log:filename').set_text('skelseltbox.l')
findWidget('Dialog-Python_Log:filename').set_text('skelseltbox.lo')
findWidget('Dialog-Python_Log:filename').set_text('skelseltbox.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('skelseltbox.log')
os.remove('skelseltbox.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint OOF.Graphics_1.File.Close
