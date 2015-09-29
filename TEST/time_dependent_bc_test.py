# -*- python -*-
# $RCSfile: time_dependent_bc_test.py,v $
# $Revision: 1.5 $
# $Author: langer $
# $Date: 2011/06/08 19:04:52 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Tests for different kinds of boundary conditions, including
# time-dependent boundary conditions, in time-dependent problems.

import unittest, os
import memorycheck
from UTILS import file_utils
reference_file = file_utils.reference_file
file_utils.generate = True

class OOF_TimeDependentDirichlet(unittest.TestCase):
    def setUp(self):
        global outputdestination
        from ooflib.engine.IO import outputdestination
        OOF.Microstructure.New(
            name='microstructure',
            width=1.0, height=1.0,
            width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(name='material', material_type='bulk')
        OOF.Material.Add_property(
            name='material',
            property='Mechanical:Elasticity:Isotropic')
        OOF.Material.Assign(
            material='material',
            microstructure='microstructure',
            pixels=every)
        OOF.Skeleton.New(
            name='skeleton',
            microstructure='microstructure',
            x_elements=5, y_elements=5,
            skeleton_geometry=QuadSkeleton(
                left_right_periodicity=False,top_bottom_periodicity=False))
        # Create a point boundary containing all nodes on the top edge.
        OOF.SegmentSelection.Select_Named_Boundary(
            skeleton='microstructure:skeleton',
            boundary='top')
        OOF.NodeSelection.Select_from_Selected_Segments(
            skeleton='microstructure:skeleton')
        OOF.Skeleton.Boundary.Construct(
            skeleton='microstructure:skeleton',
            name='toppoints',
            constructor=PointFromSegments(group=selection))

        OOF.Mesh.New(
            name='mesh', 
            skeleton='microstructure:skeleton',
            element_types=['D2_2', 'T3_3', 'Q4_4'])
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
        OOF.Mesh.Boundary_Conditions.New(
            name='bc',
            mesh='microstructure:skeleton:mesh', 
            condition=DirichletBC(
                field=Displacement,field_component='x',
                equation=Force_Balance,eqn_component='x',
                profile=ConstantProfile(value=0.0),
                boundary='bottom'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<2>',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Displacement,field_component='y',
                equation=Force_Balance,eqn_component='y',
                profile=ConstantProfile(value=0.0),
                boundary='bottom'))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Displacement,
            initializer=ConstTwoVectorFieldInit(cx=0.0,cy=0.0))
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh',
            time=0.0)

    def quasistatic(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=BasicSolverMode(
                time_stepper=BasicStaticDriver(),
                matrix_method=BasicIterative(
                    tolerance=1e-13,max_iterations=1000)))
    
    def adaptive(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=BasicSolverMode(
                time_stepper=BasicAdaptiveDriver(
                    tolerance=0.0001,minstep=1e-05),
                matrix_method=BasicIterative(
                    tolerance=1e-13,
                    max_iterations=1000)))

    def topleftOutput(self, interval, filename):
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='topleftx', 
            output=BulkAnalysis(
                output_type='Scalar',
                data=getOutput(
                    'Field:Component',component='x',
                    field=Displacement),
                operation=DirectOutput(),
                domain=SkeletonPointBoundaryDomain(boundary='topleft'),
                sampling=DiscretePointSampleSet(show_x=False,show_y=False)))
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output="topleftx", 
            scheduletype=AbsoluteOutputSchedule(),
            schedule=Periodic(delay=0.0,interval=interval))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh',
            output='topleftx',
            destination=OutputStream(filename=filename,mode='w'))

    def shearTopEdge(self):
        # Apply a shear dx=t to the top boundary
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', 
            mesh='microstructure:skeleton:mesh', 
            condition=DirichletBC(
                field=Displacement,field_component='x',
                equation=Force_Balance,eqn_component='x',
                profile=ContinuumProfileXTd(
                    function='t',timeDerivative='1.0',timeDerivative2='0.0'),
                boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Displacement,field_component='y',
                equation=Force_Balance,eqn_component='y',
                profile=ConstantProfile(value=0.0),
                boundary='top'))

    def shearTopPoints(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', 
            mesh='microstructure:skeleton:mesh', 
            condition=DirichletBC(
                field=Displacement,field_component='x',
                equation=Force_Balance,eqn_component='x',
                profile=ContinuumProfileXTd(
                    function='t',timeDerivative='1.0',timeDerivative2='0.0'),
                boundary='toppoints'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Displacement,field_component='y',
                equation=Force_Balance,eqn_component='y',
                profile=ConstantProfile(value=0.0),
                boundary='toppoints'))
            
    def tearDown(self):
        OOF.Material.Delete(name='material')


    @memorycheck.check("microstructure")
    def QuasiStatic(self):
        self.quasistatic()
        self.topleftOutput(interval=0.1, filename='test.dat')
        self.shearTopEdge()
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=1.0)
        self.assert_(
            file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'td_dirichlet.dat'),
                1.e-10))
        file_utils.remove('test.dat')
        outputdestination.forgetTextOutputStreams()

    @memorycheck.check("microstructure")
    def Adaptive(self):
        self.adaptive()
        self.topleftOutput(interval=0.1, filename='test.dat')
        self.shearTopEdge()
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=1.0)
        self.assert_(
            file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'td_dirichlet.dat'),
                1.e-10))
        file_utils.remove('test.dat')
        outputdestination.forgetTextOutputStreams()

    @memorycheck.check("microstructure")
    def QuasiStatic_Pts(self):
        self.quasistatic()
        self.topleftOutput(interval=0.1, filename='test.dat')
        self.shearTopPoints()
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=1.0)
        self.assert_(
            file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'td_dirichlet.dat'),
                1.e-10))
        file_utils.remove('test.dat')
        outputdestination.forgetTextOutputStreams()

    @memorycheck.check("microstructure")
    def Adaptive_Pts(self):
        self.adaptive()
        self.topleftOutput(interval=0.1, filename='test.dat')
        self.shearTopPoints()
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=1.0)
        self.assert_(
            file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'td_dirichlet.dat'),
                1.e-10))
        file_utils.remove('test.dat')
        outputdestination.forgetTextOutputStreams()


