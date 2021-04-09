# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import tests
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials']).activate()
findMenu(findWidget('OOF2:MenuBar'), ['Help', 'Tutorials', 'Skeleton_Boundaries']).activate()
checkpoint toplevel widget mapped Skeleton Boundaries
findWidget('Skeleton Boundaries').resize(500, 300)
findWidget('OOF2').resize(782, 545)
findWidget('Skeleton Boundaries').resize(500, 300)
findWidget('Skeleton Boundaries:Next').clicked()
findWidget('Skeleton Boundaries:Next').clicked()
findWidget('Skeleton Boundaries:Next').clicked()
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
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
findWidget('Dialog-Data:filename').set_text('examples/tw')
findWidget('Dialog-Data:filename').set_text('examples/two')
findWidget('Dialog-Data:filename').set_text('examples/two_')
findWidget('Dialog-Data:filename').set_text('examples/two_c')
findWidget('Dialog-Data:filename').set_text('examples/two_ci')
findWidget('Dialog-Data:filename').set_text('examples/two_cir')
findWidget('Dialog-Data:filename').set_text('examples/two_circ')
findWidget('Dialog-Data:filename').set_text('examples/two_circl')
findWidget('Dialog-Data:filename').set_text('examples/two_circle')
findWidget('Dialog-Data:filename').set_text('examples/two_circles')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.s')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.sk')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.ske')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.skel')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.skele')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.skelet')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.skeleto')
findWidget('Dialog-Data:filename').set_text('examples/two_circles.skeleton')
findWidget('Dialog-Data:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint pixel page sensitized
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
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
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint OOF.File.Load.Data
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New Graphics Layer
findWidget('Dialog-New Graphics Layer').resize(395, 532)
event(Gdk.EventType.BUTTON_PRESS,x= 7.2000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Graphics Layer:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Image']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
findWidget('Dialog-New Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Layer', 'New']).activate()
checkpoint toplevel widget mapped Dialog-New Graphics Layer
findWidget('Dialog-New Graphics Layer').resize(215, 193)
event(Gdk.EventType.BUTTON_PRESS,x= 4.1000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Graphics Layer:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
findWidget('Dialog-New Graphics Layer').resize(359, 380)
findWidget('Dialog-New Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+01)
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2 Messages 1').resize(410, 130)
findWidget('Skeleton Boundaries:Next').clicked()
findWidget('Skeleton Boundaries:Next').clicked()
findWidget('Skeleton Boundaries').resize(500, 326)
event(Gdk.EventType.BUTTON_PRESS,x= 7.9000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(265)
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 1.1100000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['ByDominantPixel']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.4000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 66.625, 65.75, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 66.625, 65.75, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.ByDominantPixel
assert tests.skeletonElementSelectionCheck('two_circles.png:skeleton', [222, 223, 226, 227, 271, 272, 274, 275, 277, 278, 283, 284, 286, 287, 218, 219, 220, 221, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 301, 302, 307, 308, 309, 312, 327, 328, 331, 332, 354, 355, 356, 360, 361, 362, 372, 373, 374, 391, 392, 399, 407, 408, 409, 410, 411, 415, 433, 434, 441, 442, 443, 459, 460, 477, 478, 490, 491, 493, 498, 499, 500, 502, 503, 504, 514, 532, 533, 536, 537, 544, 545, 548, 549, 550, 554, 555, 562, 563, 583, 584, 593, 594, 595, 596, 597, 600, 601, 606, 607, 610, 611, 616, 618])
assert tests.skeletonSelectionTBSizeCheck('OOF2 Graphics 1', 'Element', 105)
event(Gdk.EventType.BUTTON_PRESS,x= 2.1000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', Gtk.TreePath(10))
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+01)
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Hide
event(Gdk.EventType.BUTTON_PRESS,x= 1.8000000000000e+01,y= 6.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', Gtk.TreePath(10))
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+01)
checkpoint Move Node toolbox writable changed
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Show
event(Gdk.EventType.BUTTON_PRESS,x= 2.3000000000000e+01,y= 3.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', Gtk.TreePath(14))
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([14]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Hide
findWidget('Skeleton Boundaries:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 8.9000000000000e+01,y= 2.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Boundaries']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton Boundaries
findWidget('OOF2:Skeleton Boundaries Page:Pane').set_position(379)
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(313, 194)
findWidget('Dialog-New Boundary:name').delete_text(0, 11)
findWidget('Dialog-New Boundary:name').insert_text('r', 11)
findWidget('Dialog-New Boundary:name').insert_text('e', 1)
findWidget('Dialog-New Boundary:name').insert_text('d', 2)
findWidget('Dialog-New Boundary:name').insert_text('_', 3)
findWidget('Dialog-New Boundary:name').insert_text('c', 4)
findWidget('Dialog-New Boundary:name').insert_text('i', 5)
findWidget('Dialog-New Boundary:name').insert_text('r', 6)
findWidget('Dialog-New Boundary:name').insert_text('c', 7)
findWidget('Dialog-New Boundary:name').insert_text('l', 8)
findWidget('Dialog-New Boundary:name').insert_text('e', 9)
event(Gdk.EventType.BUTTON_PRESS,x= 9.3000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary:constructor:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Edge boundary from elements']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Construct
assert tests.chooserListCheck('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList', ['top', 'right', 'bottom', 'left', 'red_circle', None, 'topleft', 'bottomleft', 'topright', 'bottomright'])
assert tests.chooserListStateCheck('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList', ['red_circle'])
findWidget('Skeleton Boundaries:Next').clicked()
findWidget('Skeleton Boundaries:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 1.7000000000000e+01,y= 3.8000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
findCellRenderer(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), col=0, rend=0).emit('toggled', Gtk.TreePath(14))
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Element sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Show
findWidget('Skeleton Boundaries:Next').clicked()
findGfxWindow('Graphics_1').simulateMouse('down', 22.525, 42.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 22.525, 41.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 22.525, 41.95, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint selection info updated Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.ByDominantPixel
assert tests.skeletonElementSelectionCheck('two_circles.png:skeleton', [252, 253, 159, 160, 164, 165, 167, 168, 169, 170, 171, 177, 178, 179, 180, 184, 185, 186, 187, 197, 363, 364, 365, 390, 416, 417, 426, 455, 456, 457, 458, 486, 488, 489, 492, 494, 501, 507, 509, 510, 511, 522, 523, 527, 528, 538, 539, 542, 543, 561, 564, 565, 566, 567, 570, 571, 572, 573, 579, 580, 585, 586, 612, 613, 614, 622])
assert tests.skeletonSelectionTBSizeCheck('OOF2 Graphics 1', 'Element', 66)
findWidget('Skeleton Boundaries:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 9.3000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint skeleton selection page grouplist Element
checkpoint page installed Skeleton Selection
findWidget('OOF2:Skeleton Selection Page:Pane').set_position(474)
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
findWidget('OOF2:Skeleton Selection Page:Mode:Node').clicked()
checkpoint skeleton selection page grouplist Node
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
event(Gdk.EventType.BUTTON_PRESS,x= 7.5000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeAction:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select from Selected Elements']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Skeleton Selection Page:Pane:Selection:NodeHistory:OK').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.NodeSelection.Select_from_Selected_Elements
assert tests.skeletonNodeSelectionCheck('two_circles.png:skeleton', [6, 42, 78, 81, 82, 204, 244, 335, 336, 337, 340, 346, 357, 358, 361, 369, 372, 375, 381, 384, 385, 392, 393, 408, 457, 461, 462, 467, 471, 472, 479])
findWidget('Skeleton Boundaries:Next').clicked()
event(Gdk.EventType.BUTTON_PRESS,x= 8.8000000000000e+01,y= 2.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton Boundaries']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton Boundaries
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(302, 194)
event(Gdk.EventType.BUTTON_PRESS,x= 1.1400000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary:constructor:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Point boundary from nodes']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Construct
assert tests.chooserListCheck('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList', ['top', 'right', 'bottom', 'left', 'red_circle', None, 'topleft', 'bottomleft', 'topright', 'bottomright', 'red_circle<2>'])
assert tests.chooserListStateCheck('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList', ['red_circle<2>'])
findWidget('Skeleton Boundaries:Next').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Node').clicked()
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Node:Clear').clicked()
checkpoint skeleton selection page selection sensitized Node
checkpoint skeleton selection page groups sensitized Node
checkpoint Graphics_1 Node sensitized
checkpoint selection info updated Node
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Node.Clear
findWidget('Skeleton Boundaries:Next').clicked()
findWidget('Skeleton Boundaries').resize(500, 338)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
event(Gdk.EventType.BUTTON_PRESS,x= 9.6000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', -4.775, 18.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', -4.425, 18.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', -4.075, 18.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', -3.025, 18.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', -0.575, 17.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.225, 16.4, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 6.075, 15.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.525, 15.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.975, 15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 13.075, 15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 15.175, 14.65, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 18.325, 13.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 20.775, 13.6, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 22.875, 13.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.025, 13.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 29.525, 13.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 33.025, 13.25, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 37.225, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.175, 12.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.175, 11.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.125, 11.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 62.425, 11.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 69.075, 10.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.825, 10.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.725, 10.45, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.625, 10.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 93.225, 10.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 97.775, 10.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 101.275, 10.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 104.075, 10.8, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 105.125, 11.15, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 106.525, 11.5, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 107.225, 11.85, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 107.925, 12.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 108.975, 12.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.025, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.025, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.375, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.725, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.725, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.725, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.725, 12.9, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.725, 12.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.725, 12.55, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.725, 12.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.725, 12.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 110.725, 12.2, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 110.725, 12.2, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Rectangle
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Segment:Clear').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Clear
assert tests.skeletonSegmentSelectionCheck('two_circles.png:skeleton', [])
assert tests.skeletonSelectionTBSizeCheck('OOF2 Graphics 1', 'Segment', 0)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'Fill_Window']).activate()
checkpoint OOF.Graphics_1.Settings.Zoom.Fill_Window
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'In']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 7.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 7.4000000000000e+01)
checkpoint OOF.Graphics_1.Settings.Zoom.In
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'Zoom', 'In']).activate()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.0200000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.8600000000000e+02)
checkpoint OOF.Graphics_1.Settings.Zoom.In
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.0153571428571e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.8916071428571e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.4319642857143e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.8285714285714e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.8477380952381e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 2.1148809523810e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 2.5155952380952e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.0944047619048e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.4951190476190e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.5173809523810e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.6064285714286e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.5841666666667e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.6064285714286e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.6954761904762e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 3.7400000000000e+02)
findGfxWindow('Graphics_1').simulateMouse('down', -1.2674959, 16.496925, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', -1.2674959, 16.496925, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', -1.1116676, 16.496925, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', -0.64418288, 16.341097, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.1349584, 16.02944, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.60244316, 15.873612, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.91409967, 15.561956, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 1.3815844, 15.561956, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 1.8490692, 15.250299, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.316554, 15.094471, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 2.939867, 14.782814, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 3.7190083, 14.626986, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 4.3423213, 14.31533, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 4.9656343, 14.159501, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 5.5889473, 14.003673, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 6.5239169, 13.847845, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 7.3030581, 13.692017, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 8.3938559, 13.38036, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 9.640482, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.263795, 12.757047, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 10.887108, 12.445391, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 11.354593, 12.289562, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 12.133734, 12.133734, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 13.068704, 11.977906, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 14.471158, 11.977906, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 15.561956, 11.977906, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 16.96441, 11.977906, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 18.366864, 12.133734, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 19.457662, 12.289562, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 20.392632, 12.289562, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 21.950914, 12.445391, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 23.820853, 12.445391, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 26.002449, 12.445391, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 28.495701, 12.445391, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 30.833125, 12.757047, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 33.170548, 12.757047, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 35.352144, 12.757047, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 36.910427, 12.757047, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 38.157053, 12.757047, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 39.24785, 12.757047, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 40.650305, 12.757047, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 41.741102, 12.757047, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 43.455213, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 44.857668, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 46.260122, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.039263, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 47.662576, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 48.285889, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 49.688343, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 50.623313, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 51.090798, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 51.869939, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 52.804909, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 54.519019, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.142332, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.453989, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 55.921474, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.544787, 12.912875, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 56.544787, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 57.012271, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 57.479756, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 57.635584, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 57.791413, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.103069, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.258898, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.570554, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 59.193867, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 59.505524, 13.224532, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 59.661352, 13.224532, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 59.973008, 13.224532, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.440493, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.440493, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.596321, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.596321, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.596321, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.75215, 13.068704, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 61.063806, 13.224532, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 61.531291, 13.224532, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 62.310432, 13.224532, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 63.089573, 13.224532, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 63.40123, 13.224532, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 63.40123, 13.224532, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 63.40123, 13.224532, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Rectangle
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.7738095238095e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.8380952380952e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 5.3214285714286e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 5.6761904761905e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 8.5142857142857e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.1884523809524e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.2239285714286e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.4900000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.5254761904762e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.6319047619048e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 1.8270238095238e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.0398809523810e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.1817857142857e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.3059523809524e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.3946428571429e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.4301190476190e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.4123809523810e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.4168154761905e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.4212500000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.4700297619048e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.5720238095238e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.6917559523810e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.7893154761905e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.8247916666667e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.8780059523810e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.8957440476190e+02)
findGfxWindow('Graphics_1').simulateMouse('down', 58.403039, 17.120238, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.403039, 17.120238, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.558867, 16.808582, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.714695, 16.341097, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.714695, 15.873612, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 58.870523, 15.561956, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 59.18218, 15.094471, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 59.493836, 14.782814, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 60.428806, 14.471158, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 61.207947, 14.159501, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 62.142917, 13.847845, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 63.389543, 13.692017, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 64.324512, 13.536188, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 66.506108, 12.912875, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 68.376047, 12.601219, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 69.93433, 12.445391, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 72.115925, 12.289562, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 73.362551, 12.289562, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 75.23249, 12.445391, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 77.102429, 12.445391, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 78.81654, 12.445391, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 80.374823, 12.445391, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 82.40059, 12.445391, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 84.114701, 12.445391, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.04967, 12.601219, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 85.828812, 12.757047, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 87.075438, 12.912875, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 88.789548, 13.224532, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 90.815316, 13.38036, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 92.996911, 13.38036, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 96.113476, 13.38036, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 98.762557, 13.38036, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 100.32084, 13.38036, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 101.41164, 13.38036, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 101.72329, 13.38036, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 101.87912, 13.38036, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 101.87912, 13.38036, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 101.87912, 13.224532, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 101.87912, 13.224532, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('move', 101.72329, 13.224532, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 101.72329, 13.224532, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Rectangle
assert tests.skeletonSegmentSelectionCheck('two_circles.png:skeleton', [[175, 182], [175, 191], [178, 183], [182, 183], [185, 190], [185, 199], [190, 191], [193, 198], [193, 224], [198, 199], [218, 223], [218, 232], [223, 224], [226, 231], [226, 240], [231, 232], [234, 239], [234, 266], [239, 240], [260, 265], [260, 274], [265, 266], [268, 273], [268, 282], [273, 274], [276, 281], [276, 308], [281, 282], [302, 307], [302, 316], [307, 308], [310, 315], [310, 324], [315, 316], [318, 323], [323, 324]])
assert tests.skeletonSelectionTBSizeCheck('OOF2 Graphics 1', 'Segment', 36)
findWidget('Skeleton Boundaries:Next').clicked()
findWidget('OOF2:Skeleton Boundaries Page:Pane:Boundaries:New').clicked()
checkpoint toplevel widget mapped Dialog-New Boundary
findWidget('Dialog-New Boundary').resize(286, 164)
findWidget('Dialog-New Boundary:name').delete_text(0, 10)
findWidget('Dialog-New Boundary:name').insert_text('w', 11)
findWidget('Dialog-New Boundary:name').insert_text('h', 1)
findWidget('Dialog-New Boundary:name').insert_text('i', 2)
findWidget('Dialog-New Boundary:name').insert_text('t', 3)
findWidget('Dialog-New Boundary:name').insert_text('e', 4)
findWidget('Dialog-New Boundary:name').insert_text('_', 5)
findWidget('Dialog-New Boundary:name').insert_text('c', 6)
findWidget('Dialog-New Boundary:name').insert_text('y', 7)
findWidget('Dialog-New Boundary:name').insert_text('a', 8)
findWidget('Dialog-New Boundary:name').insert_text('n', 9)
event(Gdk.EventType.BUTTON_PRESS,x= 9.4000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Boundary:constructor:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Edge boundary from segments']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-New Boundary').resize(306, 194)
findWidget('Dialog-New Boundary:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint boundary page updated
checkpoint boundary page updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.Boundary.Construct
assert tests.chooserListCheck('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList', ['top', 'right', 'bottom', 'left', 'red_circle', 'white_cyan', None, 'topleft', 'bottomleft', 'topright', 'bottomright', 'red_circle<2>'])
assert tests.chooserListStateCheck('OOF2:Skeleton Boundaries Page:Pane:Boundaries:BoundaryListScroll:BoundaryList', ['white_cyan'])
findWidget('Skeleton Boundaries:Next').clicked()
findWidget('Skeleton Boundaries:Next').clicked()
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Python_Log']).activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(192, 122)
findWidget('Dialog-Python_Log:filename').set_text('')
findWidget('Dialog-Python_Log:filename').set_text('s')
findWidget('Dialog-Python_Log:filename').set_text('se')
findWidget('Dialog-Python_Log:filename').set_text('ses')
findWidget('Dialog-Python_Log:filename').set_text('sess')
findWidget('Dialog-Python_Log:filename').set_text('sessi')
findWidget('Dialog-Python_Log:filename').set_text('sessio')
findWidget('Dialog-Python_Log:filename').set_text('session')
findWidget('Dialog-Python_Log:filename').set_text('session.')
findWidget('Dialog-Python_Log:filename').set_text('session.l')
findWidget('Dialog-Python_Log:filename').set_text('session.lo')
findWidget('Dialog-Python_Log:filename').set_text('session.log')
findWidget('Dialog-Python_Log').resize(194, 122)
findWidget('Dialog-Python_Log:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff('session.log')
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
