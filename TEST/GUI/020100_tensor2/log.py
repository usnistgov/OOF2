# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Tests for second rank tensor widgets

import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)

# Create a material
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(289)
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('OOF2').resize(782, 545)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New

# Open Cubic thermal expansion
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Color')
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4, 0]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4, 0, 1]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Cubic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic').resize(309, 220)
widget_0=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_0: wevent(widget_0, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
widget_1=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_1: wevent(widget_1, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_1.get_window())
del widget_1
# Check initial values
assert tests.testAij("Cubic", a11=1.0, a22=1.0, a33=1.0)
assert tests.sensitiveAij("Cubic", a11=1)

# Change a_11 to 3
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0').set_text('3')
widget_2=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_2: wevent(widget_2, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_2.get_window())
del widget_2
assert tests.testAij("Cubic", a11=3.0, a22=3.0, a33=3.0)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Cubic
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open hexagonal thermal expansion
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Hexagonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal').resize(309, 220)
widget_3=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0')
if widget_3: wevent(widget_3, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_3.get_window())
del widget_3
widget_4=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0')
if widget_4: wevent(widget_4, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_4.get_window())
del widget_4
widget_5=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0')
if widget_5: wevent(widget_5, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_5.get_window())
del widget_5
# Check initial values
assert tests.testAij("Hexagonal", a11=1.0, a22=1.0, a33=0.5)
assert tests.sensitiveAij("Hexagonal", a11=1, a33=1)

# Change a_11 to 4
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0').set_text('4')
widget_6=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0')
if widget_6: wevent(widget_6, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_6.get_window())
del widget_6
widget_7=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:2,2')
if widget_7: wevent(widget_7, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_7.get_window())
del widget_7
widget_8=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:2,2')
if widget_8: wevent(widget_8, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_8.get_window())
del widget_8
widget_9=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:2,2')
if widget_9: wevent(widget_9, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_9.get_window())
del widget_9
assert tests.testAij("Hexagonal", a11=4.0, a22=4.0, a33=0.5)
# Change a_33 to 1

findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:2,2').set_text('1')
widget_10=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:2,2')
if widget_10: wevent(widget_10, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_10.get_window())
del widget_10
assert tests.testAij("Hexagonal", a11=4.0, a22=4.0, a33=1.0)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Hexagonal
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open trigonal thermal expansion
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Trigonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal').resize(309, 220)
widget_11=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0')
if widget_11: wevent(widget_11, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_11.get_window())
del widget_11
widget_12=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0')
if widget_12: wevent(widget_12, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_12.get_window())
del widget_12
widget_13=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0')
if widget_13: wevent(widget_13, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_13.get_window())
del widget_13
# Check initial values
assert tests.testAij("Trigonal", a11=1.0, a22=1.0, a33=0.5)
assert tests.sensitiveAij("Trigonal", a11=1, a33=1)

# Change a_11 to 5
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0').set_text('5')
widget_14=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0')
if widget_14: wevent(widget_14, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_14.get_window())
del widget_14
widget_15=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:2,2')
if widget_15: wevent(widget_15, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_15.get_window())
del widget_15
widget_16=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:2,2')
if widget_16: wevent(widget_16, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_16.get_window())
del widget_16
widget_17=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:2,2')
if widget_17: wevent(widget_17, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_17.get_window())
del widget_17
assert tests.testAij("Trigonal", a11=5.0, a22=5.0, a33=0.5)

# Change a_33 to 0.6
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:2,2').set_text('0.')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:2,2').set_text('0.6')
widget_18=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:2,2')
if widget_18: wevent(widget_18, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_18.get_window())
del widget_18
assert tests.testAij("Trigonal", a11=5.0, a22=5.0, a33=0.6)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Trigonal
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open tetragonal thermalexpansion
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Tetragonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 3]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal').resize(309, 220)
widget_19=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0')
if widget_19: wevent(widget_19, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_19.get_window())
del widget_19
widget_20=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0')
if widget_20: wevent(widget_20, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_20.get_window())
del widget_20
widget_21=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0')
if widget_21: wevent(widget_21, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_21.get_window())
del widget_21
# Check initial values
assert tests.testAij('Tetragonal', a11=1.0, a22=1.0, a33=0.5)
assert tests.sensitiveAij("Tetragonal", a11=1, a33=1)

