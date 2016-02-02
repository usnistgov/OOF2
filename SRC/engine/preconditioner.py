from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump

class PreconditionerBase(registeredclass.RegisteredClass):
    registry = []
    tip = "Preconditioners for efficient solution of matrix equations."
    discussion = xmlmenudump.loadFile('DISCUSSIONS/engine/reg/preconditioner.xml')
    def shortrepr(self):
        return self.__class__.__name__

class UnPreconditioner(PreconditionerBase):
    name = "Un"

class JacobiPreconditioner(PreconditionerBase):
    name = "Diag"

class ILUTPreconditioner(PreconditionerBase):
    name = "ILUT"

# ILU preconditioner actually points to ILUT preconditioner
class ILUPreconditioner(PreconditionerBase):
    name = "ILU"

registeredclass.Registration(
    "Null",
    PreconditionerBase,
    UnPreconditioner,
    ordering=2000,
    params=[],
    tip="Be bold (or foolhardy) and attempt to solve the mesh without a preconditioner")

registeredclass.Registration(
    "Jacobi",
    PreconditionerBase,
    JacobiPreconditioner,
    ordering=500,
    params=[],
    tip="A light-weight preconditioner, that simply inverts the diagonal part of the matrix.")

registeredclass.Registration(
    "IncompleteLUT",
    PreconditionerBase,
    ILUTPreconditioner,
    ordering=100,
    params=[],
    tip="Incomplete LU-factorization with dual thresholding.")

registeredclass.Registration(
    "ILU",
    PreconditionerBase,
    ILUPreconditioner,
    ordering=101,
    params=[],
    tip="ILU is not supported. It points to IncompleteLUT instead.") 
