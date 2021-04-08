# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


# Despite its name, the bug_activity_viewer test does not view the
# activity of bugs, but checks for the presence of an old activity
# viewer bug, involving incorrect order in the destruction of windows
# progress bars.  This test simply starts a progress bar and closes
# the activity viewer window before the progress bar is complete.  If
# the test runs to the end without raising an exception or crashing,
# it's successful.

# The task associated with the progress bar is auto-grouping a
# ridiculously large image.  This ensures, sort of, that the progress
# bar is not complete before the window is closed.

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 545)

findMenu(findWidget('OOF2:MenuBar'), ['Windows', 'Activity_Viewer']).activate()
checkpoint toplevel widget mapped OOF2 Activity Viewer
checkpoint OOF.Windows.Activity_Viewer
findWidget('OOF2 Activity Viewer').resize(400, 300)
findWidget('OOF2').resize(782, 545)
findMenu(findWidget('OOF2 Activity Viewer:MenuBar'), ['Settings', 'DelayProgressBarCreation']).activate()
checkpoint toplevel widget mapped Dialog-DelayProgressBarCreation
findWidget('Dialog-DelayProgressBarCreation').resize(192, 92)
findWidget('Dialog-DelayProgressBarCreation:milliseconds').set_text('')
findWidget('Dialog-DelayProgressBarCreation:milliseconds').set_text('0')
findWidget('Dialog-DelayProgressBarCreation:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.ActivityViewer.Settings.DelayProgressBarCreation

wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
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
findWidget('Dialog-Load Image and create Microstructure:filename').set_text('examples/big.ppm')
findWidget('Dialog-Load Image and create Microstructure:widget_GTK_RESPONSE_OK').clicked()
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint pixel page updated
checkpoint active area status updated
findWidget('OOF2:Microstructure Page:Pane').set_position(189)
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
findWidget('OOF2:Navigation:Next').clicked()
checkpoint page installed Image
findWidget('OOF2:Image Page:Pane').set_position(546)
findWidget('OOF2:Image Page:Group').clicked()
checkpoint toplevel widget mapped Dialog-AutoGroup
findWidget('Dialog-AutoGroup').resize(207, 92)
findWidget('Dialog-AutoGroup:widget_GTK_RESPONSE_OK').clicked()

event(Gdk.EventType.DELETE,window=findWidget('OOF2 Activity Viewer').get_window())
checkpoint OOF.ActivityViewer.File.Close

checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint skeleton selection page groups sensitized Element
checkpoint microstructure page sensitized
checkpoint meshable button set
checkpoint meshable button set
checkpoint microstructure page sensitized
checkpoint OOF.Image.AutoGroup
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(336, 86)
findWidget('Questioner:Don"t Save').clicked()
