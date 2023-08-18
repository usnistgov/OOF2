# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# This file is run with execfile from within guitests.py.  "directory"
# is set to the directory containing the test files.

# This test must be done *after* oof2 quits, which is why it's here
# instead of in log.py.  It's checking to see if the python log is
# saved correctly from the quit dialog box.

from generics import *
assert filediff("session.log", tolerance=0.)
