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
    pid = 1

class JacobiPreconditioner(PreconditionerBase):
    name = "Diag"
    pid = 2

class ILUPreconditioner(PreconditionerBase):
    name = "ILUT"
    pid = 3

class ICPreconditioner(PreconditionerBase):
    name = "IC"
    pid = 4

registeredclass.Registration(
    "Null",
    PreconditionerBase,
    UnPreconditioner,
    ordering=2000,
    params=[],
    tip="Be bold (or foolhardy) and attempt to solve the mesh without a preconditioner",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/null_preconditioner.xml'))

registeredclass.Registration(
    "Jacobi",
    PreconditionerBase,
    JacobiPreconditioner,
    ordering=500,
    params=[],
    tip="A light-weight preconditioner, that simply inverts the diagonal part of the matrix.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/jacobi_preconditioner.xml'))

registeredclass.Registration(
    "ILU",
    PreconditionerBase,
    ILUPreconditioner,
    ordering=100,
    params=[],
    tip="Incomplete LU-factorization",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/ilu_preconditioner.xml')
)

