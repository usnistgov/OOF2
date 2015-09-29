# -*- python -*-
# $RCSfile: nonlinear_floatbc_test.py,v $
# $Revision: 1.13 $
# $Author: langer $
# $Date: 2011/06/09 13:36:37 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import os
import unittest

import memorycheck
from UTILS import file_utils
#file_utils.generate = True

# A trivial linear thermal diffusion problem, with T=1 fixed on the
# left edge, initialized to T=0 in the interior.  Check that the
# solution is the same whether or not there's a floating boundary
# condition on the right edge.

class OOF_SimpleFloat(unittest.TestCase):
    def setUp(self):
        OOF.Microstructure.New(
            name='microstructure',
            width=1.0, height=1.0,
            width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(
            name='material', material_type='bulk')
        OOF.Material.Assign(
            material='material',
            microstructure='microstructure',
            pixels=all)
        OOF.Material.Add_property(
            name='material',
            property='Thermal:Conductivity:Isotropic')
        OOF.Material.Add_property(
            name='material',
            property='Thermal:HeatCapacity:ConstantHeatCapacity')
        OOF.Skeleton.New(
            name='skeleton', microstructure='microstructure',
            x_elements=4, y_elements=4,
            skeleton_geometry=QuadSkeleton(
                left_right_periodicity=False,top_bottom_periodicity=False))
        OOF.Mesh.New(
            name='mesh', skeleton='microstructure:skeleton',
            element_types=['D2_2', 'T3_3', 'Q4_4'])
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', field=Temperature)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Heat_Eqn)
        OOF.Mesh.Boundary_Conditions.New(
            name='bc',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=1),
                boundary='left'))

        # Measure the average temperature on the right edge, which
        # will sometimes be the location of a floating BC.
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name=AutomaticName('GraphicsUpdate'),
            output=GraphicsUpdate())
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('GraphicsUpdate'),
            scheduletype=AbsoluteOutputSchedule(), 
            schedule=Periodic(delay=0.0,interval=0.1))
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='right.out', output=GraphicsUpdate())
        OOF.Mesh.Scheduled_Output.Edit(
            mesh='microstructure:skeleton:mesh', 
            output='right.out', 
            new_output=BoundaryAnalysis(
                operation=AverageField(field=Temperature),
                boundary='right'))
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output='right.out', 
            scheduletype=AbsoluteOutputSchedule(),
            schedule=Periodic(delay=0.0,interval=0.1))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh',
            output='right.out',
            destination=OutputStream(filename='right.out',mode='w'))

        # Select segments through the middle of the Skeleton,
        # construct a Boundary on those segments, and measure the
        # average temperature on it, in order to have a check that's
        # *not* on the floating BC.
        OOF.Windows.Graphics.New()
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='microstructure:skeleton',
            points=[Point(0.536026,0.829039)], shift=0, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='microstructure:skeleton',
            points=[Point(0.507205,0.675328)], shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='microstructure:skeleton',
            points=[Point(0.526419,0.382314)], shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='microstructure:skeleton', 
            points=[Point(0.516812,0.118122)], shift=1, ctrl=0)
        OOF.Skeleton.Boundary.Construct(
            skeleton='microstructure:skeleton',
            name='50 yard line',
            constructor=EdgeFromSegments(
                group=selection,
                direction='Bottom to top'))
        OOF.Mesh.Modify(
            mesh='microstructure:skeleton:mesh',
            modifier=RebuildMesh())

        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='middle.out',
            output=BoundaryAnalysis(
                operation=AverageField(field=Temperature),
                boundary='50 yard line'))
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output='middle.out', 
            scheduletype=AbsoluteOutputSchedule(), 
            schedule=Periodic(delay=0.0,interval=0.1))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh', 
            output='middle.out', 
            destination=OutputStream(filename='middle.out',mode='w'))

        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='centerpoint.out',
            output=BulkAnalysis(
                output_type='Scalar',
                data=getOutput(
                    'Field:Component',component='',field=Temperature),
                operation=DirectOutput(),
                domain=SinglePoint(point=Point(0.5,0.5)),
                sampling=DiscretePointSampleSet(show_x=False,show_y=False)))
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh', 
            output='centerpoint.out',
            scheduletype=AbsoluteOutputSchedule(),
            schedule=Periodic(delay=0.0,interval=0.1))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh', 
            output='centerpoint.out',
            destination=OutputStream(filename='center.out',mode='w'))

        # # Output the full mesh, for debugging.
        # OOF.Mesh.Scheduled_Output.New(
        #     mesh='microstructure:skeleton:mesh',
        #     name='mesh', output=MeshFileOutput())
        # OOF.Mesh.Scheduled_Output.Schedule.Set(
        #     mesh='microstructure:skeleton:mesh',
        #     output='mesh',
        #     scheduletype=AbsoluteOutputSchedule(),
        #     schedule=Periodic(delay=0.0,interval=0.1))
        # OOF.Mesh.Scheduled_Output.Destination.Set(
        #     mesh='microstructure:skeleton:mesh', 
        #     output='mesh',
        #     destination=DataFileOutput(
        #         filename='temptop.mesh',mode='w',format='ascii'))

        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh', 
            field=Temperature, 
            initializer=ConstScalarFieldInit(value=0.0))
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh', time=0.0)

    def check(self, tolerance):
        self.assert_(file_utils.fp_file_compare(
                'center.out',
                os.path.join('mesh_data', 'simplecenter.out'),
                tolerance))
        file_utils.remove('center.out')

        self.assert_(file_utils.fp_file_compare(
                'middle.out',
                os.path.join('mesh_data', 'simplemiddle.out'),
                tolerance))
        file_utils.remove('middle.out')
                             
        self.assert_(file_utils.fp_file_compare(
                'right.out',
                os.path.join('mesh_data', 'simpleright.out'),
                tolerance))
        file_utils.remove('right.out')

    def tearDown(self):
        from ooflib.engine.IO import outputdestination
        outputdestination.forgetTextOutputStreams()
        OOF.Material.Delete(name='material')
        OOF.Graphics_1.File.Close()

    def linearSolver(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=1.e-05,
                    minstep=1.e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=CrankNicolson())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))

    def nonlinearSolver(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=1.e-05,
                    minstep=1.e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=CrankNicolson())),
                nonlinear_solver=Newton(
                    relative_tolerance=1.e-08,
                    absolute_tolerance=1.e-13,
                    maximum_iterations=200),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))

    def nonlinearUniformSolver(self, stepsize):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=UniformDriver(
                    stepsize=stepsize,
                    stepper=CrankNicolson()),
                nonlinear_solver=Newton(
                    relative_tolerance=1.e-08,
                    absolute_tolerance=1.e-13,
                    maximum_iterations=200),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))

    def floatBC(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<2>', 
            mesh='microstructure:skeleton:mesh', 
            condition=FloatBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=0.0),boundary='right'))
        OOF.Mesh.Boundary_Conditions.Set_BC_Initializer(
            mesh='microstructure:skeleton:mesh',
            bc='bc<2>',
            initializer=FloatBCInitMin(value=0.0))

    def solve(self):
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh',
                       endtime=3.0)

    # The reference calculation uses a linear solver and a free BC on
    # the right side.
    @memorycheck.check("microstructure")
    def LinearFree(self):
        self.linearSolver()
        self.solve()
        self.check(1.e-6)
    
    # Sanity-check calculation, still linear, but with a FloatBC on
    # the right.
    @memorycheck.check("microstructure")
    def LinearFloat(self):
        self.linearSolver()
        self.floatBC()
        self.solve()
        self.check(1.e-6)

    # Now check the nonlinear solver with the free BC.
    @memorycheck.check("microstructure")
    def NonlinearFree(self):
        self.nonlinearSolver()
        self.solve()
        self.check(1.e-6)

    # And again with the floating BC.
    @memorycheck.check("microstructure")
    def NonlinearFloat(self):
        self.nonlinearSolver()
        self.floatBC()
        self.solve()
        self.check(1.e-6)

    # And again with the floating BC, with a uniform stepper
    @memorycheck.check("microstructure")
    def NonlinearUniformFloat(self):
        self.nonlinearUniformSolver(stepsize=0.01)
        self.floatBC()
        self.solve()
        self.check(1.e-3)


