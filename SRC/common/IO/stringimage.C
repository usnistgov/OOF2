// -*- C++ -*-
// $RCSfile: stringimage.C,v $
// $Revision: 1.21 $
// $Author: langer $
// $Date: 2014/09/27 21:40:32 $


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/IO/bitoverlay.h"
#include "common/IO/stringimage.h"
#include "common/trace.h"
#include "common/tostring.h"
#include <set>
#include <string.h>		// for memcpy
#include <iomanip>
#include <math.h>

StringImage::StringImage(const ICoord *isighs, const Coord *sighs)
  : isize_(*isighs), size_(*sighs)
{
  int n = 3*isize_(0)*isize_(1);
  data = new unsigned char[n+1];
  data[n] = '\0';
}

StringImage::~StringImage() {
  delete [] data;
}

int StringImage::getOffset(const ICoord &where) const {
  return 3*((isize_(1)-where(1)-1)*isize_(0) + where(0));
}

void StringImage::set(const ICoord *pos, const CColor *color) {
  int offset = getOffset(*pos);
  data[offset] = (unsigned char)rint(255*color->getRed());
  data[offset+1] = (unsigned char)rint(255*color->getGreen());
  data[offset+2] = (unsigned char)rint(255*color->getBlue());
}

CColor StringImage::get(const ICoord *pos) const {
  int offset = getOffset(*pos);
  return CColor(data[offset]/255., data[offset+1]/255., data[offset+2]/255.);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void inline hexbyte(char *&dest,int num)
{
  dest[0]=num/16;
  dest[1]=num%16;

  if(dest[0]>9)
    dest[0]+='A'-10;
  else
    dest[0]+='0';

  if(dest[1]>9)
    dest[1]+='A'-10;
  else
    dest[1]+='0';
  dest+=2;
}

//gives the string in 24 bit hexadecimal format. Used for pdf output.
const std::string *StringImage::hexstringimage() const
{
  int bytenum=isize_(1)*isize_(0)*3;
  int stringlen=bytenum*2+(bytenum/24);
  char *dest=new char[stringlen+1];
  char *dpos=dest;
  unsigned char *spos=data;

  for(int i=0; i<bytenum; i++) {
    *dpos=*spos/16;		// high order hex digit

    if(*dpos>9)
      *dpos+='a'-10;
    else
      *dpos+='0';
    dpos++;

    *dpos=*spos%16;		// low order hex digit
    if(*dpos>9)
      *dpos+='a'-10;
    else
      *dpos+='0';
    dpos++;

    spos++;
    if(i%24==23)
      *dpos++='\n';
  }
  *dpos=0;

  std::string *ret = new std::string(dest,stringlen);
  delete[] dest;
  return ret;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

AlphaStringImage::AlphaStringImage(const ICoord *isighs, const Coord *sighs)
  :  isize_(*isighs), size_(*sighs)
{
  int n = 4*isize_(0)*isize_(1);
  data = new unsigned char[n+1];
  data[n] = '\0';
}

AlphaStringImage::~AlphaStringImage() {
  delete [] data;
}

int AlphaStringImage::getOffset(const ICoord &where) const {
  return 4*((isize_(1)-where(1)-1)*isize_(0) + where(0));
}

void AlphaStringImage::set(const ICoord *pos, const CColor *color,
			   unsigned char alpha)
{
  int offset = getOffset(*pos);
  data[offset] = (unsigned char)(255*color->getRed());
  data[offset+1] = (unsigned char)(255*color->getGreen());
  data[offset+2] = (unsigned char)(255*color->getBlue());
  data[offset+3] = alpha;
}
