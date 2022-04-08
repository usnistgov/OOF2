cmake_minimum_required(VERSION 3.20)
project(oof2 VERSION 2.3.0)

if(NOT CMAKE_BUILD_TYPE)
  # copied blindly and naively from mathgl. 
  set(CMAKE_BUILD_TYPE "Release" CACHE STRING "Choose the build type, options are:
None(CMAKE_CXX_FLAGS or CMAKE_C_FLAGS used) Debug Release." FORCE)
endif(NOT CMAKE_BUILD_TYPE)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  set(DEBUG True)
endif(CMAKE_BUILD_TYPE STREQUAL "Debug")
  

# Set C++ version
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS False)	# use -std=c++11 instead of -gnu++11
set(CMAKE_CXX_STANDARD_REQUIRED True) # don't fall back to an earlier standard

set(BUILD_SHARED_LIBS ON)

set(CMAKE_FIND_FRAMEWORK LAST)	# Prefers MacPorts over system python

## TODO: Allow user to choose python version
#find_package(Python3 3.9 COMPONENTS Interpreter Development)
find_package(Python2 2.7 COMPONENTS Interpreter Development)
#message("PythonX is ${Python2_EXECUTABLE}")
#message("PythonX_INCLUDE_DIRS is ${Python2_INCLUDE_DIRS}")
#message("PythonX_LIBRARIES is ${Python2_LIBRARIES}")

include(FindSWIG)
include(UseSWIG)
find_package(SWIG 4.0 COMPONENTS python)

include(FindPkgConfig)
pkg_check_modules(OOFCANVAS REQUIRED oofcanvas>=1.0.1)
pkg_check_modules(MAGICK REQUIRED Magick\+\+>=6.0 Magick\+\+<7.0)
pkg_check_modules(GTK3 REQUIRED gtk+-3.0>=3.22)

include(TestForSSTREAM)		# sets CMAKE_NO_ANSI_STRING_STREAM
## TODO: Is there a non-stupid way of setting HAVE_SSTREAM?
if(NOT CMAKE_NO_ANSI_STRING_STREAM)
  set(HAVE_SSTREAM True)
endif()

add_library(oof2common MODULE)
#add_library(oof2commonGUI MODULE)
#add_library(oof2engine MODULE)
#add_library(oof2image MODULE)
#add_library(oof2orientationmap MODULE)

configure_file(
  ${PROJECT_SOURCE_DIR}/oofconfig.h.in
  ${PROJECT_BINARY_DIR}/oofconfig.h
  @ONLY	# only expand variables for the form @VAR@, not ${VAR}
  )

set(ooflibs "oof2common")#  "oof2commonGUI" oof2engine oof2image oof2orientationmap)

foreach(ooflib ${ooflibs})
  target_include_directories(${ooflib}
    PUBLIC
    "${PROJECT_BINARY_DIR}"
    "${CMAKE_CURRENT_BINARY_DIR}"
    "${PROJECT_SOURCE_DIR}/SRC"
    ## TODO: Don't add all include dirs here. Use only as required by
    ## setting property INCLUDE_DIRECTORIES on source files
    "${Python2_INCLUDE_DIRS}"
    #"${Python2_INCLUDE_DIRS}"
    "${OOFCANVAS_INCLUDE_DIRS}"
    "${MAGICK_INCLUDE_DIRS}"
    "${GTK3_INCLUDE_DIRS}"
    )
  target_link_libraries(${ooflib}
    ${Python2_LIBRARIES}
    )
endforeach()

  
add_subdirectory(SRC)