# A time-dependent linear diffusion problem that includes a floating
# boundary condition, solved in a variety of ways, all of which should
# give the same answer.  The material has isotropic thermal
# conductivity so there should be no difference in the solution of the
# in-plane field and out-of-plane flux cases.

class OOF_FloatBC1(unittest.TestCase):
    def setUp(self):
        OOF.Microstructure.New(
            name='microstructure',
            width=1.0, height=1.0, width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(
            name='material', material_type='bulk')
        OOF.Material.Assign(
            material='material', microstructure='microstructure', pixels=all)
        OOF.Material.Add_property(
            name='material', property='Thermal:Conductivity:Isotropic')
        OOF.Material.Add_property(
            name='material', 
            property='Thermal:HeatCapacity:ConstantHeatCapacity')
        OOF.Skeleton.New(
            name='skeleton', 
            microstructure='microstructure',
            x_elements=4, y_elements=4,
            skeleton_geometry=QuadSkeleton(
                left_right_periodicity=False,top_bottom_periodicity=False))
        OOF.Mesh.New(
            name='mesh', skeleton='microstructure:skeleton',
            element_types=['D2_2', 'T3_3', 'Q4_4'])
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default', 
            field=Temperature)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Heat_Eqn)
        OOF.Mesh.Boundary_Conditions.New(
            name='bc', 
            mesh='microstructure:skeleton:mesh', 
            condition=FloatBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=0.0),
                boundary='top'))
        OOF.Mesh.Boundary_Conditions.Set_BC_Initializer(
            mesh='microstructure:skeleton:mesh',
            bc='bc',
            initializer=FloatBCInitMin(value=0.0))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<2>', 
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=1),
                boundary='bottomleft'))
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name=AutomaticName('Average Temperature on top'),
            output=BoundaryAnalysis(
                operation=AverageField(field=Temperature),
                boundary='top'))
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('Average Temperature on top'),
            scheduletype=AbsoluteOutputSchedule(),
            schedule=Periodic(delay=0.0,interval=0.1))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('Average Temperature on top'),
            destination=OutputStream(filename='temptop.out',mode='w'))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Temperature, 
            initializer=ConstScalarFieldInit(value=0.0))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh', 
            field=Temperature_z, 
            initializer=ConstScalarFieldInit(value=0.0))

    def solve(self):
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh', time=0.0)
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh', endtime=4.0)

    def check(self, tolerance):
        self.assert_(file_utils.fp_file_compare(
                'temptop.out',
                os.path.join('mesh_data', 'temptop.out'),
                tolerance))
        file_utils.remove('temptop.out')

    @memorycheck.check("microstructure")
    def LinearCNinPlane(self):
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh',
            field=Temperature)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default', 
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    tolerance=1.e-06,
                    initialstep=0,
                    minstep=1.e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=CrankNicolson())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,max_iterations=1000)))
        self.solve()
        self.check(1.e-6)

    @memorycheck.check("microstructure")
    def LinearCNOutOfPlane(self):
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Heat_Flux)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default', 
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    tolerance=1.e-06,
                    initialstep=0,
                    minstep=1.e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=CrankNicolson())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,max_iterations=1000)))
        self.solve()
        self.check(1.e-6)

    @memorycheck.check("microstructure")
    def NewtonCNinPlane(self):
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh',
            field=Temperature)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default', 
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    tolerance=1.e-06,
                    initialstep=0,
                    minstep=1.e-06,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=CrankNicolson())),
                nonlinear_solver=Newton(
                    relative_tolerance=1.e-08,
                    absolute_tolerance=1.e-13,
                    maximum_iterations=200),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,max_iterations=1000)))
        self.solve()
        self.check(1.e-6)

    @memorycheck.check("microstructure")
    def NewtonCNOutOfPlane(self):
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Heat_Flux)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default', 
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    tolerance=1.e-06,
                    initialstep=0,
                    minstep=1.e-06,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=CrankNicolson())),
                nonlinear_solver=Newton(
                    relative_tolerance=1.e-08,
                    absolute_tolerance=1.e-13,
                    maximum_iterations=200),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,max_iterations=1000)))
        self.solve()
        self.check(1.e-6)


    def tearDown(self):
        from ooflib.engine.IO import outputdestination
        outputdestination.forgetTextOutputStreams()
        OOF.Material.Delete(name='material')

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Routine to do regression-type testing on the items in this file.
# Tests will be run in the order they appear in the list.  This
# routine will stop after the first failure.

def run_tests():
    test_set = [
        OOF_SimpleFloat("LinearFree"),
        OOF_SimpleFloat("LinearFloat"),
        OOF_SimpleFloat("NonlinearFree"),
        OOF_SimpleFloat("NonlinearFloat"),
        OOF_SimpleFloat("NonlinearUniformFloat"),

        OOF_FloatBC1("LinearCNinPlane"),
        OOF_FloatBC1("LinearCNOutOfPlane"),
        OOF_FloatBC1("NewtonCNinPlane"),
        OOF_FloatBC1("NewtonCNOutOfPlane")
        ]

    # test_set = [
    #     OOF_SimpleFloat("LinearFloat")
    #     ]

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