class OOF_TimeDependentFloat(unittest.TestCase):
    def setUp(self):
        global outputdestination
        from ooflib.engine.IO import outputdestination
        OOF.Microstructure.New(
            name='microstructure',
            width=1.0, height=1.0, 
            width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(name='material', material_type='bulk')
        OOF.Material.Add_property(
            name='material',
            property='Thermal:Conductivity:Isotropic')
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
            x_elements=10, y_elements=10, 
            skeleton_geometry=QuadSkeleton(
                left_right_periodicity=False,top_bottom_periodicity=False))
        # Create a point boundary containing all nodes on the top edge.
        OOF.SegmentSelection.Select_Named_Boundary(
            skeleton='microstructure:skeleton',
            boundary='top')
        OOF.NodeSelection.Select_from_Selected_Segments(
            skeleton='microstructure:skeleton')
        OOF.Skeleton.Boundary.Construct(
            skeleton='microstructure:skeleton',
            name='toppoints',
            constructor=PointFromSegments(group=selection))

        OOF.Mesh.New(
            name='mesh',
            skeleton='microstructure:skeleton',
            element_types=['D2_2', 'T3_3', 'Q4_4'])
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

        interval = 0.1
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
            schedule=Periodic(delay=0.0,interval=interval))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('Average Temperature on top'),
            destination=OutputStream(filename='temptop.dat',mode='w'))
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name=AutomaticName('Average Temperature on left'),
            output=BoundaryAnalysis(
                operation=AverageField(field=Temperature),
                boundary='left'))
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('Average Temperature on left'),
            scheduletype=AbsoluteOutputSchedule(),
            schedule=Periodic(delay=0.0,interval=interval))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('Average Temperature on left'), 
            destination=OutputStream(filename='templeft.dat',mode='w'))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Temperature,
            initializer=ConstScalarFieldInit(value=0.0))

    def initialize(self):
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh',
            time=0.0)

    def fixBottom(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='bottom',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=0.0),
                boundary='bottom'))

    def floatTopEdge(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='top',
            mesh='microstructure:skeleton:mesh',
            condition=FloatBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfile(function='-0.1*(x-0.5)'),
                boundary='top'))

    def floatTopPoints(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='top',
            mesh='microstructure:skeleton:mesh',
            condition=FloatBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfile(function='-0.1*(x-0.5)'),
                boundary='toppoints'))

    def floatLeftEdge(self):
        OOF.Mesh.Boundary_Conditions.New(
            name='left',
            mesh='microstructure:skeleton:mesh',
            condition=FloatBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfile(function='0.1*(s-0.5)'),
                boundary='left'))

    def adaptive(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=BasicSolverMode(
                time_stepper=BasicAdaptiveDriver(
                    tolerance=0.0001, minstep=1.e-05),
                matrix_method=BasicIterative(
                    tolerance=1e-13,max_iterations=1000)))

    def initializeMin(self, bdy, value):
        OOF.Mesh.Boundary_Conditions.Set_BC_Initializer(
            mesh='microstructure:skeleton:mesh',
            bc=bdy,
            initializer=FloatBCInitMin(value=value))

    def initializeMax(self, bdy, value):
        OOF.Mesh.Boundary_Conditions.Set_BC_Initializer(
            mesh='microstructure:skeleton:mesh',
            bc=bdy,
            initializer=FloatBCInitMax(value=value))

    def initializeAvg(self, bdy, value):
        OOF.Mesh.Boundary_Conditions.Set_BC_Initializer(
            mesh='microstructure:skeleton:mesh',
            bc=bdy,
            initializer=FloatBCInitAverage(value=value))

    def tearDown(self):
        OOF.Material.Delete(name='material')
    
    def compareFiles(self, topfile, leftfile):
        self.assert_(
            file_utils.fp_file_compare(
                'temptop.dat',
                os.path.join('mesh_data', topfile),
                1.e-10))
        self.assert_(
            file_utils.fp_file_compare(
                'templeft.dat',
                os.path.join('mesh_data', leftfile),
                1.e-10))
        file_utils.remove('temptop.dat')
        file_utils.remove('templeft.dat')
        outputdestination.forgetTextOutputStreams()

    @memorycheck.check("microstructure")
    def Adaptive(self):
        self.adaptive()
        self.fixBottom()
        self.floatTopEdge()
        self.initializeMin('top', 0)
        self.initialize()
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=1.5)
        self.compareFiles('td_float_top.dat', 'td_float_left.dat')

    @memorycheck.check("microstructure")
    def Adaptive_Pts(self):
        self.adaptive()
        self.fixBottom()
        self.floatTopPoints()
        self.initializeMin('top', 0)
        self.initialize()
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=1.5)
        self.compareFiles('td_float_top.dat', 'td_float_left.dat')

    @memorycheck.check("microstructure")
    def AdaptiveMax(self):
        self.adaptive()
        self.fixBottom()
        self.floatTopEdge()
        self.initializeMax('top', 0.1)
        self.initialize()
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=1.5)
        self.compareFiles('td_float_top.dat', 'td_float_left.dat')

    @memorycheck.check("microstructure")
    def AdaptiveAvg(self):
        self.adaptive()
        self.fixBottom()
        self.floatTopEdge()
        self.initializeAvg('top', 0.05)
        self.initialize()
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=1.5)
        self.compareFiles('td_float_top.dat', 'td_float_left.dat')

    @memorycheck.check("microstructure")
    def Adaptive_Intersect(self):
        self.adaptive()
        self.floatTopEdge()
        self.floatLeftEdge()
        self.initializeMin('top', 0.0)
        self.initializeMin('left', 0.1)
        self.initialize()
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=1.5)
        self.compareFiles('td_floatintersect_top.dat', 
                          'td_floatintersect_left.dat')

    @memorycheck.check("microstructure")
    def AdaptiveMaxMin_Intersect(self):
        self.adaptive()
        self.floatTopEdge()
        self.floatLeftEdge()
        self.initializeMax('top', 0.1)
        self.initializeMin('left', 0.1)
        self.initialize()
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=1.5)
        self.compareFiles('td_floatintersect_top.dat', 
                          'td_floatintersect_left.dat')

    @memorycheck.check("microstructure")
    def AdaptiveMaxMax_Intersect(self):
        self.adaptive()
        self.floatTopEdge()
        self.floatLeftEdge()
        self.initializeMax('top', 0.1)
        self.initializeMax('left', 0.2)
        self.initialize()
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=1.5)
        self.compareFiles('td_floatintersect_top.dat', 
                          'td_floatintersect_left.dat')

    @memorycheck.check("microstructure")
    def Conflict(self):
        from ooflib.SWIG.engine import ooferror2
        OOF.Help.No_Warnings(True)
        self.adaptive()
        self.floatTopEdge()
        self.floatLeftEdge()
        self.initializeMin('top', 0.0)
        self.initializeMin('left', 0.0)
        self.assertRaises(ooferror2.ErrWarning, self.initialize)
        OOF.Help.No_Warnings(False)
        outputdestination.forgetTextOutputStreams()


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def run_tests():

    test_set = [
        OOF_TimeDependentDirichlet("QuasiStatic"),
        OOF_TimeDependentDirichlet("Adaptive"),
        OOF_TimeDependentDirichlet("QuasiStatic_Pts"),
        OOF_TimeDependentDirichlet("Adaptive_Pts"),
        OOF_TimeDependentFloat("Adaptive"),
        OOF_TimeDependentFloat("AdaptiveMax"),
        OOF_TimeDependentFloat("AdaptiveAvg"),
        OOF_TimeDependentFloat("Adaptive_Pts"),
        OOF_TimeDependentFloat("Adaptive_Intersect"),
        OOF_TimeDependentFloat("AdaptiveMaxMin_Intersect"),
        OOF_TimeDependentFloat("AdaptiveMaxMax_Intersect"),
        OOF_TimeDependentFloat("Conflict")
        ]

    logan = unittest.TextTestRunner()

    for t in test_set:
        print >> sys.stderr, "\n *** Running test: %s\n" % t.id()
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
