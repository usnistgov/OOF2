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

wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(289)

# Open Cubic Piezoelectricity Td
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Color')
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4, 1]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4, 1, 0]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Cubic:Td')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td').resize(526, 184)
widget_0=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_0: wevent(widget_0, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_0.get_window())
del widget_0
widget_1=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_1: wevent(widget_1, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_1.get_window())
del widget_1
widget_2=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_2: wevent(widget_2, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_2.get_window())
del widget_2
assert tests.testDij("Cubic;Td", d14=1.0, d25=1.0, d36=1.0)
assert tests.sensitiveDij("Cubic;Td", d14=1)

# Change d_14 to 1.3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3').set_text('1.')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3').set_text('1.3')
widget_3=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_3: wevent(widget_3, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_3.get_window())
del widget_3
widget_4=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_4: wevent(widget_4, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_4.get_window())
del widget_4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td').resize(526, 184)
widget_5=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_5: wevent(widget_5, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_5.get_window())
del widget_5
assert tests.testDij("Cubic;Td", d14=1.3, d25=1.3, d36=1.3)

findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Cubic.Td
findWidget('OOF2:Materials Page:Pane:Material:New').clicked()
checkpoint toplevel widget mapped Dialog-New material
findWidget('Dialog-New material').resize(196, 122)
findWidget('Dialog-New material:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.New
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity hexagonal D3h
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4, 1, 1]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:D3h')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 1, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h').resize(526, 184)
widget_6=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1')
if widget_6: wevent(widget_6, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_6.get_window())
del widget_6
widget_7=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1')
if widget_7: wevent(widget_7, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_7.get_window())
del widget_7
widget_8=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1')
if widget_8: wevent(widget_8, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_8.get_window())
del widget_8
# Check initial values
assert tests.testDij("Hexagonal;D3h", d16=-2.0, d21=-1.0, d22=1.0)
assert tests.sensitiveDij("Hexagonal;D3h", d22=1)

findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1').set_text('3')
widget_9=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1')
if widget_9: wevent(widget_9, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_9.get_window())
del widget_9
assert tests.testDij("Hexagonal;D3h", d16=-6, d21=-3, d22=3)

findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Hexagonal.D3h
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity Hexagonal C6v
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:C6v')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 1, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v').resize(526, 184)
widget_10=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4')
if widget_10: wevent(widget_10, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_10.get_window())
del widget_10
widget_11=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4')
if widget_11: wevent(widget_11, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_11.get_window())
del widget_11
widget_12=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4')
if widget_12: wevent(widget_12, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_12.get_window())
del widget_12
# Check initial values
assert tests.testDij("Hexagonal;C6v", d15=1, d24=1, d31=1, d32=1, d33=1)
assert tests.sensitiveDij("Hexagonal;C6v", d15=1, d31=1, d33=1)

# Change d_15 to 2
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4').set_text('2')
widget_13=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4')
if widget_13: wevent(widget_13, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_13.get_window())
del widget_13
widget_14=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,0')
if widget_14: wevent(widget_14, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_14.get_window())
del widget_14
widget_15=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,0')
if widget_15: wevent(widget_15, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_15.get_window())
del widget_15
widget_16=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,0')
if widget_16: wevent(widget_16, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_16.get_window())
del widget_16
assert tests.testDij("Hexagonal;C6v", d15=2, d24=2, d31=1, d32=1, d33=1)

# Change d_31 to 3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,0').set_text('3')
widget_17=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,0')
if widget_17: wevent(widget_17, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_17.get_window())
del widget_17
widget_18=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,2')
if widget_18: wevent(widget_18, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_18.get_window())
del widget_18
widget_19=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,2')
if widget_19: wevent(widget_19, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_19.get_window())
del widget_19
widget_20=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,2')
if widget_20: wevent(widget_20, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_20.get_window())
del widget_20
assert tests.testDij("Hexagonal;C6v", d15=2, d24=2, d31=3, d32=3, d33=1)

# Change d_33 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,2').set_text('4')
widget_21=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,2')
if widget_21: wevent(widget_21, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_21.get_window())
del widget_21
widget_22=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,0')
if widget_22: wevent(widget_22, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_22.get_window())
del widget_22
widget_23=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,0')
if widget_23: wevent(widget_23, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_23.get_window())
del widget_23
widget_24=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,0')
if widget_24: wevent(widget_24, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_24.get_window())
del widget_24
assert tests.testDij("Hexagonal;C6v", d15=2, d24=2, d31=3, d32=3, d33=4)

# Save and add to material
widget_25=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:2,0')
if widget_25: wevent(widget_25, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_25.get_window())
del widget_25
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Hexagonal.C6v
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity hexagonal D6
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:D6')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6').resize(526, 184)
widget_26=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3')
if widget_26: wevent(widget_26, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_26.get_window())
del widget_26
widget_27=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3')
if widget_27: wevent(widget_27, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_27.get_window())
del widget_27
widget_28=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3')
if widget_28: wevent(widget_28, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_28.get_window())
del widget_28
# Check initial values
assert tests.testDij("Hexagonal;D6", d14=1, d25=-1)
assert tests.sensitiveDij("Hexagonal;D6", d14=1)

# Change d_14 to 5
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3').set_text('5')
widget_29=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3')
if widget_29: wevent(widget_29, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_29.get_window())
del widget_29
assert tests.testDij("Hexagonal;D6", d14=5, d25=-5)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Hexagonal.D6
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity hexagonal D6i
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:D6i')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i').resize(526, 184)
widget_30=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_30: wevent(widget_30, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_30.get_window())
del widget_30
widget_31=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_31: wevent(widget_31, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_31.get_window())
del widget_31
widget_32=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_32: wevent(widget_32, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_32.get_window())
del widget_32
# Check initial values
assert tests.testDij("Hexagonal;D6i", d11=1, d12=-1, d16=-2, d21=-1, d22=1, d26=-2)
assert tests.sensitiveDij("Hexagonal;D6i", d11=1, d22=1)

# Change d_11 to 3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0').set_text('3')
widget_33=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_33: wevent(widget_33, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_33.get_window())
del widget_33
widget_34=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:1,1')
if widget_34: wevent(widget_34, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_34.get_window())
del widget_34
widget_35=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:1,1')
if widget_35: wevent(widget_35, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_35.get_window())
del widget_35
widget_36=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:1,1')
if widget_36: wevent(widget_36, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_36.get_window())
del widget_36
assert tests.testDij("Hexagonal;D6i", d11=3, d12=-3, d16=-2, d21=-1, d22=1, d26=-6)

# Change d_22 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:1,1').set_text('4')
widget_37=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:1,1')
if widget_37: wevent(widget_37, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_37.get_window())
del widget_37
widget_38=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_38: wevent(widget_38, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_38.get_window())
del widget_38
widget_39=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_39: wevent(widget_39, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_39.get_window())
del widget_39
widget_40=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_40: wevent(widget_40, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_40.get_window())
del widget_40
assert tests.testDij("Hexagonal;D6i", d11=3, d12=-3, d16=-8, d21=-4, d22=4, d26=-6)

# Close and add to material
widget_41=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_41: wevent(widget_41, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_41.get_window())
del widget_41
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Hexagonal.D6i
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity hexagonal C6
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:C6')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6').resize(526, 184)
widget_42=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3')
if widget_42: wevent(widget_42, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_42.get_window())
del widget_42
widget_43=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3')
if widget_43: wevent(widget_43, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_43.get_window())
del widget_43
widget_44=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3')
if widget_44: wevent(widget_44, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_44.get_window())
del widget_44
assert tests.testDij("Hexagonal;C6", d14=1, d15=1, d24=1, d25=-1, d31=1, d32=1, d33=1)
assert tests.sensitiveDij("Hexagonal;C6", d14=1, d15=1, d31=1, d33=1)

# Change d_14 to 3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3').set_text('3')
widget_45=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3')
if widget_45: wevent(widget_45, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_45.get_window())
del widget_45
widget_46=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,4')
if widget_46: wevent(widget_46, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_46.get_window())
del widget_46
widget_47=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,4')
if widget_47: wevent(widget_47, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_47.get_window())
del widget_47
widget_48=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,4')
if widget_48: wevent(widget_48, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_48.get_window())
del widget_48
assert tests.testDij("Hexagonal;C6", d14=3, d15=1, d24=1, d25=-3, d31=1, d32=1, d33=1)

# Change d_15 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,4').set_text('4')
widget_49=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,4')
if widget_49: wevent(widget_49, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_49.get_window())
del widget_49
widget_50=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,0')
if widget_50: wevent(widget_50, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_50.get_window())
del widget_50
widget_51=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,0')
if widget_51: wevent(widget_51, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_51.get_window())
del widget_51
widget_52=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,0')
if widget_52: wevent(widget_52, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_52.get_window())
del widget_52
assert tests.testDij("Hexagonal;C6", d14=3, d15=4, d24=4, d25=-3, d31=1, d32=1, d33=1)

# Change d_31 to 5
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,0').set_text('5')
widget_53=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,0')
if widget_53: wevent(widget_53, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_53.get_window())
del widget_53
widget_54=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,2')
if widget_54: wevent(widget_54, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_54.get_window())
del widget_54
widget_55=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,2')
if widget_55: wevent(widget_55, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_55.get_window())
del widget_55
widget_56=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,2')
if widget_56: wevent(widget_56, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_56.get_window())
del widget_56
assert tests.testDij("Hexagonal;C6", d14=3, d15=4, d24=4, d25=-3, d31=5, d32=5, d33=1)

