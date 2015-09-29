# -*- python -*-
# $RCSfile: imagefilter.py,v $
# $Revision: 1.5 $
# $Author: langer $
# $Date: 2014/09/27 21:41:30 $

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
from ooflib.SWIG.image import oofimage

## This file contains all the edge detection filters. They are derived from
## the class ImageFilter and appear in the Image menu under the function
## CompleteDetection.



class ImageFilter(registeredclass.RegisteredClass):
    registry = []
    def __call__(self, image):
        pass

class NewGaborModifier(ImageFilter):
    def __init__(self, a, b, numAngles,Line_color):
        self.a = a
        self.b = b
        self.numAngles=numAngles
        self.Line_color=Line_color
    def __call__(self, image):
##        dbls=imageops.grayify(image)
##        final = imageops.newGabor(dbls,self.a,self.b,0)
##        gradDirs=intarray.makeIntArray(image.sizeInPixels(),0)
##        for i in range(self.numAngles-1):
##            phi = (i+1)*180./self.numAngles
##            temp = imageops.newGabor(dbls,self.a,self.b,phi)
##            final = imageops.findLargerVals2(final,temp,gradDirs,i+1)
##        scaled = imageops.scaleArray(final,0.0,1.0,self.Line_color)
##        scaled = imageops.nonmaxSuppress(scaled,gradDirs);
##        imageops.setFromArray(image,scaled)
        
        dbls = oofimage.grayify(image)
        for i in range(self.numAngles): 
            phi = i*180./self.numAngles
            current = imageops.newGabor(dbls,self.a,self.b,phi)
            if i!=0:
                old=imageops.findLargerVals(current,old)
            else:
                old=current

        scaled = imageops.scaleArray(old, 0.0, 1.0,self.Line_color)

        imageops.setFromArray(image,scaled)
        
registeredclass.Registration(
    'NewGabor',
    ImageFilter,
    NewGaborModifier,
    ordering=100,
    params=[
    parameter.IntParameter('a',  value=3, tip="a in pixels"),
    parameter.IntParameter('b',  value=5, tip="b in pixels"),
    parameter.IntParameter('numAngles',value=4,
                       tip="number of angles to apply the filter"),
    parameter.IntParameter('Line_color', value=2,
                        tip="Colors of the lines to detect. (2) Both white and dark lines. (1) Only white lines (0) Only black lines.")
    ],
    tip="Apply a new Gabor filter to detect edges"
)

class RealGaborModifier(ImageFilter):
    def __init__(self, a, b, numAngles):
        self.a = a
        self.b = b
        self.numAngles=numAngles
    def __call__(self, image):
        dbls = oofimage.grayify(image)
        for i in range(self.numAngles): 
            phi = i*180./self.numAngles
            current = imageops.realGabor(dbls,self.a,self.b,phi)
            if i!=0:
                old=imageops.findLargerVals(current,old)
            else:
                old=current

        scaled = imageops.scaleArray2(old, 0.0, 1.0)
        imageops.setFromArray(image,scaled)
        
registeredclass.Registration(
    'RealGabor',
    ImageFilter,
    RealGaborModifier,
    ordering=100,
    params=[
    parameter.IntParameter('a',  value=3, tip="a in pixels"),
    parameter.IntParameter('b',  value=3, tip="b in pixels"),
    parameter.IntParameter('numAngles',value=6,
                       tip="number of angles to apply the filter")
    ],
    tip="Apply a real Gabor filter to detect edges"
)

class ImagGaborModifier(ImageFilter):
    def __init__(self, a, b, numAngles):
        self.a = a
        self.b = b
        self.numAngles=numAngles      
    def __call__(self, image):
        dbls = oofimage.grayify(image)
        for i in range(self.numAngles):
            phi = i*180./self.numAngles
            current = imageops.imagGabor(dbls,self.a,self.b,phi)
            if i!=0:
                old=imageops.findLargerVals(current,old)
            else:
                old=current           
        scaled = imageops.scaleArray2(old, 0.0, 1.0)
        imageops.setFromArray(image,scaled)        
     
registeredclass.Registration(
    'ImaginaryGabor',
    ImageFilter,
    ImagGaborModifier,
    ordering=100,
    params=[
    parameter.IntParameter('a',  value=3, tip="a in pixels"),
    parameter.IntParameter('b',  value=3, tip="b in pixels"),
    parameter.IntParameter('numAngles',value=6,
                       tip="number of angles to apply the filter") 
    ],
    tip="Apply an imaginary Gabor filter to detect edges"
)

