# -*- python -*-
# $RCSfile: pyproperty_test.py,v $
# $Revision: 1.2 $
# $Author: langer $
# $Date: 2011/01/26 22:04:02 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import unittest, os
import memorycheck
from UTILS import file_utils
#file_utils.generate = True


class OOF_PyProperties(unittest.TestCase):
    def setUp(self):
        global outputdestination
        from ooflib.engine.IO import outputdestination
        OOF.Microstructure.New(
            name='microstructure',
            width=1.0, height=1.0,
            width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(
            name='material', material_type='bulk')
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
        OOF.Mesh.New(
            name='mesh',
            skeleton='microstructure:skeleton',
            element_types=['D2_2', 'T3_3', 'Q4_4'])
                  
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=BasicSolverMode(
                time_stepper=BasicStaticDriver(),
                matrix_method=BasicIterative(
                    tolerance=1e-13,max_iterations=1000)))

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    @memorycheck.check('microstructure')
    def HeatConductivity(self):
        OOF.Material.Add_property(
            name='material',
            property='Thermal:Conductivity:PyIsotropic')
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
        OOF.Mesh.Boundary_Conditions.New(
            name='bc',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=0.0),
                boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<2>', 
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=1),
                boundary='bottomleft'))
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=BasicSolverMode(
                time_stepper=BasicStaticDriver(),
                matrix_method=BasicIterative(
                    tolerance=1e-13,max_iterations=1000)))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Temperature, initializer=ConstScalarFieldInit(value=0.0))
        self.heatCondTest()

        # Repeat the calculation with the C++ Heat Conductivity Property.
        OOF.Property.Parametrize.Thermal.Conductivity.Isotropic(
            kappa=1.0)
        OOF.Material.Add_property(
            name='material',
            property='Thermal:Conductivity:Isotropic')
        OOF.Material.Remove_property(
            name='material',
            property='Thermal:Conductivity:PyIsotropic')
        self.heatCondTest()

        OOF.Material.Delete(name="material")


    def heatCondTest(self):
        OOF.Mesh.Apply_Field_Initializers(
            mesh='microstructure:skeleton:mesh')
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=0.0)
        OOF.Mesh.Analyze.Direct_Output(
            mesh='microstructure:skeleton:mesh',
            time=latest, 
            data=getOutput('Field:Value',field=Temperature),
            domain=EntireMesh(),
            sampling=GridSampleSet(
                x_points=10,y_points=10,show_x=True,show_y=True),
            destination=OutputStream(filename='pyprop.out',mode='w'))
        outputdestination.forgetTextOutputStreams()
        self.assert_(file_utils.fp_file_compare(
                'pyprop.out',
                os.path.join('mesh_data', 'pyheatcond.out'),
                1.e-6))
        file_utils.remove('pyprop.out')

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    @memorycheck.check('microstructure')
    def Elasticity(self):
        OOF.Material.Add_property(
            name='material',
            property='Mechanical:Elasticity:PyIsotropic')
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
                field=Displacement,field_component='y',
                equation=Force_Balance,eqn_component='y',
                profile=ConstantProfile(value=0.1),
                boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<2>', 
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Displacement,field_component='y',
                equation=Force_Balance,eqn_component='y',
                profile=ConstantProfile(value=0),
                boundary='bottom'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', 
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Displacement,field_component='x',
                equation=Force_Balance,eqn_component='x',
                profile=ConstantProfile(value=0),
                boundary='bottom'))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Displacement,
            initializer=ConstTwoVectorFieldInit(cx=0.0,cy=0.0))
        self.elasticityTest()

        OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic(
            cijkl=IsotropicRank4TensorCij(c11=1.0,c12=0.5))
        OOF.Material.Add_property(
            name='material', 
            property='Mechanical:Elasticity:Isotropic')
        OOF.Material.Remove_property(
            name='material', 
            property='Mechanical:Elasticity:PyIsotropic')
        self.elasticityTest()

        OOF.Material.Delete(name="material")

    def elasticityTest(self):
        OOF.Mesh.Apply_Field_Initializers(
            mesh='microstructure:skeleton:mesh')
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=0.0)
        OOF.Mesh.Analyze.Direct_Output(
            mesh='microstructure:skeleton:mesh',
            time=latest, 
            data=getOutput('Field:Value',field=Displacement),
            domain=EntireMesh(),
            sampling=GridSampleSet(
                x_points=10,y_points=10,show_x=True,show_y=True),
            destination=OutputStream(filename='pyprop.out',mode='w'))
        outputdestination.forgetTextOutputStreams()
        self.assert_(file_utils.fp_file_compare(
                'pyprop.out',
                os.path.join('mesh_data', 'pyelasticity.out'),
                1.e-6))
        file_utils.remove('pyprop.out')

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    @memorycheck.check('microstructure')
    def StressFreeStrain(self):
        OOF.Material.Add_property(
            name='material', 
            property='Mechanical:StressFreeStrain:PyIsotropic')
        OOF.Material.Add_property(
            name='material', 
            property='Mechanical:Elasticity:Isotropic')
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
        self.stressFreeStrainTest()

        OOF.Property.Parametrize.Mechanical.StressFreeStrain.Isotropic(
            epsilon0=0.1)
        OOF.Material.Add_property(
            name='material', 
            property='Mechanical:StressFreeStrain:Isotropic')
        OOF.Material.Remove_property(
            name='material', 
            property='Mechanical:StressFreeStrain:PyIsotropic')
        self.stressFreeStrainTest()

        OOF.Material.Delete(name="material")

    def stressFreeStrainTest(self):
        OOF.Mesh.Apply_Field_Initializers(
            mesh='microstructure:skeleton:mesh')
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=0.0)
        OOF.Mesh.Analyze.Direct_Output(
            mesh='microstructure:skeleton:mesh',
            time=latest, 
            data=getOutput('Field:Value',field=Displacement),
            domain=EntireMesh(),
            sampling=GridSampleSet(
                x_points=10,y_points=10,show_x=True,show_y=True),
            destination=OutputStream(filename='pyprop.out',mode='w'))
        outputdestination.forgetTextOutputStreams()
        self.assert_(file_utils.fp_file_compare(
                'pyprop.out',
                os.path.join('mesh_data', 'pystressfreestrain.out'),
                1.e-6))
        file_utils.remove('pyprop.out')


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def run_tests():
    
    test_set = [OOF_PyProperties("HeatConductivity"),
                OOF_PyProperties("Elasticity"),
                OOF_PyProperties("StressFreeStrain")]

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

