# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Buttons for creating Microstructures from Images appear on the
# Microstructure page, but have to be defined here in the image
# module.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
if config.dimension() == 2:
    from ooflib.SWIG.image import oofimage
elif config.dimension() == 3:
    from ooflib.SWIG.image import oofimage3d
    #from ooflib.image import oofimage3d
from ooflib.common import debug
from ooflib.common import microstructure
from ooflib.common.IO import microstructuremenu
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import microstructurePage
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import tooltips
from ooflib.image.IO import imagemenu  # ensures that OOFMenuItems have been created.
from ooflib.image import imagecontext
import gtk

def newMSfromImage(button):
    menuitem = microstructuremenu.micromenu.Create_From_Image
    if parameterwidgets.getParameters(title='Create Microstructure from Image',
                                      *menuitem.params):
        menuitem.callWithDefaults()

newfromimagebutton = gtkutils.StockButton(gtk.STOCK_NEW, "New from Image")
gtklogger.setWidgetName(newfromimagebutton, "NewFromImage")
gtklogger.connect(newfromimagebutton, 'clicked', newMSfromImage)
tooltips.set_tooltip_text(newfromimagebutton,
    "Create a new Microstructure with an Image that has been loaded already.")
newfromimagebutton.set_sensitive(0)


def sensitizeNewFromImageButton():
    newfromimagebutton.set_sensitive(imagecontext.imageContexts.nActual() > 0)

microstructurePage.addNewButton(newfromimagebutton, sensitizeNewFromImageButton)

def newwhoCB(path):
    sensitizeNewFromImageButton()
    
switchboard.requestCallbackMain(('new who', 'Image'), newwhoCB)
switchboard.requestCallbackMain(('remove who', 'Image'), newwhoCB)

##############

def newMSfromImageFile(button):
    menuitem = microstructuremenu.micromenu.Create_From_ImageFile
    if parameterwidgets.getParameters(
        title='Load Image and create Microstructure',
        *menuitem.params):
        menuitem.callWithDefaults()

from ooflib.common.IO.GUI import fileselector
def newMSfromImageFiles(button):
    ## TODO 3D: Use FileSelectorWidget instead of fileSelector, and
    ## don't import fileselector anymore.
    menuitem = microstructuremenu.micromenu.Create_From_ImageFile
    wparam = menuitem.get_arg('width')
    hparam = menuitem.get_arg('height')
    dparam = menuitem.get_arg('depth')
    msparam = menuitem.get_arg('microstructure_name')
    file = fileselector.fileSelector(
        ident='Image/MS',
        mode='r',
        title='Load Images and create Microstructure',
        params=(msparam, wparam, hparam, dparam),
        pattern=True)
    # TODO 3D: We will need to make filepattern behavior more clear to
    # the user
    if file is not None:
        menuitem.callWithDefaults(filename=file)

        
if config.dimension() == 2:
    newfromfilebutton = gtkutils.StockButton(gtk.STOCK_NEW, "New from Image File")
    gtklogger.setWidgetName(newfromfilebutton, "NewFromFile")
    gtklogger.connect(newfromfilebutton, 'clicked', newMSfromImageFile)
    tooltips.set_tooltip_text(newfromfilebutton,
        "Create a new microstructure with a new image that is being loaded.")

elif config.dimension() == 3:
    newfromfilebutton = gtkutils.StockButton(gtk.STOCK_NEW, "New from Image Files")
    gtklogger.setWidgetName(newfromfilebutton, "NewFromFile")
    gtklogger.connect(newfromfilebutton, 'clicked', newMSfromImageFiles)
    tooltips.set_tooltip_text(newfromfilebutton,
        "Create a new microstructure with a new set of images that is being loaded.")
    

microstructurePage.addNewButton(newfromfilebutton)

