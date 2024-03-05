# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

target_sources(oof2orientationmap
  PRIVATE
  orientmapdata.C
  orientmapdata.h
  orientmapproperty.C
  orientmapproperty.h
  polefigure.C
  polefigure.h
  pixelselectioncouriero.C
  pixelselectioncouriero.h
  pixeldifferentiatoro.C
  pixeldifferentiatoro.h)

oof_swig_sources(
  SWIGFILES
  orientmapdata
  orientmapproperty
  pixeldifferentiatoro
  pixelselectioncouriero
  polefigure
  LIBRARIES
  oof2common
  oof2orientationmap
  oof2engine)

add_subdirectory(GUI)