# Change d_33 to 6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,2').set_text('6')
widget_57=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,2')
if widget_57: wevent(widget_57, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_57.get_window())
del widget_57
widget_58=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,0')
if widget_58: wevent(widget_58, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_58.get_window())
del widget_58
widget_59=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,0')
if widget_59: wevent(widget_59, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_59.get_window())
del widget_59
widget_60=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,0')
if widget_60: wevent(widget_60, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_60.get_window())
del widget_60
assert tests.testDij("Hexagonal;C6", d14=3, d15=4, d24=4, d25=-3, d31=5, d32=5, d33=6)

# Save and add to material
widget_61=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:2,0')
if widget_61: wevent(widget_61, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_61.get_window())
del widget_61
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Hexagonal.C6
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity trigonal C3v
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4, 1, 2]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Trigonal:C3v')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 2, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v').resize(526, 184)
widget_62=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4')
if widget_62: wevent(widget_62, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_62.get_window())
del widget_62
widget_63=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4')
if widget_63: wevent(widget_63, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_63.get_window())
del widget_63
widget_64=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4')
if widget_64: wevent(widget_64, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_64.get_window())
del widget_64
assert tests.testDij("Trigonal;C3v", d15=1, d16=-2, d21=-1, d22=1, d24=1, d31=1, d32=1, d33=1)
assert tests.sensitiveDij("Trigonal;C3v", d15=1, d22=1, d31=1, d33=1)

# Change d_15 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4').set_text('4')
widget_65=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4')
if widget_65: wevent(widget_65, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_65.get_window())
del widget_65
widget_66=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:1,1')
if widget_66: wevent(widget_66, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_66.get_window())
del widget_66
widget_67=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:1,1')
if widget_67: wevent(widget_67, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_67.get_window())
del widget_67
widget_68=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:1,1')
if widget_68: wevent(widget_68, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_68.get_window())
del widget_68
assert tests.testDij("Trigonal;C3v", d15=4, d16=-2, d21=-1, d22=1, d24=4, d31=1, d32=1, d33=1)

# Change d_22 to 5
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:1,1').set_text('5')
widget_69=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:1,1')
if widget_69: wevent(widget_69, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_69.get_window())
del widget_69
widget_70=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,0')
if widget_70: wevent(widget_70, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_70.get_window())
del widget_70
widget_71=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,0')
if widget_71: wevent(widget_71, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_71.get_window())
del widget_71
widget_72=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,0')
if widget_72: wevent(widget_72, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_72.get_window())
del widget_72
assert tests.testDij("Trigonal;C3v", d15=4, d16=-10, d21=-5, d22=5, d24=4, d31=1, d32=1, d33=1)

# Change d_31 to 6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,0').set_text('6')
widget_73=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,0')
if widget_73: wevent(widget_73, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_73.get_window())
del widget_73
widget_74=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,2')
if widget_74: wevent(widget_74, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_74.get_window())
del widget_74
widget_75=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,2')
if widget_75: wevent(widget_75, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_75.get_window())
del widget_75
widget_76=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,2')
if widget_76: wevent(widget_76, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_76.get_window())
del widget_76
assert tests.testDij("Trigonal;C3v", d15=4, d16=-10, d21=-5, d22=5, d24=4, d31=6, d32=6, d33=1)

# Change d_33 to 7
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,2').set_text('7')
widget_77=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,2')
if widget_77: wevent(widget_77, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_77.get_window())
del widget_77
widget_78=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,0')
if widget_78: wevent(widget_78, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_78.get_window())
del widget_78
widget_79=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,0')
if widget_79: wevent(widget_79, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_79.get_window())
del widget_79
widget_80=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,0')
if widget_80: wevent(widget_80, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_80.get_window())
del widget_80
assert tests.testDij("Trigonal;C3v", d15=4, d16=-10, d21=-5, d22=5, d24=4, d31=6, d32=6, d33=7)

# Close and add to material
widget_81=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:2,0')
if widget_81: wevent(widget_81, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_81.get_window())
del widget_81
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Trigonal.C3v
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity Trigonal D3
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Trigonal:D3')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 2, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3').resize(526, 184)
widget_82=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0')
if widget_82: wevent(widget_82, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_82.get_window())
del widget_82
widget_83=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0')
if widget_83: wevent(widget_83, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_83.get_window())
del widget_83
widget_84=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0')
if widget_84: wevent(widget_84, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_84.get_window())
del widget_84
# check initial values
assert tests.testDij("Trigonal;D3", d11=1, d12=-1, d14=1, d25=-1, d26=-2)
assert tests.sensitiveDij("Trigonal;D3", d11=1, d14=1)

# Change d_11 to 3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0').set_text('3')
widget_85=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0')
if widget_85: wevent(widget_85, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_85.get_window())
del widget_85
widget_86=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,3')
if widget_86: wevent(widget_86, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_86.get_window())
del widget_86
widget_87=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,3')
if widget_87: wevent(widget_87, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_87.get_window())
del widget_87
widget_88=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,3')
if widget_88: wevent(widget_88, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_88.get_window())
del widget_88
widget_89=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,3')
if widget_89: wevent(widget_89, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_89.get_window())
del widget_89
assert tests.testDij("Trigonal;D3", d11=3, d12=-3, d14=1, d25=-1, d26=-6)

# Change d_14 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,3').set_text('4')
widget_90=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,3')
if widget_90: wevent(widget_90, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_90.get_window())
del widget_90
assert tests.testDij("Trigonal;D3", d11=3, d12=-3, d14=4, d25=-4, d26=-6)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Trigonal.D3
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity trigonal C3
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Trigonal:C3')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3').resize(526, 184)
widget_91=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0')
if widget_91: wevent(widget_91, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_91.get_window())
del widget_91
widget_92=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0')
if widget_92: wevent(widget_92, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_92.get_window())
del widget_92
widget_93=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0')
if widget_93: wevent(widget_93, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_93.get_window())
del widget_93
# Check initial values
assert tests.testDij("Trigonal;C3", d11=1, d12=-1, d14=1, d15=1, d16=-2, d21=-1, d22=1, d24=1, d25=-1, d26=-2, d31=1, d32=1, d33=1)
assert tests.sensitiveDij("Trigonal;C3", d11=1, d14=1, d15=1, d22=1, d31=1, d33=1)

# Change d_11 to 3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0').set_text('3')
widget_94=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0')
if widget_94: wevent(widget_94, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_94.get_window())
del widget_94
widget_95=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,3')
if widget_95: wevent(widget_95, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_95.get_window())
del widget_95
widget_96=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,3')
if widget_96: wevent(widget_96, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_96.get_window())
del widget_96
widget_97=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,3')
if widget_97: wevent(widget_97, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_97.get_window())
del widget_97
assert tests.testDij("Trigonal;C3", d11=3, d12=-3, d14=1, d15=1, d16=-2, d21=-1, d22=1, d24=1, d25=-1, d26=-6, d31=1, d32=1, d33=1)

# Change d_14 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,3').set_text('4')
widget_98=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,3')
if widget_98: wevent(widget_98, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_98.get_window())
del widget_98
widget_99=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,4')
if widget_99: wevent(widget_99, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_99.get_window())
del widget_99
widget_100=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,4')
if widget_100: wevent(widget_100, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_100.get_window())
del widget_100
widget_101=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,4')
if widget_101: wevent(widget_101, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_101.get_window())
del widget_101
widget_102=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,4')
if widget_102: wevent(widget_102, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_102.get_window())
del widget_102
assert tests.testDij("Trigonal;C3", d11=3, d12=-3, d14=4, d15=1, d16=-2, d21=-1, d22=1, d24=1, d25=-4, d26=-6, d31=1, d32=1, d33=1)

# Change d_15 to 5
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,4').set_text('5')
widget_103=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,4')
if widget_103: wevent(widget_103, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_103.get_window())
del widget_103
widget_104=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:1,1')
if widget_104: wevent(widget_104, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_104.get_window())
del widget_104
widget_105=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:1,1')
if widget_105: wevent(widget_105, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_105.get_window())
del widget_105
widget_106=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:1,1')
if widget_106: wevent(widget_106, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_106.get_window())
del widget_106
assert tests.testDij("Trigonal;C3", d11=3, d12=-3, d14=4, d15=5, d16=-2, d21=-1, d22=1, d24=5, d25=-4, d26=-6, d31=1, d32=1, d33=1)

# Change d_22 to 6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:1,1').set_text('6')
widget_107=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:1,1')
if widget_107: wevent(widget_107, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_107.get_window())
del widget_107
widget_108=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:1,1')
if widget_108: wevent(widget_108, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_108.get_window())
del widget_108
widget_109=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:1,1')
if widget_109: wevent(widget_109, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_109.get_window())
del widget_109
assert tests.testDij("Trigonal;C3", d11=3, d12=-3, d14=4, d15=5, d16=-12, d21=-6, d22=6, d24=5, d25=-4, d26=-6, d31=1, d32=1, d33=1)

# Change d_31 to 7
widget_110=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:1,1')
if widget_110: wevent(widget_110, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_110.get_window())
del widget_110
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:2,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:2,0').set_text('7')
widget_111=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:2,0')
if widget_111: wevent(widget_111, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_111.get_window())
del widget_111
widget_112=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:2,2')
if widget_112: wevent(widget_112, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_112.get_window())
del widget_112
widget_113=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:2,2')
if widget_113: wevent(widget_113, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_113.get_window())
del widget_113
widget_114=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:2,2')
if widget_114: wevent(widget_114, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_114.get_window())
del widget_114
assert tests.testDij("Trigonal;C3", d11=3, d12=-3, d14=4, d15=5, d16=-12, d21=-6, d22=6, d24=5, d25=-4, d26=-6, d31=7, d32=7, d33=1)

