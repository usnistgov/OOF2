# -*- python -*-
# $RCSfile: imagemenu.py,v $
# $Revision: 1.88 $
# $Author: langer $
# $Date: 2014/12/23 17:13:36 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import progress
from ooflib.SWIG.image import autogroupMP
if config.dimension() == 2:
    from ooflib.SWIG.image import oofimage
elif config.dimension() == 3:
    from ooflib.SWIG.image import oofimage3d as oofimage
from ooflib.common import debug
from ooflib.common import labeltree
from ooflib.common import parallel_enable
from ooflib.common import utils
from ooflib.common.IO import automatic
from ooflib.common.IO import filenameparam
from ooflib.common.IO import mainmenu
from ooflib.common.IO import microstructuremenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
from ooflib.image import imagecontext
from ooflib.image import imagemodifier
import ooflib.common.microstructure

import os.path

imagemenu = mainmenu.OOF.addItem(oofmenu.OOFMenuItem(
    'Image',
    cli_only=1,
    help='Operations involving Images.'))

imagemodmenu = mainmenu.OOF.Image.addItem(oofmenu.OOFMenuItem(
    'Modify',
    help='Tools for modifying images.'
    ))

def buildImageModMenu():
    imagemodmenu.clearMenu()
    for registration in imagemodifier.ImageModifier.registry:
        try:
            help = registration.tip
        except AttributeError:
            help = None
        params = [whoville.WhoParameter('image', whoville.getClass('Image'),
                                        tip=parameter.emptyTipString)] \
                 + registration.params
        menuitem = imagemodmenu.addItem(
            oofmenu.OOFMenuItem(registration.name(),
                                callback=imagemodifier.doImageMod,
                                params=params,
                                help=help,
                                discussion=registration.discussion))
        menuitem.data = registration

switchboard.requestCallback(imagemodifier.ImageModifier, buildImageModMenu)
buildImageModMenu()

###################################

# Size params are reused several times
sizeparams = parameter.ParameterGroup(
    parameter.AutoNumericParameter('height',
                                   automatic.automatic,
                                   tip= \
                                   "Physical height of image, or 'automatic'."),
    parameter.AutoNumericParameter('width',
                                   automatic.automatic,
                                   tip= \
                                   "Physical width of image, or 'automatic'."))

if config.dimension() == 3:
    sizeparams.append(parameter.AutoNumericParameter(
        'depth',
        automatic.automatic,
        tip= \
        "Physical depth of image, or 'automatic'."))
                      

###################################

def loadImage(menuitem, filename, microstructure, height, width, depth=0):
    if filename:
        # Read file and create an OOFImage object
        image = autoReadImage(filename, height, width, depth)
        loadImageIntoMS(image, microstructure)
        switchboard.notify("redraw")

def autoReadImage(filename, height, width, depth=0):
    kwargs = {}
    if height is not automatic.automatic:
        kwargs['height'] = height
    if width is not automatic.automatic:
        kwargs['width'] = width

    if config.dimension() == 2:
        return oofimage.readImage(filename, **kwargs) # OOFImage object

    elif config.dimension() == 3:
        if depth is not automatic.automatic:
            kwargs['depth'] = depth
        return oofimage.readImage(filename, **kwargs)
    
        
def loadImageIntoMS(image, microstructure):
    # 'image' is an OOFImage object.
    # 'microstructure' is a Microstructure name.
    
    # See if the Microstructure already exists
    msclass = whoville.getClass('Microstructure')
    try:                            # look for existing microstructure
        ms = msclass[microstructure] # Who object
    except KeyError:
        msobj = ooflib.common.microstructure.Microstructure(microstructure,
                                                     image.sizeInPixels(),
                                                     image.size())
        ms = msclass.add(microstructure, msobj, parent=None)

    # Check size of microstructure
    if ms.getObject().sizeInPixels() != image.sizeInPixels():
        raise ooferror.ErrUserError("Cannot load an image into an existing Microstructure of a different size.")

    # See if the image name is unique in the Microstructure
    newname = imagecontext.imageContexts.uniqueName([ms.name(), image.name()])
    image.rename(newname)
    # Create ImageContext object
    immidgecontext = imagecontext.imageContexts.add([ms.name(),newname], image,
                                              parent=ms)

