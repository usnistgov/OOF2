# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# This test was copied from the old gtk2 test suite and updated. The
# old one doesn't have any assert statements, so presumably the test
# passes if the program doesn't crash.

import tests

checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
findWidget('OOF2').resize(782, 511)
event(Gdk.EventType.BUTTON_PRESS,x= 9.7000000000000e+01,y= 1.9000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint page installed Microstructure
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Microstructure Page:Pane').set_position(235)
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
findWidget('OOF2').resize(782, 545)
# load K1_small.pgm
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
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
# load cyallow.png
findWidget('OOF2:Microstructure Page:NewFromFile').clicked()
checkpoint toplevel widget mapped Dialog-Load Image and create Microstructure
findWidget('Dialog-Load Image and create Microstructure').resize(237, 200)
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.pg')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_small')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_smal')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_sma')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_sm')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_s')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1_')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K1')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/K')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/c')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cy')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cya')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyal')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyall')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallo')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallow')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallow.')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallow.p')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallow.pn')
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/cyallow.png')
findWidget('Dialog-Load Image and create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
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
checkpoint microstructure page sensitized
checkpoint OOF.Microstructure.Create_From_ImageFile
event(Gdk.EventType.BUTTON_PRESS,x= 7.7000000000000e+01,y= 1.7000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Image']).activate() # MenuItemLogger
checkpoint page installed Image
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Image Page:Pane').set_position(546)
event(Gdk.EventType.BUTTON_PRESS,x= 7.5000000000000e+01,y= 1.6000000000000e+01,button=1,state=0,window=findWidget('OOF2:Image Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['K1_small.pgm']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
findWidget('OOF2:Image Page:Load').clicked()
checkpoint toplevel widget mapped Dialog-Load Image
findWidget('Dialog-Load Image').resize(235, 200)
event(Gdk.EventType.BUTTON_PRESS,x= 9.5000000000000e+01,y= 1.1000000000000e+01,button=1,state=0,window=findWidget('Dialog-Load Image:microstructure:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['cyallow.png']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
findWidget('Dialog-Load Image:filename').set_text('')
findWidget('Dialog-Load Image:filename').set_text('e')
findWidget('Dialog-Load Image:filename').set_text('ex')
findWidget('Dialog-Load Image:filename').set_text('exa')
findWidget('Dialog-Load Image:filename').set_text('exam')
findWidget('Dialog-Load Image:filename').set_text('examp')
findWidget('Dialog-Load Image:filename').set_text('exampl')
findWidget('Dialog-Load Image:filename').set_text('example')
findWidget('Dialog-Load Image:filename').set_text('examples')
findWidget('Dialog-Load Image:filename').set_text('examples/')
findWidget('Dialog-Load Image:filename').set_text('examples/c')
findWidget('Dialog-Load Image:filename').set_text('examples/cy')
findWidget('Dialog-Load Image:filename').set_text('examples/cya')
findWidget('Dialog-Load Image:filename').set_text('examples/cyal')
findWidget('Dialog-Load Image:filename').set_text('examples/cyall')
findWidget('Dialog-Load Image:filename').set_text('examples/cyallo')
findWidget('Dialog-Load Image:filename').set_text('examples/cyallon')
findWidget('Dialog-Load Image:filename').set_text('examples/cyallong')
findWidget('Dialog-Load Image:filename').set_text('examples/cyallon')
findWidget('Dialog-Load Image:filename').set_text('examples/cyallo')
findWidget('Dialog-Load Image:filename').set_text('examples/cyallow')
findWidget('Dialog-Load Image:filename').set_text('examples/cyallow.')
findWidget('Dialog-Load Image:filename').set_text('examples/cyallow.p')
findWidget('Dialog-Load Image:filename').set_text('examples/cyallow.pn')
findWidget('Dialog-Load Image:filename').set_text('examples/cyallow.png')
findWidget('Dialog-Load Image:filename').set_text('examples/')
findWidget('Dialog-Load Image:filename').set_text('examples/K')
findWidget('Dialog-Load Image:filename').set_text('examples/K1')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_s')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_sm')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_sma')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_smal')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_small')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_small.')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_small.p')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_small.pn')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_small.png')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_small.pn')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_small.p')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_small.pg')
findWidget('Dialog-Load Image:filename').set_text('examples/K1_small.pgm')
event(Gdk.EventType.BUTTON_PRESS,x= 5.1000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-Load Image:microstructure:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['K1_small.pgm']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
findWidget('Dialog-Load Image:widget_GTK_RESPONSE_OK').clicked()
checkpoint microstructure page sensitized
checkpoint OOF.File.Load.Image
event(Gdk.EventType.BUTTON_PRESS,x= 7.7000000000000e+01,y= 1.2000000000000e+01,button=1,state=0,window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint page installed Microstructure
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Auto').clicked()
checkpoint toplevel widget mapped Dialog-AutoGroup
findWidget('Dialog-AutoGroup').resize(313, 392)
findWidget('Dialog-AutoGroup:minsize').set_text('10')
findWidget('Dialog-AutoGroup:widget_GTK_RESPONSE_OK').clicked()
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.AutoGroup
# group_0 (2160) group_1 (1440)
event(Gdk.EventType.BUTTON_PRESS,x= 3.5000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('OOF2:Microstructure Page:Microstructure').get_window())
checkpoint toplevel widget mapped chooserPopup-Microstructure
findMenu(findWidget('chooserPopup-Microstructure'), ['K1_small.pgm']).activate() # MenuItemLogger
checkpoint meshable button set
checkpoint microstructure page sensitized
deactivatePopup('chooserPopup-Microstructure') # MenuItemLogger
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Auto').clicked()
checkpoint toplevel widget mapped Dialog-AutoGroup
findWidget('Dialog-AutoGroup').resize(333, 392)
event(Gdk.EventType.BUTTON_PRESS,x= 7.4000000000000e+01,y= 1.3000000000000e+01,button=1,state=0,window=findWidget('Dialog-AutoGroup:grouper:Color:image:Image').get_window())
checkpoint toplevel widget mapped chooserPopup-Image
findMenu(findWidget('chooserPopup-Image'), ['K1_small.pgm<2>']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-Image') # MenuItemLogger
findWidget('Dialog-AutoGroup:minsize').set_text('0')
findWidget('Dialog-AutoGroup:minsize').set_text('40')
findWidget('Dialog-AutoGroup:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.AutoGroup
# group_0 (8298) group_1(74)
findWidget('OOF2:Microstructure Page:Pane:PixelGroups:Auto').clicked()
checkpoint toplevel widget mapped Dialog-AutoGroup
findWidget('Dialog-AutoGroup').resize(333, 392)
findWidget('Dialog-AutoGroup:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.PixelGroup.AutoGroup
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
