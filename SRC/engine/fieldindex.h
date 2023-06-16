// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef FIELDINDEX_H
#define FIELDINDEX_H

// Classes for referring to the components of a field, flux, or
// equation.  Different subtypes of FieldIndex are used to index
// different types of Fields (scalars, vectors, tensors, etc).  Having
// different types all derived from a common base class allows the
// same code to handle scalars, vectors, and tensors.  The base class
// is called 'FieldIndex' because it's commonly used to choose the
// components of a Field, and because
// 'FieldFluxEquationOrOtherIndexableObjectIndex' is too long.  In
// this discussion, the word "Field" almost always means "Field, Flux,
// Equation, or ...".

// Code that operates on generic Fields needs to use pointers to
// FieldIndexes, in order to access the virtual functions.  We need to
// be able to pass those pointers around without worrying about when
// the index they point to should be deleted.  The IndexP (P for
// "pointer") class wraps a FieldIndex pointer, allows access to the
// virtual FieldIndex methods, and takes care of deleting the
// FieldIndex.  Because IndexP is a lightweight object, containing
// only a pointer, it can be passed around freely.  Its copy
// constructor does have to allocate a new FieldIndex object, but it
// has a move constructor that doesn't involve any allocation.

// An IndexP can be converted to a FieldIndex* or FieldIndex&, so it
// can be used as an argument to any function that expects a
// FieldIndex* or FieldIndex&.

// We often want to iterate over all components of a Field, ie, loop
// over all the possible values of a FieldIndex.  For each type of
// Field, there is a subclass of ComponentIterator.  A
// ComponentIterator is like an STL forward iterator.  It can be
// incremented with operator++ and dereferenced with operator*, which
// returns an IndexP.  ComponentIterator pointers are wrapped in a
// generic ComponentIteratorP class, which is analogous to IndexP.

// For each type of Field, there is a Components subclass whose only
// purpose is to serve as the container that the iterator iterates
// over.  It has begin() and end() methods that return an appropriate
// ComponentIteratorP.  Each Field has a components() method that
// returns a ComponentsP object, which wraps Components like IndexP
// wraps FieldIndex.  Since the Components classes don't contain any
// data and aren't actually changed in any way when they're iterated
// over, the Fields contain static instances of their Components
// subclass and ComponentsP doesn't have to worry about allocation.

// So, to iterate over a Field's components in C++, you treat the
// return value of Field::components like an STL forward-iterable
// container of IndexPs:
//
//   for(ComponentIteratorP iter = field->components().begin();
//       iter != field->components().end();
//       ++iter)
//   {
//      IndexP index = *iter;
//      ...
//   }
//
// or, equivalently and more simply,
//
//   for(IndexP index: field->components()) {
//      ...
//   }

// The components() methods for Fields and Fluxes take an optional
// Planarity argument, which controls whether or not the iterators
// include the out-of-plane components.  If the argument is omitted,
// ALL_INDICES is assumed.

// You can iterate over the components of a Field in Python with:
//
//   for index in field.components():
//        # index is an instance of a swigged FieldIndex subclass
//
// In Python, Field.components() is a generator function that uses the
// begin() and end() methods of the ComponentsP object, which it
// obtains by calling the C++ Field::components() method.  (There's a
// little bit of swig renaming trickery involved so that the C++
// components() method and the Python components() method can have the
// same name but be different things. See the %rename statements in
// field.swg) The index is a swigged FieldIndex of the appropriate
// subclass, because FieldIndex is derived from PythonExportable.
// (Components and ComponentIterator don't have be be
// PythonExportable, and there's no need in Python for IndexP,
// ComponentIteratorP, or ComponentsP.)

#include <iostream>
#include <string>
#include <vector>
#include "common/pythonexportable.h"
#include "engine/indextypes.h"
#include "engine/planarity.h"

class Components; // iterator over the components of a Field, Flux or Equation
class ComponentsP;	     // wrapper around a pointer to Components

