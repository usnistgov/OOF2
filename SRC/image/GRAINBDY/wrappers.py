# -*- python -*-
# $RCSfile: wrappers.py,v $
# $Revision: 1.23 $
# $Author: langer $
# $Date: 2014/09/27 21:41:32 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.image import oofimage

from ooflib.common import debug
from ooflib.image import imagemodifier
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.SWIG.image.GRAINBDY import imageops
from ooflib.SWIG.common import intarray
from ooflib.image.GRAINBDY import imagefilter
    
class FullGaborModifier(imagemodifier.ImageModifier):
    def __init__(self, a, b, numAngles,Threshold,Line_color,d,n,B,trimYN,t):
        self.a = a
        self.b = b
        self.numAngles=numAngles
        self.Threshold=Threshold
        self.Line_color=Line_color
        self.d=d
        self.n=n
        self.B=B
        self.trimYN=trimYN
        self.t=t
    def __call__(self, image):
        dbls=oofimage.grayify(image)
        for i in range(self.numAngles):
            phi = i*180./self.numAngles
            current = imageops.realGabor(dbls,self.a,self.b,phi)
            if i!=0:
                old=imageops.findLargerVals(current,old)
            else:
                old=current
        scaled = imageops.scaleArray(old, 0.0, 1.0,self.Line_color)
        bools=imageops.connect(scaled,self.Threshold,self.t,self.d,self.n,
                               self.B,self.trimYN)
        oofimage.setFromBool(image,bools)      
        
registeredclass.Registration(
    'FullEdgeDetection',
    imagemodifier.ImageModifier,
    FullGaborModifier,
    ordering=100,
    params=[
    parameter.IntParameter('a',  value=3, tip="a in pixels"),
    parameter.IntParameter('b',  value=3, tip="b in pixels"),
    parameter.IntParameter('numAngles',value=6,
              tip="number of angles to apply the filter"),
    parameter.FloatParameter('Threshold', value=.5,
              tip="Threshold value used when thresholding image"),
    parameter.IntParameter('Line_color', value=2,
              tip="Colors of the lines to detect. (2) Both white and dark lines. (1) Only white lines (0) Only black lines."),
    parameter.IntParameter('d',value=7,
              tip="Value used for morphological closing"),
    parameter.IntParameter('n',value=9,
              tip="Number of interations"),
    parameter.IntParameter('B',value=5,
              tip="Half the size of the box in pixels"),
    parameter.IntParameter('trimYN',value=0,
              tip="Do you want to trim the image? [1 or 0]"),
    parameter.FloatParameter('t',value=.5,
              tip="Percent to decrease threshold by")
    ],
    tip="Apply a full edge detection process"
)

class GaussSmoothModifier(imagemodifier.ImageModifier):
    def __init__(self, stdDev):
        self.stdDev=stdDev
    def __call__(self, image):
        dbls = oofimage.grayify(image)
        temp = imageops.gaussSmooth(dbls,self.stdDev)  
           
        scaled = imageops.scaleArray2(temp, 0.0, 1.0)

        imageops.setFromArray(image,scaled)
        
registeredclass.Registration(
    'GaussianSmoothing',
    imagemodifier.ImageModifier,
    GaussSmoothModifier,
    ordering=200,
    params=[ parameter.FloatParameter('stdDev', value=1,
                       tip="Standard deviation for the gaussian smoothing")  ],
    tip="Apply Gaussian Smoothing to a noisy image"
)

#####################################################
#functions that apply the filters at a single angle.#
#####################################################

##class RealGaborAngleModifier(imagemodifier.ImageModifier):
##    def __init__(self, a, b, phi):
##        self.a = a
##        self.b = b
##        self.phi = phi
##    def __call__(self, image):
##        dbls = imageops.grayify(image)
##        gaborimg = imageops.realGabor(dbls,self.a,self.b,self.phi)
##        scaled = imageops.scaleArray2(gaborimg, 0.0, 1.0)
##        imageops.setFromArray(image,scaled)
        
