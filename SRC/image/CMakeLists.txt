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
  autogroupMP.C
  autogroupMP.h
  pixeldifferentiator.C
  pixeldifferentiator.h
  )

# Anything that links to oofimage.h has to be compiled with the
# ImageMagick flags.
set_source_files_properties(
  oofimage.h
  DIRECTORY ${PROJECT_SOURCE_DIR}
  PROPERTIES
  COMPILE_OPTIONS ${MAGICK_CFLAGS})

add_subdirectory(IO)
