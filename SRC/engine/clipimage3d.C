// -*- C++ -*-
// $RCSfile: clipimage3d.C,v $
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

#include "clipimage3d.h"

#include "vtk-5.0/vtkCellData.h"
#include "vtk-5.0/vtkFloatArray.h"
#include "vtk-5.0/vtkDoubleArray.h"
#include "vtk-5.0/vtkIntArray.h"
#include "vtk-5.0/vtkGarbageCollector.h"
#include "vtk-5.0/vtkPolyData.h"
#include "vtk-5.0/vtkImplicitFunction.h"
#include "vtk-5.0/vtkMergePoints.h"
#include "vtk-5.0/vtkInformation.h"
#include "vtk-5.0/vtkInformationVector.h"
#include "vtk-5.0/vtkExecutive.h"
#include "vtk-5.0/vtkObjectFactory.h"
#include "vtk-5.0/vtkOrderedTriangulator.h"
#include "vtk-5.0/vtkPointData.h"
#include "vtk-5.0/vtkUnstructuredGrid.h"
#include "vtk-5.0/vtkVoxel.h"
#include "vtk-5.0/vtkGenericCell.h"
#include "vtk-5.0/vtkTetra.h"
#include "vtk-5.0/vtkCellArray.h"
#include "vtk-5.0/vtkIdTypeArray.h"
#include "vtk-5.0/vtkUnsignedCharArray.h"
#include "vtk-5.0/vtkMath.h"
#include "vtk-5.0/vtkPolygon.h"
#include "vtk-5.0/vtkImageClip.h"
#include "vtk-5.0/vtkImageDataGeometryFilter.h"
#include "vtk-5.0/vtkExtractEdges.h"
#include "vtk-5.0/vtkCutter.h"
#include "vtk-5.0/vtkCellLocator.h"
#include "vtk-5.0/vtkCell.h"
#include "vtk-5.0/vtkPointsProjectedHull.h"
#include "vtk-5.0/vtkPlane.h"
#include "vtk-5.0/vtkBox.h"
#include "vtk-5.0/vtkExtractPolyDataGeometry.h"
#include "vtk-5.0/vtkGeometryFilter.h"
#include "vtk-5.0/vtkPolyDataConnectivityFilter.h"

#include "common/coord.h"
#include "engine/ooferror.h"
#include "engine/cskeleton.h"
#include <math.h>

vtkStandardNewMacro(ClipImage3D);
vtkCxxSetObjectMacro(ClipImage3D,ClipCell,vtkCell3D);
vtkCxxSetObjectMacro(ClipImage3D,IndexedImage,vtkImageData);

const int ClipImage3D::HexahedronEdgeMap[][4] = { 
	{8, 7, 10, 3},
	{1, 11, 5, 9},
	{0, 9, 4, 8},
	{10, 6, 11, 2},
	{3, 2, 1, 0},
	{4, 5, 6, 7}
};

const int ClipImage3D::HexahedronDirMap[] = {1, 1, -1, -1};

const int ClipImage3D::TetrahedronEdgeMap[][3] = {
	{0, 4, 3},
	{1, 5, 4},
	{2, 3, 5},
	{2, 1, 0}
};

const int ClipImage3D::TetrahedronDirMap[][3] = {
	{1, 1, -1},
	{1, 1, -1},
	{1, 1, -1},
	{-1, -1, -1}
};

ClipImage3D::ClipImage3D()
{
  this->Locator = NULL;
  this->ClipCell = NULL;
  this->IndexedImage = NULL;
  this->Value = 0;

	// need to examine uses of tolerance and perturbation!  Find combinations that work all the time!

  //this->MergeTolerance = 1e-6;
  this->IntersectionTolerance = 1e-8;
}



ClipImage3D::~ClipImage3D()
{
  if ( this->Locator )
    {
    this->Locator->UnRegister(this);
    this->Locator = NULL;
    }
//   if ( this->IndexedImage )
//     {
//     this->IndexedImage->UnRegister(this);
//     this->IndexedImage = NULL;
//     }
//   if ( this->ClipCell )
//     {
//     this->ClipCell->UnRegister(this);
//     this->ClipCell = NULL;
//     }
	this->IndexedImage->Delete();
	this->ClipCell->Delete();
}


