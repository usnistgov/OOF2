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

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Check that the expected error message was produced.

# The error message format differs in different Python versions, so
# generics.errorMsg() takes a bunch of strings and returns True if any
# one of them matches.  See comments in generics.py.

# Also, different versions of ScriptLoader.run() produce different
# error messages.  So here we use the templated wrapper,
# generics.errorMsgTemplates(), for generics.errorMsg().  The wrapper
# allows different values of a substring in the messages.  Once we've
# settled on a single version of ScriptLoader.run(), just replace
# FNAME in the templates with the appropriate value, and call errorMsg
# instead of errorMsgTemplates.

errmsg_templates = [
# Python 3.8
"""  File "FNAME", line 2
    'Twas brillig, and the slithy toves did gyre and gimble in the wabe.
                                                                       ^
SyntaxError: EOL while scanning string literal
""",

# Python 3.9
"""  File "FNAME", line 2
    'Twas brillig, and the slithy toves did gyre and gimble in the wabe.
                                                                        ^
SyntaxError: EOL while scanning string literal
""",

# Python 3.10, 3.11, 3.12 and 3.13
"""  File "FNAME", line 2
    'Twas brillig, and the slithy toves did gyre and gimble in the wabe.
    ^
SyntaxError: unterminated string literal (detected at line 2)
""",
    ]


def errorMsgTest():
    return generics.errorMsgTemplates(
        "FNAME",
        ("TEST_DATA/syntaxerror.py", "<string>"),
        errmsg_templates)
    #return generics.errorMsg(*msgs, verbose=True)
