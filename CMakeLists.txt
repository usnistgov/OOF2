# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

cmake_minimum_required(VERSION 3.20)
project(oof2 VERSION 2.2.3)

set(oof_build_types Debug Release)
set(CMAKE_BUILD_TYPE Release)
set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS ${oof_build_types})

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  set(DEBUG True)
endif(CMAKE_BUILD_TYPE STREQUAL "Debug")
  

# Set C++ version
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS False)	# use -std=c++11 instead of -std=gnu++11
set(CMAKE_CXX_STANDARD_REQUIRED True) # don't fall back to an earlier standard

set(BUILD_SHARED_LIBS ON)

set(CMAKE_FIND_FRAMEWORK LAST)	# Prefers MacPorts over system python

set(PythonVersions Python2 Python3)
set(PythonVersion Python3 CACHE STRING "Which Python to use")
set_property(CACHE PythonVersion PROPERTY STRINGS ${PythonVersions})

## TODO: Allow user to choose python sub version
#find_package(Python3 3.9 COMPONENTS Interpreter Development)
if(PythonVersion STREQUAL "Python2")
  message("looking for Python2")
  find_package(Python2 2.7 COMPONENTS Interpreter Development)
endif()
if(PythonVersion STREQUAL "Python3")
  message("looking for Python3")
  find_package(Python3 3.9 COMPONENTS Interpreter Development)
endif()
#message("PythonX is ${Python2_EXECUTABLE}")
#message("PythonX_INCLUDE_DIRS is ${Python2_INCLUDE_DIRS}")
#message("PythonX_LIBRARIES is ${Python2_LIBRARIES}")

include(FindBLAS)
 
#include(FindSWIG)
#include(UseSWIG)
#find_package(SWIG 4.0 COMPONENTS python)

# Use pkg-config to get info about dependencies
include(FindPkgConfig)

# MacPorts puts some pkg-config files in the python library
set(ENV{PKG_CONFIG_PATH}
  "$ENV{PKG_CONFIG_PATH}:${${PythonVersion}_LIBRARY_DIRS}/pkgconfig")
# Not sure why cmake_path(APPEND...) doesn't work.
#cmake_path(APPEND $ENV{PKG_CONFIG_PATH}
#  "${${PythonVersion}_LIBRARY_DIRS}/pkgconfig")

pkg_check_modules(OOFCANVAS REQUIRED oofcanvas>=1.0.1)
pkg_check_modules(MAGICK REQUIRED Magick\+\+>=6.0 Magick\+\+<7.0)
pkg_check_modules(GTK3 REQUIRED gtk+-3.0>=3.22)

## Dump all variables
# get_cmake_property(_variableNames VARIABLES)
# list (SORT _variableNames)
# foreach (_variableName ${_variableNames})
#     message(STATUS "${_variableName}=${${_variableName}}")
# endforeach()

include(TestForSSTREAM)		# sets CMAKE_NO_ANSI_STRING_STREAM
## TODO: Is there a non-stupid way of setting HAVE_SSTREAM?
if(NOT CMAKE_NO_ANSI_STRING_STREAM)
  set(HAVE_SSTREAM True)
endif()

## TODO: These need to be SHARED, but the swig generated libs need to
## be MODULE.  Maybe.
add_library(oof2common SHARED)
add_library(oof2commonGUI SHARED)
add_library(oof2engine SHARED)
add_library(oof2image SHARED)
add_library(oof2orientationmap SHARED)

configure_file(
  ${PROJECT_SOURCE_DIR}/oofconfig.h.in
  ${PROJECT_BINARY_DIR}/oofconfig.h
  @ONLY
  )

set(ooflibs
  oof2common
  oof2commonGUI
  oof2engine
  oof2image
  oof2orientationmap
  )

foreach(ooflib ${ooflibs})
  target_include_directories(${ooflib}
    PUBLIC
    "${PROJECT_BINARY_DIR}"
    "${CMAKE_CURRENT_BINARY_DIR}"
    "${PROJECT_SOURCE_DIR}/SRC"
    ## TODO: Don't add all include dirs here. Use only as required by
    ## setting property INCLUDE_DIRECTORIES on source files
    "${Python2_INCLUDE_DIRS}"
    #"${Python3_INCLUDE_DIRS}"
    "${OOFCANVAS_INCLUDE_DIRS}"
    "${MAGICK_INCLUDE_DIRS}"
    "${GTK3_INCLUDE_DIRS}"
    )
  target_compile_options(${ooflib} PRIVATE -Wno-deprecated-register)
endforeach()

target_compile_options(oof2image PRIVATE ${MAGICK_CFLAGS} ${OOFCANVAS_CFLAGS})
target_compile_options(oof2orientationmap PRIVATE ${MAGICK_CFLAGS})

target_link_libraries(oof2common
  PRIVATE
  ${${PythonVersion}_LIBRARIES}
  ${OOFCANVAS_LINK_LIBRARIES}
  ${BLAS_LIBRARIES}
  )

target_link_libraries(oof2commonGUI
  PRIVATE
  ${${PythonVersion}_LIBRARIES}
  ${OOFCANVAS_LINK_LIBRARIES}
  oof2common
  )

target_link_libraries(oof2engine
  PRIVATE
  ${${PythonVersion}_LIBRARIES}
  ${OOFCANVAS_LINK_LIBRARIES}
  ${BLAS_LIBRARIES}
  oof2common
  )

target_link_libraries(oof2image
  PRIVATE
  ${${PythonVersion}_LIBRARIES}
  ${OOFCANVAS_LINK_LIBRARIES}
  oof2common
  ${MAGICK_LINK_LIBRARIES}
  )

target_link_libraries(oof2orientationmap
  PRIVATE
  ${${PythonVersion}_LIBRARIES}
  ${OOFCANVAS_LINK_LIBRARIES}
  oof2common
  oof2engine
  oof2image
  ${MAGICK_LINK_LIBRARIES}
  )
  
add_subdirectory(SRC)

install(
  TARGETS
  oof2common
  oof2commonGUI
  oof2engine
  oof2image
  oof2orientationmap
  DESTINATION lib)
