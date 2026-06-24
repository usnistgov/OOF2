# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import sys

# Check to see if tifffile is usable.

# Recent versions of tifffile don't support python versions older than
# 3.12.  Some systems (MacPorts!) will install incompatible versions.
# Tifffile 2026.4.11 dropped support for Python 3.11.

OK = False

if sys.version_info[1] > 11:    # Python is 3.12 or newer
    OK = True
else:
    # For Python 3.11 or older, tifffile must be 2026.4.10 or older.
    try:
        # Some, maybe all, bad combinations of python and tifffile
        # will throw a syntax error if tifffile is too new.
        import tifffile
    except:
        pass
    else:
        tiffversion = [int(x) for x in tifffile.__version__.split('.')]
        badversion = [2026, 4, 11]
        OK = tiffversion < badversion
        del tifffile


if __name__ == "__main__":
    print(OK)
