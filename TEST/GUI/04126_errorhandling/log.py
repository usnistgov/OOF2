# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.5 $
# $Author: langer $
# $Date: 2011/01/14 15:49:56 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import tests

checkpoint OOF.File.Load.Script
assert tests.syntaxErrorMsg('File "TEST_DATA/syntaxerror.py", line 2\n    \'Twas brillig, and the slithy toves did gyre and gimble in the wabe.\n                                                                       ^\nSyntaxError: EOL while scanning string literal\n\nErrUserError: Script \'TEST_DATA/nestedsyntaxerr.py\' raised a SyntaxError exception')
checkpoint OOF.File.LoadStartUp.Script
checkpoint toplevel widget mapped Error
findWidget('Error').resize(592, 160)
findWidget('Error:gtk-ok').clicked()
assert tests.noExecution()

findMenu(findWidget('OOF2:MenuBar'), 'File:Load:Script').activate()
checkpoint toplevel widget mapped Dialog-Script
findWidget('Dialog-Script').resize(191, 71)
findWidget('Dialog-Script:filename').set_text('TEST_DATA/nestedsyntaxerr.py')
findWidget('Dialog-Script:gtk-ok').clicked()
checkpoint OOF.File.Load.Script
checkpoint OOF.File.Load.Script
checkpoint toplevel widget mapped Error
findWidget('Error').resize(592, 160)
assert tests.syntaxErrorMsg('File "TEST_DATA/syntaxerror.py", line 2\n    \'Twas brillig, and the slithy toves did gyre and gimble in the wabe.\n                                                                       ^\nSyntaxError: EOL while scanning string literal\n\nErrUserError: Script \'TEST_DATA/nestedsyntaxerr.py\' raised a SyntaxError exception')
findWidget('Error:gtk-ok').clicked()
assert tests.noExecution()
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
