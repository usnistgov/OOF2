# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

cmake_minimum_required(VERSION 3.18)
project(oof2 VERSION 2.3.3)

# cmake functions and settings that are used both by oof2 and oof2
# extensions are in oofbuildtools.cmake so that the extensions can
# include them easily.
include("oofbuildtools.cmake")


# If OOF2 is being installed by a regular user, the python files
# should be installed into lib/pythonX.Y/site-packages/oofcanvas,
# which is probably in /usr/local or the user's home directory.  But
# if it's being installed by MacPorts or another package manager they
# should be installed in
# ${Python3_LIBRARY_DIRS}/pythonX.Y/site-packages.  The package
# manager should set OOF2_SYSTEM_INSTALL to ON, which will cause
# the files to be installed under Python3_LIBRARY_DIRS.
option(OOF2_SYSTEM_INSTALL OFF "Install in system directory?")
mark_as_advanced(OOF2_SYSTEM_INSTALL)

option(OOF2_DEV_INSTALL OFF "Install development files?")


## TODO PYTHON3: Get openMP working. See the openmp-branch branch.

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# OOF2/SRC subdirectories containing python files to install.  The
# entire hierarchies under these will be installed in
# .../site-packages/oof2/ooflib.

set(oofdirs
  common
  engine
  image
  orientationmap
  tutorials
  EXTENSIONS
  )

# OOF2 libraries to build

set(ooflibs
  oof2common
  oof2commonGUI
  oof2engine
  oof2image
  oof2orientationmap
  )

# executable python scripts to install

set(oofscripts
  oof2
  oof2-test
  oof2-guitest
  )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Required version numbers for dependencies

set(OOFCANVAS_MIN_VERSION 1.1.2)
set(MAGICK_MIN_VERSION 6.0.0)
set(MAGICK_MAX_VERSION 7.0.0)
set(GTK3_MIN_VERSION 3.22)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

include(FindBLAS)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# SITE_PACKAGES is used to set the path in oof2.in, oof2-test.in and
# oof2-guitest.in so that users can run the top level scripts without
# setting PYTHONPATH.
if(OOF2_SYSTEM_INSTALL)
  set(SITE_PACKAGES ${Python3_LIBRARY_DIRS}/${PYLIBPATH})
else()
  set(SITE_PACKAGES lib/${PYLIBPATH})
endif()
# PYDEST is the destination for installing OOF2 python files.
set(PYDEST ${SITE_PACKAGES}/${CMAKE_PROJECT_NAME})

# message("PYDEST is ${PYDEST}")
# message("SITE_PACKAGES is ${SITE_PACKAGES}")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Use pkg-config to get info about dependencies
include(FindPkgConfig)
# Update the pkgconfig search path
# MacPorts puts some pkg-config files in the python library
if(APPLE)
  set(ENV{PKG_CONFIG_PATH}
    "$ENV{PKG_CONFIG_PATH}:${Python3_LIBRARY_DIRS}/pkgconfig")
endif()
# Look in the anaconda directory if necessary
if($ENV{CONDA_PREFIX})
  set(ENV{PKG_CONFIG_PATH}
    "$ENV{PKG_CONFIG_PATH}:$ENV{CONDA_PREFIX}/lib/pkgconfig")
endif()

# TODO: OOFCanvas was probably installed with the same prefix, so it
# would be nice to add CMAKE_INSTALL_PREFIX/lib/pkgconfig to
# PKG_CONFIG_PATH here, and not require users to set PKG_CONFIG_PATH
# themselves.  But when ccmake opens this file for the first time,
# CMAKE_INSTALL_PREFIX is not set, and so oofcanvas is not found.  I
# don't know how to delay the pkg_check_modules call until after
# CMAKE_INSTALL_PREFIX is set.
#   if(EXISTS ${CMAKE_INSTALL_PREFIX}/lib/pkgconfig/oofcanvas.pc})
#     set(ENV{PKG_CONFIG_PATH}
#       "$ENV{PKG_CONFIG_PATH}:${CMAKE_INSTALL_PREFIX}/lib/pkgconfig")
#   endif()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

pkg_check_modules(
  OOFCANVAS REQUIRED
  oofcanvas>=${OOFCANVAS_MIN_VERSION})
list(APPEND CMAKE_INSTALL_RPATH ${OOFCANVAS_LIBDIR})

