# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

target_sources(oof2engine
  PRIVATE
  quad4.C
  quad4_8.C
  quad8.C
  quad9.C
  tri3.C
  tri6.C
  tri3_6.C
  quad4shapefunction.C
  quad4shapefunction.h
  quad8shapefunction.C
  quad8shapefunction.h
  quad9shapefunction.C
  quad9shapefunction.h
  tri3shapefunction.C
  tri3shapefunction.h
  tri6shapefunction.C
  tri6shapefunction.h
  edge2.C
  edge2shapefunction.C
  edge2shapefunction.h
  edge3.C
  edge3shapefunction.C
  edge3shapefunction.h
  edge3sub.C
  edge3super.C
  )
