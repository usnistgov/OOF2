// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/corientation.h"
#include "common/latticesystem.h"
#include "common/sincos.h"
#include "common/smallmatrix.h"
#include <math.h>

COrientation::COrientation()
  : cachedrot(0)
{}

COrientation::COrientation(const COrientation &other)
  : cachedrot(0)
{
  if(other.cachedrot)
    cachedrot = new SmallMatrix(*other.cachedrot);
}

COrientation::~COrientation() {
  if(cachedrot)
    delete cachedrot;
}

const SmallMatrix &COrientation::rotation() const {
  if(!cachedrot)
    cachedrot = rotation_();
  return *cachedrot;
}

COrientABG COrientation::abg() const {
    return COrientABG(rotation()); 
}

COrientBunge COrientation::bunge() const {
  return COrientBunge(rotation()); 
}

COrientQuaternion COrientation::quaternion() const {
  return COrientQuaternion(rotation());
}

COrientX COrientation::X() const {
  return COrientX(rotation()); 
}

COrientXYZ COrientation::XYZ() const {
  return COrientXYZ(rotation());
}

COrientAxis COrientation::axis() const { 
  return COrientAxis(rotation());
}

COrientRodrigues COrientation::rodrigues() const {
  return COrientRodrigues(rotation());
}

double COrientation::misorientation(const COrientation &other,
				    const LatticeSymmetry &lattice)
  const
{
  // The misorientation between two orientations is the angular part
  // of the axis-angle representation of the "difference" between the
  // orientations.  The difference is the product of one orientation
  // and the inverse of the other.
  SmallMatrix transp(rotation()); // copy the matrix
  transp.transpose();		  // and transpose it
  SmallMatrix diff = other.rotation() * transp;

#ifdef DEBUG
  std::cerr << "COrientation::misorientation:  this=" << axis()
	    << " " << rotation() << std::endl;
  std::cerr << "COrientation::misorientation: other=" << other.axis()
	    << " " << other.rotation()
	    << std::endl;
  std::cerr << "COrientation::misorientation:  diff=" << diff
  	    << " det=" << diff.determinant() << std::endl;
  COrientABG abg(diff);
  std::cerr << "COrientation::misorientation: diff=" << abg << std::endl
  	    << "                                  =" << abg.axis() << std::endl;
#endif // DEBUG
  
  // When the crystal symmetry allows multiple equivalent
  // orientations, we need to measure the difference between one
  // orientation and all possible equivalent versions of the other,
  // and return the minumum misorientation.
  const std::vector<SmallMatrix> &latticerotations(lattice.matrices());
  double minangle = std::numeric_limits<double>::max();
#ifdef DEBUG
  const SmallMatrix *bestrot = nullptr;
#endif // DEBUG
  for(const SmallMatrix &latrot : latticerotations) {
    COrientAxis axisrot(latrot * diff);
    double angle = fabs(axisrot.angle());
    std::cerr << "COrientation::misorientation: latrot=" << latrot
	      << " " << COrientAxis(latrot)
	      << " " << COrientAxis(latrot).rotation()
	      << "\t misorient. angle=" << angle*180/M_PI << std::endl;
    if(fabs(angle) < fabs(minangle)) {
      minangle = angle;
#ifdef DEBUG
      bestrot = &latrot;
#endif // DEBUG
    }
  }
#ifdef DEBUG
  std::cerr << "COrientation::misorientation: minangle=" << minangle
	    << " lattice rotation=" << *bestrot << std::endl;
#endif // DEBUG
  return minangle;
}

