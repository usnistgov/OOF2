# -*- python -*-
# $RCSfile: colormap.py,v $
# $Revision: 1.31 $
# $Author: langer $
# $Date: 2013/07/03 19:28:52 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Colormaps map numbers in the range [0,1] to colors

from ooflib.SWIG.common import config
from ooflib.common import color
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from types import *
import math

FloatParameter = parameter.FloatParameter
FloatRangeParameter = parameter.FloatRangeParameter

class ColorMap(registeredclass.RegisteredClass):
    registry = []
    tip = "Color maps used in contour displays."
    discussion = """<para>
    <classname>ColorMap</classname> objects are used when generating
    contour displays.  They specify a way of converting numbers into
    colors.
    </para>"""

    if config.dimension()==3:
        def getVtkLookupTable(self, numcolors, min, max):
            if max == min:
                max += 1.0
            lut = vtk.vtkLookupTable()
            lut.SetNumberOfColors(numcolors)
            lut.SetTableRange(min,max)
            delta = (max-min)/(numcolors-1)
            x = min
            for i in xrange(numcolors):
                color = self.__call__((x-min)/(max-min))
                x += delta
                lut.SetTableValue(i,color.getRed(),color.getGreen(),color.getBlue(),1)
            return lut
            
        

class ColorMapRegistration(registeredclass.Registration):
    def __init__(self, name, subclass, ordering, params=[], tip=None,
                 discussion=None):
        registeredclass.Registration.__init__(self, name, ColorMap, subclass,
                                              ordering, params=params, tip=tip,
                                              discussion=discussion)
##########################


class GrayMap(ColorMap):
    def __call__(self, x):
        return color.Gray(x)

ColorMapRegistration(
    'Gray',
    GrayMap,
    0,
    tip="Linear gray scale.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/reg/graymap.xml')
    )

class ThermalMap(ColorMap):
    "black->red->yellow->white"
    def __call__(self, x):
        if x < 0.33:
            return color.RGBColor(x/0.33, 0, 0)
        if x < 0.67:
            return color.RGBColor(1, (x-0.33)/0.34, 0)
        return color.RGBColor(1, 1, (x-0.67)/0.33)

