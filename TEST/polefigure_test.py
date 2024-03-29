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
reference_file = file_utils.reference_file
pdf_compare = file_utils.pdf_compare
file_utils.generate = False

class OOF_PoleFigureTest(unittest.TestCase):
    def setUp(self):
        global colormap
        from ooflib.common.IO import colormap
    def tearDown(self):
        OOF.Material.Delete(name='material')

    def createFromMap(self, filename):
        # Create a Microstructure from an orientation map file.
        OOF.Microstructure.Create_From_OrientationMap_File(
            filename=reference_file('polefigure_data', filename),
            reader=GenericReader(
                comment_character='#',
                separator=WhiteSpaceSeparator(),
                angle_column=1,
                angle_type=Bunge,
                angle_units='Radians',
                angle_offset=0.0,
                xy_column=4,
                scale_factor=1.0,
                flip_x=False,flip_y=True,
                groups=[('group_%s', 11)]),
            microstructure='microstructure')
        OOF.Material.New(name='material', material_type='bulk')
        OOF.Material.Add_property(name='material', property='OrientationMap')
        OOF.Material.Assign(
            material='material', microstructure='microstructure', pixels=every)

    def createFromProperty(self):
        # Create a pole figure from an Orientation Property.  These
        # should produce the same output as FromMap.
        OOF.Microstructure.New(
            name='microstructure',
            width=1.0, height=1.0,
            width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(name='material', material_type='bulk')
        OOF.Material.Assign(
            material='material',
            microstructure='microstructure',
            pixels=every)
        OOF.Material.Add_property(name='material', property='Orientation')
        OOF.Property.Parametrize.Orientation(
            angles=Abg(alpha=0,beta=0,gamma=0))

    def checkPoleFigures(self, prefix, nBins=None, colorMap=None):
        nBins = nBins or 30
        colorMap = colorMap or colormap.GrayMap()

        OOF.OrientationMap.Pole_Figure(
            microstructure='microstructure', 
            pixels=every, 
            symmetry='Cubic',
            pole=AngleDirection(theta=0,phi=0),
            nBins=nBins,
            min=0, max=automatic,
            colormap=colorMap,
            size=500,
            filename='test.pdf', overwrite=True)
        # If pdf_compare fails after generating new reference pdf
        # files, make sure that the time zone is set to "Etc/UTC"
        # before generating them.  See the comment in regression.py.
        self.assertTrue(pdf_compare('test.pdf', os.path.join('polefigure_data',
                                                             prefix+'_0.pdf')))
        file_utils.remove("test.pdf")

        OOF.OrientationMap.Pole_Figure(
            microstructure='microstructure', 
            pixels=every, 
            symmetry='Cubic',
            pole=AngleDirection(theta=45,phi=0),
            nBins=nBins,
            min=0, max=automatic,
            colormap=colorMap,
            size=500,
            filename='test.pdf', overwrite=True)
        self.assertTrue(pdf_compare('test.pdf', os.path.join('polefigure_data',
                                                          prefix+'_1.pdf')))
        file_utils.remove("test.pdf")

        OOF.OrientationMap.Pole_Figure(
            microstructure='microstructure', 
            pixels=every, 
            symmetry='Orthorhombic',
            pole=AngleDirection(theta=45,phi=0),
            nBins=nBins,
            min=0, max=automatic,
            colormap=colorMap,
            size=500,
            filename='test.pdf', overwrite=True)
        self.assertTrue(pdf_compare('test.pdf', os.path.join('polefigure_data',
                                                          prefix+'_2.pdf')))
        file_utils.remove('test.pdf') 

        OOF.OrientationMap.Pole_Figure(
            microstructure='microstructure', 
            pixels=every, 
            symmetry='Orthorhombic',
            pole=AngleDirection(theta=45,phi=30),
            nBins=nBins,
            min=0, max=automatic,
            colormap=colorMap,
            size=500,
            filename='test.pdf', overwrite=True)
        self.assertTrue(pdf_compare('test.pdf', os.path.join('polefigure_data',
                                                          prefix+'_3.pdf')))
        file_utils.remove('test.pdf')
        
    @memorycheck.check("microstructure")
    def FromMap0(self):
        # Create a pole figure from an orientation map.
        self.createFromMap('orientmap0.tsl')
        self.checkPoleFigures('orientmap0')

    @memorycheck.check("microstructure")
    def FromProperty0(self):
        self.createFromProperty()
        self.checkPoleFigures('orientmap0')

    @memorycheck.check("microstructure")
    def FromMap1(self):
        # Create a pole figure from an orientation map.
        # orientmap1.tsl was created by tslsimulator.py with the
        # arguments: 
        #       -x 100 -y 100 -m "TwoAngles(0, 0, 0, 10, 10, 10)"
        # In order to make a version of this test that uses a
        # Orientation Property instead of an OrientationMap, it'd be
        # necessary to create a corresponding Microstructure, which is
        # probably not worth the trouble.
        self.createFromMap('orientmap1.tsl')
        self.checkPoleFigures('orientmap1')

    @memorycheck.check("microstructure")
    def FromMap2(self):
        # orientmap2.tsl was created by tslsimulator.py with the
        # arguments: -x 100 -y 100 -m "Gauss(0, 45, 0, 10)"
        self.createFromMap('orientmap2.tsl')
        self.checkPoleFigures('orientmap2', nBins=60,
                              colorMap=colormap.SpectralMap())

## All tests are commented out because pdf generation is not portable.
## Pdfs generated on different systems are different, and not just in
## their time stamp.  TODO: Figure out how to compare pdfs portably.
# test_set = [
#     OOF_PoleFigureTest("FromMap0"),
#     OOF_PoleFigureTest("FromProperty0"),
#     OOF_PoleFigureTest("FromMap1"),
#     OOF_PoleFigureTest("FromMap2")
# ]

test_set = []
