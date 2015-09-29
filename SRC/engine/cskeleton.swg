// -*- C++ -*-
// $RCSfile: cskeleton.swg,v $
// $Revision: 1.51 $
// $Author: langer $
// $Date: 2014/09/27 21:40:42 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CSKELETON_SWG
#define CSKELETON_SWG

%module cskeleton

%include "engine/typemaps.swg"
%include "common/typemaps.swg"
%extern "common/coord.swg"
%extern "common/timestamp.swg"
%pragma(python) code="from ooflib.SWIG.common.timestamp import TimeStampPtr"
%extern "common/cmicrostructure.swg"
%extern "common/coord.swg"
   %pragma(python) code="from ooflib.SWIG.common.coord import CoordPtr"

#ifdef DIM_3
%{
#include "vtk-5.0/vtkPythonUtil.h"
#include "vtk-5.0/vtkHexahedron.h"
#include "vtk-5.0/vtkTetra.h"
#include "vtk-5.0/vtkPoints.h"
#include "vtk-5.0/vtkIdList.h"
#include "vtk-5.0/vtkUnstructuredGrid.h"
%}
#endif


 // TODO: define typemaps for more vtk objects and streamline code
%typemap(python, in) vtkPoints* {
	$target = vtkPoints::SafeDownCast( vtkPythonGetPointerFromObject( $source, "vtkPoints") );
}

%{
#include <oofconfig.h>
#include "engine/cskeleton.h"
  %}

class CSkeletonNode {
public:
#ifdef DIM_3
  //CSkeletonNode(double, double, double);
  CSkeletonNode(double, double, double, vtkPoints*, int);
#else
  CSkeletonNode(double, double);
#endif
  ~CSkeletonNode();
  Coord position();
  bool movable_x();
  bool movable_y();
#ifdef DIM_3
  bool movable_z();
#endif
  bool movable();
  bool pinned();
  void setMobilityX(bool);
  void setMobilityY(bool);
#ifdef DIM_3
  void setMobilityZ(bool);
#endif
  void setPinned(bool);
  void copyMobility(CSkeletonNode*);
  bool canMergeWith(CSkeletonNode*);
  bool moveTo(Coord *Point);
  bool canMoveTo(Coord *Point);
  void unconstrainedMoveTo(Coord *Point);
  bool moveBy(Coord *Point);
  void moveBack();
//   Coord random_position(double, double);
  TimeStamp nodemoved;

#ifdef DIM_3
  %addmethods {
    PyObject* getPoints() {
       return vtkPythonGetObjectFromPointer( self->getPoints() );
    }
  }
#endif

};

class HomogeneityData {
public:
  ~HomogeneityData();
};

class CSkeletonElement {
public:
  ~CSkeletonElement();
  int nnodes();
  void replaceNode(int, CSkeletonNode*);
  %new PointVec *perimeter();
  double perimeterLength();
  double edgeLength(int);
#ifndef DIM_3
  double cosCornerAngle(int);
  double getRealAngle(int);
#else
  double cosCornerAngle(int, int);
  double solidCornerAngle(int);
  double cosDihedralAngle(int, int);
#endif
  Coord frommaster(MasterCoord *Point, int);
  Coord center();
  double area();
#ifdef DIM_3
  double volume();
#endif
  bool illegal();
  bool interior(Coord *Point);
  %new ICoordVec *underlying_pixels(CMicrostructure);
  double homogeneity(CMicrostructure);
  int dominantPixel(CMicrostructure);
  void copyHomogeneity(CSkeletonElement);
  double energyHomogeneity(CMicrostructure&);
  void findHomogeneityAndDominantPixel(CMicrostructure&);
  void revertHomogeneity();
  HomogeneityData getHomogeneityData();
  void setHomogeneityData(HomogeneityData);
  void setHomogeneous(int);
#ifndef DIM_3
  // %new DoubleList *categoryAreas(CMicrostructure);
#else
  void updateVtkCellPoints();
#endif
  bool transitionPoint(CMicrostructure, int, Coord *cskel_OutPoint);
};

#ifndef DIM_3

class CSkeletonTriangle : public CSkeletonElement {
public:
  CSkeletonTriangle(CSkeletonNode*, CSkeletonNode*, CSkeletonNode*);
  double energyShape();
};

class CSkeletonQuad : public CSkeletonElement {
public:
  CSkeletonQuad(CSkeletonNode*, CSkeletonNode*, CSkeletonNode*, CSkeletonNode*);
  ~CSkeletonQuad();
  double energyShape();
};


#else

