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
findWidget('OOF2').resize(782, 545)
# Open the Pixel Selection page first, so that its initial
# sensitization runs.
event(Gdk.EventType.BUTTON_PRESS,x= 2.4000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
assert tests.sensitization0()
event(Gdk.EventType.BUTTON_PRESS,x= 3.2000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/c')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/co')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/com')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/comp')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/compo')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/compos')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/compost')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/composti')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/compost')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/compos')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/composi')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/composit')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/compositi')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/compositio')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/composition')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/composition.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/composition.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/composition.pn')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/composition.png')
findWidget('Dialog-Load Image and create Microstructure:width').insert_text('1', 6)
findWidget('Dialog-Load Image and create Microstructure:width').insert_text('.', 1)
findWidget('Dialog-Load Image and create Microstructure:width').insert_text('0', 2)
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
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
findMenu(findWidget('OOF2:MenuBar'), ['Settings', 'Graphics_Defaults', 'New_Layer_Policy']).activate()
checkpoint toplevel widget mapped Dialog-New_Layer_Policy
findWidget('Dialog-New_Layer_Policy').resize(192, 86)
event(Gdk.EventType.BUTTON_PRESS,x= 2.0000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('Dialog-New_Layer_Policy:policy').get_window())
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
findWidget('OOF2 Graphics 1:Pane0:LayerScroll:LayerList').get_selection().select_path(Gtk.TreePath([13]))
checkpoint OOF.Graphics_1.Layer.Select
findWidget('OOF2 Graphics 1').resize(800, 492)
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Windows.Graphics.New
findWidget('OOF2 Graphics 1').resize(800, 492)
event(Gdk.EventType.BUTTON_PRESS,x= 5.0000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
event(Gdk.EventType.BUTTON_PRESS,x= 6.7000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Burn']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findGfxWindow('Graphics_1').simulateMouse('down', 0.25325, 0.129, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.25325, 0.129, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionPageStatusCheck(1938, 10000, 19.38)
assert tests.pixelSelectionSizeCheck('composition.png', 1938)
assert tests.sensitization2()


findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Introduction
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 2.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 11)
findWidget('Dialog-Create new pixel group:name').insert_text('l', 11)
findWidget('Dialog-Create new pixel group:name').insert_text('o', 1)
findWidget('Dialog-Create new pixel group:name').insert_text('w', 2)
findWidget('Dialog-Create new pixel group:name').insert_text('e', 3)
findWidget('Dialog-Create new pixel group:name').insert_text('r', 4)
findWidget('Dialog-Create new pixel group:name').insert_text('l', 5)
findWidget('Dialog-Create new pixel group:name').insert_text('e', 6)
findWidget('Dialog-Create new pixel group:name').insert_text('f', 7)
findWidget('Dialog-Create new pixel group:name').insert_text('t', 8)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
checkpoint microstructure page sensitized
checkpoint meshable button set
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
event(Gdk.EventType.BUTTON_PRESS,x= 7.0000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Pixel Selection
findWidget('OOF2:Pixel Selection Page:Pane').set_position(273)
checkpoint pixel page updated
checkpoint pixel page sensitized
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Invert
assert tests.pixelSelectionPageStatusCheck(8062, 10000, 80.62)
assert tests.pixelSelectionSizeCheck('composition.png', 8062)
assert tests.sensitization2()
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Undo
assert tests.pixelSelectionPageStatusCheck(1938, 10000, 19.38)
assert tests.pixelSelectionSizeCheck('composition.png', 1938)
assert tests.sensitization3()
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Clear
assert tests.pixelSelectionPageStatusCheck(0, 10000, 0)
assert tests.pixelSelectionSizeCheck('composition.png', 0)
assert tests.sensitization4()
event(Gdk.EventType.BUTTON_PRESS,x= 1.4700000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Select_Group
assert tests.pixelSelectionPageStatusCheck(1938, 10000, 19.38)
assert tests.pixelSelectionSizeCheck('composition.png', 1938)
findGfxWindow('Graphics_1').simulateMouse('down', 0.19025, 0.906, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.19025, 0.906, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.19025, 0.9095, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.19025, 0.9095, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.19025, 0.9095, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.19025, 0.9095, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
event(Gdk.EventType.BUTTON_PRESS,x= 6.9000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:New').clicked()
checkpoint toplevel widget mapped Dialog-Create new pixel group
findWidget('Dialog-Create new pixel group').resize(192, 92)
findWidget('Dialog-Create new pixel group:name').delete_text(0, 9)
findWidget('Dialog-Create new pixel group:name').insert_text('u', 11)
findWidget('Dialog-Create new pixel group:name').insert_text('p', 1)
findWidget('Dialog-Create new pixel group:name').insert_text('p', 2)
findWidget('Dialog-Create new pixel group:name').insert_text('e', 3)
findWidget('Dialog-Create new pixel group:name').insert_text('r', 4)
findWidget('Dialog-Create new pixel group:name').insert_text('l', 5)
findWidget('Dialog-Create new pixel group:name').insert_text('e', 6)
findWidget('Dialog-Create new pixel group:name').insert_text('f', 7)
findWidget('Dialog-Create new pixel group:name').insert_text('t', 8)
findWidget('Dialog-Create new pixel group:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.PixelGroup.New
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Add').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelGroup.AddSelection
event(Gdk.EventType.BUTTON_PRESS,x= 5.7000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Microstructure Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findWidget('chooserPopup-Microstructure').deactivate() # MenuLogger
event(Gdk.EventType.BUTTON_PRESS,x= 9.1000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Select_Group
event(Gdk.EventType.BUTTON_PRESS,x= 1.2400000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Add Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.2300000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Add Group:group').get_window())
checkpoint toplevel widget mapped chooserPopup-group
findMenu(findWidget('chooserPopup-group'), ['upperleft']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-group') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Add_Group
assert tests.pixelSelectionPageStatusCheck(3060, 10000, 30.6)
assert tests.pixelSelectionSizeCheck('composition.png', 3060)

event(Gdk.EventType.BUTTON_PRESS,x= 1.1200000000000e+02,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Unselect Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Unselect_Group
assert tests.pixelSelectionPageStatusCheck(1122, 10000, 11.22)
assert tests.pixelSelectionSizeCheck('composition.png', 1122)

findWidget('OOF2 Graphics 1').resize(800, 492)
event(Gdk.EventType.BUTTON_PRESS,x= 7.9000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('chooserPopup-TBChooser').deactivate() # MenuLogger
event(Gdk.EventType.BUTTON_PRESS,x= 9.1000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rectangle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findGfxWindow('Graphics_1').simulateMouse('down', 0.27775, 0.871, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.27425, 0.864, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.26725, 0.8465, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.25325, 0.8045, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.23925, 0.731, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.22875, 0.612, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.22875, 0.5665, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.23575, 0.5455, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.24625, 0.528, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.26375, 0.4965, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.29875, 0.444, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.38625, 0.409, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.49825, 0.381, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.56825, 0.3425, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.60325, 0.3145, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.63125, 0.2935, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.65225, 0.276, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68025, 0.248, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68025, 0.248, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68025, 0.248, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68025, 0.241, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('move', 0.68025, 0.241, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.68025, 0.241, 1, False, False)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle
assert tests.pixelSelectionSizeCheck('composition.png', 2688)
assert tests.pixelSelectionPageStatusCheck(2688, 10000, 26.88)
event(Gdk.EventType.BUTTON_PRESS,x= 1.4200000000000e+02,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Intersect Group']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Intersect_Group
assert tests.pixelSelectionPageStatusCheck(336, 10000, 3.36)
assert tests.pixelSelectionSizeCheck('composition.png', 336)
assert tests.sensitization5()
event(Gdk.EventType.BUTTON_PRESS,x= 1.1500000000000e+02,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Expand']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Expand
assert tests.pixelSelectionPageStatusCheck(412, 10000, 4.12)

event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Shrink']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Shrink:radius').set_text('')
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Shrink:radius').set_text('4')
checkpoint pixel page sensitized
checkpoint pixel page sensitized
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Shrink
assert tests.pixelSelectionPageStatusCheck(144, 10000, 1.44)
event(Gdk.EventType.BUTTON_PRESS,x= 9.5000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Color']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
event(Gdk.EventType.BUTTON_PRESS,x= 1.5400000000000e+02,y= 7.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Color Range']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2').resize(782, 652)
findWidget('OOF2:Pixel Selection Page:Pane').set_position(190)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 1.3888888888889e-02)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 7.8703703703704e-02)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 1.7592592592593e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 2.9166666666667e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 4.1203703703704e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 5.0000000000000e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 5.7407407407407e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 6.6203703703704e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 7.1296296296296e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 7.5925925925926e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 8.0555555555556e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 8.4259259259259e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 8.7500000000000e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 9.0277777777778e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 9.2592592592593e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 9.3518518518519e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 9.3981481481481e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 9.4444444444444e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 9.4907407407407e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 9.6296296296296e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 9.9537037037037e-01)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:reference:RGBColor:blue:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:range:DeltaRGB:delta_red:entry').set_text('0.')
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:range:DeltaRGB:delta_red:entry').set_text('0.0')
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:range:DeltaRGB:delta_red:entry').set_text('0.01')
widget_0=weakRef(findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:range:DeltaRGB:delta_red:entry'))
if widget_0(): wevent(widget_0(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0().get_window())
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:range:DeltaRGB:delta_green:entry').set_text('0.')
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:range:DeltaRGB:delta_green:entry').set_text('0.0')
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:range:DeltaRGB:delta_green:entry').set_text('0.01')
widget_1=weakRef(findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:range:DeltaRGB:delta_green:entry'))
if widget_1(): wevent(widget_1(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_1().get_window())
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:range:DeltaRGB:delta_blue:entry').set_text('0.')
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:range:DeltaRGB:delta_blue:entry').set_text('0.0')
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:range:DeltaRGB:delta_blue:entry').set_text('0.01')
widget_2=weakRef(findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Color Range:range:DeltaRGB:delta_blue:entry'))
if widget_2(): wevent(widget_2(), Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_2().get_window())
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Color_Range
assert tests.pixelSelectionPageStatusCheck(1428, 10000, 14.28)

findWidget('OOF2').resize(782, 652)
event(Gdk.EventType.BUTTON_PRESS,x= 4.0000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy microstructure
findWidget('Dialog-Copy microstructure').resize(192, 92)
findWidget('Dialog-Copy microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
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
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint OOF.Microstructure.Copy
event(Gdk.EventType.BUTTON_PRESS,x= 5.9000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
assert tests.chooserCheck('OOF2:Pixel Selection Page:Microstructure', ['composition.png', 'microstructure'])
assert tests.chooserStateCheck('OOF2:Pixel Selection Page:Microstructure', 'composition.png')
assert tests.pixelSelectionPageStatusCheck(1428, 10000, 14.28)
assert tests.pixelSelectionSizeCheck('microstructure', 0)
assert tests.pixelSelectionSizeCheck('composition.png', 1428)
event(Gdk.EventType.BUTTON_PRESS,x= 3.3000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
checkpoint pixel page updated
checkpoint pixel page sensitized
assert tests.pixelSelectionPageStatusCheck(0, 10000, 0)

findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Color_Range
findWidget('OOF2 Graphics 1').resize(800, 492)
assert tests.pixelSelectionPageStatusCheck(1428, 10000, 14.28)
assert tests.pixelSelectionSizeCheck('microstructure', 1428)

event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 4.9000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Skeleton Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['composition.png']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_OK').clicked()
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page sensitized
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
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint skeleton page info updated
checkpoint skeleton page info updated
checkpoint Solver page sensitized
checkpoint skeleton page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Skeleton.New
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
event(Gdk.EventType.BUTTON_PRESS,x= 9.4000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Element Pixels']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane').set_position(271)
event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Info']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Skeleton Info sensitized
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(243)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 1.8000000000000e+01)
event(Gdk.EventType.BUTTON_PRESS,x= 6.6000000000000e+01,y= 0.0000000000000e+00,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Skeleton Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(265)
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
findGfxWindow('Graphics_1').simulateMouse('down', 0.27425, 0.493, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.27425, 0.493, 1, False, False)
checkpoint Graphics_1 Element sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Single_Element
findWidget('OOF2 Messages 1').resize(542, 214)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
# 1903 pixel selected
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Select_Element_Pixels
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Clear
assert tests.pixelSelectionPageStatusCheck(0, 10000, 0)
assert tests.pixelSelectionSizeCheck('microstructure', 0)
assert tests.pixelSelectionSizeCheck('composition.png', 1428)
event(Gdk.EventType.BUTTON_PRESS,x= 6.6000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['composition.png']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
checkpoint pixel page updated
checkpoint pixel page sensitized
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Clear
assert tests.pixelSelectionPageStatusCheck(0, 10000, 0)
assert tests.pixelSelectionSizeCheck('composition.png', 0)

findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Select_Element_Pixels
assert tests.pixelSelectionPageStatusCheck(625, 10000, 6.25)
assert tests.pixelSelectionSizeCheck('composition.png', 625)

findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Element:Clear').clicked()
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint Graphics_1 Element sensitized
checkpoint selection info updated Element
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Element.Clear
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Skeleton Selection:Select:Segment').clicked()
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.41775, 0.745, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.41775, 0.745, 1, False, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.50175, 0.612, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.50175, 0.612, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
findGfxWindow('Graphics_1').simulateMouse('down', 0.62775, 0.507, 1, True, False)
findGfxWindow('Graphics_1').simulateMouse('up', 0.62775, 0.507, 1, True, False)
checkpoint Graphics_1 Segment sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment
event(Gdk.EventType.BUTTON_PRESS,x= 1.1800000000000e+02,y= 3.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Select Segment Pixels']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane').set_position(269)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Select_Segment_Pixels
assert tests.pixelSelectionSizeCheck('composition.png', 700)
assert tests.pixelSelectionPageStatusCheck(700, 10000, 7)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Clear').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Clear
assert tests.pixelSelectionSizeCheck('composition.png', 0)
assert tests.pixelSelectionPageStatusCheck(0, 10000, 0)

event(Gdk.EventType.BUTTON_PRESS,x= 4.2000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(196, 86)
findWidget('Questioner:Yes').clicked()
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
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
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
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
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
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.4000000000000e+01)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Materials page updated
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint skeleton selection page updated
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.Delete
findWidget('OOF2:Microstructure Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(207, 86)
findWidget('Questioner:Yes').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint Graphics_1 Skeleton Info sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint skeleton page sensitized
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page groups sensitized Element
checkpoint Graphics_1 Move Nodes sensitized
checkpoint Move Node toolbox writable changed
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
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint mesh bdy page updated
checkpoint Field page sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page subproblems sensitized
checkpoint mesh page sensitized
checkpoint boundary page updated
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint Field page sensitized
checkpoint pixel page sensitized
checkpoint Solver page sensitized
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint Graphics_1 Element sensitized
checkpoint Graphics_1 Segment sensitized
checkpoint contourmap info updated for Graphics_1
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
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint Solver page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint OOF.Microstructure.Delete
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Python_Log']).activate()
checkpoint toplevel widget mapped Dialog-Python_Log
findWidget('Dialog-Python_Log').resize(192, 122)
findWidget('Dialog-Python_Log:filename').set_text('s')
findWidget('Dialog-Python_Log:filename').set_text('ss')
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
assert tests.filediff('session.log')
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
