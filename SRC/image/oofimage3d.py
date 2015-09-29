# -*- python -*-
# $RCSfile: oofimage3d.py,v $
# $Revision: 1.5 $
# $Author: langer $
# $Date: 2010/12/04 03:50:04 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import timestamp
from ooflib.common import debug
from ooflib.common import utils
from ooflib.common import parallel_enable
from ooflib.common import primitives
from ooflib.common import color
from ooflib.common.IO import whoville
import ooflib.common.microstructure
from ooflib.image.imagecontext import *
import os
import string
import imghdr
import copy
import math


class ImageResample:
    # Container class for resample information, so we can do and undo resamples easily.

    def __init__(self, voxels, tint_color, tint_alpha, overall_alpha):
        self.voxels = voxels
        self.tint_color = tint_color
        self.tint_alpha = tint_alpha
        self.overall_alpha = overall_alpha
        self.original_colors = []

    # TODO: perhaps this should be in the image
    # class... image.doResample(resample) instead of
    # resample.doResample(image)

    # TODO: Fix this for non zero fourth channel value
    def doResample(self, image):
        newimage = image.deepCopy()
        for voxel in self.voxels:
            current = image[voxel]
            self.original_colors.append(current)
            newcolor = (self.tint_alpha*255*self.tint_color.getRed() \
                          + (1-self.tint_alpha)*255*current.getRed(),
                        self.tint_alpha*255*self.tint_color.getGreen() \
                          + (1-self.tint_alpha)*255*current.getGreen(),
                        self.tint_alpha*255*self.tint_color.getBlue() \
                          + (1-self.tint_alpha)*255*current.getBlue())
            for i in xrange(3):
                newimage.image.SetScalarComponentFromFloat(voxel[0],voxel[1],voxel[2],i,newcolor[i])
            alpha = 255*math.log(101-100*self.overall_alpha)/math.log(101);
            newimage.image.SetScalarComponentFromFloat(voxel[0],voxel[1],voxel[2],3,alpha)
        return newimage

    def undoResample(self, image):
        newimage = image.deepCopy()
        j=0
        for voxel in self.voxels:
            newcolor = (255*self.original_colors[j].getRed(),
                        255*self.original_colors[j].getGreen(),
                        255*self.original_colors[j].getBlue())
            j+=1
            for i in xrange(3):
                newimage.image.SetScalarComponentFromFloat(voxel[0],voxel[1],voxel[2],i,newcolor[i])
            newimage.image.SetScalarComponentFromFloat(voxel[0],voxel[1],voxel[2],3,1.0)
        return newimage


# Python version of the OOFImage3D class -- eventually we will rewrite
# in C++ for performance


class OOFImage3D:

    def __init__(self, name=None, firstimage=None, filepattern=None, numfiles=None):

        # eventually this will be C++ and we will have multiple constructors
        if (name is not None and firstimage is not None
            and filepattern is not None and numfiles is not None):
            self._name = name
            self._timestamp = timestamp.TimeStamp()

            format = imghdr.what(firstimage)
            depth = numfiles

            readers = {'pbm':vtk.vtkPNMReader,
                       'pgm':vtk.vtkPNMReader,
                       'ppm':vtk.vtkPNMReader,
                       'bmp':vtk.vtkBMPReader,
                       'jpeg':vtk.vtkJPEGReader,
                       'tiff':vtk.vtkTIFFReader,
                       'png':vtk.vtkPNGReader}

            try:
                imageReader = readers[format]()
            except KeyError:
                raise ooferror.ErrUserError("Unrecognized Image Format")

            # the width and height are set based on the actual image size
            imageReader.SetDataExtent(0,0,0,0,0,depth-1)
            imageReader.SetDataSpacing(1,1,1)
            imageReader.SetFilePattern(filepattern)
            self.image = imageReader.GetOutput()
            self.image.Update()
            self.makeFourChannel()
            self.padImage()

            self.setup()

    def deepCopy(self):
        # will be replaced with a copy constructor when we convert to C++
        newoofimage = OOFImage3D()
        copy = vtk.vtkImageData()
        copy.DeepCopy(self.image)
        newoofimage.image = copy
        newoofimage.setup()
        return newoofimage


    def __getitem__(self, idx):
