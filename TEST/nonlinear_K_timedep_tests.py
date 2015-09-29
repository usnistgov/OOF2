# -*- python -*-
# $RCSfile: nonlinear_K_timedep_tests.py,v $
# $Revision: 1.8 $
# $Author: langer $
# $Date: 2011/04/14 21:01:43 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import unittest 
import os
import memorycheck
import exact_solns

class NonlinearTimedependentTest(unittest.TestCase):
    def setUp(self):
        self.numX = 20
        self.numY = 20

        OOF.Microstructure.New(
            name='microstructure',
            width=1.0, height=1.0, width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(
            name='material', material_type='bulk')
        OOF.Material.Assign(
            material='material', microstructure='microstructure',
            pixels=all)
        OOF.Skeleton.New(
            name='skeleton', microstructure='microstructure',
            x_elements=self.numX, y_elements=self.numY,
            skeleton_geometry=QuadSkeleton(
                left_right_periodicity=False,top_bottom_periodicity=False))
        OOF.Mesh.New(
            name='mesh',
            skeleton='microstructure:skeleton',
            element_types=['D2_2', 'T3_3', 'Q4_4'])

    def tearDown(self):
        OOF.Material.Delete(name='material')
        ## We have to delete all named Properties because they can
        ## interfere with other tests.  It's not correct to do it
        ## here, because this tearDown routine is called for all
        ## tests, but different Properties might have been created in
        ## different tests.  At the moment, this seems to work, and
        ## fixing it is nontrivial.
        OOF.Property.Delete(
            property='Thermal:HeatCapacity:ConstantHeatCapacity:cap')

    def heatConductivity(self, test_no, source_no):
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh',
            field=Temperature)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Heat_Eqn)

        OOF.Property.Parametrize.Thermal.Conductivity.\
            TestNonlinearHeatConductivity(
            testno=test_no)
        OOF.Material.Add_property(
            name='material',
            property='Thermal:Conductivity:TestNonlinearHeatConductivity')
        # add the nonconstant heat source property to the material
        OOF.Property.Parametrize.Thermal.HeatSource.TestNonconstantHeatSource(
            testno=source_no)
        OOF.Material.Add_property(
            name='material',
            property='Thermal:HeatSource:TestNonconstantHeatSource')

        OOF.Property.Copy(
            property='Thermal:HeatCapacity:ConstantHeatCapacity',
            new_name='cap')
        OOF.Property.Parametrize.Thermal.HeatCapacity.ConstantHeatCapacity.cap(
            cv=100.0)
        OOF.Material.Add_property(
            name='material',
            property='Thermal:HeatCapacity:ConstantHeatCapacity:cap')

    def newton(self):
        self.nlsolver = Newton(
            relative_tolerance=1e-08,
            absolute_tolerance=1.0e-13,
            maximum_iterations=20)

    def picard(self):
        self.nlsolver = Picard(
            relative_tolerance=1e-08,
            absolute_tolerance=1.0e-13,
            maximum_iterations=20)

    def linear(self):
        self.nlsolver = NoNonlinearSolver()

    def uniform(self, stepper, timestep=0.01):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
               time_stepper=UniformDriver(
                    stepsize=timestep,
                    stepper=stepper),
               nonlinear_solver=self.nlsolver,
               symmetric_solver=ConjugateGradient(
                   preconditioner=ILUPreconditioner(),
                   tolerance=1e-13,
                   max_iterations=1000),
               asymmetric_solver=BiConjugateGradient(
                   preconditioner=ILUPreconditioner(),
                   tolerance=1e-13,
                   max_iterations=1000)))

    def adaptive(self, stepper, initialstep=0.1, steptol=1.e-5):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
               time_stepper=AdaptiveDriver(
                    initialstep=initialstep,
                    tolerance=steptol,
                    minstep=1.e-8,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=stepper)),
               nonlinear_solver=self.nlsolver,
               symmetric_solver=ConjugateGradient(
                   preconditioner=ILUPreconditioner(),
                   tolerance=1e-13,
                   max_iterations=1000),
               asymmetric_solver=BiConjugateGradient(
                   preconditioner=ILUPreconditioner(),
                   tolerance=1e-13,
                   max_iterations=1000)))

    def setBoundaryConditions(self, BC_type, BC_field, BC_equation,BC_list):
        for BC_no, BC in enumerate(BC_list):
            if BC_type == 'Dirichlet':
                new_BC = DirichletBC(
                    field           = BC_field,
                    field_component = BC[1],
                    equation        = BC_equation,
                    eqn_component   = BC[2],
                    profile         = ContinuumProfileXTd(
                                          function        = BC[3],
                                          timeDerivative  = BC[4],
                                          timeDerivative2 = BC[5]),
                    boundary        = BC[0])

            elif BC_type == 'Neumann':
                new_BC = NeumannBC(
                    field           = BC_field,
                    field_component = BC[1],
                    equation        = BC_equation,
                    eqn_component   = BC[2],
                    profile         = ContinuumProfileXTd(
                                          function        = BC[3],
                                          timeDerivative  = BC[4],
                                          timeDerivative2 = BC[5]),
                    boundary        = BC[0])

            OOF.Mesh.Boundary_Conditions.New(
                name = 'bc<%d>'%BC_no,
                mesh = 'microstructure:skeleton:mesh',
                condition = new_BC )

    def initializeScalarFields(self, field, func):
        OOF.Mesh.Set_Field_Initializer(
            mesh="microstructure:skeleton:mesh",
            field=field,
            initializer=FuncScalarFieldInit(function=func))
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh',
            time=0.0)

    def setOutput(self, interval=0.01):
        # OOF.Mesh.Scheduled_Output.New(
        #     mesh='microstructure:skeleton:mesh',
        #     name=AutomaticName('MeshFileOutput'), output=MeshFileOutput())
        try:
            OOF.Mesh.Scheduled_Output.Delete(
                mesh='microstructure:skeleton:mesh',
                output='GraphicsUpdate')
        except:
            pass
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name=AutomaticName('GraphicsUpdate'), output=GraphicsUpdate())
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('GraphicsUpdate'),
            scheduletype=AbsoluteOutputSchedule(),
            schedule=Periodic(delay=0.0,interval=interval))


    def check(self, time, soln, tolerance, expected=True):
        from ooflib.engine import mesh
        from ooflib.SWIG.engine import field
        
        mesh_obj = mesh.meshes["microstructure:skeleton:mesh"].getObject()
        L2_error = exact_solns.computeScalarErrorL2(
            soln, mesh_obj, Temperature, self.numX, self.numY, time=time)
        print >> sys.stderr, "L2 error = %g" % L2_error
        self.assert_((L2_error < tolerance) == expected)

    def uniformTest(self, stepper, solver, time,
                    nsteps, tolerance,
                    test_no, source_no, soln_no):
        self.heatConductivity(test_no, source_no)
        solver()
        soln_data = exact_solns.exact_solns["scalar"][soln_no]
        self.setBoundaryConditions('Dirichlet', Temperature, Heat_Eqn,
                                   soln_data["DirichletBC"])
        self.uniform(stepper, timestep=time/nsteps)
        self.initializeScalarFields(Temperature, soln_data["Solution"])
        # Requiring output at intermediate times exercises the time
        # step selection logic, especially when the timesteps fall
        # within roundoff error of the output times..
        self.setOutput()
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=time)
        self.check(time, soln_data["Solution"], tolerance)


    def uniformTest2(self, stepper, solver, time,
                    nsteps, tolerance,
                    test_no, source_no, soln_no):
        # Check that everything still works if the time evolution is
        # performed in two stages.
        self.heatConductivity(test_no, source_no)
        solver()
        soln_data = exact_solns.exact_solns["scalar"][soln_no]
        self.setBoundaryConditions('Dirichlet', Temperature, Heat_Eqn,
                                   soln_data["DirichletBC"])
        self.uniform(stepper, timestep=time/nsteps)
        self.initializeScalarFields(Temperature, soln_data["Solution"])
        # Requiring output at intermediate times exercises the time
        # step selection logic, especially when the timesteps fall
        # within roundoff error of the output times..
        self.setOutput()
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=time)
        self.check(time, soln_data["Solution"], tolerance)
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=2*time)
        self.check(2*time, soln_data["Solution"], tolerance)

    def uniformTestQS(self, stepper, solver, time,
                    nsteps, tolerance,
                    test_no, source_no, soln_no):
        # Check that removing the heat capacity property, which makes
        # the problem quasistatic, has a measurable effect on the
        # results.  Lots of time was wasted by testing with a problem
        # that was remarkably insenstive to the presence or absence of
        # the heat capacity.
        self.heatConductivity(test_no, source_no)
        OOF.Material.Remove_property(
            name='material',
            property='Thermal:HeatCapacity:ConstantHeatCapacity:cap')
        solver()
        soln_data = exact_solns.exact_solns["scalar"][soln_no]
        self.setBoundaryConditions('Dirichlet', Temperature, Heat_Eqn,
                                   soln_data["DirichletBC"])
        self.uniform(stepper, timestep=time/nsteps)
        self.initializeScalarFields(Temperature, soln_data["Solution"])
        self.setOutput()
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=time)
        self.check(time, soln_data["Solution"], tolerance, expected=False)

    def comboTest(self, stepper1, solver1, stepper2, solver2,
                  time, nsteps, tolerance,
                  test_no, source_no, soln_no):
        # Solve two uniform stepping problems on the same mesh.  This
        # checks that everything is reset properly after the first
        # solution.
        soln_data = exact_solns.exact_solns["scalar"][soln_no]
        self.heatConductivity(test_no, source_no)
        self.setBoundaryConditions('Dirichlet', Temperature, Heat_Eqn,
                                   soln_data["DirichletBC"])

        solver1()
        self.uniform(stepper1, timestep=time/nsteps)
        self.initializeScalarFields(Temperature, soln_data["Solution"])
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=time)
        self.check(time, soln_data["Solution"], tolerance)

        solver2()
        self.uniform(stepper2, timestep=time/nsteps)
        self.initializeScalarFields(Temperature, soln_data["Solution"])
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=time)
        self.check(time, soln_data["Solution"], tolerance)

    def adaptiveTest(self, stepper, solver, time,
                     steptol, tolerance,
                     test_no, source_no, soln_no, 
                     initialstep=0.01):
        self.heatConductivity(test_no, source_no)
        solver()
        soln_data = exact_solns.exact_solns["scalar"][soln_no]
        self.setBoundaryConditions('Dirichlet', Temperature, Heat_Eqn,
                                   soln_data["DirichletBC"])
        self.adaptive(stepper, initialstep, steptol)
        self.initializeScalarFields(Temperature, soln_data["Solution"])
        self.setOutput(interval=0.02)
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=time)
        self.check(time, soln_data["Solution"], tolerance)

    def adaptiveTest2(self, stepper, solver, time,
                     steptol, tolerance,
                     test_no, source_no, soln_no, 
                     initialstep=0.01):
        self.heatConductivity(test_no, source_no)
        solver()
        soln_data = exact_solns.exact_solns["scalar"][soln_no]
        self.setBoundaryConditions('Dirichlet', Temperature, Heat_Eqn,
                                   soln_data["DirichletBC"])
        self.adaptive(stepper, initialstep, steptol)
        self.initializeScalarFields(Temperature, soln_data["Solution"])
        self.setOutput(interval=0.02)
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=time)
        self.check(time, soln_data["Solution"], tolerance)
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=2*time)
        self.check(2*time, soln_data["Solution"], tolerance)

    @memorycheck.check("microstructure")
    def unif189BEnewton(self):
        self.uniformTest(
            BackwardEuler(), self.newton,
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def unif189BEnewtonQS(self):
        # Quasistatic version of the above.  The comparison is still
        # to the nonstatic solution.  If the comparison *doesn't*
        # fail, then the rest of the tests can't be trusted.
        self.uniformTestQS(
            BackwardEuler(), self.newton,
            time=0.1, nsteps=10, 
            tolerance=0.1,      # L2 error must be *greater* than this.
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def unif189CNnewton(self):
        self.uniformTest(
            CrankNicolson(), self.newton, 
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def unif189CNnewton2(self):
        self.uniformTest2(
            CrankNicolson(), self.newton, 
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def unif189SSnewton(self):
        self.uniformTest(
            SS22(theta1=0.5,theta2=0.5), self.newton,
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def unif189BEpicard(self):
        self.uniformTest(
            BackwardEuler(), self.picard,
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def unif189CNpicard(self):
        self.uniformTest(
            CrankNicolson(), self.picard, 
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def unif189SSpicard(self):
        self.uniformTest(
            SS22(theta1=0.5,theta2=0.5), self.picard,
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def unif189FEnewton(self):
        self.uniformTest(
            ForwardEuler(), self.newton,
            time=0.1, nsteps=100, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def unif189FElinear(self):
        # Check that using a linear solver is legal for a nonlinear
        # problem if the stepper is explicit.  The answer isn't going
        # to be very good, though.
        self.uniformTest(
            ForwardEuler(), self.linear,
            time=0.1, nsteps=100, tolerance=1.e-3,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def combo189SSpicardSSpicard(self):
        self.comboTest(
            SS22(theta1=0.5, theta2=0.5), self.picard,
            SS22(theta1=0.5, theta2=0.5), self.picard,
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)
            
    @memorycheck.check("microstructure")
    def combo189SSpicardSSnewton(self):
        self.comboTest(
            SS22(theta1=0.5, theta2=0.5), self.picard,
            SS22(theta1=0.5, theta2=0.5), self.newton,
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)
            
    @memorycheck.check("microstructure")
    def combo189SSnewtonSSnewton(self):
        self.comboTest(
            SS22(theta1=0.5, theta2=0.5), self.newton,
            SS22(theta1=0.5, theta2=0.5), self.newton,
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)
            
    @memorycheck.check("microstructure")
    def combo189CNpicardCNpicard(self):
        self.comboTest(
            CrankNicolson(), self.picard,
            CrankNicolson(), self.picard,
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def combo189CNnewtonCNnewton(self):
        self.comboTest(
            CrankNicolson(), self.newton,
            CrankNicolson(), self.newton,
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def combo189CNnewtonSSnewton(self):
        self.comboTest(
            CrankNicolson(), self.newton,
            SS22(theta1=0.5, theta2=0.5), self.newton,
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)
            
    @memorycheck.check("microstructure")
    def combo189SSnewtonCNnewton(self):
        self.comboTest(
            SS22(theta1=0.5, theta2=0.5), self.newton,
            CrankNicolson(), self.newton,
            time=0.1, nsteps=10, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)
            
    @memorycheck.check("microstructure")
    def adapt189BEnewton(self):
        self.adaptiveTest(
            BackwardEuler(), self.newton,
            time=0.1, steptol=1.e-5, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def adapt189CNnewton(self):
        self.adaptiveTest(
            CrankNicolson(), self.newton, 
            time=0.1, steptol=1.e-5, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def adapt189SSnewton(self):
        self.adaptiveTest(
            SS22(theta1=0.5,theta2=0.5), self.newton,
            time=0.1, steptol=1.e-5, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def adapt189SSnewton2(self):
        self.adaptiveTest2(
            SS22(theta1=0.5,theta2=0.5), self.newton,
            time=0.1, steptol=1.e-5, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def adapt189BEpicard(self):
        self.adaptiveTest(
            BackwardEuler(), self.picard,
            time=0.1, steptol=1.e-5, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def adapt189CNpicard(self):
        self.adaptiveTest(
            CrankNicolson(), self.picard, 
            time=0.1, steptol=1.e-5, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)

    @memorycheck.check("microstructure")
    def adapt189SSpicard(self):
        self.adaptiveTest(
            SS22(theta1=0.5,theta2=0.5), self.picard,
            time=0.1, steptol=1.e-5, tolerance=1.e-4,
            test_no=1, source_no=8, soln_no=9)


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Routine to do regression-type testing on the items in this file.
# Tests will be run in the order they appear in the list.  This
# routine will stop after the first failure.

def run_tests():
    test_set = [
        NonlinearTimedependentTest("unif189BEnewton"),
        NonlinearTimedependentTest("unif189BEnewtonQS"),
        NonlinearTimedependentTest("unif189BEpicard"),
        NonlinearTimedependentTest("unif189CNnewton"),
        NonlinearTimedependentTest("unif189CNnewton2"),
        NonlinearTimedependentTest("unif189CNpicard"),
        NonlinearTimedependentTest("unif189SSnewton"),
        NonlinearTimedependentTest("unif189SSpicard"),

        NonlinearTimedependentTest("unif189FEnewton"),
        NonlinearTimedependentTest("unif189FElinear"),

        NonlinearTimedependentTest("combo189SSpicardSSpicard"),
        NonlinearTimedependentTest("combo189SSpicardSSnewton"),
        NonlinearTimedependentTest("combo189SSnewtonSSnewton"),
        NonlinearTimedependentTest("combo189CNpicardCNpicard"),
        NonlinearTimedependentTest("combo189CNnewtonCNnewton"),
        NonlinearTimedependentTest("combo189CNnewtonSSnewton"),
        NonlinearTimedependentTest("combo189SSnewtonCNnewton"),

        NonlinearTimedependentTest("adapt189BEnewton"),
        NonlinearTimedependentTest("adapt189CNnewton"),
        NonlinearTimedependentTest("adapt189BEpicard"),
        NonlinearTimedependentTest("adapt189CNpicard"),
        NonlinearTimedependentTest("adapt189SSpicard"),
        NonlinearTimedependentTest("adapt189SSnewton"),
        NonlinearTimedependentTest("adapt189SSnewton2"),
        ]

    # test_set = [
    #     NonlinearTimedependentTest("unif189FEnewton"),
    #     NonlinearTimedependentTest("unif189FElinear")
    #     ]
    # test_set = [NonlinearTimedependentTest("adapt189CNnewton")]
        

    logan = unittest.TextTestRunner()
    for t in test_set:
        print >> sys.stderr,  "\n *** Running test: %s\n" % t.id()
        res = logan.run(t)
        if not res.wasSuccessful():
            return 0
    return 1


###################################################################
# The code below this line should be common to all testing files. #
###################################################################

if __name__=="__main__":
    # If directly run, then start oof, and run the local tests, then quit.
    import sys
    try:
        import oof2
        sys.path.append(os.path.dirname(oof2.__file__))
        from ooflib.common import oof
        from math import *
    except ImportError:
        print "OOF is not correctly installed on this system."
        sys.exit(4)
    sys.argv.append("--text")
    sys.argv.append("--quiet")
    sys.argv.append("--seed=17")
    oof.run(no_interp=1)

    success = run_tests()

    OOF.File.Quit()

    if success:
        print "All tests passed."
    else:
        print "Test failure."