##registeredclass.Registration(
##    'RealGabor_Single_Angle',
##    imagemodifier.ImageModifier,
##    RealGaborAngleModifier,
##    ordering=100,
##    params=[
##    parameter.IntParameter('a',  value=3, tip="a in pixels"),
##    parameter.IntParameter('b',  value=3, tip="b in pixels"),
##    parameter.FloatParameter('phi',  value=0.0,
##                        tip="angle in degrees")
##    ],
##    tip="Apply a real Gabor filter at a given angle"
##)

##class ImagGaborAngleModifier(imagemodifier.ImageModifier):
##    def __init__(self, a, b, phi):
##        self.a = a
##        self.b = b    
##        self.phi = phi
##    def __call__(self, image):
##        dbls = imageops.grayify(image)
##        gaborimg = imageops.imagGabor(dbls,self.a,self.b,self.phi)
##        scaled = imageops.scaleArray2(gaborimg, 0.0, 1.0)
##        imageops.setFromArray(image,scaled)
    
##registeredclass.Registration(
##    'ImaginaryGabor_Single_Angle',
##    imagemodifier.ImageModifier,
##    ImagGaborAngleModifier,
##    ordering=100,
##    params=[
##    parameter.IntParameter('a',  value=3, tip="a in pixels"),
##    parameter.IntParameter('b',  value=3, tip="b in pixels"),   
##    parameter.FloatParameter('phi',  value=0.0,
##                        tip="angle in degrees")
##    ],
##    tip="Apply an imaginary Gabor filter at a given angle"
##)

##class ModGaborAngleModifier(imagemodifier.ImageModifier):
##    def __init__(self, a, b, phi):
##        self.a = a
##        self.b = b    
##        self.phi = phi
##    def __call__(self, image):
##        dbls = imageops.grayify(image)
##        gaborimg = imageops.modGabor(dbls,self.a,self.b,self.phi)
##        scaled = imageops.scaleArray2(gaborimg, 0.0, 1.0)
##        imageops.setFromArray(image,scaled)
        
##registeredclass.Registration(
##    'ModifiedGabor_Single_Angle',
##    imagemodifier.ImageModifier,
##    ModGaborAngleModifier,
##    ordering=100,
##    params=[
##    parameter.IntParameter('a',  value=3, tip="a in pixels"),
##    parameter.IntParameter('b',  value=3, tip="b in pixels"),   
##    parameter.FloatParameter('phi',  value=0.0,
##                        tip="angle in degrees")
##    ],
##    tip="Apply a modified Gabor filter to detect edges"
##)


##class GaborAngleModifier(imagemodifier.ImageModifier):
##    def __init__(self, a, b, phi):
##        self.a = a
##        self.b = b
##        self.phi
##    def __call__(self, image):
##        dbls = imageops.grayify(image)
##        gaborimg = imageops.modGabor(dbls,self.a,self.b,self.phi)
##        scaled = imageops.scaleArray(gaborimg, 0.0, 1.0)
##        imageops.setFromArray(image,scaled)
        
##registeredclass.Registration(
##    'NormalGabor',
##    imagemodifier.ImageModifier,
##    GaborAngleModifier,
##    ordering=100,
##    params=[
##    parameter.IntParameter('a',  value=3, tip="a in pixels"),
##    parameter.IntParameter('b',  value=3, tip="b in pixels"), 
##    parameter.FloatParameter('phi',  value=0.0,
##                        tip="angle in degrees")
##    ],
##    tip="Apply the normal Gabor filter to detect edges"
##)


#class CloseImage(imagemodifier.ImageModifier):
#    def __init__(self,n):
 #       self.n=n
 #   def __call__(self,image):
 #       dbls=oofimage.grayify(image)
 #       bools=oofimage.threshold(dbls,.5)
 #       bools=imageops.close(bools,self.n)
 #       oofimage.setFromBool(image,bools)

