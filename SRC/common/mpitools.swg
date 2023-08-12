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

%include "common/typemaps.swg"
%import "common/ooferror.swg"

%{
#include "common/mpitools.h"
%}

void _Initialize(std::vector<char*> *argv);
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

void _Send_IntVec(const std::vector<int>*, int, int);
%newobject _Recv_IntVec;
std::vector<int>* _Recv_IntVec(int, int, int);

void _Send_DoubleVec(std::vector<double>*, int, int);
%newobject _Recv_DoubleVec;
std::vector<double>* _Recv_DoubleVec(int, int, int);

void _Isend_Int(int, const std::vector<int>*, int);
void _Isend_Ints(const std::vector<int>*, const std::vector<int>*, int);
%newobject _Irecv_Ints;
std::vector<int>* _Irecv_Ints(const std::vector<int>*, int);

void _Isend_Double(double, const std::vector<int>*, int);

void _Isend_String(char*, const std::vector<int>*, int);
void _Isend_Strings(char*, const std::vector<int>*, const std::vector<int>*, int);

void _Isend_IntVecs(const std::vector<int>*, const std::vector<int>*, const std::vector<int>*, int);

void _Isend_DoubleVec(std::vector<double>*, const std::vector<int>*, int);
void _Isend_DoubleVecs(std::vector<double>*, const std::vector<int>*, const std::vector<int>*, int);
%newobject _Irecv_DoubleVecs;
std::vector<double>* _Irecv_DoubleVecs(const std::vector<int>*, const std::vector<int>*, int);

bool _Iprobe(int, int);

// collective communications
int _Allreduce_IntSum(int);
double _Allreduce_DoubleSum(double);

%newobject _Allgather_Int;
std::vector<int>* _Allgather_Int(int);
%newobject _Allgather_IntVec;
std::vector<int>* _Allgather_IntVec(const std::vector<int>*, int);
%newobject _Allgather_DoubleVec;
std::vector<double>* _Allgather_DoubleVec(std::vector<double>*, int);

void bcast_ints(const std::vector<int>*, int);
%newobject recv_bcast_ints;
std::vector<int>* recv_bcast_ints(int);

void bcast_doubles(std::vector<double>*, int);
%newobject recv_bcast_doubles;
std::vector<double>* recv_bcast_doubles(int);

void bcast_string(char*, int);
std::string recv_bcast_string(int);

// Args are: Message, filename, line-number, processor
class MPIException : public ErrError {
public:
  std::string message();
  std::string filename();
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