double COrientation::misorientation(const COrientation &other,
				    const std::string &lattice)
  const
{
  // "lattice" is a Schoenflies symbol
  return misorientation(other, *getLatticeSymmetry(lattice));
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


COrientABG::COrientABG(const SmallMatrix &matrix) {
  double cosa = matrix(2,2);
  double sina = sqrt(matrix(2,0)*matrix(2,0) + matrix(2,1)*matrix(2,1));
  double sinb, cosb, sing, cosg;
  if(sina != 0.0) {
    // Skip division by sina, it just gets eaten by the arctangent.
    cosb = matrix(2,0);
    sinb = matrix(2,1);
    cosg = -matrix(0,2);
    sing = matrix(1,2);
  }
  else {
    if(cosa > 0.0) {		// i.e., it's 1.0, but there's roundoff.
      cosb = matrix(0,0);
      sinb = matrix(0,1);
      sing = 0.0;
      cosg = 1.0;
    }
    else {			// In this case, cosa must be -1.
      cosb = -matrix(0,0);
      sinb = -matrix(0,1);
      sing = 0.0;
      cosg = 1.0;
    }
  }
  alpha_ = atan2(sina, cosa);
  beta_ = atan2(sinb, cosb);
  gamma_ = atan2(sing, cosg);
}

SmallMatrix *COrientABG::rotation_() const {
  double cosa, sina, cosb, sinb, cosg, sing;
  sincos(alpha_, sina, cosa);
  sincos(beta_, sinb, cosb);
  sincos(gamma_, sing, cosg);
  
  SmallMatrix *r = new SmallMatrix(3, 3);
  (*r)(0, 0) =  cosa*cosb*cosg - sinb*sing;
  (*r)(0, 1) =  cosa*sinb*cosg + cosb*sing;
  (*r)(0, 2) = -sina*cosg;
  (*r)(1, 0) = -cosa*cosb*sing - sinb*cosg;
  (*r)(1, 1) = -cosa*sinb*sing + cosb*cosg;
  (*r)(1, 2) =  sina*sing;
  (*r)(2, 0) =  sina*cosb;
  (*r)(2, 1) =  sina*sinb;
  (*r)(2, 2) =  cosa;
  return r;
}

bool COrientABG::operator==(const COrientABG &other) const {
  return alpha_==other.alpha_ && beta_==other.beta_ && gamma_==other.gamma_;
}

bool COrientABG::operator!=(const COrientABG &other) const {
  return alpha_!=other.alpha_ or beta_!=other.beta_ or gamma_!=other.gamma_;
}

void COrientABG::print(std::ostream &os) const {
  os << "COrientABG(alpha=" << alpha() << ", beta=" << beta()
     << ", gamma=" << gamma() << ")";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

COrientBunge::COrientBunge(const SmallMatrix &matrix) {
  double costh = matrix(2,2);
  double sinth = sqrt(matrix(2,0)*matrix(2,0) + matrix(2,1)*matrix(2,1));
  double cosph1, sinph1, cosph2, sinph2;
  if(sinth != 0.0) {
    //  Strictly speaking, should divide by sinth, but they go
    //  into the arctangent, so the common factor would cancel
    //  anyways, so skip it.
    cosph1 = -matrix(1,2);
    sinph1 = matrix(0,2);
    cosph2 = matrix(2,1);
    sinph2 = matrix(2,0);
  }
  else {
    // Same-axis rotation, so let phi2 be zero, and figure out phi1.
    cosph1 = matrix(0,0);
    sinph1 = matrix(1,0);
    cosph2 = 1.0;
    sinph2 = 0.0;
  }
  phi1_ = atan2(sinph1, cosph1);
  theta_ = atan2(sinth, costh);
  phi2_ = atan2(sinph2, cosph2);
};

SmallMatrix *COrientBunge::rotation_() const {
  double sinph1, cosph1, sinph2, cosph2, sinth, costh;
  sincos(phi1_, sinph1, cosph1);
  sincos(phi2_, sinph2, cosph2);
  sincos(theta_, sinth, costh);
  SmallMatrix *r = new SmallMatrix(3,3);
  (*r)(0,0) = cosph1*cosph2-sinph1*sinph2*costh;
  (*r)(0,1) = -cosph1*sinph2-sinph1*cosph2*costh;
  (*r)(0,2) = sinph1*sinth;

  (*r)(1,0) = sinph1*cosph2+cosph1*sinph2*costh;
  (*r)(1,1) = -sinph1*sinph2+cosph1*cosph2*costh;
  (*r)(1,2) = -cosph1*sinth;

  (*r)(2,0) = sinph2*sinth;
  (*r)(2,1) = cosph2*sinth;
  (*r)(2,2) = costh;
  return r;
}

void COrientBunge::print(std::ostream &os) const {
  os << "COrientBunge(phi1=" << phi1() << ", theta=" << theta()
     << ", phi2=" << phi2() << ")";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

COrientQuaternion::COrientQuaternion(double e0, double e1,
				     double e2, double e3)
{
  q[0] = e0;
  q[1] = e1;
  q[2] = e2;
  q[3] = e3;
  // Un-normalized quaternions are probably dangerous, they
  // result in all the entries in the matrix being too large by a
  // factor of the normalization squared, which means the deduced
  // cosine from the "corner" entry will be wrong.  So, normalize.
  double n2 = norm2();
  if(n2==0.0) { // Presume the user meant "no rotation".
    q[0] = 1.0;
    for(unsigned int i=1; i<4; i++)
      q[i] = 0.0;
  }
  else {
    double norm = 1./sqrt(n2);
    for(unsigned int i=0; i<4; i++)
      q[i] *= norm;
  }
}

COrientQuaternion::COrientQuaternion(const SmallMatrix &matrix) {
  // See https://en.wikipedia.org/wiki/Rotation_matrix#Quaternion
  double t = matrix(0,0) + matrix(1,1) + matrix(2,2);
  if(t > 0) {
    double r = sqrt(1 + t);
    double s = 1/(2*r);
    q[0] = r/2.;
    q[1] = (matrix(1,2) - matrix(2,1))*s;
    q[2] = (matrix(2,0) - matrix(0,2))*s;
    q[3] = (matrix(0,1) - matrix(1,0))*s;
  } // end if t > 0
  else {
    // If the trace is negative (near -1, actually) we could be
    // dividing by something small in the expression above, so don't
    // do that.  This version is copied from
    // http://www.gamasutra.com/view/feature/131686/rotating_objects_using_quaternions.php
    // and implements the algorithm suggested in the wikipedia
    // article.
    int i = 0; 		
    if(matrix(1,1) > matrix(0,0)) i = 1;
    if(matrix(2,2) > matrix(i,i)) i = 2;
    int j = (i+1) % 3;
    int k = (j+1) % 3;
    double s = sqrt(1. + matrix(i,i) - matrix(j,j) - matrix(k,k));
    q[i] = 0.5*s;
    if(s != 0)
      s = 0.5/s;
    q[3] = (matrix(k,j) - matrix(j,k))*s;
    q[j] = (matrix(j,i) + matrix(i,j))*s;
    q[k] = (matrix(k,i) + matrix(i,k))*s;
  }
}

double COrientQuaternion::norm2() const {
  double sum = 0;
  for(unsigned int i=0; i<4; i++)
    sum += q[i]*q[i];
  return sum;
}

SmallMatrix *COrientQuaternion::rotation_() const {
  SmallMatrix *matrix = new SmallMatrix(3,3);

  double q0 = q[0];
  double q1 = q[1];
  double q2 = q[2];
  double q3 = q[3];

  (*matrix)(0,0) = q0*q0 + q1*q1 - q2*q2 - q3*q3;
  (*matrix)(0,1) = 2.0*(q1*q2 + q0*q3);
  (*matrix)(0,2) = 2.0*(q1*q3 - q0*q2);

  (*matrix)(1,0) = 2.0*(q1*q2 - q0*q3);
  (*matrix)(1,1) = q0*q0 - q1*q1 + q2*q2 - q3*q3;
  (*matrix)(1,2) = 2.0*(q2*q3 + q0*q1);

  (*matrix)(2,0) = 2.0*(q1*q3 + q0*q2);
  (*matrix)(2,1) = 2.0*(q2*q3 - q0*q1);
  (*matrix)(2,2) = q0*q0 - q1*q1 - q2*q2 + q3*q3;

  return matrix;
}

COrientAxis COrientQuaternion::axis() const {
  double vnorm = sqrt(q[1]*q[1] + q[2]*q[2] + q[3]*q[3]); // norm of vector part
  double angle = 2*atan2(vnorm, q[0]);
  return COrientAxis(angle, q[1]/vnorm, q[2]/vnorm, q[3]/vnorm);
}

void COrientQuaternion::print(std::ostream &os) const {
  os << "COrientQuaternion(e0=" << e0() << ", e1=" << e1() << ", e2=" << e2()
     << ", e3=" << e3() << ")";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Goldstein's "X" convention.  This may have some other more
// descriptive name, but I don't know what it is.  Rotations are z,x,z.

COrientX::COrientX(const SmallMatrix &matrix) {
  double costh = matrix(2,2);
  double sinth = sqrt(matrix(0,2)*matrix(0,2)+ matrix(1,2)*matrix(1,2));
  double sinps, cosps, sinph, cosph;
  if(sinth != 0.0) {
    // Skip division by sinth in these terms, since the common factor
    // will cancel out in the arctangent anyways.
    cosps = matrix(1,2);
    sinps = matrix(0,2);
    cosph = -matrix(2,1);
    sinph = matrix(2,0);
  }
  else {
    // Same-axis rotation, let psi be zero, figure out phi.
    cosph = matrix(0,0);
    sinph = matrix(0,1);
    cosps = 1.0;
    sinps = 0.0;
  }
  phi_ = atan2(sinph, cosph);
  theta_ = atan2(sinth, costh);
  psi_ = atan2(sinps, cosps);
}

SmallMatrix *COrientX::rotation_() const {
  double sinph, cosph, sinps, cosps, sinth, costh;
  sincos(phi_, sinph, cosph);
  sincos(theta_, sinth, costh);
  sincos(psi_, sinps, cosps);

  SmallMatrix *matrix = new SmallMatrix(3,3);

  (*matrix)(0,0) = cosps*cosph - costh*sinph*sinps;
  (*matrix)(0,1) = cosps*sinph + costh*cosph*sinps;
  (*matrix)(0,2) = sinps*sinth;

  (*matrix)(1,0) = -sinps*cosph - costh*sinph*cosps;
  (*matrix)(1,1) = -sinps*sinph + costh*cosph*cosps;
  (*matrix)(1,2) = cosps*sinth;

  (*matrix)(2,0) = sinth*sinph;
  (*matrix)(2,1) = -sinth*cosph;
  (*matrix)(2,2) = costh;

  return matrix;
};

void COrientX::print(std::ostream &os) const {
  os << "COrientX(phi=" << phi() << ", theta=" << theta() << ", psi=" << psi()
     << ")";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// The "aerodynamic" XYZ convention, with each rotation about a
// different principal axis.  Again the name is from Goldstein.

COrientXYZ::COrientXYZ(const SmallMatrix &matrix) {
  double sinth = matrix(2,0);
  double  costh = sqrt(matrix(2,2)*matrix(2,2)+
		       matrix(2,1)*matrix(2,1));
  double sinph, cosph, sinps, cosps;
  if(costh!=0.0) {
    // Strictly speaking, the sin of phi is this quantity divided by
    // the cosine of theta, but since both terms are divided, and they
    // go into an arctangent routine, we just skip it, and get the
    // same answer.
    sinph = -matrix(2,1);
    cosph = matrix(2,2);
    sinps = -matrix(1,0);
    cosps = matrix(0,0);
  }
  else {
    sinph = matrix(0,1);
    cosph = matrix(1,1);
    sinps = 0.0;
    cosps = 1.0;
  }
  phi_ = atan2(sinph, cosph);
  theta_ = atan2(sinth, costh);
  psi_ = atan2(sinps, cosps);
}

SmallMatrix *COrientXYZ::rotation_() const {
  double sinph, cosph, sinps, cosps, sinth, costh;
  sincos(phi_, sinph, cosph);
  sincos(theta_, sinth, costh);
  sincos(psi_, sinps, cosps);

  SmallMatrix *matrix = new SmallMatrix(3,3);

  (*matrix)(0,0) = cosps*costh;
  (*matrix)(0,1) = cosps*sinph*sinth+cosph*sinps;
  (*matrix)(0,2) = sinph*sinps-cosph*cosps*sinth;

  (*matrix)(1,0) = -costh*sinps;
  (*matrix)(1,1) = cosph*cosps-sinph*sinps*sinth;
  (*matrix)(1,2) = cosph*sinps*sinth+cosps*sinph;

  (*matrix)(2,0) = sinth;
  (*matrix)(2,1) = -costh*sinph;
  (*matrix)(2,2) = cosph*costh;

  return matrix;
}

void COrientXYZ::print(std::ostream &os) const {
  os << "COrientXYZ(phi=" << phi() << ", theta=" << theta()
     << ", psi=" << psi() << ")";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

COrientAxis::COrientAxis(const SmallMatrix &matrix) {
  COrientQuaternion quat(matrix);
// #ifdef DEBUG
//   if(quat.norm2() != 1)
//     std::cerr << "COrientAxis::ctor: |quat|=" << quat.norm2() << std::endl;
// #endif // DEBUG
  double sin_half_theta = sqrt(quat.e1()*quat.e1()+quat.e2()*quat.e2()+
			     quat.e3()*quat.e3());
  double cos_half_theta = quat.e0();
  // std::cerr << "COrientAxis::ctor: quat=" << quat
  // 	    << " s=" << sin_half_theta << " c=" << cos_half_theta
  // 	    << std::endl;

  angle_ = 2.0*atan2(sin_half_theta, cos_half_theta);
  // Assume z-axis in the absence of clues.
  if(sin_half_theta == 0.0) {
    x_ = 0.0;
    y_ = 0.0;
    z_ = 1.0;
  }
  else {
    double scale = 1./sin_half_theta;
    x_ = quat.e1()*scale;
    y_ = quat.e2()*scale;
    z_ = quat.e3()*scale;
  }
}

SmallMatrix *COrientAxis::rotation_() const {
  return quaternion().rotation_();
}

COrientQuaternion COrientAxis::quaternion() const {
  double cos_half_theta, sin_half_theta;
  sincos(0.5*angle_, sin_half_theta, cos_half_theta);
  double norm2 = x_*x_ + y_*y_ + z_*z_;
  assert(norm2 != 0.0);
  double factor = sin_half_theta/sqrt(norm2);
  return COrientQuaternion(cos_half_theta, x_*factor, y_*factor, z_*factor);
			   
}

void COrientAxis::print(std::ostream &os) const {
  os << "COrientAxis(angle=" << angle() << ", x=" << x() << ", y=" << y()
     << ", z=" << z() << ")";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Rodrigues vector. Another way of describing crystal orientations.
// This form is quite popular in the texture community; it is
// particularly useful to describe fiber-texture and poling in
// ferroelectrics. --REG

// The vector points along the axis of the rotation, and its magnitude
// is the tangent of half the angle of the rotation.

COrientRodrigues::COrientRodrigues(const SmallMatrix &matrix) {
  COrientQuaternion quat(matrix);
  double norm;			// secant of half of the rotation angle
  if(quat.e0() != 0.0) {
    norm = 1./quat.e0();
  }
  else {
    // The Rodrigues vector has a singularity at theta = \pm pi.  We
    // want to avoid the singularity, so we set 1/cos(pi/2) = 2.e9.
    // acos(1/2.e9) is within 10^-9 of pi/2, which ought to be good
    // enough precision for an orientation.
    norm = 2.0e9;
  }
  r1_ = quat.e1()*norm;
  r2_ = quat.e2()*norm;
  r3_ = quat.e3()*norm;
  // The above relationship was extracted from A. Heinz, and
  // P. Neumann "Representation of Orientation and Disorientation Data
  // for Cubic, Hexagonal, Tetragonal, and Orthorhombic
  // Crystals". Acta Cryst. (1991) A47, 780-789
}

SmallMatrix *COrientRodrigues::rotation_() const {
  double mag2 = r1_*r1_ + r2_*r2_ + r3_*r3_;
  double q0 = 1./sqrt(1.0 + mag2);
  return COrientQuaternion(q0, q0*r1_, q0*r2_, q0*r3_).rotation_();
  // The above equations were taken from A. Morawiec, and D. P. Field
  // "Rodrigues parametrization for orientation and misorientation
  // distributions". Phylosophical Magazine A, 1996, Vol. 73, No. 4,
  // 1113-1130
}

void COrientRodrigues::print(std::ostream &os) const {
  os << "COrientRodrigues(r1=" << r1() << ", r2=" << r2() << ", r3=" << r3()
     << ")";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream &operator<<(std::ostream &os, const COrientation &orient) {
  orient.print(os);
  return os;
}
