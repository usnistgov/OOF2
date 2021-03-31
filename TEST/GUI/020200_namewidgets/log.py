# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Check that colons are prohibited in names where necessary.
import tests

findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)

# Try to create a Microstructure with a colon in its name.
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Microstructure']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Microstructure
findWidget('OOF2:Microstructure Page:Pane').set_position(184)
checkpoint meshable button set
checkpoint microstructure page sensitized
findWidget('OOF2:Microstructure Page:New').clicked()
checkpoint toplevel widget mapped Dialog-Create Microstructure
findWidget('Dialog-Create Microstructure').resize(210, 236)
findWidget('OOF2').resize(782, 545)
findWidget('Dialog-Create Microstructure').resize(210, 236)
assert tests.msOKsensitive()

findWidget('Dialog-Create Microstructure:name').insert_text('a', 6)
assert tests.msOKsensitive()

findWidget('Dialog-Create Microstructure:name').insert_text(':', 1)
assert not tests.msOKsensitive()

findWidget('Dialog-Create Microstructure:name').insert_text('b', 2)
findWidget('Dialog-Create Microstructure:name').insert_text('c', 3)
assert not tests.msOKsensitive()

findWidget('Dialog-Create Microstructure:name').delete_text(1, 2)
assert tests.msOKsensitive()

findWidget('Dialog-Create Microstructure:name').insert_text('d', 3)
findWidget('Dialog-Create Microstructure:name').insert_text('e', 4)
findWidget('Dialog-Create Microstructure:name').insert_text('f', 5)
findWidget('Dialog-Create Microstructure:widget_GTK_RESPONSE_OK').clicked()
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
checkpoint OOF.Microstructure.New
# Try to create a Property with a colon in its name.
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Materials']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint Materials page updated
checkpoint page installed Materials
findWidget('OOF2:Materials Page:Pane').set_position(289)
getTree('PropertyTree').simulateSelect('Color')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0]), open_all=False)
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
getTree('PropertyTree').simulateSelect('Mechanical:Elasticity:Isotropic')
checkpoint Materials page updated
checkpoint property selected
wevent(findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree'), Gdk.EventType.BUTTON_RELEASE, button=1, state=256, window=findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').get_window())
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Isotropic
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic').resize(192, 92)
assert tests.propertyOKsensitive()

findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').delete_text(0, 11)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('a', 11)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('b', 1)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text('c', 2)
assert tests.propertyOKsensitive()

findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').insert_text(':', 3)
assert not tests.propertyOKsensitive()

findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:new_name').delete_text(3, 4)
assert tests.propertyOKsensitive()

findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic:widget_GTK_RESPONSE_OK').clicked()
findWidget('OOF2:Materials Page:Pane:Property:PropertyScroll:PropertyTree').expand_row(Gtk.TreePath([1, 0, 0]), open_all=False)
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy

# Copy the new property and try to give it a name with a colon in it.
findWidget('OOF2:Materials Page:Pane:Property:Copy').clicked()
checkpoint toplevel widget mapped Dialog-Copy property Mechanical;Elasticity;Isotropic;abc
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc').resize(192, 92)
assert tests.property2OKsensitive()

findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').delete_text(0, 3)
assert tests.property2OKsensitive()

findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').delete_text(0, 11)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').insert_text('a', 11)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').insert_text('b', 1)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').insert_text('c', 2)
assert tests.property2OKsensitive()

findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').insert_text(':', 3)
assert not tests.property2OKsensitive()

findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').insert_text('d', 4)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').insert_text('e', 5)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').insert_text('f', 6)
assert not tests.property2OKsensitive()

findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').delete_text(6, 7)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').delete_text(5, 6)
assert not tests.property2OKsensitive()

findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').delete_text(4, 5)
findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').delete_text(3, 4)
assert tests.property2OKsensitive()

findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:new_name').insert_text('d', 3)
assert tests.property2OKsensitive()

findWidget('Dialog-Copy property Mechanical;Elasticity;Isotropic;abc:widget_GTK_RESPONSE_OK').clicked()
checkpoint Materials page updated
checkpoint property selected
checkpoint OOF.Property.Copy

# Same thing with a Skeleton
wevent(findWidget('OOF2:Navigation:PageMenu'), Gdk.EventType.BUTTON_PRESS, button=1, state=0, window=findWidget('OOF2:Navigation:PageMenu').get_window())
checkpoint toplevel widget mapped chooserPopup-PageMenu
findMenu(findWidget('chooserPopup-PageMenu'), ['Skeleton']).activate() # MenuItemLogger
deactivatePopup('chooserPopup-PageMenu') # MenuItemLogger
checkpoint page installed Skeleton
findWidget('OOF2:Skeleton Page:Pane').set_position(417)
checkpoint skeleton page sensitized
checkpoint skeleton page sensitized
findWidget('OOF2:Skeleton Page:New').clicked()
checkpoint toplevel widget mapped Dialog-New skeleton
findWidget('Dialog-New skeleton').resize(346, 254)
assert tests.skelOKsensitive()

findWidget('Dialog-New skeleton:name').delete_text(0, 11)
findWidget('Dialog-New skeleton:name').insert_text(':', 11)
assert not tests.skelOKsensitive()

findWidget('Dialog-New skeleton:name').delete_text(0, 1)
assert tests.skelOKsensitive()

findWidget('Dialog-New skeleton:name').delete_text(0, 11)
findWidget('Dialog-New skeleton:name').insert_text('a', 11)
findWidget('Dialog-New skeleton:name').insert_text('b', 1)
assert tests.skelOKsensitive()

findWidget('Dialog-New skeleton:name').insert_text(':', 2)
assert not tests.skelOKsensitive()

findWidget('Dialog-New skeleton:name').insert_text('d', 3)
findWidget('Dialog-New skeleton:name').insert_text('e', 4)
assert not tests.skelOKsensitive()

findWidget('Dialog-New skeleton:name').delete_text(2, 3)
assert tests.skelOKsensitive()

findWidget('Dialog-New skeleton:widget_GTK_RESPONSE_CANCEL').clicked()
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
