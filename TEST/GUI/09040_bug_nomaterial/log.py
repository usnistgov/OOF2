# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.10 $
# $Author: langer $
# $Date: 2010/12/25 01:40:43 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

## This tests for the absense of a bug that crashed the program when
## computing PropertyOutputs of Meshes that had elements with no
## assigned Material.

setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
findWidget('OOF2').resize(566, 350)
findWidget('OOF2:Microstructure Page:Pane').set_position(155)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(312, 163)
findWidget('Dialog-Create Microstructure:width_in_pixels').set_text('')
findWidget('Dialog-Create Microstructure:width_in_pixels').set_text('4')
findWidget('Dialog-Create Microstructure:height_in_pixels').set_text('')
findWidget('Dialog-Create Microstructure:height_in_pixels').set_text('4')
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(159)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
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
# checkpoint interface page updated
checkpoint OOF.Microstructure.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Materials')
findWidget('OOF2').resize(657, 350)
findWidget('OOF2:Materials Page:Pane').set_position(263)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(298, 98)
findWidget('Dialog-New material:gtk-ok').clicked()
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((0,))
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1,), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row((1, 0), open_all=False)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((1, 0, 0))
widget_0=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_0.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_0.window))
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint OOF.Material.Add_property
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
findWidget('OOF2 Graphics 1:Pane0').set_position(285)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(693)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1').resize(800, 400)
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(717)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(259)
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1').resize(800, 400)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), 'Layer:New').activate()
checkpoint layereditor layerset changed
checkpoint toplevel widget mapped OOF2 Graphics Layer Editor
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.New
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:category'), 'Microstructure')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:New').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Microstructure microstructure
findWidget('PopUp-Layer').deactivate()
findWidget('Dialog-New Display Method for Microstructure microstructure').resize(377, 313)
findWidget('Dialog-New Display Method for Microstructure microstructure:gtk-ok').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Add_Method
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), 'Pixel Selection')
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 2.0057915057915e-01,y=-8.0366795366795e-01,button=1,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 2.0057915057915e-01,y=-8.0366795366795e-01,button=1,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 3.6196911196911e-01,y=-7.9942084942085e-01,button=1,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 3.6196911196911e-01,y=-7.9942084942085e-01,button=1,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint selection info updated
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 6.3803088803089e-01,y=-8.1640926640927e-01,button=1,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 6.3803088803089e-01,y=-8.1640926640927e-01,button=1,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 8.4189189189189e-01,y=-7.9092664092664e-01,button=1,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.4613899613900e-01,y=-7.9092664092664e-01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 8.4613899613900e-01,y=-7.9092664092664e-01,button=1,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 8.6312741312741e-01,y=-6.7625482625483e-01,button=1,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6737451737452e-01,y=-6.7625482625483e-01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.6737451737452e-01,y=-6.7200772200772e-01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 8.7162162162162e-01,y=-6.7200772200772e-01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 8.7162162162162e-01,y=-6.7200772200772e-01,button=1,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 9.2683397683398e-01,y=-4.1718146718147e-01,button=1,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.2683397683398e-01,y=-4.1293436293436e-01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.2683397683398e-01,y=-4.0868725868726e-01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 9.2683397683398e-01,y=-4.0868725868726e-01,button=1,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 9.0984555984556e-01,y=-1.2413127413127e-01,button=1,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 9.1409266409266e-01,y=-1.1988416988417e-01,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 9.1409266409266e-01,y=-1.1988416988417e-01,button=1,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 6.5077220077220e-01,y=-9.0154440154440e-02,button=1,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 6.4227799227799e-01,y=-9.0154440154440e-02,state=257,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 6.4227799227799e-01,y=-9.0154440154440e-02,button=1,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 3.9169884169884e-01,y=-5.1930501930502e-02,button=1,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 3.9169884169884e-01,y=-5.1930501930502e-02,button=1,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.4536679536680e-01,y=-4.3436293436294e-02,button=1,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 1.4536679536680e-01,y=-4.3436293436294e-02,button=1,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.0289575289575e-01,y=-3.7046332046332e-01,button=1,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 1.0289575289575e-01,y=-3.7046332046332e-01,button=1,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 7.3166023166023e-02,y=-5.6583011583012e-01,button=1,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 7.3166023166023e-02,y=-5.6583011583012e-01,button=1,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Point
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_selection().select_path((0,))
widget_1=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
widget_1.event(event(gtk.gdk.BUTTON_RELEASE,button=1,window=widget_1.window))
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('PopUp-Layer').deactivate()
findWidget('Dialog-Assign material material to pixels').resize(258, 106)
findWidget('Dialog-Assign material material to pixels:gtk-ok').clicked()
checkpoint OOF.Material.Assign
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
findWidget('OOF2').resize(657, 424)
findWidget('OOF2:Skeleton Page:Pane').set_position(312)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('PopUp-Layer').deactivate()
findWidget('Dialog-New skeleton').resize(388, 198)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(473, 200)
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint OOF.Skeleton.New
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'FE Mesh')
findWidget('OOF2:FE Mesh Page:Pane').set_position(389)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('PopUp-Layer').deactivate()
findWidget('Dialog-Create a new mesh').resize(326, 210)
findWidget('Dialog-Create a new mesh:gtk-ok').clicked()
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint OOF.Mesh.New
findWidget('OOF2 Graphics Layer Editor:NewLayer').clicked()
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint layereditor layerset changed
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.New
setComboBox(findWidget('OOF2 Graphics Layer Editor:ObjectScroll:category'), 'Mesh')
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint OOF.LayerEditor.LayerSet.DisplayedObject
findWidget('OOF2 Graphics Layer Editor:DisplayMethods:New').clicked()
checkpoint toplevel widget mapped Dialog-New Display Method for Mesh mesh
findWidget('PopUp-Layer').deactivate()
findWidget('Dialog-New Display Method for Mesh mesh').resize(337, 227)
setComboBox(findWidget('Dialog-New Display Method for Mesh mesh:method:Chooser'), 'Filled Contour')
findWidget('Dialog-New Display Method for Mesh mesh').resize(382, 333)
setComboBox(findWidget('Dialog-New Display Method for Mesh mesh:method:Filled Contour:what:what_0'), 'Energy')
findWidget('Dialog-New Display Method for Mesh mesh:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(599, 200)
findWidget('OOF2 Graphics Layer Editor').resize(600, 250)
checkpoint layer editor updated
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint OOF.LayerEditor.LayerSet.Send
checkpoint layereditor layerset changed
checkpoint OOF.LayerEditor.LayerSet.Add_Method
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint toplevel widget mapped Questioner
findWidget('PopUp-Layer').deactivate()
findWidget('Questioner').resize(355, 93)
findWidget('Questioner:gtk-delete').clicked()
checkpoint OOF.Graphics_1.File.Close
