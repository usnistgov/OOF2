# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Check that the "peeked" node is drawn correctly, and is consistent
# with the selection in the toolbox's node list.

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)

wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('OOF2').resize(782, 545)
findWidget('Dialog-Create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
checkpoint pixel page sensitized
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint Materials page updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.New
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Material:Assign').clicked()
checkpoint toplevel widget mapped Dialog-Assign material material to pixels
findWidget('Dialog-Assign material material to pixels').resize(235, 122)
wevent(findWidget('Dialog-Assign material material to pixels:pixels'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Assign material material to pixels:pixels').get_window())
checkpoint toplevel widget mapped chooserPopup-pixels
findMenu(findWidget('chooserPopup-pixels'), ['<every>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-pixels') # MenuItemLogger
findWidget('Dialog-Assign material material to pixels:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Material.Assign
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
checkpoint skeleton selection page updated
checkpoint skeleton selection page selection sensitized Element
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
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['FE Mesh']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint page installed FE Mesh
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(130)
findWidget('OOF2:FE Mesh Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create a new mesh
findWidget('Dialog-Create a new mesh').resize(299, 244)
wevent(findWidget('Dialog-Create a new mesh:element_types:Func'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Create a new mesh:element_types:Func').get_window())
checkpoint toplevel widget mapped chooserPopup-Func
findMenu(findWidget('chooserPopup-Func'), ['2']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Func') # MenuItemLogger
findWidget('Dialog-Create a new mesh:widget_GTK_RESPONSE_OK').clicked()
checkpoint mesh bdy page updated
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint Solver page sensitized
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Mesh.New
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
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
findWidget('OOF2 Graphics 1:Pane0').set_position(360)
findWidget('OOF2 Graphics 1:Pane0:Pane1').set_position(672)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(212)
checkpoint toplevel widget mapped OOF2 Graphics 1
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([10]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
# Click on an Element
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Mesh Info']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(227)
findGfxWindow('Graphics_1').simulateMouse('down', 0.20373153, 0.1178312, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.20373153, 0.1178312, 1, False, False)
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryElement
assert tests.elementMode()
assert tests.nodeListCheck(['FuncNode 0 at (0, 0)', 'FuncNode 25 at (0.125, 0)', 'FuncNode 1 at (0.25, 0)', 'FuncNode 26 at (0.25, 0.125)', 'FuncNode 6 at (0.25, 0.25)', 'FuncNode 27 at (0.125, 0.25)', 'FuncNode 5 at (0, 0.25)', 'FuncNode 28 at (0, 0.125)'])

# Click on another Element
findGfxWindow('Graphics_1').simulateMouse('down', 0.31040571, 0.14211119, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.31040571, 0.14211119, 1, False, False)
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryElement
assert tests.nodeListCheck(['FuncNode 1 at (0.25, 0)', 'FuncNode 29 at (0.375, 0)', 'FuncNode 2 at (0.5, 0)', 'FuncNode 30 at (0.5, 0.125)', 'FuncNode 7 at (0.5, 0.25)', 'FuncNode 31 at (0.375, 0.25)', 'FuncNode 6 at (0.25, 0.25)', 'FuncNode 26 at (0.25, 0.125)'])

# Clikc on a third Element
findGfxWindow('Graphics_1').simulateMouse('down', 0.70861508, 0.20872777, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.70861508, 0.20872777, 1, False, False)
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryElement
assert tests.nodeListCheck(['FuncNode 2 at (0.5, 0)', 'FuncNode 32 at (0.625, 0)', 'FuncNode 3 at (0.75, 0)', 'FuncNode 33 at (0.75, 0.125)', 'FuncNode 8 at (0.75, 0.25)', 'FuncNode 34 at (0.625, 0.25)', 'FuncNode 7 at (0.5, 0.25)', 'FuncNode 30 at (0.5, 0.125)'])
assert tests.peekNodeCheck(None)

# Click on a node in the nodes list
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:ElementInfo:NodeList').get_selection().select_path(Gtk.TreePath([1]))
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.5000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 5.0000000000000e+00)
checkpoint contourmap info updated for Graphics_1
assert tests.peekNodeCheck(32)

# Click on a different node
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:ElementInfo:NodeList').get_selection().select_path(Gtk.TreePath([0]))
checkpoint contourmap info updated for Graphics_1
assert tests.peekNodeCheck(2)

# Click on another node
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:ElementInfo:NodeList').get_selection().select_path(Gtk.TreePath([4]))
checkpoint contourmap info updated for Graphics_1
assert tests.peekNodeCheck(8)

# Click on an element (on the canvas) that shares the currently selected node (in the node list).
findGfxWindow('Graphics_1').simulateMouse('down', 0.69809667, 0.32443025, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.69809667, 0.32443025, 1, False, False)
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryElement
assert tests.nodeListCheck(['FuncNode 7 at (0.5, 0.25)', 'FuncNode 34 at (0.625, 0.25)', 'FuncNode 8 at (0.75, 0.25)', 'FuncNode 43 at (0.75, 0.375)', 'FuncNode 13 at (0.75, 0.5)', 'FuncNode 44 at (0.625, 0.5)', 'FuncNode 12 at (0.5, 0.5)', 'FuncNode 41 at (0.5, 0.375)'])
assert tests.peekNodeCheck(8)

# Click on a node in the node list
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:ElementInfo:NodeList').get_selection().select_path(Gtk.TreePath([3]))
checkpoint contourmap info updated for Graphics_1
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 3.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 1.0000000000000e+00)
assert tests.peekNodeCheck(43)

# Double-click the node in the node list
findGfxWindow('Graphics_1').simulateMouse('scroll', -1, -0, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('scroll', -3, -0, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('scroll', -1, -0, 1, False, False)
tree=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:ElementInfo:NodeList')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([3]), column)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryNode
assert tests.nodeMode()

# Click on a different node on the canvas
findGfxWindow('Graphics_1').simulateMouse('down', 0.74367643, 0.62972702, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.74367643, 0.62972702, 1, False, False)
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryNode
assert tests.nodeMode()

# Click Prev
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:Prev').clicked()
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
assert tests.nodeMode()

# Click Prev again
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:Prev').clicked()
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
assert tests.elementMode()
assert tests.nodeListCheck(['FuncNode 7 at (0.5, 0.25)', 'FuncNode 34 at (0.625, 0.25)', 'FuncNode 8 at (0.75, 0.25)', 'FuncNode 43 at (0.75, 0.375)', 'FuncNode 13 at (0.75, 0.5)', 'FuncNode 44 at (0.625, 0.5)', 'FuncNode 12 at (0.5, 0.5)', 'FuncNode 41 at (0.5, 0.375)'])
assert tests.peekNodeCheck(43)

# Click Prev again
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 2.8000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 5.4000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 8.2000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 1.2800000000000e+02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:Prev').clicked()
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
assert tests.elementMode()
assert tests.nodeListCheck(['FuncNode 2 at (0.5, 0)', 'FuncNode 32 at (0.625, 0)', 'FuncNode 3 at (0.75, 0)', 'FuncNode 33 at (0.75, 0.125)', 'FuncNode 8 at (0.75, 0.25)', 'FuncNode 34 at (0.625, 0.25)', 'FuncNode 7 at (0.5, 0.25)', 'FuncNode 30 at (0.5, 0.125)'])
assert tests.peekNodeCheck(None)

# Prev yet again
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:Prev').clicked()
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
assert tests.elementMode()
assert tests.nodeListCheck(['FuncNode 1 at (0.25, 0)', 'FuncNode 29 at (0.375, 0)', 'FuncNode 2 at (0.5, 0)', 'FuncNode 30 at (0.5, 0.125)', 'FuncNode 7 at (0.5, 0.25)', 'FuncNode 31 at (0.375, 0.25)', 'FuncNode 6 at (0.25, 0.25)', 'FuncNode 26 at (0.25, 0.125)'])
assert tests.peekNodeCheck(None)

# Click Next
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 9.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:Next').clicked()
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
assert tests.nodeListCheck(['FuncNode 2 at (0.5, 0)', 'FuncNode 32 at (0.625, 0)', 'FuncNode 3 at (0.75, 0)', 'FuncNode 33 at (0.75, 0.125)', 'FuncNode 8 at (0.75, 0.25)', 'FuncNode 34 at (0.625, 0.25)', 'FuncNode 7 at (0.5, 0.25)', 'FuncNode 30 at (0.5, 0.125)'])
assert tests.peekNodeCheck(None)

# Next again
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 6.0000000000000e+00)
findGfxWindow('Graphics_1').simulateMouse('scroll', -0, 5, 1, False, False)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.0000000000000e+00)
findGfxWindow('Graphics_1').simulateMouse('scroll', -0, 13, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('scroll', -0, -0, 1, False, False)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:Next').clicked()
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 0.0000000000000e+00)
assert tests.elementMode()
assert tests.nodeListCheck(['FuncNode 7 at (0.5, 0.25)', 'FuncNode 34 at (0.625, 0.25)', 'FuncNode 8 at (0.75, 0.25)', 'FuncNode 43 at (0.75, 0.375)', 'FuncNode 13 at (0.75, 0.5)', 'FuncNode 44 at (0.625, 0.5)', 'FuncNode 12 at (0.5, 0.5)', 'FuncNode 41 at (0.5, 0.375)'])
assert tests.peekNodeCheck(None)

# Next yet again
findGfxWindow('Graphics_1').simulateMouse('up', -0.16791886, 0.48597546, 1, False, False)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:Next').clicked()
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info sensitized
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint Graphics_1 Mesh Info updated
checkpoint contourmap info updated for Graphics_1
assert tests.nodeMode()

# Check x=0.75 y=0.375 index=43 position=(0.75, 0.375)
findWidget('OOF2 Graphics 1').resize(800, 492)
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Python_Log']).activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(192, 122)
findWidget('Dialog-Python_Log:filename').set_text('d')
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
findWidget('Dialog-Python_Log:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Python_Log
assert tests.filediff("session.log")

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close