// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// NOTE: Updated for swig4 but not tested at all!

#ifndef MPITOOLS_SWG
#define MPITOOLS_SWG

%module(package="ooflib.SWIG.common") mpitools

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "common/ooferror.swg"
#endif // NOSECONDIMPORTS

%{
#include "common/mpitools.h"
%}

void _Initialize(CharPtrVec *argv);
int Initialized();
void Finalize();
void Abort();
int Size();
int Rank();
std::string Get_processor_name();
void Barrier();

// p2p communications
void _Send_Int(int, int, int);
int _Recv_Int(int, int);

int _Sendrecv_Int(int, int, int);

void _Send_Double(double, int, int);
double _Recv_Double(int, int);

void _Send_String(char*, int, int);
std::string _Recv_String(int, int, int);

void _Send_IntVec(IntVec*, int, int);
%newobject _Recv_IntVec;
IntVec* _Recv_IntVec(int, int, int);

void _Send_DoubleVec(DoubleList*, int, int);
%newobject _Recv_DoubleVec;
DoubleList* _Recv_DoubleVec(int, int, int);

void _Isend_Int(int, IntVec*, int);
void _Isend_Ints(IntVec*, IntVec*, int);
%newobject _Irecv_Ints;
IntVec* _Irecv_Ints(IntVec*, int);

void _Isend_Double(double, IntVec*, int);

void _Isend_String(char*, IntVec*, int);
void _Isend_Strings(char*, IntVec*, IntVec*, int);

void _Isend_IntVecs(IntVec*, IntVec*, IntVec*, int);

void _Isend_DoubleVec(DoubleList*, IntVec*, int);
void _Isend_DoubleVecs(DoubleList*, IntVec*, IntVec*, int);
%newobject _Irecv_DoubleVecs;
DoubleList* _Irecv_DoubleVecs(IntVec*, IntVec*, int);

bool _Iprobe(int, int);

// collective communications
int _Allreduce_IntSum(int);
double _Allreduce_DoubleSum(double);

%newobject _Allgather_Int;
IntVec* _Allgather_Int(int);
%newobject _Allgather_IntVec;
IntVec* _Allgather_IntVec(IntVec*, int);
%newobject _Allgather_DoubleVec;
DoubleList* _Allgather_DoubleVec(DoubleList*, int);

void bcast_ints(IntVec*, int);
%newobject recv_bcast_ints;
IntVec* recv_bcast_ints(int);

void bcast_doubles(DoubleList*, int);
%newobject recv_bcast_doubles;
DoubleList* recv_bcast_doubles(int);

void bcast_string(char*, int);
std::string recv_bcast_string(int);

// Args are: Message, filename, line-number, processor
class MPIException : public ErrError {
public:
  string message();
  string filename();
  int lineno();
  MPIException(char *, char *, int, int);
  ~MPIException();
};

%extend MPIException {
  std::string __repr__() {
    // TODO: To be like other oof2 reprs, this should return a new
    // string*.  But since it's not used at the moment I'm not going
    // to change it, because I don't know if MPIException::message can
    // be changed to return a pointer.
    return self->message();
  }
};

%pythoncode "common/mpitools.spy"

#endif // MPITOOLS_SWG

