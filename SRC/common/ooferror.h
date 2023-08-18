// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFERROR_H
#define OOFERROR_H

#include <oofconfig.h>
#include "common/pythonexportable.h"
#include "common/tostring.h"

#include <iostream>

// Error namespace causes too many problems for SWIG.  Instead,
// use a customizing prefix for error names.

// Base class so that all OOF errors can be caught by the one catch
// statement typemap in oof.swg.

class ErrError : public PythonExportable<ErrError> {
public:
  static PyObject *pyconverter;
  virtual ~ErrError() {}
  // These functions all return pointers to new string objects.  They
  // do this so that the strings may be handed off to Python via swig
  // without additional copying or memory leaks.
  virtual const std::string *summary() const = 0;
  virtual const std::string *details() const { return new std::string(""); }
  virtual void throw_self() const = 0;
  virtual ErrError *clone() const = 0;
};


// ErrErrorBase exists just so that a base class pointer can re-throw
// itself.  It's used in pythonErrorRelay, when throwing a C++
// exception that was originally raised in Python.  The template
// trickery is necessary because it's not possible to throw an object
// of an abstract class (such as ErrError).  The template parameter
// must be the derived class.

template <class E>
class ErrErrorBase : public ErrError {
public:
  virtual void throw_self() const {
    const E *self = dynamic_cast<const E*>(this);
    throw *self;
  }
  ErrError *clone() const {
    return new E(*dynamic_cast<const E*>(this));
  }
};

void pyErrorInit(PyObject*);


// Programming errors are fatal (to the program...)

template <class E>
class ErrProgrammingErrorBase : public ErrErrorBase<E> {
protected:
  const std::string file;
  const int line;
  const std::string msg;
public:
  ErrProgrammingErrorBase(const std::string &f, int l)
    : file(f), line(l), msg("")
  {}
  ErrProgrammingErrorBase(const std::string &m, const std::string &f, int l)
    : file(f), line(l), msg(m)
  {}
  ErrProgrammingErrorBase(const ErrProgrammingErrorBase &other)
    : file(other.file), line(other.line), msg(other.msg)
  {}
  virtual ~ErrProgrammingErrorBase() {}
  virtual const std::string *summary() const {
    return new std::string(file + ":" + tostring(line) + " " + msg);
  }
  // filename and lineno are for reading from Python
  const std::string &filename() const { return file; }
  int lineno() const { return line; }  
};

class ErrProgrammingError
  : public ErrProgrammingErrorBase<ErrProgrammingError>
{
public:
  ErrProgrammingError(const std::string &f, int l);
  ErrProgrammingError(const std::string &m, const std::string &f, int l);
  virtual const std::string &classname() const;
};

class ErrPyProgrammingError
  : public ErrProgrammingErrorBase<ErrPyProgrammingError>
{
public:
  ErrPyProgrammingError(const std::string &m, const std::string &f, int l)
    : ErrProgrammingErrorBase<ErrPyProgrammingError>(m, f, l) {}
  virtual const std::string &classname() const;
};


// Resource shortages are probably fatal.

class ErrResourceShortage : public ErrErrorBase<ErrResourceShortage> {
private:
  const std::string msg;
public:
  ErrResourceShortage(const std::string &m) 
    : msg(m) 
  {}
  ErrResourceShortage(const ErrResourceShortage &other)
    : ErrErrorBase<ErrResourceShortage>(other), msg(other.msg) {}
  virtual ~ErrResourceShortage() {}
  virtual const std::string *summary() const { return new std::string(msg); }
  virtual const std::string &classname() const;
};


class ErrBoundsError : public ErrErrorBase<ErrBoundsError> {
private:
  const std::string msg;
public:
  ErrBoundsError(const std::string &m) 
    : msg(m) 
  {}
  ErrBoundsError(const ErrBoundsError &other)
    : ErrErrorBase<ErrBoundsError>(other), msg(other.msg) {}
  virtual ~ErrBoundsError() {}
  virtual const std::string *summary() const { return new std::string(msg); }
  virtual const std::string &classname() const;
};


class ErrBadIndex : public ErrProgrammingErrorBase<ErrBadIndex> {
private:
  int badindex;
public:
  ErrBadIndex(int i, const std::string &f, int l)
    : ErrProgrammingErrorBase<ErrBadIndex>(f, l),
      badindex(i)
  {}
  ErrBadIndex(const ErrBadIndex &other)
    : ErrProgrammingErrorBase<ErrBadIndex>(other), badindex(other.badindex) {}
  virtual const std::string *summary() const;
  virtual const std::string &classname() const;
};


// User errors shouldn't be fatal.

template <class E>
class ErrUserErrorBase : public ErrErrorBase<E> {
public:
  const std::string msg;
  ErrUserErrorBase(const std::string &m) : msg(m) {}
  ErrUserErrorBase(const ErrUserErrorBase &other)
    : ErrErrorBase<E>(other), msg(other.msg) {}
  virtual ~ErrUserErrorBase() {}
  virtual const std::string *summary() const { return new std::string(msg); }
};

// Generic user error
class ErrUserError : public ErrUserErrorBase<ErrUserError> {
public:
  ErrUserError(const std::string &m) : ErrUserErrorBase<ErrUserError>(m) {}
  ErrUserError(const ErrUserError &other)
    : ErrUserErrorBase<ErrUserError>(other)
  {}
  virtual const std::string &classname() const;
};

class ErrSetupError : public ErrUserErrorBase<ErrSetupError> {
public:
  ErrSetupError(const std::string &m) : ErrUserErrorBase<ErrSetupError>(m) {}
  virtual const std::string &classname() const;
};

class ErrInterrupted : public ErrUserErrorBase<ErrInterrupted> {
public:
  ErrInterrupted() : ErrUserErrorBase<ErrInterrupted>("Interrupted!") {}
  virtual const std::string &classname() const;
};

class ErrDataFileError : public ErrUserErrorBase<ErrDataFileError> {
public:
  ErrDataFileError(const std::string &m)
    : ErrUserErrorBase<ErrDataFileError>(m) {}
  virtual const std::string &classname() const;
};

class ErrWarning : public ErrUserErrorBase<ErrWarning> {
public:
  ErrWarning(const std::string &m)
    : ErrUserErrorBase<ErrWarning>(m) {}
  virtual const std::string &classname() const;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// ErrNoProgress is used when building Progress objects.

class ErrNoProgress : public ErrErrorBase<ErrNoProgress> {
public:
  virtual const std::string &classname() const;
  virtual const std::string *summary() const { return new std::string(""); }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Separate "stub" class for passing Python errors out through C++.
// This happens when a callback sets the Python error state, but 
// doesn't return to the Python environment.  The C++ caller should
// detect the error (by NULL return), and throw this exception,
// which will be caught in the exception typemap.

class PythonError {};

// pythonErrorRelay() should be called when C++ detects that a Python
// exception has been raised in a Python API call, if there's any
// chance that the exception might want to be handled in C++.  It
// converts the Python exception to a C++ exception (ie, an ErrError
// subclass) if possible.  Otherwise it just throws PythonError.

void pythonErrorRelay();

#endif	// OOFERROR_H