int ClipImage3D::getIndexedImageValue(double x[3], double y[3]) {
	// perturb the value inwards wrt the clip cell, incase the point we
	// are looking at borders both the clip cell, and a face of the
	// voxel group boundaries.   x
	// is for the original value, y is for the perturbed value.

	// TODO: We have to consider that the voxel boundary edge could
	// point towards the center of the element, in which case this
	// perturbation won't help.  Will need to perturb in different
	// directions to resolve this.

	int i, ptinside, nearestId, subId;
	double pcoords[3], dist2, weights[8], closestpt[3], pcenter[3];
	double perturb = this->IntersectionTolerance;
	ptinside = this->ClipCell->EvaluatePosition(x, closestpt, nearestId, pcoords, dist2, weights);
 	if(this->ClipCell->GetCellType() == VTK_HEXAHEDRON) 
		pcenter[0] = pcenter[1] = pcenter[2] = 0.5;
	else
		this->ClipCell->GetParametricCenter(pcenter);
	for(i=0; i<3; i++) 
		pcoords[i] = pcenter[i]+(pcoords[i]-pcenter[i])*(1-perturb);
	this->ClipCell->EvaluateLocation(subId,pcoords,y,weights);
	// TODO: Stop assuming the coordinates coincide with the indices of the image!!!
	return this->IndexedImage->GetScalarComponentAsFloat(int(y[0]),int(y[1]),int(y[2]),0);
}


typedef std::multimap<double, Coord> CellEdgeMap;
typedef std::vector<CellEdgeMap> CellEdge;
typedef std::pair<double, Coord> CellEdgeDatum;

bool ClipImage3D::pointOnFaceEdge(int numPoints, double *weights) {
	// Helper function to tell us if one point is on an edge of the clip
	// cell face.
	int i, contributingPoints = 0;
	for(i=0; i<numPoints; i++) {
		if(weights[i] > this->IntersectionTolerance) {
			contributingPoints++;
		}
	}
	return ( contributingPoints <= 2 );
}


bool ClipImage3D::edgeOnFaceEdge(int numPoints, double *weights1, double *weights2) {
	// Helper function for determining if two points are on the edge of
	// a face.  The weights should come from calling the vtk routine
	// "EvaluatePosition" on the relevant cell.  If two points are on
	// the same edge, they will have weights equal to zero for the same
	// point(s).  There will be only two points in the cell for which
	// both test points do not have zero weights.
	int i, mutuallyNonContributingPoints = 0;
	for(i=0; i<numPoints; i++) {
		if(weights1[i] <= this->IntersectionTolerance && weights2[i] <= this->IntersectionTolerance)
			mutuallyNonContributingPoints++;
	}
	return ( (numPoints-mutuallyNonContributingPoints) == 2 );
}


