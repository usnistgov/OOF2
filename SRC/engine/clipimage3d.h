// $RCSfile: clipimage3d.h,v $
// $Revision: 1.3 $
// $Author: langer $
// $Date: 2014/09/27 21:40:41 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */


#ifndef CLIPIMAGE_H
#define CLIPIMAGE_H

#include "vtk-5.0/vtkUnstructuredGridAlgorithm.h"
//#include "vtk-5.0/vtkClipVolume.h"
#include "vtk-5.0/vtkImageData.h"
#include "vtk-5.0/vtkAlgorithm.h"
//#include "vtk-5.0/vtkPolyDataAlgorithm.h"
#include "vtk-5.0/vtkPythonUtil.h"
#include "vtk-5.0/vtkObject.h"
#include "vtk-5.0/vtkObjectBase.h"
#include "vtk-5.0/vtkCell3D.h"
#include "vtk-5.0/vtkDelaunay3D.h"


#include <vector>


class vtkCellData;
class vtkCell3D;
class vtkDelaunay3D;
class vtkDataArray;
class vtkIdList;
class vtkImplicitFunction;
class vtkImageData;
class vtkMergePoints;
class vtkOrderedTriangulator;
class vtkPointData;
class vtkPointLocator;
class vtkPoints;
class vtkUnstructuredGrid;
class vtkCell;
class vtkTetra;
class vtkCellArray;
class vtkIdTypeArray;
class vtkUnsignedCharArray;

class VTK_GRAPHICS_EXPORT ClipImage3D : public vtkUnstructuredGridAlgorithm
{

public:
  static ClipImage3D *New();

  ClipImage3D();
  ~ClipImage3D();

  double getVolume() const {return volume;};

	virtual void SetClipCell(vtkCell3D *ClipCell);

	virtual void SetIndexedImage(vtkImageData *IndexedImage);

	void CreateDefaultLocator();

	vtkSetMacro(Value,int);
	vtkGetMacro(Value,int);


	virtual void ReportReferences(vtkGarbageCollector*);


	static const int HexahedronEdgeMap[][4];
	static const int HexahedronDirMap[];
	static const int TetrahedronEdgeMap[][3];
	static const int TetrahedronDirMap[][3];


protected:

	
  virtual int RequestData(vtkInformation *, vtkInformationVector **, vtkInformationVector *);
	virtual int FillInputPortInformation(int port, vtkInformation *info);

	int getIndexedImageValue(double x[3], double y[3]);
	bool pointOnFaceEdge(int numPoints, double *weights);
	bool edgeOnFaceEdge(int numFaceEdges, double *weights1, double *weights2);

  void ClipVoxel(double value, vtkDataArray *cellScalars, int flip,
                 double origin[3], double spacing[3], vtkIdList *cellIds,
                 vtkPoints *cellPts, vtkPointData *inPD, 
                 vtkCellData *inCD, vtkIdType cellId, int matindex, vtkCell *voxel);

  vtkPointLocator     *Locator;
	double                MergeTolerance;
	double               IntersectionTolerance;
  
private:
  
  // Used temporarily to pass data around
  vtkIdType             NumberOfCells;
  vtkCellArray          *Connectivity;
  vtkUnsignedCharArray  *Types;
  vtkIdTypeArray        *Locations;
  vtkIdType             NumberOfClippedCells;
  vtkCellArray          *ClippedConnectivity;
  vtkUnsignedCharArray  *ClippedTypes;
  vtkIdTypeArray        *ClippedLocations;

	vtkCell3D             *ClipCell;
	vtkImageData          *IndexedImage;
	int                   Value;

	double volume;

private:
  ClipImage3D(const ClipImage3D&);  // Not implemented.
  void operator=(const ClipImage3D&);  // Not implemented.
};

#endif
