# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

set(CPACK_PACKAGE_DESCRIPTION_SUMMARY
  "Image-based finite element analysis of microstructures")

set(CPACK_PACKAGE_VENDOR "NIST")

set(CPACK_PACKAGE_VERSION_MAJOR
    ${PROJECT_VERSION_MAJOR}
)
set(CPACK_PACKAGE_VERSION_MINOR
    ${PROJECT_VERSION_MINOR}
)
set(CPACK_PACKAGE_VERSION_PATCH
    ${PROJECT_VERSION_PATCH}
)
set(CPACK_VERBATIM_VARIABLES YES)

if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
  set(CPACK_GENERATOR TGZ RPM DEB)
else()
  set(CPACK_GENERATOR TGZ)
endif()
message("CPACK_GENERATOR=${CPACK_GENERATOR}")

set(CPACK_SOURCE_IGNORE_FILES
  /\\.git
  SEGMENTATION
  image/GRAINBDY
  )

include(CPack)

  
