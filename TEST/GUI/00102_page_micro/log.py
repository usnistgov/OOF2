checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.26 $
# $Author: langer $
# $Date: 2011/01/14 22:43:01 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

findWidget('OOF2').resize(550, 350)
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
# check that nothing is sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
assert tests.sensitization0()
findWidget('OOF2:Microstructure Page:Pane').set_position(150)

# create a microstructure 'micro1' from an image file
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
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Auto').clicked()
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Text').set_text('m')
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Text').set_text('mi')
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Text').set_text('mic')
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Text').set_text('micr')
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Text').set_text('micro')
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Text').set_text('micro1')
findWidget('Dialog-Load Image and create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint microstructure page sensitized
checkpoint active area status updated
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
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized
checkpoint Solver page sensitized
# checkpoint interface page updated
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile

# check that the new group button is sensitized
assert tests.sensitization1()

# open a graphics window
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

# load a second image, creating microstructure micro2
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
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/t')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/tr')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/tri')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/tria')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/trian')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triang')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triangl')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triangle')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triangle.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triangle.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triangle.pn')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/triangle.png')
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Text').set_text('micro')
findWidget('Dialog-Load Image and create Microstructure:microstructure_name:Text').set_text('micro2')
findWidget('Dialog-Load Image and create Microstructure:gtk-ok').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
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
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Microstructure.Create_From_ImageFile
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)

# check that the microstructure page sensitization hasn't changed
assert tests.sensitization1()
# check that micro2 is selected
assert tests.microstructureCheck('micro2')

findWidget('OOF2:Microstructure Page:Pane').set_position(153)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)

# open the pixel selection toolbox
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), 'Pixel Selection')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
# choose the circle selector
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Chooser'), 'Circle')
# select pixels in micro1
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 3.2282608695652e+01,y=-1.0010869565217e+02,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.2282608695652e+01,y=-9.9456521739130e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.2934782608696e+01,y=-9.9456521739130e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.3586956521739e+01,y=-9.8804347826087e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.4891304347826e+01,y=-9.6847826086957e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.5543478260870e+01,y=-9.6195652173913e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.6195652173913e+01,y=-9.4239130434783e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.7500000000000e+01,y=-9.2934782608696e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.0108695652174e+01,y=-9.0978260869565e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.3369565217391e+01,y=-8.9021739130435e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.8586956521739e+01,y=-8.8369565217391e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1195652173913e+01,y=-8.7065217391304e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2500000000000e+01,y=-8.5760869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4456521739130e+01,y=-8.5760869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5760869565217e+01,y=-8.4456521739130e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5760869565217e+01,y=-8.3804347826087e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 5.5760869565217e+01,y=-8.3804347826087e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page sensitized
checkpoint pixel page updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
findWidget('OOF2 Graphics 1:Pane0').set_position(278)

# just selecting pixels doesn't change the sensitization, because no
# groups have been made (and micro2 is selected)
assert tests.sensitization1()

findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set

# A group has been created in micro2, but no pixels are selected
assert tests.sensitization2()
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (0 pixels, meshable)')

# switch to micro1
setComboBox(findWidget('OOF2:Microstructure Page:Microstructure'), 'micro1')
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
# check that sensitization is correct for a micro. with no groups
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
assert tests.sensitization1()
assert tests.meshableCheck(0)

# create groups in micro1
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set

assert tests.sensitization3()
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (0 pixels, meshable)')

# add pixels to the group
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.sensitization4()
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2564 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (2564 pixels, meshable)')

# select more pixels
findWidget('OOF2').resize(550, 350)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 7.0108695652174e+01,y=-6.4891304347826e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.0760869565217e+01,y=-6.4239130434783e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.1413043478261e+01,y=-6.3586956521739e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.2717391304348e+01,y=-6.2934782608696e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.4021739130435e+01,y=-6.0978260869565e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.5978260869565e+01,y=-6.0326086956522e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7934782608696e+01,y=-5.9673913043478e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.9239130434783e+01,y=-5.8369565217391e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.1847826086957e+01,y=-5.5760869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.2500000000000e+01,y=-5.5108695652174e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3152173913043e+01,y=-5.4456521739130e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3804347826087e+01,y=-5.3804347826087e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4456521739130e+01,y=-5.1847826086957e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5108695652174e+01,y=-5.1847826086957e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5760869565217e+01,y=-5.0543478260870e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.5760869565217e+01,y=-4.9891304347826e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6413043478261e+01,y=-4.9239130434783e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7065217391304e+01,y=-4.9239130434783e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7065217391304e+01,y=-4.8586956521739e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7065217391304e+01,y=-4.7934782608696e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7717391304348e+01,y=-4.7934782608696e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7717391304348e+01,y=-4.7282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8369565217391e+01,y=-4.7282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.8369565217391e+01,y=-4.6630434782609e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 8.8369565217391e+01,y=-4.6630434782609e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
findWidget('OOF2 Graphics 1:Pane0').set_position(278)

