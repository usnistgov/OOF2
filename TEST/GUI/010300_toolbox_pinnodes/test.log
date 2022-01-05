# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests
tbox = 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pin Nodes'

checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)

findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
findWidget('OOF2').resize(782, 545)
wevent(findWidget('Dialog-New_Layer_Policy:policy'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Settings.Graphics_Defaults.New_Layer_Policy
findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Graphics', 'New']).activate()
checkpoint Move Node toolbox info updated
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint toplevel widget mapped OOF2 Graphics 1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
findWidget('OOF2 Graphics 1').resize(800, 492)
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pin Nodes']).activate() # MenuItemLogger
checkpoint Graphics_1 Pin Nodes updated
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(230)
checkpoint_count("Pin Nodes toolbox move event")

assert tests.gtkMultiTextCompare({'Mouse X':'','Mouse Y':'','Node X':'','Node Y':''},tbox)
assert findWidget(tbox+":Pin Label").get_text()==''
assert findWidget(tbox+":Status").get_text()=='0 nodes pinned.'
assert tests.sensitizationCheck({'Undo':False,'Invert':False,'Redo':False,'UnPinAll':False},tbox)

# Load a Skeleton
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
findWidget('Dialog-Data:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint active area status updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
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
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Pin Nodes updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Graphics_1 Pin Nodes updated
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
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
assert tests.gtkMultiTextCompare({'Mouse X':'','Mouse Y':'','Node X':'','Node Y':''},tbox)
assert findWidget(tbox+":Pin Label").get_text()==''
assert findWidget(tbox+":Status").get_text()=='0 nodes pinned.'
assert tests.sensitizationCheck({'Undo':False,'Invert':True,'Redo':False,'UnPinAll':False},tbox)

# Move mouse to the node at (22, 50). Half way up the image, on the
# left edge of the triangle.  Then pin the node.
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('move', 46.15, 102.15, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 43.7, 100.05, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 40.55, 96.55, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 38.8, 94.1, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 36.7, 90.6, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 34.6, 86.05, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 33.2, 82.55, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 31.1, 79.05, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 29.7, 74.5, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 29.7, 69.25, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 29.35, 64.35, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 28.65, 60.85, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 26.9, 57, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 25.85, 54.2, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 24.8, 52.1, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 23.4, 49.65, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.3, 47.55, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 20.6, 46.85, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 20.95, 46.85, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 20.95, 47.2, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.3, 47.9, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.3, 48.25, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.3, 48.25, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.3, 48.6, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.3, 48.6, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.3, 48.6, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.65, 48.6, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.65, 48.95, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.65, 48.95, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.65, 49.3, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.65, 49.3, 0, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 21.65, 49.3, 0, False, False)
checkpoint Pin Nodes toolbox move event

# Arrived at node.
assert tests.gtkMultiTextCompare({'Mouse X':'21.65','Mouse Y':'49.3','Node X':'22','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='unpinned'
assert findWidget(tbox+":Status").get_text()=='0 nodes pinned.'
assert tests.sensitizationCheck({'Undo':False,'Invert':True,'Redo':False,'UnPinAll':False},tbox)

# Pin node.
findGfxWindow('Graphics_1').simulateMouse('down', 21.65, 49.3, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 21.65, 49.3, 1, False, False)
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.Pin
assert tests.gtkMultiTextCompare({'Mouse X':'21.65','Mouse Y':'49.3','Node X':'22','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='pinned'
assert findWidget(tbox+":Status").get_text()=='1 node pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)

# Move to next node (37.5, 50), next one in the +x direction from the
# previous one
findGfxWindow('Graphics_1').simulateMouse('move', 22.35, 96.2, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 24.45, 86.4, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 25.15, 82.2, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 25.5, 80.1, 1, False, False)
checkpoint Pin Nodes toolbox move event
assert tests.gtkMultiTextCompare({'Mouse X':'25.5','Mouse Y':'80.1','Node X':'25','Node Y':'87.5'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='unpinned'
assert findWidget(tbox+":Status").get_text()=='1 node pinned.'
findGfxWindow('Graphics_1').simulateMouse('move', 25.5, 79.75, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 26.55, 75.9, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 27.6, 65.75, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 27.6, 59.1, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 30.75, 51.75, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 31.1, 50, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 33.55, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 35.65, 47.55, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 35.65, 47.55, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 36.7, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 37.05, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 37.05, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 37.05, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 37.05, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 37.05, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 37.05, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event

# Arrived at next node.
assert tests.gtkMultiTextCompare({'Mouse X':'37.05','Mouse Y':'48.95','Node X':'37.5','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='unpinned'
assert findWidget(tbox+":Status").get_text()=='1 node pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)
findGfxWindow('Graphics_1').simulateMouse('down', 37.05, 48.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 37.05, 48.95, 1, False, False)
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.Pin

# Pinned it.
assert tests.gtkMultiTextCompare({'Mouse X':'37.05','Mouse Y':'48.95','Node X':'37.5','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='pinned'
assert findWidget(tbox+":Status").get_text()=='2 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)

# Move to center node and pin it
findGfxWindow('Graphics_1').simulateMouse('move', 49.65, 100.4, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50.7, 94.1, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 53.5, 85.35, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 55.25, 75.55, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 56.3, 70.3, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 57, 67.15, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 57.35, 62.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 57, 58.75, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 55.6, 54.55, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 54.2, 52.45, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.8, 51.05, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.1, 51.05, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.4, 50.7, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.4, 50.7, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.4, 50.7, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50.7, 50.35, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50.35, 50.35, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50, 50.35, 1, False, False)
checkpoint Pin Nodes toolbox move event

# Arrived at third node.
assert tests.gtkMultiTextCompare({'Mouse X':'50','Mouse Y':'50.35','Node X':'50','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='unpinned'
assert findWidget(tbox+":Status").get_text()=='2 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)
findGfxWindow('Graphics_1').simulateMouse('down', 50, 50.35, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 50, 50.35, 1, False, False)
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.Pin
# Pinned it.
assert tests.gtkMultiTextCompare({'Mouse X':'50','Mouse Y':'50.35','Node X':'50','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='pinned'
assert findWidget(tbox+":Status").get_text()=='3 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)

findGfxWindow('Graphics_1').simulateMouse('move', 50, 50.35, 1, False, False)
checkpoint Pin Nodes toolbox move event


# Move to and pin a fourth node, on the right edge of the triangle at y=50
findGfxWindow('Graphics_1').simulateMouse('move', 65.05, 4.5, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 59.45, 18.5, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 58.05, 26.9, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 55.95, 32.5, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 55.6, 34.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.45, 38.8, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.05, 43.35, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50.35, 45.1, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50, 46.15, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 49.65, 47.55, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 49.65, 47.55, 1, False, False)
checkpoint Pin Nodes toolbox move event
assert tests.gtkMultiTextCompare({'Mouse X':'49.65','Mouse Y':'47.55','Node X':'50','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='pinned'
assert findWidget(tbox+":Status").get_text()=='3 nodes pinned.'
findGfxWindow('Graphics_1').simulateMouse('move', 49.65, 47.9, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 49.65, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 49.65, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50.35, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50.7, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.4, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.1, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.8, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 53.5, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 54.55, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 55.25, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 56.3, 47.9, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 57.35, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 60.5, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 63.65, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 65.4, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 67.15, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 68.2, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 68.2, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 68.9, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 68.9, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 69.25, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 69.6, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 69.95, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 69.95, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 69.95, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 70.3, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 70.3, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 70.65, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 71.35, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 71.35, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event

# Arrived at fourth node.
assert tests.gtkMultiTextCompare({'Mouse X':'71.35','Mouse Y':'48.95','Node X':'72','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='unpinned'
assert findWidget(tbox+":Status").get_text()=='3 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)
findGfxWindow('Graphics_1').simulateMouse('down', 71.35, 48.95, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 71.35, 48.95, 1, False, False)
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.Pin

# Pinned it.
assert tests.gtkMultiTextCompare({'Mouse X':'71.35','Mouse Y':'48.95','Node X':'72','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='pinned'
assert findWidget(tbox+":Status").get_text()=='4 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)

# Undo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pin Nodes:Undo').clicked()
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.Undo
assert tests.gtkMultiTextCompare({'Mouse X':'71.35','Mouse Y':'48.95','Node X':'72','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='pinned'
assert findWidget(tbox+":Status").get_text()=='3 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':True,'UnPinAll':True},tbox)

# Undo again
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pin Nodes:Undo').clicked()
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.Undo
assert tests.gtkMultiTextCompare({'Mouse X':'71.35','Mouse Y':'48.95','Node X':'72','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='pinned'
assert findWidget(tbox+":Status").get_text()=='2 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':True,'UnPinAll':True},tbox)

# Redo
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pin Nodes:Redo').clicked()
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.Redo
assert tests.gtkMultiTextCompare({'Mouse X':'71.35','Mouse Y':'48.95','Node X':'72','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='pinned'
assert findWidget(tbox+":Status").get_text()=='3 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':True,'UnPinAll':True},tbox)

# Move to the node at (50,50) and control-click to toggle it.
findGfxWindow('Graphics_1').simulateMouse('move', 25.15, 2.75, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 25.5, 19.2, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 27.95, 26.9, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 33.55, 29.35, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 36.7, 31.1, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 37.75, 32.85, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 43.7, 40.55, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 46.15, 44.75, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 48.6, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50.35, 51.05, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50.35, 51.05, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50.35, 51.05, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50, 51.05, 1, False, False)
checkpoint Pin Nodes toolbox move event

# Arrived at another node.
assert tests.gtkMultiTextCompare({'Mouse X':'50','Mouse Y':'51.05','Node X':'50','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='pinned'
assert findWidget(tbox+":Status").get_text()=='3 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':True,'UnPinAll':True},tbox)

# Ctrl-click to toggle it.
findGfxWindow('Graphics_1').simulateMouse('down', 50, 51.05, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 50, 51.05, 1, False, True)
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.TogglePin

assert tests.gtkMultiTextCompare({'Mouse X':'50','Mouse Y':'51.05','Node X':'50','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='unpinned'
assert findWidget(tbox+":Status").get_text()=='2 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)

# Move to the node at (50,50) and toggle it off.
findGfxWindow('Graphics_1').simulateMouse('move', 54.55, 2.75, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 54.9, 8, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 54.2, 17.45, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 53.15, 32.15, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.75, 38.45, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.75, 40.55, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.4, 43, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.4, 43.7, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.75, 44.75, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.75, 45.8, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.1, 46.85, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.1, 47.55, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.1, 47.9, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.1, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.1, 48.25, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.1, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.1, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 52.1, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.75, 48.6, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.75, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.75, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.75, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.75, 48.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.4, 49.3, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 51.05, 49.3, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 50.7, 49.65, 1, False, False)
checkpoint Pin Nodes toolbox move event
# Arrived at the node
assert tests.gtkMultiTextCompare({'Mouse X':'50.7','Mouse Y':'49.65','Node X':'50','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='unpinned'
assert findWidget(tbox+":Status").get_text()=='2 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)

# Toggle it off
findGfxWindow('Graphics_1').simulateMouse('down', 50.7, 49.65, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 50.7, 49.65, 1, False, True)
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.TogglePin
assert tests.gtkMultiTextCompare({'Mouse X':'50.7','Mouse Y':'49.65','Node X':'50','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='pinned'
assert findWidget(tbox+":Status").get_text()=='3 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)

# Move to the second pinned node (37.5, 50) and unpin it with shift-click
findGfxWindow('Graphics_1').simulateMouse('move', 32.15, -0.05, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 32.85, 10.45, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 33.2, 15.35, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 33.9, 21.65, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 35.3, 34.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 36, 45.1, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 37.4, 50.35, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 37.4, 51.05, 1, False, False)
checkpoint Pin Nodes toolbox move event
# Arrived at another node.
assert tests.gtkMultiTextCompare({'Mouse X':'37.4','Mouse Y':'51.05','Node X':'37.5','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='pinned'
assert findWidget(tbox+":Status").get_text()=='3 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)

# Shift-click to unpin it.
findGfxWindow('Graphics_1').simulateMouse('down', 37.4, 51.05, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 37.4, 51.05, 1, True, False)
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.UnPin
assert tests.gtkMultiTextCompare({'Mouse X':'37.4','Mouse Y':'51.05','Node X':'37.5','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='unpinned'
assert findWidget(tbox+":Status").get_text()=='2 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)

# Shift-click to unpin it again -- should be a no-op.
findGfxWindow('Graphics_1').simulateMouse('down', 37.05, 50.35, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 37.05, 50.35, 1, True, False)
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.UnPin
assert tests.gtkMultiTextCompare({'Mouse X':'37.05','Mouse Y':'50.35','Node X':'37.5','Node Y':'50'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='unpinned'
assert findWidget(tbox+":Status").get_text()=='2 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)

# Invert
findGfxWindow('Graphics_1').simulateMouse('move', 37.05, 53.15, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 26.2, 50.7, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', 2.05, 41.95, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', -18.95, 30.4, 1, False, False)
checkpoint Pin Nodes toolbox move event
findGfxWindow('Graphics_1').simulateMouse('move', -22.1, 26.9, 1, False, False)
checkpoint Pin Nodes toolbox move event
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pin Nodes:Invert').clicked()
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.Invert
assert tests.gtkMultiTextCompare({'Mouse X':'-22.1','Mouse Y':'26.9','Node X':'0','Node Y':'25'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='unpinned'
assert findWidget(tbox+":Status").get_text()=='73 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':True},tbox)

# Unpin all
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pin Nodes:UnPinAll').clicked()
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pin_Nodes.UnPinAll
assert tests.gtkMultiTextCompare({'Mouse X':'-22.1','Mouse Y':'26.9','Node X':'0','Node Y':'25'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='unpinned'
assert findWidget(tbox+":Status").get_text()=='0 nodes pinned.'
assert tests.sensitizationCheck({'Undo':True,'Invert':True,'Redo':False,'UnPinAll':False},tbox)

# Delete the skeleton layer from the graphics window
wevent(findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList'), Gdk.EventType.BUTTON_PRESS, button=3, state=0, window=findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_window())
checkpoint toplevel widget mapped PopUp-0
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
checkpoint OOF.Graphics_1.Layer.Select
findMenu(findWidget('PopUp-0'), ['Delete']).activate() # MenuItemLogger
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
checkpoint Graphics_1 Pin Nodes updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.Delete
deactivatePopup('PopUp-0') # MenuItemLogger
assert tests.gtkMultiTextCompare({'Mouse X':'-22.1','Mouse Y':'26.9','Node X':'0','Node Y':'25'},tbox)
assert findWidget(tbox+":Pin Label").get_text()=='unpinned'
assert findWidget(tbox+":Status").get_text()=='0 nodes pinned.'
assert tests.sensitizationCheck({'Undo':False,'Invert':False,'Redo':False,'UnPinAll':False},tbox)

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Python_Log']).activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(192, 122)
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
findWidget('Dialog-Python_Log:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff("session.log")

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
