// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef POINTDATA_SWG
#define POINTDATA_SWG

%module(package="ooflib.SWIG.engine") pointdata

// TODO PYTHON3: Swig prints warnings when processing this file, but
// they're harmless.  The problem is that this file imports field.swg,
// which imports femesh.swg, which imports node.swg, which imports
// this file.  FuncNode, in node.swg, uses PointData as a base class,
// and PointData hasn't been defined when node.swg is imported.
// Declaring PointData here before anything else is imported doesn't
// help.  But we're not generating code for FuncNode here, so the
// warning is spurious.

%include "common/typemaps.swg"
%import "engine/field.swg"

%{
#include "engine/pointdata.h"
  #include "engine/flux.h"	// SWIGBUG
  #include "engine/node.h"	// SWIGBUG
%}

%nodefaultctor PointData;

class PointData {
public:
  bool hasField(const Field&);
  int fieldDefCount(const Field&);
  int fieldSetID();
};

#endif