class ModGaborModifier(ImageFilter):
    def __init__(self, a, b, numAngles):
        self.a = a
        self.b = b
        self.numAngles=numAngles  
    def __call__(self, image):
        dbls = oofimage.grayify(image)
        for i in range(self.numAngles):
            phi = i*180./self.numAngles
            current = imageops.modGabor(dbls,self.a,self.b,phi)
            if i!=0:
                old=imageops.findLargerVals(current,old)
            else:
                old=current          
        scaled = imageops.scaleArray2(old, 0.0, 1.0)
        imageops.setFromArray(image,scaled)        
        
registeredclass.Registration(
    'ModifiedGabor',
    ImageFilter,
    ModGaborModifier,
    ordering=100,
    params=[
    parameter.IntParameter('a',  value=3, tip="a in pixels"),
    parameter.IntParameter('b',  value=3, tip="b in pixels"),
    parameter.IntParameter('numAngles',value=6,
                       tip="number of angles to apply the filter")
    ],
    tip="Apply a modified Gabor filter to detect edges"
)

class GaborModifier(ImageFilter):
    def __init__(self, a, b, numAngles):
        self.a = a
        self.b = b
        self.numAngles=numAngles     
    def __call__(self, image):
        dbls=oofimage.grayify(image)
        
        for i in range(self.numAngles):
            phi = i*180./self.numAngles
            current = imageops.normGabor(dbls,self.a,self.b,phi)
            if i!=0:
                old=imageops.findLargerVals(current,old)
            else:
                old=current
    
        scaled=imageops.scaleArray2(old,0.0,1.0)
        imageops.setFromArray(image,scaled)            
        
registeredclass.Registration(
    'NormalGabor',
    ImageFilter,
    GaborModifier,
    ordering=100,
    params=[
    parameter.IntParameter('a',  value=3, tip="a in pixels"),
    parameter.IntParameter('b',  value=3, tip="b in pixels"),
    parameter.IntParameter('numAngles',value=6,
                       tip="number of angles to apply the filter")
    ],
    tip="Apply the normal Gabor filter to detect edges"
)



class SobelModifier(ImageFilter):
    def __call__(self, image):
        dbls = oofimage.grayify(image)
        temp1=imageops.sobel(dbls,0)
        temp2=imageops.sobel(dbls,2)
        combined=imageops.combineVals(temp1,temp2)  
           
        scaled = imageops.scaleArray2(combined, 0.0, 1.0)

        imageops.setFromArray(image,scaled)
        
registeredclass.Registration(
    'Sobel',
    ImageFilter,
    SobelModifier,
    ordering=200,
    params=[    ],
    tip="Apply the Sobel mask to detect edges"
)

class CannyModifier(ImageFilter):
    def __init__(self, stdDev):
        self.stdDev=stdDev
    def __call__(self, image):
        dbls = oofimage.grayify(image)
        largest=imageops.canny(dbls,self.stdDev)
 ##       smoothed = imageops.gaussSmooth(dbls,self.stdDev)
        
##        for i in range(4):
##            temp=imageops.sobel(smoothed,i)
##            if i!=0:
##                largest=imageops.findLargerVals(largest,temp)
##            else:
##                largest=temp 
           
        scaled = imageops.scaleArray2(largest, 0.0, 1.0)

        imageops.setFromArray(image,scaled)
        
registeredclass.Registration(
    'Canny',
    ImageFilter,
    CannyModifier,
    ordering=200,
    params=[ parameter.FloatParameter('stdDev', value=1,
                       tip="Standard deviation for the gaussian smoothing")    ],
    tip="Apply the Canny Edge Detector to detect edges"
)

class LaplacianFilterModifier(ImageFilter):
    def __call__(self, image):
        dbls = oofimage.grayify(image)
        temp = imageops.laplacian(dbls)  
        scaled = imageops.scaleArray2(temp, 0.0, 1.0)
        imageops.setFromArray(image,scaled)
        
registeredclass.Registration(
    'LaplacianFilter',
    ImageFilter,
    LaplacianFilterModifier,
    ordering=200,
    params=[ ],
    tip="Apply the Laplacian Filter to detect edges"
)

class LaplacianGaussFilterModifier(ImageFilter):
    def __init__(self, stdDev):
        self.stdDev=stdDev
    def __call__(self, image):
        dbls = oofimage.grayify(image)
        temp = imageops.laplacGauss(dbls,self.stdDev)  
        scaled = imageops.scaleArray2(temp, 0.0, 1.0)
        imageops.setFromArray(image,scaled)
        
registeredclass.Registration(
    'LaplacianGaussFilter',
    ImageFilter,
    LaplacianGaussFilterModifier,
    ordering=200,
    params=[ parameter.FloatParameter('stdDev', value=1,
                       tip="Standard deviation for the filter") ],
    tip="Apply the Laplacian Filter to detect edges"
)
