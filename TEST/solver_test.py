# -*- python -*-
# $RCSfile: solver_test.py,v $
# $Revision: 1.73 $
# $Author: langer $
# $Date: 2011/07/11 15:19:18 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

import unittest, os
import memorycheck
import math
from UTILS import file_utils
reference_file = file_utils.reference_file
# file_utils.generate = True

class SaveableMeshTest(unittest.TestCase):
    def saveAndLoad(self, filename):
        # Save the mesh in ascii format, and compare with a reference file.
        asciifilename = filename + suffix + "-ascii.dat"
        OOF.File.Save.Mesh(
            filename=asciifilename, mode='w', format='ascii',
            mesh = 'microstructure:skeleton:mesh')
        self.assert_(file_utils.fp_file_compare(
                asciifilename,
                os.path.join('mesh_data', asciifilename),
                1.e-6))
        # Reload the mesh and compare it to the original.  In order to
        # prevent conflicts when reloading, rename the original
        # Microstructure before reloading the saved mesh.
        OOF.Microstructure.Rename(
            microstructure='microstructure', name='original')
        OOF.File.Load.Data(filename=reference_file('mesh_data', asciifilename))
        from ooflib.engine import mesh
        reloaded = mesh.meshes['microstructure:skeleton:mesh']
        original = mesh.meshes['original:skeleton:mesh']
        self.assertEqual(reloaded.compare(original, 1.e-6), 0)
        
        # Delete the reloaded Microstructure, and restore the name of
        # the original Microstructure.
        del reloaded
        OOF.Microstructure.Delete(microstructure='microstructure')
        OOF.Microstructure.Rename(
            microstructure='original', name='microstructure')

        # Save the mesh in binary format, reload it, and compare with the
        # original.
        binaryfilename = filename + suffix + "-binary.dat"
        OOF.File.Save.Mesh(
            filename=binaryfilename, mode='w', format='binary',
            mesh='microstructure:skeleton:mesh')
        OOF.Microstructure.Rename(
            microstructure='microstructure', name='original')
        OOF.File.Load.Data(filename=binaryfilename)
        reloaded = mesh.meshes['microstructure:skeleton:mesh']
        original = mesh.meshes['original:skeleton:mesh']
        self.assertEqual(reloaded.compare(original, 1.e-6), 0)
        print >> sys.stderr, "Successful binary mesh file comparison."
        file_utils.remove(asciifilename)
        file_utils.remove(binaryfilename)
        OOF.Microstructure.Delete(microstructure='original')
    

