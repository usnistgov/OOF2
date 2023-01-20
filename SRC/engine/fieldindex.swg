// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef FIELDINDEX_SWG
#define FIELDINDEX_SWG

%module(package="ooflib.SWIG.engine") fieldindex

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/planarity.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/fieldindex.h"
#include "common/tostring.h"

// TODO PYTHON3: Do we still need this here?
#ifndef HAVE_SSTREAM
#include <strstream.h>
#else 
#include <sstream>	
#endif // HAVE_SSTREAM
%}

%nodefaultctor FieldIndex;

class FieldIndex {
public:
  ~FieldIndex();
  int integer();
  bool in_plane();
  const std::string &shortrepr();
};

bool operator==(const FieldIndex&, const FieldIndex&);

PYTHONEXPORTABLE(FieldIndex);
ADD_REPR_GENERIC(FieldIndex);

class ScalarFieldIndex : public FieldIndex {
public:
  ScalarFieldIndex();
};

ADD_REPR_GENERIC(ScalarFieldIndex);

class VectorFieldIndex : public FieldIndex {
public:
  VectorFieldIndex(int);
};

ADD_REPR_GENERIC(VectorFieldIndex);

class OutOfPlaneVectorFieldIndex : public VectorFieldIndex {
public:
  OutOfPlaneVectorFieldIndex(int);
};

ADD_REPR_GENERIC(OutOfPlaneVectorFieldIndex);

class SymTensorIndex : public FieldIndex {
public:
  SymTensorIndex(int, int);
  int row();
  int col();
  bool diagonal();
};

ADD_REPR_GENERIC(SymTensorIndex);

class OutOfPlaneSymTensorIndex : public SymTensorIndex {
public:
  OutOfPlaneSymTensorIndex(int, int);
};

ADD_REPR_GENERIC(SymTensorIndex);

//==\\==//==\\==//==\\==//==\\==//==\\==//==\\==//==\\==//==\\==//==\\==//

%nodefaultctor ComponentIteratorP;

// The only thing we need from ComponentIteratorP is direct access to
// the FieldIndex that it's current referring to.

%nodefaultctor ComponentIteratorP;
%feature("valuewrapper") ComponentIteratorP;
%rename(increment) ComponentIteratorP::operator++;

ADD_REPR_GENERIC(ComponentIteratorP);

%{
  typedef FieldIndex NewFieldIndex;
%}

class ComponentIteratorP {
public:
  ComponentIteratorP &operator++();
  NewFieldIndex *current();
  bool operator!=(const ComponentIteratorP&) const;
};

%nodefaultctor ComponentsP;
%feature("valuewrapper") ComponentsP;

class ComponentsP {
public:
  ComponentIteratorP begin() const;
  ComponentIteratorP end() const;
};

//==\\==//==\\==//==\\==//==\\==//==\\==//==\\==//==\\==//==\\==//==\\==//

%nodefaultctor SymTensorIJIterator;
%nodefaultctor SymTensorIJComponents;
%rename(increment) SymTensorIJIterator::operator++;
%rename(getIndex) SymTensorIJIterator::operator*;

class SymTensorIJIterator {
public:
  SymTensorIJIterator &operator++();
  NewFieldIndex *fieldindex() const;
  bool operator!=(const SymTensorIJIterator&) const;
};

ADD_REPR_GENERIC(SymTensorIJIterator);

class SymTensorIJComponents {
public:
  SymTensorIJIterator begin() const;
  SymTensorIJIterator end() const;
};

extern const SymTensorIJComponents symTensorIJComponents;

%pythoncode "engine/fieldindex.spy"

#endif // FIELDINDEX_SWG