if config.dimension() == 2:
    imageparams = parameter.ParameterGroup(
        filenameparam.ReadFileNameParameter('filename', 'image',
                                            tip="Name of the image file."),
        whoville.WhoParameter('microstructure',
                              whoville.getClass('Microstructure'),
                              tip=parameter.emptyTipString))
    
elif config.dimension() == 3:
    imageparams = parameter.ParameterGroup(
        parameter.StringParameter('filename', 'image',
                                  tip="Pattern for the image files."),
        whoville.WhoParameter('microstructure',
                              whoville.getClass('Microstructure'),
                              tip=parameter.emptyTipString))
    
mainmenu.OOF.File.Load.addItem(
    oofmenu.OOFMenuItem(
    'Image',
    callback=loadImage,
    ellipsis=1,
    params=imageparams+sizeparams,
    help="Load an Image into an existing Microstructure.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/menu/loadimage.xml')
    ))

def _sensitize(*args, **kwargs):
    if ooflib.common.microstructure.microStructures.nActual() == 0:
        mainmenu.OOF.File.Load.Image.disable()
    else:
        mainmenu.OOF.File.Load.Image.enable()

_sensitize()        
switchboard.requestCallback(('new who', 'Microstructure'), _sensitize)
switchboard.requestCallback(('remove who', 'Microstructure'), _sensitize)

##################################

# Use ImageMagick to save an image file.

def saveImage(menuitem, image, filename, overwrite):
    immidge = oofimage.getImage(image)
    if immidge and (overwrite or not os.path.exists(filename)):
        immidge.save(filename)
    else:
        reporter.warn("Image was not saved!")
    

