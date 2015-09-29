# -*- python -*-
# $RCSfile: nonlinear_timedependent_tests.py,v $
# $Revision: 1.9 $
# $Author: langer $
# $Date: 2011/01/07 20:54:46 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import unittest, os
import memorycheck
from math import *
from exact_solns import *

class NonlinearTimedependentTest(unittest.TestCase):
    def tearDown(self):
        OOF.Material.Delete(name="material")

    def setUp(self):

        self.numX = 32
        self.numY = 32
        self.time = 0.1
        self.timestep = 0.01

        self.time_steppers = [
            # ForwardEuler(),
            BackwardEuler(),
            CrankNicolson(),
            SS22(theta1=0.5,theta2=0.5)
            ]

        OOF.Microstructure.New(
            name='microstructure',
            width=1.0, height=1.0, width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(
            name='material', material_type='bulk')
        OOF.Skeleton.New(
            name='skeleton', microstructure='microstructure',
            x_elements=self.numX, y_elements=self.numY,
            skeleton_geometry=QuadSkeleton(
                left_right_periodicity=False,top_bottom_periodicity=False))
        OOF.Mesh.New(
            name='mesh',
            skeleton='microstructure:skeleton',
            element_types=['D2_2', 'T3_3', 'Q4_4'])

        self.heat_solns = exact_solns["scalar"]
        self.elasticity_solns = exact_solns["vector2D"]

        self.boundary_condition_count = 0


    def setBoundaryConditions(self,BC_type,BC_field,BC_equation,BC_list):

        BC_no = 0
        for BC in BC_list:

            BC_no = BC_no + 1

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
                name = 'bc<' + str(BC_no) + '>',
                mesh = 'microstructure:skeleton:mesh',
                condition = new_BC )

        self.boundary_condition_count = BC_no


    def removeBoundaryConditions(self):

        for bc_no in range(1, self.boundary_condition_count+1):
             OOF.Mesh.Boundary_Conditions.Delete(
                 mesh='microstructure:skeleton:mesh',
                 name='bc<' + str(bc_no) + '>')

        self.boundary_condition_count = 0


    @memorycheck.check("microstructure")
    def NonlinearHeatSource(self):

        nonlin_heat_source_tests = [ {"test_no":2,"soln_no":3},
                                     {"test_no":4,"soln_no":4},
                                     {"test_no":5,"soln_no":5} ]


        # define the heat equation related quantities needed for this test
        OOF.Property.Parametrize.Thermal.Conductivity.Isotropic(
            kappa=1.0)
        OOF.Material.Add_property(
            name='material',
            property='Thermal:Conductivity:Isotropic')
        OOF.Property.Parametrize.Thermal.HeatCapacity.ConstantHeatCapacity(
            cv=1.0)
        OOF.Material.Add_property(
            name='material',
            property='Thermal:HeatCapacity:ConstantHeatCapacity')
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

        # iterate through nonlinear heat source test by alternating
        # between various test examples and nonlinear solvers
        for test in nonlin_heat_source_tests:

            test_no = test["test_no"]
            soln_no = test["soln_no"]

            # add the nonlinear heat source property to the material
            OOF.Property.Parametrize.Thermal.HeatSource.TestNonlinearHeatSource(
                testno=test_no)
            OOF.Material.Add_property(
                name='material',
                property='Thermal:HeatSource:TestNonlinearHeatSource')
            OOF.Material.Assign(
                material='material', microstructure='microstructure',
                pixels=all)

            # set the boundary conditions for the given test no
            self.setBoundaryConditions('Dirichlet', Temperature, Heat_Eqn,
                                       self.heat_solns[soln_no]["DirichletBC"] )

            for test_stepper in self.time_steppers:

                # compute the solution using Picard iterations
                test_solver = Picard(
                    relative_tolerance=1e-08,
                    absolute_tolerance=1.0e-13,
                    maximum_iterations=20)

                self.heatEqnEngine( test_no, soln_no, test_solver, 
                                    test_stepper )

                # compute the solution using Newton's method
                test_solver = Newton(
                    relative_tolerance=1e-08,
                    absolute_tolerance=1.0e-13,
                    maximum_iterations=20)

                self.heatEqnEngine( test_no, soln_no, test_solver,
                                    test_stepper )

            # remove the boundary conditions for the given test no
            self.removeBoundaryConditions()

            # remove the current version of the nonlinear heat source property
            OOF.Material.Remove_property(
                name='material',
                property='Thermal:HeatSource:TestNonlinearHeatSource')

        # delete the other properties, fields, equations needed for this test
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Heat_Eqn)
        OOF.Subproblem.Field.Undefine(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Material.Remove_property(
            name='material',
            property='Thermal:Conductivity:Isotropic')
        OOF.Material.Remove_property(
            name='material',
            property='Thermal:HeatCapacity:ConstantHeatCapacity')


    def heatEqnEngine(self,test_no,soln_no,test_solver,test_stepper):

        soln_func = self.heat_solns[soln_no]["Solution"]
        init_func = self.heat_solns[soln_no]["InitialValue"]

        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
               time_stepper=UniformDriver(
                    stepsize=self.timestep,
                    stepper=test_stepper),
               nonlinear_solver=test_solver,
               symmetric_solver=ConjugateGradient(
                   preconditioner=ILUPreconditioner(),
                   tolerance=1e-13,
                   max_iterations=1000),
               asymmetric_solver=BiConjugateGradient(
                   preconditioner=ILUPreconditioner(),
                   tolerance=1e-13,
                   max_iterations=1000)))

        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Temperature,
            initializer=FuncScalarFieldInit(
                function=init_func))
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh',
            time=0.0)

        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=self.time)

        from ooflib.engine import mesh
        from ooflib.SWIG.engine import field

        mesh_obj  = mesh.meshes["microstructure:skeleton:mesh"].getObject()
        field_ptr = field.getField( "Temperature" )

        L2_error = computeScalarErrorL2( soln_func, mesh_obj, field_ptr,
                                         self.numX, self.numY, time=self.time )
        print "L2 error: ", L2_error

        self.assert_( L2_error < 1.e-1 )


    @memorycheck.check("microstructure")
    def NonlinearForceDensity(self):

        nonlin_force_density_tests = [ {"test_no":2,"soln_no":1},
                                       {"test_no":4,"soln_no":4} 
                                       ]

        # define the force density related quantities needed for this test
        OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic(
            cijkl=IsotropicRank4TensorLame(lmbda=-1,mu=1))
        OOF.Material.Add_property(
            name='material',
            property='Mechanical:Elasticity:Isotropic')
        OOF.Property.Parametrize.Mechanical.MassDensity.ConstantMassDensity(
            rho=1.0)
        OOF.Material.Add_property(
            name='material',
            property='Mechanical:MassDensity:ConstantMassDensity')
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh',
            field=Displacement)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Force_Balance)

        # iterate through nonlinear force density test by alternating
        # between various test examples and nonlinear solvers
        for test in nonlin_force_density_tests:

            test_no = test["test_no"]
            soln_no = test["soln_no"]

            # add the nonlinear force density property to the material
            OOF.Property.Parametrize.Mechanical.ForceDensity.TestNonlinearForceDensity(
                testno=test_no)
            OOF.Material.Add_property(
                name='material',
                property='Mechanical:ForceDensity:TestNonlinearForceDensity')
            OOF.Material.Assign(
                material='material', microstructure='microstructure',
                pixels=all)

            # set the boundary conditions for the given test no
            self.setBoundaryConditions( 
                'Dirichlet', Displacement, Force_Balance,
                self.elasticity_solns[soln_no]["DirichletBC"] )

            for test_stepper in self.time_steppers:

                # compute the solution using Picard iterations
                test_solver = Picard(
                    relative_tolerance=1e-08,
                    absolute_tolerance=1.0e-13,
                    maximum_iterations=20)

                self.elasticityEqnEngine( test_no, soln_no, test_solver,
                                          test_stepper )

                # compute the solution using Newton's method
                test_solver = Newton(
                    relative_tolerance=1e-08,
                    absolute_tolerance=1.0e-13,
                    maximum_iterations=20)

                self.elasticityEqnEngine( test_no, soln_no, test_solver,
                                          test_stepper )

            # remove the boundary conditions for the given test no
            self.removeBoundaryConditions()

            # remove the current version of the nonlinear force density property
            OOF.Material.Remove_property(
                name='material',
                property='Mechanical:ForceDensity:TestNonlinearForceDensity')

        # delete the other properties, fields, equations needed for this test
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Force_Balance)
        OOF.Subproblem.Field.Undefine(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Material.Remove_property(
            name='material',
            property='Mechanical:Elasticity:Isotropic')
        OOF.Material.Remove_property(
            name='material',
            property='Mechanical:MassDensity:ConstantMassDensity')


    def elasticityEqnEngine(self,test_no,soln_no,test_solver,test_stepper):

        soln_func = self.elasticity_solns[soln_no]["Solution"]
        init_func = self.elasticity_solns[soln_no]["InitialValue"]
        init_deriv_func = self.elasticity_solns[soln_no]["InitialTimeDeriv"]

        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
               time_stepper=UniformDriver(
                    stepsize=self.timestep,
                    stepper = test_stepper ),
               nonlinear_solver = test_solver,
               symmetric_solver=ConjugateGradient(
                   preconditioner=ILUPreconditioner(),
                   tolerance=1e-13,
                   max_iterations=1000),
               asymmetric_solver=BiConjugateGradient(
                   preconditioner=ILUPreconditioner(),
                   tolerance=1e-13,
                   max_iterations=1000)))

        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Displacement,
            initializer=FuncTwoVectorFieldInit(
                fx = init_func[0],
                fy = init_func[1] ))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Displacement_t,
            initializer=FuncTwoVectorFieldInit(
                fx = init_deriv_func[0],
                fy = init_deriv_func[1] ))
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh',
            time=0.0)

        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=self.time)

        from ooflib.engine import mesh
        from ooflib.SWIG.engine import field

        mesh_obj  = mesh.meshes["microstructure:skeleton:mesh"].getObject()
        field_ptr = field.getField( "Displacement" )

        L2_error = computeVector2DErrorL2( soln_func, mesh_obj, field_ptr,
                                           self.numX, self.numY, time=self.time)
        print "L2 error: ", L2_error

        self.assert_( L2_error < 1.e-1 )


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Routine to do regression-type testing on the items in this file.
# Tests will be run in the order they appear in the list.  This
# routine will stop after the first failure.

def run_tests():
    property_set = [
        NonlinearTimedependentTest("NonlinearHeatSource"),
        NonlinearTimedependentTest("NonlinearForceDensity"),
        ]

    test_set = property_set

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

