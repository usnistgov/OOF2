# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

target_sources(oof2image
  PRIVATE
  oofimage.C
  oofimage.h
  evenlyilluminate.C
  pixelselectioncourieri.C
  pixelselectioncourieri.h
  autogroup.C
  autogroup.h
  pixeldifferentiator.C
  pixeldifferentiator.h
  )
target_include_directories(oof2image
  PUBLIC
  ## TODO NUMPY: Find out how to find this directory
  /opt/local/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/numpy/core/include
  )

swig_sources(
  SWIGFILES
  autogroup
  oofimage
  pixeldifferentiator
  pixelselectioncourieri
  LIBRARIES
  oof2common
  oof2image
  INCLUDE_DIRECTORIES
  ## TODO NUMPY: Find out how to find this directory
  /opt/local/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/numpy/core/include
  )

add_subdirectory(IO)
