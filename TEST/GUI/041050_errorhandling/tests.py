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
    
def errorMsgTest():
    return generics.errorMsg(
        # Python 3.8
"""  File "TEST_DATA/syntaxerror.py", line 2
    'Twas brillig, and the slithy toves did gyre and gimble in the wabe.
                                                                       ^
SyntaxError: EOL while scanning string literal

ooflib.SWIG.common.ooferror.PyErrUserError: Script TEST_DATA/nestedsyntaxerr.py raised a SyntaxError exception""",

        # Python 3.9
"""  File "TEST_DATA/syntaxerror.py", line 2
    'Twas brillig, and the slithy toves did gyre and gimble in the wabe.
                                                                        ^
SyntaxError: EOL while scanning string literal

ooflib.SWIG.common.ooferror.PyErrUserError: Script TEST_DATA/nestedsyntaxerr.py raised a SyntaxError exception""",
        
        # Python 3.10
"""File "TEST_DATA/syntaxerror.py", line 2
'Twas brillig, and the slithy toves did gyre and gimble in the wabe.
^
SyntaxError: unterminated string literal (detected at line 2)

ooflib.SWIG.common.ooferror.PyErrUserError: Script TEST_DATA/nestedsyntaxerr.py raised a SyntaxError exception"""
        )
