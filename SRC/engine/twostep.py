# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import sys

from ooflib.SWIG.common import doublevec
from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import timestepper

debugcounter = 0

# TwoStep is a QCTimeStepper (Quality Controlled time stepper) that is
# used by AdaptiveDriver.  It takes one timestep and compares the
# result to two half timesteps in order to get an error estimate.

class TwoStep(timestepper.QCTimeStepper):
    def __init__(self, singlestep):
        self.singlestep = singlestep
    # Most TwoStep methods just pass off the work to the underlying
    # stepper.
    def derivOrder(self):
        return self.singlestep.derivOrder()
    def errorOrder(self):
        return self.singlestep.errorOrder()
    def require_timederiv_field(self):
        return self.singlestep.require_timederiv_field()
    def evaluateBeginning(self):
        return self.singlestep.evaluateBeginning()
    def initialize(self, *args):
        self.singlestep.initialize(*args)
    def shortrepr(self):
        return "TwoStep / " + self.singlestep.shortrepr()
    def computeStaticFieldsL(self, *args, **kwargs):
        self.singlestep.computeStaticFieldsL(*args, **kwargs)
    def computeStaticFieldsNL(self, *args, **kwargs):
        self.singlestep.computeStaticFieldsNL(*args, **kwargs)

    def get_unknowns(self, linsys, source):
        return self.singlestep.get_unknowns(linsys, source)

    def set_unknowns(self, linsys, vals, dest):
        debug.fmsg(f"TwoStep.set_unknowns calling {type(self.singlestep).__name__}.set_unknowns vals={vals.addr()} refcount={debug.getrefcount(vals)}")
        return self.singlestep.set_unknowns(linsys, vals, dest)

    def get_derivs_part(self, part, linsys, unknowns):
        return self.singlestep.get_derivs_part(part, linsys, unknowns)
    def set_derivs_part(self, part, linsys, vals, unknowns):
        return self.singlestep.set_derivs_part(part, linsys, vals, unknowns)
    def n_unknowns(self, linsys):
        return self.singlestep.n_unknowns(linsys)
    def get_unknowns_part(self, part, linsys, unknowns):
        return self.singlestep.get_unknowns_part(part, linsys, unknowns)
    def set_unknowns_part(self, part, linsys, vals, unknowns):
        return self.singlestep.set_unknowns_part(part, linsys, vals, unknowns)

    def M_submatrix(self, linsys, rowpart, colpart):
        return self.singlestep.M_submatrix(linsys, rowpart, colpart)
    def C_submatrix(self, linsys, rowpart, colpart):
        return self.singlestep.C_submatrix(linsys, rowpart, colpart)
    def K_submatrix(self, linsys, rowpart, colpart):
        return self.singlestep.K_submatrix(linsys, rowpart, colpart)
    def J_submatrix(self, linsys, rowpart, colpart):
        return self.singlestep.J_submatrix(linsys, rowpart, colpart)

    def rhs_ind_part(self, part, linsys):
        return self.singlestep.rhs_ind_part(part, linsys)

    def linearstep(self, *args, **kwargs):
        v = self._step(stepper=self.singlestep.linearstep, *args, **kwargs)
        return v

    def explicit(self):
        return self.singlestep.explicit()

    def nonlinearstep(self, *args, **kwargs):
        debug.fmsg("TwoStep.nonlinearstep: calling _step")
        # debug.fmsg(f"kwargs: {kwargs.keys()}")
        result = self._step(stepper=self.singlestep.nonlinearstep,
                          *args, **kwargs)
        return result

    def _step(self, subproblem, linsys, time, unknowns,
             endtime, errorscaling, stepper, *args, **kwargs):
        # If stepper is a nonlinear stepper, then kwargs includes
        # nonlinearMethod.
        #
        # errorscaling is a steperrorscaling.StepErrorScaling
        # instance.
        debug.fmsg(f"unknowns={unknowns.addr()}")
       
            
            
        unknownsCopy = unknowns.clone()
        unknownsCopy.verbose(True)
        debug.fmsg(f"unknownsCopy={unknownsCopy.addr()}")
        lsCopy = linsys.clone()

        # Take a single step to endtime.
        # debug.fmsg("taking full step")
        debug.fmsg(f"Calling stepper {stepper}")
        result1 = stepper(subproblem, linsys, time, unknowns, endtime,
                          *args, **kwargs)
        debug.fmsg(f"back from stepper, result1={result1.endValues.addr()} refcount={debug.getrefcount(result1.endValues)}")
        #debug.fmsg("no, really")
        #debug.fmsg(f"result1 is {'' if result1.endValues.is_verbose() else 'not'} verbose")
        # debug.fmsg("full step norm=", result1.endValues.norm(),
        #            "time=", endtime, "n=", len(result1.endValues))

        # Take a half step.
        halftime = 0.5*(time + endtime)
        debug.fmsg(f"TwoStep getting midresult from {stepper}")
        midresult = stepper(subproblem, lsCopy, time, unknownsCopy, halftime,
                            *args, **kwargs)
        midresult.endValues.verbose(True)
        debug.fmsg(f"back from stepper, midresult={midresult.endValues.addr()} refcount={debug.getrefcount(midresult.endValues)}")        
        # debug.fmsg("first half step norm=", midresult.endValues.norm(),
        #            "time=", halftime)

        # Take the second half step to endtime.
        # debug.fmsg("Twostep._step: calling SubProblemContext.installValues before step 2")
        subproblem.installValues(lsCopy, midresult.endValues, halftime)
        # debug.fmsg("TwoStep._step: back from installValues")
        linsys = subproblem.make_linear_system( halftime, lsCopy )
        # debug.fmsg(f"Calling stepper for step 2")
        result2 = stepper(subproblem, linsys, halftime, midresult.endValues,
                          endtime, *args, **kwargs)
        debug.fmsg(f"result2={midresult.endValues.addr()} refcount={debug.getrefcount(result2)}")
        # debug.fmsg("second half step norm=", result2.endValues.norm(),
        #            "time=", endtime)
        result2.errorEstimate = errorscaling(
            endtime-time,
            self.singlestep.error_estimation_dofs(linsys, unknowns),
            self.singlestep.error_estimation_dofs(linsys, result1.endValues),
            self.singlestep.error_estimation_dofs(linsys, result2.endValues))

        ## TODO: recombine single and double step results to get one
        ## higher order?  This should be done *after* error
        ## estimation, if at all, according to NR.
        debug.fmsg("done")
        return result2


registeredclass.Registration(
    'Two Step',
    timestepper.QCTimeStepper,
    TwoStep,
    ordering=0,
    params=[
        parameter.RegisteredParameter(
            'singlestep', timestepper.TimeStepper,
            tip="Method for individual steps.")],
    tip="Compare the results of one big step to two smaller steps, and adjust the step size to keep the difference within the given tolerance.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/twostep.xml')
)