mainmenu.OOF.File.Save.addItem(oofmenu.OOFMenuItem(
    'Image',
    callback=saveImage,
    ordering=40,
    params=[filenameparam.WriteFileNameParameter('filename', 'filename',
                                                 tip="Name of the file."),
            filenameparam.OverwriteParameter(
                'overwrite',
                tip="Whether or not to overwrite an existing file."),
            whoville.WhoParameter('image', whoville.getClass('Image'),
                                   tip=parameter.emptyTipString)],
    help="Save an Image in a file.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/menu/saveimage.xml')))

def _fix_image_save(*args):
    if imagecontext.imageContexts.nActual()==0:
        mainmenu.OOF.File.Save.Image.disable()
    else:
        mainmenu.OOF.File.Save.Image.enable()

switchboard.requestCallback(('new who', 'Image'), _fix_image_save)
switchboard.requestCallback(('remove who', 'Image'), _fix_image_save)
_fix_image_save()
    

##################################

def imageNameResolver(param, startname):
    if param.automatic():
        basename = param.group['image'].value
    else:
        basename = startname
    imagename = labeltree.makePath(basename)[-1]
    msname = labeltree.makePath(param.group['microstructure'].value)[0]
    return whoville.getClass('Image').uniqueName([msname, imagename])

def copyImage(menuitem, image, microstructure, name):
    sourceimage = oofimage.getImage(image)
    immidge = sourceimage.clone(name)
    loadImageIntoMS(immidge, microstructure)

imagemenu.addItem(oofmenu.OOFMenuItem(
    'Copy',
    ellipsis=1,
    callback=copyImage,
    params=parameter.ParameterGroup(
    whoville.WhoParameter('image', whoville.getClass('Image'),
                          tip=parameter.emptyTipString),
    whoville.NewWhoParameter('microstructure',
                             ooflib.common.microstructure.microStructures,
                             tip="Microstructure to receive copied image."),
    whoville.AutoWhoNameParameter('name',
                                  resolver=imageNameResolver,
                                  value=automatic.automatic,
                                  tip="Name to give to copied image.")
    ),
    help='Copy an Image.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/menu/copyimage.xml')
    ))


def renameImage(menuitem, image, name):
    immidge = imagecontext.imageContexts[image]
    immidge.reserve()
    immidge.begin_writing()
    try:
        immidge.rename(name, exclude=immidge.getObject().name())
    finally:
        immidge.end_writing()
        immidge.cancel_reservation()


imagemenu.addItem(oofmenu.OOFMenuItem(
    'Rename',
    callback=renameImage,
    params=[whoville.WhoParameter('image', whoville.getClass('Image'),
                                  tip=parameter.emptyTipString),
            whoville.WhoNameParameter('name', value='',
                                      tip='New name for the image')],
    help="Rename an Image.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/menu/renameimage.xml')
    ))
    
##################################


def deleteImage(menuitem, image):
    immidge = imagecontext.imageContexts[image]
    immidge.reserve()
    immidge.begin_writing()
    try:
        immidge.getMicrostructure().removeImage(immidge)
    finally:
        immidge.end_writing()
        immidge.cancel_reservation()
    switchboard.notify("redraw")

imagemenu.addItem(oofmenu.OOFMenuItem(
    'Delete',
    callback=deleteImage,
    params=[whoville.WhoParameter('image', whoville.getClass('Image'),
                                  tip=parameter.emptyTipString)
            ],
    help="Delete an Image.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/menu/deleteimage.xml')
    ))
                                      


##################################

def undoImageMod(menuitem, image):
    if parallel_enable.enabled():
        from ooflib.image.IO import oofimageIPC
        oofimageIPC.imenu.Undo(image=image)

    who = imagecontext.imageContexts[image]    
    who.begin_writing()
    oofimage.undoModification(image)
    who.end_writing()
    switchboard.notify('modified image', None, image)
    switchboard.notify('redraw')

def redoImageMod(menuitem, image):
    if parallel_enable.enabled():
        from ooflib.image.IO import oofimageIPC
        oofimageIPC.imenu.Redo(image=image)

    who = imagecontext.imageContexts[image]
    who.begin_writing()
    oofimage.redoModification(image)
    who.end_writing()
    switchboard.notify('modified image', None, image)
    switchboard.notify('redraw')

imagemenu.addItem(oofmenu.OOFMenuItem(
    'Undo',
    callback=undoImageMod,
    params=[whoville.WhoParameter('image', whoville.getClass('Image'),
                                  tip=parameter.emptyTipString)],
    help="Undo an Image modification.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/menu/undoimage.xml')
    ))

imagemenu.addItem(oofmenu.OOFMenuItem(
    'Redo',
    callback=redoImageMod,
    params=[
    whoville.WhoParameter('image', whoville.getClass('Image'),
                          tip=parameter.emptyTipString)],
    help="Redo an Image modification.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/menu/redoimage.xml')
    ))

################################

def createPixelGroups(menuitem, image, name_template):
    if name_template is None:
        name_template = '%c'            # pre-2.0.4 behavior
        
    immidgecontext = imagecontext.imageContexts[image]
    ms = immidgecontext.getMicrostructure()
    mscontext = ooflib.common.microstructure.microStructures[ms.name()]
    immidge = immidgecontext.getObject()
    prog = progress.getProgress("AutoGroup", progress.DEFINITE)
    prog.setMessage("Categorizing pixels...")
    mscontext.begin_writing()
    try:
        newgrpname = autogroupMP.autogroup(ms, immidge, name_template)
    finally:
        prog.finish()
        mscontext.end_writing()

    switchboard.notify('redraw')
        
    if not prog.stopped():      # not interrupted
        # Do this only after releasing the ms write lock!  If the main
        # thread is waiting for the read lock, then switchboard.notify
        # will deadlock here.
        if newgrpname:
            # We only have to send the notification for the most
            # recently created group.
            switchboard.notify("new pixel group", ms.findGroup(newgrpname))
        switchboard.notify("changed pixel groups", ms.name())

imagemenu.addItem(oofmenu.OOFMenuItem(
    'AutoGroup',
    callback=createPixelGroups,
    params=[whoville.WhoParameter('image', whoville.getClass('Image'),
                                  tip=parameter.emptyTipString),
            parameter.StringParameter('name_template', value='%c',
                                      tip='Name for the pixel groups. %n is replaced by a number, %c by the pixel color.')
            ],
    threadable=oofmenu.THREADABLE,
    help='Create a pixel group for each color in the image.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/menu/autogroup.xml')
    ))


###############################

# Create a Microstructure from an existing Image.  Since the Image
# exists, it must be in another Microstructure, so we have to clone
# it and add the clone to the new Microstructure.