# Change d_33 to 8
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:2,2').set_text('8')
widget_115=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:2,2')
if widget_115: wevent(widget_115, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_115.get_window())
del widget_115
assert tests.testDij("Trigonal;C3", d11=3, d12=-3, d14=4, d15=5, d16=-12, d21=-6, d22=6, d24=5, d25=-4, d26=-6, d31=7, d32=7, d33=8)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Trigonal.C3
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity tetragonal D2d
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.5000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.7000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.9000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.1000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.3000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.6000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.7000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.9000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.0000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.1000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.2000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.4000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.6000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.8000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.9000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.0000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.1000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.3000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4, 1, 3]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.2145038167939e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.3725190839695e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.5305343511450e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.8465648854962e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.0045801526718e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.3206106870229e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.9526717557252e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.2687022900763e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.9007633587786e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.2167938931298e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.8488549618321e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.1648854961832e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.6389312977099e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.9549618320611e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0429007633588e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0587022900763e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1061068702290e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1377099236641e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2009160305344e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2799236641221e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3115267175573e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3747328244275e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4221374045802e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5327480916031e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5801526717557e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6433587786260e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6591603053435e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6749618320611e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6849618320611e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6907633587786e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7065648854962e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7165648854962e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7223664122137e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7323664122137e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7381679389313e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7481679389313e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7381679389313e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7539694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7639694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7539694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7639694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7539694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7639694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7839694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7639694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7439694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7139694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7539694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7339694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7539694656489e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7439694656489e+02)
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:D2d')
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7436613355754e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7427991992526e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7420842847218e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7402356096639e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7400000000000e+02)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d').resize(526, 184)
widget_116=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3')
if widget_116: wevent(widget_116, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_116.get_window())
del widget_116
widget_117=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3')
if widget_117: wevent(widget_117, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_117.get_window())
del widget_117
widget_118=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3')
if widget_118: wevent(widget_118, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_118.get_window())
del widget_118
# Check initial values
assert tests.testDij("Tetragonal;D2d", d14=1, d25=1, d36=1)
assert tests.sensitiveDij("Tetragonal;D2d", d14=1, d36=1)

# Change d_14 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3').set_text('4')
widget_119=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3')
if widget_119: wevent(widget_119, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_119.get_window())
del widget_119
widget_120=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:2,5')
if widget_120: wevent(widget_120, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_120.get_window())
del widget_120
widget_121=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:2,5')
if widget_121: wevent(widget_121, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_121.get_window())
del widget_121
widget_122=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:2,5')
if widget_122: wevent(widget_122, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_122.get_window())
del widget_122
assert tests.testDij("Tetragonal;D2d", d14=4, d25=4, d36=1)

# Change d_36 to 5
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:2,5').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:2,5').set_text('5')
widget_123=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:2,5')
if widget_123: wevent(widget_123, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_123.get_window())
del widget_123
assert tests.testDij("Tetragonal;D2d", d14=4, d25=4, d36=5)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Tetragonal.D2d

findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity tetragonal C4v
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:C4v')
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7600000000000e+02)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7300000000000e+02)
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v').resize(526, 184)
widget_124=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4')
if widget_124: wevent(widget_124, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_124.get_window())
del widget_124
widget_125=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4')
if widget_125: wevent(widget_125, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_125.get_window())
del widget_125
widget_126=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4')
if widget_126: wevent(widget_126, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_126.get_window())
del widget_126
# Check initial values
assert tests.testDij("Tetragonal;C4v", d15=1, d24=1, d31=1, d32=1, d33=1)
assert tests.sensitiveDij("Tetragonal;C4v", d15=1, d31=1, d33=1)

# Change d_15 to 3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4').set_text('3')
widget_127=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4')
if widget_127: wevent(widget_127, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_127.get_window())
del widget_127
widget_128=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:2,0')
if widget_128: wevent(widget_128, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_128.get_window())
del widget_128
widget_129=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:2,0')
if widget_129: wevent(widget_129, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_129.get_window())
del widget_129
widget_130=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:2,0')
if widget_130: wevent(widget_130, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_130.get_window())
del widget_130
assert tests.testDij("Tetragonal;C4v", d15=3, d24=3, d31=1, d32=1, d33=1)

# Change d_31 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:2,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:2,0').set_text('4')
widget_131=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:2,0')
if widget_131: wevent(widget_131, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_131.get_window())
del widget_131
widget_132=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:2,2')
if widget_132: wevent(widget_132, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_132.get_window())
del widget_132
widget_133=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:2,2')
if widget_133: wevent(widget_133, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_133.get_window())
del widget_133
widget_134=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:2,2')
if widget_134: wevent(widget_134, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_134.get_window())
del widget_134
assert tests.testDij("Tetragonal;C4v", d15=3, d24=3, d31=4, d32=4, d33=1)

# Change d_33 to 5
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:2,2').set_text('5')
widget_135=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:2,2')
if widget_135: wevent(widget_135, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_135.get_window())
del widget_135
assert tests.testDij("Tetragonal;C4v", d15=3, d24=3, d31=4, d32=4, d33=5)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Tetragonal.C4v
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity tetragonal D4
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:D4')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4').resize(526, 184)
widget_136=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3')
if widget_136: wevent(widget_136, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_136.get_window())
del widget_136
widget_137=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3')
if widget_137: wevent(widget_137, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_137.get_window())
del widget_137
widget_138=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3')
if widget_138: wevent(widget_138, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_138.get_window())
del widget_138
# Check initial values
assert tests.testDij("Tetragonal;D4", d14=1, d25=-1)
assert tests.sensitiveDij("Tetragonal;D4", d14=1)

# Change d_14 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3').set_text('4')
widget_139=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3')
if widget_139: wevent(widget_139, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_139.get_window())
del widget_139
assert tests.testDij("Tetragonal;D4", d14=4, d25=-4)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Tetragonal.D4
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity tetragonal C4i
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:C4i')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i').resize(526, 184)
widget_140=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_140: wevent(widget_140, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_140.get_window())
del widget_140
widget_141=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_141: wevent(widget_141, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_141.get_window())
del widget_141
widget_142=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_142: wevent(widget_142, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_142.get_window())
del widget_142
# Check initial values
assert tests.testDij("Tetragonal;C4i", d14=1, d15=1, d24=-1, d25=1, d31=1, d32=-1, d36=1)
assert tests.sensitiveDij("Tetragonal;C4i", d14=1, d15=1, d31=1, d36=1)

# Change d_14 to 3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3').set_text('3')
widget_143=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_143: wevent(widget_143, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_143.get_window())
del widget_143
widget_144=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,4')
if widget_144: wevent(widget_144, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_144.get_window())
del widget_144
widget_145=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,4')
if widget_145: wevent(widget_145, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_145.get_window())
del widget_145
widget_146=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,4')
if widget_146: wevent(widget_146, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_146.get_window())
del widget_146
assert tests.testDij("Tetragonal;C4i", d14=3, d15=1, d24=-1, d25=3, d31=1, d32=-1, d36=1)

# Change d_15 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,4').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,4').set_text('4')
widget_147=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,4')
if widget_147: wevent(widget_147, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_147.get_window())
del widget_147
widget_148=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:2,0')
if widget_148: wevent(widget_148, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_148.get_window())
del widget_148
widget_149=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:2,0')
if widget_149: wevent(widget_149, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_149.get_window())
del widget_149
widget_150=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:2,0')
if widget_150: wevent(widget_150, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_150.get_window())
del widget_150
assert tests.testDij("Tetragonal;C4i", d14=3, d15=4, d24=-4, d25=3, d31=1, d32=-1, d36=1)

# Change d_31 to 5
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:2,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:2,0').set_text('5')
widget_151=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:2,0')
if widget_151: wevent(widget_151, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_151.get_window())
del widget_151
widget_152=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:2,5')
if widget_152: wevent(widget_152, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_152.get_window())
del widget_152
widget_153=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:2,5')
if widget_153: wevent(widget_153, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_153.get_window())
del widget_153
widget_154=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:2,5')
if widget_154: wevent(widget_154, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_154.get_window())
del widget_154
assert tests.testDij("Tetragonal;C4i", d14=3, d15=4, d24=-4, d25=3, d31=5, d32=-5, d36=1)

# Change d_36 to 6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:2,5').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:2,5').set_text('6')
widget_155=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:2,5')
if widget_155: wevent(widget_155, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_155.get_window())
del widget_155
assert tests.testDij("Tetragonal;C4i", d14=3, d15=4, d24=-4, d25=3, d31=5, d32=-5, d36=6)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Tetragonal.C4i
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity tetragonal C4
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:C4')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 4]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4').resize(526, 184)
widget_156=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3')
if widget_156: wevent(widget_156, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_156.get_window())
del widget_156
widget_157=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3')
if widget_157: wevent(widget_157, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_157.get_window())
del widget_157
widget_158=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3')
if widget_158: wevent(widget_158, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_158.get_window())
del widget_158
# Check initial values
assert tests.testDij("Tetragonal;C4", d14=1, d15=1, d24=1, d25=-1, d31=1, d32=1, d33=1)
assert tests.sensitiveDij("Tetragonal;C4", d14=1, d15=1, d31=1, d33=1)

# Change d_14 to 3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3').set_text('3')
widget_159=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3')
if widget_159: wevent(widget_159, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_159.get_window())
del widget_159
widget_160=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,4')
if widget_160: wevent(widget_160, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_160.get_window())
del widget_160
widget_161=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,4')
if widget_161: wevent(widget_161, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_161.get_window())
del widget_161
widget_162=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,4')
if widget_162: wevent(widget_162, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_162.get_window())
del widget_162
assert tests.testDij("Tetragonal;C4", d14=3, d15=1, d24=1, d25=-3, d31=1, d32=1, d33=1)