class OOF_StaticIsoElastic(SaveableMeshTest):
    def setUp(self):
        global mesh, femesh, cskeleton, cmicrostructure
        from ooflib.engine import mesh
        from ooflib.SWIG.engine import femesh
        from ooflib.SWIG.engine import cskeleton
        from ooflib.SWIG.common import cmicrostructure
        OOF.File.Load.Data(filename=reference_file("mesh_data", "solveable"))

    def tearDown(self):
        OOF.Property.Delete(property='Color:bloo')
        OOF.Property.Delete(property='Color:wred')
        OOF.Property.Delete(property='Mechanical:Elasticity:Isotropic:soft')
        OOF.Property.Delete(property='Mechanical:Elasticity:Isotropic:stiff')
        OOF.Material.Delete(name="bricks")
        OOF.Material.Delete(name="mortar")

    @memorycheck.check("solve_test")
    def Null(self):             # Establish baseline for memory leak tests
        pass

    @memorycheck.check("solve_test")
    def Solve(self):
        global solution
        make_solution()
        OOF.Subproblem.Set_Solver(
            subproblem='solve_test:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver= ConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)))

        OOF.Mesh.Solve(mesh='solve_test:skeleton:mesh', endtime=0.0)


        # Then look for evidence that it worked.  Direct evidence
        # would be that the solution exists and is right, so poll
        # DOFs.
        from ooflib.engine import mesh
        msh_obj = mesh.meshes["solve_test:skeleton:mesh"].getObject()
        for fn in msh_obj.funcnode_iterator():
            delta = fn.displaced_position(msh_obj)-solution[fn.index()]
            self.assertAlmostEqual(delta**2, 0.0, 6)
        del msh_obj


# The expected solution, to some number of digits...
solution = {}

def make_solution():
    global solution
    from ooflib.common import primitives
    Point = primitives.Point
    solution = {
        0 : Point(0,0),
        1 : Point(15.3456,0),
        2 : Point(29.3792,0),
        3 : Point(44.4774,0),
        4 : Point(53.7066,0),
        5 : Point(79.1839,0),
        6 : Point(91.3082,0),
        7 : Point(103.883,0),
        8 : Point(120.872,0),
        9 : Point(133.066,0),
        10 : Point(150,0),
        11 : Point(1.02728,16.4524),
        12 : Point(15.6609,16.2508),
        13 : Point(30.4716,16.2151),
        14 : Point(43.6244,15.7484),
        15 : Point(60.3963,16.754),
        16 : Point(75.0237,17.5751),
        17 : Point(91.5844,14.1872),
        18 : Point(102.949,15.5236),
        19 : Point(120.474,16.6512),
        20 : Point(132.625,16.241),
        21 : Point(148.972,16.5332),
        22 : Point(1.52051,30.0604),
        23 : Point(16.2071,33.3001),
        24 : Point(30.8991,30.4828),
        25 : Point(45.6079,33.4832),
        26 : Point(60.7761,33.9675),
        27 : Point(74.0779,37.4084),
        28 : Point(83.8242,33.2106),
        29 : Point(104.411,30.1855),
        30 : Point(119.091,29.37),
        31 : Point(134.16,33.7042),
        32 : Point(148.34,30.0331),
        33 : Point(2.19445,50.2799),
        34 : Point(16.7242,50.7027),
        35 : Point(31.2362,51.7433),
        36 : Point(45.8163,51.7643),
        37 : Point(60.2318,51.9829),
        38 : Point(74.457,49.75),
        39 : Point(88.8261,50.7005),
        40 : Point(104.913,50.3512),
        41 : Point(118.196,49.2456),
        42 : Point(132.525,51.4415),
        43 : Point(147.79,53.4387),
        44 : Point(2.05798,67.5431),
        45 : Point(14.8366,67.3739),
        46 : Point(31.2821,65.9517),
        47 : Point(46.1495,65.8259),
        48 : Point(60.7822,69.0642),
        49 : Point(75.7266,66.6852),
        50 : Point(93.3626,65.9692),
        51 : Point(103.441,67.0739),
        52 : Point(118.719,69.3317),
        53 : Point(135.207,65.789),
        54 : Point(147.787,64.6342),
        55 : Point(1.99675,80.9863),
        56 : Point(16.7526,81.8107),
        57 : Point(29.1946,81.378),
        58 : Point(48.1439,82.7936),
        59 : Point(60.4777,82.3962),
        60 : Point(73.5941,82.7034),
        61 : Point(92.2705,81.7089),
        62 : Point(106.38,80.4622),
        63 : Point(119.175,81.4804),
        64 : Point(131.641,82.1859),
        65 : Point(147.781,85.4699),
        66 : Point(1.88776,95.9814),
        67 : Point(17.2527,96.4019),
        68 : Point(30.1717,99.5727),
        69 : Point(49.4866,99.4899),
        70 : Point(59.6651,97.3678),
        71 : Point(74.9832,98.6638),
        72 : Point(88.8785,98.9017),
        73 : Point(103.448,98.0985),
        74 : Point(119.347,96.7856),
        75 : Point(133.161,98.7585),
        76 : Point(147.765,96.1162),
        77 : Point(2.24623,117.006),
        78 : Point(17.6256,113.88),
        79 : Point(30.4922,111.41),
        80 : Point(46.5759,121.402),
        81 : Point(59.963,115.714),
        82 : Point(74.8293,121.31),
        83 : Point(89.4507,116.556),
        84 : Point(104.341,116.026),
        85 : Point(119.383,120.032),
        86 : Point(133.368,115.822),
        87 : Point(147.875,117.23),
        88 : Point(1.75494,134.545),
        89 : Point(16.3664,132.979),
        90 : Point(31.4934,134.875),
        91 : Point(44.9669,133.591),
        92 : Point(59.5566,133.689),
        93 : Point(75.214,132.016),
        94 : Point(90.0049,132.202),
        95 : Point(106.91,133.193),
        96 : Point(120.19,132.849),
        97 : Point(134.102,133.763),
        98 : Point(148.42,132.849),
        99 : Point(1.22331,147.769),
        100 : Point(12.4483,148.211),
        101 : Point(30.0218,148.003),
        102 : Point(43.8137,151.562),
        103 : Point(59.2445,145.003),
        104 : Point(74.5036,144.654),
        105 : Point(89.1165,148.237),
        106 : Point(105.194,148.662),
        107 : Point(121.625,148.048),
        108 : Point(134.024,148.261),
        109 : Point(148.959,148.564),
        110 : Point(0,165),
        111 : Point(10.9222,165),
        112 : Point(29.495,165),
        113 : Point(43.6219,165),
        114 : Point(59.5322,165),
        115 : Point(76.1102,165),
        116 : Point(94.2732,165),
        117 : Point(109.84,165),
        118 : Point(122.217,165),
        119 : Point(134.538,165),
        120 : Point(150,165),
        121 : Point(39.5967,0),
        122 : Point(45.9346,8.15438),
        123 : Point(38.3474,7.99599),
        124 : Point(47.778,0),
        125 : Point(56.8694,8.69266),
        126 : Point(53.3768,15.0907),
        127 : Point(50.1103,7.79032),
        128 : Point(64.762,0),
        129 : Point(75.5827,9.80986),
        130 : Point(70.2517,15.2455),
        131 : Point(67.4264,8.71299),
        132 : Point(81.2923,18.4121),
        133 : Point(83.3039,8.55795),
        134 : Point(112.459,0),
        135 : Point(111.804,15.879),
        136 : Point(142.019,0),
        137 : Point(141.709,16.397),
        138 : Point(15.6663,27.6216),
        139 : Point(10.4221,32.9438),
        140 : Point(10.031,25.5778),
        141 : Point(23.6054,33.6652),
        142 : Point(23.051,25.7457),
        143 : Point(45.0869,25.6473),
        144 : Point(38.5011,33.49),
        145 : Point(38.5876,24.2525),
        146 : Point(64.2572,24.7054),
        147 : Point(53.0029,34.6801),
        148 : Point(55.2326,25.1952),
        149 : Point(75.4335,24.5275),
        150 : Point(66.2885,34.6352),
        151 : Point(69.1308,28.7841),
        152 : Point(89.5627,25.2533),
        153 : Point(79.9291,33.9315),
        154 : Point(81.9201,29.9363),
        155 : Point(95.3881,31.6527),
        156 : Point(97.0168,23.9474),
        157 : Point(110.748,29.7889),
        158 : Point(133.722,24.5659),
        159 : Point(125.218,34.8498),
        160 : Point(127.521,23.6718),
        161 : Point(148.735,23.0719),
        162 : Point(142.579,30.0657),
        163 : Point(141.278,23.7942),
        164 : Point(16.4,40.2806),
        165 : Point(9.72393,49.4974),
        166 : Point(1.96095,39.5143),
        167 : Point(9.15347,39.2943),
        168 : Point(30.9716,41.3014),
        169 : Point(23.9819,51.7764),
        170 : Point(23.9692,40.2717),
        171 : Point(45.5963,41.3319),
        172 : Point(38.5148,51.7425),
        173 : Point(38.279,41.304),
        174 : Point(60.2841,42.568),
        175 : Point(52.87,52.1594),
        176 : Point(52.9197,41.3792),
        177 : Point(76.7987,42.5638),
        178 : Point(67.822,52.8658),
        179 : Point(67.6439,42.5751),
        180 : Point(90.0995,42.2706),
        181 : Point(83.1881,51.03),
        182 : Point(81.6933,42.1624),
        183 : Point(105.548,40.4896),
        184 : Point(96.5672,54.1836),
        185 : Point(99.654,43.1961),
        186 : Point(119.735,37.9323),
        187 : Point(111.327,50.7031),
        188 : Point(111.728,39.7193),
        189 : Point(133.919,44.9828),
        190 : Point(127.381,50.6295),
        191 : Point(126.159,46.2146),
        192 : Point(147.727,40.6607),
        193 : Point(140.023,49.9206),
        194 : Point(141.106,41.8387),
        195 : Point(16.133,57.9615),
        196 : Point(8.89851,57.7089),
        197 : Point(31.2716,57.786),
        198 : Point(24.9079,65.8988),
        199 : Point(23.9937,57.7987),
        200 : Point(45.4739,58.3905),
        201 : Point(38.571,65.9605),
        202 : Point(38.5526,57.785),
        203 : Point(60.2874,58.3558),
        204 : Point(52.4529,65.8977),
        205 : Point(53.0394,58.1728),
        206 : Point(74.5979,57.1723),
        207 : Point(68.5952,66.0119),
        208 : Point(67.1802,59.2531),
        209 : Point(92.8165,58.6084),
        210 : Point(83.8933,66.6782),
        211 : Point(85.3598,57.4013),
        212 : Point(103.588,58.1025),
        213 : Point(97.6893,64.9933),
        214 : Point(97.7566,59.7746),
        215 : Point(118.045,57.0093),
        216 : Point(110.804,66.86),
        217 : Point(112.468,58.1711),
        218 : Point(133.216,56.8574),
        219 : Point(125.867,66.0993),
        220 : Point(125.977,58.0998),
        221 : Point(140.523,57.7308),
        222 : Point(31.8145,73.85),
        223 : Point(23.9717,74.0992),
        224 : Point(45.8775,73.7822),
        225 : Point(39.1212,84.3652),
        226 : Point(38.7251,73.7068),
        227 : Point(52.477,74.6887),
        228 : Point(76.3496,73.6233),
        229 : Point(68.1102,74.5697),
        230 : Point(93.3797,74.2518),
        231 : Point(85.011,81.9347),
        232 : Point(83.4839,73.2173),
        233 : Point(103.685,73.2667),
        234 : Point(97.5085,81.7252),
        235 : Point(97.5307,75.4813),
        236 : Point(111.164,73.3295),
        237 : Point(135.236,73.3525),
        238 : Point(125.789,72.8491),
        239 : Point(147.783,74.674),
        240 : Point(8.20569,98.409),
        241 : Point(1.91709,91.1306),
        242 : Point(8.43269,88.5794),
        243 : Point(38.2234,97.2791),
        244 : Point(74.5727,91.8969),
        245 : Point(68.3574,100.918),
        246 : Point(67.8065,90.6077),
        247 : Point(88.6435,91.1772),
        248 : Point(84.9046,98.9998),
        249 : Point(84.8486,90.7584),
        250 : Point(102.459,90.1602),
        251 : Point(93.4556,99.0457),
        252 : Point(94.3286,90.5665),
        253 : Point(111.065,98.2107),
        254 : Point(111.873,89.9417),
        255 : Point(132.817,92.1574),
        256 : Point(125.989,99.1315),
        257 : Point(126.781,90.8571),
        258 : Point(140.017,98.8549),
        259 : Point(140.539,92.0804),
        260 : Point(15.0287,106.402),
        261 : Point(8.40523,114.296),
        262 : Point(2.3649,109.518),
        263 : Point(9.27901,102.027),
        264 : Point(22.6791,114.327),
        265 : Point(22.6228,107.201),
        266 : Point(39.5459,112.898),
        267 : Point(60.5346,107.478),
        268 : Point(53.3171,117.272),
        269 : Point(54.2262,104.831),
        270 : Point(74.7058,109.246),
        271 : Point(67.186,112.315),
        272 : Point(67.7973,105.509),
        273 : Point(90.9312,106.958),
        274 : Point(81.4102,117.514),
        275 : Point(84.3106,108.032),
        276 : Point(104.198,105.547),
        277 : Point(97.0138,116.075),
        278 : Point(96.2387,105.82),
        279 : Point(118.7,105.428),
        280 : Point(111.666,116.002),
        281 : Point(111.432,105.473),
        282 : Point(133.226,105.6),
        283 : Point(126.794,115.339),
        284 : Point(125.963,105.4),
        285 : Point(147.574,106.727),
        286 : Point(139.841,116.805),
        287 : Point(140.767,105.431),
        288 : Point(17.1803,124.891),
        289 : Point(9.93468,129.004),
        290 : Point(2.11943,123.035),
        291 : Point(10.9028,119.233),
        292 : Point(31.9623,122.805),
        293 : Point(22.589,131.043),
        294 : Point(24.9115,120.131),
        295 : Point(45.7518,126.407),
        296 : Point(36.8902,132.167),
        297 : Point(42.5213,123.989),
        298 : Point(61.1858,127.719),
        299 : Point(52.3798,134.339),
        300 : Point(53.5735,127.795),
        301 : Point(75.2042,126.876),
        302 : Point(66.7429,132.113),
        303 : Point(67.6962,124.291),
        304 : Point(90.0591,124.425),
        305 : Point(82.5053,132.496),
        306 : Point(81.7562,124.702),
        307 : Point(104.291,123.562),
        308 : Point(97.0838,132.372),
        309 : Point(97.6964,124.405),
        310 : Point(111.689,124.269),
        311 : Point(133.779,122.587),
        312 : Point(127.979,124.36),
        313 : Point(140.294,123.345),
        314 : Point(15.286,138.744),
        315 : Point(8.45871,139.741),
        316 : Point(31.9619,141.667),
        317 : Point(22.4461,156.63),
        318 : Point(22.1735,141.951),
        319 : Point(45.2828,140.095),
        320 : Point(38.5952,149.433),
        321 : Point(38.101,142.11),
        322 : Point(60.041,138.682),
        323 : Point(51.1775,152.985),
        324 : Point(52.5351,140.848),
        325 : Point(74.5153,139.482),
        326 : Point(67.2908,147.136),
        327 : Point(67.2998,138.69),
        328 : Point(89.9052,140.603),
        329 : Point(81.3357,146.637),
        330 : Point(82.5132,140.071),
        331 : Point(103.778,142.094),
        332 : Point(95.9196,150.642),
        333 : Point(97.1926,140.285),
        334 : Point(110.383,148.498),
        335 : Point(111.953,140.613),
        336 : Point(13.7456,158.646),
        337 : Point(7.71359,165),
        338 : Point(6.87261,157.146),
        339 : Point(33.9257,156.539),
        340 : Point(17.6892,165),
        341 : Point(22.379,156.692),
        342 : Point(44.8747,157.939),
        343 : Point(37.735,165),
        344 : Point(38.4635,156.332),
        345 : Point(59.9679,156.792),
        346 : Point(52.5661,165),
        347 : Point(52.426,159.325),
        348 : Point(74.7428,151.475),
        349 : Point(66.2683,165),
        350 : Point(67.8035,159.412),
        351 : Point(90.1436,156.794),
        352 : Point(85.7691,165),
        353 : Point(82.7241,154.369),
        354 : Point(104.195,155.532),
        355 : Point(102.857,165),
        356 : Point(97.4033,160.367),
        357 : Point(112.594,156.332)
        }

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## OOF_NonrectMixedBCStaticElastic is a full blown test of a lot of
## features.  It creates a microstructure by selecting pixels and
## assigning a Material to *some* of them, so the microstructure isn't
## rectangular.  It then solves a simple static elasticity problem
## with Dirichlet, Neumann, and Floating BCs all mixed together.

class OOF_NonrectMixedBCStaticElastic(SaveableMeshTest):
    @memorycheck.check("saved", "microstructure")
    def Solve(self):
        OOF.File.Load.Script(filename=reference_file("mesh_data", "eltest.log"))
        OOF.File.Load.Data(filename=reference_file("mesh_data", "eltest.mesh"))
        from ooflib.engine import mesh
        from ooflib.SWIG.engine import femesh
        from ooflib.SWIG.engine import cskeleton
        from ooflib.SWIG.common import cmicrostructure
        saved = mesh.meshes["saved:skeleton:mesh"]
        damned = mesh.meshes["microstructure:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-13), 0)

        # Check that re-solving the mesh works. This line isn't in
        # eltest.log because exceptions raised in scripts don't seem
        # to make the tests fail.  TODO: Fix that.
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=0.0)
        self.assertEqual(saved.compare(damned, 1.0e-13), 0)

    def tearDown(self):
        OOF.Material.Delete(name='materialx')
        OOF.Property.Delete(property='Mechanical:Elasticity:Isotropic:elastix')

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## Similar to OOF_NonrectMixedBCStaticElastic, but edits some boundary
## conditions and re-solves the system a few more times.
class OOF_NewBCNonrectMixedEtc(SaveableMeshTest):
    @memorycheck.check("saved2", "microstructure")
    def Solve(self):
        OOF.File.Load.Script(filename=reference_file("mesh_data", "eltest.log"))
        #Edit neumann and float boundary conditions and solve again (2x)
        OOF.Mesh.Boundary_Conditions.Edit(
            name='bc<5>', mesh='microstructure:skeleton:mesh',
            condition=NeumannBC(
                flux=Stress,
                profile=[ConstantProfile(value=0.0),
                         ConstantProfile(value=-0.04)],
                boundary='right',normal=True))
        OOF.Mesh.Boundary_Conditions.Edit(
            name='bc<6>', mesh='microstructure:skeleton:mesh',
            condition=FloatBC(field=Displacement,field_component='x',
                              equation=Force_Balance,eqn_component='x',
                              profile=ContinuumProfile(
            function='-(y-0.16)**2'),boundary='right'))
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=0.0)
        OOF.Mesh.Boundary_Conditions.Edit(
            name='bc<5>', mesh='microstructure:skeleton:mesh',
            condition=NeumannBC(
                flux=Stress,
                profile=[ConstantProfile(value=0.0),
                         ConstantProfile(value=-0.05)],
                boundary='right',normal=True))
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh', endtime=0.0)
        OOF.File.Load.Data(filename=reference_file("mesh_data", "eltest2.mesh"))
        from ooflib.engine import mesh
        saved = mesh.meshes["saved2:skeleton:mesh"]
        damned = mesh.meshes["microstructure:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-13), 0)
    def tearDown(self):
        # Delete stuff added by script.
        OOF.Material.Delete(name='materialx')
        OOF.Property.Delete(
            property='Mechanical:Elasticity:Isotropic:elastix')

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# OOF_AnisoRotation tests that an anisotropic property is rotated
# correctly by solving a thermal conductivity problem.  To regenerate
# the reference file for this test, change the first line
# mesh_data/anisotherm.log to "generate=True", load that file into
# oof2, and save the resulting mesh into mesh_data/anisotherm.mesh.

class OOF_AnisoRotation(SaveableMeshTest):
    @memorycheck.check("saved", "damned")
    def Solve(self):
        OOF.File.Load.Script(filename=reference_file("mesh_data",
                                                   "anisotherm.log"))
        OOF.File.Load.Data(filename=reference_file("mesh_data",
                                                 "anisotherm.mesh"))
        from ooflib.engine import mesh
        saved = mesh.meshes["saved:skeleton:mesh"]
        damned = mesh.meshes["damned:skeleton:mesh"]
        self.assertEqual(saved.compare(damned, 1.0e-13), 0)
    def tearDown(self):
        OOF.Material.Delete(name="materialx")
        OOF.Property.Delete(property='Orientation:unsure')
        OOF.Property.Delete(
            property='Thermal:Conductivity:Anisotropic:Monoclinic:mono')

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class OOF_Solver_SimplePiezo(SaveableMeshTest):
    @memorycheck.check("microstructure")
    def Solve(self):
        from ooflib.engine.IO import outputdestination
        OOF.Microstructure.New(
            name='microstructure',
            width=1.0, height=1.0, width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(
            name='material', material_type='bulk')
        OOF.Material.Assign(
            material='material', microstructure='microstructure', pixels=all)
        # Reset the default parameter values for Properties..  This
        # shouldn't be necessary if earlier tests clean up after
        # themselves properly.
        OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic(
            cijkl=IsotropicRank4TensorCij(c11=1.0,c12=0.5))
        OOF.Material.Add_property(
            name='material', property='Mechanical:Elasticity:Isotropic')
        OOF.Property.Parametrize.Electric.DielectricPermittivity.Isotropic(
            epsilon=1.0)
        OOF.Material.Add_property(
            name='material',
            property='Electric:DielectricPermittivity:Isotropic')
        OOF.Property.Parametrize.Couplings.PiezoElectricity.Cubic.Td(
            dijk=TdRank3Tensor(d14=1))
        OOF.Material.Add_property(
            name='material', property='Couplings:PiezoElectricity:Cubic:Td')
        OOF.Property.Parametrize.Orientation(
            angles=Abg(alpha=0,beta=0,gamma=0))
        OOF.Material.Add_property(
            name='material', property='Orientation')
        OOF.Skeleton.New(
            name='skeleton',
            microstructure='microstructure',
            x_elements=1, y_elements=1, 
            skeleton_geometry=QuadSkeleton(
                left_right_periodicity=False,top_bottom_periodicity=False))
        OOF.Mesh.New(
            name='mesh', 
            skeleton='microstructure:skeleton',
            element_types=['D2_2', 'T3_3', 'Q4_4'])
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Voltage)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Voltage)
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', field=Voltage)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Coulomb_Eqn)
        OOF.Mesh.Boundary_Conditions.New(
            name='bc',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Voltage,field_component='',
                equation=Coulomb_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='0',timeDerivative='0',timeDerivative2='0'),
                boundary='bottomleft'))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh', 
            field=Displacement,
            initializer=FuncTwoVectorFieldInit(fx='0.1*y',fy='0.1*x'))
        OOF.Mesh.Apply_Field_Initializers(mesh="microstructure:skeleton:mesh")
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=BasicSolverMode(
                time_stepper=BasicStaticDriver(),
                matrix_method=BasicIterative(tolerance=1e-13,
                                             max_iterations=1000)))
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.0)
        OOF.Mesh.Analyze.Average(
            mesh='microstructure:skeleton:mesh',
            data=getOutput('Flux:Value',flux=Total_Polarization),
            time=latest,
            domain=EntireMesh(),
            sampling=ElementSampleSet(order=automatic),
            destination=OutputStream(filename='test.dat', mode='w'))
        outputdestination.forgetTextOutputStreams()
        self.assert_(
            file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'piezopolar'+suffix+'.dat'),
                1.e-10))
        file_utils.remove('test.dat')
        OOF.Mesh.Analyze.Average(
            mesh='microstructure:skeleton:mesh',
            data=getOutput('Field:Value',field=Voltage),
            time=latest,
            domain=EntireMesh(),
            sampling=ElementSampleSet(order=automatic),
            destination=OutputStream(filename='test.dat', mode='w'))
        outputdestination.forgetTextOutputStreams()
        self.assert_(
            file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'piezovoltage'+suffix+'.dat'),
                1.e-10))
        file_utils.remove('test.dat')
        # Switch to in-plane polarization.
        OOF.Mesh.Field.Out_of_Plane(
            mesh='microstructure:skeleton:mesh',
            field=Voltage)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=InPlanePolarization)
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.0)
        OOF.Mesh.Analyze.Average(
            mesh='microstructure:skeleton:mesh',
            data=getOutput('Flux:Value',flux=Total_Polarization),
            time=latest,
            domain=EntireMesh(),
            sampling=ElementSampleSet(order=automatic),
            destination=OutputStream(filename='test.dat', mode='w'))
        outputdestination.forgetTextOutputStreams()
        self.assert_(
            file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'piezoplanepolar'+suffix+'.dat'),
                1.e-10))
        file_utils.remove('test.dat')
        OOF.Mesh.Analyze.Average(
            mesh='microstructure:skeleton:mesh',
            data=getOutput('Field:Value',field=Voltage),
            time=latest,
            domain=EntireMesh(),
            sampling=ElementSampleSet(order=automatic),
            destination=OutputStream(filename='test.dat', mode='w'))
        outputdestination.forgetTextOutputStreams()
        self.assert_(
            file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'piezoplanevoltage'+suffix+'.dat'),
                1.e-10))
        file_utils.remove('test.dat')
        OOF.Mesh.Analyze.Average(
            mesh='microstructure:skeleton:mesh',
            data=getOutput('Field:Value',field=Voltage_z), 
            time=latest,
            domain=EntireMesh(),
            sampling=ElementSampleSet(order=automatic),
            destination=OutputStream(filename='test.dat', mode='w'))
        outputdestination.forgetTextOutputStreams()
        self.assert_(
            file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'piezoplanevoltageZ'+suffix+'.dat'),
                1.e-10))
        file_utils.remove('test.dat')
    def tearDown(self):
        OOF.Material.Delete(name='material')

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Check that solving a static problem after a nonstatic problem on the
# same mesh works correctly.