#registeredclass.Registration(
#    'CloseImage',
#    imagemodifier.ImageModifier,
#    CloseImage,
 #   ordering=10,
 #   params=[parameter.IntParameter('n',value=7,
 #                               tip="Diameter for closing. Must be odd")],
 #   tip="Close the gaps in a binary image"
#)

#class SkeletonizeImage(imagemodifier.ImageModifier):
 #   def __call__(self,image):
 #       dbls=oofimage.grayify(image)
 #       bools=oofimage.threshold(dbls,.5)
 #       bools=imageops.skeletonize(bools)
 #       oofimage.setFromBool(image,bools)

#registeredclass.Registration(
#    'SkeletonizeImage',
 #   imagemodifier.ImageModifier,
#    SkeletonizeImage,
 #   ordering=11,
 #   tip="Skeletonize the image"
#)

class ConnectEdges(imagemodifier.ImageModifier):
    def __init__(self,Threshold,d,n,B,trimYN,t):
        self.d=d;
        self.Threshold=Threshold
        self.n=n
        self.B=B
        self.trimYN=trimYN
        self.t=t
    def __call__(self,image):
        dbls=oofimage.grayify(image)
 #     bools=oofimage.threshold(dbls,.5)
        bools=imageops.connecter(dbls,self.Threshold,self.t,self.d,self.n,
                               self.B,self.trimYN)
        oofimage.setFromBool(image,bools)

registeredclass.Registration(
    'Connect_Edges',
    imagemodifier.ImageModifier,
    ConnectEdges,
    ordering=11,
    params=[parameter.FloatParameter('Threshold',value=.5,
                                tip="Initial threshold value"),
            parameter.IntParameter('d',value=7,
                                tip="Value used for morphological closing"),
            parameter.IntParameter('n',value=9,
                                tip="Number of interations"),
            parameter.IntParameter('B',value=5,
                                tip="Half the size of the box in pixels"),
            parameter.IntParameter('trimYN',value=0,
                                tip="Do you want to trim the image? [1 or 0]"),
            parameter.FloatParameter('t',value=.5,
                                tip="Percent to decrease threshold by")],  
    tip="Connect the edges in the image"
)

class AddGausNoise(imagemodifier.ImageModifier):
    def __init__(self,Standard_deviation):
        self.Standard_deviation=Standard_deviation
    def __call__(self,image):
        dbls=oofimage.grayify(image)
        dbls=imageops.addNoise(dbls,self.Standard_deviation)
        imageops.setFromArray(image,dbls)

registeredclass.Registration(
    "Add_Gaussian_Noise",
    imagemodifier.ImageModifier,
    AddGausNoise,
    ordering=200,
    params=[parameter.FloatParameter('Standard_deviation', value=.5)],
    tip="Adds Gausseian noise to an image"
)

class SpreadValues(imagemodifier.ImageModifier):
    def __init__(self,T):
        self.T=T
    def __call__(self,image):
        dbls=oofimage.grayify(image)
        dbls=imageops.spread(dbls,self.T)
        imageops.setFromArray(image,dbls)

registeredclass.Registration(
    "SpreadDataValues",
    imagemodifier.ImageModifier,
    SpreadValues,
    ordering=200,
    params=[parameter.FloatRangeParameter('T', (0,1,.01),value=.5)],
    tip="Scale values over given threshold for larger spread."
)


class SpreadValues2(imagemodifier.ImageModifier):
    def __init__(self,T):
        self.T=T
    def __call__(self,image):
        dbls=oofimage.grayify(image)
        dbls=imageops.spread2(dbls,self.T)
        imageops.setFromArray(image,dbls)

registeredclass.Registration(
    "SpreadDataValues2",
    imagemodifier.ImageModifier,
    SpreadValues2,
    ordering=200,
    params=[parameter.FloatRangeParameter('T', (0,1,.01),value=.5)],
    tip="Scale values under given threshold for larger spread."
)

