# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# This file contains cmake function definitions and other code that is
# used when building oof2 but are also used when building extensions.
# They're in a separate file so that they can be shared easily.


set(OOF2_SWIG_VERSION 4.1 CACHE STRING "Use this version of swig")
set_property(CACHE OOF2_SWIG_VERSION PROPERTY STRINGS 4.0 4.1 4.2)

# The initial value of OOF2_PYTHON3_VERSION is "Latest" so that the
# initial configuration pass doesn't raise an error if the requested
# version isn't found.
## TODO: Can we list only the available versions of swig and python?
set(OOF2_PYTHON3_VERSION "Latest" CACHE STRING "Use this version of Python")
set_property(CACHE OOF2_PYTHON3_VERSION PROPERTY STRINGS
  3.8 3.9 3.10 3.11 3.12 Latest)


include(GNUInstallDirs)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Set the build type.

# These are the build types that we support:
set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS Debug Release)

# Set the default build type.  See
# https://www.kitware.com/cmake-and-the-default-build-type/
set(default_build_type "Release")
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE
    STRING "Debug or Release" FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release")
endif()

# Apparently using -DDEBUG for debugging is not the modern
# convention. CMake instead assumes that we're using -DNDEBUG when not
# debugging, so add -DDEBUG here.
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Set C++ version
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS False)	# use -std=c++11 instead of -std=gnu++11
set(CMAKE_CXX_STANDARD_REQUIRED True) # don't fall back to an earlier standard

set(BUILD_SHARED_LIBS ON)

# On macOS 12, we need to set RPATH or libraries installed outside the
# default locations won't be found.
set(CMAKE_INSTALL_RPATH ${CMAKE_INSTALL_PREFIX}/lib)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

include(FindSWIG)
include(UseSWIG)
find_package(SWIG ${OOF2_SWIG_VERSION} COMPONENTS python)
## UseSWIG can generate dependencies only for cmake >= 3.20.  Setting
## the flag for it is harmless even if it doesn't always work.
set(SWIG_USE_SWIG_DEPENDENCIES True)
set(UseSWIG_TARGET_NAME_PREFERENCE STANDARD)
set(SWIG_SOURCE_FILE_EXTENSIONS ".swg" ".i")
if(${SWIG_VERSION} VERSION_LESS "4.1")
  set(CMAKE_SWIG_FLAGS -py3)
endif()
# add_compile_definitions(SWIG_TYPE_TABLE=oof2)
if(${SWIG_USE_BUILTIN})		# wishful thinking
  list(APPEND CMAKE_SWIG_FLAGS -builtin)
endif()
# UseSWIG doesn't seem to use -DNDEBUG or -DDEBUG when calling
# swig.  This has to be set with a generator expression because
# CMAKE_BUILD_TYPE can't be evaluated reliably at this time.
list(APPEND CMAKE_SWIG_FLAGS $<$<CONFIG:Debug>:-DDEBUG>)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Find dependencies

# Find Python3.

# Without this line, cmake finds the system python on Mac even if
# MacPorts is installed.  With this line, it finds MacPorts' python,
# whether the argument is FIRST or LAST. This confuses me.  If
# Python_FIND_FRAMEWORK is used instead, it seems to always find the
# system python.
set(CMAKE_FIND_FRAMEWORK LAST)

include(FindPython)
if(${OOF2_PYTHON3_VERSION} STREQUAL "Latest")
  find_package(Python3 COMPONENTS Interpreter Development)
else()
  find_package(
    Python3 ${OOF2_PYTHON3_VERSION} EXACT
    COMPONENTS Interpreter Development)
endif()
set(PYVERSION ${Python3_VERSION_MAJOR}.${Python3_VERSION_MINOR})

# message("Python3 is ${Python3_EXECUTABLE}")
# message("Python3_INCLUDE_DIRS is ${Python3_INCLUDE_DIRS}")
# message("Python3_LIBRARIES is ${Python3_LIBRARIES}")
# message("Python3_LIBRARY_DIRS is ${Python3_LIBRARY_DIRS}")
# message("Python3_RUNTIME_LIBRARY_DIRS is ${Python3_RUNTIME_LIBRARY_DIRS}")
# message("Python3_SITELIB is ${Python3_SITELIB}")

# SITE_PACKAGES is used to set the path in oof2.in, oof2-test.in and
# oof2-guitest.in so that users can run the top level scripts without
# setting PYTHONPATH.
set(PYLIBPATH python${Python3_VERSION_MAJOR}.${Python3_VERSION_MINOR}/site-packages)
if(OOF2_SYSTEM_INSTALL)
  set(SITE_PACKAGES ${Python3_LIBRARY_DIRS}/${PYLIBPATH})
else()
  set(SITE_PACKAGES lib/${PYLIBPATH})