## Dump all variables
# get_cmake_property(_variableNames VARIABLES)
# list (SORT _variableNames)
# foreach (_variableName ${_variableNames})
#     message(STATUS "${_variableName}=${${_variableName}}")
# endforeach()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

pkg_check_modules(
  MAGICK REQUIRED
  Magick\+\+>=${MAGICK_MIN_VERSION}
  Magick\+\+<${MAGICK_MAX_VERSION})

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

pkg_check_modules(
  GTK3 REQUIRED
  gtk+-3.0>=${GTK3_MIN_VERSION})

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

include(TestForSSTREAM)		# sets CMAKE_NO_ANSI_STRING_STREAM
## TODO: Is there a non-stupid way of setting HAVE_SSTREAM?
if(NOT ${CMAKE_NO_ANSI_STRING_STREAM})
  set(HAVE_SSTREAM True)
endif()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Create the shared library targets, which are listed in the ooflibs
# macro defined above.

foreach(olib ${ooflibs})
  add_library(${olib} SHARED)
  target_include_directories(${olib}
    PRIVATE
    ${PROJECT_BINARY_DIR}
    ${CMAKE_CURRENT_BINARY_DIR}
    ${PROJECT_SOURCE_DIR}/SRC
    ## TODO: Don't add all include dirs here. Use only as required by
    ## setting property INCLUDE_DIRECTORIES on source files
    ${Python3_INCLUDE_DIRS} 
    ${OOFCANVAS_INCLUDE_DIRS}
    ${MAGICK_INCLUDE_DIRS}
    ${GTK3_INCLUDE_DIRS}
    )
  # It's necessary to include OOFCANVAS_CFLAGS for all files that
  # include oofcanvas.h, because oofcanvas.h indirectly includes
  # ImageMagick headers, and ImageMagick complains bitterly if
  # MAGICKCORE_QUANTUM_DEPTH isn't defined.  OOFCANVAS_CFLAGS includes
  # the ImageMagick preprocessor definitions that it used.  This
  # results in the ImageMagick definitions being used in far more
  # places than actually necessary, which is messy but probably
  # harmless.
  target_compile_options(${olib}
    PRIVATE
    -Wno-deprecated-register
    ${OOFCANVAS_CFLAGS})
endforeach()

# oofconfig.h is used when building oof2, but is not installed.
configure_file(
  ${PROJECT_SOURCE_DIR}/oofconfig.h.in
  ${PROJECT_BINARY_DIR}/oofconfig.h
  @ONLY
  )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Create swigruntime.h by running "swig -external-runtime". The
# dependence of oofswigruntime.h on swigruntime.h is set explicitly in
# SRC/common/CMakeLists.txt.

