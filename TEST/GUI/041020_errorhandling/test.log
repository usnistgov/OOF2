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

checkpoint OOF.File.Load.Script
checkpoint OOF.File.LoadStartUp.Script
checkpoint toplevel widget mapped Error
findWidget('Error').resize(592, 160)
assert generics.errorMsg("ErrProgrammingError: Somebody made a mistake!\n(./SRC/common/cdebug.C:124)\n\nErrUserError: Script 'TEST_DATA/errorcmd.py' raised an ErrProgrammingError exception\n\nErrUserError: Script 'TEST_DATA/nestederror.py' raised an ErrUserError exception")

findWidget('Error:widget_GTK_RESPONSE_OK').clicked()
assert utils.OOFeval('teststring') == 'ok' and utils.OOFeval('anothertest') == 'ok'

utils.OOFexec("teststring = None")
utils.OOFexec("anothertest = None")

findMenu(findWidget('OOF2:MenuBar'), ['File','Load','Script']).activate()
checkpoint toplevel widget mapped Dialog-Script
findWidget('Dialog-Script:filename').set_text('TEST_DATA/nestederror.py')
findWidget('Dialog-Script:widget_GTK_RESPONSE_OK').clicked()
checkpoint OOF.File.Load.Script
checkpoint OOF.File.Load.Script
checkpoint toplevel widget mapped Error
findWidget('Error').resize(592, 160)
assert generics.errorMsg("ErrProgrammingError: Somebody made a mistake!\n(./SRC/common/cdebug.C:124)\n\nErrUserError: Script 'TEST_DATA/errorcmd.py' raised an ErrProgrammingError exception\n\nErrUserError: Script 'TEST_DATA/nestederror.py' raised an ErrUserError exception")
findWidget('Error:widget_GTK_RESPONSE_OK').clicked()
assert utils.OOFeval('teststring') == 'ok' and utils.OOFeval('anothertest') == 'ok'
findMenu(findWidget('OOF2:MenuBar'), ['File','Quit']).activate()
checkpoint toplevel widget mapped Questioner
findWidget('Questioner').resize(353, 93)
findWidget('Questioner:Don"t Save').clicked()
