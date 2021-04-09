# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


## This file tests for the presence of a bug that caused
## Skeleton.hashNodes to divide by zero.  The origin of the bug is
## Microstructure._size being a Point with x and y set to integers,
## and y > x.  hashNodes computes an aspect ratio, which was set to
## zero by integer arithmetic.

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)

# Create a Microstructure with height > width where both are integers
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('OOF2').resize(782, 545)
findWidget('Dialog-Create Microstructure:width').set_text('')
findWidget('Dialog-Create Microstructure:width').set_text('1')
findWidget('Dialog-Create Microstructure:width').set_text('10')
findWidget('Dialog-Create Microstructure:height').set_text('1')
findWidget('Dialog-Create Microstructure:height').set_text('12')
findWidget('Dialog-Create Microstructure:height').set_text('120')
findWidget('Dialog-Create Microstructure:height').set_text('20')
findWidget('Dialog-Create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint pixel page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
checkpoint mesh bdy page updated
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
checkpoint OOF.Microstructure.New

# Create a Skeleton
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton page info updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton page info updated
checkpoint skeleton selection page selection sensitized Element
checkpoint Solver page sensitized
checkpoint OOF.Skeleton.New
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton page sensitized

# Open a graphics window and display the skeleton
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
wevent(findWidget('Dialog-New Graphics Layer:category'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New Graphics Layer:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
findWidget('Dialog-New Graphics Layer:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
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

# Get info on nodes
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Info']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Skeleton Info sensitized
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(243)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Info:Click:Node').clicked()
findGfxWindow('Graphics_1').simulateMouse('down', 2.5807663, 19.747057, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 2.5807663, 19.466566, 1, False, False)
checkpoint Graphics_1 Skeleton Info showed position
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryNode
findGfxWindow('Graphics_1').simulateMouse('down', 2.5106436, 15.481843, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 2.5106436, 15.341598, 1, False, False)
checkpoint Graphics_1 Skeleton Info showed position
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryNode
findGfxWindow('Graphics_1').simulateMouse('down', 2.4405209, 10.350614, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 2.5106436, 10.070123, 1, False, False)
checkpoint Graphics_1 Skeleton Info showed position
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryNode
findGfxWindow('Graphics_1').simulateMouse('down', 2.5106436, 5.2316554, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 2.5106436, 5.2316554, 1, False, False)
checkpoint Graphics_1 Skeleton Info showed position
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryNode
findGfxWindow('Graphics_1').simulateMouse('down', 2.5106436, 0.60355622, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 2.5106436, 0.60355622, 1, False, False)
checkpoint Graphics_1 Skeleton Info showed position
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryNode
findGfxWindow('Graphics_1').simulateMouse('down', -0.083896819, 0.3809166, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.05634861, 0.3809166, 1, False, False)
checkpoint Graphics_1 Skeleton Info showed position
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryNode
findGfxWindow('Graphics_1').simulateMouse('down', 10.036564, 19.945154, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 10.036564, 19.945154, 1, False, False)
checkpoint Graphics_1 Skeleton Info showed position
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Skeleton_Info.QueryNode
findWidget('OOF2 Graphics 1').resize(800, 492)
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
assert tests.filediff("session.log", tolerance=1.e-6)

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