##         num_components = self.image.GetNumberOfScalarComponents()
##         if num_components == 1:
##             return color.Gray(self.image.GetScalarComponentAsFloat(idx[0],idx[1],idx[2],0)/255)
##         elif num_components == 3 or num_components == 4:

        # Don't return the alpha channel since we just use it for
        # manipulating the visualization of materials, selected
        # regions, active areas, etc.
        return color.RGBColor(
            self.image.GetScalarComponentAsFloat(idx[0],idx[1],idx[2],0)/255,
            self.image.GetScalarComponentAsFloat(idx[0],idx[1],idx[2],1)/255,
            self.image.GetScalarComponentAsFloat(idx[0],idx[1],idx[2],2)/255)


    def padImage(self, amount=1):
        # pad the image with extra voxels because of vtk off by 1
        # annoyance in calculating image bounds

        self.image.Update()
        extent = list(self.image.GetExtent())
        if extent[1]+amount<=1 or extent[3]+amount<=1 or extent[5]+amount<=1:
            raise ooferror.ErrSetupError("Image dimensions too small")

        for i in xrange(1,7,2):
            extent[i] += amount
        padder = vtk.vtkImageConstantPad()
        padder.SetInput(self.image)
        padder.SetOutputWholeExtent(extent) 
        padder.SetConstant(255)
        temp = padder.GetOutput()
        self.image = temp
        self.image.Update()


    def makeFourChannel(self):
        # We make all images, even if they are grayscale, four
        # channel.  Since we need to resample the image when we select
        # voxels, etc, we always need 3 channels for RGB.  In order to
        # display one material or pixel group at a time, such as with
        # active area, we need an alpha channel.  If all of these
        # channels are initialized once in the beggining, rendering
        # selected voxels, active areas, etc, will be more responsive.

        # The initial image will have 1 to 4 channels.
        num_components = self.image.GetNumberOfScalarComponents()

        if num_components > 4:
            raise ooferror.ErrUserError("Image must have four or less components.")

        imagecopy = vtk.vtkImageData()
        imagecopy.DeepCopy(self.image)

        if num_components != 4:

            # extract the first component
            extractor = vtk.vtkImageExtractComponents()
            extractor.AddInputConnection(imagecopy.GetProducerPort())
            extractor.SetComponents(0)

            # append the first component up to 3 times.
            appender = vtk.vtkImageAppendComponents()
            if num_components < 3:
                # only use the first component if we have less than 3 components
                for i in xrange(num_components):
                    appender.AddInputConnection(extractor.GetOutputPort())
            else:
                # otherwise use all of the components
                appender.AddInputConnection(imagecopy.GetProducerPort())
            for i in xrange(4-num_components):
                appender.AddInputConnection(extractor.GetOutputPort())
            imagecopy = appender.GetOutput()
            imagecopy.Update()
            imagecopy.UpdateInformation()

        # Set all voxels to have full opacity.  This will be slow but
        # eventually we are converting this class to C++.
        sighs = imagecopy.GetDimensions()
        for i in xrange(sighs[0]):
            for j in xrange(sighs[1]):
                for k in xrange(sighs[2]):
                    # For some bizarre reason, vtk doesn't like
                    # rendering images when the alpha component is
                    # initialized above 100 or so.  So the numbers on
                    # the fourth component will represent the
                    # translucency - 0 indicates an opaque image and
                    # 255 indicates complete transparency.
                    imagecopy.SetScalarComponentFromFloat(i,j,k,3,0.0)
        imagecopy.Update()
        imagecopy.UpdateInformation()
        self.image = imagecopy


    def clone(self, nm):
        newoofimage3d = copy.copy(self)
        newoofimage3d.rename(nm)
        return newoofimage3d


    def setSize(self, sighs):

        self._size = sighs
        if self._sizeInPixels != self._size:
            tempimage = vtk.vtkImageData()
            changer = vtk.vtkImageChangeInformation()

            x_spacing = self._size[0]/self._sizeInPixels[0]
            y_spacing = self._size[1]/self._sizeInPixels[1]
            z_spacing = self._size[2]/self._sizeInPixels[2]
            tempimage = self.image
            changer.SetInput(tempimage)
            if not (x_spacing and y_spacing and z_spacing):
                raise ooferror.ErrSetupError("Pixels have zero size!")
            changer.SetOutputSpacing(x_spacing, y_spacing, z_spacing)
            self.image = changer.GetOutput()
            self.image.Update()


    def setup(self):
        sighs = self.image.GetDimensions()
        # subtract 1 because of padding
        self._sizeInPixels = primitives.iPoint(sighs[0]-1, sighs[1]-1, sighs[2]-1)


    def name(self):
        return self._name

    def rename(self, newname):
        self._name = newname

    def size(self):
        return self._size

    def sizeInPixels(self):
        return self._sizeInPixels

    def setMicrostructure(self, ms):
        self._microstructure = ms

    def getCMicrostructure(self):
        return self._microstructure

    def removeMicrostructure(self):
        self._microstructure = 0

    # no longer needed....
    def getImageData(self):
        return self.image

    def getVolumeActor(self):
        # return a volume actor based on the image for rendering in the canvas
        extent = self.image.GetExtent()
        mapper = vtk.vtkFixedPointVolumeRayCastMapper()
        mapper.IntermixIntersectingGeometryOn()
        mapper.SetInput(self.image)

        volproperty = vtk.vtkVolumeProperty()
        volproperty.IndependentComponentsOff()

        opacity = vtk.vtkPiecewiseFunction()
        opacity.AddSegment(0,1,255,0)
        volproperty.SetScalarOpacity(opacity)

        volume = vtk.vtkVolume()
        volume.SetMapper(mapper)
        volume.SetProperty(volproperty)
        return volume

    def addImageToPicker(self, picker):
        picker.SetImage(self.image)


    def resampleVoxel(self, voxel, tintcolor, tintopacity, overallopacity):
        current = self[voxel]
        newcolor = (tintopacity*255*tintcolor.getRed() + (1-tintopacity)*255*current.getRed(),
                    tintopacity*255*tintcolor.getGreen() + (1-tintopacity)*255*current.getGreen(),
                    tintopacity*255*tintcolor.getBlue() + (1-tintopacity)*255*current.getBlue())
        for i in xrange(3):
            self.image.SetScalarComponentFromFloat(voxel[0],voxel[1],voxel[2],i,newcolor[i])
        alpha = 255*math.log(101-100*overallopacity)/math.log(101);
        self.image.SetScalarComponentFromFloat(voxel[0],voxel[1],voxel[2],3,alpha)


    def pixelInBounds(self, coord):
        if coord[0]<0 or coord[0]>=self.sizeInPixels[0] \
           or coord[1]<0 or coord[1]>=self.sizeInPixels[1] \
           or coord[1]<0 or coord[1]>=self.sizeInPixels[1]:
            return False
        return True

    def getPixels(self):
        # VERY slow!!!
        string = ""
        numcomponents = self.image.GetNumberOfScalarComponents()
        for i in xrange(self._sizeInPixels[0]):
            for j in xrange(self._sizeInPixels[1]):
                for k in xrange(self._sizeInPixels[2]):
                    for c in xrange(numcomponents):
                        string = string + str(self.image.GetScalarComponentAsFloat(i,j,k,c)) + " "
        return string

    def save(self, filename):
        writer = vtk.vtkMetaImageWriter()
        writer.SetFileName(filename)
        writer.SetInput(self.image)
        writer.Write()

    def getTimeStamp(self):
        return self._timestamp

    def imageChanged(self):
        self.image.Update()
        self.image.UpdateInformation()
        self._timestamp.increment()

    def getRGB(self):
        extractor = vtk.vtkImageExtractComponents()
        extractor.SetInput(self.image)
        extractor.SetComponents(0,1,2)
        rgb = extractor.GetOutput()
        rgb.Update()
        return rgb

    def getAlpha(self):
        extractor = vtk.vtkImageExtractComponents()
        extractor.SetInput(self.image)
        extractor.SetComponents(3)
        alpha = extractor.GetOutput()
        alpha.Update()
        return alpha

    def combineChannels(self, color, alpha):
        # TODO - consolidate with makeFourChannel"
        appender = vtk.vtkImageAppendComponents()
        numcomponents = color.GetNumberOfScalarComponents()
        if numcomponents == 1:
            for i in xrange(3): appender.AddInput(color)
        elif numcomponents == 3:
            appender.AddInput(color)
        appender.AddInput(alpha)
        return appender.GetOutput()
        
    def gray(self):
        # extract first three components and find luminance
        rgb = self.getRGB()
        luminance = vtk.vtkImageLuminance()
        luminance.SetInput(rgb)
        gray = luminance.GetOutput()

        # extract alpha from original image
        alpha = self.getAlpha()

        # put it all back together
        self.image = self.combineChannels(gray, alpha)

        self.imageChanged()

    def threshold(self, T):
        # extract first three components and find luminance
        rgb = self.getRGB()
        luminance = vtk.vtkImageLuminance()
        luminance.SetInput(rgb)
        gray = luminance.GetOutput()

        # extract alpha from original image
        alpha = self.getAlpha()

        # threshold the luminance
        thresholder = vtk.vtkImageThreshold()
        thresholder.ThresholdByUpper(T*255)
        thresholder.SetOutValue(0)
        thresholder.SetInput(gray)

        thresholder2 = vtk.vtkImageThreshold()        
        thresholder2.ThresholdByLower(T*255)
        thresholder2.SetOutValue(255)
        thresholder2.SetInput(thresholder.GetOutput())
        
        # put it all back together
        self.image = self.combineChannels(thresholder2.GetOutput(), alpha)
    
        self.imageChanged()

    def blur(self, radius, stddev):
        self.padImage(-1)
        gauss = vtk.vtkImageGaussianSmooth()
        gauss.SetRadiusFactors(radius, radius, radius)
        gauss.SetStandardDeviation(stddev, stddev, stddev)
        gauss.SetInput(self.image)
        self.image = gauss.GetOutput()
        
        self.padImage()
        self.imageChanged()


    def dim(self, factor):
        # TODO LATER: handle case where value is greater than 1.
        rgb = self.getRGB()
        alpha = self.getAlpha()
        dimmer = vtk.vtkImageMathematics()
        dimmer.SetOperationToMultiplyByK()
        dimmer.SetConstantK(factor)
        dimmer.SetInput(rgb)
        rgb = dimmer.GetOutput()
        rgb.SetScalarTypeToUnsignedChar()
        rgb.Update()
        self.image = self.combineChannels(rgb,alpha)
        self.imageChanged()


    def fade(self, factor):
        rgb = self.getRGB()
        alpha = self.getAlpha()
        fadestep1 = vtk.vtkImageMathematics()
        fadestep1.SetOperationToMultiplyByK()
        fadestep1.SetConstantK(1.0-factor)
        fadestep1.SetInput(rgb)
        fadestep2 = vtk.vtkImageMathematics()
        fadestep2.SetOperationToAddConstant()
        fadestep2.SetConstantC(255*factor)
        fadestep2.SetInput(fadestep1.GetOutput())
        rgb = fadestep2.GetOutput()
        rgb.SetScalarTypeToUnsignedChar()
        rgb.Update()
        self.image = self.combineChannels(rgb,alpha)
        self.imageChanged()


    def negate(self, dummy):
        # dummy input is a hack to keep compatibility with 2D code
        rgb = self.getRGB()
        alpha = self.getAlpha()
        negator = vtk.vtkImageMathematics()
        negator.SetOperationToMultiplyByK()
        negator.SetConstantK(-1.0)
        negator.SetInput(rgb)
        # we need to add 255 again to avoid getting artifacts due to
        # truncation.
        adder = vtk.vtkImageMathematics()
        adder.SetOperationToAddConstant()
        adder.SetConstantC(255)
        adder.SetInput(negator.GetOutput())
        rgb = adder.GetOutput()
        rgb.SetScalarTypeToUnsignedChar()
        rgb.Update()
        self.image = self.combineChannels(rgb,alpha)
        self.imageChanged()

    def medianFilter(self, radius):
        rgb = self.getRGB()
        alpha = self.getAlpha()
        median = vtk.vtkImageMedian3D()
        median.SetKernelSize(radius*2, radius*2, radius*2)
        median.SetInput(rgb)
        self.image = self.combineChannels(median.GetOutput(),alpha)
        self.imageChanged()

    def normalize(self):
        self.padImage(-1)
        numcomponents = self.image.GetNumberOfScalarComponents()
        appender = vtk.vtkImageAppendComponents()

        # In order to process an image one channel at a time, by
        # extracting, processing, and appending, we must keep all
        # parts of the pipeline separate for each channel
        results = {}
        adder = {}
        mult = {}
        extractor = {}

        for c in xrange(4):
            # we only want to normalize the first three channels, but
            # because of the conditions, this should do nothing to the
            # fourth channel.  We still need to extract and append the
            # fourth channel.

            extractor[c] = vtk.vtkImageExtractComponents()
            extractor[c].SetInput(self.image)
            extractor[c].SetComponents(c)
            results[c] = extractor[c].GetOutput()
            results[c].Update()
            (mincolor,maxcolor) = results[c].GetScalarRange()
 
            if mincolor > 0 and mincolor!=maxcolor and c < 3:
                adder[c] = vtk.vtkImageMathematics()
                adder[c].SetOperationToAddConstant()
                adder[c].SetConstantC(256-mincolor)
                adder[c].SetInput(results[c])            
                results[c] = adder[c].GetOutput()
                results[c].Update()

            if mincolor!=maxcolor and c < 3:
                K = 255.0/(maxcolor-mincolor)
                mult[c] = vtk.vtkImageMathematics()
                mult[c].SetOperationToMultiplyByK()
                mult[c].SetConstantK(K)
                mult[c].SetInput(results[c])
                results[c] = mult[c].GetOutput()
                results[c].Update()


            appender.AddInputConnection(results[c].GetProducerPort())

        self.image = appender.GetOutput()
        self.image.SetScalarTypeToUnsignedChar()
        self.padImage()
        self.imageChanged()


    def flip(self, axiskey):
        self.padImage(-1)
        axes = {'x':[0],
                'y':[1],
                'z':[2],
                'xy':[0,1],
                'yz':[1,2],
                'xz':[0,2],
                'xyz':[0,1,2]}
        for axis in axes[axiskey]:
            flipper = vtk.vtkImageFlip()
            flipper.SetFilteredAxis(axis)
            flipper.SetInput(self.image)
            self.image = flipper.GetOutput()
            self.image.Update()
        self.padImage()
        self.imageChanged()
        

    # TODO LATER:
    # Despeckle - subtract off low frequency
    # Edge - get low frequency
    # Enhance - might not need to do this one - the imagemagick documentation is missing - and we have other smoothers
    # Equalize - histogram equalization, channel by channel
    # ReduceNoise - might not want to do - it would be slow
    # Sharpen - convolve with gaussian (how to make this the opposite of blur?)
    # Reilluminate - something we wrote - don't know if we can do it for 3d
    # Contrast - what is the algorithm
    


