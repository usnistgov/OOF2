// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CRYSTALSYMMETRY_SWG
#define CRYSTALSYMMETRY_SWG

%module(package="ooflib.SWIG.engine") crystalsymmetry

%include "common/typemaps.swg"

%{
#include "engine/crystalsymmetry.h"
%}

// The C++ AnisoCrystalSymmetry enum defined in crystalsymmetry.h is
// *not* swigged.  Instead, a Python Enum class is defined in the
// pythoncode block below.  This typemap converts from one to the
// other.

// TODO: Is there a better way to do this?  Can a python Enum
// class be built automatically from a swigged C++ enum?

%typemap(in) AnisoCrystalSymmetry* (AnisoCrystalSymmetry sym) {
  // typemap(in) AnisoCrystalSymmetry*
  PyObject *pname= PyObject_CallMethod($input, "string", NULL);
  PyObject *ustr = PyUnicode_AsEncodedString(pname, "UTF-8", "replace");
  std::string name(PyBytes_AsString(ustr));
  if(name == "Tetragonal")
    sym = TETRAGONAL;
  if(name == "Hexagonal")
    sym = HEXAGONAL;
  if(name == "Cubic")
    sym = CUBIC;
  if(name == "Trigonal")
    sym = TRIGONAL;
  if(name == "Orthorhombic")
    sym = ORTHORHOMBIC;
  if(name == "Monoclinic")
    sym = MONOCLINIC;
  if(name == "Triclinic")
    sym = TRICLINIC;
  $1 = &sym;
};


%pythoncode %{

from ooflib.common import enum
from ooflib.common.IO import xmlmenudump

# Don't change this Enum without also changing crystalsymmetry.h.
class AnisoCrystalSymmetry(enum.EnumClass(
        "Tetragonal",
        "Hexagonal",
        "Cubic",
        "Trigonal",
        "Orthorhombic",
        "Monoclinic",
        "Triclinic")):
    tip="Crystal symmetry types."
    discussion="""<para>
  When computing <link linkend="MenuItem-OOF.OrientationMap.Pole_Figure">
  pole figures</link>, this specifies the crystal symmetry.
  </para>"""

%}


#endif // CRYSTALSYMMETRY_SWG