# create a new pixel group
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint OOF.PixelGroup.New
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2564 pixels, meshable)',                                  'pixelgroup<2> (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (0 pixels, meshable)')
assert tests.sensitization3()

findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2564 pixels, meshable)',                                  'pixelgroup<2> (2102 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (2102 pixels, meshable)')
assert tests.sensitization4()

# undo the pixel selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Undo
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2564 pixels, meshable)',                                  'pixelgroup<2> (2102 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (2102 pixels, meshable)')
assert tests.sensitization4()

# select the other group
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path((0,))
findWidget('OOF2').resize(550, 350)
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2564 pixels, meshable)',                                  'pixelgroup<2> (2102 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (2564 pixels, meshable)')
assert tests.sensitization4()

# go back to the first group
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path((1,))
checkpoint microstructure page sensitized
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2564 pixels, meshable)',                                  'pixelgroup<2> (2102 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (2102 pixels, meshable)')
assert tests.sensitization4()

# remove some pixels from a group
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Remove').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.RemoveSelection

assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2564 pixels, meshable)',                                  'pixelgroup<2> (2072 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (2072 pixels, meshable)')
assert tests.sensitization4()

# actually, we wanted to remove all the pixels from a group, so select
# the pixels in the group first.
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Image
findWidget('OOF2').resize(593, 350)
findWidget('OOF2:Image Page:Pane').set_position(380)
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Pixel Selection
findWidget('OOF2:Pixel Selection Page:Pane').set_position(324)
checkpoint pixel page updated
setComboBox(findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Chooser'), 'Select Group')
checkpoint pixel page sensitized
setComboBox(findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Select Group:group'), 'pixelgroup<2>')
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Image
findWidget('OOF2:Image Page:Pane').set_position(380)
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Microstructure

# now remove the pixels again
findWidget('OOF2:Microstructure Page:Pane').set_position(212)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Remove').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.RemoveSelection
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
# oops, we didn't click 'ok' when selecting the pixels! nothing's changed.
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2564 pixels, meshable)',                                  'pixelgroup<2> (2072 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (2072 pixels, meshable)')
assert tests.sensitization4()

# try again, clicking 'ok' this time
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Image
findWidget('OOF2:Image Page:Pane').set_position(380)
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Pixel Selection
findWidget('OOF2:Pixel Selection Page:Pane').set_position(324)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint selection info updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Select_Group
findWidget('OOF2:Pixel Selection Page:Pane').set_position(324)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Image
findWidget('OOF2:Image Page:Pane').set_position(380)
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(212)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Remove').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.RemoveSelection
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2564 pixels, meshable)',                                  'pixelgroup<2> (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (0 pixels, meshable)')
assert tests.sensitization3()

# draw the second layer in the graphics window
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'Layer:New').activate()
checkpoint layereditor layerset changed
checkpoint toplevel widget mapped OOF2 Graphics Layer Editor
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.New
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:category'), 'Image')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:object:Microstructure'), 'micro2')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:New').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Image triangle.png
findWidget('Dialog-New Display Method for Image triangle.png').resize(197, 80)
findWidget('Dialog-New Display Method for Image triangle.png:gtk-ok').clicked()
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
# checkpoint Move Node toolbox writable changed
# checkpoint Graphics_1 Move Nodes sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
widget_0=findWidget('OOF2 Graphics Layer Editor')
handled_0=widget_0.event(event(gtk.gdk.DELETE,window=widget_0.window))
postpone if not handled_0: widget_0.destroy()

# select pixels in micro2
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 4.5978260869565e+01,y=-5.0543478260870e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5978260869565e+01,y=-4.9891304347826e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6630434782609e+01,y=-4.9891304347826e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6630434782609e+01,y=-4.8586956521739e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7282608695652e+01,y=-4.7934782608696e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7282608695652e+01,y=-4.7282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7934782608696e+01,y=-4.6630434782609e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.8586956521739e+01,y=-4.4673913043478e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9239130434783e+01,y=-4.4021739130435e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0543478260870e+01,y=-4.3369565217391e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.0543478260870e+01,y=-4.2065217391304e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2500000000000e+01,y=-4.1413043478261e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2500000000000e+01,y=-4.0760869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3804347826087e+01,y=-4.0108695652174e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4456521739130e+01,y=-4.0108695652174e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4456521739130e+01,y=-3.9456521739130e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5108695652174e+01,y=-3.9456521739130e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5760869565217e+01,y=-3.8804347826087e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.6413043478261e+01,y=-3.8804347826087e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.6413043478261e+01,y=-3.8152173913043e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.7717391304348e+01,y=-3.7500000000000e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.8369565217391e+01,y=-3.6847826086957e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.9021739130435e+01,y=-3.6195652173913e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.9673913043478e+01,y=-3.6195652173913e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.0326086956522e+01,y=-3.6195652173913e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.0978260869565e+01,y=-3.5543478260870e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1630434782609e+01,y=-3.5543478260870e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1630434782609e+01,y=-3.4891304347826e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 6.1630434782609e+01,y=-3.4891304347826e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
findWidget('OOF2 Graphics 1:Pane0').set_position(278)

