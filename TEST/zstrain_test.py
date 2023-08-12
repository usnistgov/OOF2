# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import unittest, os
from . import memorycheck
from .UTILS import file_utils
#file_utils.generate = True


# Test of the ZStrain property, which allows for plane strain
# calculations with the planar strain different from zero.  Uses an
# example triclinic Cijkl and small rotation, the idea being that
# this is a low-symmetry example which will be sensitive to indexing
# faults or sense errors.

class OOF_ZStrain(unittest.TestCase):
    def setUp(self):
        OOF.Microstructure.New(
            name='microstructure', width=1.0, height=1.0,
            width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(name='artest', material_type='bulk')
        OOF.Property.Copy(
            property='Mechanical:Elasticity:Anisotropic:Triclinic',
            new_name='arelastic')
        OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Triclinic.arelastic(cijkl=TriclinicRank4TensorCij(
            c11=1.0, c12=0.3, c13=0.5, c14=0.0, c15=0.0, c16=0.0,
            c22=1.1, c23=0.2, c24=0.0, c25=0.0, c26=0.0, c33=1.2,
            c34=0.0, c35=0.0, c36=0.0, c44=0.25, c45=0.0, c46=0.0,
            c55=0.22, c56=0.0, c66=0.2))
        OOF.Material.Add_property(
            name='artest',
            property='Mechanical:Elasticity:Anisotropic:Triclinic:arelastic')
        OOF.Property.Copy(property='Orientation', new_name='arorientation')
        OOF.Property.Parametrize.Orientation.arorientation(
            angles=Abg(alpha=0.1,beta=0.2,gamma=0))
        OOF.Material.Add_property(name='artest',
                                  property='Orientation:arorientation')
        OOF.Property.Copy(property='Mechanical:ZStrain', new_name='arz')
        OOF.Property.Parametrize.Mechanical.ZStrain.arz(ezz=0.01)
        OOF.Material.Add_property(name='artest',
                                  property='Mechanical:ZStrain:arz')
        OOF.Skeleton.New(name='skeleton', microstructure='microstructure',
                         x_elements=4, y_elements=4,
                         skeleton_geometry=QuadSkeleton(
                             left_right_periodicity=False,
                             top_bottom_periodicity=False))
        OOF.Mesh.New(name='mesh', skeleton='microstructure:skeleton',
                     element_types=['D2_2', 'T3_3', 'Q4_4'])
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Mesh.Field.In_Plane(mesh='microstructure:skeleton:mesh',
                                field=Displacement)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Force_Balance)
        OOF.Mesh.Boundary_Conditions.New(
            name='bc', mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(field=Displacement,
                                  field_component='x',
                                  equation=Force_Balance,
                                  eqn_component='x',
                                  profile=ConstantProfile(value=0.0),
                                  boundary='left'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<2>', mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(field=Displacement,
                                  field_component='y',
                                  equation=Force_Balance,eqn_component='y',
                                  profile=ConstantProfile(value=0.0),
                                  boundary='bottomleft'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>', mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(field=Displacement,
                                  field_component='x',
                                  equation=Force_Balance,eqn_component='x',
                                  profile=ConstantProfile(value=0.01),
                                  boundary='right'))
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=BasicSolverMode(time_stepper=BasicStaticDriver(),
                                        matrix_method=BasicIterative(tolerance=1e-13,max_iterations=1000)))
        OOF.Material.Assign(material='artest',
                            microstructure='microstructure', pixels=every)

    @memorycheck.check("microstructure")
    def Triclinic_ZStrain(self):
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh',endtime=0.0)
        OOF.Mesh.Analyze.Direct_Output(
            mesh='microstructure:skeleton:mesh',time=latest,
            data=getOutput('Strain:Value',type=ElasticStrain()),
            domain=SinglePoint(point=Point(0.1,0.1)),
            sampling=DiscretePointSampleSet(show_x=True,show_y=True),
            destination=OutputStream(filename='artest.dat',mode='w'))
        OOF.Mesh.Analyze.Direct_Output(
            mesh='microstructure:skeleton:mesh', time=latest,
            data=getOutput('Flux:Value',flux=Stress),
            domain=SinglePoint(point=Point(0.1,0.1)),
            sampling=DiscretePointSampleSet(show_x=True,show_y=True),
            destination=OutputStream(filename='artest.dat',mode='a'))
        self.assertTrue(file_utils.fp_file_compare(
            'artest.dat',
            os.path.join('mesh_data','archeck.dat'),
            1.e-8))
        file_utils.remove('artest.dat')
        
    def tearDown(self):
        OOF.Material.Delete(name='artest')
        OOF.Property.Delete(
            property='Mechanical:Elasticity:Anisotropic:Triclinic:arelastic')
        OOF.Property.Delete(
            property='Mechanical:ZStrain:arz')
        OOF.Property.Delete(
            property='Orientation:arorientation')

        
test_set = [OOF_ZStrain("Triclinic_ZStrain")]