add_custom_command(
  OUTPUT swigruntime.h
  COMMAND ${SWIG_EXECUTABLE} -python -external-runtime swigruntime.h
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

foreach(script ${oofscripts})
  configure_file(
  ${PROJECT_SOURCE_DIR}/${script}.in
  ${PROJECT_BINARY_DIR}/${script}
  @ONLY
  )
endforeach()

target_link_libraries(oof2common
  PRIVATE
  ${Python3_LIBRARIES}
  ${OOFCANVAS_LINK_LIBRARIES}
  ${BLAS_LIBRARIES}
  )

target_link_libraries(oof2commonGUI
  PRIVATE
  ${Python3_LIBRARIES}
  ${OOFCANVAS_LINK_LIBRARIES}
  oof2common
  )

target_link_libraries(oof2engine
  PRIVATE
  ${Python3_LIBRARIES}
  ${OOFCANVAS_LINK_LIBRARIES}
  ${BLAS_LIBRARIES}
  oof2common
  )

target_link_libraries(oof2image
  PRIVATE
  ${Python3_LIBRARIES}
  ${OOFCANVAS_LINK_LIBRARIES}
  oof2common
  ${MAGICK_LINK_LIBRARIES}
  )

target_link_libraries(oof2orientationmap
  PRIVATE
  ${Python3_LIBRARIES}
  ${OOFCANVAS_LINK_LIBRARIES}
  oof2common
  oof2engine
  oof2image
  ${MAGICK_LINK_LIBRARIES}
  )
  
add_subdirectory(SRC)

# Install compiled libraries

install(
  TARGETS
  oof2common
  oof2commonGUI
  oof2engine
  oof2image
  oof2orientationmap
  DESTINATION ${CMAKE_INSTALL_LIBDIR})

# Install python files from SRC subdirectories, excluding SWIG output

foreach(pydir ${oofdirs})
  install(DIRECTORY SRC/${pydir}
    DESTINATION ${PYDEST}/ooflib/
    FILES_MATCHING
    PATTERN "*.py"
    PATTERN EXTRA EXCLUDE
    )
endforeach()

# Create and install the top level __init__.py files. 

file(TOUCH ${PROJECT_BINARY_DIR}/__init__.py)

install(
  FILES
  ${PROJECT_BINARY_DIR}/__init__.py
  DESTINATION ${PYDEST}
  )

install(
  FILES
  ${PROJECT_BINARY_DIR}/__init__.py
  DESTINATION ${PYDEST}/ooflib
  )
  
# Install the start up and test wrapper scripts

install(
  PROGRAMS
  ${CMAKE_BINARY_DIR}/oof2
  ${CMAKE_BINARY_DIR}/oof2-test
  ${CMAKE_BINARY_DIR}/oof2-guitest
  DESTINATION ${CMAKE_INSTALL_BINDIR})

# Install the TEST and GUITEST directories and their data

install(
  DIRECTORY TEST
  DESTINATION ${PYDEST}
  PATTERN "*~" EXCLUDE
  PATTERN "NOTES" EXCLUDE
  )

# Install examples into <prefix>/share/oof2/examples
install(
  DIRECTORY examples
  DESTINATION ${CMAKE_INSTALL_DATADIR}/oof2
  )


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Machinery for building extensions.  Everything that an extension
# might require from the oof2 source directory has to be installed
# somewhere under CMAKE_INSTALL_PREFIX because the source directory
# might not be available when a user is building an extension.  If
# oof2 was installed via a package manager, the source directory might
# not have ever been installed.

# Create the script for creating the structure of an extension and
# install it into bin.

if(OOF2_DEV_INSTALL)

  # configure  oof2-extension-setup and install it into bin
  configure_file(
    ${PROJECT_SOURCE_DIR}/EXTENSION_TEMPLATES/oof2-extension-setup.in
    ${PROJECT_BINARY_DIR}/oof2-extension-setup
    @ONLY
  )
  install(
    PROGRAMS
    ${CMAKE_BINARY_DIR}/oof2-extension-setup
    DESTINATION ${CMAKE_INSTALL_BINDIR}
  )

  # Install the extension templates into share/oof2/templates.
  install(
    DIRECTORY EXTENSION_TEMPLATES/ # trailing slash means copy subdirectories
    DESTINATION share/oof2/templates
    PATTERN "oof2-extension-setup.in" EXCLUDE
    PATTERN "TODO" EXCLUDE
  )

  # Install the oof2 header and swig files into include/oof2.
  set(headerdirs common engine image orientationmap) # dirs with headers
  foreach(headerdir ${headerdirs})
    install(
      DIRECTORY ${PROJECT_SOURCE_DIR}/SRC/${headerdir}/
      DESTINATION include/oof2/${headerdir}
      FILES_MATCHING REGEX ".*\\.(h|swg|spy)$"
    )
  endforeach()
  # Copy oofconfig.h from the build directory.
  install(
    FILES ${PROJECT_BINARY_DIR}/oofconfig.h
    DESTINATION include/oof2
    )

  # Install the cmake functions (also used in this file) into
  # share/oof2/templates
  install(
    FILES ${PROJECT_SOURCE_DIR}/oofbuildtools.cmake
    DESTINATION share/oof2/templates
  )

endif()  # OOF2_DEV_INSTALL

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Packaging

# Don't use cmake's packaging tools because I couldn't get them to
# work and we have a perfectly good make_dist script from the old
# days.  But in order to ensure that the version number used by the
# script is the same as the version number defined here, the script is
# created from make_dist.in.  Check that the file exists because
# make_dist.in isn't itself included in the distribution.

if(EXISTS "${PROJECT_SOURCE_DIR}/make_dist.in")
  configure_file(
    ${PROJECT_SOURCE_DIR}/make_dist.in
    ${PROJECT_BINARY_DIR}/make_dist
    @ONLY
  )
endif()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Add an "uninstall" target.  Copied from
# https://gitlab.kitware.com/cmake/community/-/wikis/FAQ#can-i-do-make-uninstall-with-cmake

if(NOT TARGET uninstall)
  configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake_uninstall.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake"
    IMMEDIATE @ONLY)

  add_custom_target(uninstall
    COMMAND ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake)
endif()