// class CSkeletonBrick : public CSkeletonElement, public vtkHexahedron {
// public:
//   CSkeletonBrick(CSkeletonNode*, CSkeletonNode*, CSkeletonNode*, CSkeletonNode*, 
// 		 CSkeletonNode*, CSkeletonNode*, CSkeletonNode*, CSkeletonNode*);
//   ~CSkeletonBrick();
//   double energyShape();
  
//   %addmethods {
//     // Not thread safe!
//     PyObject* GetPointIds() {
//       return vtkPythonGetObjectFromPointer( self->GetPointIds() );
//     }
    
//     void AddCellToGrid(PyObject *grid) {
//       vtkUnstructuredGrid *ugrid = vtkUnstructuredGrid::SafeDownCast( vtkPythonGetPointerFromObject( grid, "vtkUnstructuredGrid") );
//       ugrid->InsertNextCell(self->GetCellType(), self->GetPointIds());
//     }
    
//     void SetPointId(int i, int id) {
//       self->GetPointIds()->SetId(i,id);
//     }
    
//     int GetCellType() {
//       return self->GetCellType();
//     }
//   }
  
// };

class CSkeletonTetra : public CSkeletonElement {
public:
  CSkeletonTetra(CSkeletonNode*, CSkeletonNode*, CSkeletonNode*, CSkeletonNode*);
  double energyShape();
  int getCellType();
  int getNumberOfEdges();
  int getNumberOfFaces();

  %addmethods {
//     // Not thread safe!
//     PyObject* GetPointIds() {
//       return vtkPythonGetObjectFromPointer( self->cell->GetPointIds() );
//     }

//     int GetReferenceCount() {
//       return self->cell->GetReferenceCount();
//     }
    PyObject* getFaceToEdgesMap() {
      int numfaces = 4;
      int numedges = 3;
      PyObject *tuple = PyTuple_New((Py_ssize_t) numfaces);
      for(int i=0; i<numfaces; ++i) {
	PyObject *sub = PyTuple_New((Py_ssize_t) numedges);
	for(int j=0; j<numedges; ++j) 
	  PyTuple_SET_ITEM(sub, (Py_ssize_t) j, PyInt_FromLong(self->faceToEdgesMap[i][j]));
	PyTuple_SET_ITEM(tuple, (Py_ssize_t) i, sub);
      }
      return tuple;
    }

    PyObject* getNodeToOppFaceMap() {
      int numfaces = 4;
      PyObject *tuple = PyTuple_New((Py_ssize_t) numfaces);
      for(int i=0; i<numfaces; ++i) {
	PyTuple_SET_ITEM(tuple, (Py_ssize_t) i, PyInt_FromLong(self->nodeToOppFaceMap[i]) );
      }
      return tuple;
    }

    void AddCellToGrid(PyObject *grid) {
      vtkUnstructuredGrid *ugrid = vtkUnstructuredGrid::SafeDownCast( 
	    vtkPythonGetPointerFromObject( grid, "vtkUnstructuredGrid") );
      ugrid->InsertNextCell(self->getCellType(), self->getPointIds());
      //cout << "in AddCellToGrid" << endl;
      //for(int i = 0; i<4; i++)
      //cout << self->getPointIds()->GetId(i) << endl;
    }


    PyObject* getEdge(int i) {
      return vtkPythonGetObjectFromPointer( self->getEdge(i) );
    }

    PyObject* getPointIds() {
       return vtkPythonGetObjectFromPointer( self->getPointIds() );
    }

    PyObject* getPoints() {
       return vtkPythonGetObjectFromPointer( self->getPoints() );
    }

    // needed to be consistent with vtk 
    // TODO 3D: clean this up
    PyObject* GetPoints() {
       return vtkPythonGetObjectFromPointer( self->getPoints() );
    }
    
    int GetCellType() {
      return self->getCellType();
    }

    PyObject* getWeights(double x, double y, double z) {
      double p[3], closestPoint[3], pcoords[3], dist2, weights[4];
      int subId, inside;
      p[0] = x;
      p[1] = y;
      p[2] = z;
      inside = self->evaluatePosition(p, closestPoint, subId, pcoords, dist2, weights);
      PyObject *pylist = PyList_New((Py_ssize_t) 4);
      for(int i = 0; i<4; i++)
	PyList_SET_ITEM(pylist, (Py_ssize_t) i, PyFloat_FromDouble(weights[i]));
      return pylist;
    }


//     void SetPoint(int i, int id, Coord *Point) {
//       self->cell->GetPointIds()->SetId(i,id);
//       self->Points->InsertPoint(i,(*Point).x,(*Point).y,(*Point).z);
//     }
    

  }
  
};


#endif

long get_globalNodeCount();
long get_globalElementCount();

//%typemap(python, argout) Coord *cskel_OutPoint {}
//%typemap(python, ignore) Coord *cskel_OutPoint {}

#endif // CSKELETON_SWG
