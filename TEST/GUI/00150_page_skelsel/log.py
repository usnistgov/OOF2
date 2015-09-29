checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.26 $
# $Author: langer $
# $Date: 2010/12/25 01:40:39 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton Selection')
checkpoint skeleton selection page grouplist
checkpoint page installed Skeleton Selection
checkpoint skeleton selection page selection sensitized
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(222)
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
assert tests.sensitization0()
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(150)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(314, 168)
findWidget('Dialog-Create Microstructure:width_in_pixels').set_text('100')
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('Dialog-Create Microstructure:height_in_pixels').set_text('100')
checkpoint meshable button set
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint pixel page updated
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
checkpoint skeleton selection page groups sensitized
checkpoint Solver page sensitized
# checkpoint interface page updated
checkpoint OOF.Microstructure.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton Selection')
checkpoint page installed Skeleton Selection
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(222)
assert tests.sensitization0()
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
checkpoint Move Node toolbox info updated
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
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
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'Layer:New').activate()
checkpoint layereditor layerset changed
checkpoint toplevel widget mapped OOF2 Graphics Layer Editor
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.New
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:category'), 'Microstructure')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:New').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Microstructure microstructure
findWidget('Dialog-New Display Method for Microstructure microstructure').resize(381, 320)
findWidget('Dialog-New Display Method for Microstructure microstructure:method:Material:no_material:Gray:Gray:slider').get_adjustment().set_value( 3.1746031746032e-02)
findWidget('Dialog-New Display Method for Microstructure microstructure:method:Material:no_material:Gray:Gray:slider').get_adjustment().set_value( 4.7619047619048e-02)
findWidget('Dialog-New Display Method for Microstructure microstructure:method:Material:no_material:Gray:Gray:slider').get_adjustment().set_value( 6.3492063492063e-02)
findWidget('Dialog-New Display Method for Microstructure microstructure:method:Material:no_material:Gray:Gray:slider').get_adjustment().set_value( 9.5238095238095e-02)
findWidget('Dialog-New Display Method for Microstructure microstructure:method:Material:no_material:Gray:Gray:slider').get_adjustment().set_value( 4.7619047619048e-01)
findWidget('Dialog-New Display Method for Microstructure microstructure:method:Material:no_material:Gray:Gray:slider').get_adjustment().set_value( 4.9206349206349e-01)
findWidget('Dialog-New Display Method for Microstructure microstructure:method:Material:no_material:Gray:Gray:slider').get_adjustment().set_value( 5.0793650793651e-01)
findWidget('Dialog-New Display Method for Microstructure microstructure:method:Material:no_material:Gray:Gray:slider').get_adjustment().set_value( 5.5555555555556e-01)
findWidget('Dialog-New Display Method for Microstructure microstructure:method:Material:no_material:Gray:Gray:slider').get_adjustment().set_value( 5.7142857142857e-01)
findWidget('Dialog-New Display Method for Microstructure microstructure:method:Material:no_material:Gray:Gray:slider').get_adjustment().set_value( 5.8730158730159e-01)
findWidget('Dialog-New Display Method for Microstructure microstructure:gtk-ok').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Add_Method
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findMenu(findWidget('OOF2 Graphics Layer Editor:MenuBar'), 'File:Close').activate()
checkpoint OOF.LayerEditor.File.Close
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), 'Pixel Selection')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Chooser'), 'Circle')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.6739130434783e-01,y=-7.8043478260870e-01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.6739130434783e-01,y=-7.7608695652174e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.7173913043478e-01,y=-7.6304347826087e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.7608695652174e-01,y=-7.6304347826087e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.9782608695652e-01,y=-7.4565217391304e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.1956521739130e-01,y=-7.3260869565217e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.4130434782609e-01,y=-7.1956521739130e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.6739130434783e-01,y=-6.9782608695652e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.8478260869565e-01,y=-6.7173913043478e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.0652173913043e-01,y=-6.6304347826087e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.1086956521739e-01,y=-6.5869565217391e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.1521739130435e-01,y=-6.5869565217391e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.1521739130435e-01,y=-6.5434782608696e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 3.1521739130435e-01,y=-6.5434782608696e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2').resize(684, 350)
findWidget('OOF2:Materials Page:Pane').set_position(272)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(249, 72)
findWidget('Dialog-New material:name:Auto').clicked()
findWidget('Dialog-New material:name:Text').set_text('stuff')
findWidget('Dialog-New material:gtk-ok').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material stuff to pixels
findWidget('Dialog-Assign material stuff to pixels').resize(268, 108)
findWidget('Dialog-Assign material stuff to pixels:gtk-ok').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Material.Assign
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2').resize(684, 434)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:Pane').set_position(340)
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
checkpoint skeleton page sensitized
findWidget('Dialog-New skeleton').resize(334, 152)
findWidget('Dialog-New skeleton:x_elements').set_text('')
findWidget('Dialog-New skeleton:x_elements').set_text('9')
findWidget('Dialog-New skeleton:y_elements').set_text('')
findWidget('Dialog-New skeleton:y_elements').set_text('9')
findWidget('Dialog-New skeleton:gtk-ok').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
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
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New
findWidget('OOF2:Skeleton Page:Pane').set_position(340)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton Selection')
checkpoint page installed Skeleton Selection
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.sensitization1()
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), 'Skeleton Selection')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:Chooser'), 'Circle')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 6.6304347826087e-01,y=-3.2826086956522e-01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6739130434783e-01,y=-3.2826086956522e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8043478260870e-01,y=-3.2391304347826e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.0217391304348e-01,y=-3.1956521739130e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.2391304347826e-01,y=-3.0652173913043e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.4565217391304e-01,y=-2.8913043478261e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.5869565217391e-01,y=-2.5869565217391e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7173913043478e-01,y=-2.4565217391304e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7608695652174e-01,y=-2.3695652173913e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.8478260869565e-01,y=-2.3260869565217e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.8913043478261e-01,y=-2.2826086956522e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.1086956521739e-01,y=-2.2391304347826e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.1956521739130e-01,y=-2.2391304347826e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.2391304347826e-01,y=-2.2391304347826e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.2826086956522e-01,y=-2.2391304347826e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.2826086956522e-01,y=-2.1956521739130e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3260869565217e-01,y=-2.1521739130435e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3695652173913e-01,y=-2.1521739130435e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4130434782609e-01,y=-2.1086956521739e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4130434782609e-01,y=-2.0652173913043e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 8.4130434782609e-01,y=-2.0652173913043e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Circle
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.sensitization2()
assert tests.selectionModeCheck('Elements')
assert tests.selectionSizeCheck(4)
assert tests.elementSelectionCheck([23, 24, 32, 33])
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new Element group
findWidget('Dialog-Create a new Element group').resize(249, 72)
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('Dialog-Create a new Element group:name:Auto').clicked()
findWidget('Dialog-Create a new Element group:name:Text').set_text('four')
findWidget('Dialog-Create a new Element group:gtk-ok').clicked()
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint OOF.ElementGroup.New_Group
assert tests.sensitization3()
assert tests.groupCheck(['four (0 elements)'])
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2:Skeleton Selection Page:Pane:Groups:Add').clicked()
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint OOF.ElementGroup.Add_to_Group
assert tests.sensitization4()
assert tests.groupCheck(['four (4 elements)'])
assert tests.selectionSizeCheck(4)
assert tests.elementSelectionCheck([23, 24, 32, 33])
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Undo
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.sensitization5()
assert tests.selectionSizeCheck(0)
assert tests.elementSelectionCheck([])
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Redo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page groups sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Redo
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.sensitization4()
assert tests.selectionSizeCheck(4)
assert tests.elementSelectionCheck([23, 24, 32, 33])
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(340)
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Chooser'), 'Selected Elements')
findWidget('OOF2:Skeleton Page:Pane').set_position(355)
checkpoint skeleton page sensitized
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:Chooser'), 'Bisection')
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:Bisection:rule_set'), 'liberal')
findWidget('OOF2:Skeleton Page:Pane:Modification:OK').clicked()
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
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Modify
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton Selection')
checkpoint page installed Skeleton Selection
assert tests.selectionSizeCheck(16)
assert tests.elementSelectionCheck([110, 111, 112, 113, 114, 115, 116, 117, 129, 130, 131, 132, 133, 134, 135, 136])
assert tests.sensitization4()
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Undo
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.elementSelectionCheck([])
assert tests.selectionSizeCheck(0)
assert tests.sensitization5()
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Redo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Redo
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.sensitization4()
assert tests.selectionSizeCheck(16)
assert tests.groupCheck(['four (16 elements)'])
assert tests.elementSelectionCheck([110, 111, 112, 113, 114, 115, 116, 117, 129, 130, 131, 132, 133, 134, 135, 136])
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(355)
findWidget('OOF2:Skeleton Page:Pane:Modification:Undo').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint skeleton page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Undo
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton Selection')
checkpoint page installed Skeleton Selection
assert tests.elementSelectionCheck([23, 24, 32, 33])
assert tests.groupCheck(['four (4 elements)'])
assert tests.selectionSizeCheck(4)
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Undo
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.sensitization5()
assert tests.selectionSizeCheck(0)
assert tests.elementSelectionCheck([])
assert tests.groupCheck(['four (4 elements)'])
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(355)
findWidget('OOF2:Skeleton Page:Pane:Modification:Redo').clicked()
checkpoint skeleton page sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page groups sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Redo
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton Selection')
checkpoint page installed Skeleton Selection
assert tests.selectionSizeCheck(0)
assert tests.groupCheck(['four (16 elements)'])
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Redo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Redo
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.groupCheck(['four (16 elements)'])
assert tests.selectionSizeCheck(16)
assert tests.sensitization4()
findWidget('OOF2 Graphics 1').resize(800, 400)
setComboBox(findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Chooser'), 'Select by Material')
setComboBox(findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Material:material'), 'stuff')
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_by_Material
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.elementSelectionCheck([155, 163, 164, 165, 172, 173, 174, 182])
assert tests.selectionSizeCheck(8)
assert tests.sensitization4()
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:Undo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Undo
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.selectionSizeCheck(16)
setComboBox(findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Chooser'), 'Select by Homogeneity')
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_by_Homogeneity
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.selectionSizeCheck(8)
assert tests.elementSelectionCheck([154, 155, 156, 166, 175, 181, 182, 183])
assert tests.sensitization6()
setComboBox(findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Chooser'), 'Select by Shape Energy')
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_by_Shape_Energy
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.elementSelectionCheck([])
assert tests.selectionSizeCheck(0)
assert tests.sensitization7()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), 'Skeleton Info')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 5.9347826086957e-01,y=-4.5869565217391e-01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 5.9347826086957e-01,y=-4.5869565217391e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryElement
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(260)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(281)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(329)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(329)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(340)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(341)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 7.1428571428571e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.4285714285714e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 2.1428571428571e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 2.8571428571429e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 3.5714285714286e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 4.2857142857143e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 5.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 5.7142857142857e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 6.4285714285714e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 7.1428571428571e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 7.8571428571429e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 9.2857142857143e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.0000000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.0714285714286e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.1428571428571e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.2142857142857e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.2857142857143e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.5000000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.6428571428571e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.7142857142857e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.7857142857143e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.8571428571429e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.9285714285714e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 2.0000000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 2.0714285714286e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 2.1428571428571e+02)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 7.8947368421053e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 7.8195488721805e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 7.6691729323308e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 7.5939849624060e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 7.2180451127820e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 6.7669172932331e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 5.1879699248120e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 4.8872180451128e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 4.7368421052632e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 4.6616541353383e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 4.2857142857143e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 4.1353383458647e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 3.9097744360902e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 3.8345864661654e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 3.6090225563910e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 3.4586466165414e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 3.3834586466165e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 3.3082706766917e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 3.1578947368421e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 3.0827067669173e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 3.0075187969925e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 2.9323308270677e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Select by Shape Energy:threshold:slider').get_adjustment().set_value( 2.8571428571429e-01)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_by_Shape_Energy
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.elementSelectionCheck([95, 97, 98, 100, 107, 109, 118, 120, 126, 128, 137, 139, 146, 148, 149, 151])
assert tests.selectionSizeCheck(16)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 2.2142857142857e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 2.2857142857143e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 2.3571428571429e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 2.4285714285714e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 2.5000000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:Clear').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation').get_vadjustment().set_value( 1.4200000000000e+02)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Chooser'), 'Select Illegal Elements')
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_Illegal_Elements
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.selectionSizeCheck(0)
assert tests.elementSelectionCheck([])
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(341)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), 'Skeleton Selection')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(341)
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Element').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Node').clicked()
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Node sensitized
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 4.5000000000000e-01,y=-4.4130434782609e-01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 4.5000000000000e-01,y=-4.4130434782609e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint Graphics_1 Node sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Single_Node
setComboBox(findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Chooser'), 'Select from Selected Nodes')
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_from_Selected_Nodes
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.elementSelectionCheck([125, 127, 128, 144, 145])
assert tests.selectionSizeCheck(5)
setComboBox(findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Chooser'), 'Select from Selected Segments')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Node').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated
checkpoint selection info updated
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 4.1521739130435e-01,y=-6.6304347826087e-01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 4.1521739130435e-01,y=-6.6304347826087e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 4.7173913043478e-01,y=-6.6304347826087e-01,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 4.7173913043478e-01,y=-6.6304347826087e-01,state=257,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 4.8913043478261e-01,y=-7.5869565217391e-01,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 4.8913043478261e-01,y=-7.5869565217391e-01,state=257,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_from_Selected_Segments
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.selectionSizeCheck(5)
assert tests.elementSelectionCheck([157, 158, 166, 167, 176])
setComboBox(findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Chooser'), 'Expand Element Selection')
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Expand_Element_Selection
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.selectionSizeCheck(20)
assert tests.elementSelectionCheck([143, 144, 145, 146, 147, 156, 157, 158, 159, 165, 166, 167, 168, 174, 175, 176, 177, 184, 185, 186])
setComboBox(findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Chooser'), 'Select Group')
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Select_Group
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.elementSelectionCheck([110, 111, 112, 113, 114, 115, 116, 117, 129, 130, 131, 132, 133, 134, 135, 136])
assert tests.selectionSizeCheck(16)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Element').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 6.7173913043478e-01,y=-3.1086956521739e-01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7608695652174e-01,y=-3.0217391304348e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8043478260870e-01,y=-2.8043478260870e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9347826086957e-01,y=-2.5000000000000e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.0217391304348e-01,y=-2.2826086956522e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.2391304347826e-01,y=-2.0217391304348e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.5434782608696e-01,y=-1.6739130434783e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.9782608695652e-01,y=-1.3260869565217e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3695652173913e-01,y=-1.0652173913043e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8478260869565e-01,y=-6.7391304347826e-02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.0652173913043e-01,y=-3.6956521739130e-02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.1956521739130e-01,y=-2.8260869565217e-02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4130434782609e-01,y=-6.5217391304346e-03,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.4565217391304e-01,y= 2.1739130434784e-03,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5434782608696e-01,y= 6.5217391304349e-03,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5869565217391e-01,y= 6.5217391304349e-03,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.6304347826087e-01,y= 1.0869565217391e-02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.7608695652174e-01,y= 1.0869565217391e-02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.8478260869565e-01,y= 1.5217391304348e-02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.9347826086957e-01,y= 1.9565217391304e-02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.9782608695652e-01,y= 1.9565217391304e-02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.0021739130435e+00,y= 1.9565217391304e-02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 1.0021739130435e+00,y= 1.9565217391304e-02,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Circle
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Chooser'), 'Unselect Group')
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Unselect_Group
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
assert tests.elementSelectionCheck([84, 85, 86, 87, 88, 89, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 105, 106, 107, 108, 109, 118, 119, 120, 121, 125, 126, 127, 128, 137, 138, 139, 140, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 158, 159, 160, 161])
assert tests.selectionSizeCheck(47)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Chooser'), 'Add Group')
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Add_Group
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementAction:Chooser'), 'Intersect Group')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 3.5000000000000e-01,y=-3.4565217391304e-01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.5434782608696e-01,y=-3.4565217391304e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.5869565217391e-01,y=-3.4565217391304e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.6304347826087e-01,y=-3.4130434782609e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.6739130434783e-01,y=-3.4130434782609e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.7173913043478e-01,y=-3.4130434782609e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.9347826086957e-01,y=-3.4130434782609e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.1521739130435e-01,y=-3.4130434782609e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.4130434782609e-01,y=-3.4130434782609e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6304347826087e-01,y=-3.4130434782609e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7608695652174e-01,y=-3.4130434782609e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.8913043478261e-01,y=-3.4130434782609e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.8913043478261e-01,y=-3.3695652173913e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9782608695652e-01,y=-3.3695652173913e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0217391304348e-01,y=-3.3695652173913e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0652173913043e-01,y=-3.3695652173913e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1086956521739e-01,y=-3.3695652173913e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1521739130435e-01,y=-3.3695652173913e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1956521739130e-01,y=-3.3695652173913e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2391304347826e-01,y=-3.3695652173913e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2826086956522e-01,y=-3.3695652173913e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3260869565217e-01,y=-3.3695652173913e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3695652173913e-01,y=-3.3260869565217e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4130434782609e-01,y=-3.3260869565217e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4565217391304e-01,y=-3.3260869565217e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5000000000000e-01,y=-3.3260869565217e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5000000000000e-01,y=-3.2826086956522e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5434782608696e-01,y=-3.2826086956522e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5869565217391e-01,y=-3.2826086956522e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.6304347826087e-01,y=-3.2826086956522e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.7608695652174e-01,y=-3.2391304347826e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.8043478260870e-01,y=-3.2391304347826e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.8913043478261e-01,y=-3.1956521739130e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.9347826086957e-01,y=-3.1956521739130e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.9782608695652e-01,y=-3.1956521739130e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.0217391304348e-01,y=-3.1956521739130e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.0652173913043e-01,y=-3.1956521739130e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.0652173913043e-01,y=-3.1521739130435e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1521739130435e-01,y=-3.1521739130435e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1956521739130e-01,y=-3.1521739130435e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2391304347826e-01,y=-3.1521739130435e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2826086956522e-01,y=-3.1521739130435e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2826086956522e-01,y=-3.1086956521739e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3260869565217e-01,y=-3.1086956521739e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3695652173913e-01,y=-3.1086956521739e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3695652173913e-01,y=-3.0652173913043e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4130434782609e-01,y=-3.0652173913043e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4565217391304e-01,y=-3.0652173913043e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.5000000000000e-01,y=-3.0652173913043e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.5434782608696e-01,y=-3.0652173913043e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.5869565217391e-01,y=-3.0217391304348e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6304347826087e-01,y=-3.0217391304348e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6739130434783e-01,y=-3.0217391304348e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7173913043478e-01,y=-3.0217391304348e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7173913043478e-01,y=-2.9782608695652e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7608695652174e-01,y=-2.9347826086957e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8043478260870e-01,y=-2.9347826086957e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8478260869565e-01,y=-2.9347826086957e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8913043478261e-01,y=-2.9347826086957e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 6.8913043478261e-01,y=-2.9347826086957e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Circle
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:ElementHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.ElementSelection.Intersect_Group
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(356)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Skeleton Selection Page:Mode:Element').clicked()
checkpoint skeleton selection page grouplist
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page groups sensitized
checkpoint skeleton selection page updated
findWidget('Dialog-Python_Log').resize(194, 72)
findWidget('Dialog-Python_Log:filename').set_text('skelselel.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('skelselel.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint OOF.Graphics_1.File.Close
