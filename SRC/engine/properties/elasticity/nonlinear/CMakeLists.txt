# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

target_sources(oof2engine
  PRIVATE
  general_nonlinear_elasticity.C
  general_nonlinear_elasticity.h)

swig_sources(
  SWIGFILES
  general_nonlinear_elasticity
  LIBRARIES
  oof2common
  oof2engine)