# switch to micro2 in the microstructure page
setComboBox(findWidget('OOF2:Microstructure Page:Microstructure'), 'micro2')
findWidget('OOF2:Microstructure Page:Pane').set_position(212)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (0 pixels, meshable)')
assert tests.sensitization3()

# add pixels
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (1540 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (1540 pixels, meshable)')
assert tests.sensitization4()

# select more pixels
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 6.1630434782609e+01,y=-2.1195652173913e+01,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.1630434782609e+01,y=-2.0543478260870e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2282608695652e+01,y=-2.0543478260870e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.2282608695652e+01,y=-1.9239130434783e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.3586956521739e+01,y=-1.8586956521739e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4239130434783e+01,y=-1.7934782608696e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.5543478260870e+01,y=-1.5978260869565e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6195652173913e+01,y=-1.5326086956522e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6847826086957e+01,y=-1.4673913043478e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7500000000000e+01,y=-1.4021739130435e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.7500000000000e+01,y=-1.3369565217391e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8152173913043e+01,y=-1.3369565217391e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8804347826087e+01,y=-1.2717391304348e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9456521739130e+01,y=-1.2717391304348e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.9456521739130e+01,y=-1.2065217391304e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.0108695652174e+01,y=-1.2065217391304e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.0760869565217e+01,y=-1.1413043478261e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.1413043478261e+01,y=-1.1413043478261e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.2065217391304e+01,y=-1.1413043478261e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.2717391304348e+01,y=-1.1413043478261e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.3369565217391e+01,y=-1.0760869565217e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.4021739130435e+01,y=-1.0760869565217e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.5978260869565e+01,y=-1.0108695652174e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.6630434782609e+01,y=-1.0108695652174e+01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7282608695652e+01,y=-9.4565217391304e+00,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7934782608696e+01,y=-9.4565217391304e+00,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.8586956521739e+01,y=-8.8043478260870e+00,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.9239130434783e+01,y=-8.8043478260870e+00,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.9239130434783e+01,y=-8.1521739130435e+00,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.9891304347826e+01,y=-8.1521739130435e+00,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.9891304347826e+01,y=-7.5000000000000e+00,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.0543478260870e+01,y=-6.8478260869565e+00,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 8.0543478260870e+01,y=-6.8478260869565e+00,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (1540 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (1540 pixels, meshable)')
assert tests.sensitization4()

# clear the pixel selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (1540 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup (1540 pixels, meshable)')
assert tests.sensitization5()

# select more pixels
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 3.2934782608696e+01,y=-2.4456521739130e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.3586956521739e+01,y=-2.4456521739130e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.4239130434783e+01,y=-2.3804347826087e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.4891304347826e+01,y=-2.3804347826087e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.5543478260870e+01,y=-2.3152173913043e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.6847826086957e+01,y=-2.2500000000000e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.7500000000000e+01,y=-2.1847826086957e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.8804347826087e+01,y=-2.1195652173913e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.0760869565217e+01,y=-2.0543478260870e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.1413043478261e+01,y=-1.9891304347826e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.2717391304348e+01,y=-1.8586956521739e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.3369565217391e+01,y=-1.7934782608696e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.3369565217391e+01,y=-1.7282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.4021739130435e+01,y=-1.6630434782609e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.4673913043478e+01,y=-1.6630434782609e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.4673913043478e+01,y=-1.5978260869565e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5326086956522e+01,y=-1.5326086956522e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5326086956522e+01,y=-1.4673913043478e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5978260869565e+01,y=-1.4021739130435e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6630434782609e+01,y=-1.4021739130435e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.6630434782609e+01,y=-1.3369565217391e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7282608695652e+01,y=-1.2717391304348e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7934782608696e+01,y=-1.2717391304348e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.8586956521739e+01,y=-1.2065217391304e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.8586956521739e+01,y=-1.1413043478261e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9891304347826e+01,y=-1.1413043478261e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9891304347826e+01,y=-1.0760869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1195652173913e+01,y=-1.0108695652174e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1847826086957e+01,y=-1.0108695652174e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.1847826086957e+01,y=-9.4565217391304e+00,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2500000000000e+01,y=-8.8043478260870e+00,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2500000000000e+01,y=-8.1521739130435e+00,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3152173913043e+01,y=-7.5000000000000e+00,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3152173913043e+01,y=-6.8478260869565e+00,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 5.3152173913043e+01,y=-6.8478260869565e+00,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
findWidget('OOF2 Graphics 1:Pane0').set_position(278)

# create a new pixel group in micro2
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized
checkpoint OOF.PixelGroup.New
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (1540 pixels, meshable)',                                  'pixelgroup<2> (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (0 pixels, meshable)')
assert tests.sensitization3()

findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (1540 pixels, meshable)',                                  'pixelgroup<2> (2228 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (2228 pixels, meshable)')
assert tests.sensitization4()

findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Meshable').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint contourmap info updated for Graphics_1
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.Meshable
assert tests.meshableCheck(0)
assert tests.pixelGroupListCheck('pixelgroup (1540 pixels, meshable)',                                  'pixelgroup<2> (2228 pixels)')
assert tests.selectedGroupCheck('pixelgroup<2> (2228 pixels)')
assert tests.sensitization4()

findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path((0,))
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (1540 pixels, meshable)',                                  'pixelgroup<2> (2228 pixels)')
assert tests.selectedGroupCheck('pixelgroup (1540 pixels, meshable)')
assert tests.sensitization4()

findWidget('OOF2:Microstructure Page:Pane:PixelGroups:GroupListScroll:GroupList').get_selection().select_path((1,))
checkpoint meshable button set
assert tests.pixelGroupListCheck('pixelgroup (1540 pixels, meshable)',                                  'pixelgroup<2> (2228 pixels)')
assert tests.selectedGroupCheck('pixelgroup<2> (2228 pixels)')
assert tests.meshableCheck(0)
assert tests.sensitization4()

setComboBox(findWidget('OOF2:Microstructure Page:Microstructure'), 'micro1')
checkpoint microstructure page sensitized
checkpoint meshable button set
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2564 pixels, meshable)',                                  'pixelgroup<2> (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (0 pixels, meshable)')
assert tests.sensitization3()

findWidget('OOF2:Microstructure Page:Pane').set_position(212)
setComboBox(findWidget('OOF2:Microstructure Page:Microstructure'), 'micro2')
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
assert tests.meshableCheck(0)
assert tests.pixelGroupListCheck('pixelgroup (1540 pixels, meshable)',                                  'pixelgroup<2> (2228 pixels)')
assert tests.selectedGroupCheck('pixelgroup<2> (2228 pixels)')
assert tests.sensitization4()

findWidget('OOF2:Microstructure Page:Pane').set_position(212)
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(194, 94)
findWidget('Questioner:gtk-yes').clicked()
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
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
# checkpoint Move Node toolbox writable changed
# checkpoint Graphics_1 Move Nodes sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
# checkpoint Move Node toolbox writable changed
# checkpoint Graphics_1 Move Nodes sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint contourmap info updated for Graphics_1
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
# checkpoint Move Node toolbox writable changed
# checkpoint Graphics_1 Move Nodes sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(212)
# checkpoint Move Node toolbox writable changed
# checkpoint Graphics_1 Move Nodes sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.Delete
findWidget('OOF2:Microstructure Page:Pane').set_position(212)
assert tests.meshableCheck(1)
assert tests.pixelGroupListCheck('pixelgroup (2564 pixels, meshable)',                                  'pixelgroup<2> (0 pixels, meshable)')
assert tests.selectedGroupCheck('pixelgroup<2> (0 pixels, meshable)')
assert tests.sensitization3()
assert tests.microstructureCheck('micro1')

findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(194, 72)
findWidget('Dialog-Python_Log:filename').set_text('m')
findWidget('Dialog-Python_Log:filename').set_text('me')
findWidget('Dialog-Python_Log:filename').set_text('mes')
findWidget('Dialog-Python_Log:filename').set_text('mesh')
findWidget('Dialog-Python_Log:filename').set_text('mesha')
findWidget('Dialog-Python_Log:filename').set_text('meshab')
findWidget('Dialog-Python_Log:filename').set_text('meshabl')
findWidget('Dialog-Python_Log:filename').set_text('meshable')
findWidget('Dialog-Python_Log:filename').set_text('meshable.')
findWidget('Dialog-Python_Log:filename').set_text('meshable.l')
findWidget('Dialog-Python_Log:filename').set_text('meshable.lo')
findWidget('Dialog-Python_Log:filename').set_text('meshable.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
checkpoint_count("meshable button set")
assert tests.filediff('meshable.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint OOF.Graphics_1.File.Close