endif()
# PYDEST is the destination for installing OOF2 python files.
set(PYDEST ${SITE_PACKAGES}/${CMAKE_PROJECT_NAME})

# message("PYDEST is ${PYDEST}")
# message("SITE_PACKAGES is ${SITE_PACKAGES}")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Call swig_sources in the CMakeLists.txt files in all subdirectories
# that contain swig files.
#  swig_sources(
#        SWIGFILES  a b      # .swg suffix is assumed
#     optional arguments
#        LIBRARIES  <names of libraries to link to, must be cmake targets>
#        CFLAGS <additional compiler options>)
#        INCLUDE_DIRECTORIES <additional directories to search for C++ headers>
#        TARGET_SFX <suffix to use for the cmake target.  See below>
#  )

function(swig_sources)
  set(multiValueArgs SWIGFILES LIBRARIES CFLAGS INCLUDE_DIRECTORIES TARGET_SFX)
  cmake_parse_arguments(PARSE_ARGV 0 SS "" "" "${multiValueArgs}")
  #                                  ^ "SS" for Swig_Sources

  foreach(swigfile ${SS_SWIGFILES})
    set_property(
      SOURCE ${swigfile}.swg
      PROPERTY CPLUSPLUS ON)
    # Set include directories for the swig command.
    set_property(
      SOURCE ${swigfile}.swg
      PROPERTY INCLUDE_DIRECTORIES
      ${CMAKE_CURRENT_SOURCE_DIR}
      ${PROJECT_SOURCE_DIR}/SRC
      ${SS_INCLUDE_DIRECTORIES})
    # Set include directories for the compiler
    set_property(
      SOURCE ${swigfile}.swg
      PROPERTY GENERATED_INCLUDE_DIRECTORIES
      ${SS_INCLUDE_DIRECTORIES}
      ${CMAKE_CURRENT_SOURCE_DIR}
      ${PROJECT_SOURCE_DIR}/SRC
      ${PROJECT_BINARY_DIR}	# for headers generated by configure_file
      ${PYINCL}
      ${Python3_INCLUDE_DIRS})
    set_property(
      SOURCE ${swigfile}.swg
      PROPERTY GENERATED_COMPILE_OPTIONS
      "${SS_CFLAGS}"
      "${OOFCANVAS_CFLAGS}"
    )

    if(SS_TARGET_SFX)
      # If the TARGET_SFX argument is supplied, append it to
      # ${swigfile} to create the target name, although the installed
      # name will still be ${swigfile}.  This allows us to build two
      # modules with the same names but different locations, despite
      # the fact that cmake requires all target names to be unique.
      set(TARGET ${swigfile}${SS_TARGET_SFX}) # create a unique target name
      # set_property(			      # but don't use it for the files
      # 	SOURCE ${swigfile}.swg
      # 	PROPERTY OUTPUT_NAME
      # 	${swigfile})	 # *not* ${TARGET}, which has the suffix added
    else()
      set(TARGET ${swigfile})
    endif()

    swig_add_library(
      ${TARGET}
      TYPE MODULE
      LANGUAGE PYTHON
      SOURCES ${swigfile}.swg)

    target_link_libraries(
      ${TARGET}
      PRIVATE
      ${Python3_LIBRARIES}
      ${SS_LIBRARIES}
      ${OOFCANVAS_LINK_LIBRARIES}
      )

    # Get the path from the top of the source directory hierarchy to
    # the current directory.  This is the path from the top of the
    # installation directory hierarchy to the installation directory
    # for the compiled swig output and python file.

    # file(RELATIVE_PATH ...) has been superseded by cmake_path(...)
    # in cmake 3.20, but 3.20 isn't available on Ubuntu 20.04.
    if(${CMAKE_VERSION} VERSION_LESS "3.20")
      file(
	RELATIVE_PATH relpath	     # this is the path ...
	${PROJECT_SOURCE_DIR}/SRC    # ... from here ...
	${CMAKE_CURRENT_SOURCE_DIR}) # ... to here
    else()
      set(relpath ${CMAKE_CURRENT_SOURCE_DIR})
      cmake_path(
	RELATIVE_PATH
	relpath			# Change this path ...
	BASE_DIRECTORY ${PROJECT_SOURCE_DIR}/SRC) # ... to be relative to this
    endif()
    # Install the swig-generated and compiled library
    install(
      TARGETS ${TARGET}
      DESTINATION ${PYDEST}/ooflib/SWIG/${relpath})
    # Install the swig-generated python file
    install(
      FILES ${CMAKE_CURRENT_BINARY_DIR}/${swigfile}.py
      DESTINATION ${PYDEST}/ooflib/SWIG/${relpath})
  endforeach()

endfunction()