class FieldIndex : public PythonExportable<FieldIndex> {
public:
  FieldIndex() {}
  virtual ~FieldIndex() { }
  virtual FieldIndex *clone() const = 0; // create a copy

  // The possible values of the index must be ordered in some
  // (possibly arbitrary) way, so that, for example, the corresponding
  // degrees of freedom of a Field at a Node can be listed in order.
  // FieldIndex::integer() returns the rank of the index in this
  // arbitrary ordering.  For example, the VectorFieldIndex just
  // returns the value of the index, and the SymTensorIndex returns
  // the index's Voigt representation.
  virtual int integer() const = 0;

  // in_plane() is false if the index represents an out-of-plane
  // component of a field.  This doesn't make sense in some
  // subclasses, but it can be ignored there.  See the TODO in
  // outputval.h.
  virtual bool in_plane() const { return true; }

  virtual void print(std::ostream &os) const = 0;
  virtual const std::string &shortrepr() const = 0;
};

std::ostream &operator<<(std::ostream &os, const FieldIndex &fi);

// operator== should only be used in contexts where it's clear that
// the two FieldIndices have the same subclass.

bool operator==(const FieldIndex&, const FieldIndex&);

// The ScalarFieldIndex has no value, which is not to say that it is
// worthless.  It just doesn't do anything.

class ScalarFieldIndex : public FieldIndex {
public:
  ScalarFieldIndex() {}
  virtual ~ScalarFieldIndex() {}
  virtual const std::string &classname() const;
  virtual FieldIndex *clone() const { return new ScalarFieldIndex; }
  virtual int integer() const { return 0; }
  virtual bool in_plane() const { return true; }
  virtual void print(std::ostream&) const;
  virtual const std::string &shortrepr() const;
};


// The VectorFieldIndex stores a single int.

class VectorFieldIndex : public FieldIndex {
protected:
  int index_;
public:
  VectorFieldIndex() : index_(0) {}
  VectorFieldIndex(SpaceIndex i) : index_(i) {}
  VectorFieldIndex(const VectorFieldIndex &o) : index_(o.index_) {}
  virtual ~VectorFieldIndex() {}
  virtual const std::string &classname() const;
  virtual FieldIndex *clone() const { return new VectorFieldIndex(*this); }
  virtual int integer() const { return index_; }
  virtual bool in_plane() const { return index_ < 2; }
  virtual void print(std::ostream&) const;
  virtual const std::string &shortrepr() const;
  friend class VectorFieldCompIterator;
};

// The OutOfPlaneVectorFieldIndex is a VectorFieldIndex that only
// represents the out-of-plane part of the vector field.  The only
// substantial difference is in the integer function, which says that
// the 2 (z) component is the first component.

class OutOfPlaneVectorFieldIndex : public VectorFieldIndex {
public:
  OutOfPlaneVectorFieldIndex() : VectorFieldIndex(2) {}
  OutOfPlaneVectorFieldIndex(SpaceIndex i) : VectorFieldIndex(i) {}
  virtual const std::string &classname() const;
  virtual int integer() const { return index_ - 2; }
  virtual FieldIndex *clone() const {
    return new OutOfPlaneVectorFieldIndex(*this);
  }
};

// The SymTensorIndex stores the Voigt representation of the ij index
// of a 3x3 symmetric tensor.  i and j can be retrieved with the row()
// and col() functions.

//  i j  Voigt
//  0 0  0
//  1 0  5
//  1 1  1
//  2 0  4
//  2 1  3
//  2 2  2

// TODO: Use a separate variety of IndexType for a Voigt index?  Get
// rid of IndexType completely and just use int?

