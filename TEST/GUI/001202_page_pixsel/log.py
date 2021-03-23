import tests
findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 545)
event(Gdk.EventType.BUTTON_PRESS,x= 8.6000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
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
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_s')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_sm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_sma')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_smal')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.pg')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.pgm')
findWidget('Dialog-Load Image and create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
checkpoint OOF.Microstructure.Create_From_ImageFile
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
checkpoint toplevel widget mapped Dialog-New
findWidget('Dialog-New').resize(395, 532)
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('Dialog-New:category').get_window())
checkpoint toplevel widget mapped chooserPopup-category
findMenu(findWidget('chooserPopup-category'), ['Image']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-category') # MenuItemLogger
findWidget('Dialog-New:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Layer.New
findWidget('OOF2 Graphics 1').resize(800, 492)
event(Gdk.EventType.BUTTON_PRESS,x= 6.4000000000000e+01,y= 1.8000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-TBChooser
findMenu(findWidget('chooserPopup-TBChooser'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-TBChooser') # MenuItemLogger
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2').set_position(249)
event(Gdk.EventType.BUTTON_PRESS,x= 6.6000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Burn']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 4.0000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll').get_hadjustment().set_value( 6.7000000000000e+01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:entry').set_text('0.14')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:entry').set_text('0.142')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:entry').set_text('0.1428')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:entry').set_text('0.14285')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:entry').set_text('0.142857')
widget_0=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:entry')
if widget_0: wevent(widget_0, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:global_flammability:entry').set_text('0.')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:global_flammability:entry').set_text('0.1')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:global_flammability:entry').set_text('0.14')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:global_flammability:entry').set_text('0.142')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:global_flammability:entry').set_text('0.1428')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:global_flammability:entry').set_text('0.14285')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:global_flammability:entry').set_text('0.142857')
findGfxWindow('Graphics_1').simulateMouse('down', 32.78225, 39.4485, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 32.78225, 39.4485, 1, False, False)
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
widget_1=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:global_flammability:entry')
if widget_1: wevent(widget_1, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_1.get_window())
del widget_1
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
event(Gdk.EventType.BUTTON_PRESS,x= 8.0000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Pixel Selection']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Pixel Selection
findWidget('OOF2:Pixel Selection Page:Pane').set_position(273)
checkpoint pixel page updated
checkpoint pixel page sensitized
assert tests.pixelSelectionPageStatusCheck(401, 8372)
event(Gdk.EventType.BUTTON_PRESS,x= 1.7200000000000e+02,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Despeckle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane').set_position(234)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Despeckle
assert tests.pixelSelectionPageStatusCheck(401, 8372)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 7.9810426540284e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 7.9431279620853e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 7.8862559241706e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 7.8293838862559e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 7.7914691943128e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 7.7535545023697e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 7.6966824644550e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 7.6777251184834e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 7.6966824644550e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Despeckle
assert tests.pixelSelectionPageStatusCheck(401, 8372)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:entry').set_text('')
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:entry').set_text('6')
checkpoint pixel page sensitized
checkpoint pixel page sensitized
widget_2=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:entry')
if widget_2: wevent(widget_2, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_2.get_window())
del widget_2
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Despeckle
assert tests.pixelSelectionPageStatusCheck(402, 8372)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:entry').set_text('')
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:entry').set_text('5')
checkpoint pixel page sensitized
checkpoint pixel page sensitized
widget_3=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:entry')
if widget_3: wevent(widget_3, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_3.get_window())
del widget_3
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Despeckle
assert tests.pixelSelectionPageStatusCheck(422, 8372)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 4.9668246445498e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 4.9289099526066e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 4.8909952606635e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 4.8530805687204e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 4.7962085308057e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 4.7772511848341e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 4.7582938388626e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 4.6824644549763e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 4.6445497630332e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 4.5687203791469e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 4.5308056872038e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Despeckle:neighbors:slider').get_adjustment().set_value( 4.5497630331754e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Despeckle
assert tests.pixelSelectionPageStatusCheck(1114, 8372)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:slider').get_adjustment().set_value( 1.2500000000000e-01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:slider').get_adjustment().set_value( 1.1111111111111e-01)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:slider').get_adjustment().set_value( 9.7222222222222e-02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:slider').get_adjustment().set_value( 9.0909090909091e-02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:slider').get_adjustment().set_value( 8.7121212121212e-02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:slider').get_adjustment().set_value( 8.3333333333333e-02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:slider').get_adjustment().set_value( 7.9545454545455e-02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:slider').get_adjustment().set_value( 7.5757575757576e-02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:slider').get_adjustment().set_value( 7.1969696969697e-02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:slider').get_adjustment().set_value( 6.8181818181818e-02)
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:entry').set_text('0.')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:entry').set_text('0.0')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:entry').set_text('0.04')
widget_4=findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:local_flammability:entry')
if widget_4: wevent(widget_4, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_4.get_window())
del widget_4
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:global_flammability:entry').set_text('0.')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:global_flammability:entry').set_text('0.0')
findWidget('OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:Method:Burn:global_flammability:entry').set_text('0.04')

