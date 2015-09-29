checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.14 $
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
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
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
checkpoint OOF.Microstructure.Create_From_ImageFile
assert tests.activeAreaCheck(0)
assert tests.pixelSelectionCheck(0)
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(250)
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
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
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Chooser'), 'Burn')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 3.0978260869565e+01,y=-4.6630434782609e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.0978260869565e+01,y=-4.7282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 3.0978260869565e+01,y=-4.7282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
findWidget('OOF2 Messages 1').resize(552, 200)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2:Navigation:Next').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
findWidget('Dialog-Create new pixel group:name:Auto').clicked()
findWidget('Dialog-Create new pixel group:name:Text').set_text('g')
findWidget('Dialog-Create new pixel group:name:Text').set_text('gr')
findWidget('Dialog-Create new pixel group:name:Text').set_text('gre')
findWidget('Dialog-Create new pixel group:name:Text').set_text('gree')
findWidget('Dialog-Create new pixel group:name:Text').set_text('green')
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.New
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.AddSelection
assert tests.pixelGroupSizeCheck('small.ppm', 'green', 4795)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 3.8152173913043e+01,y=-1.2423913043478e+02,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 3.8152173913043e+01,y=-1.2423913043478e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(249, 72)
findWidget('Dialog-Create new pixel group:name:Text').set_text('')
findWidget('Dialog-Create new pixel group:name:Text').set_text('w')
findWidget('Dialog-Create new pixel group:name:Text').set_text('wh')
findWidget('Dialog-Create new pixel group:name:Text').set_text('whi')
findWidget('Dialog-Create new pixel group:name:Text').set_text('whit')
findWidget('Dialog-Create new pixel group:name:Text').set_text('white')
findWidget('Dialog-Create new pixel group:gtk-ok').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.New
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.AddSelection
assert tests.pixelGroupSizeCheck('small.ppm', 'white', 4781)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Active Area')
findWidget('OOF2:Active Area Page:Pane').set_position(249)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Chooser'), 'Circle')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaPageSensitivityCheck0()
assert tests.activeAreaStatusCheck(22500, 22500)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 7.7934782608696e+01,y=-7.0760869565217e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.9239130434783e+01,y=-7.0760869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.0543478260870e+01,y=-6.9456521739130e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4456521739130e+01,y=-6.6847826086957e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7717391304348e+01,y=-6.4239130434783e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.0978260869565e+01,y=-6.0978260869565e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.6847826086957e+01,y=-5.7065217391304e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.0010869565217e+02,y=-5.5108695652174e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.0402173913043e+02,y=-5.3152173913043e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.0663043478261e+02,y=-5.1847826086957e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1054347826087e+02,y=-4.9891304347826e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1315217391304e+02,y=-4.8586956521739e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1380434782609e+02,y=-4.7934782608696e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1510869565217e+02,y=-4.7934782608696e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1576086956522e+02,y=-4.7282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1641304347826e+02,y=-4.7282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1706521739130e+02,y=-4.6630434782609e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1771739130435e+02,y=-4.6630434782609e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1902173913043e+02,y=-4.6630434782609e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1967391304348e+02,y=-4.6630434782609e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.2032608695652e+02,y=-4.5978260869565e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.2032608695652e+02,y=-4.5326086956522e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.2032608695652e+02,y=-4.5978260869565e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 1.2032608695652e+02,y=-4.5978260869565e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Activate Selection Only')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint active area status updated
checkpoint OOF.ActiveArea.Activate_Selection_Only
assert tests.pixelSelectionCheck(7572)
findWidget('OOF2:Active Area Page:Pane').set_position(249)
assert tests.activeAreaStatusCheck(7572, 22500)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaCheck(7572)
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2:Active Area Page:Pane:Store').clicked()
checkpoint toplevel widget mapped Dialog-Store the active area
findWidget('Dialog-Store the active area').resize(249, 72)
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('Dialog-Store the active area:name:Auto').clicked()
findWidget('Dialog-Store the active area:name:Text').set_text('c')
findWidget('Dialog-Store the active area:name:Text').set_text('ci')
findWidget('Dialog-Store the active area:name:Text').set_text('cir')
findWidget('Dialog-Store the active area:name:Text').set_text('circ')
findWidget('Dialog-Store the active area:name:Text').set_text('circl')
findWidget('Dialog-Store the active area:name:Text').set_text('circle')
findWidget('Dialog-Store the active area:gtk-ok').clicked()
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint OOF.ActiveArea.Store
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.activeAreaPageSensitivityCheck1()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.pixelSelectionCheck(0)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Chooser'), 'Burn')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 6.8152173913043e+01,y=-1.0336956521739e+02,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 6.8152173913043e+01,y=-1.0336956521739e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionCheck(2050)
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint active area status updated
assert tests.activeAreaStatusCheck(0, 22500, True)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.ActiveArea.Override
assert tests.activeAreaOverrideCheck(True)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.5102040816327e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 6.0408163265306e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.0571428571429e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 4.2285714285714e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 5.2857142857143e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 7.4000000000000e+01)
widget = findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat')
widget.event(event(gtk.gdk.BUTTON_RELEASE,x= 6.1000000000000e+01,y= 1.8000000000000e+01,state=256,window=widget.window))
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
assert tests.pixelSelectionCheck(4781)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint active area status updated
assert tests.activeAreaStatusCheck(7572, 22500)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.ActiveArea.Override
assert tests.activeAreaOverrideCheck(False)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.pixelSelectionCheck(2731)
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint active area status updated
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.ActiveArea.Override
assert tests.activeAreaOverrideCheck(True)
assert tests.activeAreaStatusCheck(0, 22500, True)
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.pixelSelectionCheck(0)
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint active area status updated
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.ActiveArea.Override
assert tests.activeAreaOverrideCheck(False)
assert tests.activeAreaStatusCheck(7572, 22500)
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Activate All')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint active area status updated
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.ActiveArea.Activate_All
assert tests.activeAreaStatusCheck(22500, 22500)
assert tests.activeAreaCheck(22500)
widget = findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat')
widget.event(event(gtk.gdk.BUTTON_RELEASE,x= 5.3000000000000e+01,y= 2.2000000000000e+01,state=256,window=widget.window))
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionCheck(4781)
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Activate Selection')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint active area status updated
checkpoint OOF.ActiveArea.Activate_Selection
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaCheck(22500)
assert tests.activeAreaStatusCheck(22500, 22500)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.pixelSelectionCheck(0)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 7.0979591836735e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 6.6448979591837e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 6.1918367346939e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.7755102040816e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.0204081632653e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 7.5510204081633e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 3.0204081632653e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.5102040816327e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 0.0000000000000e+00)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Chooser'), 'Circle')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 6.3586956521739e+01,y=-9.2934782608696e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4239130434783e+01,y=-9.2934782608696e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4239130434783e+01,y=-9.2282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.6195652173913e+01,y=-9.1630434782609e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.8152173913043e+01,y=-9.0978260869565e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.2065217391304e+01,y=-8.9021739130435e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.5326086956522e+01,y=-8.5760869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.1195652173913e+01,y=-8.1847826086957e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.9021739130435e+01,y=-7.5326086956522e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.5543478260870e+01,y=-6.8152173913043e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.9456521739130e+01,y=-6.4239130434783e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.0793478260870e+02,y=-5.9021739130435e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1184782608696e+02,y=-5.6413043478261e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1576086956522e+02,y=-5.3152173913043e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1771739130435e+02,y=-5.1195652173913e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1836956521739e+02,y=-4.9891304347826e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1902173913043e+02,y=-4.7282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1967391304348e+02,y=-4.7282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.2032608695652e+02,y=-4.7282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1967391304348e+02,y=-4.7282608695652e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1902173913043e+02,y=-4.9239130434783e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1706521739130e+02,y=-5.1195652173913e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1510869565217e+02,y=-5.2500000000000e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1445652173913e+02,y=-5.3152173913043e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1315217391304e+02,y=-5.3152173913043e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1250000000000e+02,y=-5.5108695652174e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1054347826087e+02,y=-5.5108695652174e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.1054347826087e+02,y=-5.5760869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.0793478260870e+02,y=-5.7717391304348e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.0728260869565e+02,y=-5.8369565217391e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.0663043478261e+02,y=-5.9673913043478e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.0597826086957e+02,y=-5.9673913043478e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 1.0597826086957e+02,y=-6.0326086956522e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 1.0597826086957e+02,y=-6.0326086956522e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionCheck(8985)
assert tests.activeAreaStatusCheck(22500, 22500)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint active area status updated
checkpoint OOF.ActiveArea.Activate_Selection
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaStatusCheck(22500, 22500)
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2:Active Area Page:Pane:Restore').clicked()
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint active area status updated
assert tests.activeAreaStatusCheck(7572, 22500)
findWidget('OOF2:Active Area Page:Pane:Restore').clicked()
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint active area status updated
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.ActiveArea.Restore
checkpoint OOF.ActiveArea.Restore
assert tests.activeAreaCheck(7572)
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint active area status updated
checkpoint OOF.ActiveArea.Activate_Selection
assert tests.activeAreaStatusCheck(10991, 22500)
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaCheck(10991)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.pixelSelectionCheck(0)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Chooser'), 'Burn')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 2.5760869565217e+01,y=-1.1836956521739e+02,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 2.5760869565217e+01,y=-1.1836956521739e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionCheck(3065)
assert tests.activeAreaCheck(10991)
assert tests.activeAreaStatusCheck(10991, 22500)
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Activate Pixel Group Only')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint active area status updated
checkpoint OOF.ActiveArea.Activate_Pixel_Group_Only
assert tests.activeAreaStatusCheck(4795, 22500)
assert tests.activeAreaCheck(4795)
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
checkpoint active area status updated
checkpoint OOF.ActiveArea.Override
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaOverrideCheck(True)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
assert tests.pixelSelectionCheck(0)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint active area status updated
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.ActiveArea.Override
assert tests.activeAreaOverrideCheck(False)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Chooser'), 'Circle')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 7.4021739130435e+01,y=-9.6195652173913e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.5978260869565e+01,y=-9.6195652173913e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 7.7934782608696e+01,y=-9.6195652173913e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3152173913043e+01,y=-9.6195652173913e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.3804347826087e+01,y=-9.5543478260870e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.9021739130435e+01,y=-9.2934782608696e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.3586956521739e+01,y=-9.0326086956522e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.6847826086957e+01,y=-8.8369565217391e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.7500000000000e+01,y=-8.7717391304348e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.8152173913043e+01,y=-8.7065217391304e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.8804347826087e+01,y=-8.6413043478261e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.8804347826087e+01,y=-8.5760869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.9456521739130e+01,y=-8.5760869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 9.9456521739130e+01,y=-8.5760869565217e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionCheck(1130)
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Activate Pixel Group')
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Activate Pixel Group:group'), 'white')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint active area status updated
checkpoint OOF.ActiveArea.Activate_Pixel_Group
assert tests.activeAreaStatusCheck(9576, 22500)
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaCheck(9576)
widget = findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat')
widget.event(event(gtk.gdk.BUTTON_RELEASE,x= 4.6000000000000e+01,y= 1.1000000000000e+01,state=256,window=widget.window))
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.pixelSelectionCheck(1824)
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Deactivate Selection')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint active area status updated
checkpoint OOF.ActiveArea.Deactivate_Selection
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaCheck(7752)
assert tests.activeAreaStatusCheck(7752, 22500)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.pixelSelectionCheck(1824)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Chooser'), 'Burn')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 8.7717391304348e+01,y=-6.9456521739130e+01,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 8.7717391304348e+01,y=-6.9456521739130e+01,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionCheck(3986)
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
checkpoint active area status updated
checkpoint OOF.ActiveArea.Override
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.pixelSelectionCheck(0)
findWidget('OOF2:Active Area Page:Pane:Modify:Override').clicked()
checkpoint active area status updated
checkpoint OOF.ActiveArea.Override
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Deactivate Group')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated
checkpoint active area status updated
checkpoint OOF.ActiveArea.Deactivate_Group
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaStatusCheck(4087, 22500)
assert tests.activeAreaCheck(4087)
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Chooser'), 'Circle')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 2.8369565217391e+01,y=-1.2489130434783e+02,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.8369565217391e+01,y=-1.2423913043478e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.9021739130435e+01,y=-1.2293478260870e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 2.9673913043478e+01,y=-1.2293478260870e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.0978260869565e+01,y=-1.2032608695652e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.0978260869565e+01,y=-1.1967391304348e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.1630434782609e+01,y=-1.1902173913043e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.2934782608696e+01,y=-1.1771739130435e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.3586956521739e+01,y=-1.1641304347826e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.4891304347826e+01,y=-1.1510869565217e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.4891304347826e+01,y=-1.1380434782609e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.6195652173913e+01,y=-1.1315217391304e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.6847826086957e+01,y=-1.1315217391304e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.8804347826087e+01,y=-1.1184782608696e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.8804347826087e+01,y=-1.1119565217391e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 3.9456521739130e+01,y=-1.1119565217391e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.0108695652174e+01,y=-1.1119565217391e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.0760869565217e+01,y=-1.1119565217391e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.1413043478261e+01,y=-1.1119565217391e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.1413043478261e+01,y=-1.1054347826087e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.2065217391304e+01,y=-1.0989130434783e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.3369565217391e+01,y=-1.0989130434783e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.4021739130435e+01,y=-1.0989130434783e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.4021739130435e+01,y=-1.0923913043478e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.4673913043478e+01,y=-1.0923913043478e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5326086956522e+01,y=-1.0923913043478e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5978260869565e+01,y=-1.0923913043478e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7934782608696e+01,y=-1.0728260869565e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.9891304347826e+01,y=-1.0663043478261e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.2500000000000e+01,y=-1.0402173913043e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3152173913043e+01,y=-1.0402173913043e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3152173913043e+01,y=-1.0336956521739e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3804347826087e+01,y=-1.0336956521739e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.4456521739130e+01,y=-1.0336956521739e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.3152173913043e+01,y=-1.0336956521739e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 5.3152173913043e+01,y=-1.0336956521739e+02,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.activeAreaCheck(4087)
assert tests.activeAreaStatusCheck(4087, 22500)
assert tests.pixelSelectionCheck(1019)
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Expand')
findWidget('OOF2:Active Area Page:Pane:Modify:Method:Expand:radius').set_text('.0')
findWidget('OOF2:Active Area Page:Pane:Modify:Method:Expand:radius').set_text('5.0')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint active area status updated
findWidget('OOF2:Active Area Page:Pane').set_position(249)
assert tests.activeAreaStatusCheck(8034, 22500)
checkpoint OOF.ActiveArea.Expand
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaCheck(8034)
widget = findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat')
widget.event(event(gtk.gdk.BUTTON_RELEASE,x= 4.6000000000000e+01,y= 1.0000000000000e+01,state=256,window=widget.window))
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionCheck(1900)
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Shrink')
findWidget('OOF2:Active Area Page:Pane:Modify:Method:Shrink:radius').set_text('')
findWidget('OOF2:Active Area Page:Pane:Modify:Method:Shrink:radius').set_text('1')
findWidget('OOF2:Active Area Page:Pane:Modify:Method:Shrink:radius').set_text('10')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Clear
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.pixelSelectionCheck(0)
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint active area status updated
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint OOF.ActiveArea.Shrink
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaCheck(429)
assert tests.activeAreaStatusCheck(429, 22500)
widget = findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat')
widget.event(event(gtk.gdk.BUTTON_RELEASE,x= 4.1000000000000e+01,y= 1.6000000000000e+01,state=256,window=widget.window))
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionCheck(141)
tree=findWidget('OOF2:Active Area Page:Pane:NamedAreasScroll:NamedAreas')
column = tree.get_column(0)
tree.row_activated((0,), column)
checkpoint active area status updated
checkpoint OOF.ActiveArea.Restore
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaStatusCheck(7572, 22500)
assert tests.activeAreaCheck(7572)
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Invert')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint active area status updated
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.ActiveArea.Invert
assert tests.activeAreaCheck(14928)
assert tests.activeAreaStatusCheck(14928, 22500)
widget = findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat')
widget.event(event(gtk.gdk.BUTTON_RELEASE,x= 5.6000000000000e+01,y= 8.0000000000000e+00,state=256,window=widget.window))
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
assert tests.pixelSelectionCheck(2858)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
findWidget('OOF2:Microstructure Page:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy microstructure
findWidget('Dialog-Copy microstructure').resize(249, 72)
findWidget('Dialog-Copy microstructure:name:Auto').clicked()
findWidget('Dialog-Copy microstructure:name:Text').set_text('c')
findWidget('Dialog-Copy microstructure:name:Text').set_text('co')
findWidget('Dialog-Copy microstructure:name:Text').set_text('cop')
findWidget('Dialog-Copy microstructure:name:Text').set_text('copy')
findWidget('Dialog-Copy microstructure:name:Text').set_text('cop')
findWidget('Dialog-Copy microstructure:name:Text').set_text('copi')
findWidget('Dialog-Copy microstructure:name:Text').set_text('copie')
findWidget('Dialog-Copy microstructure:name:Text').set_text('copied')
findWidget('Dialog-Copy microstructure:gtk-ok').clicked()
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findWidget('OOF2:Microstructure Page:Pane').set_position(153)
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
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
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint meshable button set
checkpoint OOF.Microstructure.Copy
checkpoint meshable button set
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Active Area')
findWidget('OOF2:Active Area Page:Pane').set_position(249)
setComboBox(findWidget('OOF2:Active Area Page:Microstructure'), 'copied')
checkpoint active area status updated
assert tests.activeAreaMSCheck('copied', 14928)
findWidget('OOF2:Active Area Page:Pane').set_position(249)
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Activate All')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint active area status updated
checkpoint OOF.ActiveArea.Activate_All
assert tests.activeAreaStatusCheck(22500, 22500)
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Copy')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint active area status updated
assert tests.activeAreaStatusCheck(14928, 22500)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
checkpoint OOF.ActiveArea.Copy
assert tests.activeAreaStatusCheck(14928, 22500)
assert tests.chooserCheck('OOF2:Active Area Page:Pane:NamedAreasScroll:NamedAreas', [])
setComboBox(findWidget('OOF2:Active Area Page:Microstructure'), 'small.ppm')
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint active area status updated
assert tests.activeAreaStatusCheck(14928, 22500)
assert tests.chooserCheck('OOF2:Active Area Page:Pane:NamedAreasScroll:NamedAreas', ['circle'])
setComboBox(findWidget('OOF2:Active Area Page:Pane:Modify:Method:Chooser'), 'Activate All')
findWidget('OOF2:Active Area Page:Pane:Modify:OK').clicked()
checkpoint active area status updated
checkpoint OOF.ActiveArea.Activate_All
assert tests.pixelSelectionCheck(2858)
findWidget('OOF2:Active Area Page:Pane').set_position(249)
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
assert tests.activeAreaStatusCheck(22500, 22500)
setComboBox(findWidget('OOF2:Active Area Page:Microstructure'), 'copied')
findWidget('OOF2:Active Area Page:Pane').set_position(249)
checkpoint active area status updated
assert tests.activeAreaStatusCheck(14928, 22500)
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 1.7333333333333e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.6000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path((13,))
checkpoint OOF.Graphics_1.Layer.Select
tree=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList')
column = tree.get_column(3)
tree.row_activated((13,), column)
checkpoint layereditor layerset changed
checkpoint toplevel widget mapped OOF2 Graphics Layer Editor
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Edit
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:object:Microstructure'), 'copied')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
findWidget('OOF2 Graphics Layer Editor:Send').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.LayerEditor.LayerSet.Send
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
widget = findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat')
widget.event(event(gtk.gdk.BUTTON_RELEASE,x= 5.0000000000000e+01,y= 2.2000000000000e+01,state=256,window=widget.window))
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Repeat').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Circle
findWidget('OOF2 Graphics 1:Pane0').set_position(278)
findMenu(findWidget('OOF2:MenuBar'), 'File:Save:Python_Log').activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(194, 72)
findWidget('Dialog-Python_Log:filename').set_text('a')
findWidget('Dialog-Python_Log:filename').set_text('aa')
findWidget('Dialog-Python_Log:filename').set_text('aa.')
findWidget('Dialog-Python_Log:filename').set_text('aa.l')
findWidget('Dialog-Python_Log:filename').set_text('aa.lo')
findWidget('Dialog-Python_Log:filename').set_text('aa.log')
findWidget('Dialog-Python_Log:gtk-ok').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('aa.log')
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
