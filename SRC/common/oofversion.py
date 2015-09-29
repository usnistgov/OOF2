# -*- python -*-
# $RCSfile: oofversion.py,v $
# $Revision: 1.7 $
# $Author: langer $
# $Date: 2014/09/27 21:40:25 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## The value assigned to 'version' here is modified by a sed command
## in the make_distutils_dist script when an oof distribution is
## packaged.  The value in the original must be the same as the value
## that the script is looking for, so don't edit this file without
## editing the script.

version = "(unreleased)"

# This version tag is presented to the user on the intro page, and is
# also the reply to the "--version" command-line switch.  It might be
# better characterized as a "release version".  See also "version.py",
# which is the version number used when writing and reading data
# files.

