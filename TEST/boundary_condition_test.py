# -*- python -*-

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
from . import memorycheck
from .UTILS.file_utils import reference_file

# Flag that says whether to generate missing reference data files for
# the Modify tests.  Should be false unless you really know what
# you're doing.  New reference files won't be generated unless the old
# one is removed first, though.
generate = False

## TODO: Most tolerances had to be increased from 1e-12 after
## upgrading to Eigen 3.3.9 and switching preconditioners from ILU to
## IC.  Probably the reference files should be recomputed and the
## tolerances set back as low as they can go.

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
                    preconditioner=ICPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)
        fname = reference_file("bc_data", "simple_solution_test")
        if generate and not os.path.exists(fname):
            OOF.Microstructure.Rename(microstructure="bc_test",
                                      name="saved_data")
            OOF.File.Save.Mesh(filename=fname,
                               mode="w", format="ascii",
                               mesh="saved_data:skeleton:mesh")
            OOF.Microstructure.Rename(microstructure="saved_data",
                                      name="bc_test")
        OOF.File.Load.Data(filename=fname)
        from ooflib.engine import mesh
        saved = mesh.meshes["saved_data:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-7), 0)

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
                    preconditioner=ICPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)

        fname = reference_file("bc_data", "periodic_1")
        if generate and not os.path.exists(fname):
            OOF.Microstructure.Rename(microstructure="bc_test",
                                      name="periodic_1")
            OOF.File.Save.Mesh(filename=fname,
                               mode="w", format="ascii",
                               mesh="periodic_1:skeleton:mesh")
            OOF.Microstructure.Rename(microstructure="periodic_1",
                                      name="bc_test")

        OOF.File.Load.Data(filename=fname)
        from ooflib.engine import mesh
        saved = mesh.meshes["periodic_1:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        # Tolerance increased from 1.e-13 when new version of Eigen installed.
        self.assertEqual(saved.compare(damned, 1.0e-7), 0)


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
                    preconditioner=ICPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)

        fname = reference_file("bc_data", "periodic_2")
        if generate and not os.path.exists(fname):
            OOF.Microstructure.Rename(microstructure="bc_test",
                                      name="periodic_2")
            OOF.File.Save.Mesh(filename=fname,
                               mode="w", format="ascii",
                               mesh="periodic_2:skeleton:mesh")
            OOF.Microstructure.Rename(microstructure="periodic_2",
                                      name="bc_test")

        OOF.File.Load.Data(filename=fname)
        from ooflib.engine import mesh
        saved = mesh.meshes["periodic_2:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        # Tolerance increased from 1.e-13 when new version of Eigen installed.
        self.assertEqual(saved.compare(damned, 1.0e-7), 0)


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
                    preconditioner=ICPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)
        
        fname = reference_file("bc_data", "twofloats")
        if generate and not os.path.exists(fname):
            OOF.Microstructure.Rename(microstructure="bc_test",
                                      name="twofloats")
            OOF.File.Save.Mesh(filename=fname,
                               mode="w", format="ascii",
                               mesh="twofloats:skeleton:mesh")
            OOF.Microstructure.Rename(microstructure="twofloats",
                                      name="bc_test")

        OOF.File.Load.Data(filename=fname)
        from ooflib.engine import mesh
        saved = mesh.meshes["twofloats:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-6), 0)


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
                    preconditioner=ICPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)

        fname = reference_file("bc_data", "floatloop")
        if generate and not os.path.exists(fname):
            OOF.Microstructure.Rename(microstructure="bc_test",
                                      name="floatloop")
            OOF.File.Save.Mesh(filename=fname,
                               mode="w", format="ascii",
                               mesh="floatloop:skeleton:mesh")
            OOF.Microstructure.Rename(microstructure="floatloop",
                                      name="bc_test")

        OOF.File.Load.Data(filename=fname)
        from ooflib.engine import mesh
        saved = mesh.meshes["floatloop:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]

        # TODO: Fails on 1.0e-13 tolerance, but didn't always -- why?
        self.assertEqual(saved.compare(damned, 1.0e-6), 0)


    # inconsistent loop of floats
    @memorycheck.check("twofloats", "bc_test")
    def InconsistentFloatLoop(self):
        OOF.Subproblem.Set_Solver(
            subproblem='bc_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ICPreconditioner(),
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
        from ooflib.SWIG.engine import ooferror
        self.assertRaises(ooferror.PyErrSetupError,
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
        self.assertEqual(saved.compare(damned, 1.0e-6), 0)

        # now re-enable the boundary conditions and make sure that
        # attempting to solve raises the error again
        OOF.Mesh.Boundary_Conditions.Enable(mesh='bc_test:skeleton:mesh',
                                            name='bc<6>')
        OOF.Mesh.Boundary_Conditions.Enable(mesh='bc_test:skeleton:mesh',
                                            name='bc<5>')
        self.assertRaises(ooferror.PyErrSetupError,
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
                    preconditioner=ICPreconditioner(),
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
                    preconditioner=ICPreconditioner(),
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
                    preconditioner=ICPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)

        fname = reference_file("bc_data", "fixedfloatloop")
        if generate and not os.path.exists(fname):
            OOF.Microstructure.Rename(microstructure="bc_test",
                                      name="fixedfloatloop")
            OOF.File.Save.Mesh(filename=fname,
                               mode="w", format="ascii",
                               mesh="fixedfloatloop:skeleton:mesh")
            OOF.Microstructure.Rename(microstructure="fixedfloatloop",
                                      name="bc_test")

        OOF.File.Load.Data(filename=fname)
        from ooflib.engine import mesh
        saved = mesh.meshes["fixedfloatloop:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-7), 0)

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
                    preconditioner=ICPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)

        OOF.File.Load.Data(filename=reference_file("bc_data", "fixedfloatloop"))
        from ooflib.engine import mesh
        saved = mesh.meshes["fixedfloatloop:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-7), 0)


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
                    preconditioner=ICPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        OOF.Mesh.Solve(mesh='bc_test:skeleton:mesh',
                       endtime=0.0)


        OOF.File.Load.Data(filename=reference_file("bc_data", "twofixed"))
        from ooflib.engine import mesh
        saved = mesh.meshes["twofixed:skeleton:mesh"]
        damned = mesh.meshes["bc_test:skeleton:mesh"]
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
                    preconditioner=ICPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        from ooflib.SWIG.common import ooferror
        self.assertRaises(ooferror.PyErrWarning,
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
                    preconditioner=ICPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)))
        from ooflib.SWIG.common import ooferror
        self.assertRaises(ooferror.PyErrUserError,
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