# Change a_11 to 6
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0').set_text('6')
widget_22=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0')
if widget_22: wevent(widget_22, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_22.get_window())
del widget_22
widget_23=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:2,2')
if widget_23: wevent(widget_23, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_23.get_window())
del widget_23
widget_24=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:2,2')
if widget_24: wevent(widget_24, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_24.get_window())
del widget_24
widget_25=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:2,2')
if widget_25: wevent(widget_25, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_25.get_window())
del widget_25
assert tests.testAij('Tetragonal', a11=6.0, a22=6.0, a33=0.5)

# Change a_33 to 1
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:2,2').set_text('1')
widget_26=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:2,2')
if widget_26: wevent(widget_26, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_26.get_window())
del widget_26
assert tests.testAij('Tetragonal', a11=6.0, a22=6.0, a33=1.0)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Tetragonal
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open orthorhombic thermalexpansion
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Orthorhombic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 4]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic').resize(309, 220)
widget_27=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0')
if widget_27: wevent(widget_27, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_27.get_window())
del widget_27
widget_28=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0')
if widget_28: wevent(widget_28, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_28.get_window())
del widget_28
widget_29=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0')
if widget_29: wevent(widget_29, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_29.get_window())
del widget_29
# Check initial values
assert tests.testAij("Orthorhombic", a11=1.0, a22=1.0, a33=1.0)
assert tests.sensitiveAij("Orthorhombic", a11=1, a22=1, a33=1)

# Change a_11 to 3
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0').set_text('3')
widget_30=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0')
if widget_30: wevent(widget_30, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_30.get_window())
del widget_30
widget_31=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:1,1')
if widget_31: wevent(widget_31, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_31.get_window())
del widget_31
widget_32=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:1,1')
if widget_32: wevent(widget_32, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_32.get_window())
del widget_32
widget_33=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:1,1')
if widget_33: wevent(widget_33, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_33.get_window())
del widget_33
assert tests.testAij("Orthorhombic", a11=3.0, a22=1.0, a33=1.0)

# Change a_22 to 4
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:1,1').set_text('4')
widget_34=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:1,1')
if widget_34: wevent(widget_34, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_34.get_window())
del widget_34
widget_35=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:2,2')
if widget_35: wevent(widget_35, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_35.get_window())
del widget_35
widget_36=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:2,2')
if widget_36: wevent(widget_36, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_36.get_window())
del widget_36
widget_37=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:2,2')
if widget_37: wevent(widget_37, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_37.get_window())
del widget_37
assert tests.testAij("Orthorhombic", a11=3.0, a22=4.0, a33=1.0)

# Change a_33 to 5
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:2,2').set_text('5')
widget_38=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:2,2')
if widget_38: wevent(widget_38, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_38.get_window())
del widget_38
assert tests.testAij("Orthorhombic", a11=3.0, a22=4.0, a33=5.0)

# Save and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Orthorhombic
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open monoclinic thermalexpansion
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Monoclinic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 5]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic').resize(309, 220)
widget_39=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0')
if widget_39: wevent(widget_39, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_39.get_window())
del widget_39
widget_40=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0')
if widget_40: wevent(widget_40, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_40.get_window())
del widget_40
widget_41=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0')
if widget_41: wevent(widget_41, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_41.get_window())
del widget_41
# Check initial values
assert tests.testAij("Monoclinic", a11=1.0, a13=0.5, a22=1.0, a33=1.0)
assert tests.sensitiveAij("Monoclinic", a11=1, a13=1, a22=1, a33=1)

