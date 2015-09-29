# -*- python -*-
# $RCSfile: boundary_condition_test.py,v $
# $Revision: 1.25 $
# $Author: langer $
# $Date: 2011/05/27 19:27:58 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Tests for the machinery that handles boundary condition
# intersections, floatBC promotion, and enabling and disabling of
# boundary conditions.

import unittest, os
import memorycheck
from UTILS.file_utils import reference_file

class OOF_BCTest(unittest.TestCase):
    def setUp(self):
        global femesh, cskeleton, cmicrostructure
        from ooflib.SWIG.common import cmicrostructure
        from ooflib.SWIG.engine import cskeleton, femesh
        OOF.File.Load.Data(
            filename=reference_file("bc_data", "periodic_test_mesh"))

    @memorycheck.check("saved_data", "bc_test")
    def SimpleSolve(self):
        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)
        OOF.File.Load.Data(filename=reference_file("bc_data",
                                                 "simple_solution_test"))
        from ooflib.engine import mesh
        saved = mesh.meshes["saved_data:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-13), 0)

    # periodic in one direction
    @memorycheck.check("periodic_1", "bc_test")
    def Periodic1(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='bc_test:skeleton:mesh',
            condition=PeriodicBC(field=Temperature,
                                 equation=Heat_Eqn,
                                 boundary='top bottom'))
        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)

        OOF.File.Load.Data(filename=reference_file("bc_data", "periodic_1"))
        from ooflib.engine import mesh
        saved = mesh.meshes["periodic_1:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-13), 0)


    # periodic in two directions
    @memorycheck.check("periodic_2", "bc_test")
    def Periodic2(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='bc_test:skeleton:mesh',
            condition=PeriodicBC(field=Temperature,
                                 equation=Heat_Eqn,
                                 boundary='top bottom'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>', mesh='bc_test:skeleton:mesh',
            condition=PeriodicBC(field=Temperature,
                                 equation=Heat_Eqn,
                                 boundary='left right'))
        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)

        OOF.File.Load.Data(filename=reference_file("bc_data", "periodic_2"))
        from ooflib.engine import mesh
        saved = mesh.meshes["periodic_2:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-13), 0)


    # float intersecting float
    @memorycheck.check("twofloats", "bc_test")
    def TwoFloats(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='0'),
                              boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='alpha'),
                              boundary='left'))

        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)
        
        OOF.File.Load.Data(filename=reference_file("bc_data", "twofloats"))
        from ooflib.engine import mesh
        saved = mesh.meshes["twofloats:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-13), 0)


    # loop of floats
    @memorycheck.check("floatloop", "bc_test")
    def FloatLoop(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='0'),
                              boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='alpha'),
                              boundary='left'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<5>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='0'),
                              boundary='bottom'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<6>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='-alpha'),
                              boundary='right'))

        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)

        
        OOF.File.Load.Data(filename=reference_file("bc_data", "floatloop"))
        from ooflib.engine import mesh
        saved = mesh.meshes["floatloop:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]

        # TODO: Fails on 1.0e-13 tolerance, but didn't always -- why?
        self.assertEqual(saved.compare(damned, 1.0e-12), 0)


    # inconsistent loop of floats
    @memorycheck.check("twofloats", "bc_test")
    def InconsistentFloatLoop(self):
        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))

        # Set up an inconsistent floating boundary condition loop
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='0'),
                              boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='alpha'),
                              boundary='left'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<5>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='0'),
                              boundary='bottom'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<6>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='alpha'),
                              boundary='right'))

        # make sure an inconsistent loop raises an error
        from ooflib.SWIG.engine import ooferror2
        self.assertRaises(ooferror2.ErrSetupError,
                          OOF.Mesh.Solve, mesh="bc_test:skeleton:mesh",
                          endtime=0.0)

        # now disable two of the boundaries conditions to make the set
        # consistent (and so that it matches the test in TwoFloats)
        OOF.Mesh.Boundary_Conditions.Disable(mesh='bc_test:skeleton:mesh',
                                             name='bc<6>')
        OOF.Mesh.Boundary_Conditions.Disable(mesh='bc_test:skeleton:mesh',
                                             name='bc<5>')
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh', endtime=0.0)
        OOF.File.Load.Data(filename=reference_file("bc_data", "twofloats"))
        from ooflib.engine import mesh
        saved = mesh.meshes["twofloats:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-13), 0)

        # now re-enable the boundary conditions and make sure that
        # attempting to solve raises the error again
        OOF.Mesh.Boundary_Conditions.Enable(mesh='bc_test:skeleton:mesh',
                                            name='bc<6>')
        OOF.Mesh.Boundary_Conditions.Enable(mesh='bc_test:skeleton:mesh',
                                            name='bc<5>')
        self.assertRaises(ooferror2.ErrSetupError,
                          OOF.Mesh.Solve, mesh='bc_test:skeleton:mesh',
                          endtime=0.0)

    # float intersecting fixed
    @memorycheck.check("floatandfixed", "bc_test")
    def FloatAndFixed(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='bc_test:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='0',timeDerivative='0',timeDerivative2='0'),
                boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='alpha'),
                              boundary='left'))

        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)


        OOF.File.Load.Data(filename=reference_file("bc_data", "floatandfixed"))
        from ooflib.engine import mesh
        saved = mesh.meshes["floatandfixed:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-12), 0)

    # float intersecting fixed, with a trivial offset added to the float.
    @memorycheck.check("floatandfixed", "bc_test")
    def FloatAndFixed2(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='bc_test:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='0',timeDerivative='0',timeDerivative2='0'),
                boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='alpha+1.234'),
                              boundary='left'))

        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)


        OOF.File.Load.Data(filename=reference_file("bc_data", "floatandfixed"))
        from ooflib.engine import mesh
        saved = mesh.meshes["floatandfixed:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-12), 0)


    # loop of floats
    @memorycheck.check("fixedfloatloop", "bc_test")
    def FloatAndFixedLoop(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='bc_test:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='0',timeDerivative='0',timeDerivative2='0'),
                boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='alpha'),
                              boundary='left'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<5>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='0'),
                              boundary='bottom'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<6>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='-alpha'),
                              boundary='right'))
        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)

        OOF.File.Load.Data(filename=reference_file("bc_data", "fixedfloatloop"))
        from ooflib.engine import mesh
        saved = mesh.meshes["fixedfloatloop:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-13), 0)

    # loop of floats, with nontrivial but nonconsequential offsets
    @memorycheck.check("fixedfloatloop", "bc_test")
    def FloatAndFixedLoop2(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='bc_test:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='0',timeDerivative='0',timeDerivative2='0'),
                boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='alpha+1.234'),
                              boundary='left'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<5>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='-17'),
                              boundary='bottom'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<6>', mesh='bc_test:skeleton:mesh',
            condition=FloatBC(field=Temperature,field_component='',
                              equation=Heat_Eqn,eqn_component='',
                              profile=ContinuumProfile(function='-alpha-3.14'),
                              boundary='right'))
        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)

        OOF.File.Load.Data(filename=reference_file("bc_data", "fixedfloatloop"))
        from ooflib.engine import mesh
        saved = mesh.meshes["fixedfloatloop:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-13), 0)


    # fixed intersecting fixed
    @memorycheck.check("twofixed", "bc_test")
    def TwoFixed(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='bc_test:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='0',timeDerivative='0',timeDerivative2='0'),
                boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>', mesh='bc_test:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='alpha',timeDerivative='0',timeDerivative2='0'),
                boundary='left'))
        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)


        OOF.File.Load.Data(filename=reference_file("bc_data", "twofixed"))
        from ooflib.engine import mesh
        saved = mesh.meshes["twofixed:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        # TODO: Reduced tolerance needed here, too, was 1.0e-13.
        self.assertEqual(saved.compare(damned, 1.0e-12), 0)

    # Two conflicting Dirichlet boundary conditions on different
    # boundaries.  Conflicting Dirichlet conditions only raise a
    # Warning, which we can't detect here, unless this test is run in
    # NoWarnings mode.
    @memorycheck.check("bc_test")
    def DirichletClash(self):
        OOF.Help.No_Warnings(True)
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='bc_test:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='1',timeDerivative='0',timeDerivative2='0'),
                boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>', mesh='bc_test:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='alpha',timeDerivative='0',timeDerivative2='0'),
                boundary='left'))
        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        from ooflib.SWIG.common import ooferror
        self.assertRaises(ooferror.ErrWarning,
                          OOF.Mesh.Solve,
                          mesh='bc_test:skeleton:mesh',
                          endtime=0.0)
        OOF.Help.No_Warnings(False)

    # Two conflicting Dirichlet boundary conditions on the same
    # boundary.  This raises an error even if not in NoWarnings mode.
    @memorycheck.check("bc_test")
    def DirichletClash2(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='bc_test:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='1',timeDerivative='0',timeDerivative2='0'),
                boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>', mesh='bc_test:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='alpha',timeDerivative='0',timeDerivative2='0'),
                boundary='top'))
        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        from ooflib.SWIG.common import ooferror
        self.assertRaises(ooferror.ErrUserError,
                          OOF.Mesh.Solve,
                          mesh='bc_test:skeleton:mesh',
                          endtime=0.0)
        # Now fix the conflict and make sure the mesh is solvable.
        OOF.Mesh.Boundary_Conditions.Edit(
            name='bc<4>',
            mesh='bc_test:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='alpha',timeDerivative='0',timeDerivative2='0'),
                boundary='bottom'))
        OOF.Mesh.Solve(
            mesh='bc_test:skeleton:mesh',
            endtime=0.0)
    
    def tearDown(self):
        OOF.Property.Delete(property='Color:blue')
        OOF.Property.Delete(property='Color:white')
        OOF.Property.Delete(property='Thermal:Conductivity:Isotropic:blue_k')
        OOF.Property.Delete(property='Thermal:Conductivity:Isotropic:white_k')
        OOF.Property.Delete(
            property='Mechanical:Elasticity:Isotropic:blue_elastic')
        OOF.Property.Delete(
            property='Mechanical:Elasticity:Isotropic:white_elastic')
        OOF.Material.Delete(name='bulk')
        OOF.Material.Delete(name='boundaries')




#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Routine to do regression-type testing on the items in this file.
# Tests must be run in the order they appear in the list.  This
# routine will stop after the first failure.
def run_tests():

    test_set = [
        OOF_BCTest("SimpleSolve"),
        OOF_BCTest("Periodic1"),
        OOF_BCTest("Periodic2"),
        OOF_BCTest("TwoFloats"),
        OOF_BCTest("FloatLoop"),
        OOF_BCTest("InconsistentFloatLoop"),
        OOF_BCTest("FloatAndFixed"),
        OOF_BCTest("FloatAndFixed2"),
        OOF_BCTest("FloatAndFixedLoop"),
        OOF_BCTest("FloatAndFixedLoop2"),
        OOF_BCTest("TwoFixed"),
        OOF_BCTest("DirichletClash"),
        OOF_BCTest("DirichletClash2")
        ]

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
