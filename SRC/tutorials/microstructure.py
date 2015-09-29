# -*- python -*-
# $RCSfile: microstructure.py,v $
# $Revision: 1.17 $
# $Author: langer $
# $Date: 2014/09/27 21:41:43 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.tutorials import tutorial
TutoringItem = tutorial.TutoringItem
TutorialClass = tutorial.TutorialClass

TutorialClass(subject="Microstructure",
              ordering=1,

              lessons = [
    TutoringItem(
    subject="Introduction",
    comments=

    """This tutorial covers most of the basic operations related to
    Microstructures in OOF2 by letting users create and manipulate a
    Microstructure based on a typical micrograph.

    A digitized image on a computer is nothing but a two dimensional
    array of colored pixels.  These pixels become meaningful in OOF2
    only after materials have been assigned to them or they have been
    assembled into pixel groups.

    An OOF2 Microstructure is the data structure that stores this
    information."""  ),

    TutoringItem(
    subject="Graphics Window",
    comments=

    """Open a graphics window with the BOLD(Graphics/New) command in
    the BOLD(Windows) menu.

    Let us get started by creating a microstructure from an image
    file.  """
    ),

    TutoringItem(
    subject="Locate the Data",
    comments=

    """Locate the file BOLD(K1_small.pgm) within the
    share/oof2/examples directory in your OOF2 installation.

    """
    ),
    

    TutoringItem(
    subject="Creating a Microstructure",
    comments=

    """This tutorial page contains a lot of instructions, but you
    won't be able to scroll the page after following the first
    instruction.  So before you do anything else, enlarge this window
    so that you can see all of the text.
    
    Open the BOLD(Microstructure) page in the main OOF2 window.  Click
    on BOLD(New from Image File).

    In the file selection dialog box, navigate to BOLD(K1_small.pgm).

    Look for a parameter named BOLD(microstructure_name) in the middle
    of the window.

    If you want to set the name of the microstructure yourself, click
    on the check box next to BOLD(microstructure_name) and type in a
    name.  To use an automatically generated name (which will be the
    same as the image name), leave the box unchecked.

    The parameters BOLD(width) and BOLD(height) are the physical size
    of the microstructure.  Leave these set to BOLD(automatic).  The
    size will be determined by assuming that each pixel is 1 unit
    square.

    Click BOLD(OK) to create the Microstructure.""",

    signal = ("new who", "Microstructure") ),

    TutoringItem(
    subject="A Glance at the Microstructure",
    comments=

    """As shown in the graphics window, the micrograph
    BOLD('K1_small.ppm') features two distinct materials, one in
    BOLD(black) and the other in BOLD(white).

    The boundaries between two materials are rather blurry and some
    parts of materials are not as discernable as others.

    At this point, your Microstructure object doesn't contain any
    useful information other than its size and the micrograph itself.

    The ultimate goal of this tutorial session is to establish two
    distinct pixel groups that represent the two materials featured in
    the micrograph.

    For any given pixel, you could decide individually whether it
    belongs to BOLD(black) or BOLD(white).  This process would be
    tedious.  OOF2 contains image manipulation tools to make it
    easier.

    """
    ),
    
    TutoringItem(
    subject="The Image Page",
    comments=

    """
    Open the BOLD(Image) page in the main OOF2 window.

    The two pull-down menus at the top of the page, labelled
    BOLD(Microstructure) and BOLD(Image) comprise the BOLD(Image
    Selector).  They let you choose which BOLD(Image) object the page
    operates on. (Most OOF2 main window pages have some sort of
    Selector at the top.) Since we currently have only one
    Microstructure and it contains only one Image, neither menu in the
    Selector has any other choices in it.

    The left hand pane on the BOLD(Image) page just displays
    information about the chosen Image.

    The right hand BOLD(Image Modification) pane contains a pull-down
    menu labelled BOLD(Method) which lets you select an image
    modification method.
    """
    ),
      
    TutoringItem(
    subject="Normalizing the image",
    comments=

    """Select BOLD(Normalize) from the BOLD(Method) pull-down menu.

    Click BOLD(OK).

    The gray values in the image now span the full range from black to white.
    """,

    signal= "modified image"
    ),

    TutoringItem(
    subject="Increasing Contrast",
    comments=

    """Select BOLD(Contrast) and apply it BOLD(three) times.

    The darker region gets darker and the brighter region gets
    brighter, which make materials more distinguishable than
    before.

    The two materials are now clearly distinguishable except a
    questionable spot in the lower-middle part of the image, where a
    supposedly-white material looks dark.

    We'll deal with it later.
    """,
    signal= "modified image"
    ),

    TutoringItem(
    subject="The Pixel Selection Toolbox",
    comments=

    """The image is ready for categorization.

    Unfortunately, one-click do-it-all feature (the BOLD(Group) button
    in the Image page) is not going to work for this micrograph,
    because it contains too many shades of gray. Thus, we will
    categorize the pixels manually using a few BOLD(pixel selection)
    algorithms.

    Go to the graphics window and open the BOLD(Pixel Selection)
    toolbox, using the BOLD(Toolbox) menu at the top of the left hand
    pane. """
        ),

    TutoringItem(
    subject="Point Selector",
    comments=

    """There are a few methods to select desired pixels in the
    toolbox.

    Select BOLD(Point) in the BOLD(Method) pull-down menu.

    Click on a pixel in the Image to select it.  The selected pixel
    will be marked in BOLD(red).
    """,
    signal= "new pixel selection"
    ),

    TutoringItem(
    subject="Selection Modifiers -- shift",
    comments=

    """You can accumulate the selected pixels by holding the
    BOLD(shift) key while clicking the mouse on the image.

    Try selecting multiple pixels by using this feature.
    """,
    signal= "new pixel selection"
    ),

    TutoringItem(
    subject="Undo, Redo, Clear and Invert",
    comments=

    """If you've made a mistake, you can undo the latest few
    selections by clicking on the BOLD(Undo) button in the toolbox.

    If you changed your mind while undoing, you can restore the
    selection status by clicking the BOLD(Redo) button.

    Also available are BOLD(Clear) and BOLD(Invert) buttons, which do
    just what they say.

    """
        ),

    TutoringItem(
    subject="Zooming",
    comments=

    """If you're having a hard time selecting pixels due to their
    small size on the screen, you can zoom in either with the
    BOLD(Zoom/In) command in the BOLD(Settings) menu, or by typing
    BOLD(ctrl-.)

    You can zoom out with BOLD(ctrl-,) or BOLD(Settings/Zoom/Out).

    Finally, you can resize the image to fit the window with
    BOLD(ctrl-=) or BOLD(Settings/Zoom/Fill Window).

    (If you want to keep a particular pixel fixed on the screen while
    you zoom, use the BOLD(Viewer) toolbox instead.)

    """
        ),

    TutoringItem(
    subject="Geometrical Selectors",
    comments=

    """At this point, if you had a lot of patience, you could select
    all the pixels from either the BOLD(black) or BOLD(white) material
    in a pixel-by-pixel fashion and create a pixel group out of them.

    OOF2 provides the geometrical selectors BOLD(Rectangle),
    BOLD(Circle), and BOLD(Ellipse) for selecting regions of pixels.

    Choose one of these in the BOLD(Method) pull-down menu in the
    BOLD(Pixel Selection) toolbox and select pixels by clicking and
    dragging on the Image.
    """,
    signal= "new pixel selection"
    ),
      
    TutoringItem(
    subject="The Brush Selector",
    comments=

    """The BOLD(Brush) selector allows you to select irregular shapes.
    It works just like a brush tool in most drawing applications.

    Select the BOLD(Brush) pixel selector.

    Two brush BOLD(style)s are available: BOLD(Circle) and
    BOLD(Square).  The size of the brush can be specified.  The units
    are the same as the units used to specify the BOLD(physical) size
    of the microstructure.

    Try using the brush selector.
    """,
    signal= "new pixel selection"
    ),

    TutoringItem(
    subject="Better Selectors",
    comments=

    """Although the geometrical and brush selectors make it possible
    to select pixels for each material more efficiently than
    BOLD(Point) selector, BOLD(Burn) and BOLD(Color) selection methods
    are more suited for the task.

    Basically, they can select pixels of similar color ranges automatically.

    BOLD(Burn) only selects contiguous pixels, whereas BOLD(Color)
    works on the entire microstructure.

    BOLD(Clear) the current pixel selection, if any, and move on to
    the next slide for some real action.
    """
    ),

    TutoringItem(
    subject="The Color Selector",
    comments=

    """Select BOLD(Color) for the selection method.

    The BOLD(Color) selector selects all pixels whose color is within
    a specified range of the color of a pixel that you choose with the
    mouse.  Colors in OOF2 are specified in one of three formats:

    BOLD(Gray): a single floating point value between 0 and 1.

    BOLD(RGB): three floating point values between 0 and 1,
    representing red, green, and blue intensities, respectively.

    BOLD(HSV): three floating point values representing hue,
    saturation and value, respectively.  Hue is between 0 and 360.
    Saturation and value are between 0 and 1.

    Since we have a gray-scale image, set the BOLD(range) of the selector
    to BOLD(DeltaGray) with the parameter BOLD(delta_gray) set to 0.4.  

    Now, we need to provide a reference color by clicking on a pixel.
    Click on any BOLD(black) pixel.
    """,
    signal= "new pixel selection"
    ),

    TutoringItem(
    subject="Erroneous Spot",
    comments=

    """The result seems satisfactory except for a region where two black
    islands are mistakenly connected in the BOLD(lower-middle) of the
    image.

    If you're unsure of the location of the erroneous region, repeat
    BOLD(Clear)-BOLD(Undo) to make it more apparent.

    If you located the spot, click BOLD(Invert) to invert the selection.
    """,
    signal= "new pixel selection"
    ),

    TutoringItem(
    subject="The Brush Selector in Action",
    comments=

    """A gray region should be visible in the lower-middle part of the
    image.

    These gray pixels belong to the BOLD(white) material.

    We'll select these pixels and add to the current selection for the
    BOLD(white) material.

    Select BOLD(Brush) with the BOLD(Circle) profile and set its
    radius to BOLD(3.0).

    Hold BOLD(shift) and try to bridge the gap by selecting gray pixels.
    
    If you don't like the result, you can BOLD(Undo) and repeat the
    process until you're satisfied.
    """,
    signal= "new pixel selection"
    ),

    TutoringItem(
    subject="Creating a Pixel Group",
    comments=

    """Now that we have selected all the pixels belonging to the white
    material, it is a good idea to let the microstructure know about
    it.

    Open the BOLD(Microstructure) page, create a new pixel group by
    clicking BOLD(New...) in the BOLD(Pixel Groups) pane.

    Check the little box next to the parameter BOLD(name) and type in
    BOLD(white) for its name. (If you want to use a generic name, just
    skip this part.)

    Click BOLD(OK) to create a new pixel group.

    The BOLD(Pixel Groups) pane should show the pixel group you just created.
    """,
    signal= "new pixel group"
    ),
    
    TutoringItem(
    subject="Storing Pixels in a Pixel Group",
    comments=

    """ The pixel group you just created doesn't yet contain any
    pixels.  Click BOLD(Add) in the BOLD(Pixel Groups) pane to add the
    currently selected pixels to the group.

    The information for the group will be updated immediately.

    About 2600 pixels should be present in the group, if you did it correctly.
    """,
    signal= "changed pixel group"
    ),

    TutoringItem(
    subject="Playing with Fire",
    comments=

    """As mentioned, BOLD(Burn) works in a similar way to the BOLD(Color)
    selector but with a major difference -- it only selects
    contiguous pixels.

    BOLD(Clear) the selection (it's okay, it's saved) and select
    BOLD(Burn) in the BOLD(Pixel Selection) toolbox.
    
    Try clicking on any black pixel.

    You'll immediately notice that each selection forms an island and
    does not extend into the white material.

    Thus, if you need to store islands of black pixels to different
    pixel groups, BOLD(Burn) is the way to go.

    Hold the shift key as you click on a black region to select
    multiple islands.
    """,
    signal= "new pixel selection"
    ),

    TutoringItem(
    subject="Copying an Image",
    comments=

    """OOF2 Microstructures can contain multiple versions of an Image,
    or, indeed, multiple unrelated Images, as long as they are all the
    same size.  This can be useful when different microstructural
    features are easier to observe in different images.

    In the BOLD(Image) page, click BOLD(Copy), and click BOLD(OK) in
    the dialog box.

    The BOLD(Image Selector) now shows that the current BOLD(Image) is
    "K1_small.pgm<2>" in the BOLD(Microstructure) named "K1_small.pgm"
    (unless you gave it a different name when loading the image).  The
    "<2>" is part of the automatically generated name for the copied
    Image."""

    ),


    TutoringItem(
    subject="Displaying the Copied Image",
    comments=

    """In the BOLD(Layer List) at the bottom of the BOLD(Graphics)
    window, double click on the BOLD(Image) layer, or click once to
    select it and choose BOLD(Edit) from the BOLD(Layer) menu in the
    menu bar.

    In the BOLD(Displayed Object) pane in the BOLD(Layer Editor)
    window, notice that there are two pull-down menus next to the
    BOLD(object) label.  The first menu lists Microstructures and the
    second menu lists the Images that are stored in the chosen
    Microstructure.  (If you didn't choose a name for the
    Microstructure back in step 2, both menus say "K1_small.pgm".)
    Switch the second menu to "K1_small.pgm<2>".

    The Layer Editor works by composing graphics layers and sending
    them to a Graphics window.  If an old layer is selected in the
    recipient window, the old layer is replaced with the new layer
    from the editor.  In the BOLD(Graphics) window, deselect the Image
    layer in the Layer List by clicking with BOLD(ctrl) on it once.

    Click BOLD(Send) in the BOLD(Layer Editor) window.  Note that
    there are now two Image layers in the Layer List (you may have to
    scroll or enlarge it to see both) and that the copied Image
    (K1_small.pgm<2>) is drawn and listed on top."""

    ),

    TutoringItem(
    subject="Revert to the Original Image",
    comments=

    """ Copying an Image isn't very useful if you don't do anything
    different with the copy.  Since we copied the modified Image, we
    can BOLD(undo) the modifications on the original Image.

    Switch the BOLD(Image Selector) in the BOLD(Image) page in the
    main window to the original Image, "K1_small.pgm", and click
    BOLD(Undo) four times.  """
    
    ),

    TutoringItem(
    subject="Switching Layers",
    comments=
    
    """In the BOLD(Layer List) in the BOLD(Graphics) window, drag
    the top Image layer (which should be
    "K1_small.pgm<2>") and drop it below the bottom layer ("K1_small.pgm").
    This will lower the modified Image layer,
    letting you see the original Image again.

    Notice that the layers change their order both in the display and
    in the layer list. """
    ),
    
    TutoringItem(
    subject="Making Selections with Multiple Images",
    comments=

    """The set of currently selected pixels is a property of a
    BOLD(Microstructure), not of an BOLD(Image).  It's possible to
    select pixels in one Image, switch Images, and then modify the
    selection.

    In the graphics window, switch the BOLD(Pixel Selection Method)
    to BOLD(Color) and set BOLD(range) to BOLD(DeltaGray) with
    BOLD(delta_gray)=0.05.

    Click the mouse in the middle of one of the dark regions in the
    Image.  Note how many pixels have been selected, in the box at the
    bottom of the BOLD(Pixel Selection) toolbox.

    Using the BOLD(Layer List), switch to the other version of the
    Image (using drag-and-drop).
    Notice that the selection hasn't changed, since you
    haven't changed Microstructures.

    Click on the BOLD(Repeat) button in the toolbox.  This repeats the
    previous mouse click, but this time the selection method will act
    on the other Image.  Notice that a different set of pixels have
    been selected."""
    ),
    

    TutoringItem(
    subject="The Pixel Selection Page",
    comments=

    """Open the BOLD(Pixel Selection) page in the main OOF2 window.
    This page allows you to create and manipulate pixel selections in
    ways that don't require mouse clicks on the graphics window.

    The page has two panes: an information pane on the left and a
    BOLD(Pixel Selection Modification) pane on the right.
    
    Select BOLD(Select Group) in the BOLD(Method) pull-down menu in
    the Pixel Selection Modification pane.

    Select BOLD(white) for the pixel BOLD(group) and click BOLD(OK).
    """,
    signal= "new pixel selection"
    ),

    TutoringItem(
    subject="Inverting the Pixel Selection",
    comments=

    """Now that you have selected BOLD(white), to select black pixels
    you only need to invert the current selection.

    Click BOLD(Invert) in the BOLD(Pixel Selection) toolbox in the
    graphics window, or, equivalently, select BOLD(Invert) in the
    BOLD(Method) menu in the BOLD(Pixel Selection) page and click
    BOLD(OK).
    """,
    signal= "new pixel selection"
    ),

    TutoringItem(
    subject="Creating Another Pixel Group",
    comments=
    
    """Open the BOLD(Microstructure) page and create a new pixel group
    named BOLD(black).


    """,

    signal= "new pixel group"
    ),

    TutoringItem(
    subject="Storing Pixels in a Pixel Group -- again",
    comments=

    """ Add the currently selected pixels to the group by clicking the
    BOLD(Add) button.

    The Microstructure now has enough information to go on to the next
    step -- creating a Skeleton.  Although we haven't assigned
    Materials to the pixels, the pixels have been differentiated by
    virtue of being assigned to different pixel groups.  This is
    sufficient for establishing the Skeleton geometry.""",

    signal= "changed pixel group"
    ),

    TutoringItem(
    subject="Saving a Microstructure",
    comments=

    """
    In the main OOF2 window, select BOLD(Save/Microstructure) from the
    BOLD(File) menu.

    (Now click BOLD(Cancel) so that you can finish reading this
    tutorial entry.  Go back to the BOLD(Save/Microstructure) dialog
    when you're ready.)

    The file selector has a pull-down menu labelled
    BOLD(microstructure) which lets you choose which Microstructure to
    save.

    The BOLD(format) menu has three choices:

    BOLD(script): This saves the Microstructure as a Python script.
    It's a text file, so it can be edited in any text editor.  Because
    it's a Python script, it can contain any valid Python commands, so
    you could augment it in interesting and creative ways.  A data
    file saved as a script can be loaded by the BOLD(Load/Script)
    command in the BOLD(File) menu, or by the BOLD(--script) command
    line option at startup time.  If you're paranoid, you don't want
    to load scripts from untrustworthy sources, since they could
    conceivably contain malicious code.

    BOLD(ascii): This saves the Microstructure as a text file that is
    BOLD(not) a valid Python script.  It can be reloaded with the
    BOLD(Load/Data) command in the BOLD(File) menu, or by the
    BOLD(--data) command line option.  Because this file format cannot
    contain arbitrary Python commands, it is more trustworthy than the
    BOLD(script) format (for the paranoid).

    BOLD(binary): This saves the Microstructure as a binary file.
    Binary files are usually smaller and load faster than text files.
    Furthermore, they are not subject to round-off errors from
    converting numbers to text, and cannot contain arbitrary Python
    code.  Their one disadvantage is that they are not easily
    editable.  Binary data files can be loaded into OOF2 with the
    BOLD(Load/Data) command in the BOLD(File) menu.

    Select BOLD(Save/Microstructure) from the BOLD(File) menu again.
    Enter a file name, select a data format and click BOLD(OK).

    """
    ),

    TutoringItem(
    subject="Homework",
    comments=

    """So far, most of the significant issues involving
    BOLD(Microstructure)/BOLD(Pixel Selections) have been addressed.
    Topics not covered in the tutorials are covered in the manual,
    and, of course, in the tooltips.  Some relevant topics are:

    BOLD(Active Areas): This is a way of restricting OOF2 operations
    to a given set of pixels in the Microstructure.

    BOLD(Image Modification Tools): Other techniques for modifying
    Images before selecting pixels.

    BOLD(Pixel Selection Modification Tools): Techniques for modifying
    the set of currently selected pixels, in the BOLD(Pixel Selection)
    page of the main OOF2 window.
    """
    )
    ])