int ClipImage3D::RequestData(
  vtkInformation *vtkNotUsed(request),
  vtkInformationVector **inputVector,
  vtkInformationVector *outputVector)
{

  // get the info objects
  vtkInformation *inInfo = inputVector[0]->GetInformationObject(0);
  //vtkInformation *outInfo = outputVector->GetInformationObject(0);

  // get the input and ouptut
  vtkPolyData *input = vtkPolyData::SafeDownCast(
    inInfo->Get(vtkDataObject::DATA_OBJECT()));
//   vtkUnstructuredGrid *output = vtkUnstructuredGrid::SafeDownCast(
//     outInfo->Get(vtkDataObject::DATA_OBJECT()));


	vtkIdType i;
  int  j, k, nearestId, inside, outside, ptinside, p1inside, p2inside;
  double x[3], y[3], closestpt[3], weights[8], dist2, pcoords[3];
  vtkIdType estimatedSize, numCells=input->GetNumberOfCells();
  vtkIdType numPts=input->GetNumberOfPoints();
	int numEdges, ptId, proji[2], l, numFaceEdges, numIntersections, m;
	double t, p1[3], p2[3], projfactor;
	int subId, intersect, numFaces, hullnum, numClipCellFaces;
	double normal[3], center[3], dot, area, p[4][3];
	double hullpts[1024], basearea;
  vtkPointsProjectedHull *newPoints;
	vtkPoints *polypoints;
	vtkPolyData *boundedInput;
	double *bounds = this->ClipCell->GetBounds();

	vtkIndent indent;

	volume = 0;

  estimatedSize = numCells;
  estimatedSize = estimatedSize / 1024 * 1024; //multiple of 1024
  if (estimatedSize < 1024)
    {
    estimatedSize = 1024;
    }

  // Create objects to hold output of clip operation
  // TODO: Are we creating any output????  We would need two locators,
  // one for the hull of each face contribution, and one for all of
  // the points that would be in the output.
//   this->NumberOfCells = 0;
//   this->Connectivity = vtkCellArray::New();
//   this->Connectivity->Allocate(estimatedSize*2); //allocate storage for cells
//   this->Locations = vtkIdTypeArray::New();
//   this->Locations->Allocate(estimatedSize);
//   this->Types = vtkUnsignedCharArray::New();
//   this->Types->Allocate(estimatedSize);

  // locator used to merge potentially duplicate points
  if ( this->Locator == NULL )
    {
    this->CreateDefaultLocator();
    }


	// extract the portion of the input that is within the bounds of the element

	// There seems to be a bug in the ExtractPolyDataGeometry where the
	// cell data is not copied over, that's why we use GeometryFilter
	// for now, but eventually, we should incorporate a fixed version of
	// the code from ExtractPolyDataGeometry in here, instead of using a
	// filter....

	// Will need to fix this for when we combine voxel group boundaries.

	vtkGeometryFilter *extractBoundedInput = vtkGeometryFilter::New();
 	extractBoundedInput->SetInput(input);	
	// TODO: need subtract real size of voxel OR modify ExtractPolyDataGeometry to preserve cell data - be more careful here in general.
	//extractBoundedInput->SetExtent(bounds[0]-2,bounds[1]+2,bounds[2]-2,bounds[3]+2,bounds[4]-2,bounds[5]+2);
	extractBoundedInput->SetExtent(floor(bounds[0]-1),ceil(bounds[1]+1),floor(bounds[2]-1),ceil(bounds[3]+1),floor(bounds[4]-1),ceil(bounds[5]+1));
	//extractBoundedInput->SetExtent(floor(bounds[0]),ceil(bounds[1]),floor(bounds[2]),ceil(bounds[3]),floor(bounds[4]),ceil(bounds[5]));
	extractBoundedInput->ExtentClippingOn();

	boundedInput = extractBoundedInput->GetOutput();
	boundedInput->Update();

	// First, we find the volume contribution of the faces of the voxel
	// group boundaries (the input).  We find which faces are totally
	// inside the element (clipCell) and the interior portions of the
	// faces that intersect the element (clipCell).

	numFaces = boundedInput->GetNumberOfPolys();
	numClipCellFaces = this->ClipCell->GetNumberOfFaces();
	int numClipCellEdges = this->ClipCell->GetNumberOfEdges();
	CellEdge clipCellEdgeData(numClipCellEdges);

	// Start by looping over the points in the input and storing whether
	// they are in, out, or on the border of the clipCell.
 	int numPoints = boundedInput->GetPoints()->GetNumberOfPoints();
// 	vtkPoints *
	// 0 for outside, 1 for inside and not on boundary, 2 if on boundary
	vtkIntArray *insideinfo = vtkIntArray::New();
	insideinfo->Allocate(numPoints,numPoints);
 	for(i=0; i<numPoints; i++) {
		boundedInput->GetPoints()->GetPoint(i,x);
 		ptinside = this->ClipCell->EvaluatePosition(x, closestpt, nearestId, pcoords, dist2, weights);
		insideinfo->InsertNextValue(ptinside);
	}


	for(i=0; i<numFaces; i++) {
		polypoints = boundedInput->GetCell(i)->GetPoints();
		boundedInput->GetCellData()->GetNormals()->GetTuple(i,normal);

		newPoints = vtkPointsProjectedHull::New(); 
		newPoints->Allocate(estimatedSize/2,estimatedSize/2);
		this->Locator->InitPointInsertion(newPoints, bounds);

		center[0] = center[1] = center[2] = 0.0;
		dot = 0.0;
		inside = 0;
		outside = 0;
		for(j=0; j<4; j++ ){
			polypoints->GetPoint(j,p[j]);
			ptinside = insideinfo->GetTuple1(boundedInput->GetCell(i)->GetPointIds()->GetId(j));
			//ptinside = this->ClipCell->EvaluatePosition(p[j], closestpt, nearestId, pcoords, dist2, weights);
			inside |= ptinside;
			outside |= !ptinside;
			if(ptinside) {
				if(this->Locator->InsertUniquePoint(p[j], ptId))
					for(k=0; k<3; k++) center[k] += p[j][k];
			}
		}

		if(inside && !outside) { // face totally inside

			// we need to check if it is on the boundary of the clip cell
			// TODO: Code a more efficient way of keeping track of which
			// points are in and which are out.
			int onFace=1;
			for(j=0; j<numClipCellFaces; j++) {
				onFace=1;
				for(k=0; k<4; k++) {
					// is the point on one of the faces?
					ptinside = this->ClipCell->GetFace(j)->EvaluatePosition(p[k], closestpt, nearestId, pcoords, dist2, weights);
					// TODO: handle units better or find a different condition.  IntersectionTolerance should only be compared to pcoords or weights.
					if(sqrt(dist2)<=this->IntersectionTolerance)
						onFace &= 1;
					else {
						onFace &= 0;
					}
				}
				if(onFace)
					break;
			}

			if(!onFace) {
				area = boundedInput->GetCellData()->GetScalars()->GetComponent(i,0);
				dot = boundedInput->GetCellData()->GetScalars()->GetComponent(i,1);
				volume += 1.0/3.0 * dot * area;

			//loop over edges of clip cell - store points by edge for later.
			for(j=0; j<numClipCellEdges; j++) {
				this->ClipCell->GetEdge(j)->GetPoints()->GetPoint(0,p1);
				this->ClipCell->GetEdge(j)->GetPoints()->GetPoint(1,p2);
				// it's only possible the edge intersects the face in one place
				intersect = boundedInput->GetCell(i)->IntersectWithLine(p1,p2,this->IntersectionTolerance,t,x,pcoords,subId);
				if(intersect) {
					if(!clipCellEdgeData[j].count(t) && t > this->IntersectionTolerance && t < (1-this->IntersectionTolerance) )
						// wrap x as a coord so that it is passed by value
						clipCellEdgeData[j].insert(CellEdgeDatum(t,Coord(x[0],x[1],x[2])));
				}
			}


			}
		} // end if(inside && !outside)

		// the face can be partially inside whether or not any corners are inside.
		else {

			// loop over edges of quad
			for(j=0; j<4; j++) {
				// we could probably hard code the points here...
				boundedInput->GetCell(i)->GetEdge(j)->GetPoints()->GetPoint(0,p1);
				boundedInput->GetCell(i)->GetEdge(j)->GetPoints()->GetPoint(1,p2);
				intersect = this->ClipCell->IntersectWithLine(p1,p2,this->IntersectionTolerance,t,x,pcoords,subId);
				if(intersect) {
					if(this->Locator->InsertUniquePoint(x, ptId))
						for(k=0; k<3; k++) center[k] += x[k];
				}
				// go the other way because it's possible the line intersects the clip cell in 2 places
				intersect = this->ClipCell->IntersectWithLine(p2,p1,this->IntersectionTolerance,t,x,pcoords,subId);
				if(intersect) {
					if(this->Locator->InsertUniquePoint(x, ptId))
						for(k=0; k<3; k++) center[k] += x[k];
				}
			}

			//loop over edges of clip cell - store points by edge for later.
			for(j=0; j<numClipCellEdges; j++) {
				this->ClipCell->GetEdge(j)->GetPoints()->GetPoint(0,p1);
				this->ClipCell->GetEdge(j)->GetPoints()->GetPoint(1,p2);
				// it's only possible the edge intersects the face in one place
				intersect = boundedInput->GetCell(i)->IntersectWithLine(p1,p2,this->IntersectionTolerance,t,x,pcoords,subId);
				if(intersect) {
					if(!clipCellEdgeData[j].count(t) && t > this->IntersectionTolerance && t < (1-this->IntersectionTolerance) )
						clipCellEdgeData[j].insert(CellEdgeDatum(t,Coord(x[0],x[1],x[2])));
					if(this->Locator->InsertUniquePoint(x, ptId))
						for(k=0; k<3; k++) center[k] += x[k];
				}
			}


			// Since we are intersecting two convex shapes, the result must
			// be convex.  Also, the normal is always along an axis.  This
			// means we can use vtk's built in methods to find the 2D points
			// that make up the face in CCW order.  Then we can calculate
			// the base area of this pyramidal volume contribution the same
			// way we calculate areas for the 2D homogeneity calculaton.
			numPts = this->Locator->GetPoints()->GetNumberOfPoints();

			if(numPts > 2) {

				// we need to check if it is on the boundary of the clip cell
				// TODO: Code a more efficient way of keeping track of which
				// points are in and which are out.
				int onFace=1;
				for(j=0; j<numClipCellFaces; j++) {
					onFace=1;
					for(k=0; k<numPts; k++) {
						newPoints->GetPoint(k,x);
						ptinside = this->ClipCell->GetFace(j)->EvaluatePosition(x, closestpt, nearestId, pcoords, dist2, weights);
						if(sqrt(dist2)<=this->IntersectionTolerance)
							onFace &= 1;
						else 
							onFace &= 0;
					}
					if(onFace)
						break;
				}


				if(!onFace) {


					for(k=0; k<3; k++) center[k] /= numPts;
					dot = normal[0]*center[0] + normal[1]*center[1] + normal[2]*center[2]; 
					basearea = 0.0;
					hullnum = 0;
					
					// Since the faces are axis aligned, only one component of the
					// normal is non zero.
					if(fabs(normal[0]))
						hullnum = newPoints->GetCCWHullX(hullpts, numPts);
					if(fabs(normal[1]))
						hullnum = newPoints->GetCCWHullY(hullpts, numPts);
					if(fabs(normal[2]))
						hullnum = newPoints->GetCCWHullZ(hullpts, numPts);
					
					for(j=0; j<hullnum; j++) {
						basearea += (1.0/2.0)*(hullpts[j*2]*hullpts[((j+1)%hullnum)*2+1]-hullpts[j*2+1]*hullpts[((j+1)%hullnum)*2]);
					}

					volume += 1.0/3.0 * dot * basearea;
				} // end if(!onFace)

			} // end if(numPts)
			newPoints->Delete();
			this->Locator->Initialize();
		} // end else






	} // end loop over i
		

	// Now find the contribution of the faces of the element.  For this,
	// we find the intersection of the voxel group boundaries (input)
	// with each face of the element (clipCell).  This is a polydata
	// with a series of line cells, oriented counterclockwise about the
	// voxel group in question.  We use a ConnectivityFilter to break
	// this into parts.  We then traverse each part and look for
	// intersections with the element face.
 		cout << "end phase 1" << endl;
		cout << "volume = " << volume << endl;

	//numFaces = this->ClipCell->GetNumberOfFaces();
	vtkCell *face;
	vtkPlane *plane;
	vtkCutter *edgeExtractor;
	vtkPolyData *edges;
 	for(i=0; i<numClipCellFaces; i++) {
		face = this->ClipCell->GetFace(i);
		numFaceEdges = face->GetNumberOfEdges();
		bounds = face->GetBounds();
		polypoints = face->GetPoints();
		vtkPolygon::ComputeNormal(polypoints,normal);

		// We find the axis direction which has the maximum contribution
		// to the normal.  We can save floating point operations later on
		// by projecting onto this direction, calculating the 2D cross
		// product, and then dividing by the cosine of the normal to find
		// the area contribution for each segment.  The sign of the
		// projfactor will correct for whether the bounding segments are
		// oriented CCW when projected onto the given axis oriented plane.
		if(fabs(normal[0]) >= fabs(normal[1]) && fabs(normal[0]) >= fabs(normal[2])) {
			projfactor = normal[0];
			proji[0]=1;
			proji[1]=2;
		}
		if(fabs(normal[1]) >= fabs(normal[0]) && fabs(normal[1]) >= fabs(normal[2])) {
			projfactor = normal[1];
			proji[0]=2;
			proji[1]=0;
		}
		if(fabs(normal[2]) >= fabs(normal[0]) && fabs(normal[2]) >= fabs(normal[1])) {
			projfactor = normal[2];
			proji[0]=0;
			proji[1]=1;
		}

		// Find where voxel group boundaries intersect the plane
		plane = vtkPlane::New();
		plane->SetNormal(normal);
		polypoints->GetPoint(0,x);
		plane->SetOrigin(x);
		edgeExtractor = vtkCutter::New();
		edgeExtractor->SetInput(boundedInput);
		edgeExtractor->SetCutFunction(plane);
		edges = edgeExtractor->GetOutput();
		edges->Update();
		edges->BuildLinks();

		newPoints = vtkPointsProjectedHull::New(); 
		newPoints->Allocate(estimatedSize/2,estimatedSize/2);
		this->Locator->InitPointInsertion(newPoints, bounds);

		basearea = 0.0;
		center[0] = center[1] = center[2] = 0.0;
		dot = 0.0;

		numEdges = edges->GetNumberOfCells();
		cout << "numEdges = " << numEdges << endl;

		double debugbounds[6];
		boundedInput->GetBounds(debugbounds);
		double length, maxLength = 0;
		for(j=0; j<5; j+=2) {
			length = debugbounds[j+1]-debugbounds[j];
			if(length>maxLength)
				maxLength=length;
		}


		// Need to handle case where all points are inside, or all
		// points are outside (no intersections).  For each edge, we
		// want to handle cases of 0, 1, or 2 intersections.

		// Loop over the edges, testing for intersections and
		// whether they are inside or outside the element face.
		// Consider the following cases: 1. If both points are inside,
		// then there must be no intersections, and the whole segment
		// contributes to the area. 2. If one point is in, and one point
		// is out, there must be only one intersection, and the segment
		// between the intersection and the inside point contribute to
		// the area. 3.  If there are no intersections and both points
		// are outside, then there is no contribution.  4. If both
		// points are outside, and there are two intersections, then the
		// segment between the intersections contributes to the area.
			
		// Note, the segments are directed so that each segment is CCW
		// around the material in question, WRT the plane normal using the
		// RHR.  BUT the segments are NOT necessarily in order, which
		// actually doesn't matter.
		double pcoords1[3], pcoords2[3], weights1[4], weights2[4];
		int onEdge;
		for(k=0; k<numEdges; k++) {
			edges->GetCell(k)->GetPoints()->GetPoint(0,p1);
			edges->GetCell(k)->GetPoints()->GetPoint(1,p2);
			// If the points are actually on the edge, we treat them as if they are outside.
			p1inside = face->EvaluatePosition(p1, closestpt, nearestId, pcoords1, dist2, weights1);
			onEdge = pointOnFaceEdge(numFaceEdges, weights1);
			if(onEdge) p1inside = 0;
			p2inside = face->EvaluatePosition(p2, closestpt, nearestId, pcoords2, dist2, weights2);
			onEdge = pointOnFaceEdge(numFaceEdges, weights2);
			if(onEdge) p2inside = 0;

			// case 1 - both points inside
			if(p1inside && p2inside){

				onEdge = edgeOnFaceEdge(numFaceEdges, weights1, weights2);

				if(!onEdge) {
					basearea+=(1.0/2.0)*(p1[proji[0]]*p2[proji[1]]-p1[proji[1]]*p2[proji[0]]);
					if(this->Locator->InsertUniquePoint(p1, ptId)) 
						for(l=0; l<3; l++) center[l] += p1[l];
					if(this->Locator->InsertUniquePoint(p2, ptId)) 
						for(l=0; l<3; l++) center[l] += p2[l];
				}

 			} // end (p1inside and p2inside)


			// case 2 - one point inside and one point outside
			if(p1inside != p2inside) {
				for(l=0, intersect=0; l<numFaceEdges && !intersect; l++) {
					intersect = face->GetEdge(l)->IntersectWithLine(p1,p2,this->IntersectionTolerance,t,x,pcoords,subId);
				}
				if(intersect) {

					// test if both points on edge
					inside = face->EvaluatePosition(x, closestpt, nearestId, pcoords, dist2, weights);
					for(l=0;l<2;l++) {
						if(p1inside) {
							onEdge = edgeOnFaceEdge(numFaceEdges, weights1, weights);
						}
						if(p2inside) {
							onEdge = edgeOnFaceEdge(numFaceEdges, weights2, weights);
						}
					}

					if(!onEdge) {

						if(this->Locator->InsertUniquePoint(x, ptId))
							for(l=0; l<3; l++) center[l] += x[l];

						if(p1inside) { 
							basearea+=(1.0/2.0)*(p1[proji[0]]*x[proji[1]]-p1[proji[1]]*x[proji[0]]);
							if(this->Locator->InsertUniquePoint(p1, ptId)) 
								for(l=0; l<3; l++) center[l] += p1[l];
						}
						if(p2inside) {
							basearea+=(1.0/2.0)*(x[proji[0]]*p2[proji[1]]-x[proji[1]]*p2[proji[0]]);
							if(this->Locator->InsertUniquePoint(p2, ptId)) 
								for(l=0; l<3; l++) center[l] += p2[l];
						}
					}
				} // end if(intersect)
				else {
					cerr << "did not find required intersections" << endl;
					throw ErrProgrammingError("ClipImage3D: did not find required intersection.", __FILE__, __LINE__);
				}
			}

			// cases 3 and 4 - both points outside
			if(!p1inside and !p2inside) {

				// There cannot be more than two intersections.  We ignore the
				// case of 0 or 1 (corner graze) intersections.  So we need to
				// find two intersections and order them by t (the parametric
				// distance along p1 to p2).  The intersections should be
				// along two different edges of the cell.  If they are on the
				// same edge, we ignore it.
				double t1, t2;
				for(l=0, intersect=0; l<numFaceEdges && !intersect; l++)
					intersect = face->GetEdge(l)->IntersectWithLine(p1,p2,this->IntersectionTolerance,t1,x,pcoords,subId);
				if(intersect) {
					if(this->Locator->InsertUniquePoint(x, ptId))
						for(m=0; m<3; m++) center[m] += x[m];
					// now search rest of edges for another intersection
					for(intersect=0; l<numFaceEdges && !intersect; l++) 
						intersect = face->GetEdge(l)->IntersectWithLine(p1,p2,this->IntersectionTolerance,t2,y,pcoords,subId);
					if(intersect) {
						if(this->Locator->InsertUniquePoint(y, ptId))
							for(m=0; m<3; m++) center[m] += y[m];
						if(t1<t2)
							basearea+=(1.0/2.0)*(x[proji[0]]*y[proji[1]]-x[proji[1]]*y[proji[0]]);
						if(t1>t2)
							basearea+=(1.0/2.0)*(y[proji[0]]*x[proji[1]]-y[proji[1]]*x[proji[0]]);
					}
				}
			}

		} // end loop over edges (k)
			

			// Now loop over the edges in the face. 
		double tmpval;
		int edgeId, edgeDir;
		for(k=0; k<numFaceEdges; k++) {
			face->GetEdge(k)->GetPoints()->GetPoint(0,p1);
			face->GetEdge(k)->GetPoints()->GetPoint(1,p2);
			edgeId = HexahedronEdgeMap[i][k];
			tmpval = getIndexedImageValue(p1,p1);
			for(l=0; l<3; l++) x[l] = p1[l];
			if(int(tmpval)==this->Value) {
				inside=1;
				if(this->Locator->InsertUniquePoint(p1, ptId))
					for(l=0; l<3; l++) center[l] += p1[l];
			}
			else
				inside=0;
			tmpval = getIndexedImageValue(p2,p2);			
			if(int(tmpval)==this->Value) {
				if(this->Locator->InsertUniquePoint(p2, ptId))
					for(l=0; l<3; l++) center[l] += p2[l];
			}
			// retrieve intersections, there can be any number
			if(numEdges) {

				// get the "global" edgeId and dir
				if(this->ClipCell->GetCellType() == VTK_HEXAHEDRON){
					edgeId = HexahedronEdgeMap[i][k];
					edgeDir = HexahedronDirMap[k];
				}
				if(this->ClipCell->GetCellType() == VTK_TETRA){
					edgeId = TetrahedronEdgeMap[i][k];
					edgeDir = TetrahedronDirMap[i][k];
				}

				double q1[3], q2[3];
				this->ClipCell->GetEdge(edgeId)->GetPoints()->GetPoint(0,q1);
				this->ClipCell->GetEdge(edgeId)->GetPoints()->GetPoint(1,q2);
				double tmp1, tmp2 = 0;
				for(l=0; l<3 && tmp2==0; l++){
					tmp1 = q2[l]-q1[l];
					tmp2 = p2[l]-p1[l];
				}

				//cout << "edgeDir = " << edgeDir << " real edge dir = " << tmp1/tmp2 << endl;
// 				if(edgeDir != (int)(tmp1/tmp2)) {
// 					cerr << "wrong edge dir" << endl;
// 					cerr << edgeDir << " " << tmp1/tmp2 << endl;
// 					throw ErrProgrammingError("ClipImage3D: wrong edge dir." __FILE__, __LINE__);
// 				}


 				if(edgeDir==1) {
					for(CellEdgeMap::iterator here = clipCellEdgeData[edgeId].begin(); here!=clipCellEdgeData[edgeId].end(); ++here) {
						if(inside) {
							basearea+=(1.0/2.0)*(x[proji[0]]*(*here).second(proji[1])-x[proji[1]]*(*here).second(proji[0]));
						}				
						for(l=0; l<3; l++) x[l] = p1[l] + (p2[l]-p1[l])*((*here).first+this->IntersectionTolerance);
 						inside = (this->IndexedImage->GetScalarComponentAsFloat(int(x[0]),int(x[1]),int(x[2]),0) == this->Value);
					}
				}
			
 				if(edgeDir==-1) {
 					for(CellEdgeMap::reverse_iterator here = clipCellEdgeData[edgeId].rbegin(); here!=clipCellEdgeData[edgeId].rend(); ++here) {
						if(inside) {
							basearea+=(1.0/2.0)*(x[proji[0]]*(*here).second(proji[1])-x[proji[1]]*(*here).second(proji[0]));
						}				
							for(l=0; l<3; l++) x[l] = p1[l] + (p2[l]-p1[l])*((1-(*here).first)+this->IntersectionTolerance);
 						inside = (this->IndexedImage->GetScalarComponentAsFloat(int(x[0]),int(x[1]),int(x[2]),0) == this->Value);
					}
				}


			} // end if(numEdges)

				// check that we have a consistent value for inside
				if( (int(tmpval)==this->Value) != inside){
					cout << "clip cell edge data size: " << clipCellEdgeData[edgeId].size() << endl;
					cerr << tmpval << " " << inside << endl;
					cerr << "finding invalid number of intersection points" << endl;
					cerr << p1[0] << " " << p1[1] << " " << p1[2] << endl;
					cerr << p2[0] << " " << p2[1] << " " << p2[2] << endl;
					throw ErrProgrammingError("ClipImage3D: Finding inconsistent number of intersections." __FILE__, __LINE__);
				}
				if(inside) {
					basearea+=(1.0/2.0)*(x[proji[0]]*p2[proji[1]]-x[proji[1]]*p2[proji[0]]);
				}
					
			} // end loop over face edges


		numPts = this->Locator->GetPoints()->GetNumberOfPoints();
		if(numPts>2) { // if there were any internal and intersection points
			for(k=0; k<3; k++) center[k] /= numPts;
			dot = normal[0]*center[0] + normal[1]*center[1] + normal[2]*center[2]; 
			basearea /= projfactor;
			if( fabs(1.0/3.0 * dot * basearea) > 1e-6 ) {
				for(k=0; k<numPts; k++) {
					newPoints->GetPoint(k,x);
					cout << "point " << k << ": " << x[0] << " " << x[1] << " " << x[2] << endl;
				}
				cout << "normal = " << normal[0] << " " << normal[1] << " " << normal[2] << endl;
				cout << "dot = " << dot << " basearea = " << basearea << endl;
				cout << "volume contrib = " << 1.0/3.0 * dot * basearea << endl;
			}
			volume += 1.0/3.0 * dot * basearea;
		}

		// clean up temporary objects
		edgeExtractor->Delete();
		plane->Delete();
		newPoints->Delete();
		this->Locator->Initialize();
		
	} // end of loop over clip cell faces (i)


  // Clean up
	extractBoundedInput->Delete();
	
  return 1;
}


void ClipImage3D::CreateDefaultLocator()
{
  if ( this->Locator == NULL )
    {
			// we use MergePoints instead of the parent class PointLocator.
			// We only want to merge points if they are exactly coincident.
			// PointLocator merges them based on a tolerance in the distance
			// between their global coordinates.  This is not good since we
			// want the user to be able to use arbitrary units.  The
			// consequence is that we cannot use the uniqueness of points as
			// a test for sanity.  TODO MAYBE: If we decide that we need to
			// use uniqueness, we can set the merge tolerance to a small
			// fraction of the extent of a voxel.
    this->Locator = vtkMergePoints::New();
		//this->Locator->SetTolerance(this->MergeTolerance);
    }
}


int ClipImage3D::FillInputPortInformation(int, vtkInformation *info)
{
  info->Set(vtkAlgorithm::INPUT_REQUIRED_DATA_TYPE(), "vtkPolyData");
  return 1;
}

void ClipImage3D::ReportReferences(vtkGarbageCollector* collector)
{
  this->Superclass::ReportReferences(collector);
	//vtkGarbageCollectorReport(collector, this->ClipCell, "ClipCell");
	//vtkGarbageCollectorReport(collector, this->IndexedImage, "IndexedImage");
}

