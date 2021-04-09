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
checkpoint meshable button set
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
checkpoint skeleton selection page grouplist Element
checkpoint skeleton selection page selection sensitized Element
checkpoint skeleton selection page updated
checkpoint skeleton selection page groups sensitized Element
checkpoint Solver page sensitized
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
findWidget('OOF2').resize(782, 545)
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Image
assert tests.sensitization0()
assert tests.chooserCheck('OOF2:Image Page:Microstructure', ['serendipity.png'])
assert tests.chooserCheck('OOF2:Image Page:Image', ['serendipity.png'])
assert tests.chooserStateCheck('OOF2:Image Page:Image', 'serendipity.png')
findWidget('OOF2:Image Page:Pane').set_position(546)
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
event(Gdk.EventType.BUTTON_PRESS,x= 5.4000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('Dialog-New Graphics Layer:category').get_window())
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
findWidget('OOF2 Graphics 1').resize(800, 492)
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
assert tests.sensitization1()
checkpoint OOF.Image.Modify.Gray
findWidget('OOF2:Image Page:Pane:Undo').clicked()
checkpoint contourmap info updated for Graphics_1
assert tests.sensitization2()
checkpoint OOF.Image.Undo
event(Gdk.EventType.BUTTON_PRESS,x= 6.3000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Flip']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
assert tests.sensitization3()
checkpoint OOF.Image.Modify.Flip
event(Gdk.EventType.BUTTON_PRESS,x= 5.8000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:Flip:axis').get_window())
checkpoint toplevel widget mapped chooserPopup-axis
findMenu(findWidget('chooserPopup-axis'), ['y']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-axis') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
assert tests.sensitization3()
checkpoint OOF.Image.Modify.Flip
findWidget('OOF2:Image Page:Pane:Undo').clicked()
checkpoint contourmap info updated for Graphics_1
assert tests.sensitization4()
checkpoint OOF.Image.Undo
findWidget('OOF2:Image Page:Pane:Undo').clicked()
checkpoint contourmap info updated for Graphics_1
assert tests.sensitization5()
checkpoint OOF.Image.Undo
findWidget('OOF2:Image Page:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy Image
findWidget('Dialog-Copy Image').resize(317, 134)
findWidget('Dialog-Copy Image:widget_GTK_RESPONSE_OK').clicked()
checkpoint microstructure page sensitized
checkpoint OOF.Image.Copy
assert tests.chooserCheck('OOF2:Image Page:Image', ['serendipity.png', 'serendipity.png<2>'])
assert tests.chooserStateCheck('OOF2:Image Page:Image', 'serendipity.png<2>')
findWidget('OOF2:Image Page:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy Image
findWidget('Dialog-Copy Image').resize(317, 134)
findWidget('Dialog-Copy Image:name').insert_text('c', 7)
findWidget('Dialog-Copy Image:name').insert_text('o', 1)
findWidget('Dialog-Copy Image:name').insert_text('p', 2)
findWidget('Dialog-Copy Image:name').insert_text('y', 3)
findWidget('Dialog-Copy Image:widget_GTK_RESPONSE_OK').clicked()
checkpoint microstructure page sensitized
checkpoint OOF.Image.Copy
assert tests.chooserCheck('OOF2:Image Page:Image', ['serendipity.png', 'serendipity.png<2>', 'copy'])
assert tests.chooserStateCheck('OOF2:Image Page:Image', 'copy')
event(Gdk.EventType.BUTTON_PRESS,x= 8.5000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findWidget('chooserPopup-Microstructure').deactivate() # MenuLogger
event(Gdk.EventType.BUTTON_PRESS,x= 7.5000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Image').get_window())
checkpoint toplevel widget mapped chooserPopup-Image
findMenu(findWidget('chooserPopup-Image'), ['serendipity.png<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Image') # MenuItemLogger
findWidget('OOF2:Image Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(222, 86)
findWidget('Questioner:Yes').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 2.0000000000000e+00)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
assert tests.sensitization5()
assert tests.chooserCheck('OOF2:Image Page:Image', ['serendipity.png', 'copy'])
assert tests.chooserStateCheck('OOF2:Image Page:Image', 'serendipity.png')
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Delete
findWidget('OOF2:Image Page:Group').clicked()
checkpoint toplevel widget mapped Dialog-AutoGroup
findWidget('Dialog-AutoGroup').resize(207, 92)
findWidget('Dialog-AutoGroup:widget_GTK_RESPONSE_OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.Image.AutoGroup
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Microstructure
assert tests.micro_sensitization()

checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Image
event(Gdk.EventType.BUTTON_PRESS,x= 4.7000000000000e+01,y= 8.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Blur']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Blur
findWidget('OOF2 Messages 1').resize(586, 237)
event(Gdk.EventType.BUTTON_PRESS,x= 5.6000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Dim']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane').set_position(508)
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Dim
event(Gdk.EventType.BUTTON_PRESS,x= 6.2000000000000e+01,y= 3.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Contrast']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane').set_position(546)
findWidget('OOF2:Image Page:Pane:Method:Contrast:sharpen').clicked()
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Contrast
findWidget('OOF2:Image Page:Pane:Undo').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Undo
findWidget('OOF2:Image Page:Pane:Method:Contrast:sharpen').clicked()
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Contrast
event(Gdk.EventType.BUTTON_PRESS,x= 5.7000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Despeckle']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Despeckle
event(Gdk.EventType.BUTTON_PRESS,x= 5.7000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Edge']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Edge
event(Gdk.EventType.BUTTON_PRESS,x= 5.2000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Enhance']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Enhance
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 1.5000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Equalize']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Equalize
event(Gdk.EventType.BUTTON_PRESS,x= 6.4000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['MedianFilter']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.MedianFilter
event(Gdk.EventType.BUTTON_PRESS,x= 4.9000000000000e+01,y= 1.4000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Negate']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Negate
event(Gdk.EventType.BUTTON_PRESS,x= 5.3000000000000e+01,y= 6.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Normalize']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Normalize
event(Gdk.EventType.BUTTON_PRESS,x= 6.1000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['ReduceNoise']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.ReduceNoise
event(Gdk.EventType.BUTTON_PRESS,x= 6.0000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Sharpen']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Sharpen
event(Gdk.EventType.BUTTON_PRESS,x= 6.5000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Reilluminate']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.Reilluminate
event(Gdk.EventType.BUTTON_PRESS,x= 8.0000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Pane:Method:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['ThresholdImage']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('OOF2:Image Page:Pane').set_position(531)
findWidget('OOF2:Image Page:Pane:OK').clicked()
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Modify.ThresholdImage
findWidget('OOF2:Navigation:Prev').clicked()
checkpoint page installed Microstructure
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('Dialog-Create Microstructure:widget_GTK_RESPONSE_OK').clicked()
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
checkpoint OOF.Microstructure.New
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Image
assert tests.chooserCheck('OOF2:Image Page:Microstructure', ['serendipity.png', 'microstructure'])
assert tests.chooserStateCheck('OOF2:Image Page:Microstructure', 'serendipity.png')
event(Gdk.EventType.BUTTON_PRESS,x= 7.1000000000000e+01,y= 1.0000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findWidget('chooserPopup-Microstructure').deactivate() # MenuLogger

findMenu(findWidget('chooserPopup-Microstructure'), ['microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
assert tests.chooserStateCheck('OOF2:Image Page:Microstructure', 'microstructure')
assert tests.chooserCheck('OOF2:Image Page:Image', [])
assert tests.sensitization6()

event(Gdk.EventType.BUTTON_PRESS,x= 6.0000000000000e+01,y= 9.0000000000000e+00,button=1,state=0,window=findWidget('OOF2:Image Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findWidget('chooserPopup-Microstructure').deactivate() # MenuLogger
findMenu(findWidget('chooserPopup-Microstructure'), ['serendipity.png']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
assert tests.sensitization3()
assert tests.chooserCheck('OOF2:Image Page:Image', ['serendipity.png', 'copy'])
assert tests.chooserStateCheck('OOF2:Image Page:Image', 'serendipity.png')
findWidget('OOF2:Image Page:Rename').clicked()
checkpoint toplevel widget mapped Dialog-Rename Image
findWidget('Dialog-Rename Image').resize(192, 92)
findWidget('Dialog-Rename Image:name').set_text('')
findWidget('Dialog-Rename Image:name').set_text('r')
findWidget('Dialog-Rename Image:name').set_text('re')
findWidget('Dialog-Rename Image:name').set_text('ren')
findWidget('Dialog-Rename Image:name').set_text('rena')
findWidget('Dialog-Rename Image:name').set_text('renam')
findWidget('Dialog-Rename Image:name').set_text('rename')
findWidget('Dialog-Rename Image:name').set_text('renamed')
findWidget('Dialog-Rename Image:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Image.Rename
assert tests.sensitization3()
assert tests.chooserCheck('OOF2:Image Page:Image', ['renamed', 'copy'])
assert tests.chooserStateCheck('OOF2:Image Page:Image', 'renamed')
findWidget('OOF2:Image Page:Save').clicked()
checkpoint toplevel widget mapped Dialog-Save Image
findWidget('Dialog-Save Image').resize(192, 116)
findWidget('Dialog-Save Image:filename').set_text('')
findWidget('Dialog-Save Image:filename').set_text('i')
findWidget('Dialog-Save Image:filename').set_text('im')
findWidget('Dialog-Save Image:filename').set_text('ima')
findWidget('Dialog-Save Image:filename').set_text('imag')
findWidget('Dialog-Save Image:filename').set_text('image')
findWidget('Dialog-Save Image:filename').set_text('image.')
findWidget('Dialog-Save Image:filename').set_text('image.p')
findWidget('Dialog-Save Image:filename').set_text('image.pp')
findWidget('Dialog-Save Image:filename').set_text('image.ppm')
findWidget('Dialog-Save Image:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Image
## This test has been be removed because the exact final image can
## depend upon which version of ImageMagick is being used.  In
## particular, the results using ImageMagick 6.9.11 on macOS 10.15.7
## differ from the results using ImageMagick 6.9.7 on Ubuntu 18.04 in
## a single pixel.
#assert tests.filediff('image.ppm')
findWidget('OOF2:Image Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(184, 86)
findWidget('Questioner:Yes').clicked()
findWidget('OOF2 Graphics 1:Pane0:LayerScroll').get_vadjustment().set_value( 0.0000000000000e+00)
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Element
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Delete
findWidget('OOF2:Image Page:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(184, 86)
findWidget('Questioner:Yes').clicked()
checkpoint Graphics_1 Pixel Info updated
checkpoint selection info updated Pixel Selection
checkpoint selection info updated Element
assert tests.sensitization6()
assert tests.chooserCheck('OOF2:Image Page:Image', [])
checkpoint Graphics_1 Pixel Selection sensitized
checkpoint selection info updated Node
checkpoint selection info updated Segment
checkpoint contourmap info updated for Graphics_1
checkpoint microstructure page sensitized
checkpoint Field page sensitized
checkpoint Solver page sensitized
checkpoint contourmap info updated for Graphics_1
checkpoint OOF.Image.Delete
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
