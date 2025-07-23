# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.


target_sources(
  # New material properties should be added to the oof2engine library.
  oof2engine
  PRIVATE
  # The C++ source files in this directory must be listed here.
  diffusion.C
  diffusion.h
  charge.C
  charge.h
  ion.C
  ion.h
  )

oof_swig_sources(
  SWIGFILES
  # The swig source files in this directory must be listed here.
  # Don't include the filename suffix.  The suffix must be either ".i"
  # or ".swg".
  charge
  diffusion
  ion
  LIBRARIES
  # The oof2 libraries that the source files refer to must be listed
  # here.
  oof2common
  oof2engine)

# Python files with a ".py" suffix will be included automatically.

# If there are subdirectories that should be included, add
# "add_subdirectory()" lines for them here.  The subdirectories must
# contain their own CMakeLists.txt files.