class OOF_NonstaticThenStatic(SaveableMeshTest):
    @memorycheck.check("microstructure")
    def Solve(self):
        OOF.File.Load.Script(filename=reference_file("mesh_data",
                                                   "timenotime.log"))
        from ooflib.engine import mesh
        mesh0 = mesh.meshes["microstructure:skeleton:mesh"]
        mesh1 = mesh.meshes["microstructure:skeleton:mesh<2>"]
        self.assertEqual(mesh0.compare(mesh1, 1.0e-13), 0)
    def tearDown(self):
        OOF.Material.Delete(name='material')

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Check that a simple time dependent problem is solved correctly.  The
# 1x1 linear quad grid with isotropic elasticity (default parameters)
# has an oscillation period of 2*pi/sqrt(3).  This test runs the time
# evolution for one period and checks it against the exact solution of
# the discretized problem.

class OOF_1x1ElasticDynamic(SaveableMeshTest):
    def setUp(self):
        global outputdestination
        from ooflib.engine.IO import outputdestination
        OOF.File.LoadStartUp.Data(
            filename=reference_file('mesh_data', 'simplespring.mesh'))

    @memorycheck.check("microstructure")
    def Static(self):
        # OOF.Mesh.Set_Field_Initializer(
        #     mesh='microstructure:skeleton:mesh',
        #     field=Displacement,
        #     initializer=ConstTwoVectorFieldInit(cx=0, cy=0))
        # OOF.Mesh.Apply_Field_Initializers_at_Time(
        #     mesh='microstructure:skeleton:mesh', time=0.0)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=StaticDriver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.0)
        # Check that all displacements are zero.
        from ooflib.engine import mesh
        msh_obj = mesh.meshes['microstructure:skeleton:mesh'].getObject()
        for fn in msh_obj.funcnode_iterator():
            dispx = Displacement.value(msh_obj, fn, 0)
            dispy = Displacement.value(msh_obj, fn, 1)
            rr = dispx*dispx + dispy*dispy
            self.assertAlmostEqual(rr, 0.0, 6)

    @memorycheck.check("microstructure")
    def Dynamic(self):
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name=AutomaticName('Average Displacement on right'),
            output=BoundaryAnalysis(
                operation=AverageField(field=Displacement),boundary='right'))
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('Average Displacement on right'),
            scheduletype=AbsoluteOutputSchedule(),
            schedule=Periodic(delay=0.0,interval=0.01*shortening))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('Average Displacement on right'),
            destination=OutputStream(filename='springtest.out',mode='w'))
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                nonlinear_solver=NoNonlinearSolver(),
                time_stepper=AdaptiveDriver(
                    tolerance=1.e-6,
                    initialstep=0,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=SS22(theta1=0.5,theta2=0.5))
                    ),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,max_iterations=1000)
                )
            )
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Displacement_t,
            initializer=ConstTwoVectorFieldInit(cx=0.0,cy=0.0))
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh', time=0.0)
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=3.6275987284684357*shortening)

        self.assert_(file_utils.fp_file_compare(
                'springtest.out',
                os.path.join('mesh_data', 'springtest'+suffix+'.exact'),
                1.e-4))
        file_utils.remove('springtest.out')
    def tearDown(self):
        outputdestination.forgetTextOutputStreams()
        OOF.Material.Delete(name='material')

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Use various time steppers to solve a simple thermal diffusion
# problem.

