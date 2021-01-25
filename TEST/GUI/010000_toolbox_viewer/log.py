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

findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 3.2000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
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
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1').resize(800, 492)

# Check the text in the zoom factor, should be 1.5
assert tests.gtkTextCompare('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer:Zoom:Factor','1.5')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer:Info').clicked()
findWidget('OOF2').resize(782, 545)

# Check tail of messages for text correctness.
assert tests.gtkTextviewTail('OOF2 Messages 1:Text', "Pixels per unit   :  0.0\n", tolerance=1.e-6)

# Load an image
event(Gdk.EventType.BUTTON_PRESS,x= 7.9000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('OOF2:Microstructure Page:NewFromFile').clicked()
checkpoint toplevel widget mapped Dialog-Load Image and create Microstructure
findWidget('Dialog-Load Image and create Microstructure').resize(237, 200)
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
findWidget('Dialog-Load Image and create Microstructure:widget_GTK_RESPONSE_OK').clicked()
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
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Microstructure.Create_From_ImageFile

# Check viewer info again
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer:Info').clicked()
assert tests.gtkTextviewTail('OOF2 Messages 1:Text',"Pixels per unit   :  1.9047619\n", tolerance=1.e-6)

# Get ppu for later checks
starting_ppu = tests.getCanvasPPU()

# Click in the graphics window
findGfxWindow('Graphics_1').simulateMouse('down', 51.9, 68.7, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 51.9, 68.7, 1, False, False)
assert tests.gtkMultiTextCompare({'PixelX':'51','PixelY':'68','PhysicalX':'51.9','PhysicalY':'68.7'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer')

# Zoom in
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer:Zoom:In').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 7.5000000000000e+01)
checkpoint OOF.Graphics_1.Settings.Zoom.In
assert tests.checkCanvasPPU(starting_ppu, 1.5)

# Click again on the canvas
findGfxWindow('Graphics_1').simulateMouse('up', 34.05, 42.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('down', 34.75, 42.1, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 34.75, 42.1, 1, False, False)
assert tests.gtkMultiTextCompare({'PixelX':'34','PixelY':'42','PhysicalX':'34.75','PhysicalY':'42.1'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer')

# Zoom out
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer:Zoom:Out').clicked()
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 0.0000000000000e+00)
checkpoint OOF.Graphics_1.Settings.Zoom.Out
assert tests.checkCanvasPPU(starting_ppu, 1.0)

# Control-click to zoom out
findWidget('OOF2 Graphics 1').resize(800, 492)
findGfxWindow('Graphics_1').simulateMouse('down', 49.8, 65.025, 1, False, True)
findGfxWindow('Graphics_1').simulateMouse('up', 49.8, 65.025, 1, False, True)
checkpoint OOF.Graphics_1.Settings.Zoom.OutFocussed
assert tests.gtkMultiTextCompare({'PixelX':'49','PixelY':'65','PhysicalX':'49.8','PhysicalY':'65.03'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer')
assert tests.checkCanvasPPU(starting_ppu, 1.0/1.5)

# Fill window
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 2.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer:Zoom:Fill').clicked()
checkpoint OOF.Graphics_1.Settings.Zoom.Fill_Window
assert tests.checkCanvasPPU(starting_ppu, 1.0)

# Shift-click to zoom in
findGfxWindow('Graphics_1').simulateMouse('down', 144.3, 146.925, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 144.825, 146.925, 1, True, False)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:hscroll').get_adjustment().set_value( 2.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:Canvas:vscroll').get_adjustment().set_value( 7.0000000000000e+00)
checkpoint OOF.Graphics_1.Settings.Zoom.InFocussed
assert tests.checkCanvasPPU(starting_ppu, 1.5)

# Click on a pixel
findGfxWindow('Graphics_1').simulateMouse('up', 35.45, 124, 1, False, False)
assert tests.gtkMultiTextCompare({'PixelX':'144','PixelY':'146','PhysicalX':'144.8','PhysicalY':'146.9'},'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Viewer')

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
findMenu(findWidget('OOF2 Graphics 1:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
