# -*- python -*-
# $RCSfile: log.py,v $
# $Revision: 1.2 $
# $Author: langer $
# $Date: 2010/12/04 01:08:20 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import tests

checkpoint OOF.File.LoadStartUp.Script
assert tests.syntaxErrorMsg('TEST_DATA/syntaxerror.py", line 2\n    \'Twas brillig, and the slithy toves did gyre and gimble in the wabe.\n                                                                       ^\nSyntaxError: EOL while scanning string literal')
checkpoint toplevel widget mapped Error
findWidget('Error').resize(592, 160)
findWidget('Error:gtk-ok').clicked()
assert tests.noExecution()

findMenu(findWidget('OOF2:MenuBar'), 'File:Load:Script').activate()
checkpoint toplevel widget mapped Dialog-Script
findWidget('Dialog-Script').resize(191, 71)
findWidget('Dialog-Script:filename').set_text('TEST_DATA/syntaxerror.py')
findWidget('Dialog-Script:gtk-ok').clicked()
checkpoint OOF.File.Load.Script
checkpoint toplevel widget mapped Error
findWidget('Error').resize(592, 160)
assert tests.syntaxErrorMsg('TEST_DATA/syntaxerror.py", line 2\n    \'Twas brillig, and the slithy toves did gyre and gimble in the wabe.\n                                                                       ^\nSyntaxError: EOL while scanning string literal')
findWidget('Error:gtk-ok').clicked()

assert tests.noExecution()
findMenu(findWidget('OOF2:MenuBar'), 'File:Quit').activate()