# Change a_11 to 2
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0').set_text('2')
widget_42=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0')
if widget_42: wevent(widget_42, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_42.get_window())
del widget_42
widget_43=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,2')
if widget_43: wevent(widget_43, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_43.get_window())
del widget_43
widget_44=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,2')
if widget_44: wevent(widget_44, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_44.get_window())
del widget_44
widget_45=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,2')
if widget_45: wevent(widget_45, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_45.get_window())
del widget_45
assert tests.testAij("Monoclinic", a11=2.0, a13=0.5, a22=1.0, a33=1.0)

# Change a_13 to 3
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,2').set_text('3')
widget_46=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,2')
if widget_46: wevent(widget_46, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_46.get_window())
del widget_46
widget_47=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:1,1')
if widget_47: wevent(widget_47, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_47.get_window())
del widget_47
widget_48=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:1,1')
if widget_48: wevent(widget_48, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_48.get_window())
del widget_48
widget_49=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:1,1')
if widget_49: wevent(widget_49, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_49.get_window())
del widget_49
assert tests.testAij("Monoclinic", a11=2.0, a13=3.0, a22=1.0, a33=1.0)

# Change a_22 to 4
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:1,1').set_text('4')
widget_50=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:1,1')
if widget_50: wevent(widget_50, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_50.get_window())
del widget_50
widget_51=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:2,2')
if widget_51: wevent(widget_51, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_51.get_window())
del widget_51
widget_52=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:2,2')
if widget_52: wevent(widget_52, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_52.get_window())
del widget_52
widget_53=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:2,2')
if widget_53: wevent(widget_53, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_53.get_window())
del widget_53
assert tests.testAij("Monoclinic", a11=2.0, a13=3.0, a22=4.0, a33=1.0)

# Change a_33 to 45
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:2,2').set_text('4')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:2,2').set_text('45')
widget_54=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:2,2')
if widget_54: wevent(widget_54, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_54.get_window())
del widget_54
assert tests.testAij("Monoclinic", a11=2.0, a13=3.0, a22=4.0, a33=45.0)
 
# Save and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Monoclinic
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open triclinic thermalexpansion
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Triclinic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 6]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic').resize(309, 220)
widget_55=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0')
if widget_55: wevent(widget_55, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_55.get_window())
del widget_55
widget_56=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0')
if widget_56: wevent(widget_56, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_56.get_window())
del widget_56
widget_57=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0')
if widget_57: wevent(widget_57, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_57.get_window())
del widget_57
# Check initial values
assert tests.testAij("Triclinic", a11=1.0, a22=1.0, a33=1.0)
assert tests.sensitiveAij("Triclinic", a11=1, a12=1, a13=1, a22=1, a23=1, a33=1)

# Change a_11 to 2
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic').resize(309, 220)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0').set_text('2')
widget_58=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0')
if widget_58: wevent(widget_58, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_58.get_window())
del widget_58
widget_59=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,1')
if widget_59: wevent(widget_59, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_59.get_window())
del widget_59
widget_60=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,1')
if widget_60: wevent(widget_60, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_60.get_window())
del widget_60
widget_61=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,1')
if widget_61: wevent(widget_61, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_61.get_window())
del widget_61
assert tests.testAij("Triclinic", a11=2.0, a22=1.0, a33=1.0)

# Change a_12 to 34
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,1').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,1').set_text('3')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,1').set_text('34')
widget_62=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,1')
if widget_62: wevent(widget_62, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_62.get_window())
del widget_62
widget_63=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,2')
if widget_63: wevent(widget_63, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_63.get_window())
del widget_63
widget_64=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,2')
if widget_64: wevent(widget_64, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_64.get_window())
del widget_64
widget_65=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,2')
if widget_65: wevent(widget_65, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_65.get_window())
del widget_65
assert tests.testAij("Triclinic", a11=2.0, a12=34.0, a22=1.0, a33=1.0)

