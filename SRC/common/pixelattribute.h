// -*- C++ -*-
// $RCSfile: pixelattribute.h,v $
// $Revision: 1.12 $
// $Author: langer $
// $Date: 2014/09/27 21:40:26 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef PIXELATTRIBUTE_H
#define PIXELATTRIBUTE_H

#include "common/coord.h"
#include "common/array.h"
#include "common/pythonexportable.h"
#include <string>
#include <vector>

class CMicrostructure;

// Pixels in a Microstructure are assigned a set of attributes.
// Pixels with the same set of attributes are put into the same
// category.  When a mesh is generated, it is adjusted to segregate
// pixels of different categories into different elements.

// In principle, the attributes of a pixel may not be definable within
// the "common" module, where the Microstructure lives.  For example,
// the Material assigned to a pixel is an attribute, but it's defined
// in "engine".  Therefore we need a generic way of managing unknown
// attributes.

// Each type of pixel attribute has two classes associated with it,
// derived from the base classes PixelAttribute and
// PxlAttributeRegistration.  The PxlAttributeRegistration contains
// information about how to create the attributes, retrieve values
// from a Microstructure, and save them to a file.  There is one
// PxlAttributeRegistration instance for each type of pixel attribute.
// On the other hand, there is one PixelAttribute instance for each
// pixel in the Microstructure (for each attribute type).

// Subclasses of PixelAttribute must provide an operator< const member
// function which takes a const PixelAttribute& argument.  The
// argument can be safely cast (with dynamic_cast) to the derived
// type.  This function is what's used to determine if two attributes
// are different when categorizing pixels.

// Subclasses of PixelAttribute must also provide a strictLessThan
// method, which is exactly like operator< except that it notices
// differences that are not usually important.  It's used when
// categorizing pixels in order to save them in a data file.  For
// example, the pixel group attribute's operator< ignores groups that
// don't have the "meshable" flag set, but strictLessThan does not
// ignore the flag.

// Subclasses of PxlAttributeRegistration have the following requirements:

// 1. They must define a virtual function, createAttribute(), which
// returns a pointer to a new PixelAttribute of the appropriate
// derived type.

// 1a. They may contain an optional function
// createAttributeGlobalData(), which creates a subclass of
// PixelAttributeGlobalData, which holds data specific to a
// Microstructure but not to a pixel.

// 2. PxlAttributeRegistration is a PythonExportable class, so
// subclasses must define classname() and modulename() functions.

// 3. The subclass must be swigged.

// 4. The OOF.LoadData.Microstructure.DefineCategory menu (aka
// common.IO.microstructureIO.categorymenu) must be given a menu item
// whose name is the name of the PxlAttributeRegistration. This menu
// item reads attributes from a data file and stores them in a
// Microstructure.  It has at least two arguments: a microstructure
// name ("microstructure") and an integer ("category").  To be useful
// it should have *additional* arguments that define a pixel attribute.
// The callback should use microstructureIO.getCategoryPixels() to
// retrieve the list of pixels in the given category and then assign
// the pixel attribute to those pixels.

// 5. The Python shadow class for the PxlAttributeRegistration must
// have a writeData() function which writes the additional arguments
// mentioned above into a datafile.  The arguments to writeData are
// the DataFile object (see common/IO/datafile.py), the
// Microstructure, and a representative pixel from the Microstructure.
// The attributes of the given pixel should be used to construct the
// arguments, which should be written to the file with
// DataFile.argument().  If the given pixel does not have the
// attribute (eg, a pixel to which no Material has been assigned)
// writeData should return 0 and not call DataFile.argument().
// Otherwise it should return 1.

// 6. A single instance of the subclass must be created.


// The CMicrostructure keeps a list of arrays of pointers to
// PixelAttributes.  The attribute code can get access to the array
// with PxlAttributeRegistration::map(CMicrostructure&).  It can then
// set the attributes for individual pixels in the array.

// -------------

// Base class for attributes.

class PixelAttribute {
public:
  virtual ~PixelAttribute() {}
  virtual bool operator<(const PixelAttribute&) const = 0;
  virtual bool strictLessThan(const PixelAttribute&) const = 0;
  virtual void print(std::ostream&) const = 0; // for debugging
};

class PixelAttributeGlobalData {
public:
  virtual ~PixelAttributeGlobalData() {}
};

// The PxlAttributeRegistration class stores information about a set
// of Attributes: name, initialization function, output functions, etc.

class PxlAttributeRegistration
  : public PythonExportable<PxlAttributeRegistration>
{
private:
  static std::vector<PxlAttributeRegistration*> &registrations();
  const std::string name_;
  int index_;
  friend class CMicrostructure;
public:
  PxlAttributeRegistration(const std::string &name);
  virtual ~PxlAttributeRegistration() {}
  static int nRegistrations() { return registrations().size(); }
  static const PxlAttributeRegistration *getRegistration(int i);
  const std::string &name() const { return name_; }
  // Get the appropriate pixel map from the microstructure.
  Array<PixelAttribute*> &map(const CMicrostructure*) const;
  PixelAttributeGlobalData *globalData(const CMicrostructure*) const;

  // Create a PixelAttribute object of the appropriate type.
  virtual PixelAttribute *createAttribute(const ICoord &x) const = 0;

  virtual PixelAttributeGlobalData *createAttributeGlobalData(const
							      CMicrostructure*)
    const { return 0; }

};

std::ostream &operator<<(std::ostream&, const PixelAttribute&);

int nAttributes();
const PxlAttributeRegistration *getRegistration(int);

#endif
