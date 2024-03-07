# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# This file, SRC/EXTENSIONS/CMakeLists.txt, is used when building
# OOF2.  It shoud list all the subdirectories that contain OOF2 C,
# C++, or Python code.  Those directories must contain CMakeLists.txt
# files of their own.  For an example, see the file in the diffusion
# subdirectory.

add_subdirectory(diffusion)
add_subdirectory(ramberg_osgood)
