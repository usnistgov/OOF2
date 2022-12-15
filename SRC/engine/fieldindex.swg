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
  void set(const std::vector<int>*);
  // %newobject getComponents;
  // std::vector<int> *getComponents();
  const std::string &shortstring();
};

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

// %nodefaultctor FieldIterator;

// // This adds an increment method to all FieldIterator subclasses in
// // this file and in any file that %includes or %imports this one.
// %rename(increment) FieldIterator::operator++();

// class FieldIterator : public FieldIndex {
// public:
//   int size();
//   bool end();
//   FieldIterator *cloneIterator();
//   void operator++();
// };

// class ScalarFieldIterator: public ScalarFieldIndex, public FieldIterator {
// public:
//   ScalarFieldIterator();
// };

// class VectorFieldIterator: public VectorFieldIndex, public FieldIterator {
// public:
//   VectorFieldIterator();
// };

// // class OutOfPlaneVectorFieldIterator
// //   : public OutOfPlaneVectorFieldIndex, public FieldIterator
// // {
// // public:
// //   OutOfPlaneVectorFieldIterator();
// // };

// class SymTensorIterator: public SymTensorIndex, public FieldIterator {
// public:
//   SymTensorIterator();
// };

// ADD_REPR_GENERIC(SymTensorIterator);

// class SymTensorInPlaneIterator: public SymTensorIterator {
// public:
//   SymTensorInPlaneIterator();
// };

// class SymTensorOutOfPlaneIterator: public SymTensorIterator {
// public:
//   SymTensorOutOfPlaneIterator();
// };

// class OutOfPlaneSymTensorIterator:
//   public OutOfPlaneSymTensorIndex, public FieldIterator
// {
//   OutOfPlaneSymTensorIterator();
// };


// IndexP and IteratorP objects should NOT be created directly in
// Python, because it leads to arguments over whose job it is to
// delete the enclosed FieldIndex or FieldIterator object.

%nodefaultctor IndexP;
%feature("valuewrapper") IndexP;

class IndexP {
public:
  ~IndexP();
  int integer();
  bool in_plane();
  IndexP clone();
  void set(const std::vector<int>*);
  %newobject getComponents;
  std::vector<int> *getComponents();
  const std::string &shortstring();
};

ADD_REPR_GENERIC(IndexP);

%nodefaultctor IteratorP;
%feature("valuewrapper") IteratorP;
%rename(increment) IteratorP::operator++();

class IteratorP: public IndexP {
public:
  ~IteratorP();
  bool end();
  int size();
  IteratorP cloneIterator();
  void operator++();
};

// fieldindex.spy added __iter__ and __next__ methods to IteratorP,
// making it into a real python iterator, but the code is commented
// out.  The old TODO about doing that said "Fixing this at this late
// date will be a pain".  TODO PYTHON3: Find out what broke.  If the
// iterator code in fieldindex.spy isn't resurrected, move the rest of
// that file into a %pythoncode block in this file.

// TODO INDEXING: Don't swig IteratorP and IndexP.  Make the
// underlying FieldIndex and FieldIterator classes PythonExportable,
// and swig those.  Operations like SymmMatrix.__getitem__ would
// expect a FieldIndex of the correct type, not an IndexP, and the
// index object's special methods, like SymTensorIndex.diagonal, would
// be available.  The Field, Flux, and Equation classes should be
// iterable, with __iter__ returning an appropriate FieldIndex.


%extend IteratorP {
  void __next__() {
    ++(*self);
  }
};

ADD_REPR_GENERIC(IteratorP);

%newobject getSymTensorIterator;
IteratorP *getSymTensorIterator(Planarity);

%pythoncode "engine/fieldindex.spy"

#endif // FIELDINDEX_SWG