class OOF_ThermalDiffusionTimeSteppers(SaveableMeshTest):
    def setUp(self):
        global outputdestination
        from ooflib.engine.IO import outputdestination
        global mesh
        from ooflib.engine import mesh
        OOF.Microstructure.New(
            name='microstructure', width=1.0, height=1.0,
            width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(name='material', material_type='bulk')
        OOF.Material.Add_property(
            name='material', property='Thermal:Conductivity:Isotropic')
        OOF.Material.Add_property(
            name='material',
            property='Thermal:HeatCapacity:ConstantHeatCapacity')
        OOF.Material.Assign(
            material='material', microstructure='microstructure', pixels=all)
        OOF.Skeleton.New(
            name='skeleton', microstructure='microstructure',
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
                profile=ConstantProfile(value=2),boundary='left'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<2>',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=1),boundary='right'))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Temperature,
            initializer=ConstScalarFieldInit(value=4))
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh', time=0.0)
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name=AutomaticName('Average Temperature on top'),
            output=BoundaryAnalysis(operation=AverageField(field=Temperature),
                                    boundary='top'))
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('Average Temperature on top'),
            scheduletype=AbsoluteOutputSchedule(),
            schedule=Periodic(delay=0.0,interval=0.05*shortening))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('Average Temperature on top'),
            destination=OutputStream(filename='test.dat',mode='w'))

    @memorycheck.check('microstructure')
    def SS22directSaveRestore(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=1.e-6,
                    minstep=1e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=SS22(theta1=0.5,theta2=0.5))),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=DirectMatrixSolver(),
                asymmetric_solver=DirectMatrixSolver()
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_inplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

        self.saveAndLoad('timedep-thermo-inplane')

    @memorycheck.check('microstructure')
    def CNdirect(self):
        if file_utils.generate:
            tol = 1.e-8
        else:
            tol = 1.e-6
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=tol,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=CrankNicolson())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=DirectMatrixSolver(),
                asymmetric_solver=DirectMatrixSolver()
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_inplane'+suffix+'.dat'),
                1.e-5))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def BEdirect(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-5,
                    minstep=1e-6,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=BackwardEuler())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=DirectMatrixSolver(),
                asymmetric_solver=DirectMatrixSolver()
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_inplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def RK4direct(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-6,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=RK4())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=DirectMatrixSolver(),
                asymmetric_solver=DirectMatrixSolver()
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_inplane'+suffix+'.dat'),
                1.e-6))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def RK2direct(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-5,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=RK2())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=DirectMatrixSolver(),
                asymmetric_solver=DirectMatrixSolver()
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_inplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def SS22(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=1e-6,
                    minstep=1e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=SS22(theta1=0.5,theta2=0.5))),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_inplane'+suffix+'.dat'),
                1.e-3))

        # Repeat, because there seems to be some problem with repeated
        # SS22 nonlinear solutions, so it's good to know if repeated
        # linear solutions work.
        OOF.Mesh.Scheduled_Output.Destination.RewindAll(
            mesh='microstructure:skeleton:mesh')
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh', time=0.0)

        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_inplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def CN(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-7,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=CrankNicolson())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_inplane'+suffix+'.dat'),
                1.e-6))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def CNdouble(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-7,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=CrankNicolson())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        # Get there in two stages.
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.25*shortening)
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_inplane'+suffix+'.dat'),
                1.e-6))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def BE(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-5,
                    minstep=1e-06,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=BackwardEuler())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_inplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def RK4(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-6,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=RK4())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_inplane'+suffix+'.dat'),
                1.e-6))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def RK2(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-5,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=RK2())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_inplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    def tearDown(self):
        outputdestination.forgetTextOutputStreams()
        OOF.Material.Delete(name='material')

