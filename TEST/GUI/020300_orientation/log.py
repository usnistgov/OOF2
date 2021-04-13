checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
checkpoint toplevel widget mapped OOF2 Activity Viewer
# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(587)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(94)
findWidget('OOF2 Messages 1').resize(449, 94)
findWidget('OOF2').resize(800, 520)
findWidget('OOF2 Messages 1').resize(449, 122)
findWidget('OOF2').resize(800, 520)

wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
findWidget('OOF2:Materials Page:Pane').set_position(305)
getTree('PropertyTree').simulateSelect('Orientation')
checkpoint Materials page updated
checkpoint property selected

# Open the Orientation property
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([5]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Orientation
findWidget('Dialog-Parametrize Orientation').resize(349, 201)
# Check the default value
assert tests.checkOrientation("Abg", alpha=0, beta=0, gamma=0)

# Switch to X
wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['X']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.checkOrientation("X", phi=0, theta=0, psi=0)

# Switch to XYZ
wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['XYZ']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.checkOrientation("XYZ", phi=0, theta=0, psi=0)

# Switch to Axis
wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Axis']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
findWidget('Dialog-Parametrize Orientation').resize(349, 232)
assert tests.checkOrientation("Axis", angle=0, x=0, y=0, z=1)

# Switch to Quaternion
wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Quaternion']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.checkOrientation("Quaternion", e0=1, e1=0, e2=0, e3=0)

# Switch to Rodrigues
wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rodrigues']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.checkOrientation("Rodrigues", r1=0, r2=0, r3=0)

# Switch to Bunge
wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Bunge']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.checkOrientation("Bunge", phi1=0, theta=0, phi2=0)

# Back to Abg
wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Abg']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.checkOrientation("Abg", alpha=0, beta=0, gamma=0)

# Set a value that earlier had failed to convert to XYZ properly:
# Abg(45, 105, 0)
findWidget('Dialog-Parametrize Orientation:angles:Abg:alpha:entry').set_text('')
findWidget('Dialog-Parametrize Orientation:angles:Abg:alpha:entry').set_text('4')
findWidget('Dialog-Parametrize Orientation:angles:Abg:alpha:entry').set_text('45')
widget_0=findWidget('Dialog-Parametrize Orientation:angles:Abg:alpha:entry')
if widget_0: wevent(widget_0, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
findWidget('Dialog-Parametrize Orientation:angles:Abg:beta:entry').set_text('-')
findWidget('Dialog-Parametrize Orientation:angles:Abg:beta:entry').set_text('')
findWidget('Dialog-Parametrize Orientation:angles:Abg:beta:entry').set_text('1')
findWidget('Dialog-Parametrize Orientation:angles:Abg:beta:entry').set_text('10')
findWidget('Dialog-Parametrize Orientation:angles:Abg:beta:entry').set_text('105')
widget_1=findWidget('Dialog-Parametrize Orientation:angles:Abg:beta:entry')
if widget_1: wevent(widget_1, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_1.get_window())
del widget_1
assert tests.checkOrientation("Abg", alpha=45, beta=105, gamma=0)

wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
widget_2=findWidget('Dialog-Parametrize Orientation:angles:Abg:beta:entry')
if widget_2: wevent(widget_2, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_2.get_window())
del widget_2
findMenu(findWidget('chooserPopup-RCFChooser'), ['X']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.checkOrientation("X", phi=-165, theta=45, psi=-90)

wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Abg']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.checkOrientation("Abg", alpha=45, beta=105, gamma=0)

findWidget('Dialog-Parametrize Orientation:angles:Abg:gamma:entry').set_text('')
findWidget('Dialog-Parametrize Orientation:angles:Abg:gamma:entry').set_text('0')
wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
widget_3=findWidget('Dialog-Parametrize Orientation:angles:Abg:gamma:entry')
if widget_3: wevent(widget_3, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_3.get_window())
del widget_3
findMenu(findWidget('chooserPopup-RCFChooser'), ['XYZ']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.checkOrientation("XYZ", phi=-44.007, theta=-10.5453, psi=100.729)

wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Axis']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
widget_4=findWidget('Dialog-Parametrize Orientation:angles:Axis:angle:entry')
if widget_4: wevent(widget_4, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_4.get_window())
del widget_4
widget_5=findWidget('Dialog-Parametrize Orientation:angles:Axis:angle:entry')
if widget_5: wevent(widget_5, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_5.get_window())
del widget_5
widget_6=findWidget('Dialog-Parametrize Orientation:angles:Axis:angle:entry')
if widget_6: wevent(widget_6, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_6.get_window())
del widget_6
assert tests.checkOrientation("Axis", angle=111.553, x=-0.3671784835763848, y=0.28174788198168854, z=0.8864525323994393)

wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Quaternion']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.checkOrientation("Quaternion", e0=0.5624225596255993, e1=-0.30360151625029885, e2=0.2329632263219369, e3= 0.7329632452834063)

wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findWidget('chooserPopup-RCFChooser').deactivate() # MenuLogger
wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findWidget('chooserPopup-RCFChooser').deactivate() # MenuLogger
wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Rodrigues']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.checkOrientation("Rodrigues", r1=-0.5398103455387784, r2=0.4142138723543005, r3=1.3032251867196347)

wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
findMenu(findWidget('chooserPopup-RCFChooser'), ['Bunge']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
widget_7=findWidget('Dialog-Parametrize Orientation:angles:Bunge:phi1:entry')
if widget_7: wevent(widget_7, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_7.get_window())
del widget_7
widget_8=findWidget('Dialog-Parametrize Orientation:angles:Bunge:phi1:entry')
if widget_8: wevent(widget_8, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_8.get_window())
del widget_8
widget_9=findWidget('Dialog-Parametrize Orientation:angles:Bunge:phi1:entry')
if widget_9: wevent(widget_9, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_9.get_window())
del widget_9
widget_10=findWidget('Dialog-Parametrize Orientation:angles:Bunge:theta:entry')
if widget_10: wevent(widget_10, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_10.get_window())
del widget_10
# The long chain of conversions adds error, so the tolerance has to be
# increased here.
assert tests.checkOrientation("Bunge", phi1=-90, theta=45, phi2=-15, tolerance=1.e-4)

wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
widget_11=findWidget('Dialog-Parametrize Orientation:angles:Bunge:theta:entry')
if widget_11: wevent(widget_11, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_11.get_window())
del widget_11
findWidget('chooserPopup-RCFChooser').deactivate() # MenuLogger
wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
widget_12=findWidget('Dialog-Parametrize Orientation:angles:Bunge:theta:entry')
if widget_12: wevent(widget_12, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_12.get_window())
del widget_12
findWidget('chooserPopup-RCFChooser').deactivate() # MenuLogger
wevent(findWidget('Dialog-Parametrize Orientation:angles:RCFChooser'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('Dialog-Parametrize Orientation:angles:RCFChooser').get_window())
checkpoint toplevel widget mapped chooserPopup-RCFChooser
widget_13=findWidget('Dialog-Parametrize Orientation:angles:Bunge:theta:entry')
if widget_13: wevent(widget_13, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_13.get_window())
del widget_13
findMenu(findWidget('chooserPopup-RCFChooser'), ['Abg']).activate() # MenuItemLogger
checkpoint convertible RCF
deactivatePopup('chooserPopup-RCFChooser') # MenuItemLogger
assert tests.checkOrientation("Abg", alpha=45, beta=105, gamma=0, tolerance=5.e-4)

findWidget('Dialog-Parametrize Orientation:widget_GTK_RESPONSE_CANCEL').clicked()
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