def readImage(filepattern, **kwargs):
    # We make the basename the name of the first
    # image, we also use this in OOFImage3D to probe the image type
    # using ImageMagick.
    dirname = os.path.dirname(filepattern)
    numfiles = utils.countmatches(filepattern, dirname, utils.matchvtkpattern)
    if numfiles == 0:
        raise ooferror.ErrUserError("No files match pattern: "+filepattern)
    # return something?
    else:
        items = os.listdir(dirname)
        for item in items:
            if utils.matchvtkpattern(filepattern, item):
                basename = item
        firstimagename = os.path.join(dirname, basename)

        # vtk wants a file pattern with some string that includes
        # integers.  The pattern must be sprintf style with '%i' where the
        # integers belong.
        pattern = string.replace(filepattern, "*", "%i")
        image = OOFImage3D(os.path.basename(filepattern), firstimagename, pattern, numfiles)
        # set physical size of image
        pixelsize = image.sizeInPixels()
        given_height = 'height' in kwargs
        given_width = 'width' in kwargs
        given_depth = 'depth' in kwargs
    ##     if not (given_height or given_width or given_depth):
    ##         width = float(pixelsize.x)
    ##         height = float(pixelsize.y)
    ##         depth = float(pixelsize.z)
    ##     elif given_height and given_width and given_depth:
    ##         width = float(kwargs['width'])
    ##         height = float(kwargs['height'])
    ##         depth = float(kwargs['depth'])
    ##     else:
    ##         #aspect = float(pixelsize.x)/pixelsize.y
    ##         if given_width:
    ##             width = float(kwargs['width'])
    ##             height = width/aspect
    ##         elif given_height:
    ##             height = float(kwargs['height'])
    ##             width = height*aspect
        # for now, this works differently from the 2d version.  Any
        # dimension not explicity set gets set to 1. TODO: figure out the
        # aspect ratio stuff.  Should it just use the largest of the ones
        # that are set?
        if given_width:
            width = float(kwargs['width'])
        else:
            width = float(pixelsize.x)
        if given_height:
            height = float(kwargs['height'])
        else:
            height = float(pixelsize.y)
        if given_depth:
            depth = float(kwargs['depth'])
        else:
            depth = float(pixelsize.z)

        image.setSize(primitives.Point(width, height, depth))

        return image

# TODO: much of this code is repeated from oofimage.spy, perhaps
# should be consolidated?
## def _getTimeStamp_optional_args(self, *args):
##     return self._getTimeStamp()
## OOFImagePtr.getTimeStamp = _getTimeStamp_optional_args

def getImage(imagename):
    ## returns the actual image
    ## imagename = microstructurename:image_name OR imagename = [microstructurename, image_name]
    return imageContexts[imagename].getObject()

def pushModification(imagename, image):
    imageContexts[imagename].pushModification(image)

def undoModification(imagename):
    imageContexts[imagename].undoModification()

def redoModification(imagename):
    imageContexts[imagename].redoModification()

def undoable(imagename):
    return imageContexts[imagename].undoable()

def redoable(imagename):
    return imageContexts[imagename].redoable()