# OOF_ThermalDiffusionTSPlaneFlux is the same as
# OOF_ThermalDiffusionTimeSteppers, except that it's plane-flux.
## TODO: Find a neater way to do this, instead of copying the whole
## test class.  The reason that it's not easy is that the tolerances
## are different than in Solver7.

class OOF_ThermalDiffusionTSPlaneFlux(SaveableMeshTest):
    def setUp(self):
        global outputdestination
        from ooflib.engine.IO import outputdestination
        global mesh
        from ooflib.engine import mesh

        OOF.Microstructure.New(
            name='microstructure', width=1.0, height=1.0,
            width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(name='material', material_type='bulk')
        OOF.Material.Add_property(
            name='material',
            property='Thermal:HeatCapacity:ConstantHeatCapacity')
        OOF.Property.Copy(
            property='Thermal:Conductivity:Anisotropic:Monoclinic',
            new_name='cond7')
        OOF.Property.Parametrize.Thermal.Conductivity.Anisotropic.Monoclinic.cond7(
            kappa=MonoclinicRank2Tensor(xx=3.0, yy=0.5, zz=0.7, xz=0.5))
        OOF.Material.Add_property(
            name='material',
            property='Thermal:Conductivity:Anisotropic:Monoclinic:cond7')

        OOF.Property.Copy(property='Orientation', new_name='orientation7')
        OOF.Property.Parametrize.Orientation.orientation7(
            angles=Abg(alpha=30,beta=30,gamma=0))
        OOF.Material.Add_property(
            name='material', property='Orientation:orientation7')


        OOF.Material.Assign(
            material='material', microstructure='microstructure', pixels=all)
        OOF.Skeleton.New(
            name='skeleton', microstructure='microstructure',
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
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            field=Temperature)
        OOF.Mesh.Field.Out_of_Plane(
            mesh='microstructure:skeleton:mesh', field=Temperature)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Heat_Eqn)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Heat_Flux)
        OOF.Mesh.Boundary_Conditions.New(
            name='bc',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=2),boundary='left'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<2>',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=1),boundary='right'))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Temperature,
            initializer=ConstScalarFieldInit(value=4))
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh', time=0.0)
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name=AutomaticName('Average Temperature on top'),
            output=BoundaryAnalysis(operation=AverageField(field=Temperature),
                                    boundary='top'))
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('Average Temperature on top'),
            scheduletype=AbsoluteOutputSchedule(),
            schedule=Periodic(delay=0.0,interval=0.05*shortening))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh',
            output=AutomaticName('Average Temperature on top'),
            destination=OutputStream(filename='test.dat',mode='w'))

    @memorycheck.check('microstructure')
    def SS22direct(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=1.e-4,
                    minstep=1e-6,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=SS22(theta1=0.5,theta2=0.5))),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=DirectMatrixSolver(),
                asymmetric_solver=DirectMatrixSolver()
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_outofplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def CNdirect(self):
        if file_utils.generate:
            tol = 1.e-8
        else:
            tol = 1.e-6
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=tol,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=CrankNicolson())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=DirectMatrixSolver(),
                asymmetric_solver=DirectMatrixSolver()
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_outofplane'+suffix+'.dat'),
                1.e-5))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def BEdirect(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-5,
                    minstep=1e-6,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=BackwardEuler())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=DirectMatrixSolver(),
                asymmetric_solver=DirectMatrixSolver()
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_outofplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def RK4direct(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-4,
                    minstep=1e-6,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=RK4())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=DirectMatrixSolver(),
                asymmetric_solver=DirectMatrixSolver()
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_outofplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def RK2direct(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-5,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=RK2())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=DirectMatrixSolver(),
                asymmetric_solver=DirectMatrixSolver()
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_outofplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def SS22(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-5,
                    minstep=1e-6,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=SS22(theta1=0.5,theta2=0.5))),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_outofplane'+suffix+'.dat'),
                1.e-3))

        # Repeat, because there seems to be some problem with repeated
        # SS22 nonlinear solutions, so it's good to know if repeated
        # linear solutions work.
        OOF.Mesh.Scheduled_Output.Destination.RewindAll(
            mesh='microstructure:skeleton:mesh')
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh', time=0.0)

        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_outofplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def CNSaveRestore(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-7,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=CrankNicolson())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_outofplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

        self.saveAndLoad('timedep-thermo-outofplane')

    @memorycheck.check('microstructure')
    def CNdouble(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-7,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=CrankNicolson())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        # Get there in two stages.
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.25*shortening)
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_outofplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def BE(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-5,
                    minstep=1e-06,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=BackwardEuler())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_outofplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def RK4(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-6,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=RK4())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_outofplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    @memorycheck.check('microstructure')
    def RK2(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0.001,
                    tolerance=1e-5,
                    minstep=1e-5,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=RK2())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgtemp_outofplane'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')

    def tearDown(self):
        outputdestination.forgetTextOutputStreams()
        OOF.Property.Delete(property='Orientation:orientation7')
        OOF.Property.Delete(
            property='Thermal:Conductivity:Anisotropic:Monoclinic:cond7')
        OOF.Material.Delete(name='material')

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## Check that static plane stress and plane strain give the correct
## answers for a simple elasticity problem.

class OOF_ElasticPlaneStressPlaneStrainExact(SaveableMeshTest):
    def setUp(self):
        global outputdestination
        from ooflib.engine.IO import outputdestination

        OOF.Microstructure.New(
            name='microstructure',
            width=1.0, height=1.0, width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(
            name='material', material_type='bulk')
        OOF.Material.Assign(
            material='material', microstructure='microstructure', pixels=all)
        OOF.Property.Copy(
            property='Mechanical:Elasticity:Isotropic',
            new_name='iso8')
        OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.iso8(
            cijkl=IsotropicRank4TensorEnu(young=0.66666666666666663,
                                          poisson=0.2))
        OOF.Material.Add_property(
            name='material', property='Mechanical:Elasticity:Isotropic:iso8')
        OOF.Skeleton.New(
            name='skeleton', microstructure='microstructure',
            x_elements=10, y_elements=10,
            skeleton_geometry=QuadSkeleton(left_right_periodicity=False,
                                           top_bottom_periodicity=False))
        OOF.Mesh.New(
            name='mesh', skeleton='microstructure:skeleton',
            element_types=['D2_2', 'T3_3', 'Q4_4'])
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:default',
            field=Displacement)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:default',
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
                profile=ConstantProfile(value=0.0),boundary='left'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<2>',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Displacement,field_component='x',
                equation=Force_Balance,eqn_component='x',
                profile=ConstantProfile(value=0.1),boundary='right'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Displacement,field_component='y',
                equation=Force_Balance,eqn_component='y',
                profile=ConstantProfile(value=0.0),boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Displacement,field_component='y',
                equation=Force_Balance,eqn_component='y',
                profile=ConstantProfile(value=0.0),boundary='bottom'))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Displacement,
            initializer=ConstTwoVectorFieldInit(cx=0.0,cy=0.0))

    @memorycheck.check("microstructure")
    def StaticPlaneStrain(self):
        OOF.Mesh.Field.In_Plane(mesh='microstructure:skeleton:mesh',
                                field=Displacement)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=StaticDriver(),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.0)
        OOF.Mesh.Boundary_Analysis.Analyze(
            mesh='microstructure:skeleton:mesh',
            time=latest,
            boundary='right',
            analyzer=IntegrateBdyFlux(flux=Stress),
            destination=OutputStream(filename='test.dat', mode='w'))
        self.assert_(file_utils.compare_last('test.dat',
                                             (0.0, 0.0740740741, 0.0)))
        OOF.Mesh.Analyze.Average(
            mesh='microstructure:skeleton:mesh',
            time=latest,
            data=getOutput('Flux:Value',flux=Stress),
            domain=EntireMesh(),
            sampling=ElementSampleSet(order=automatic),
            destination=OutputStream(filename='test.dat', mode='w'))
        self.assert_(file_utils.compare_last(
                'test.dat',
                (0.0,
                 0.0740740740741, 0.0185185185185, 0.0185185185185,
                 0.0, 0.0, 0.0)))
        file_utils.remove('test.dat')

    @memorycheck.check("microstructure")
    def StaticPlaneStress(self):
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=StaticDriver(),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.0)
        OOF.Mesh.Boundary_Analysis.Analyze(
            mesh='microstructure:skeleton:mesh',
            time=latest,
            boundary='right',
            analyzer=IntegrateBdyFlux(flux=Stress),
            destination=OutputStream(filename='test.dat', mode='w'))
        self.assert_(file_utils.compare_last('test.dat',
                                             (0.0, 0.0694444444, 0.0)))
        OOF.Mesh.Analyze.Average(
            mesh='microstructure:skeleton:mesh',
            time=latest,
            data=getOutput('Flux:Value',flux=Stress),
            domain=EntireMesh(),
            sampling=ElementSampleSet(order=automatic),
            destination=OutputStream(filename='test.dat', mode='w'))
        self.assert_(file_utils.compare_last(
                'test.dat',
                (0.0,
                 0.0694444444444, 0.0138888889, 0.0,
                 0.0, 0.0, 0.0)))
        file_utils.remove('test.dat')

    def tearDown(self):
        outputdestination.forgetTextOutputStreams()
        OOF.Property.Delete(property='Mechanical:Elasticity:Isotropic:iso8')
        OOF.Material.Delete(name="material")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# ElasticTimeSteppers is a dynamic version of