# Change a_13 to 5
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,2').set_text('5')
widget_66=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,2')
if widget_66: wevent(widget_66, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_66.get_window())
del widget_66
widget_67=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,1')
if widget_67: wevent(widget_67, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_67.get_window())
del widget_67
widget_68=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,1')
if widget_68: wevent(widget_68, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_68.get_window())
del widget_68
widget_69=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,1')
if widget_69: wevent(widget_69, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_69.get_window())
del widget_69
assert tests.testAij("Triclinic", a11=2.0, a12=34.0, a13=5.0, a22=1.0, a33=1.0)

# Change a_22 to 6
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,1').set_text('6')
widget_70=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,1')
if widget_70: wevent(widget_70, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_70.get_window())
del widget_70
widget_71=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,2')
if widget_71: wevent(widget_71, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_71.get_window())
del widget_71
widget_72=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,2')
if widget_72: wevent(widget_72, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_72.get_window())
del widget_72
widget_73=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,2')
if widget_73: wevent(widget_73, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_73.get_window())
del widget_73
assert tests.testAij("Triclinic", a11=2.0, a12=34.0, a13=5.0, a22=6.0, a33=1.0)

# Change a_23 = 7
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,2').set_text('7')
widget_74=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:1,2')
if widget_74: wevent(widget_74, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_74.get_window())
del widget_74
widget_75=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:2,2')
if widget_75: wevent(widget_75, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_75.get_window())
del widget_75
widget_76=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:2,2')
if widget_76: wevent(widget_76, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_76.get_window())
del widget_76
widget_77=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:2,2')
if widget_77: wevent(widget_77, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_77.get_window())
del widget_77
assert tests.testAij("Triclinic", a11=2.0, a12=34.0, a13=5.0, a22=6.0, a23=7.0, a33=1.0)

# Change a_33 to 8
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:2,2').set_text('8')
widget_78=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:2,2')
if widget_78: wevent(widget_78, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_78.get_window())
del widget_78
assert tests.testAij("Triclinic", a11=2.0, a12=34.0, a13=5.0, a22=6.0, a23=7.0, a33=8.0)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Triclinic
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Save material to rank2mat.dat
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Materials']).activate()
checkpoint toplevel widget mapped Dialog-Materials
findWidget('Dialog-Materials').resize(192, 227)
findWidget('Dialog-Materials:filename').set_text('r')
findWidget('Dialog-Materials:filename').set_text('ra')
findWidget('Dialog-Materials:filename').set_text('ran')
findWidget('Dialog-Materials:filename').set_text('rank')
findWidget('Dialog-Materials:filename').set_text('rank2')
findWidget('Dialog-Materials:filename').set_text('rank2m')
findWidget('Dialog-Materials:filename').set_text('rank2ma')
findWidget('Dialog-Materials:filename').set_text('rank2mat')
findWidget('Dialog-Materials:filename').set_text('rank2mat.')
findWidget('Dialog-Materials:filename').set_text('rank2mat.d')
findWidget('Dialog-Materials:filename').set_text('rank2mat.da')
findWidget('Dialog-Materials:filename').set_text('rank2mat.dat')
findWidget('Dialog-Materials:materials').get_selection().unselect_all()
findWidget('Dialog-Materials:materials').get_selection().select_path(Gtk.TreePath([0]))
findWidget('Dialog-Materials:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Materials
assert tests.filediff('rank2mat.dat')

# Delete material
findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(192, 86)
findWidget('Questioner:OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.Delete

# Open cubic thermalexpansion and check for previous values
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Cubic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic').resize(309, 220)
widget_79=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_79: wevent(widget_79, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_79.get_window())
del widget_79
widget_80=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_80: wevent(widget_80, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_80.get_window())
del widget_80
widget_81=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_81: wevent(widget_81, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_81.get_window())
del widget_81
assert tests.testAij("Cubic", a11=3.0, a22=3.0, a33=3.0)

# Change a_00 to 5. 
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0').set_text('5')
widget_82=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_82: wevent(widget_82, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_82.get_window())
del widget_82
assert tests.testAij("Cubic", a11=5.0, a22=5.0, a33=5.0)
# Close dialog
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:widget_GTK_RESPONSE_CANCEL').clicked()

# Change all the moduli so that we can tell if the file is reloaded correctly.
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic').resize(309, 220)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0').set_text('0')
widget_83=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_83: wevent(widget_83, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_83.get_window())
del widget_83
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Cubic
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Hexagonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal').resize(309, 220)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0').set_text('0')
widget_84=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0')
if widget_84: wevent(widget_84, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_84.get_window())
del widget_84
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Hexagonal
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Trigonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal').resize(309, 220)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0').set_text('0')
widget_85=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0')
if widget_85: wevent(widget_85, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_85.get_window())
del widget_85
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Trigonal
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Tetragonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 3]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal').resize(309, 220)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0').set_text('0')
widget_86=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0')
if widget_86: wevent(widget_86, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_86.get_window())
del widget_86
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Tetragonal
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Orthorhombic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 4]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic').resize(309, 220)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0').set_text('0')
widget_87=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0')
if widget_87: wevent(widget_87, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_87.get_window())
del widget_87
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Orthorhombic
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 4]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic').resize(309, 220)
widget_88=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0')
if widget_88: wevent(widget_88, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_88.get_window())
del widget_88
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:widget_GTK_RESPONSE_CANCEL').clicked()
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Monoclinic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 5]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic').resize(309, 220)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0').set_text('0')
widget_89=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0')
if widget_89: wevent(widget_89, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_89.get_window())
del widget_89
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Monoclinic
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Triclinic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 6]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic').resize(309, 220)
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0').set_text('0')
widget_90=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0')
if widget_90: wevent(widget_90, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_90.get_window())
del widget_90
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.ThermalExpansion.Anisotropic.Triclinic

