# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

target_sources(oof2common
  PRIVATE
  abstractimage.h
  activearea.C
  activearea.h
  argv.C
  argv.h
  array.h
  bitmask.C
  bitmask.h
  boolarray.C
  boolarray.h
  brushstyle.C
  brushstyle.h
  burn.C
  burn.h
  cachedvalue.h
  ccolor.C
  ccolor.h
  cdebug.C
  cdebug.h
  chunkyvector.h
  cleverptr.h
  cmicrostructure.C
  cmicrostructure.h
  colordifference.C
  colordifference.h
  coord.C
  coord.h
  cpixelselection.C
  cpixelselection.h
  despeckle.C
  direction.C
  direction.h
  doublearray.h
  doublevec.C
  doublevec.h
  expandgrp.C
  geometry.h
  guitop.C
  guitop.h
  identification.C
  identification.h
  intarray.C
  intarray.h
  latticesystem.C
  latticesystem.h
  lock.C
  lock.h
  ooferror.C
  ooferror.h
  oofomp.h
  oofswigruntime.h
  pixelattribute.C
  pixelattribute.h
  pixelgroup.C
  pixelgroup.h
  pixelselectioncourier.C
  pixelselectioncourier.h
  pixelsetboundary.C
  pixelsetboundary.h
  printvec.h
  progress.C
  progress.h
  pythonexportable.h
  pythonlock.h
  pyutils.C
  pyutils.h
  random.C
  random.h
  removeitem.h
  sincos.C
  sincos.h
  smallmatrix.C
  smallmatrix.h
  statgroups.C
  statgroups.h
  switchboard.C
  switchboard.h
  threadstate.C
  threadstate.h
  timestamp.C
  timestamp.h
  tostring.h
  trace.C
  trace.h
)

# oofswigruntime.h depends on swigruntime.h.  Because swigruntime.h is
# the output of a custom command the dependency isn't picked up by the
# usual methods.
set_property(
  SOURCE oofswigruntime.h
  DIRECTORY ${PROJECT_SOURCE_DIR}
  PROPERTY OBJECT_DEPENDS swigruntime.h
)

swig_sources(
  SWIGFILES
  abstractimage
  activearea
  argv
  boolarray
  brushstyle
  burn
  ccolor
  cdebug
  cmicrostructure
  colordifference
  config
  coord
  cpixelselection
  crandom
  direction
  doublearray
  doublevec
  geometry
  guitop
  identification
  intarray
  latticesystem
  lock
  # mpitools  ## TODO: Add an mpi compilation option 
  ooferror
  oofversion
  pixelattribute
  pixelgroup
  pixelselectioncourier
  pixelsetboundary
  progress
  smallmatrix
  statgroups
  switchboard
  threadstate
  timestamp
  trace
  LIBRARIES
  oof2common)

add_subdirectory(IO)