# Change d_15 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,4').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,4').set_text('4')
widget_163=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,4')
if widget_163: wevent(widget_163, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_163.get_window())
del widget_163
widget_164=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:2,0')
if widget_164: wevent(widget_164, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_164.get_window())
del widget_164
widget_165=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:2,0')
if widget_165: wevent(widget_165, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_165.get_window())
del widget_165
widget_166=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:2,0')
if widget_166: wevent(widget_166, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_166.get_window())
del widget_166
assert tests.testDij("Tetragonal;C4", d14=3, d15=4, d24=4, d25=-3, d31=1, d32=1, d33=1)

# Change d_31 to 5
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:2,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:2,0').set_text('5')
widget_167=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:2,0')
if widget_167: wevent(widget_167, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_167.get_window())
del widget_167
widget_168=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:2,2')
if widget_168: wevent(widget_168, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_168.get_window())
del widget_168
widget_169=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:2,2')
if widget_169: wevent(widget_169, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_169.get_window())
del widget_169
widget_170=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:2,2')
if widget_170: wevent(widget_170, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_170.get_window())
del widget_170
assert tests.testDij("Tetragonal;C4", d14=3, d15=4, d24=4, d25=-3, d31=5, d32=5, d33=1)

# Change d_33 to 6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:2,2').set_text('6')
widget_171=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:2,2')
if widget_171: wevent(widget_171, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_171.get_window())
del widget_171
assert tests.testDij("Tetragonal;C4", d14=3, d15=4, d24=4, d25=-3, d31=5, d32=5, d33=6)

# Save and add to material
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Tetragonal.C4
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity orthorhombic C2v
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateUnselect()
checkpoint Materials page updated
checkpoint property deselected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').collapse_row(Gtk.TreePath([4, 1, 3]))
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4, 1, 4]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Orthorhombic:C2v')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 4, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v').resize(526, 184)
widget_172=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:0,4')
if widget_172: wevent(widget_172, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_172.get_window())
del widget_172
widget_173=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:0,4')
if widget_173: wevent(widget_173, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_173.get_window())
del widget_173
widget_174=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:0,4')
if widget_174: wevent(widget_174, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_174.get_window())
del widget_174
# Check initial values
assert tests.testDij("Orthorhombic;C2v", d15=1, d24=1, d31=1, d32=1, d33=1)
assert tests.sensitiveDij("Orthorhombic;C2v", d15=1, d24=1, d31=1, d32=1, d33=1)

# Change d_15 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:0,4').set_text('4')
widget_175=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:0,4')
if widget_175: wevent(widget_175, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_175.get_window())
del widget_175
widget_176=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:1,3')
if widget_176: wevent(widget_176, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_176.get_window())
del widget_176
widget_177=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:1,3')
if widget_177: wevent(widget_177, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_177.get_window())
del widget_177
widget_178=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:1,3')
if widget_178: wevent(widget_178, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_178.get_window())
del widget_178
assert tests.testDij("Orthorhombic;C2v", d15=4, d24=1, d31=1, d32=1, d33=1)

# Change d_24 to 5
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:1,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:1,3').set_text('5')
widget_179=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:1,3')
if widget_179: wevent(widget_179, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_179.get_window())
del widget_179
widget_180=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,0')
if widget_180: wevent(widget_180, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_180.get_window())
del widget_180
widget_181=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,0')
if widget_181: wevent(widget_181, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_181.get_window())
del widget_181
widget_182=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,0')
if widget_182: wevent(widget_182, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_182.get_window())
del widget_182
assert tests.testDij("Orthorhombic;C2v", d15=4, d24=5, d31=1, d32=1, d33=1)

# Change d_31 to 6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,0').set_text('6')
widget_183=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,0')
if widget_183: wevent(widget_183, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_183.get_window())
del widget_183
widget_184=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,1')
if widget_184: wevent(widget_184, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_184.get_window())
del widget_184
widget_185=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,1')
if widget_185: wevent(widget_185, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_185.get_window())
del widget_185
widget_186=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,1')
if widget_186: wevent(widget_186, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_186.get_window())
del widget_186
assert tests.testDij("Orthorhombic;C2v", d15=4, d24=5, d31=6, d32=1, d33=1)

# Change d_32 to 7
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,1').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,1').set_text('7')
widget_187=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,1')
if widget_187: wevent(widget_187, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_187.get_window())
del widget_187
widget_188=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,2')
if widget_188: wevent(widget_188, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_188.get_window())
del widget_188
widget_189=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,2')
if widget_189: wevent(widget_189, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_189.get_window())
del widget_189
widget_190=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,2')
if widget_190: wevent(widget_190, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_190.get_window())
del widget_190
assert tests.testDij("Orthorhombic;C2v", d15=4, d24=5, d31=6, d32=7, d33=1)

# Change d_33 to 8
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,2').set_text('8')
widget_191=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:2,2')
if widget_191: wevent(widget_191, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_191.get_window())
del widget_191
assert tests.testDij("Orthorhombic;C2v", d15=4, d24=5, d31=6, d32=7, d33=8)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Orthorhombic.C2v
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property

# Open piezoelectricity orthorhombic D2
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Orthorhombic:D2')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2').resize(526, 184)
widget_192=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3')
if widget_192: wevent(widget_192, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_192.get_window())
del widget_192
widget_193=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3')
if widget_193: wevent(widget_193, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_193.get_window())
del widget_193
widget_194=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3')
if widget_194: wevent(widget_194, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_194.get_window())
del widget_194
# Check initial values
assert tests.testDij("Orthorhombic;D2", d14=1, d25=1, d36=1)
assert tests.sensitiveDij("Orthorhombic;D2", d14=1, d25=1, d36=1)

# Change d_14 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3').set_text('4')
widget_195=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3')
if widget_195: wevent(widget_195, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_195.get_window())
del widget_195
widget_196=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:1,4')
if widget_196: wevent(widget_196, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_196.get_window())
del widget_196
widget_197=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:1,4')
if widget_197: wevent(widget_197, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_197.get_window())
del widget_197
widget_198=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:1,4')
if widget_198: wevent(widget_198, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_198.get_window())
del widget_198
assert tests.testDij("Orthorhombic;D2", d14=4, d25=1, d36=1)

# Change d_25 to 5
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:1,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:1,4').set_text('5')
widget_199=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:1,4')
if widget_199: wevent(widget_199, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_199.get_window())
del widget_199
widget_200=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:2,5')
if widget_200: wevent(widget_200, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_200.get_window())
del widget_200
widget_201=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:2,5')
if widget_201: wevent(widget_201, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_201.get_window())
del widget_201
widget_202=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:2,5')
if widget_202: wevent(widget_202, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_202.get_window())
del widget_202
assert tests.testDij("Orthorhombic;D2", d14=4, d25=5, d36=1)

# Change d_36 to 6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:2,5').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:2,5').set_text('6')
widget_203=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:2,5')
if widget_203: wevent(widget_203, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_203.get_window())
del widget_203
assert tests.testDij("Orthorhombic;D2", d14=4, d25=5, d36=6)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Orthorhombic.D2
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 9.0000000000000e+00)

# Open piezoelectricity monoclinic Cs
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4, 1, 5]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Monoclinic:Cs')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 5, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs').resize(526, 184)
widget_204=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0')
if widget_204: wevent(widget_204, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_204.get_window())
del widget_204
widget_205=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0')
if widget_205: wevent(widget_205, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_205.get_window())
del widget_205
widget_206=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0')
if widget_206: wevent(widget_206, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_206.get_window())
del widget_206
# Check initial values
assert tests.testDij("Monoclinic;Cs", d11=1, d12=1, d13=1, d15=1, d24=1, d26=1, d31=1, d32=1, d33=1, d35=1)
assert tests.sensitiveDij("Monoclinic;Cs", d11=1, d12=1, d13=1, d15=1, d24=1, d26=1, d31=1, d32=1, d33=1, d35=1)

# Change d_11 to 3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0').set_text('3')
widget_207=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0')
if widget_207: wevent(widget_207, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_207.get_window())
del widget_207
widget_208=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,1')
if widget_208: wevent(widget_208, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_208.get_window())
del widget_208
widget_209=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,1')
if widget_209: wevent(widget_209, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_209.get_window())
del widget_209
widget_210=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,1')
if widget_210: wevent(widget_210, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_210.get_window())
del widget_210
assert tests.testDij("Monoclinic;Cs", d11=3, d12=1, d13=1, d15=1, d24=1, d26=1, d31=1, d32=1, d33=1, d35=1)

# Change d_12 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,1').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,1').set_text('4')
widget_211=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,1')
if widget_211: wevent(widget_211, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_211.get_window())
del widget_211
widget_212=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,2')
if widget_212: wevent(widget_212, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_212.get_window())
del widget_212
widget_213=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,2')
if widget_213: wevent(widget_213, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_213.get_window())
del widget_213
widget_214=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,2')
if widget_214: wevent(widget_214, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_214.get_window())
del widget_214
assert tests.testDij("Monoclinic;Cs", d11=3, d12=4, d13=1, d15=1, d24=1, d26=1, d31=1, d32=1, d33=1, d35=1)

# Change d_13 to 5
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,2').set_text('5')
widget_215=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,2')
if widget_215: wevent(widget_215, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_215.get_window())
del widget_215
widget_216=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,4')
if widget_216: wevent(widget_216, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_216.get_window())
del widget_216
widget_217=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,4')
if widget_217: wevent(widget_217, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_217.get_window())
del widget_217
widget_218=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,4')
if widget_218: wevent(widget_218, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_218.get_window())
del widget_218
assert tests.testDij("Monoclinic;Cs", d11=3, d12=4, d13=5, d15=1, d24=1, d26=1, d31=1, d32=1, d33=1, d35=1)

