# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.8 $
# $Author: langer $
# $Date: 2010/12/27 07:24:51 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import tests

setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
findWidget('OOF2').resize(585, 350)
findWidget('OOF2:Microstructure Page:Pane').set_position(161)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(316, 163)
findWidget('Dialog-Create Microstructure:gtk-ok').clicked()
findWidget('OOF2:Microstructure Page:Pane').set_position(166)
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
findMenu(findWidget('OOF2:MenuBar'), 'Windows:Graphics:New').activate()
checkpoint Move Node toolbox info updated
findWidget('OOF2 Graphics 1:Pane0').set_position(285)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(691)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1').resize(800, 400)
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(714)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(258)
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1').resize(800, 400)
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Skeleton')
findWidget('OOF2:Skeleton Page:Pane').set_position(227)
findWidget('OOF2').resize(712, 424)
findWidget('OOF2:Skeleton Page:Pane').set_position(354)
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(397, 198)
findWidget('Dialog-New skeleton:gtk-ok').clicked()
findWidget('OOF2 Messages 1').resize(542, 200)
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
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
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint OOF.Skeleton.New
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:targets:Chooser'), 'All Elements')
findWidget('OOF2:Skeleton Page:Pane').set_position(379)
setComboBox(findWidget('OOF2:Skeleton Page:Pane:Modification:Method:Refine:degree:Chooser'), 'Bisection')
findWidget('OOF2:Skeleton Page:Pane:Modification:OK').clicked()
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
checkpoint OOF.Skeleton.Modify
findWidget('OOF2 Graphics 1').resize(800, 400)
findWidget('OOF2:Skeleton Page:Pane:Modification:Undo').clicked()
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint OOF.Skeleton.Undo
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), 'Skeleton Selection')
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.6235521235521e-01,y=-5.7007722007722e-01,button=1,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 1.6235521235521e-01,y=-5.7007722007722e-01,button=1,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Single_Element
findWidget('OOF2:Skeleton Page:Pane:Modification:Redo').clicked()
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint OOF.Skeleton.Redo
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 1.7934362934363e-01,y=-5.1911196911197e-01,button=1,state=1,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 1.7934362934363e-01,y=-5.1911196911197e-01,button=1,state=257,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Single_Element
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 2.2181467181467e-01,y=-7.0598455598456e-01,button=1,state=4,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 2.2181467181467e-01,y=-7.0598455598456e-01,button=1,state=260,window=findCanvasGdkWindow('Graphics_1')))
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Single_Element
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Undo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Undo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Undo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Redo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Redo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Redo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Redo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Redo').clicked()
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Redo
setComboBox(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), 'Skeleton Info')
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 4.7239382239382e-01,y=-7.2297297297297e-01,button=1,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.7239382239382e-01,y=-7.1872586872587e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 4.7239382239382e-01,y=-7.1872586872587e-01,button=1,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryElement
findWidget('OOF2:Skeleton Page:Pane:Modification:Undo').clicked()
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint OOF.Skeleton.Undo
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 4.5115830115830e-01,y=-5.7007722007722e-01,button=1,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 4.5115830115830e-01,y=-5.7007722007722e-01,button=1,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryElement
findWidget('OOF2:Skeleton Page:Pane:Modification:Redo').clicked()
checkpoint skeleton selection page grouplist
checkpoint skeleton selection page selection sensitized
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page updated
checkpoint selection info updated
checkpoint boundary page updated
checkpoint skeleton page sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint OOF.Skeleton.Redo
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 4.4266409266409e-01,y=-5.9131274131274e-01,button=1,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 4.5115830115830e-01,y=-5.9131274131274e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 4.5115830115830e-01,y=-5.9131274131274e-01,button=1,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryElement
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_PRESS,x= 5.5733590733591e-01,y=-4.6814671814672e-01,button=1,state=0,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.MOTION_NOTIFY,x= 5.5733590733591e-01,y=-4.6389961389961e-01,state=256,window=findCanvasGdkWindow('Graphics_1')))
canvasobj = findCanvasRoot(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas'), windowname='Graphics_1')
canvasobj.emit('event', event(gtk.gdk.BUTTON_RELEASE,x= 5.5733590733591e-01,y=-4.6389961389961e-01,button=1,state=256,window=findCanvasGdkWindow('Graphics_1')))
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryElement
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation:NodeList').get_selection().select_path((0,))
tree=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:ElementInformation:NodeList')
column = tree.get_column(0)
tree.row_activated((0,), column)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:Click:Node').clicked()
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryNodeByID
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:NodeInformation:ElementList').get_selection().select_path((0,))
tree=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:NodeInformation:ElementList')
column = tree.get_column(0)
tree.row_activated((0,), column)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:Click:Element').clicked()
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryElementByID
setComboBox(findWidget('OOF2:Navigation:PageMenu'), 'Microstructure')
findWidget('OOF2:Microstructure Page:Pane').set_position(203)
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(219, 93)
findWidget('Questioner:gtk-yes').clicked()
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
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
checkpoint Graphics_1 Element sensitized
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
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated
checkpoint selection info updated
checkpoint selection info updated
checkpoint Graphics_1 Element sensitized
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
findWidget('OOF2:Microstructure Page:Pane').set_position(197)
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint OOF.Microstructure.Delete
assert tests.objectInventory()
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(356, 93)
findWidget('Questioner:gtk-delete').clicked()
checkpoint OOF.Graphics_1.File.Close