# ElasticPlaneStressPlaneStrainExact.  We're not comparing to an exact
# solution here, but are checking that different steppers give the
# same answer, and checking that the out-of-plane stresses are zero
# when they're supposed to be.

class OOF_ElasticTimeSteppers(OOF_ElasticPlaneStressPlaneStrainExact):
    def setUp(self):
        OOF_ElasticPlaneStressPlaneStrainExact.setUp(self)
        OOF.Material.Add_property(
            name='material',
            property='Mechanical:MassDensity:ConstantMassDensity')
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='right',
            output=BoundaryAnalysis(
                operation=AverageField(field=Displacement),
                boundary='right'))
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output='right',
            scheduletype=AbsoluteOutputSchedule(),
            schedule=Periodic(delay=0.0,interval=0.1*shortening))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh',
            output='right',
            destination=OutputStream(filename='test.dat', mode='w'))
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='zz',
            output=BulkAnalysis(
                output_type='Aggregate',
                data=getOutput('Flux:Value',flux=Stress),
                operation=AverageOutput(),
                domain=EntireMesh(),
                sampling=ElementSampleSet(order=automatic)))
        OOF.Mesh.Scheduled_Output.Schedule.Copy(
            mesh='microstructure:skeleton:mesh',
            source='right',
            targetmesh='microstructure:skeleton:mesh',
            target='zz')
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh',
            output='zz',
            destination=OutputStream(filename='testz.dat',mode='w'))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Displacement_t,
            initializer=ConstTwoVectorFieldInit(cx=0.0,cy=0.0))
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh',
            time=0.0)
        # Change BC on right from Dirichlet to Neumann
        OOF.Mesh.Boundary_Conditions.Edit(
            name='bc<2>',
            mesh='microstructure:skeleton:mesh',
            condition=NeumannBC(
                flux=Stress,
                profile=[ConstantProfile(value=0.1),
                         ConstantProfile(value=0.0)],
                boundary='right',
                normal=False))
    @memorycheck.check("microstructure")
    def SS22PlaneStrain(self):
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', field=Displacement)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=0.00001,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=SS22(theta1=0.5,theta2=0.5))),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=3.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestrain'+suffix+'.dat'),
                1.e-6))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestrain'+suffix+'.dat'),
                1.e-6))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

    @memorycheck.check("microstructure")
    def SS22PlaneStress(self):
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=0.0001,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=SS22(theta1=0.5,theta2=0.5))),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=3.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestress'+suffix+'.dat'),
                1.e-6))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestress'+suffix+'.dat'),
                1.e-6))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

    # Plane stress followed by plane strain on the same Mesh.  Makes
    # sure that maps are recomputed properly.
    @memorycheck.check("microstructure")
    def SS22PlaneStressPlaneStrain(self):
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=0.00001,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=SS22(theta1=0.5,theta2=0.5))),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=3.0*shortening)

        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', field=Displacement)
        OOF.Subproblem.Equation.Deactivate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh',
            time=0.0)
        OOF.Mesh.Scheduled_Output.Destination.RewindAll(
            mesh='microstructure:skeleton:mesh')
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=3.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestrain'+suffix+'.dat'),
                1.e-3))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestrain'+suffix+'.dat'),
                1.e-6))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')


    @memorycheck.check("microstructure")
    def CNPlaneStrainSaveRestore(self):
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', field=Displacement)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=0.00001,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=CrankNicolson())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=3.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestrain'+suffix+'.dat'),
                1.e-6))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestrain'+suffix+'.dat'),
                1.e-6))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

        self.saveAndLoad("timedep-elastic-inplane")

    @memorycheck.check("microstructure")
    def CNPlaneStressSaveRestore(self):
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=0.00001,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=CrankNicolson())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=3.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestress'+suffix+'.dat'),
                1.e-3))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestress'+suffix+'.dat'),
                1.e-3))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

        self.saveAndLoad("timedep-elastic-outofplane")

    @memorycheck.check("microstructure")
    def RK4PlaneStrain(self):
        # This test is slow, so it's only done up to t=1.0.
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', field=Displacement)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    tolerance=0.00001,
                    initialstep=0,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=RK4())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=1.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestrain'+suffix+'.dat'),
                1.e-4,
                nlines=17
                ))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestrain'+suffix+'.dat'),
                1.e-4,
                nlines=23
                ))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

    @memorycheck.check("microstructure")
    def RK2PlaneStrain(self):
        # This test is slow, so it's only done up to t=1.0.
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', field=Displacement)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=0.00001,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=RK2())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=1.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestrain'+suffix+'.dat'),
                1.e-4,
                nlines=17
                ))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestrain'+suffix+'.dat'),
                1.e-4,
                nlines=23
                ))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

    @memorycheck.check("microstructure")
    def BEPlaneStrain(self):
        # This test is slow, so it's only done up to t=1.0, and uses
        # loose tolerances.
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', field=Displacement)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=1e-5,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=BackwardEuler())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=1.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestrain'+suffix+'.dat'),
                1.e-3,
                nlines=17
                ))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestrain'+suffix+'.dat'),
                1.e-3,
                nlines=23
                ))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

    @memorycheck.check("microstructure")
    def BEPlaneStress(self):
        # This test is very slow, so it's only done up to t=0.5 with
        # loose tolerances.
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=1e-5,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=BackwardEuler())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestress'+suffix+'.dat'),
                1.e-3,
                nlines=12
                ))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestress'+suffix+'.dat'),
                1.e-3,
                nlines=18
                ))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

    @memorycheck.check("microstructure")
    def RK4PlaneStress(self):
        # This test is slow, so it's only done up to t=1.0.
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=0.00001,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=RK4())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=1.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestress'+suffix+'.dat'),
                1.e-4,
                nlines=17
                ))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestress'+suffix+'.dat'),
                1.e-4,
                nlines=23))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

    @memorycheck.check("microstructure")
    def RK2PlaneStress(self):
        # This test is slow, so it's done with loose tolerances.  It
        # passed on 9/15/10 with step tolerance=1.e-6 and comparison
        # tolerance=1.e-4, but took a very long time.
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=1.e-3,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(singlestep=RK2())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=1.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestress'+suffix+'.dat'),
                1.e-2,
                nlines=17
                ))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestress'+suffix+'.dat'),
                1.e-2,
                nlines=23))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

    @memorycheck.check("microstructure")
    def ForwardEulerPlaneStrain(self):
        # This test is slow, so it's only done up to t=1.0 with loose
        # tolerances.
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', field=Displacement)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    tolerance=1e-6,
                    initialstep=0,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=ForwardEuler())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1.e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=1.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestrain'+suffix+'.dat'),
                1.e-3,
                nlines=17
                ))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestrain'+suffix+'.dat'),
                1.e-3,
                nlines=23
                ))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

    @memorycheck.check("microstructure")
    def ForwardEulerPlaneStress(self):
        # This test is very slow, so it's only done up to t=0.5 with
        # loose tolerances.
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=1e-5,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=ForwardEuler())),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000),
                asymmetric_solver=BiConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=0.5*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestress'+suffix+'.dat'),
                1.e-3,
                nlines=12
                ))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestress'+suffix+'.dat'),
                1.e-3,
                nlines=18
                ))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## Check anisotropic elasticity for a simple plane stress and plane
## strain dynamic problem.  The reference files were generated by
## running the tests and aren't based on exact results. However the
## out-of-plane stresses are zero where they're supposed to be zero.