# Load the data file
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('r')
findWidget('Dialog-Data:filename').set_text('ra')
findWidget('Dialog-Data:filename').set_text('ran')
findWidget('Dialog-Data:filename').set_text('rank')
findWidget('Dialog-Data:filename').set_text('rank2')
findWidget('Dialog-Data:filename').set_text('rank2m')
findWidget('Dialog-Data:filename').set_text('rank2ma')
findWidget('Dialog-Data:filename').set_text('rank2mat')
findWidget('Dialog-Data:filename').set_text('rank2mat.')
findWidget('Dialog-Data:filename').set_text('rank2mat.d')
findWidget('Dialog-Data:filename').set_text('rank2mat.da')
findWidget('Dialog-Data:filename').set_text('rank2mat.dat')
findWidget('Dialog-Data:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.File.Load.Data

# Open cubic thermalexpansion
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Cubic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic').resize(309, 220)
widget_91=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_91: wevent(widget_91, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_91.get_window())
del widget_91
widget_92=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_92: wevent(widget_92, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_92.get_window())
del widget_92
widget_93=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_93: wevent(widget_93, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_93.get_window())
del widget_93
widget_94=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_94: wevent(widget_94, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_94.get_window())
del widget_94
assert tests.testAij("Cubic", a11=3.0, a22=3.0, a33=3.0)

widget_95=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:alpha:0,0')
if widget_95: wevent(widget_95, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_95.get_window())
del widget_95
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Cubic:widget_GTK_RESPONSE_CANCEL').clicked()

# Open hexagonal thermalexpansion
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Hexagonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal').resize(309, 220)
widget_96=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0')
if widget_96: wevent(widget_96, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_96.get_window())
del widget_96
widget_97=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0')
if widget_97: wevent(widget_97, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_97.get_window())
del widget_97
widget_98=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0')
if widget_98: wevent(widget_98, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_98.get_window())
del widget_98
widget_99=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0')
if widget_99: wevent(widget_99, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_99.get_window())
del widget_99
assert tests.testAij("Hexagonal", a11=4.0, a22=4.0, a33=1.0)
# Cancel
widget_100=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:alpha:0,0')
if widget_100: wevent(widget_100, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_100.get_window())
del widget_100
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Hexagonal:widget_GTK_RESPONSE_CANCEL').clicked()

# Open trigonal thermalexpansion
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Trigonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal').resize(309, 220)
widget_101=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0')
if widget_101: wevent(widget_101, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_101.get_window())
del widget_101
widget_102=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0')
if widget_102: wevent(widget_102, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_102.get_window())
del widget_102
widget_103=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0')
if widget_103: wevent(widget_103, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_103.get_window())
del widget_103
assert tests.testAij("Trigonal", a11=5.0, a22=5.0, a33=0.6)
# Cancel
widget_104=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:alpha:0,0')
if widget_104: wevent(widget_104, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_104.get_window())
del widget_104
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Trigonal:widget_GTK_RESPONSE_CANCEL').clicked()

# Open tetragonal thermalexpansion
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Tetragonal')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 3]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal').resize(309, 220)
widget_105=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0')
if widget_105: wevent(widget_105, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_105.get_window())
del widget_105
widget_106=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0')
if widget_106: wevent(widget_106, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_106.get_window())
del widget_106
widget_107=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0')
if widget_107: wevent(widget_107, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_107.get_window())
del widget_107
widget_108=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0')
if widget_108: wevent(widget_108, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_108.get_window())
del widget_108
assert tests.testAij('Tetragonal', a11=6.0, a22=6.0, a33=1.0)