ColorMapRegistration(
    'Thermal',
    ThermalMap,
    1,
    tip="Black to red to yellow to white.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/reg/thermalmap.xml'))

class GammaGrayMap(ColorMap):
    def __init__(self, gamma):
        self.gamma = gamma
        self.invgamma = 1.0/gamma
    def __call__(self, x):
        return color.Gray(math.pow(x, self.invgamma))

ColorMapRegistration(
    'GammaGray',
    GammaGrayMap,
    0.1,
    [FloatParameter('gamma', 1.0, tip="gamma correction")],
    tip="gray = x^(1/gamma)",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/reg/gammagray.xml')
    )

class HSVMap(ColorMap):
    def __init__(self, saturation=1.0, value=1.0, phase_shift=0.0):
        self.saturation = saturation
        self.value = value
        self.phase_shift = phase_shift
    def __call__(self, x):
        return color.HSVColor(hue=x*360+self.phase_shift,
                               saturation=self.saturation,
                               value=self.value)

ColorMapRegistration(
    'HSV',
    HSVMap,
    2,
    [FloatRangeParameter('saturation', (0., 1., .01), 1.0,
                         tip='0.0=weak, 1.0=strong'),
     FloatRangeParameter('value', (0., 1., .01), 1.0,
                         tip='0.0=dark, 1.0=light'),
     FloatRangeParameter('phase_shift', (0., 360., 1.), 0.0,
                         tip='initial hue, in degrees')],
    tip="Varying hue, at fixed saturation and value.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/reg/hsvmap.xml'))

# The ROYGBIV map -- although, since it starts from blue, it's really
# the VIBGYOR map.
class SpectralMap(ColorMap):
    def __init__(self, saturation=1.0, value=1.0):
        self.saturation = saturation
        self.value = value
    def __call__(self,x):
        return color.HSVColor(hue=(1.0-x)*240,
                               saturation=self.saturation,
                               value=self.value)

ColorMapRegistration(
    'Spectral',
    SpectralMap,
    2.5,
    [FloatRangeParameter('saturation', (0, 1., .01), 1.0,
                         tip='0.0=weak, 1.0=strong'),
     FloatRangeParameter('value', (0, 1., .01), 1.0,
                         tip='0.0=dark, 1.0=light')],
    tip="blue, green, yellow, orange, red",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/reg/spectralmap.xml'))


class TequilaSunrise(ColorMap):
    def __call__(self,x):
        return color.RGBColor(1.0, 0.86667*math.sqrt(x), 0.0)

ColorMapRegistration(
    'TequilaSunrise',
    TequilaSunrise,
    3.,
    tip="It's another Tequila sunrise/Stirrin' slowly 'cross the sky...",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/reg/tequilamap.xml'))


# Table-interpolating color map, from matplotlib. Geologically
# inspired, goes from dark blue at the low end, through green
# (lowlands), beige (highlands), then gray and white (mountains and
# mountain tops).  Tabular definition taken from the Google code
# page at:
# 
# https://code.google.com/p/guillaumemaze/source/browse/trunk/matlab/
# codes/colors/matplotlib/gist_earth.txt?spec=svn234&r=234
# 
class GistEarth(ColorMap):
    def __init__(self):
        self.redlist = [0.002613,0.007840,0.013067,0.018294,0.023521,
                        0.028748,0.033975,0.039202,0.044429,0.047042,
                        0.054883,0.057496,0.065336,0.067950,0.075790,
                        0.078404,0.086244,0.091471,0.094084,0.101925,
                        0.107152,0.112378,0.114992,0.122832,0.128059,
                        0.133286,0.135900,0.143740,0.148967,0.154194,
                        0.156807,0.164648,0.169874,0.175101,0.180328,
                        0.185555,0.190027,0.191877,0.197426,0.201125,
                        0.204824,0.208524,0.212223,0.215922,0.219621,
                        0.221471,0.227020,0.230719,0.234419,0.238118,
                        0.241817,0.245516,0.249216,0.251065,0.256614,
                        0.260313,0.264013,0.267712,0.271452,0.288886,
                        0.306320,0.315037,0.341188,0.358622,0.376056,
                        0.393490,0.410924,0.428359,0.445793,0.463227,
                        0.478399,0.491332,0.504266,0.517199,0.530132,
                        0.536599,0.555999,0.568932,0.581865,0.594798,
                        0.607732,0.620665,0.633598,0.646532,0.659465,
                        0.672398,0.685331,0.698265,0.711198,0.719255,
                        0.722534,0.724173,0.729090,0.732368,0.735646,
                        0.738924,0.742202,0.745480,0.748759,0.752037,
                        0.755339,0.764112,0.772885,0.781657,0.790430,
                        0.799203,0.807975,0.812361,0.825520,0.834293,
                        0.843066,0.851838,0.860611,0.869383,0.878156,
                        0.886929,0.895701,0.904474,0.913246,0.922019,
                        0.930792,0.939564,0.948337,0.952723,0.965882,
                        0.974655,0.983427,0.992200]
        self.greenlist = [0.000000,0.000000,0.000000,0.000000,0.017927,
                          0.035968,0.054008,0.072048,0.090088,0.099108,
                          0.126168,0.135189,0.162249,0.171269,0.197466,
                          0.205623,0.230095,0.246410,0.254568,0.279040,
                          0.295355,0.310845,0.318178,0.340179,0.354846,
                          0.369513,0.376847,0.396564,0.408959,0.421355,
                          0.427552,0.446146,0.458541,0.470937,0.483332,
                          0.495728,0.504230,0.506488,0.513261,0.517776,
                          0.522291,0.526806,0.531321,0.535836,0.540351,
                          0.542608,0.549381,0.553896,0.558411,0.562926,
                          0.567441,0.571956,0.576471,0.578729,0.585501,
                          0.590016,0.594531,0.599046,0.603562,0.608077,
                          0.612592,0.614849,0.621622,0.626137,0.630652,
                          0.635167,0.639682,0.643128,0.646569,0.650010,
                          0.653452,0.656893,0.660334,0.663776,0.667217,
                          0.668938,0.674100,0.677541,0.680983,0.684424,
                          0.687866,0.691307,0.694748,0.698190,0.701631,
                          0.705072,0.708514,0.711955,0.715397,0.713679,
                          0.706906,0.703519,0.693358,0.686585,0.679811,
                          0.673038,0.666264,0.659490,0.652717,0.645943,
                          0.639219,0.642991,0.646409,0.651513,0.658287,
                          0.665084,0.671882,0.675280,0.685476,0.692274,
                          0.699071,0.710314,0.721533,0.732295,0.743077,
                          0.758418,0.773759,0.789101,0.804442,0.819783,
                          0.836438,0.854422,0.872514,0.881617,0.915975,
                          0.938880,0.961785,0.984300]
        self.bluelist = [0.168692,0.263805,0.348089,0.432373,0.455606,
                         0.457028,0.458449,0.459871,0.461293,0.462004,
                         0.464136,0.464847,0.466980,0.467691,0.469824,
                         0.470534,0.472667,0.474089,0.474800,0.476932,
                         0.478354,0.479776,0.480487,0.482619,0.484041,
                         0.485463,0.486174,0.488306,0.489728,0.491150,
                         0.491861,0.493994,0.495415,0.496837,0.498259,
                         0.499681,0.495657,0.490857,0.476456,0.466855,
                         0.457254,0.447654,0.438053,0.428452,0.418852,
                         0.414051,0.399650,0.390049,0.380449,0.370848,
                         0.361247,0.351647,0.342046,0.337245,0.322844,
                         0.313244,0.303643,0.294042,0.284442,0.274841,
                         0.279352,0.281638,0.288496,0.293068,0.297640,
                         0.302212,0.306783,0.311355,0.315927,0.320499,
                         0.322978,0.325457,0.327936,0.330415,0.332894,
                         0.334133,0.337851,0.340330,0.342809,0.345288,
                         0.347767,0.350246,0.352724,0.355203,0.357682,
                         0.360161,0.362640,0.365119,0.367598,0.370076,
                         0.372555,0.373795,0.377513,0.379992,0.382471,
                         0.384950,0.387428,0.389907,0.392386,0.394865,
                         0.405741,0.424956,0.444171,0.463386,0.482601,
                         0.501816,0.521031,0.530638,0.559461,0.578676,
                         0.597891,0.617106,0.636321,0.655536,0.676973,
                         0.700614,0.724254,0.747895,0.771535,0.795176,
                         0.818816,0.842457,0.866097,0.877918,0.913378,
                         0.937019,0.960659,0.984300]
        # Assume all lists are the same length.  Maybe check for that?
        self.listlen = len(self.redlist)
        self.delta = 1.0/float(self.listlen-1)

    def __call__(self,x):
        lowdx = int(math.floor(x*float(self.listlen-1)))

        if lowdx<=0:
            return color.RGBColor(self.redlist[0],
                                  self.greenlist[0],
                                  self.bluelist[0])

        if lowdx>=(self.listlen-1):
            return color.RGBColor(self.redlist[-1], 
                                  self.greenlist[-1],
                                  self.bluelist[-1])
        frac = x*self.listlen-lowdx
        
        rl = self.redlist[lowdx]
        rh = self.redlist[lowdx+1]

        gl = self.greenlist[lowdx]
        gh = self.greenlist[lowdx+1]
        
        bl = self.bluelist[lowdx]
        bh = self.bluelist[lowdx+1]

        return color.RGBColor(rl+frac*(rh-rl), 
                              gl+frac*(gh-gl),
                              bl+frac*(bh-bl))



ColorMapRegistration(
    'GistEarth',
    GistEarth,
    4.,
    tip="Geographically inspired topography-like color scheme.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/reg/gistearth.xml'))

# For parameters containing these, use the appropriate RegisteredParameter.
