# -*- python -*-
# $RCSfile: setup.py,v $
# $Revision: 1.3 $
# $Author: langer $
# $Date: 2011-02-18 16:14:40 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# This setup script compiles an oof2 extension.  It assumes that oof2
# is already installed correctly.

import os

modulename = 'ramberg_osgood'
libname  = 'oof_ramberg_osgood'

# We'll use the Python distutils to build the extension
import distutils.core

# oof2config contains information about the oof2 installation, and
# imports modules needed for building oof2. oof2config also adjusts
# sys.path so that oof2extutils can be located.  If oof2 has been
# installed correctly, and your PYTHONPATH is set correctly (if
# necessary), then oof2config is accessible.
import oof2config

# oof2extutils contains some helpful functions.  Import it *after*
# oof2config, or else Python may not be able to find it.
import oof2extutils

# oof2installlib contains code that allows libraries to be relocated
# on OS X.
import oof2installlib
oof2installlib.shared_libs = [libname]

# One (or more) SharedLibrary object must be created from the user's
# C++ files (as opposed to C++ files created by swig).  'sources' is a
# list of C++ file names.  oof2extutils.SharedLibrary is derived from
# build_shlib.SharedLibrary, and accepts all arguments that
# build_shlib.SharedLibrary does.  oof2extutils.SharedLibrary
# automatically includes header files and libraries required by oof2.

rolib = oof2extutils.SharedLibrary(
    name=libname,
    sources= [os.path.join('ramberg_osgood','ramberg_osgood.C')])

# get_swig_ext runs swig and creates an Extension object that contains
# the information necessary to build a Python extension module from
# the swig output files.  The destination directory will be created if
# necessary.  get_swig_ext returns the Extension object and the name
# of the Python package that contains the Python wrapper for the
# extension module.

roext, ropkg = oof2extutils.get_swig_ext(
    srcdir='ramberg_osgood',
    srcfile = 'ramberg_osgood.swg',
    destdir = 'ramberg_osgood_SWIG',
    libraries= [libname])

distutils.core.setup(
    # The first arguments here are pretty much self-explanatory.
    name = "ramberg_osgood",
    version = "0.9.1",
    author = "Andrew Reid",
    author_email = "andrew.reid@nist.gov",
    url = "http://www.ctcms.nist.gov/oof/",

    # 'ext_modules' is a list of all of the Extension objects defined above.
    ext_modules = [roext],

    # 'packages' is a list of all subdirectories that contain Python
    # files.  They must all have an __init__.py file.  Subdirectories
    # created by run_swig or get_swig_ext must also be listed here.
    # Their __init__.py files have been created automatically.
    packages = ['ramberg_osgood', ropkg],

    # shlibs is a list of all of the SharedLibrary objects defined above.
    shlibs = [rolib],

    # Use the install_lib class from oof2installlib instead of the
    # standard distutils install_lib.
    cmdclass = {"install_lib":oof2installlib.oof_install_lib}
    )