widget_109=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:alpha:0,0')
if widget_109: wevent(widget_109, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_109.get_window())
del widget_109
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Tetragonal:widget_GTK_RESPONSE_CANCEL').clicked()

# Open orthorhombic thermalexpansion
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Orthorhombic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 4]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic').resize(309, 220)
widget_110=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0')
if widget_110: wevent(widget_110, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_110.get_window())
del widget_110
widget_111=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0')
if widget_111: wevent(widget_111, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_111.get_window())
del widget_111
widget_112=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0')
if widget_112: wevent(widget_112, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_112.get_window())
del widget_112
assert tests.testAij("Orthorhombic", a11=3.0, a22=4.0, a33=5.0)

# Cancel
widget_113=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:alpha:0,0')
if widget_113: wevent(widget_113, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_113.get_window())
del widget_113
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Orthorhombic:widget_GTK_RESPONSE_CANCEL').clicked()

# Open monoclinic thermalexpansion
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Monoclinic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 5]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic').resize(309, 220)
widget_114=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0')
if widget_114: wevent(widget_114, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_114.get_window())
del widget_114
widget_115=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0')
if widget_115: wevent(widget_115, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_115.get_window())
del widget_115
widget_116=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0')
if widget_116: wevent(widget_116, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_116.get_window())
del widget_116
assert tests.testAij("Monoclinic", a11=2.0, a13=3.0, a22=4.0, a33=45.0)

widget_117=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:alpha:0,0')
if widget_117: wevent(widget_117, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_117.get_window())
del widget_117
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Monoclinic:widget_GTK_RESPONSE_CANCEL').clicked()

# Open triclinic thermalexpansion
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:ThermalExpansion:Anisotropic:Triclinic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 0, 1, 6]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic').resize(309, 220)
widget_118=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0')
if widget_118: wevent(widget_118, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_118.get_window())
del widget_118
widget_119=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0')
if widget_119: wevent(widget_119, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_119.get_window())
del widget_119
widget_120=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0')
if widget_120: wevent(widget_120, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_120.get_window())
del widget_120
assert tests.testAij("Triclinic", a11=2.0, a12=34.0, a13=5.0, a22=6.0, a23=7.0, a33=8.0)

widget_121=findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:alpha:0,0')
if widget_121: wevent(widget_121, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_121.get_window())
del widget_121
findWidget('Dialog-Parametrize Couplings;ThermalExpansion;Anisotropic;Triclinic:widget_GTK_RESPONSE_CANCEL').clicked()

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
