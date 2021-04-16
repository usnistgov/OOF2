# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# If this test finishes, it passes.  It checks for a strange gtk/Field
# bug that only appeared on the Mac, with gtk+2.  If the user loaded a
# script that defined a Field, and then switched immediately to the
# Analysis page, gtk went into an infinite loop.  The test is probably
# irrelevannt in the gtk3 version, but there's no harm in running it.

# First, make sure that the script has loaded.
checkpoint OOF.Subproblem.Field.Define

# # # # # # # # # # # # # # # # # # 
#
# If the test hangs on the following line, it has failed.  Hit
# control-C in the terminal window to escape the infinite loop.
#
# # # # # # # # # # # # # # # # # # 

wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Analysis']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Analysis
findWidget('OOF2:Analysis Page:mainpane:bottom').set_position(320)
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(336, 86)
findWidget('Questioner:Don"t Save').clicked()