findGfxWindow('Graphics_1').simulateMouse('down', 38.83375, 39.13, 1, False, False)
findGfxWindow('Graphics_1').simulateMouse('up', 38.83375, 39.13, 1, False, False)
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Graphics_1.Toolbox.Pixel_Select.Burn
assert tests.pixelSelectionPageStatusCheck(14, 8372)
event(Gdk.EventType.BUTTON_PRESS,x= 1.5000000000000e+02,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Elkcepsed']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Elkcepsed
assert tests.pixelSelectionPageStatusCheck(9, 8372)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.0331753554502e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.0758293838863e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.1469194312796e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.2180094786730e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.2748815165877e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3317535545024e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3459715639810e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3601895734597e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3744075829384e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3886255924171e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.4028436018957e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.4170616113744e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.4312796208531e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.4454976303318e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.4312796208531e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.4170616113744e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.4028436018957e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3886255924171e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3744075829384e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3459715639810e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3317535545024e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3459715639810e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3601895734597e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.4028436018957e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.4739336492891e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.5308056872038e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.5734597156398e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.6018957345972e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.6161137440758e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.6303317535545e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.6445497630332e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.6587677725118e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.6729857819905e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.6872037914692e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.7014218009479e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.7156398104265e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.7440758293839e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.8009478672986e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.8578199052133e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.8862559241706e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.9573459715640e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Undo
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Elkcepsed
assert tests.pixelSelectionPageStatusCheck(0, 8372)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint pixel page updated
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Undo
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.9857819905213e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.9715639810427e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.9573459715640e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.9146919431280e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.8436018957346e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.7298578199052e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.5876777251185e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3886255924171e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.3459715639810e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.2464454976303e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.2180094786730e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.2037914691943e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.1895734597156e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.1753554502370e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.1327014218009e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.0758293838863e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 3.0047393364929e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.9478672985782e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.9336492890995e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.9194312796209e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.9052132701422e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.8767772511848e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.8199052132701e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.7488151658768e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.6919431279621e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.6635071090047e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.6350710900474e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.6208530805687e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.6066350710900e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.5924170616114e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.5781990521327e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.5639810426540e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Elkcepsed
assert tests.pixelSelectionPageStatusCheck(12, 8372)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Undo').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Undo
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.5497630331754e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.5355450236967e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.4360189573460e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.3507109004739e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.1943127962085e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 2.1090047393365e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.9952606635071e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.9383886255924e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.8957345971564e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.8815165876777e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.8246445497630e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.7962085308057e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.7819905213270e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.7677725118483e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint pixel page sensitized
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Elkcepsed
assert tests.pixelSelectionPageStatusCheck(14, 8372)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.7393364928910e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.7251184834123e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.6398104265403e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.5118483412322e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.2132701421801e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.0142180094787e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:Method:Elkcepsed:neighbors:slider').get_adjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Pixel Selection Page:Pane:SelectionModification:OK').clicked()
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Pixel Selection
checkpoint pixel page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.PixelSelection.Elkcepsed
assert tests.pixelSelectionPageStatusCheck(14, 8372)
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
assert tests.filediff('session.log')
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint OOF.Graphics_1.File.Close