class SymTensorIndex : public FieldIndex {
protected:
  int v;			// voigt index
public:
  SymTensorIndex() : v(0) {}
  SymTensorIndex(int i) : v(i) {}
  SymTensorIndex(SpaceIndex i, SpaceIndex j) : v(i==j? int(i) : int(6-i-j)) {}
  SymTensorIndex(const SymTensorIndex &o) : v(o.v) {}
  virtual ~SymTensorIndex() {}
  virtual const std::string &classname() const;
  virtual FieldIndex *clone() const { return new SymTensorIndex(*this); }
  virtual int integer() const { return v; }
  int row() const;		// i
  int col() const;		// j
  bool diagonal() const { return v < 3; }
  virtual bool in_plane() const { return v < 2 || v == 5; }
  virtual void print(std::ostream&) const;
  static int ij2voigt(int i, int j) { return ( i==j ? i : 6-i-j ); }
  // The argument str in str2voigt must be "pq" where p and q are in
  // ('x', 'y', 'z')
  static int str2voigt(const std::string &str) {
    return ij2voigt(str[0]-'x', str[1]-'x');
  }
  virtual const std::string &shortrepr() const;
};

// See comment above wrt OutOfPlaneVectorFieldIndex.

class OutOfPlaneSymTensorIndex : public SymTensorIndex {
public:
  OutOfPlaneSymTensorIndex() : SymTensorIndex(2) {}
  OutOfPlaneSymTensorIndex(SpaceIndex i) : SymTensorIndex(i) {}
  OutOfPlaneSymTensorIndex(SpaceIndex i, SpaceIndex j) : SymTensorIndex(i,j) {}
  virtual const std::string &classname() const;
  virtual FieldIndex *clone() const {
    return new OutOfPlaneSymTensorIndex(*this);
  }
  virtual int integer() const { return v - 2; }
};


// Wrapper class so that Fluxes and Fields can return an appropriate
// type of FieldIndex, other classes don't have to worry about
// deallocating it, and the virtual functions still work.

class IndexP {
protected:
  FieldIndex *fieldindex;
public:
  IndexP(FieldIndex *i) : fieldindex(i) {}
  IndexP(const IndexP &o) : fieldindex(o.fieldindex->clone()) {}
  IndexP(IndexP &&o) : fieldindex(o.fieldindex) { o.fieldindex = nullptr; }
  ~IndexP() { delete fieldindex; }
  int integer() const { return fieldindex->integer(); }
  bool in_plane() const { return fieldindex->in_plane(); }
  // Allow IndexP to be used where a FieldIndex& or FieldIndex* is expected
  operator const FieldIndex&() const { return *fieldindex; }
  operator const FieldIndex*() const { return fieldindex; }
  IndexP clone() const {
    return IndexP(fieldindex->clone());
  }
  const std::string &shortrepr() const {
    return fieldindex->shortrepr();
  }
};

std::ostream &operator<<(std::ostream &, const IndexP&);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Components and ComponentIterators.

// A Components object holds the indices of the components of a Field,
// Flux, or Equation. There are different subclasses for different
// kinds of Fields, Fluxes, and Equations (scalar, vector, etc).

// A ComponentIterator is used to iterate over the indices stored in
// the Components.  The indices don't have to be stored explicitly --
// they can be generated on the fly.

class ComponentIterator {
public:
  ComponentIterator() {}
  virtual ~ComponentIterator() {}
  virtual bool operator!=(const ComponentIterator&) const = 0;
  virtual ComponentIterator& operator++() = 0;
  virtual FieldIndex *fieldindex() const = 0; // returns new FieldIndex
  IndexP operator*() const { return IndexP(fieldindex()); }
  virtual ComponentIterator *clone() const = 0;
  virtual void print(std::ostream&) const = 0;
};

std::ostream &operator<<(std::ostream&, const ComponentIterator&);

class ComponentIteratorP {
private:
  ComponentIterator *iter;
public:
  ComponentIteratorP(ComponentIterator *iter) : iter(iter) {}
  ~ComponentIteratorP() {
    if(iter)
      delete iter;
  }
  ComponentIteratorP(ComponentIteratorP &&other)
    : iter(other.iter)
  {
    other.iter = nullptr; // move constructor takes ownership of the pointer
  }
  ComponentIteratorP(const ComponentIteratorP &other)
    : iter(other.iter->clone())
  {}
  bool operator!=(const ComponentIteratorP &other) const {
    return *iter != *other.iter;
  }
  ComponentIteratorP& operator++() {
    ++(*iter);
    return *this;
  }
  IndexP operator*() const {
    return **iter;
  }
  ComponentIterator *iterator() const { return iter; }
  FieldIndex *current() const {
    return iter->fieldindex();	// returns a new FieldIndex*.
  }
};