class OOF_AnisoElasticDynamic(OOF_ElasticTimeSteppers):
    def setUp(self):
        OOF_ElasticTimeSteppers.setUp(self)
        OOF.Material.Remove_property(
            name='material',
            property='Mechanical:Elasticity:Isotropic:iso8')
        OOF.Property.Copy(
            property='Mechanical:Elasticity:Anisotropic:Hexagonal',
            new_name='hex')
        OOF.Property.Parametrize.Mechanical.Elasticity.Anisotropic.Hexagonal.hex(
            cijkl=HexagonalRank4TensorCij(
                c11=4, c12=0.2, c13=0.1, c33=1.0, c44=0.5))
        OOF.Material.Add_property(
            name='material',
            property='Mechanical:Elasticity:Anisotropic:Hexagonal:hex')
        OOF.Property.Copy(
            property="Orientation",
            new_name="orient10")
        OOF.Property.Parametrize.Orientation.orient10(
            angles=Abg(alpha=120,beta=-60,gamma=0))
        OOF.Material.Add_property(
            name='material',
            property='Orientation:orient10')
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=1e-6,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=SS22(theta1=0.5,theta2=0.5))),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
    @memorycheck.check("microstructure")
    def AnisoPlaneStrain(self):
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', field=Displacement)
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=1.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data',
                             'avgdisp_anisoplanestrain'+suffix+'.dat'),
                1.e-6))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data',
                             'stress_anisoplanestrain'+suffix+'.dat'),
                1.e-6))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')
    @memorycheck.check("microstructure")
    def AnisoPlaneStress(self):
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:default',
            equation=Plane_Stress)
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=1.0*shortening)
        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data',
                             'avgdisp_anisoplanestress'+suffix+'.dat'),
                1.e-6))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data',
                             'stress_anisoplanestress'+suffix+'.dat'),
                1.e-6))
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')

    def tearDown(self):
        OOF.Property.Delete(
            property='Mechanical:Elasticity:Anisotropic:Hexagonal:hex')
        OOF.Property.Delete(
            property='Orientation:orient10')
        OOF_ElasticTimeSteppers.tearDown(self)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# OOF_StaticAndDynamic is just like OOF_ElasticTimeSteppers, but it
# also includes a separate quasistatic thermal diffusion subproblem,
# and only uses SS22.

## TODO: Technically, this test shouldn't be in this module.  It
## should be part of subproblem_test_extra.py.  But importing
## OOF_ElasticTimeSteppers into that file didn't work because when
## this module is imported into another module, the oofglobals aren't
## defined here.  That could be fixed.

class OOF_StaticAndDynamic(OOF_ElasticTimeSteppers):
    def setUp(self):
        OOF_ElasticTimeSteppers.setUp(self)
        OOF.Material.Add_property(
            name='material',
            property='Thermal:Conductivity:Isotropic')
        OOF.Subproblem.New(
            name='temp', 
            mesh='microstructure:skeleton:mesh',
            subproblem=EntireMeshSubProblem())
        OOF.Subproblem.Field.Define(
            subproblem='microstructure:skeleton:mesh:temp',
            field=Temperature)
        OOF.Subproblem.Field.Activate(
            subproblem='microstructure:skeleton:mesh:temp',
            field=Temperature)
        OOF.Subproblem.Equation.Activate(
            subproblem='microstructure:skeleton:mesh:temp',
            equation=Heat_Eqn)
        OOF.Mesh.Scheduled_Output.New(
            mesh='microstructure:skeleton:mesh',
            name='tempo',
            output=BoundaryAnalysis(
                operation=AverageField(field=Temperature),
                boundary='right'))
        OOF.Mesh.Scheduled_Output.Schedule.Set(
            mesh='microstructure:skeleton:mesh',
            output='tempo',
            scheduletype=AbsoluteOutputSchedule(),
            schedule=Periodic(delay=0.0, interval=0.1*shortening))
        OOF.Mesh.Scheduled_Output.Destination.Set(
            mesh='microstructure:skeleton:mesh',
            output='tempo',
            destination=OutputStream(filename='testt.dat', mode='w'))
        # set boundary conditions: T=0 at y=0, T=t at y=1
        OOF.Mesh.Boundary_Conditions.New(
            name='bct',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ContinuumProfileXTd(
                    function='t',
                    timeDerivative='1',
                    timeDerivative2='0.0'),
                boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bct<2>', 
            mesh='microstructure:skeleton:mesh', 
            condition=DirichletBC(
                field=Temperature,field_component='',
                equation=Heat_Eqn,eqn_component='',
                profile=ConstantProfile(value=0.0),
                boundary='bottom'))
        # set initial T=0 at t=0
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Temperature,
            initializer=ConstScalarFieldInit(value=0.0))
        OOF.Mesh.Set_Field_Initializer(
            mesh='microstructure:skeleton:mesh',
            field=Temperature_t,
            initializer=ConstScalarFieldInit(value=0.0))
        OOF.Mesh.Apply_Field_Initializers_at_Time(
            mesh='microstructure:skeleton:mesh',
            time=0.0)
        # set static solver for subproblem temp
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:temp',
            solver_mode=BasicSolverMode(
                time_stepper=BasicStaticDriver(),
                matrix_method=BasicIterative(
                    tolerance=1e-13,max_iterations=1000)))

    def timetest(self):
        # check that testt.dat contains T_avg =  t/2.
        datafile = file("testt.dat", "r")
        for line in datafile:
            if line[0] == '#':
                continue
            time, temp = map(eval, line.split(','))
            self.assertAlmostEqual(temp, 0.5*time, 6)

    @memorycheck.check("microstructure")
    def SS22PlaneStrain(self):
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', field=Temperature)
        OOF.Mesh.Field.In_Plane(
            mesh='microstructure:skeleton:mesh', field=Displacement)
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=AdvancedSolverMode(
                time_stepper=AdaptiveDriver(
                    initialstep=0,
                    tolerance=0.00001,
                    minstep=1.0e-05,
                    errorscaling=AbsoluteErrorScaling(),
                    stepper=TwoStep(
                        singlestep=SS22(theta1=0.5,theta2=0.5))),
                nonlinear_solver=NoNonlinearSolver(),
                symmetric_solver=ConjugateGradient(
                    preconditioner=ILUPreconditioner(),
                    tolerance=1e-13,
                    max_iterations=1000)
                )
            )
        OOF.Mesh.Solve(
            mesh='microstructure:skeleton:mesh',
            endtime=3.0*shortening)

        self.assert_(file_utils.fp_file_compare(
                'test.dat',
                os.path.join('mesh_data', 'avgdisp_planestrain'+suffix+'.dat'),
                1.e-6))
        self.assert_(file_utils.fp_file_compare(
                'testz.dat',
                os.path.join('mesh_data', 'stress_planestrain'+suffix+'.dat'),
                1.e-6))
        self.timetest()
        file_utils.remove('test.dat')
        file_utils.remove('testz.dat')
        file_utils.remove('testt.dat')

        self.saveAndLoad("static-dynamic-inplane")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Periodic boundary conditions work differently when there are
# out-of-plane components to the field -- the out-of-plane parts
# should be consistent also.  This test examines this functionality.

