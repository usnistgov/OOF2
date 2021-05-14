# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)

# Open a graphics window
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
findWidget('OOF2').resize(782, 545)
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['Settings', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
wevent(findWidget('Dialog-New_Layer_Policy:policy'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
checkpoint toplevel widget mapped chooserPopup-policy
findMenu(findWidget('chooserPopup-policy'), ['Single']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-policy') # MenuItemLogger
findWidget('Dialog-New_Layer_Policy:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Graphics_1.Settings.New_Layer_Policy
findWidget('OOF2 Graphics 1').resize(800, 492)
# Open the Mesh Info toolbox
wevent(findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Mesh Info']).activate() # MenuItemLogger
checkpoint Graphics_1 Mesh Info sensitized
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(227)
# Open a Data viewer
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Mesh Info:NewDataViewer').clicked()
checkpoint Mesh_Data_1 time updated
checkpoint Mesh_Data_1 mesh updated
checkpoint toplevel widget mapped Mesh Data 1
findWidget('Mesh Data 1').resize(278, 372)
# Load a Mesh
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('T')
findWidget('Dialog-Data:filename').set_text('TE')
findWidget('Dialog-Data:filename').set_text('TES')
findWidget('Dialog-Data:filename').set_text('TEST')
findWidget('Dialog-Data:filename').set_text('TEST_')
findWidget('Dialog-Data:filename').set_text('TEST_D')
findWidget('Dialog-Data:filename').set_text('TEST_DA')
findWidget('Dialog-Data:filename').set_text('TEST_DAT')
findWidget('Dialog-Data:filename').set_text('TEST_DATA')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/m')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/me')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/mes')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/mesh')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshi')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshin')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinf')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfo')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfot')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotb')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbo')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbox')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbox.')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbox.m')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbox.me')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbox.mes')
findWidget('Dialog-Data:filename').set_text('TEST_DATA/meshinfotbox.mesh')
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
checkpoint Mesh_Data_1 data updated
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
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
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
checkpoint Mesh_Data_1 time updated
checkpoint Mesh_Data_1 data updated
checkpoint Mesh_Data_1 mesh updated
checkpoint Mesh_Data_1 data updated
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
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page groups sensitized Element
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
checkpoint Graphics_1 Mesh Info cleared position
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Mesh_Data_1 time updated
checkpoint Mesh_Data_1 data updated
checkpoint Mesh_Data_1 data updated
checkpoint Mesh_Data_1 mesh updated
checkpoint Mesh_Data_1 data updated
checkpoint contourmap info updated for Graphics_1
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
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Mesh_Data_1 data updated
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Mesh_Data_1 data updated
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Mesh_Data_1 data updated
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Mesh_Data_1 data updated
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Mesh_Data_1 data updated
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Mesh_Data_1 data updated
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Mesh_Data_1 data updated
checkpoint Field page sensitized
checkpoint mesh page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Mesh_Data_1 data updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.File.Load.Data
# Switch Data Viewer to Flux mode
wevent(findWidget('Mesh Data 1:ViewSource:output:output_0'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Mesh Data 1:ViewSource:output:output_0').get_window())
checkpoint toplevel widget mapped chooserPopup-output_0
findMenu(findWidget('chooserPopup-output_0'), ['Flux']).activate() # MenuItemLogger
checkpoint Mesh_Data_1 data updated
deactivatePopup('chooserPopup-output_0') # MenuItemLogger
# Click on an element
findGfxWindow('Graphics_1').simulateMouse('down', 44.56549, 95.846481, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 44.56549, 95.846481, 1, False, False)
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info updated
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Mesh_Data_1 data updated
checkpoint Mesh_Data_1 position updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryElement
findWidget('Mesh Data 1').resize(543, 492)
assert findWidget('Mesh Data 1:ViewSource').get_expanded()
assert tests.gtkMultiTextCompare({'xx':'0.00155625','xy':'0.00141672','xz':'0','yy':'0.0654975','yz':'0','zz':'-0.00492302'},'Mesh Data 1:Data', tolerance=1.e-8)
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','x':'44.2653','y':'88.0063'},'Mesh Data 1:ViewSource')
assert not findWidget('Mesh Data 1:Freeze:Space').get_active()
assert tests.is_sensitive('Mesh Data 1:Close')

# Unexpand the source part of the Data Viewer
findWidget('Mesh Data 1:ViewSource').set_expanded(0)
assert not findWidget('Mesh Data 1:ViewSource').get_expanded()
assert tests.gtkMultiTextCompare({'xx':'0.00155625','xy':'0.00141672','xz':'0','yy':'0.0654975','yz':'0','zz':'-0.00492302'},'Mesh Data 1:Data', tolerance=1.e-8)
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','x':'44.2653','y':'88.0063'},'Mesh Data 1:ViewSource')
assert not findWidget('Mesh Data 1:Freeze:Space').get_active()
assert tests.is_sensitive('Mesh Data 1:Close')

# Click on another element
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.0740740740741e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 4.2962962962963e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 1.1814814814815e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 2.9000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 67.4177, 44.1224, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 67.4177, 44.1224, 1, False, False)
checkpoint Graphics_1 Mesh Info showed position
checkpoint Graphics_1 Mesh Info updated
checkpoint Graphics_1 Mesh Info sensitized
checkpoint Mesh_Data_1 data updated
checkpoint Mesh_Data_1 position updated
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Mesh_Info.QueryElement
# New query, data changed, source still contracted.
assert not findWidget('Mesh Data 1:ViewSource').get_expanded()
assert tests.gtkMultiTextCompare({'xx':'0.00435063','xy':'0.00123586','xz':'0','yy':'0.0767109','yz':'0','zz':'-0.00161553'},'Mesh Data 1:Data', tolerance=1.e-8)
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','x':'67.608','y':'39.9644'},'Mesh Data 1:ViewSource')
assert not findWidget('Mesh Data 1:Freeze:Space').get_active()
assert tests.is_sensitive('Mesh Data 1:Close')

# Re-expand the Source view
findWidget('Mesh Data 1:ViewSource').set_expanded(1)
assert findWidget('Mesh Data 1:ViewSource').get_expanded()
assert tests.gtkMultiTextCompare({'xx':'0.00435063','xy':'0.00123586','xz':'0','yy':'0.0767109','yz':'0','zz':'-0.00161553'},'Mesh Data 1:Data', tolerance=1.e-8)
assert tests.gtkMultiTextCompare({'meshname':'microstructure:skeleton:mesh','x':'67.608','y':'39.9644'},'Mesh Data 1:ViewSource')
assert not findWidget('Mesh Data 1:Freeze:Space').get_active()
assert tests.is_sensitive('Mesh Data 1:Close')

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