# Change d_15 to 6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,4').set_text('6')
widget_219=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,4')
if widget_219: wevent(widget_219, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_219.get_window())
del widget_219
widget_220=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:1,3')
if widget_220: wevent(widget_220, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_220.get_window())
del widget_220
widget_221=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:1,3')
if widget_221: wevent(widget_221, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_221.get_window())
del widget_221
widget_222=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:1,3')
if widget_222: wevent(widget_222, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_222.get_window())
del widget_222
assert tests.testDij("Monoclinic;Cs", d11=3, d12=4, d13=5, d15=6, d24=1, d26=1, d31=1, d32=1, d33=1, d35=1)

# Change d_24 to 7
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:1,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:1,3').set_text('7')
widget_223=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:1,3')
if widget_223: wevent(widget_223, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_223.get_window())
del widget_223
assert tests.testDij("Monoclinic;Cs", d11=3, d12=4, d13=5, d15=6, d24=7, d26=1, d31=1, d32=1, d33=1, d35=1)

# Change d_26 to 8
widget_226=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0')
if widget_226: wevent(widget_226, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_226.get_window())
del widget_226
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:1,5').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:1,5').set_text('8')
widget_227=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:1,5')
if widget_227: wevent(widget_227, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_227.get_window())
del widget_227
widget_228=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,0')
if widget_228: wevent(widget_228, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_228.get_window())
del widget_228
widget_229=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,0')
if widget_229: wevent(widget_229, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_229.get_window())
del widget_229
widget_230=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,0')
if widget_230: wevent(widget_230, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_230.get_window())
del widget_230
widget_231=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,0')
if widget_231: wevent(widget_231, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_231.get_window())
del widget_231
assert tests.testDij("Monoclinic;Cs", d11=3, d12=4, d13=5, d15=6, d24=7, d26=8, d31=1, d32=1, d33=1, d35=1)

# Change d_31 to 9
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,0').set_text('9')
widget_232=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,0')
if widget_232: wevent(widget_232, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_232.get_window())
del widget_232
widget_233=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,1')
if widget_233: wevent(widget_233, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_233.get_window())
del widget_233
widget_234=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,1')
if widget_234: wevent(widget_234, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_234.get_window())
del widget_234
widget_235=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,1')
if widget_235: wevent(widget_235, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_235.get_window())
del widget_235
assert tests.testDij("Monoclinic;Cs", d11=3, d12=4, d13=5, d15=6, d24=7, d26=8, d31=9, d32=1, d33=1, d35=1)

# Change d_32 to 10
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,1').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,1').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,1').set_text('10')
widget_236=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,1')
if widget_236: wevent(widget_236, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_236.get_window())
del widget_236
widget_237=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,2')
if widget_237: wevent(widget_237, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_237.get_window())
del widget_237
widget_238=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,2')
if widget_238: wevent(widget_238, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_238.get_window())
del widget_238
widget_239=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,2')
if widget_239: wevent(widget_239, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_239.get_window())
del widget_239
assert tests.testDij("Monoclinic;Cs", d11=3, d12=4, d13=5, d15=6, d24=7, d26=8, d31=9, d32=10, d33=1, d35=1)

# Change d_33 to 11
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,2').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,2').set_text('11')
widget_240=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,2')
if widget_240: wevent(widget_240, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_240.get_window())
del widget_240
widget_241=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,4')
if widget_241: wevent(widget_241, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_241.get_window())
del widget_241
widget_242=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,4')
if widget_242: wevent(widget_242, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_242.get_window())
del widget_242
widget_243=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,4')
if widget_243: wevent(widget_243, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_243.get_window())
del widget_243
assert tests.testDij("Monoclinic;Cs", d11=3, d12=4, d13=5, d15=6, d24=7, d26=8, d31=9, d32=10, d33=11, d35=1)

# Change d_35 to 12
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,4').set_text('1.')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,4').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,4').set_text('12')
widget_244=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:2,4')
if widget_244: wevent(widget_244, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_244.get_window())
del widget_244
assert tests.testDij("Monoclinic;Cs", d11=3, d12=4, d13=5, d15=6, d24=7, d26=8, d31=9, d32=10, d33=11, d35=12)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Monoclinic.Cs
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 2.7000000000000e+01)

# Open piezoelectricity monoclinic C2
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Monoclinic:C2')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1900000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2100000000000e+02)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 5, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2').resize(526, 184)
widget_245=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3')
if widget_245: wevent(widget_245, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_245.get_window())
del widget_245
widget_246=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3')
if widget_246: wevent(widget_246, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_246.get_window())
del widget_246
widget_247=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3')
if widget_247: wevent(widget_247, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_247.get_window())
del widget_247
# Check initial values
assert tests.testDij("Monoclinic;C2", d14=1, d16=1, d21=1, d22=1, d23=1, d25=1, d34=1, d36=1)
assert tests.sensitiveDij("Monoclinic;C2", d14=1, d16=1, d21=1, d22=1, d23=1, d25=1, d34=1, d36=1)

# Change d_14 to 2
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3').set_text('2')
widget_248=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3')
if widget_248: wevent(widget_248, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_248.get_window())
del widget_248
widget_249=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,5')
if widget_249: wevent(widget_249, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_249.get_window())
del widget_249
widget_250=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,5')
if widget_250: wevent(widget_250, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_250.get_window())
del widget_250
widget_251=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,5')
if widget_251: wevent(widget_251, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_251.get_window())
del widget_251
widget_252=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,5')
if widget_252: wevent(widget_252, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_252.get_window())
del widget_252
assert tests.testDij("Monoclinic;C2", d14=2, d16=1, d21=1, d22=1, d23=1, d25=1, d34=1, d36=1)

# Change d_16 to 3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,5').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,5').set_text('3')
widget_253=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,5')
if widget_253: wevent(widget_253, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_253.get_window())
del widget_253
widget_254=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,0')
if widget_254: wevent(widget_254, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_254.get_window())
del widget_254
widget_255=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,0')
if widget_255: wevent(widget_255, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_255.get_window())
del widget_255
widget_256=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,0')
if widget_256: wevent(widget_256, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_256.get_window())
del widget_256
assert tests.testDij("Monoclinic;C2", d14=2, d16=3, d21=1, d22=1, d23=1, d25=1, d34=1, d36=1)

# Change d_21 to 4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,0').set_text('4')
widget_257=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,0')
if widget_257: wevent(widget_257, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_257.get_window())
del widget_257
widget_258=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,1')
if widget_258: wevent(widget_258, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_258.get_window())
del widget_258
widget_259=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,1')
if widget_259: wevent(widget_259, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_259.get_window())
del widget_259
widget_260=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,1')
if widget_260: wevent(widget_260, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_260.get_window())
del widget_260
assert tests.testDij("Monoclinic;C2", d14=2, d16=3, d21=4, d22=1, d23=1, d25=1, d34=1, d36=1)

# Change d_22 to 5
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,1').set_text('5')
widget_261=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,1')
if widget_261: wevent(widget_261, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_261.get_window())
del widget_261
widget_262=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,2')
if widget_262: wevent(widget_262, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_262.get_window())
del widget_262
widget_263=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,2')
if widget_263: wevent(widget_263, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_263.get_window())
del widget_263
widget_264=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,2')
if widget_264: wevent(widget_264, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_264.get_window())
del widget_264
assert tests.testDij("Monoclinic;C2", d14=2, d16=3, d21=4, d22=5, d23=1, d25=1, d34=1, d36=1)

# Change d_23 to 6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,2').set_text('6')
widget_265=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,2')
if widget_265: wevent(widget_265, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_265.get_window())
del widget_265
widget_266=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,4')
if widget_266: wevent(widget_266, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_266.get_window())
del widget_266
widget_267=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,4')
if widget_267: wevent(widget_267, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_267.get_window())
del widget_267
widget_268=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,4')
if widget_268: wevent(widget_268, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_268.get_window())
del widget_268
assert tests.testDij("Monoclinic;C2", d14=2, d16=3, d21=4, d22=5, d23=6, d25=1, d34=1, d36=1)

# Change d_25 to 7
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,4').set_text('7')
widget_269=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:1,4')
if widget_269: wevent(widget_269, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_269.get_window())
del widget_269
widget_270=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:2,3')
if widget_270: wevent(widget_270, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_270.get_window())
del widget_270
widget_271=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:2,3')
if widget_271: wevent(widget_271, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_271.get_window())
del widget_271
widget_272=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:2,3')
if widget_272: wevent(widget_272, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_272.get_window())
del widget_272
assert tests.testDij("Monoclinic;C2", d14=2, d16=3, d21=4, d22=5, d23=6, d25=7, d34=1, d36=1)

# Change d_34 to 8
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:2,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:2,3').set_text('8')
widget_273=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:2,3')
if widget_273: wevent(widget_273, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_273.get_window())
del widget_273
widget_274=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:2,5')
if widget_274: wevent(widget_274, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_274.get_window())
del widget_274
widget_275=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:2,5')
if widget_275: wevent(widget_275, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_275.get_window())
del widget_275
widget_276=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:2,5')
if widget_276: wevent(widget_276, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_276.get_window())
del widget_276
assert tests.testDij("Monoclinic;C2", d14=2, d16=3, d21=4, d22=5, d23=6, d25=7, d34=8, d36=1)

# Change d_36 to 9
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:2,5').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:2,5').set_text('9')
widget_277=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:2,5')
if widget_277: wevent(widget_277, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_277.get_window())
del widget_277
assert tests.testDij("Monoclinic;C2", d14=2, d16=3, d21=4, d22=5, d23=6, d25=7, d34=8, d36=9)

# Close and add to material
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Monoclinic.C2
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 9.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 4.5000000000000e+01)