std::ostream &operator<<(std::ostream&, const ComponentIteratorP&);

class Components {
public:
  virtual ~Components() {}
  // Nothing can change the Components object, so begin() and end()
  // are const.
  virtual ComponentIteratorP begin() const = 0;
  virtual ComponentIteratorP end() const = 0;
};

class ComponentsP {
private:
  const Components *components;
public:
  ComponentsP(const Components *c) : components(c) {}
  ComponentIteratorP begin() const { return components->begin(); }
  ComponentIteratorP end() const { return components->end(); }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// EmptyFieldComponents is used to "iterate" over fields that have no
// components, like the out-of-plane parts of a scalar or 2-vector.
// It just lets us define all the classes identically and put
// outOfPlaneComponents in the Field base class.

class EmptyFieldIterator : public ComponentIterator {
public:
  EmptyFieldIterator() {}
  virtual ~EmptyFieldIterator() {}
  virtual EmptyFieldIterator &operator++() { return *this; }
  virtual bool operator!=(const ComponentIterator&) const { return false; }
  virtual FieldIndex *fieldindex() const { return nullptr; }
  virtual ComponentIterator *clone() const {
    return new EmptyFieldIterator();
  }
  virtual void print(std::ostream&) const;
};

class EmptyFieldComponents : public Components {
public:
  virtual ComponentIteratorP begin() const {
    return ComponentIteratorP(new EmptyFieldIterator());
  }
  virtual ComponentIteratorP end() const {
    return ComponentIteratorP(new EmptyFieldIterator());
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class ScalarFieldCompIterator : public ComponentIterator {
private:
  bool done;
public:
  ScalarFieldCompIterator(bool done=false) : done(done) {}
  virtual ScalarFieldCompIterator &operator++();
  virtual bool operator!=(const ComponentIterator&) const;
  virtual FieldIndex *fieldindex() const;
  virtual ComponentIterator *clone() const {
    return new ScalarFieldCompIterator(*this);
  }
  virtual void print(std::ostream&) const;
};

class ScalarFieldComponents : public Components {
public:
  virtual ComponentIteratorP begin() const {
    return ComponentIteratorP(new ScalarFieldCompIterator(false)); 
  }
  virtual ComponentIteratorP end() const {
    return ComponentIteratorP(new ScalarFieldCompIterator(true)); 
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class VectorFieldCompIterator : public ComponentIterator {
protected:
  SpaceIndex index, imax;
public:
  VectorFieldCompIterator(SpaceIndex imin, SpaceIndex imax)
    : index(imin), imax(imax)
  {}
  virtual VectorFieldCompIterator &operator++() {
    ++index;
    return *this;
  }
  virtual bool operator!=(const ComponentIterator&) const;
  virtual FieldIndex *fieldindex() const {
    return new VectorFieldIndex(index);
  }
  virtual ComponentIterator *clone() const {
    return new VectorFieldCompIterator(*this);
  }
  virtual void print(std::ostream&) const;
};

class VectorFieldComponents : public Components {
protected:
  SpaceIndex imin, imax;
public:
  VectorFieldComponents(SpaceIndex imin, SpaceIndex imax)
    : imin(imin), imax(imax)
  {}
  virtual ComponentIteratorP begin() const {
    return ComponentIteratorP(new VectorFieldCompIterator(imin, imax));
  }
  virtual ComponentIteratorP end() const {
    return ComponentIteratorP(new VectorFieldCompIterator(imax, imax));
  }
  int min() const { return imin; }
  int max() const { return imax; }
};

// OutOfPlaneVectorFieldCompIterator iterates over the out-of-plane
// components of a vector field, like VectorFieldCompIterator with
// planarity=OUT_OF_PLANE, but it dereferences into an
// OutOfPlaneVectorFieldIndex instead of a VectorFieldIndex.

class OutOfPlaneVectorFieldCompIterator : public ComponentIterator {
protected:
  SpaceIndex index, imax;
public:
  OutOfPlaneVectorFieldCompIterator(SpaceIndex imin, SpaceIndex imax)
    : index(imin), imax(imax)
  {}
  virtual OutOfPlaneVectorFieldCompIterator &operator++() {
    ++index;
    return *this;
  }
  virtual bool operator!=(const ComponentIterator&) const;
  virtual FieldIndex *fieldindex() const {
    return new OutOfPlaneVectorFieldIndex(index);
  }
  virtual ComponentIterator *clone() const {
    return new OutOfPlaneVectorFieldCompIterator(*this);
  }
  virtual void print(std::ostream&) const;
};

class OutOfPlaneVectorFieldComponents : public Components {
protected:
  SpaceIndex imax;
public:
  OutOfPlaneVectorFieldComponents(SpaceIndex imax): imax(imax) {}
  virtual ComponentIteratorP begin() const {
    return ComponentIteratorP(new OutOfPlaneVectorFieldCompIterator(2, imax));
  }
  virtual ComponentIteratorP end() const {
    return ComponentIteratorP(
		      new OutOfPlaneVectorFieldCompIterator(imax, imax));
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// 3x3 Symmetric tensor field components and iterators.  There are
// different varieties for different planarities.

// SymTensorComponents contains all components, or just the in-plane
// or just the out-of-plane components of a SymmetricTensor Field
// (according to the Planarity argument).  The field has components
// xx, yy, zz, yz, xz, xy, numbered 0-5.

// SymTensorInPlaneComponents contains only the in-plane components of
// a symmetric tensor field.  The components are xx, yy, and xy,
// numbered 0, 1, and 5.  The field has out-of-plane components, but
// they're not iterated over.

// SymTensorOutOfPlaneComponents contains the out-of-plane components
// of a symmetric tensor field.  The components are zz, yz, and xz,
// and are numbered 2, 3, and 4.  The field has in-plane components,
// but they aren't iterated over.

// OutOfPlaneSymTensorComponents contains the components of a
// out-of-plane symmetric tensor field.  The field has components zz,
// yz, and xz, numbered 0, 1, and 2.  The *field* has no in-plane
// components.

class SymTensorIterator : public ComponentIterator {
protected:
  int v;
public:
  SymTensorIterator() : v(0) {}
  SymTensorIterator(int v) : v(v) {} // arg is the initial voigt index
  SymTensorIterator(SpaceIndex i, SpaceIndex j);
  SymTensorIterator &operator++() { v++; return *this; }
  virtual bool operator!=(const ComponentIterator &) const;
  virtual FieldIndex *fieldindex() const {
    return new SymTensorIndex(v);
  }
  virtual ComponentIterator *clone() const {
    return new SymTensorIterator(*this);
  }
  // SymTensorIterator is sometimes used directly, where the
  // generalization introduced by Components just gets in the way.
  // Giving it some of the SymTensorIndex methods is convenient.
  int row() const;
  int col() const;
  int integer() const { return v; }
  virtual void print(std::ostream&) const;
};

class SymTensorInPlaneIterator : public SymTensorIterator {
public:
  SymTensorInPlaneIterator() : SymTensorIterator(0) {}
  SymTensorInPlaneIterator(int v) : SymTensorIterator(v) {}
  SymTensorInPlaneIterator(int i, int j) : SymTensorIterator(i, j) {}
  SymTensorInPlaneIterator &operator++() {
    v++;
    if(v == 2) v = 5;
    return *this;
  }
  virtual ComponentIterator *clone() const {
    return new SymTensorInPlaneIterator(*this);
  }
  virtual void print(std::ostream&) const;
};

class SymTensorOutOfPlaneIterator : public SymTensorIterator {
public:
  SymTensorOutOfPlaneIterator() : SymTensorIterator(2) {}
  SymTensorOutOfPlaneIterator(int v) : SymTensorIterator(v) {}
  SymTensorOutOfPlaneIterator(int i, int j) : SymTensorIterator(i, j) {}
  SymTensorOutOfPlaneIterator &operator++() { v++; return *this; }
  virtual int integer() const { return v; }
  virtual ComponentIterator *clone() const {
    return new SymTensorOutOfPlaneIterator(*this);
  }
  virtual void print(std::ostream&) const;
};

class OutOfPlaneSymTensorIterator : public SymTensorOutOfPlaneIterator {
public:
  OutOfPlaneSymTensorIterator() : SymTensorOutOfPlaneIterator(2) {}
  OutOfPlaneSymTensorIterator(int v) : SymTensorOutOfPlaneIterator(v) {}
  OutOfPlaneSymTensorIterator(int i, int j):SymTensorOutOfPlaneIterator(i, j){}
  virtual FieldIndex *fieldindex() const {
    return new OutOfPlaneSymTensorIndex(v);
  }
  virtual int integer() const { return v - 2; }
  virtual ComponentIterator *clone() const {
    return new OutOfPlaneSymTensorIterator(*this);
  }
  virtual void print(std::ostream&) const;
};

class SymTensorComponents : public Components {
public:
  virtual ComponentIteratorP begin() const {
    return ComponentIteratorP(new SymTensorIterator(0));
  }
  virtual ComponentIteratorP end() const {
    return ComponentIteratorP(new SymTensorIterator(6));
  }
};

class SymTensorInPlaneComponents : public Components {
public:
  virtual ComponentIteratorP begin() const {
    return ComponentIteratorP(new SymTensorInPlaneIterator(0));
  }
  virtual ComponentIteratorP end() const {
    return ComponentIteratorP(new SymTensorInPlaneIterator(6));
  }
};

class SymTensorOutOfPlaneComponents : public Components {
public:
  virtual ComponentIteratorP begin() const {
    return ComponentIteratorP(new SymTensorOutOfPlaneIterator(2));
  }
  virtual ComponentIteratorP end() const {
    return ComponentIteratorP(new SymTensorOutOfPlaneIterator(5));
  }
};

class OutOfPlaneSymTensorComponents : public Components {
public:
  virtual ComponentIteratorP begin() const {
    return ComponentIteratorP(new OutOfPlaneSymTensorIterator(2));
  }
  virtual ComponentIteratorP end() const {
    return ComponentIteratorP(new OutOfPlaneSymTensorIterator(5));
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// SymTensorIJIterator and SymTensorIJComponents are used to iterate
// over the components of a symmetric 3x3 tensor and get a real
// SymTensorIndex out, not a FieldIndex or IndexP.  An instance called
// symTensorIJComponents is created for convenience.  Use it like
//   for(SymTensorIndex ij : symTensorIJComponents) { ... }
// or
//   for(SymTensorIterator it=symTensorIJComponents.begin();
//       it != symTensorIJComponents.end(); ++it)
//      { ... }

class SymTensorIJIterator {
private:
  int v;
public:
  SymTensorIJIterator() : v(0) {}
  SymTensorIJIterator(int v): v(v) {}
  SymTensorIJIterator &operator++() { v++; return *this; }
  SymTensorIndex operator*() const { return SymTensorIndex(v); }
  FieldIndex *fieldindex() const {
    return new SymTensorIndex(v);
  }
  bool operator!=(const SymTensorIJIterator &other) const {
    return v != other.v;
  }
  friend std::ostream &operator<<(std::ostream&, const SymTensorIJIterator&);
};

std::ostream &operator<<(std::ostream&, const SymTensorIJIterator&);

class SymTensorIJComponents {
public:
  SymTensorIJIterator begin() const { return SymTensorIJIterator(0); }
  SymTensorIJIterator end() const { return SymTensorIJIterator(6); }
};

extern SymTensorIJComponents symTensorIJComponents;


#endif // FIELDINDEX_H
