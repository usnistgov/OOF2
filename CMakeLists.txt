# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

cmake_minimum_required(VERSION 3.16)
project(oof2 VERSION 2.2.3)

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

# executable python scripts to install, after changing @PYEXEC@ to the
# full path name of the desired python version.

set(oofscripts
  oof2
  oof2-test
  oof2-guitest
  )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

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
set(PythonVersion Python2 CACHE STRING "Which Python to use")
set_property(CACHE PythonVersion PROPERTY STRINGS ${PythonVersions})

# Find Python. Set some variables so that the rest of the script
# doesn't need to know if we're using Python2 or Python3, just to make
# it easier while we're converting to Python3.
## TODO: Allow user to choose python sub version
if(PythonVersion STREQUAL "Python2")
  message("looking for Python2")
  find_package(Python2 2.7 COMPONENTS Interpreter Development)
  set(PYVERSION ${Python2_VERSION_MAJOR}.${Python2_VERSION_MINOR})
  set(PYEXEC ${Python2_EXECUTABLE})
endif()

if(PythonVersion STREQUAL "Python3")
  message("looking for Python3")
  find_package(Python3 3.9 COMPONENTS Interpreter Development)
  set(PYVERSION ${Python3_VERSION_MAJOR}.${Python3_VERSION_MINOR})
  set(PYEXEC ${Python3_EXECUTABLE})
endif()
#message("PythonX is ${Python2_EXECUTABLE}")
#message("PythonX_INCLUDE_DIRS is ${Python2_INCLUDE_DIRS}")
#message("PythonX_LIBRARIES is ${Python2_LIBRARIES}")

# Use a relative path so that DESTDIR mechanism works
set(PYDEST lib/python${PYVERSION}/site-packages/${CMAKE_PROJECT_NAME})

include(FindBLAS)
 
#include(FindSWIG)
#include(UseSWIG)
#find_package(SWIG 4.0 COMPONENTS python)
## UseSWIG can generate dependencies only for cmake >= 3.20 ? See
## https://cmake.org/cmake/help/latest/release/3.20.html

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

foreach(script ${oofscripts})
  configure_file(
  ${PROJECT_SOURCE_DIR}/${script}.in
  ${PROJECT_BINARY_DIR}/${script}
  @ONLY
  )
endforeach()

foreach(olib ${ooflibs})
  target_include_directories(${olib}
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
  target_compile_options(${olib} PRIVATE -Wno-deprecated-register)
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

# Install compiled libraries

install(
  TARGETS
  oof2common
  oof2commonGUI
  oof2engine
  oof2image
  oof2orientationmap
  DESTINATION lib)

# Install python files from SRC subdirectories, excluding SWIG output

foreach(pydir ${oofdirs})
  install(DIRECTORY SRC/${pydir}
    DESTINATION ${PYDEST}/ooflib/
    FILES_MATCHING
    PATTERN "*.py"
    PATTERN EXTRA EXCLUDE
    PATTERN DIR.py EXCLUDE # TODO: delete this line after DIR.py files go away
    )
endforeach()

# Install the top level __init__.py. I don't know if using
# configure_file is the preferred way to do this, but it works.

configure_file(
  ${PROJECT_SOURCE_DIR}/SRC/__init__.py
  ${PYDEST}/__init__.py
  COPYONLY
  )

message("PYDEST is ${PYDEST}")
configure_file(
  ${PROJECT_SOURCE_DIR}/SRC/__init__.py
  ${PYDEST}/ooflib/__init__.py
  COPYONLY
  )

# Install the start up and test wrapper scripts

install(
  PROGRAMS
  ${CMAKE_BINARY_DIR}/oof2
  ${CMAKE_BINARY_DIR}/oof2-test
  ${CMAKE_BINARY_DIR}/oof2-guitest
  DESTINATION bin)

# Install the TEST and GUITEST directories and their data

install(
  DIRECTORY TEST
  DESTINATION ${PYDEST}
  ## TODO: This will possibly install too much.  Use patterns or exclusions.
  # FILES_MATCHING 
  # PATTERN "*.py"
  # PATTERN "*.dat"
  )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Compile and install the already swigged files in SRC/SWIG2D.  This
# will change when we actually use call swig from cmake, but there's
# no point in learning how to do that with swig1.1.

set(swigsrcroot "${PROJECT_SOURCE_DIR}/SRC/SWIG2D")

function(buildswiglibs)
  # Get list of all python files in the current directory
  file(GLOB swigpyfiles
    LIST_DIRECTORIES false
    CONFIGURE_DEPENDS
    ${CMAKE_CURRENT_SOURCE_DIR} *.py)
  foreach(pfile ${swigpyfiles})
    get_filename_component(fname ${pfile} NAME_WE) # name w/out extension or dir
    if(NOT (${fname} STREQUAL __init__))
      #message("Building swig lib for ${fname}")
      get_filename_component(dname ${pfile} DIRECTORY) # full directory path
      set(libname ${fname}cmodule)
      cmake_path(RELATIVE_PATH dname BASE_DIRECTORY ${swigsrcroot})
      add_library(${libname} MODULE ${libname}.C)
      # Delete the "lib" prefix, because swig 1.1 doesn't use it
      set_target_properties(${libname} PROPERTIES PREFIX "")
      target_link_libraries(${fname}cmodule PRIVATE ${ARGV})
      target_compile_options(${fname}cmodule PRIVATE -Wno-deprecated-register)
      install(TARGETS ${fname}cmodule
	DESTINATION ${PYDEST}/ooflib/SWIG/${dname})
    endif()

  endforeach()
endfunction()

# TODO: The CMakeLists files in the SWIG2D subdirectories won't be
# needed when we're using swig properly.
add_subdirectory(SRC/SWIG2D)

# Copy the python files from the SWIG2D directory
install(
  DIRECTORY SRC/SWIG2D/
  DESTINATION ${PYDEST}/ooflib/SWIG
  FILES_MATCHING PATTERN "*.py"
  )