# Open piezoelectricity triclinic C1
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2500000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2900000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6500000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6900000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7900000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4, 1, 6]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Triclinic:C1')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 6, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1').resize(526, 184)
widget_278=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
if widget_278: wevent(widget_278, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_278.get_window())
del widget_278
widget_279=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
if widget_279: wevent(widget_279, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_279.get_window())
del widget_279
widget_280=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
if widget_280: wevent(widget_280, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_280.get_window())
del widget_280
# Check initial values
assert tests.testDij("Triclinic;C1", d11=1, d12=1, d13=1, d14=1, d15=1, d16=1, d21=1, d22=1, d23=1, d24=1, d25=1, d26=1, d31=1, d32=1, d33=1, d34=1, d35=1, d36=1)
assert tests.sensitiveDij("Triclinic;C1", d11=1, d12=1, d13=1, d14=1, d15=1, d16=1, d21=1, d22=1, d23=1, d24=1, d25=1, d26=1, d31=1, d32=1, d33=1, d34=1, d35=1, d36=1)

# Change d_11 to 2
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0').set_text('2')
widget_281=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
if widget_281: wevent(widget_281, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_281.get_window())
del widget_281
widget_282=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,1')
if widget_282: wevent(widget_282, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_282.get_window())
del widget_282
widget_283=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,1')
if widget_283: wevent(widget_283, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_283.get_window())
del widget_283
widget_284=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,1')
if widget_284: wevent(widget_284, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_284.get_window())
del widget_284
assert tests.testDij("Triclinic;C1", d11=2, d12=1, d13=1, d14=1, d15=1, d16=1, d21=1, d22=1, d23=1, d24=1, d25=1, d26=1, d31=1, d32=1, d33=1, d34=1, d35=1, d36=1)

# Change d_12 to 3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,1').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,1').set_text('3')
widget_285=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,1')
if widget_285: wevent(widget_285, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_285.get_window())
del widget_285
# findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:widget_GTK_RESPONSE_OK').clicked()
# checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Triclinic.C1
# wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
# tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
# column = tree.get_column(0)
# tree.row_activated(Gtk.TreePath([4, 1, 6, 0]), column)
# checkpoint Materials page updated
# checkpoint property selected
# checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1
# findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1').resize(526, 184)
# widget_286=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
# if widget_286: wevent(widget_286, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_286.get_window())
# del widget_286
# widget_287=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
# if widget_287: wevent(widget_287, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_287.get_window())
# del widget_287
# widget_288=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
# if widget_288: wevent(widget_288, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_288.get_window())
# del widget_288
# # DELETE BACK TO GTK_RESPONSE_OK
widget_289=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
if widget_289: wevent(widget_289, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_289.get_window())
del widget_289
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,2').set_text('4')
widget_290=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,2')
if widget_290: wevent(widget_290, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_290.get_window())
del widget_290
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,3').set_text('5')
widget_291=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,3')
if widget_291: wevent(widget_291, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_291.get_window())
del widget_291
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,4').set_text('6')
widget_292=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,4')
if widget_292: wevent(widget_292, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_292.get_window())
del widget_292
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,5').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,5').set_text('7')
widget_293=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,5')
if widget_293: wevent(widget_293, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_293.get_window())
del widget_293
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,0').set_text('8')
widget_294=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,0')
if widget_294: wevent(widget_294, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_294.get_window())
del widget_294
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,1').set_text('9')
widget_295=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,1')
if widget_295: wevent(widget_295, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_295.get_window())
del widget_295
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,2').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,2').set_text('10')
widget_296=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,2')
if widget_296: wevent(widget_296, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_296.get_window())
del widget_296
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,3').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,3').set_text('11')
widget_297=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,3')
if widget_297: wevent(widget_297, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_297.get_window())
del widget_297
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,4').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,4').set_text('12')
widget_298=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,4')
if widget_298: wevent(widget_298, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_298.get_window())
del widget_298
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,5').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,5').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,5').set_text('13')
widget_299=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:1,5')
if widget_299: wevent(widget_299, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_299.get_window())
del widget_299
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,0').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,0').set_text('14')
widget_300=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,0')
if widget_300: wevent(widget_300, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_300.get_window())
del widget_300
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,1').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,1').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,1').set_text('15')
widget_301=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,1')
if widget_301: wevent(widget_301, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_301.get_window())
del widget_301
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,2').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,2').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,2').set_text('16')
widget_302=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,2')
if widget_302: wevent(widget_302, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_302.get_window())
del widget_302
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,3').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,3').set_text('17')
widget_303=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,3')
if widget_303: wevent(widget_303, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_303.get_window())
del widget_303
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,4').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,4').set_text('18')
widget_304=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,4')
if widget_304: wevent(widget_304, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_304.get_window())
del widget_304
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,5').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,5').set_text('1')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,5').set_text('19')
widget_305=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,5')
if widget_305: wevent(widget_305, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_305.get_window())
del widget_305
widget_306=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,5')
if widget_306: wevent(widget_306, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_306.get_window())
del widget_306
widget_307=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,5')
if widget_307: wevent(widget_307, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_307.get_window())
del widget_307
assert tests.testDij("Triclinic;C1", d11=2, d12=3, d13=4, d14=5, d15=6, d16=7, d21=8, d22=9, d23=10, d24=11, d25=12, d26=13, d31=14, d32=15, d33=16, d34=17, d35=18, d36=19)

widget_308=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:2,5')
if widget_308: wevent(widget_308, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_308.get_window())
del widget_308
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Triclinic.C1
findWidget('OOF2:Materials Page:Pane:Property:Add').clicked()
checkpoint property selected
checkpoint Materials page updated
checkpoint OOF.Material.Add_property
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 9.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 6.3000000000000e+01)

# Save material in 'rank3mat.dat'
findMenu(findWidget('OOF2:MenuBar'), ['File', 'Save', 'Materials']).activate()
checkpoint toplevel widget mapped Dialog-Materials
findWidget('Dialog-Materials').resize(192, 227)
findWidget('Dialog-Materials:filename').set_text('r')
findWidget('Dialog-Materials:filename').set_text('ra')
findWidget('Dialog-Materials:filename').set_text('ran')
findWidget('Dialog-Materials:filename').set_text('rank')
findWidget('Dialog-Materials:filename').set_text('rank3')
findWidget('Dialog-Materials:filename').set_text('rank3m')
findWidget('Dialog-Materials:filename').set_text('rank3ma')
findWidget('Dialog-Materials:filename').set_text('rank3mat')
findWidget('Dialog-Materials:filename').set_text('rank3mat.')
findWidget('Dialog-Materials:filename').set_text('rank3mat.d')
findWidget('Dialog-Materials:filename').set_text('rank3mat.da')
findWidget('Dialog-Materials:filename').set_text('rank3mat.dat')
findWidget('Dialog-Materials:materials').get_selection().unselect_all()
findWidget('Dialog-Materials:materials').get_selection().select_path(Gtk.TreePath([0]))
findWidget('Dialog-Materials:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Save.Materials
# Delete material

findWidget('OOF2:Materials Page:Pane:Material:Delete').clicked()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(192, 86)
findWidget('Questioner:OK').clicked()
checkpoint Materials page updated
checkpoint OOF.Material.Delete
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 0.0000000000000e+00)
# Open piezoelectricity cubic Td
# Check that values are what we set earlier

findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.9000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.4000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.8000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.3000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.7000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.0000000000000e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 0.0000000000000e+00)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Cubic:Td')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td').resize(526, 184)
widget_309=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_309: wevent(widget_309, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_309.get_window())
del widget_309
widget_310=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_310: wevent(widget_310, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_310.get_window())
del widget_310
widget_311=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_311: wevent(widget_311, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_311.get_window())
del widget_311
assert tests.testDij("Cubic;Td", d14=1.3, d25=1.3, d36=1.3)

# Change d_14 to 0

findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3').set_text('0')
widget_312=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_312: wevent(widget_312, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_312.get_window())
del widget_312
# Check that all d_ij are 0
assert tests.testDij("Cubic;Td")

findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Cubic.Td
# Change one entry in the rest of the piezoelectric properties so we can test that reloading changes the back.
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:D3h')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 1, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1').set_text('0')
widget_313=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1')
if widget_313: wevent(widget_313, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_313.get_window())
del widget_313
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Hexagonal.D3h
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:C6v')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 1, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4').set_text('0')
widget_314=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4')
if widget_314: wevent(widget_314, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_314.get_window())
del widget_314
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Hexagonal.C6v
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:D6')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 1, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3').set_text('0')
widget_315=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3')
if widget_315: wevent(widget_315, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_315.get_window())
del widget_315
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Hexagonal.D6
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:D6i')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 1, 3]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0').set_text('0')
widget_316=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_316: wevent(widget_316, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_316.get_window())
del widget_316
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Hexagonal.D6i
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:C6')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 1, 4]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3').set_text('0')
widget_317=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3')
if widget_317: wevent(widget_317, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_317.get_window())
del widget_317
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Hexagonal.C6
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Trigonal:C3v')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 2, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4').set_text('0')
widget_318=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4')
if widget_318: wevent(widget_318, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_318.get_window())
del widget_318
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Trigonal.C3v
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Trigonal:D3')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 2, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0').set_text('0')
widget_319=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0')
if widget_319: wevent(widget_319, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_319.get_window())
del widget_319
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Trigonal.D3
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Trigonal:C3')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 2, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0').set_text('0')
widget_320=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0')
if widget_320: wevent(widget_320, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_320.get_window())
del widget_320
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Trigonal.C3
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.8784426877160e-01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.8878442687716e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.8878442687716e+00)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.6887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.9887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.2887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.5887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 3.8887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.0887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.3887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.5887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.7887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 4.9887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.1887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.3887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.6887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 5.9887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.2887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.4887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.7887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 6.9887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.1887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.3887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.4887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.6887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.8887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.9887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.1887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.4887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.6887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.7887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.9887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.1887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.4887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.7887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.9887844268772e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0288784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0488784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0788784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0988784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1288784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1588784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1788784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2088784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2288784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2488784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2688784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2988784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3288784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3588784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3888784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4188784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4388784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4588784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4788784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4988784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5188784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5388784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5488784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5588784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5688784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5788784426877e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([4, 1, 3]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5700000000000e+02)
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:D2d')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3').set_text('0')
widget_321=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3')
if widget_321: wevent(widget_321, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_321.get_window())
del widget_321
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Tetragonal.D2d
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:C4v')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4').set_text('0')
widget_322=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4')
if widget_322: wevent(widget_322, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_322.get_window())
del widget_322
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Tetragonal.C4v
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:D4')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3').set_text('0')
widget_323=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3')
if widget_323: wevent(widget_323, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_323.get_window())
del widget_323
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Tetragonal.D4
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:C4i')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 3]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3').set_text('0')
widget_324=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_324: wevent(widget_324, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_324.get_window())
del widget_324
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Tetragonal.C4i
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:C4')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 4]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3').set_text('0')
widget_325=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3')
if widget_325: wevent(widget_325, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_325.get_window())
del widget_325
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Tetragonal.C4
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Orthorhombic:C2v')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 4, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:0,4').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:0,4').set_text('0')
widget_326=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:0,4')
if widget_326: wevent(widget_326, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_326.get_window())
del widget_326
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Orthorhombic.C2v
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Orthorhombic:D2')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 4, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3').set_text('0')
widget_327=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3')
if widget_327: wevent(widget_327, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_327.get_window())
del widget_327
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Orthorhombic.D2
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8500000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0500000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1500000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2500000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2900000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3900000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4500000000000e+02)
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Monoclinic:Cs')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 5, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0').set_text('0')
widget_328=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0')
if widget_328: wevent(widget_328, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_328.get_window())
del widget_328
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Monoclinic.Cs
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Monoclinic:C2')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 5, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3').set_text('0')
widget_329=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3')
if widget_329: wevent(widget_329, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_329.get_window())
del widget_329
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Monoclinic.C2
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Triclinic:C1')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 6, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1').resize(526, 184)
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0').set_text('')
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0').set_text('0')
widget_330=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
if widget_330: wevent(widget_330, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_330.get_window())
del widget_330
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Property.Parametrize.Couplings.PiezoElectricity.Triclinic.C1
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.5200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.5800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.6500000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.6900000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.7200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.7700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.8000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.8600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.9000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.9300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.9700000000000e+02)
# Load rank3mat.dat

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Data']).activate()
checkpoint toplevel widget mapped Dialog-Data
findWidget('Dialog-Data').resize(192, 92)
findWidget('Dialog-Data:filename').set_text('r')
findWidget('Dialog-Data:filename').set_text('ra')
findWidget('Dialog-Data:filename').set_text('ran')
findWidget('Dialog-Data:filename').set_text('rank')
findWidget('Dialog-Data:filename').set_text('rank3')
findWidget('Dialog-Data:filename').set_text('rank3m')
findWidget('Dialog-Data:filename').set_text('rank3ma')
findWidget('Dialog-Data:filename').set_text('rank3mat')
findWidget('Dialog-Data:filename').set_text('rank3mat.')
findWidget('Dialog-Data:filename').set_text('rank3mat.d')
findWidget('Dialog-Data:filename').set_text('rank3mat.da')
findWidget('Dialog-Data:filename').set_text('rank3mat.dat')
findWidget('Dialog-Data:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint Materials page updated
checkpoint OOF.File.Load.Data
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 6.3000000000000e+01)
# Open piezoelectric cubic Td

findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.9610565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.9110565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.7910565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.7310565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.6610565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.6010565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.5210565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4510565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3910565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3210565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2810565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2310565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1810565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1310565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0810565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0510565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0110565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9710565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9410565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9110565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8910565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8710565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8610565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8510565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8410565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8310565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8210565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8110565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8010565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7910565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7810565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7710565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7610565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7510565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7410565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7310565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7110565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6910565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6610565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6210565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5910565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5510565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5010565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4310565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3710565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2910565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2410565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1610565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0910565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0610565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0110565570012e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.7105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.4105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.2105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.1105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.0105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.9105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.8105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.7105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.5105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.3105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.2105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.0105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.9105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.8105655700116e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.8000000000000e+01)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Cubic:Td')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 6.0264175750083e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 2.2106928372077e-01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 2.0360461693357e-02)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 0.0000000000000e+00)
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 0, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td').resize(526, 184)
widget_331=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_331: wevent(widget_331, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_331.get_window())
del widget_331
widget_332=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_332: wevent(widget_332, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_332.get_window())
del widget_332
widget_333=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_333: wevent(widget_333, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_333.get_window())
del widget_333
assert tests.testDij("Cubic;Td", d14=1.3, d25=1.3, d36=1.3)

widget_334=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:dijk:0,3')
if widget_334: wevent(widget_334, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_334.get_window())
del widget_334
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Cubic;Td:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity hexagonal D3h

wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:D3h')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 1, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h').resize(526, 184)
widget_335=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1')
if widget_335: wevent(widget_335, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_335.get_window())
del widget_335
widget_336=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1')
if widget_336: wevent(widget_336, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_336.get_window())
del widget_336
widget_337=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1')
if widget_337: wevent(widget_337, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_337.get_window())
del widget_337
assert tests.testDij("Hexagonal;D3h", d16=-6, d21=-3, d22=3)

widget_338=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:dijk:1,1')
if widget_338: wevent(widget_338, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_338.get_window())
del widget_338
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D3h:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity hexagonal C6v

wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:C6v')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 1, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v').resize(526, 184)
widget_339=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4')
if widget_339: wevent(widget_339, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_339.get_window())
del widget_339
widget_340=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4')
if widget_340: wevent(widget_340, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_340.get_window())
del widget_340
widget_341=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4')
if widget_341: wevent(widget_341, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_341.get_window())
del widget_341
assert tests.testDij("Hexagonal;C6v", d15=2, d24=2, d31=3, d32=3, d33=4)

widget_342=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:dijk:0,4')
if widget_342: wevent(widget_342, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_342.get_window())
del widget_342
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6v:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity hexagonal D6

wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:D6')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 1, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6').resize(526, 184)
widget_343=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3')
if widget_343: wevent(widget_343, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_343.get_window())
del widget_343
widget_344=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3')
if widget_344: wevent(widget_344, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_344.get_window())
del widget_344
widget_345=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3')
if widget_345: wevent(widget_345, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_345.get_window())
del widget_345
assert tests.testDij("Hexagonal;D6", d14=5, d25=-5)

widget_346=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:dijk:0,3')
if widget_346: wevent(widget_346, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_346.get_window())
del widget_346
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity hexagonal D6i

getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:D6i')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 1, 3]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i').resize(526, 184)
widget_347=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_347: wevent(widget_347, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_347.get_window())
del widget_347
widget_348=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_348: wevent(widget_348, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_348.get_window())
del widget_348
widget_349=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_349: wevent(widget_349, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_349.get_window())
del widget_349
assert tests.testDij("Hexagonal;D6i", d11=3, d12=-3, d16=-8, d21=-4, d22=4, d26=-6)

widget_350=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:dijk:0,0')
if widget_350: wevent(widget_350, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_350.get_window())
del widget_350
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;D6i:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity hexagonal C6

getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Hexagonal:C6')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 1, 4]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6').resize(526, 184)
widget_351=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3')
if widget_351: wevent(widget_351, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_351.get_window())
del widget_351
widget_352=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3')
if widget_352: wevent(widget_352, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_352.get_window())
del widget_352
widget_353=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3')
if widget_353: wevent(widget_353, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_353.get_window())
del widget_353
assert tests.testDij("Hexagonal;C6", d14=3, d15=4, d24=4, d25=-3, d31=5, d32=5, d33=6)

widget_354=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:dijk:0,3')
if widget_354: wevent(widget_354, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_354.get_window())
del widget_354
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Hexagonal;C6:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity trigonal C3v

getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Trigonal:C3v')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 2, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v').resize(526, 184)
widget_355=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4')
if widget_355: wevent(widget_355, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_355.get_window())
del widget_355
widget_356=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4')
if widget_356: wevent(widget_356, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_356.get_window())
del widget_356
widget_357=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4')
if widget_357: wevent(widget_357, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_357.get_window())
del widget_357
assert tests.testDij("Trigonal;C3v", d15=4, d16=-10, d21=-5, d22=5, d24=4, d31=6, d32=6, d33=7)

widget_358=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:dijk:0,4')
if widget_358: wevent(widget_358, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_358.get_window())
del widget_358
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3v:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity trigonal D3

wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Trigonal:D3')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 2, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3').resize(526, 184)
widget_359=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0')
if widget_359: wevent(widget_359, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_359.get_window())
del widget_359
widget_360=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0')
if widget_360: wevent(widget_360, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_360.get_window())
del widget_360
widget_361=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0')
if widget_361: wevent(widget_361, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_361.get_window())
del widget_361
assert tests.testDij("Trigonal;D3", d11=3, d12=-3, d14=4, d25=-4, d26=-6)

widget_362=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:dijk:0,0')
if widget_362: wevent(widget_362, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_362.get_window())
del widget_362
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;D3:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity trigonal C3

wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Trigonal:C3')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 2, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3').resize(526, 184)
widget_363=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0')
if widget_363: wevent(widget_363, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_363.get_window())
del widget_363
widget_364=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0')
if widget_364: wevent(widget_364, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_364.get_window())
del widget_364
widget_365=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0')
if widget_365: wevent(widget_365, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_365.get_window())
del widget_365
assert tests.testDij("Trigonal;C3", d11=3, d12=-3, d14=4, d15=5, d16=-12, d21=-6, d22=6, d24=5, d25=-4, d26=-6, d31=7, d32=7, d33=8)

