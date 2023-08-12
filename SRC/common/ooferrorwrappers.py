# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Base class for Python exceptions created from C++ exceptions via the
# WRAP_OOFERROR_CLASS macro in ooferrorwrappers.swg.

class PyOOFError(Exception):
    pass

# Dictionary that maps C++ exception classes to their Python wrappers.

pyErrorWrappers = {}

