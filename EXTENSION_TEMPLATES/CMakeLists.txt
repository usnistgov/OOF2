# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# This file was created by oof2-setup-extension from the
# CMakeLists.txt template in OOF2/EXTENSION_TEMPLATES.

cmake_minimum_required(VERSION 3.18)

# You may want to change the version number in the following line.
project(%MODULENAME% VERSION 0.0.0)

# Set the default values of OOF2_PYTHON_VERSION and OOF2_SWIG_VERSION.
# Setting them here, *before* loading oofbuildtools.cmake, sets the
# default values to the ones from the oof2 build, transferred here
# when oof2-extension-setup replaced the template strings.
set(OOF2_PYTHON3_VERSION %PYTHON% CACHE STRING "Use this version of Python")
set(OOF2_SWIG_VERSION %SWIG% CACHE STRING "Use this version of swig")

include("%OOF2PREFIX%/share/oof2/templates/oofbuildtools.cmake")

find_library(OOF2COMMON oof2common %OOF2PREFIX%/lib)
find_library(OOF2ENGINE oof2engine %OOF2PREFIX%/lib)
mark_as_advanced(OOF2COMMON OOF2ENGINE)

install(
  FILES
  ${PROJECT_SOURCE_DIR}/__init__.py
  DESTINATION ${CMAKE_INSTALL_PREFIX}/%MODULENAME%)

add_subdirectory("source") # This does all the real work
