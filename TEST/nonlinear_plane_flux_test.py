# -*- python -*-
# $RCSfile: nonlinear_plane_flux_test.py,v $
# $Revision: 1.6 $
# $Author: langer $
# $Date: 2011/05/26 15:56:56 $

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
from UTILS import file_utils
from exact_solns import *


class NonlinearPlaneFluxTest(unittest.TestCase):
    def tearDown(self):
        OOF.Material.Delete(name="material")

    def setUp(self):
        global outputdestination
        from ooflib.engine.IO import outputdestination

        self.numX = 32
        self.numY = 32
        self.time = 0.0

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
        self.elasticity_z_solns = exact_solns["vector3D"]

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
    def LinearHeatConductivity(self):

        test_coefficients = [ TriclinicRank2Tensor(xx=1.0,yy=1.0,zz=1.0,
                                                   yz=0.5,xz=0.5,xy=0.0) ]
        const_test_sources = [ -3.0 ]

        linear_heat_conductivity_tests = [ {"test_no":0,"heat_source_no":0,
                                            "soln_no":1,"z_soln_no":6} ]

        # define the heat equation related quantities needed for this test
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Heat_Eqn)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Heat_Flux)

        # iterate through nonlinear heat conductivity test by alternating
        # between various test examples and nonlinear solvers
        for test in linear_heat_conductivity_tests:

            test_no   = test["test_no"]
            source_no = test["heat_source_no"]
            soln_no   = test["soln_no"]
            z_soln_no = test["z_soln_no"]

            # add the nonlinear heat conductivity property to the material
            OOF.Property.Parametrize.Thermal.Conductivity.Anisotropic.Triclinic(
                kappa=test_coefficients[test_no])
            OOF.Material.Add_property(
                name='material',
                property='Thermal:Conductivity:Anisotropic:Triclinic')
            # add the constant heat source property to the material
            OOF.Property.Parametrize.Thermal.HeatSource.ConstantHeatSource(
                rate=const_test_sources[source_no])
            OOF.Material.Add_property(
                name='material',
                property='Thermal:HeatSource:ConstantHeatSource')
            OOF.Property.Parametrize.Orientation(
                angles=Abg(alpha=0,beta=0,gamma=0))
            OOF.Material.Add_property(
                name='material',
                property='Orientation')
            OOF.Material.Assign(
                material='material', microstructure='microstructure', pixels=all)

            # set the boundary conditions for the given test no
            self.setBoundaryConditions( 'Dirichlet', Temperature, Heat_Eqn,
                                        self.heat_solns[soln_no]["DirichletBC"] )

            # compute the solution using Newton's method
            test_solver = Newton(
                relative_tolerance=1e-08,
                absolute_tolerance=1e-13,
                maximum_iterations=20)

            self.heatEqnEngine( soln_no, z_soln_no, test_solver )

            # remove the boundary conditions for the given test no
            self.removeBoundaryConditions()

            # remove the nonlin heat conductivity and nonconst heat source properties
            OOF.Material.Remove_property(
                name='material',
                property='Thermal:Conductivity:Anisotropic:Triclinic')
            OOF.Material.Remove_property(
                name='material',
                property='Thermal:HeatSource:ConstantHeatSource')
            OOF.Material.Remove_property(
                name='material',
                property='Orientation')

        # delete the other properties, fields, equations needed for this test
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Heat_Flux)
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Heat_Eqn)
        OOF.Subproblem.Field.Undefine(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)


    @memorycheck.check("microstructure")
    def NonlinearHeatConductivity(self):

        nonlin_heat_conductivity_tests = [ {"test_no":2,"heat_source_no":4,
                                            "soln_no":0,"z_soln_no":7} ]

        # define the heat equation related quantities needed for this test
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Heat_Eqn)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Heat_Flux)

        # iterate through nonlinear heat conductivity test by alternating
        # between various test examples and nonlinear solvers
        for test in nonlin_heat_conductivity_tests:

            test_no   = test["test_no"]
            source_no = test["heat_source_no"]
            soln_no   = test["soln_no"]
            z_soln_no = test["z_soln_no"]

            # add the nonlinear heat conductivity property to the material
            OOF.Property.Parametrize.Thermal.Conductivity.TestNonlinearHeatConductivity(
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
            OOF.Material.Assign(
                material='material', microstructure='microstructure', pixels=all)

            # set the boundary conditions for the given test no
            self.setBoundaryConditions( 'Dirichlet', Temperature, Heat_Eqn,
                                        self.heat_solns[soln_no]["DirichletBC"] )

            # compute the solution using Newton's method
            test_solver = Newton(
                relative_tolerance=1e-08,
                absolute_tolerance=1e-13,
                maximum_iterations=20)

            self.heatEqnEngine( soln_no, z_soln_no, test_solver )

            # remove the boundary conditions for the given test no
            self.removeBoundaryConditions()

            # remove the nonlin heat conductivity and nonconst heat source properties
            OOF.Material.Remove_property(
                name='material',
                property='Thermal:Conductivity:TestNonlinearHeatConductivity')
            OOF.Material.Remove_property(
                name='material',
                property='Thermal:HeatSource:TestNonconstantHeatSource')
            OOF.Material.Remove_property(
                name='material',
                property='Orientation')

        # delete the other properties, fields, equations needed for this test
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Heat_Flux)
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Heat_Eqn)
        OOF.Subproblem.Field.Undefine(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)


    @memorycheck.check("microstructure")
    def NonlinearHeatConductivityNoDeriv(self):

        nonlin_heat_conductivity_tests = [ {"test_no":2,"heat_source_no":4,
                                            "soln_no":0,"z_soln_no":7} ]

        # define the heat equation related quantities needed for this test
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Heat_Eqn)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Heat_Flux)

        # iterate through nonlinear heat conductivity test by alternating
        # between various test examples and nonlinear solvers
        for test in nonlin_heat_conductivity_tests:

            test_no   = test["test_no"]
            source_no = test["heat_source_no"]
            soln_no   = test["soln_no"]
            z_soln_no = test["z_soln_no"]

            # add the nonlinear heat conductivity property to the material
            OOF.Property.Parametrize.Thermal.Conductivity.TestNonlinearHeatConductivityNoDeriv(
                testno=test_no)
            OOF.Material.Add_property(
                name='material',
                property='Thermal:Conductivity:TestNonlinearHeatConductivityNoDeriv')
            # add the nonconstant heat source property to the material
            OOF.Property.Parametrize.Thermal.HeatSource.TestNonconstantHeatSource(
                testno=source_no)
            OOF.Material.Add_property(
                name='material',
                property='Thermal:HeatSource:TestNonconstantHeatSource')
            OOF.Material.Assign(
                material='material', microstructure='microstructure', pixels=all)

            # set the boundary conditions for the given test no
            self.setBoundaryConditions( 'Dirichlet', Temperature, Heat_Eqn,
                                        self.heat_solns[soln_no]["DirichletBC"] )

            # compute the solution using Newton's method
            test_solver = Newton(
                relative_tolerance=1e-13,
                absolute_tolerance=1e-13,
                maximum_iterations=20)

            self.heatEqnEngine( soln_no, z_soln_no, test_solver )

            # remove the boundary conditions for the given test no
            self.removeBoundaryConditions()

            # remove the nonlin heat conductivity and nonconst heat source properties
            OOF.Material.Remove_property(
                name='material',
                property='Thermal:Conductivity:TestNonlinearHeatConductivityNoDeriv')
            OOF.Material.Remove_property(
                name='material',
                property='Thermal:HeatSource:TestNonconstantHeatSource')
            OOF.Material.Remove_property(
                name='material',
                property='Orientation')

        # delete the other properties, fields, equations needed for this test
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Heat_Flux)
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Heat_Eqn)
        OOF.Subproblem.Field.Undefine(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)


    def heatEqnEngine(self, soln_no, z_soln_no, test_solver):

        soln_func   = self.heat_solns[soln_no]["Solution"]
        z_soln_func = self.heat_solns[z_soln_no]["Solution"]

        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=StaticDriver(),
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
            initializer=ConstScalarFieldInit(value=0.0))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Temperature_z,
            initializer=ConstScalarFieldInit(value=0.0))
        OOF.Mesh.Apply_Field_Initializers(
            mesh='microstructure:skeleton:mesh')

        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=self.time)

        from ooflib.engine import mesh
        from ooflib.SWIG.engine import field

        mesh_obj  = mesh.meshes["microstructure:skeleton:mesh"].getObject()

        # first compute the numerical error in the computed temperature field
        field_ptr = field.getField( "Temperature" )

        L2_error = computeScalarErrorL2( soln_func, mesh_obj, field_ptr,
                                         self.numX, self.numY, time=self.time )
        print "Temperature L2 error: ", L2_error
        self.assert_( L2_error < 1.e-2 )

        # now compute the numerical error in the computed temperature_z field
        field_ptr = field.getField( "Temperature_z" )

        L2_error = computeScalarErrorL2( z_soln_func, mesh_obj, field_ptr,
                                         self.numX, self.numY, time=self.time )
        print "Temperture_z L2 error: ", L2_error
        self.assert_( L2_error < 1.e-2 )


    @memorycheck.check("microstructure")
    def LinearElasticity(self):

        test_coefficients = [
            TriclinicRank4TensorCij(c11=4, c12=0, c13=1, c14=0, c15=2, c16=0,
                                           c22=4, c23=1, c24=2, c25=0, c26=0,
                                           c33=4, c34=0, c35=0, c36=0,
                                           c44=4, c45=0, c46=0,
                                           c55=4, c56=0,
                                           c66=4) ]
        const_test_forces = [ (-23.5,-34.0) ]

        linear_elasticity_tests = [ {"test_no":0, "force_no" :0,
                                     "soln_no":7, "z_soln_no":0} ]

        # define the elasticity eqn related quantities needed for this test
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Force_Balance)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)

        # iterate through nonlinear elasticity test by alternating
        # between various test examples and nonlinear solvers
        for test in linear_elasticity_tests:

            test_no   = test["test_no"]
            force_no  = test["force_no"]
            soln_no   = test["soln_no"]
            z_soln_no = test["z_soln_no"]

            # add the linear elasticity property to the material
            OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Triclinic(
                cijkl=test_coefficients[test_no])
            OOF.Material.Add_property(
                name='material',
                property='Mechanical:Elasticity:Anisotropic:Triclinic')
            # add the constant force density property to the material
            OOF.Property.Parametrize.Mechanical.ForceDensity.ConstantForceDensity(
                gx=const_test_forces[force_no][0],
                gy=const_test_forces[force_no][1])
            OOF.Material.Add_property(
                name='material',
                property='Mechanical:ForceDensity:ConstantForceDensity')
            # add the orientation property to the material
            OOF.Property.Parametrize.Orientation(
                angles=Abg(alpha=0,beta=0,gamma=0))
            OOF.Material.Add_property(
                name='material',
                property='Orientation')
            # assign the material to the microstructure
            OOF.Material.Assign(
                material='material', microstructure='microstructure', pixels=all)

            # set the boundary conditions for the given test no
            self.setBoundaryConditions( 'Dirichlet', Displacement, Force_Balance,
                                        self.elasticity_solns[soln_no]["DirichletBC"] )

            # compute the solution using Newton's method
            test_solver = Newton(
                relative_tolerance=1e-08,
                absolute_tolerance=1e-13,
                maximum_iterations=20)

            self.elasticityEqnEngine( soln_no, z_soln_no, test_solver )

            # remove the boundary conditions for the given test no
            self.removeBoundaryConditions()

            # remove the nonlin elasticity and nonconst force density properties
            OOF.Material.Remove_property(
                name='material',
                property='Mechanical:Elasticity:Anisotropic:Triclinic')
            OOF.Material.Remove_property(
                name='material',
                property='Mechanical:ForceDensity:ConstantForceDensity')
            OOF.Material.Remove_property(
                name='material',
                property='Orientation')

        # delete the other properties, fields, equations needed for this test
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Force_Balance)
        OOF.Subproblem.Field.Undefine(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)


    @memorycheck.check("microstructure")
    def NonlinearElasticity(self):

        nonlin_elasticity_tests = [ {"test_no":2,"force_no":5,
                                     "soln_no":6,"z_soln_no":1} ]

        # define the elasticity eqn related quantities needed for this test
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Force_Balance)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)

        # iterate through nonlinear elasticity test by alternating
        # between various test examples and nonlinear solvers
        for test in nonlin_elasticity_tests:

            test_no   = test["test_no"]
            force_no  = test["force_no"]
            soln_no   = test["soln_no"]
            z_soln_no = test["z_soln_no"]

            # add the nonlinear elasticity property to the material
            OOF.Property.Parametrize.Mechanical.Elasticity.TestGeneralNonlinearElasticity(
                testno=test_no)
            OOF.Material.Add_property(
                name='material',
                property='Mechanical:Elasticity:TestGeneralNonlinearElasticity')
            # add the nonconstant force density property to the material
            OOF.Property.Parametrize.Mechanical.ForceDensity.TestNonconstantForceDensity(
                testno=force_no)
            OOF.Material.Add_property(
                name='material',
                property='Mechanical:ForceDensity:TestNonconstantForceDensity')
            # add the orientation property to the material
            OOF.Property.Parametrize.Orientation(
                angles=Abg(alpha=0,beta=0,gamma=0))
            OOF.Material.Add_property(
                name='material',
                property='Orientation')
            # assign the material to the microstructure
            OOF.Material.Assign(
                material='material', microstructure='microstructure', pixels=all)

            # set the boundary conditions for the given test no
            self.setBoundaryConditions( 'Dirichlet', Displacement, Force_Balance,
                                        self.elasticity_solns[soln_no]["DirichletBC"] )

            # compute the solution using Newton's method
            test_solver = Newton(
                relative_tolerance=1e-08,
                absolute_tolerance=1e-13,
                maximum_iterations=20)

            self.elasticityEqnEngine( soln_no, z_soln_no, test_solver )

            # remove the boundary conditions for the given test no
            self.removeBoundaryConditions()

            # remove the nonlin elasticity and nonconst force density properties
            OOF.Material.Remove_property(
                name='material',
                property='Mechanical:Elasticity:TestGeneralNonlinearElasticity')
            OOF.Material.Remove_property(
                name='material',
                property='Mechanical:ForceDensity:TestNonconstantForceDensity')
            OOF.Material.Remove_property(
                name='material',
                property='Orientation')

        # delete the other properties, fields, equations needed for this test
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Force_Balance)
        OOF.Subproblem.Field.Undefine(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)


    @memorycheck.check("microstructure")
    def NonlinearElasticityNoDeriv(self):

        nonlin_elasticity_tests = [ {"test_no":2,"force_no":5,
                                     "soln_no":6,"z_soln_no":1} ]

        # define the elasticity eqn related quantities needed for this test
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Force_Balance)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)

        # iterate through nonlinear elasticity test by alternating
        # between various test examples and nonlinear solvers
        for test in nonlin_elasticity_tests:

            test_no   = test["test_no"]
            force_no  = test["force_no"]
            soln_no   = test["soln_no"]
            z_soln_no = test["z_soln_no"]

            # add the nonlinear elasticity property to the material
            OOF.Property.Parametrize.Mechanical.Elasticity.TestGeneralNonlinearElasticityNoDeriv(
                testno=test_no)
            OOF.Material.Add_property(
                name='material',
                property='Mechanical:Elasticity:TestGeneralNonlinearElasticityNoDeriv')
            # add the nonconstant force density property to the material
            OOF.Property.Parametrize.Mechanical.ForceDensity.TestNonconstantForceDensity(
                testno=force_no)
            OOF.Material.Add_property(
                name='material',
                property='Mechanical:ForceDensity:TestNonconstantForceDensity')
            # add the orientation property to the material
            OOF.Property.Parametrize.Orientation(
                angles=Abg(alpha=0,beta=0,gamma=0))
            OOF.Material.Add_property(
                name='material',
                property='Orientation')
            # assign the material to the microstructure
            OOF.Material.Assign(
                material='material', microstructure='microstructure', pixels=all)

            # set the boundary conditions for the given test no
            self.setBoundaryConditions( 'Dirichlet', Displacement, Force_Balance,
                                        self.elasticity_solns[soln_no]["DirichletBC"] )

            # compute the solution using Newton's method
            test_solver = Newton(
                relative_tolerance=1e-13,
                absolute_tolerance=1e-13,
                maximum_iterations=20)

            self.elasticityEqnEngine( soln_no, z_soln_no, test_solver )

            # remove the boundary conditions for the given test no
            self.removeBoundaryConditions()

            # remove the nonlin elasticity and nonconst force density properties
            OOF.Material.Remove_property(
                name='material',
                property='Mechanical:Elasticity:TestGeneralNonlinearElasticityNoDeriv')
            OOF.Material.Remove_property(
                name='material',
                property='Mechanical:ForceDensity:TestNonconstantForceDensity')
            OOF.Material.Remove_property(
                name='material',
                property='Orientation')

        # delete the other properties, fields, equations needed for this test
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Force_Balance)
        OOF.Subproblem.Field.Undefine(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)


    def elasticityEqnEngine(self, soln_no, z_soln_no, test_solver):

        soln_func   = self.elasticity_solns[soln_no]["Solution"]
        z_soln_func = self.elasticity_z_solns[z_soln_no]["Solution"]

        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=StaticDriver(),
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
            field=Displacement,
            initializer=ConstTwoVectorFieldInit(cx=0.0,cy=0.0))
        OOF.Mesh.Apply_Field_Initializers(
            mesh='microstructure:skeleton:mesh')
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Displacement_z,
            initializer=ConstThreeVectorFieldInit(cx=0.0,cy=0.0,cz=0.0))

        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=self.time)

        from ooflib.engine import mesh
        from ooflib.SWIG.engine import field

        mesh_obj  = mesh.meshes["microstructure:skeleton:mesh"].getObject()
        field_ptr = field.getField( "Displacement" )

        L2_error = computeVector2DErrorL2( soln_func, mesh_obj, field_ptr,
                                           self.numX, self.numY, time=self.time )
        print "Displacement L2 error: ", L2_error

        self.assert_( L2_error < 6.e-2 )

        field_ptr = field.getField( "Displacement_z" )

        L2_error = computeVector3DErrorL2( z_soln_func, mesh_obj, field_ptr,
                                           self.numX, self.numY, time=self.time )
        print "Displacement_z L2 error: ", L2_error

        self.assert_( L2_error < 1.1e-1 )


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Routine to do regression-type testing on the items in this file.
# Tests will be run in the order they appear in the list.  This
# routine will stop after the first failure.

def run_tests():
    property_set = [
        NonlinearPlaneFluxTest("LinearHeatConductivity"),
        NonlinearPlaneFluxTest("NonlinearHeatConductivity"),
        NonlinearPlaneFluxTest("NonlinearHeatConductivityNoDeriv"),
        NonlinearPlaneFluxTest("LinearElasticity"),
        NonlinearPlaneFluxTest("NonlinearElasticity"),
        NonlinearPlaneFluxTest("NonlinearElasticityNoDeriv"),
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