def createMSFromImage(menuitem, name, width, height, image):
    if parallel_enable.enabled():
        # For the back-end processes
        from ooflib.image.IO import oofimageIPC
        oofimageIPC.imenu.Create_From_Image_Parallel(
            msname=name, image=image)

    # For serial mode #0 in parallel mode
    imagepath = labeltree.makePath(image)
    immidgecontext = imagecontext.imageContexts[image]
    immidge = immidgecontext.getObject().clone(imagepath[-1])

    size = immidge.size() # Point object.
    if width!=automatic.automatic:
        size[0]=width
    if height!=automatic.automatic:
        size[1]=height
        
    ms = ooflib.common.microstructure.Microstructure(name,
                                                   immidge.sizeInPixels(),
                                                   size)
    newimagecontext = imagecontext.imageContexts.add(
        [name, immidge.name()],
        immidge,
        parent=ooflib.common.microstructure.microStructures[name])
    switchboard.notify("redraw")

def msImageNameResolver(param, name):
    if param.automatic():
        imagename = param.group['image'].value
        imagepath = labeltree.makePath(imagename)
        basename = imagepath[-1]
    else:
        basename = name
    return ooflib.common.microstructure.microStructures.uniqueName(basename)

microstructuremenu.micromenu.addItem(
    oofmenu.OOFMenuItem(
    'Create_From_Image',
    callback=createMSFromImage,
    params = parameter.ParameterGroup(
    whoville.AutoWhoNameParameter('name', msImageNameResolver,
                                   automatic.automatic,
                                   tip="Name of the new Microstructure."),
    parameter.AutoNumericParameter('width', automatic.automatic,
                                   tip="Width in physical units, or automatic to use the image width."),
    parameter.AutoNumericParameter('height', automatic.automatic,
                                   tip="Height in physical units. or automatic to use the image height."),
    whoville.WhoParameter('image', imagecontext.imageContexts,
                          tip='Image on which to base the Microstructure.')),
    help="Create a Microstructure from an already loaded Image.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/menu/microfromimage.xml')
    ))

##############################

# Load an Image and create a Microstructure from it in one operation.

def createMSFromImageFile(menuitem, filename, microstructure_name,
                          height, width, depth=0):
       
 
    if (height!=automatic and height<=0) or \
           (width!=automatic and width<=0) or \
           (config.dimension()==3 and depth!=automatic and depth<=0):
        raise ooferror.ErrUserError(
            "Negative microstructure sizes are not allowed.")

    image = autoReadImage(filename, height, width, depth)
    ms = ooflib.common.microstructure.Microstructure(microstructure_name,
                                              image.sizeInPixels(),
                                              image.size())

    immidgecontext = imagecontext.imageContexts.add(
        [ms.name(), image.name()], image,
        parent=ooflib.common.microstructure.microStructures[ms.name()])
 
    if parallel_enable.enabled():
        # For the rear-end guys
        from ooflib.image.IO import oofimageIPC
        oofimageIPC.imenu.Create_From_Imagefile_Parallel(
            msname=microstructure_name,
            imagename=image.name())

    switchboard.notify("redraw")
        
def msImageFileNameResolver(param, name):
    if param.automatic():
        basename = os.path.basename(param.group['filename'].value)
    else:
        basename = name
    # Remove colons from the basename, the labeltree uses them as
    # separators, and it causes confusion if they're in the names.
    return ooflib.common.microstructure.microStructures.uniqueName(
        basename.replace(':','.'))


if config.dimension() == 2:
    imageparams=parameter.ParameterGroup(
        filenameparam.ReadFileNameParameter('filename',
                                            tip="Name of the file."),
        parameter.AutomaticNameParameter('microstructure_name',
                                     msImageFileNameResolver,
                                     automatic.automatic,
                                     tip= 'Name of the new Microstructure.'))


elif config.dimension() == 3:
    imageparams=parameter.ParameterGroup(
        parameter.StringParameter('filename',tip="Pattern for the filenames."),
        parameter.AutomaticNameParameter('microstructure_name',
                                     msImageFileNameResolver,
                                     automatic.automatic,
                                     tip= 'Name of the new Microstructure.'))
    

microstructuremenu.micromenu.addItem(oofmenu.OOFMenuItem(
    'Create_From_ImageFile',
    callback=createMSFromImageFile,
    params = imageparams + sizeparams,
    help="Load an Image and create a Microstructure from it.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/menu/microfromimagefile.xml')
                        ))