class MakeHistogram(imagemodifier.ImageModifier):
    def __init__(self, val):
        self.val=val
    def __call__(self,image):
        dbls=oofimage.grayify(image)
        imageops.printHistogram(dbls,self.val)

registeredclass.Registration(
    "MakeHistogram",
    imagemodifier.ImageModifier,
    MakeHistogram,
    ordering=300,
    params=[parameter.IntParameter('val',value=20)],
    tip="Creates a histogram"
)

class compareImages(imagemodifier.ImageModifier):
    def __init__(self, val):
        self.val=val
    def __call__(self,image):
        dbls=oofimage.grayify(image)
        bool1=oofimage.threshold(dbls,.5)
        imageops.compare(bool1,self.val)

registeredclass.Registration(
    "compareImages",
    imagemodifier.ImageModifier,
    compareImages,
    ordering=400,
    params=[parameter.IntParameter('val',value=3)],
    tip="Compare 2 images"
)

class houghTransform(imagemodifier.ImageModifier):
  ##  def __init__(self):
    def __call__(self, image):
        dbls = oofimage.grayify(image)
        bools = oofimage.threshold(dbls,.5)
        hough = imageops.houghTrans(bools)

registeredclass.Registration(
    "houghTransform",
    imagemodifier.ImageModifier,
    houghTransform,
    ordering=1000,
    params=[]
    )

##############################################################################
# Thresholding Functions
##############################################################################

class ImageThreshold(registeredclass.RegisteredClass):
    registry = []
    def __call__(self,image):
        pass


class HysteresisThreshold(ImageThreshold):
    def __init__(self,T1,T2):
        self.T1=T1
        self.T2=T2
    def __call__(self, image):
        dbls = oofimage.grayify(image)
        bools = imageops.hysteresisThresh(dbls,self.T1,self.T2)
        oofimage.setFromBool(image,bools)
        
registeredclass.Registration(
    'HysteresisThreshold',
    ImageThreshold,
    HysteresisThreshold,
    ordering=100,
    params=[
    parameter.FloatRangeParameter('T1', (0,1,.01),value=.5,
                                  tip="Lower threshold value between 0 and 1"),
    parameter.FloatRangeParameter('T2', (0,1,.01),value=.5,
                                  tip="Higher threshold value between 0 and 1")
    ],
    tip="Threshold an image given a threshold value."
)

## This ThresholdFilter is an exact copy of ThresholdImage from imagemodifier.
## This copy is used in the completeDetection function while the other one
## shows up in the main "Image" menu in OOF. Copying this was the simplest way
## to have the function show up in both places, but a more "elegant" solution
## could be used later.

class ThresholdFilter(ImageThreshold):
    def __init__(self, T):
        self.T=T
    def __call__(self, image):
        dbls = oofimage.grayify(image)
        bools = oofimage.threshold(dbls,self.T)
        oofimage.setFromBool(image,bools)
        
registeredclass.Registration(
    'ThresholdFilter',
    ImageThreshold,
    ThresholdFilter,
    ordering=100,
    params=[parameter.FloatRangeParameter('T', (0,1,.01),value=.5,
                                          tip="Threshold value."),
            ],
    tip="Threshold an image given a threshold value."
##    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/threshold.xml')
    )

##############################################################################


class CompleteDetection(imagemodifier.ImageModifier):
    def __init__(self,filter,threshold):
        self.filter=filter
        self.threshold=threshold
    def __call__(self, image):
        self.filter.__call__(image)
        self.threshold.__call__(image)
        
registeredclass.Registration(
    'CompleteDetection',
    imagemodifier.ImageModifier,
    CompleteDetection,
    ordering=100000,
    params=[
    parameter.RegisteredParameter('filter', imagefilter.ImageFilter,
                                  tip = 'Choose the image filter to use'),
    parameter.RegisteredParameter('threshold', ImageThreshold,tip='Thresh')
##    parameter.RegisteredParameter('
    ],
    tip = 'Apply full edge detection process.',
)
