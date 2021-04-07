# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.common import utils
import generics


findWidget('OOF2:FE Mesh Page:Pane').set_position(557)
findWidget('OOF2:FE Mesh Page:Pane:leftpane').set_position(106)
checkpoint toplevel widget mapped OOF2
checkpoint page installed Introduction
findWidget('OOF2').resize(782, 511)
checkpoint OOF.Help.Debug.Error.CError
# The startup script loaded by the args file sets teststring to "ok",
# then causes an error, and then sets teststring to "not ok".  If the
# error is handled correctly, the last line isn't executed and
# teststring is still "ok".
assert utils.OOFeval("teststring") == "ok"

checkpoint OOF.File.LoadStartUp.Script
checkpoint toplevel widget mapped Error
findWidget('Error').resize(266, 210)
findWidget('OOF2').resize(782, 545)
assert generics.errorMsg("ErrProgrammingError: Somebody made a mistake!\n(./SRC/common/cdebug.C:124)\n\nErrUserError: Script 'TEST_DATA/errorcmd.py' raised an ErrProgrammingError exception")
findWidget('Error:widget_GTK_RESPONSE_OK').clicked()

utils.OOFexec("teststring = None")

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Load', 'Script']).activate()
checkpoint toplevel widget mapped Dialog-Script
findWidget('Dialog-Script').resize(192, 92)
findWidget('Dialog-Script:filename').set_text('TEST_DATA/errorcmd.py')
findWidget('Dialog-Script:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.Help.Debug.Error.CError
checkpoint OOF.File.Load.Script
checkpoint toplevel widget mapped Error
assert generics.errorMsg("ErrProgrammingError: Somebody made a mistake!\n(./SRC/common/cdebug.C:124)\n\nErrUserError: Script 'TEST_DATA/errorcmd.py' raised an ErrProgrammingError exception")

findWidget('Error').resize(266, 210)
findWidget('Error:widget_GTK_RESPONSE_OK').clicked()
assert utils.OOFeval("teststring") == "ok"

findMenu(findWidget('OOF2:MenuBar'), ['File', 'Quit']).activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(336, 86)
findWidget('Questioner:Don"t Save').clicked()
