# -*- python -*-
# $RCSfile: scheduled_output_test.py,v $
# $Revision: 1.3 $
# $Author: langer $
# $Date: 2011/04/14 21:01:43 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## Tests for the ScheduledOutputs, using Boundary Analysis operations.

## TODO: Add tests that continue a solution.

import unittest, os, sys
import memorycheck

from UTILS import file_utils
# Flag that says whether to generate missing reference data files.
# Should be false unless you really know what you're doing.
#file_utils.generate = True

class OOF_ScheduledOutput(unittest.TestCase):
    def setUp(self):
        # Define a problem with both elasticity and thermal
        # conductivity.  The 'time evolution' will be trival because
        # the initial conditions are in equilibrium with the boundary
        # conditions.  This lets us test the outputs against exact
        # solutions, which are:
        #    displacement = (0.1*x, 0)
        #    temperature = y
        OOF.Microstructure.New(
            name='microstructure',
            width=1.0, height=1.0,
            width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(name='material', material_type='bulk')
        OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic(
            cijkl=IsotropicRank4TensorEnu(
                young=0.66666666666666663,
                poisson=0.0))
        OOF.Material.Add_property(
            name='material',
            property='Mechanical:Elasticity:Isotropic')
        OOF.Property.Parametrize.Mechanical.MassDensity.ConstantMassDensity(
            rho=1.0)
        OOF.Material.Add_property(
            name='material',
            property='Mechanical:MassDensity:ConstantMassDensity')
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
        OOF.Material.Assign(
            material='material',
            microstructure='microstructure',
            pixels=every)
        OOF.Skeleton.New(
            name='skeleton',
            microstructure='microstructure',
            x_elements=4, y_elements=4, 
            skeleton_geometry=QuadSkeleton(
                left_right_periodicity=False,top_bottom_periodicity=False))
        OOF.Mesh.New(
            name='mesh',
            skeleton='microstructure:skeleton',
            element_types=['D2_2', 'T3_3', 'Q4_4'])
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', 
            field=Displacement)
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', 
            field=Temperature)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Heat_Eqn)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default', 
            equation=Force_Balance)
        OOF.Mesh.Boundary_Conditions.New(
            name='bc',
            mesh='microstructure:skeleton:mesh', 
            condition=DirichletBC(
                field=Displacement,field_component='x',
                equation=Force_Balance,eqn_component='x',
                profile=ConstantProfile(value=0.0),
                boundary='left'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<2>',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Displacement,field_component='y',
                equation=Force_Balance,eqn_component='y',
                profile=ConstantProfile(value=0.0),
                boundary='bottomleft'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', 
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Displacement,field_component='x',
                equation=Force_Balance,eqn_component='x',
                profile=ConstantProfile(
                    value=0.10000000000000001),
                boundary='right'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=0),
                boundary='bottom'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<5>', 
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=1),
                boundary='top'))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Temperature, 
            initializer=FuncScalarFieldInit(function='y'))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh', 
            field=Displacement, 
            initializer=FuncTwoVectorFieldInit(fx='0.1*x',fy='0.0'))
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh',
            time=0.0)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=BasicSolverMode(
                time_stepper=BasicUniformDriver(stepsize=0.1),
                matrix_method=BasicIterative(tolerance=1e-13,
                                             max_iterations=1000)))

    def tearDown(self):
        OOF.Material.Delete(name='material')

    def solve(self):
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=1.0)

    def setScheduleAndDestination(self, outputname, filename, interval=0.1):
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output=outputname, 
            scheduletype=AbsoluteOutputSchedule(),
            schedule=Periodic(delay=0.0,interval=interval))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh',
            output=outputname, 
            destination=OutputStream(filename=filename,mode='w'))
        
    def rewind(self):
        OOF.Mesh.Scheduled_Output.Destination.RewindAll(
            mesh='microstructure:skeleton:mesh')
    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    # Routines for creating named and unnamed scheduled outputs.  The
    # test routines all use one or more of these.

    def scheduleUnnamedVectorFluxNormal(self, filename, interval):
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='vfn', 
            output=BoundaryAnalysis(
                operation=IntegrateBdyFlux(flux=Heat_Flux),
                boundary='top'))
        self.setScheduleAndDestination('vfn', filename, interval)

    def scheduleNamedVectorFluxNormal(self, filename, interval):
        OOF.Mesh.Boundary_Analysis.Create(
            name='vfn-named',
            boundary='top',
            analyzer=IntegrateBdyFlux(flux=Heat_Flux))
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='vfn<2>',
            output=NamedAnalysisOutput(analysis='vfn-named'))
        self.setScheduleAndDestination('vfn<2>', filename, interval)

    def scheduleUnnamedTensorFluxNormal(self, filename, interval):
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='tfn', 
            output=BoundaryAnalysis(
                operation=IntegrateBdyFlux(flux=Stress),
                boundary='left'))
        self.setScheduleAndDestination('tfn', filename, interval)
        
    def scheduleNamedTensorFluxNormal(self, filename, interval):
        OOF.Mesh.Boundary_Analysis.Create(
            name='tfn-named',
            boundary='left',
            analyzer=IntegrateBdyFlux(flux=Stress))
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='tfn<2>',
            output=NamedAnalysisOutput(analysis='tfn-named'))
        self.setScheduleAndDestination('tfn<2>', filename, interval)

    def scheduleUnnamedScalarField(self, filename, interval):
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='sf',
            output=BoundaryAnalysis(
                operation=AverageField(field=Temperature),
                boundary='left'))        
        self.setScheduleAndDestination('sf', filename, interval)

    def scheduleNamedScalarField(self, filename, interval):
        OOF.Mesh.Boundary_Analysis.Create(
            name='sf-named',
            boundary='left',
            analyzer=AverageField(field=Temperature))
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='sf<2>',
            output=NamedAnalysisOutput(analysis='sf-named'))
        self.setScheduleAndDestination('sf<2>', filename, interval)

    def scheduleUnnamedVectorField(self, filename, interval):
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='vf',
            output=BoundaryAnalysis(
                operation=AverageField(field=Displacement),
                boundary='top'))        
        self.setScheduleAndDestination('vf', filename, interval)

    def scheduleNamedVectorField(self, filename, interval):
        OOF.Mesh.Boundary_Analysis.Create(
            name='vf-named',
            boundary='top',
            analyzer=AverageField(field=Displacement))
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='vf<2>',
            output=NamedAnalysisOutput(analysis='vf-named'))
        self.setScheduleAndDestination('vf<2>', filename, interval)

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    # Actual test routines.
    
    @memorycheck.check('microstructure')
    def UnnamedVectorFlux(self):
        self.scheduleUnnamedVectorFluxNormal('test.dat', 0.1)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'vectorfluxoutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def NamedVectorFlux(self):
        self.scheduleNamedVectorFluxNormal('test.dat', 0.1)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'vectorfluxoutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def UnnamedTensorFlux(self):
        self.scheduleUnnamedTensorFluxNormal('test.dat', 0.1)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'tensorfluxoutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('test.dat')
    
    @memorycheck.check('microstructure')
    def NamedTensorFlux(self):
        self.scheduleNamedTensorFluxNormal('test.dat', 0.1)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'tensorfluxoutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('test.dat')


    @memorycheck.check('microstructure')
    def UnnamedScalarField(self):
        self.scheduleUnnamedScalarField('test.dat', 0.1)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'scalarfieldoutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('test.dat')
    
    @memorycheck.check('microstructure')
    def NamedScalarField(self):
        self.scheduleNamedScalarField('test.dat', 0.1)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'scalarfieldoutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def UnnamedVectorField(self):
        self.scheduleUnnamedVectorField('test.dat', 0.1)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'vectorfieldoutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('test.dat')
    
    @memorycheck.check('microstructure')
    def NamedVectorField(self):
        self.scheduleNamedVectorField('test.dat', 0.1)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'vectorfieldoutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def TwoSeparateUnnamed(self):
        # Two outputs sent to separate files.
        self.scheduleUnnamedVectorField('vtest.dat', 0.1)
        self.scheduleUnnamedTensorFluxNormal('ttest.dat', 0.1)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'vtest.dat',
                os.path.join('mesh_data', 'vectorfieldoutput.dat'),
                1.e-8))
        self.assert_(file_utils.fp_file_compare(
                'ttest.dat',
                os.path.join('mesh_data', 'tensorfluxoutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('vtest.dat')
        file_utils.remove('ttest.dat')

    @memorycheck.check('microstructure')
    def TwoSeparateNamed(self):
        # Two outputs sent to separate files.
        self.scheduleNamedVectorField('vtest.dat', 0.1)
        self.scheduleNamedTensorFluxNormal('ttest.dat', 0.1)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'vtest.dat',
                os.path.join('mesh_data', 'vectorfieldoutput.dat'),
                1.e-8))
        self.assert_(file_utils.fp_file_compare(
                'ttest.dat',
                os.path.join('mesh_data', 'tensorfluxoutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('vtest.dat')
        file_utils.remove('ttest.dat')

    @memorycheck.check('microstructure')
    def TwoTogetherUnnamed(self):
        # Two outputs sent to one file.
        self.scheduleUnnamedVectorField('test.dat', 0.1)
        self.scheduleUnnamedTensorFluxNormal('test.dat', 0.1)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'combooutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('test.dat')
        
    @memorycheck.check('microstructure')
    def TwoTogetherNamed(self):
        # Two outputs sent to one file.
        self.scheduleNamedVectorField('test.dat', 0.1)
        self.scheduleNamedTensorFluxNormal('test.dat', 0.1)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'combooutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('test.dat')
        
    @memorycheck.check('microstructure')
    def TwoTogetherAsync(self):
        # Two outputs sent to one file.
        self.scheduleUnnamedVectorField('test.dat', 0.1)
        self.scheduleUnnamedTensorFluxNormal('test.dat', 0.2)
        self.solve()
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'asyncoutput.dat'),
                1.e-8))
        self.rewind()
        file_utils.remove('test.dat')
        

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Routine to do regression-type testing on the items in this file.
# Tests must be run in the order they appear in the list.  This
# routine will stop after the first failure.

def run_tests():

    from ooflib.SWIG.common import config
    
    test_set = [
        OOF_ScheduledOutput("UnnamedVectorFlux"),
        OOF_ScheduledOutput("NamedVectorFlux"),
        OOF_ScheduledOutput("UnnamedTensorFlux"),
        OOF_ScheduledOutput("NamedTensorFlux"),
        OOF_ScheduledOutput("UnnamedScalarField"),
        OOF_ScheduledOutput("NamedScalarField"),
        OOF_ScheduledOutput("UnnamedVectorField"),
        OOF_ScheduledOutput("NamedVectorField"),
        OOF_ScheduledOutput("TwoSeparateUnnamed"),
        OOF_ScheduledOutput("TwoSeparateNamed"),
        OOF_ScheduledOutput("TwoTogetherUnnamed"),
        OOF_ScheduledOutput("TwoTogetherNamed"),
        OOF_ScheduledOutput("TwoTogetherAsync")
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
        os.remove("test.dat")
    except:
        pass
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