class OOF_OutOfPlanePeriodicBC(SaveableMeshTest):
    def setUp(self):
        OOF.Microstructure.New(name='microstructure',
                               width=1.0, height=1.0,
                               width_in_pixels=10, height_in_pixels=10)
        OOF.Material.New(name='left', material_type='bulk')
        OOF.Material.New(name='right', material_type='bulk')
        OOF.Property.Copy(property='Mechanical:Elasticity:Isotropic',
                          new_name='soft')
        OOF.Property.Copy(property='Mechanical:Elasticity:Isotropic',
                          new_name='hard')
        OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.soft(
            cijkl=IsotropicRank4TensorCij(
            c11=0.80000000000000004,c12=0.29999999999999999))
        OOF.Material.Add_property(
            name='left',
            property='Mechanical:Elasticity:Isotropic:soft')
        OOF.Material.Add_property(
            name='right',
            property='Mechanical:Elasticity:Isotropic:hard')
        OOF.Windows.Graphics.New()
        OOF.Skeleton.New(
            name='skeleton',
            microstructure='microstructure',
            x_elements=4, y_elements=4,
            skeleton_geometry=QuadSkeleton(
            left_right_periodicity=True,top_bottom_periodicity=False))
        OOF.LayerEditor.LayerSet.New(window='Graphics_1')
        OOF.LayerEditor.LayerSet.DisplayedObject(
            category='Microstructure', object='microstructure')
        OOF.LayerEditor.LayerSet.Add_Method(
            method=MicrostructureMaterialDisplay(
            no_material=Gray(value=0.0),no_color=RGBColor(
            red=0.00000,green=0.00000,blue=1.00000)))
        OOF.LayerEditor.LayerSet.Send(window='Graphics_1')
        OOF.LayerEditor.LayerSet.Send(window='Graphics_1')
        OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle(
            source='microstructure',
            points=[Point(-0.0151584,1.01516),
                    Point(0.497511,-0.0300905)], shift=0, ctrl=0)
        OOF.Material.Assign(material='left',
                            microstructure='microstructure',
                            pixels=selection)
        OOF.Graphics_1.Toolbox.Pixel_Select.Invert(source='microstructure')
        OOF.Material.Assign(material='right',
                            microstructure='microstructure', pixels=selection)
        OOF.Graphics_1.Toolbox.Pixel_Select.Clear(source='microstructure')
        OOF.Mesh.New(name='mesh',
                     skeleton='microstructure:skeleton',
                     element_types=['D2_2', 'T3_3', 'Q4_4'])
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
        OOF.Mesh.Boundary_Conditions.New(
            name='bc', mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(field=Displacement,
                                  field_component='y',
                                  equation=Force_Balance,
                                  eqn_component='y',
                                  profile=ConstantProfile(value=0.0),
                                  boundary='bottom'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<2>', mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(field=Displacement,
                                  field_component='y',
                                  equation=Force_Balance,
                                  eqn_component='y',
                                  profile=ConstantProfile(value=0.1),
                                  boundary='top'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<3>',
            mesh='microstructure:skeleton:mesh',
            condition=DirichletBC(field=Displacement,
                                  field_component='x',
                                  equation=Force_Balance,
                                  eqn_component='x',
                                  profile=ConstantProfile(value=0.0),
                                  boundary='bottomleft'))
        OOF.Mesh.Boundary_Conditions.New(
            name='bc<4>',
            mesh='microstructure:skeleton:mesh',
            condition=PeriodicBC(field=Displacement,
                                 equation=Force_Balance,
                                 boundary='right left'))

    def tearDown(self):
        OOF.Graphics_1.File.Close()
        OOF.Material.Delete(name='left')
        OOF.Material.Delete(name='right')
        OOF.Property.Delete(property='Mechanical:Elasticity:Isotropic:soft')
        OOF.Property.Delete(property='Mechanical:Elasticity:Isotropic:hard')

    @memorycheck.check('microstructure')
    def Static(self):
        OOF.Subproblem.Set_Solver(
            subproblem='microstructure:skeleton:mesh:default',
            solver_mode=BasicSolverMode(
            time_stepper=BasicStaticDriver(),
            matrix_method=BasicIterative(
            tolerance=1e-13,max_iterations=1000)))
        OOF.Mesh.Solve(mesh='microstructure:skeleton:mesh',endtime=0.0)
        asciifilename = "oop_periodic_static-ascii.dat"
        OOF.File.Save.Mesh(filename=asciifilename,
                           mode='w', format='ascii',
                           mesh = 'microstructure:skeleton:mesh')
        self.assert_(file_utils.fp_file_compare(
            asciifilename,
            os.path.join('mesh_data', asciifilename),
            1.e-6))
        file_utils.remove(asciifilename)
            

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Routine to do regression-type testing on the items in this file.
# Tests will be run in the order they appear in the list.  This
# routine will stop after the first failure.

def run_tests():

    static_set = [
        OOF_StaticIsoElastic("Null"),
        OOF_StaticIsoElastic("Solve"),
        OOF_NonrectMixedBCStaticElastic("Solve"),
        OOF_NewBCNonrectMixedEtc("Solve"),
        OOF_AnisoRotation("Solve"),
        OOF_1x1ElasticDynamic("Static"),
        OOF_ElasticPlaneStressPlaneStrainExact("StaticPlaneStrain"),
        OOF_ElasticPlaneStressPlaneStrainExact("StaticPlaneStress")
        ]

    dynamic_set = [
        OOF_1x1ElasticDynamic("Dynamic"),
        OOF_NonstaticThenStatic("Solve"),

        # In "generate" mode,
        # OOF_ThermalDiffusionTimeSteppers("CNdirect") provides the
        # reference data for the rest of
        # OOF_ThermalDiffusionTimeSteppers, so it must precede the
        # rest of OOF_ThermalDiffusionTimeSteppers in this list.
        OOF_ThermalDiffusionTimeSteppers("CNdirect"),
        OOF_ThermalDiffusionTimeSteppers("SS22directSaveRestore"),
        OOF_ThermalDiffusionTimeSteppers("BEdirect"),
        OOF_ThermalDiffusionTimeSteppers("RK4direct"),
        OOF_ThermalDiffusionTimeSteppers("RK2direct"),
        OOF_ThermalDiffusionTimeSteppers("SS22"),
        OOF_ThermalDiffusionTimeSteppers("CN"),
        OOF_ThermalDiffusionTimeSteppers("RK4"),
        OOF_ThermalDiffusionTimeSteppers("RK2"),
        OOF_ThermalDiffusionTimeSteppers("BE"),
        OOF_ThermalDiffusionTimeSteppers("CNdouble"),

        OOF_ThermalDiffusionTSPlaneFlux("CNdirect"),
        OOF_ThermalDiffusionTSPlaneFlux("BEdirect"),
        OOF_ThermalDiffusionTSPlaneFlux("RK4direct"),
        OOF_ThermalDiffusionTSPlaneFlux("RK2direct"),
        OOF_ThermalDiffusionTSPlaneFlux("CNSaveRestore"),
        OOF_ThermalDiffusionTSPlaneFlux("RK4"),
        OOF_ThermalDiffusionTSPlaneFlux("RK2"),
        OOF_ThermalDiffusionTSPlaneFlux("BE"),
        OOF_ThermalDiffusionTSPlaneFlux("CNdouble"),
        OOF_ThermalDiffusionTSPlaneFlux("SS22direct"),
        OOF_ThermalDiffusionTSPlaneFlux("SS22"),

        # In "generate" mode, SS22PlaneStrain and SS22PlaneStress
        # provide the reference data for the rest of OOF_ElasticTimeSteppers, so
        # they must precede the rest of OOF_ElasticTimeSteppers in this list.
        OOF_ElasticTimeSteppers("SS22PlaneStrain"),
        OOF_ElasticTimeSteppers("SS22PlaneStress"),
        OOF_ElasticTimeSteppers("SS22PlaneStressPlaneStrain"),
        OOF_ElasticTimeSteppers("CNPlaneStrainSaveRestore"),
        OOF_ElasticTimeSteppers("CNPlaneStressSaveRestore"),
        OOF_ElasticTimeSteppers("RK4PlaneStrain"),
        OOF_ElasticTimeSteppers("RK4PlaneStress"),
        OOF_ElasticTimeSteppers("RK2PlaneStrain"),
        OOF_ElasticTimeSteppers("RK2PlaneStress"),
        OOF_ElasticTimeSteppers("BEPlaneStrain"),
        OOF_ElasticTimeSteppers("BEPlaneStress"),
        OOF_ElasticTimeSteppers("ForwardEulerPlaneStrain"),
        OOF_ElasticTimeSteppers("ForwardEulerPlaneStress"),

        OOF_AnisoElasticDynamic("AnisoPlaneStrain"),
        OOF_AnisoElasticDynamic("AnisoPlaneStress"),

        ## TODO: Figure out why OOF_StaticAndDynamic fails
        ## intermittently on OS X.
        #OOF_StaticAndDynamic("SS22PlaneStrain")
        ]

    oop_periodic_set = [
        OOF_OutOfPlanePeriodicBC('Static')
        ]

    # static_set = []
    # dynamic_set = [OOF_ThermalDiffusionTimeSteppers("SS22")]
    # dynamic_set = [OOF_StaticAndDynamic("SS22PlaneStrain")]
    # dynamic_set = [OOF_1x1ElasticDynamic("Dynamic")]
    # dynamic_set=[OOF_ElasticTimeSteppers("SS22PlaneStressPlaneStrain")]

    logan = unittest.TextTestRunner()

    for t in static_set:
        print >> sys.stderr,  "\n *** Running test: %s\n" % t.id()
        res = logan.run(t)
        if not res.wasSuccessful():
            return 0

    # There are short and long versions of all of the time-dependent
    # tests.  Originally, the short versions were only run manually,
    # when debugging the testing procedure.  But then interesting
    # roundoff errors began to occur during the short tests, but not
    # during the long tests, so the short tests have been incorporated
    # into the official test suite.  The tests are first run with
    # shortening=0.1 and suffix="-short", and then run with
    # shortening=1.0 and suffix="".
    global shortening
    global suffix
    shortening = 0.1
    suffix = "-short"
    for t in dynamic_set:
        print >> sys.stderr,  "\n *** Running test: %s (short)\n" % t.id()
        res = logan.run(t)
        if not res.wasSuccessful():
            return 0

    shortening = 1.0
    suffix=""
    for t in dynamic_set:
        print >> sys.stderr,  "\n *** Running test: %s (long)\n" % t.id()
        res = logan.run(t)
        if not res.wasSuccessful():
            return 0

    for t in oop_periodic_set:
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