widget_366=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:dijk:0,0')
if widget_366: wevent(widget_366, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_366.get_window())
del widget_366
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Trigonal;C3:widget_GTK_RESPONSE_CANCEL').clicked()
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:D2d')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
# Open piezoelectricity tetragonal D2d

wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d').resize(526, 184)
widget_367=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3')
if widget_367: wevent(widget_367, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_367.get_window())
del widget_367
widget_368=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3')
if widget_368: wevent(widget_368, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_368.get_window())
del widget_368
widget_369=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3')
if widget_369: wevent(widget_369, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_369.get_window())
del widget_369
widget_370=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3')
if widget_370: wevent(widget_370, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_370.get_window())
del widget_370
assert tests.testDij("Tetragonal;D2d", d14=4, d25=4, d36=5)

widget_371=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:dijk:0,3')
if widget_371: wevent(widget_371, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_371.get_window())
del widget_371
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D2d:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity tetragonal C4v

getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:C4v')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v').resize(526, 184)
widget_372=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4')
if widget_372: wevent(widget_372, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_372.get_window())
del widget_372
widget_373=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4')
if widget_373: wevent(widget_373, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_373.get_window())
del widget_373
widget_374=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4')
if widget_374: wevent(widget_374, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_374.get_window())
del widget_374
assert tests.testDij("Tetragonal;C4v", d15=3, d24=3, d31=4, d32=4, d33=5)

widget_375=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:dijk:0,4')
if widget_375: wevent(widget_375, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_375.get_window())
del widget_375
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4v:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity tetragonal D4

wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:D4')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 2]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4').resize(526, 184)
widget_376=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3')
if widget_376: wevent(widget_376, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_376.get_window())
del widget_376
widget_377=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3')
if widget_377: wevent(widget_377, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_377.get_window())
del widget_377
widget_378=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3')
if widget_378: wevent(widget_378, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_378.get_window())
del widget_378
assert tests.testDij("Tetragonal;D4", d14=4, d25=-4)

widget_379=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:dijk:0,3')
if widget_379: wevent(widget_379, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_379.get_window())
del widget_379
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;D4:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity tetragonal C4i

getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:C4i')
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.8244669719763e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.8894311499045e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.9432860709758e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 7.9870734643580e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.0218350592191e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.0486125847270e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.0684477700497e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.0823823443550e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.0914580368108e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.0967165765851e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.0999491147608e+01)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.1000000000000e+01)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 3]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i').resize(526, 184)
widget_380=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_380: wevent(widget_380, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_380.get_window())
del widget_380
widget_381=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_381: wevent(widget_381, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_381.get_window())
del widget_381
widget_382=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_382: wevent(widget_382, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_382.get_window())
del widget_382
assert tests.testDij("Tetragonal;C4i", d14=3, d15=4, d24=-4, d25=3, d31=5, d32=-5, d36=6)

widget_383=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_383: wevent(widget_383, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_383.get_window())
del widget_383
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:widget_GTK_RESPONSE_CANCEL').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.2000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 8.6000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.1000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.5000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 9.8000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.0600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.1700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.2900000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.3800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4500000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.4800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.5900000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6500000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.6900000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7500000000000e+02)
# Open piezoelectricity tetragonal C4

findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i').resize(526, 184)
widget_384=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_384: wevent(widget_384, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_384.get_window())
del widget_384
widget_385=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_385: wevent(widget_385, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_385.get_window())
del widget_385
widget_386=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_386: wevent(widget_386, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_386.get_window())
del widget_386
widget_387=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:dijk:0,3')
if widget_387: wevent(widget_387, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_387.get_window())
del widget_387
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4i:widget_GTK_RESPONSE_CANCEL').clicked()
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Tetragonal:C4')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 3, 4]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4').resize(526, 184)
widget_388=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3')
if widget_388: wevent(widget_388, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_388.get_window())
del widget_388
widget_389=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3')
if widget_389: wevent(widget_389, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_389.get_window())
del widget_389
widget_390=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3')
if widget_390: wevent(widget_390, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_390.get_window())
del widget_390
assert tests.testDij("Tetragonal;C4", d14=3, d15=4, d24=4, d25=-3, d31=5, d32=5, d33=6)

widget_391=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:dijk:0,3')
if widget_391: wevent(widget_391, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_391.get_window())
del widget_391
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Tetragonal;C4:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity orthorhombic C2v

getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Orthorhombic:C2v')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 4, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v').resize(526, 184)
widget_392=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:0,4')
if widget_392: wevent(widget_392, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_392.get_window())
del widget_392
assert tests.testDij("Orthorhombic;C2v", d15=4, d24=5, d31=6, d32=7, d33=8)

widget_393=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:dijk:0,4')
if widget_393: wevent(widget_393, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_393.get_window())
del widget_393
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;C2v:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity orthorhombic D2

getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Orthorhombic:D2')
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 2.0677461457646e+00)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 5.2032009369938e+00)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 6.3334133325333e+00)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 7.8750674986500e+00)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 8.3490130193021e+00)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 8.8594003109813e+00)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 8.9583458320834e+00)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 9.0000000000000e+00)
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 4, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2').resize(526, 184)
widget_394=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3')
if widget_394: wevent(widget_394, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_394.get_window())
del widget_394
widget_395=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3')
if widget_395: wevent(widget_395, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_395.get_window())
del widget_395
widget_396=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3')
if widget_396: wevent(widget_396, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_396.get_window())
del widget_396
assert tests.testDij("Orthorhombic;D2", d14=4, d25=5, d36=6)

widget_397=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:dijk:0,3')
if widget_397: wevent(widget_397, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_397.get_window())
del widget_397
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Orthorhombic;D2:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity monoclinic C2

findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.7600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.8500000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 1.9500000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.0300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.1700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.2900000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3600000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.3900000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4400000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4500000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4700000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.4800000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.5000000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.5100000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.5200000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.5300000000000e+02)
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll').get_vadjustment().set_value( 2.5400000000000e+02)
# CHANGE PREV COMMENT TO Cs
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Monoclinic:Cs')
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 1.3135492291529e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 1.9406401873988e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 2.1666826665067e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 2.4750134997300e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 2.5698026038604e+01)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 2.6718800621963e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 2.6916691664167e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 2.6989590206821e+01)
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 5, 0]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs').resize(526, 184)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 2.7000000000000e+01)
widget_398=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0')
if widget_398: wevent(widget_398, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_398.get_window())
del widget_398
widget_399=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0')
if widget_399: wevent(widget_399, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_399.get_window())
del widget_399
widget_400=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0')
if widget_400: wevent(widget_400, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_400.get_window())
del widget_400
assert tests.testDij("Monoclinic;Cs", d11=3, d12=4, d13=5, d15=6, d24=7, d26=8, d31=9, d32=10, d33=11, d35=12)

widget_401=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:dijk:0,0')
if widget_401: wevent(widget_401, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_401.get_window())
del widget_401
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;Cs:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity monoclinic C2

getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Monoclinic:C2')
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 3.1135492291529e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 3.4583458332833e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 3.9666826665067e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 4.1427236456146e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 4.2750134997300e+01)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 4.3698026038604e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 4.4333413330133e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 4.4718800621963e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 4.4916691664167e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 4.4989590206821e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 4.5000000000000e+01)
tree=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree')
column = tree.get_column(0)
tree.row_activated(Gtk.TreePath([4, 1, 5, 1]), column)
checkpoint Materials page updated
checkpoint property selected
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2').resize(526, 184)
widget_402=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3')
if widget_402: wevent(widget_402, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_402.get_window())
del widget_402
widget_403=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3')
if widget_403: wevent(widget_403, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_403.get_window())
del widget_403
widget_404=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3')
if widget_404: wevent(widget_404, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_404.get_window())
del widget_404
widget_405=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3')
if widget_405: wevent(widget_405, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_405.get_window())
del widget_405
assert tests.testDij("Monoclinic;C2", d14=2, d16=3, d21=4, d22=5, d23=6, d25=7, d34=8, d36=9)

widget_406=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:dijk:0,3')
if widget_406: wevent(widget_406, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_406.get_window())
del widget_406
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Monoclinic;C2:widget_GTK_RESPONSE_CANCEL').clicked()
# Open piezoelectricity triclinic C1

wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Couplings:PiezoElectricity:Triclinic:C1')
checkpoint Materials page updated
checkpoint property selected
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 4.9135492291529e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 5.5406401873988e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 5.9427236456146e+01)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 6.1698026038604e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 6.2718800621963e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 6.2989590206821e+01)
findWidget('OOF2:Materials Page:Pane:Material:PropertyListScroll').get_vadjustment().set_value( 6.3000000000000e+01)
findWidget('OOF2:Materials Page:Pane:Property:Parametrize').clicked()
checkpoint toplevel widget mapped Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1').resize(526, 184)
widget_407=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
if widget_407: wevent(widget_407, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_407.get_window())
del widget_407
widget_408=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
if widget_408: wevent(widget_408, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_408.get_window())
del widget_408
widget_409=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
if widget_409: wevent(widget_409, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_409.get_window())
del widget_409
assert tests.testDij("Triclinic;C1", d11=2, d12=3, d13=4, d14=5, d15=6, d16=7, d21=8, d22=9, d23=10, d24=11, d25=12, d26=13, d31=14, d32=15, d33=16, d34=17, d35=18, d36=19)

widget_410=findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:dijk:0,0')
if widget_410: wevent(widget_410, Gdk.EventType.FOCUS_CHANGE, in_=0, window=widget_410.get_window())
del widget_410
findWidget('Dialog-Parametrize Couplings;PiezoElectricity;Triclinic;C1:widget_GTK_RESPONSE_CANCEL').clicked()
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
