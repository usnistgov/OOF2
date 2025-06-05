# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import generics
from ooflib.common import utils

def noExecution():
    # The file with the syntax error shouldn't have run.  If it did,
    # then the main OOF namespace contains a variable 'borogoves'.
    try:
        utils.OOFeval('borogoves')
    except NameError:
        return True

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Instead of using generics.errorMsgTemplates() like 041010, does,
# this lists the error messages for different versions of
# ScriptLoader.run() separately, and calls generics.errorMsg()
# instead.  That's because the differences between the messages are
# greater.

def errorMsgTest():
    return generics.errorMsg(
        # Python 3.8
"""ooflib.common.IO.scriptloader.ScriptException: Error running file "TEST_DATA/nestedsyntaxerr.py", line 2
-----
ooflib.common.IO.scriptloader.ScriptParseError: Error parsing file "TEST_DATA/syntaxerror.py"
-----
  File "TEST_DATA/syntaxerror.py", line 2
    'Twas brillig, and the slithy toves did gyre and gimble in the wabe.
                                                                       ^
SyntaxError: EOL while scanning string literal
""",

        # Python 3.9 (differs from 3.8 only in the position of the caret)
"""ooflib.common.IO.scriptloader.ScriptException: Error running file "TEST_DATA/nestedsyntaxerr.py", line 2
-----
ooflib.common.IO.scriptloader.ScriptParseError: Error parsing file "TEST_DATA/syntaxerror.py"
-----
  File "TEST_DATA/syntaxerror.py", line 2
    'Twas brillig, and the slithy toves did gyre and gimble in the wabe.
                                                                        ^
SyntaxError: EOL while scanning string literal
""",

        # Python 3.10 through 3.13
"""ooflib.common.IO.scriptloader.ScriptException: Error running file "TEST_DATA/nestedsyntaxerr.py", line 2
-----
ooflib.common.IO.scriptloader.ScriptParseError: Error parsing file "TEST_DATA/syntaxerror.py"
-----
  File "TEST_DATA/syntaxerror.py", line 2
    'Twas brillig, and the slithy toves did gyre and gimble in the wabe.
    ^
SyntaxError: unterminated string literal (detected at line 2)
""",
    )
