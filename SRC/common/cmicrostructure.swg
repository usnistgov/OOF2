// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CMICROSTRUCTURE_SWG
#define CMICROSTRUCTURE_SWG

%module(package="ooflib.SWIG.common") cmicrostructure

%{
#include "common/cmicrostructure.h"
#include "common/array.h"
typedef Array<int> ArrayInt;
typedef Array<int> NewArrayInt;
%}

%include "common/typemaps.swg"
%import "common/coord.swg"
%import "common/pixelgroup.swg"
%import "common/timestamp.swg"

%typemap(out) ArrayInt* {
   // typemap(out) ArrayInt*
  int h = $1->height();
  int w = $1->width();
  $result = PyList_New((Py_ssize_t) h);
  for(int j=0; j<h; j++) {
    PyObject *row = PyList_New((Py_ssize_t) w);
    PyList_SET_ITEM($result, (Py_ssize_t) j, row);
    for(int i=0; i<w; i++) {
      PyList_SET_ITEM(row, (Py_ssize_t) i, PyInt_FromLong((*$1)[ICoord(i,j)]));
    }
  }
}

%typemap(out) NewArrayInt* {
   // typemap(out) ArrayInt*
  int h = $1->height();
  int w = $1->width();
  $result = PyList_New((Py_ssize_t) h);
  for(int j=0; j<h; j++) {
    PyObject *row = PyList_New((Py_ssize_t) w);
    PyList_SET_ITEM($result, (Py_ssize_t) j, row);
    for(int i=0; i<w; i++) {
      PyList_SET_ITEM(row, (Py_ssize_t) i, PyInt_FromLong((*$1)[ICoord(i,j)]));
    }
  }
  delete $1;
}

%nodefaultctor SegmentSection;

class SegmentSection {
public:
  const int category;
  double pixelLength();
  double physicalLength();
  Coord physicalPt0();
  Coord physicalPt1();
  Coord pixelPt0();
  Coord pixelPt1();
};

ADD_REPR_GENERIC(SegmentSection);
MAKE_LISTVEC_TYPEMAPS(SegmentSection);

class CMicrostructure {
public:
  CMicrostructure(const std::string &name, ICoord *Sequence, Coord *Sequence);
  ~CMicrostructure();
  void destroy(); 
  const std::string &name();
  const Coord &sizeOfPixels();
  Coord physical2Pixel(const Coord *Point);
  void rename(const std::string &name);
  TimeStamp &getTimeStamp();
  void setCurrentActiveArea(ActiveArea*);
  int nGroups();
  // getGroup creates a new group if necessary.  findGroup never does.
  PixelGroup *getGroup(const std::string &name, bool *OUTPUT); 
  PixelGroup *findGroup(const std::string &name); 
  void removeGroup(char *name);
  void removeAllGroups();
  void renameGroupC(char *oldname, char *newname);
  %newobject groupNames;
  std::vector<std::string> *groupNames() const;
  int nCategories();
  int category(ICoord *iPoint);
  void recategorize();
  bool is_categorized();
  ArrayInt *getCategoryMap();
  NewArrayInt *getCategoryMapRO();
  ICoord getRepresentativePixel(int category);
  double edgeHomogeneity(const Coord &Point, const Coord &Point);
  SegmentSectionVec *getSegmentSections(const Coord* Point, const Coord *Point,
					double);
};

%extend CMicrostructure {
  bool containsPixel(ICoord *iPoint) { return self->contains(*iPoint); }
  bool containsPoint(Coord *Point) { return self->contains(*Point); }
}

long get_globalMicrostructureCount();

#endif // CMICROSTRUCTURE_SWG
