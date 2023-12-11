# -*- python -*-

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
              tip="Details of the Microstructure object.",
              discussion="""<para>
              This tutorial covers most the basic operations related
              to &micros; in &oof2; by creating and manipulating a
              &micro; based on a typical micrograph.
              </para>""",
              lessons = [
    TutoringItem(
    subject="Introduction",
    comments=

"""This tutorial covers most of the basic operations related to Microstructures in OOF2 by letting users create and manipulate a Microstructure based on a typical micrograph.

A digitized image on a computer is nothing but a two dimensional array of colored pixels.  These pixels become meaningful in OOF2 only after materials have been assigned to them or they have been assembled into pixel groups.

An OOF2 Microstructure is the data structure that stores this information. """
    ),
    

    TutoringItem(
    subject="Creating a Microstructure",
    comments=

"""Locate the file <b>K1_small.pgm</b> within the share/oof2/examples directory in your OOF2 installation.

Open the <b>Microstructure</b> page in the main OOF2 window.  Click on <b>New from Image File</b>.

In the file selection dialog box, navigate to <b>K1_small.pgm</b>.

Look for a parameter named <b>microstructure_name</b> in the middle of the window.

If you want to set the name of the microstructure yourself, type in a name in place of <i>&lt;automatic&gt;</i>.  To use an automatically generated name (which will be the same as the image name), leave the box alone.  To return to automatic mode after typing something, delete the contents of the box.

The parameters <b>width</b> and <b>height</b> are the physical size of the microstructure.  Leave these set to <i>&lt;automatic&gt;</i>.  The size will be determined by assuming that each pixel is 1 unit square.

Click <b>OK</b> to create the Microstructure.""",
    ),

    TutoringItem(
        subject="Display the Image",
        comments=

"""Open a graphics window.  

Because we didn't set <b>Settings/New Layer Policy</b> before loading the Image, nothing is shown in the window.

Create a new Image layer with the <b>New</b> menu item in the <b>Layer</b> menu.  In the dialog box, set <b>category</b> to <b>Image</b>.  Leave <b>what</b> set to <b>K1_small.pgm/K1_small.pgm</b> (the Image called "K1_small.pgm" in the Microstructure also called "K1_small.pgm").  Leave <b>how</b> set to <b>Bitmap</b>.

Click <b>OK</b>. """
    ),

    TutoringItem(
    subject="A Glance at the Microstructure",
    comments=

"""As shown in the graphics window, the micrograph <b>K1_small.ppm</b> features two distinct materials, one in <b>black</b> and the other in <b>white</b>.

The boundaries between two materials are rather blurry and the black and white regions are really continuous shades of gray.

To make a useful Skeleton and Mesh from this image, we need to add information to the Microstructure so that it knows which pixels belong to which material.  We will do this by creating two pixel groups, one for each material.

For any given pixel, you could decide individually whether it belongs to <b>black</b> or <b>white</b>.  This process would be tedious.  OOF2 contains image manipulation tools to make it easier. """
    ),
    
    TutoringItem(
    subject="The Image Page",
    comments=

"""Open the <b>Image</b> page in the main OOF2 window.

The two pull-down menus at the top of the page, labelled <b>Microstructure</b> and <b>Image</b> form the <b>Image Selector</b>.  They let you choose which <b>Image</b> object the page operates on. (Most OOF2 main window pages have some sort of Selector at the top.) Since we currently have only one Microstructure and it contains only one Image, neither menu in the Selector has any other choices in it.

The left hand pane on the <b>Image</b> page just displays information about the chosen Image.

The right hand <b>Image Modification</b> pane contains a pull-down menu labelled <b>Method</b> which lets you select an image modification method. """
    ),
      
    TutoringItem(
    subject="Normalizing the image",
    comments=

"""Select <b>Normalize</b> from the <b>Method</b> pull-down menu.

Click <b>OK</b>.

The gray values in the image now span the full range from black to white. """,
    ),

    TutoringItem(
    subject="Increasing Contrast",
    comments=

"""In the <b>Method</b> menu, select <b>Contrast</b> and apply it <b>three</b> times.

The darker regions get darker and the brighter regions get brighter, making the two materials more distinguishable than before.

There is, however, questionable spot in the lower-middle part of the image, where a region that ought to be white material is dark.

We'll deal with it later.
    """,
    ),

    TutoringItem(
    subject="The Pixel Selection Toolbox",
    comments=
        
"""The image is ready for categorization.

Unfortunately, the one-click do-it-all feature (the <b>Group</b> button in the Image page) is not going to work for this micrograph, because it contains too many shades of gray. Thus, we will categorize the pixels manually using a few <b>pixel selection</b> algorithms.

Go to the graphics window and open the <b>Pixel Selection</b> toolbox, using the <b>Toolbox</b> menu at the top of the left hand pane. """
        ),

    TutoringItem(
    subject="Point Selector",
    comments=

"""There are a few methods to select desired pixels in the toolbox.

Select <b>Point</b> in the <b>Method</b> pull-down menu.

Click on a pixel in the Image to select it.  The selected pixel will be marked in <b>red</b>. """,
    ),

    TutoringItem(
    subject="Selection Modifiers",
    comments=

"""You can accumulate the selected pixels by holding the <b>shift</b> key while clicking the mouse on the image.

Try selecting multiple pixels by using this feature.

If you use the control key instead of the shift key, the pixel selection will be toggled: clicked pixels that were already selected will be deselected, and pixels that were not already selected will become selected.  This applies to all of the selection methods in the Pixel Selection toolbox. 

Holding down both control and shift while clicking the mouse, selects only those pixels that are already selected.  It's not very useful when selecting a single pixel, but is convenient when using tools that select multiple pixels. """,
    ),

    TutoringItem(
    subject="Undo, Redo, Clear and Invert",
    comments=
"""If you've made a mistake, you can undo the latest few selections by clicking on the <b>Undo</b> button in the toolbox.

If you changed your mind while undoing, you can restore the selection status by clicking the <b>Redo</b> button.

Also available are <b>Clear</b> and <b>Invert</b> buttons, which do just what they say. """
        ),

    TutoringItem(
    subject="Zooming",
    comments=
"""If you're having a hard time selecting pixels due to their small size on the screen, you can zoom in either with the <b>Zoom/In</b> command in the <b>Settings</b> menu, or by typing <b>ctrl-.</b> (ctrl-period).

You can zoom out with <b>ctrl-,</b> (ctrl-comma) or <b>Settings/Zoom/Out</b>.

Finally, you can resize the image to fit the window with <b>ctrl-=</b> or <b>Settings/Zoom/Fill Window</b>.

(If you want to keep a particular pixel fixed on the screen while you zoom, use the <b>Viewer</b> toolbox instead.) """
        ),

    TutoringItem(
    subject="Geometrical Selectors",
    comments=
"""Selecting individual pixels is tedious.  OOF2 provides the geometrical selectors <b>Rectangle</b>, <b>Circle</b>, and <b>Ellipse</b> for selecting regions of pixels.

Choose one of these in the <b>Method</b> pull-down menu in the <b>Pixel Selection</b> toolbox and select pixels by clicking and dragging on the Image.  Try it with the control and shift keys, separately and together. """,
    ),
      
    TutoringItem(
    subject="The Brush Selector",
    comments=
"""The <b>Brush</b> selector allows you to select irregular shapes. It works just like a brush tool in most drawing applications.

Select the <b>Brush</b> pixel selector.

Two brush <b>style</b>s are available: <b>Circle</b> and <b>Square</b>.  The size of the brush can be specified.  The units are the same as the units used to specify the <b>physical</b> size of the microstructure.  If you followed instructions when loading the image, a pixel is 1x1 in these units.

Choose the <b>Circle</b> selector, set <b>radius</b> to 5, and click and drag to select some pixels. """,
    ),

    TutoringItem(
    subject="Better Selectors",
    comments=
"""The point, geometrical, and brush selectors don't use any information from the image, and aren't sensitive to the geometry of the microstructure.  The <b>Burn</b> and <b>Color</b> selection methods can select pixels that are part of features in an image.

Basically, they can select pixels of similar color ranges automatically.

<b>Burn</b> only selects contiguous pixels, whereas <b>Color</b> works on the entire microstructure.

<b>Clear</b> the current pixel selection, if any, and move on to the next slide for for information. """
    ),

    TutoringItem(
    subject="The Color Selector",
    comments=
"""Select <b>Color</b> for the selection method.

The <b>Color</b> selector selects all pixels whose color is within a specified range of the color of a pixel that you choose with the mouse.  Colors in OOF2 are specified in one of three formats:

<b>Gray</b>: a single floating point value between 0 and 1.

<b>RGB</b>: three floating point values between 0 and 1, representing red, green, and blue intensities, respectively.

<b>HSV</b>: three floating point values representing hue, saturation and value, respectively.  Hue is between 0 and 360. Saturation and value are between 0 and 1.

Since we have a gray-scale image, set the <b>range</b> of the selector to <b>DeltaGray</b> with the parameter <b>delta_gray</b> set to 0.4.  

Now, we need to provide a reference color by clicking on a pixel. Click on any <b>black</b> pixel. """,
    ),

    TutoringItem(
    subject="Erroneous Spot",
    comments=
"""The result seems satisfactory except for a region where two black islands are incorrectly connected in the <b>lower-middle</b> of the image.

If you're unsure of the location of the erroneous region, <b>Clear</b> to deselect the whole image, and then the <b>Undo</b> (that is, undo the Clear) switch the view back and forth between the image and the selection.

Once you have located the spot, click <b>Invert</b> to invert the selection. """,
    ),

    TutoringItem(
    subject="The Brush Selector in Action",
    comments=
"""The white pixels are now all selected, but there is an unselected gray region in the lower-middle part of the image that belongs with the white pixels.

We'll select these pixels and add to the current selection for the <b>white</b> material.

Select <b>Brush</b> with the <b>Circle</b> profile and set its radius to <b>3.0</b>.

Hold <b>shift</b> and try to bridge the gap by selecting gray pixels.
    
If you don't like the result, you can <b>Undo</b> and repeat the process until you're satisfied. """,
    ),

    TutoringItem(
    subject="Creating a Pixel Group",
    comments=
"""Now that we have selected all the pixels belonging to the white material, it is a good idea to let the microstructure know about it.

Open the <b>Microstructure</b> page.  The right hand pane will list the pixel groups, but is currently empty.  The buttons to the left of the pane manipulate the groups as a whole, while the buttons to the right of the pane operate on the contents of the selected group.

Create a new pixel group by clicking <b>New...</b> in the <b>Pixel Groups</b> pane.

Type in <b>white</b> for its name (or leave the name set to <i>&lt;automatic&gt;</i>) if you prefer).

Click <b>OK</b> to create a new pixel group.

The <b>Pixel Groups</b> pane should show the pixel group you just created. """,
    ),
    
    TutoringItem(
    subject="Storing Pixels in a Pixel Group",
    comments=
"""The pixel group you just created doesn't yet contain any pixels. Click <b>Add</b> in the <b>Pixel Groups</b> pane (in the buttons on the right) to add the currently selected pixels to the group.

The information for the group will be updated immediately.

About 2600 pixels should be present in the group, if you did it correctly.  The exact number will depend on exactly where you clicked on the image.  """,
    ),

    TutoringItem(
    subject="Playing with Fire",
    comments=
"""As mentioned, <b>Burn</b> works in a similar way to the <b>Color</b> selector but with a major difference -- it only selects contiguous pixels.

<b>Clear</b> the selection (it's okay, it's saved in a group) and select <b>Burn</b> in the <b>Pixel Selection</b> toolbox.
    
Try clicking on any black pixel.

You'll immediately notice that each selection forms an island and does not extend into the white material.

Thus, if you need to store islands of black pixels to different pixel groups, <b>Burn</b> is the way to go.

Hold the shift key as you click on a black region to select multiple islands. """,
    ),

    TutoringItem(
    subject="Copying an Image",
    comments=
"""OOF2 Microstructures can contain multiple versions of an Image, or, indeed, multiple unrelated Images, as long as they are all the same size.  This can be useful when different microstructural features are easier to observe in different images.

First, clear the pixel selection so that you can see the whole image.

In the <b>Image</b> page, click <b>Copy</b>, and click <b>OK</b> in the dialog box.

The <b>Image Selector</b> now shows that the current <b>Image</b> is "K1_small.pgm&lt;2&gt;" in the <b>Microstructure</b> named "K1_small.pgm" (unless you gave it a different name when loading the image).  The "&lt;2&gt;" is part of the automatically generated name for the copied Image."""
    ),


    TutoringItem(
    subject="Displaying the Copied Image",
    comments=
"""In this step, we'll display a the second image in the graphics window.

In the graphics window's <b>Layer</b> menu, select <b>New</b>.

In the dialog box, set <b>category</b> to <b>Image</b>.

The first pull-down menu in the box marked <b>what</b> sets the <b>Microstructure</b> containing the <b>Image</b> that is to be displayed.  Leave it set to its current value.  The second pull-down menu sets the <b>Image</b> from the images available in the Microstructure.  Set it to <b>(K1_small.pgm&lt;2&gt;</b> (or whatever name you gave to the copied image).

Leave the <b>how</b> menu set to <b>Bitmap</b> and click <b>OK</b>.

Note that there are now two Image layers in the Layer List (you may have to scroll or enlarge it to see both) and that the copied Image (K1_small.pgm&gt;2&lt;) is drawn and listed on top."""
    ),

    TutoringItem(
    subject="Revert to the Original Image",
    comments=
"""Copying an Image isn't very useful if you don't do anything different with the copy.  Since we copied the modified Image, we can <b>undo</b> the modifications on the original Image.

Switch the <b>Image Selector</b> in the <b>Image</b> page in the main window to the original Image, "K1_small.pgm", and click <b>Undo</b> four times (corresponding to the one Normalize and three Contrast operations that you did earlier).  """
    ),

    TutoringItem(
    subject="Switching Layers",
    comments=
"""In the <b>Layer List</b> in the <b>Graphics</b> window, make sure that the top Image layer is selected, and choose <b>Lower/One Level</b> from the <b>Layer</b> menu in the menu bar.  You can also right-click on the line in the Layer list to bring up the menu. This will lower the modified (copied) Image layer, letting you see the original Image again.

Notice that the layers change their order both in the display and in the layer list. """
    ),
    
    TutoringItem(
    subject="Making Selections with Multiple Images",
    comments=
"""The set of currently selected pixels is a property of a Microstructure, not of an Image.  It's possible to select pixels in one Image, switch Images, and then modify the selection.

In the graphics window, switch the <b>Pixel Selection Method</b> to <b>Color</b> and set <b>range</b> to <b>DeltaGray</b> with <b>delta_gray</b>=0.05.

Click the mouse in the middle of one of the dark regions in the Image.  Note how many pixels have been selected, in the box at the bottom of the <b>Pixel Selection</b> toolbox.

Using the Layer list and the <b>Raise</b> or <b>Lower</b> commands in the <b>Layer</b> menu, switch to the other version of the Image. Notice that the selection hasn't changed, since you haven't changed Microstructures.

Click on the <b>Repeat</b> button in the toolbox.  This repeats the previous mouse click, but this time the selection method will act on the other Image.  Notice that a different set of pixels have been selected."""
    ),
    

    TutoringItem(
    subject="The Pixel Selection Page",
    comments=
"""Open the <b>Pixel Selection</b> page in the main OOF2 window. This page allows you to create and manipulate pixel selections in ways that don't require mouse clicks on the graphics window.

The page has two panes: an information pane on the left and a <b>Pixel Selection Modification</b> pane on the right.
    
Select <b>Select Group</b> in the <b>Method</b> pull-down menu in the Pixel Selection Modification pane.

Select <b>white</b> for the pixel <b>group</b> and click <b>OK</b>. """,
    ),

    TutoringItem(
    subject="Inverting the Pixel Selection",
    comments=
"""Now that you have selected <b>white</b>, to select black pixels you only need to invert the current selection.

Click <b>Invert</b> in the <b>Pixel Selection</b> toolbox in the graphics window, or, equivalently, select <b>Invert</b> in the <b>Method</b> menu in the <b>Pixel Selection</b> page and click <b>OK</b>. """,
    ),

    TutoringItem(
    subject="Creating Another Pixel Group",
    comments=
"""Open the <b>Microstructure</b> page and create a new pixel group named <b>black</b>. """,
    ),

    TutoringItem(
    subject="Storing Pixels in a Pixel Group -- again",
    comments=
"""Add the currently selected pixels to the group by clicking the <b>Add</b> button.

The Microstructure now has enough information to go on to the next step -- creating a Skeleton.  Although we haven't assigned Materials to the pixels, the pixels have been differentiated by virtue of being assigned to different pixel groups.  This is sufficient for establishing the Skeleton geometry.""",
    ),

    TutoringItem(
    subject="Saving a Microstructure",
    comments=
"""In the main OOF2 window, select <b>Save/Microstructure</b> from the <b>File</b> menu.

The file selector has a pull-down menu labelled <b>microstructure</b> which lets you choose which Microstructure to save.

The <b>format</b> menu has three choices:

<b>script</b>: This saves the Microstructure as a Python script. It's a text file, so it can be edited in any text editor.  Because it's a Python script, it can contain any valid Python commands, so you could augment it in interesting and creative ways.  A data file saved as a script can be loaded by the <b>Load/Script</b> command in the <b>File</b> menu, or by the <tt>--script</tt> command line option at startup time.  If you're paranoid, you don't want to load scripts from untrustworthy sources, since they could conceivably contain malicious code.

<b>ascii</b>: This saves the Microstructure as a text file that is <b>not</b> a valid Python script.  It can be reloaded with the <b>Load/Data</b> command in the <b>File</b> menu, or by the <tt>--data</tt> command line option.  Because this file format cannot contain arbitrary Python commands, it is more trustworthy than the <b>script</b> format (for the paranoid).

<b>binary</b>: This saves the Microstructure as a binary file. Binary files are usually smaller and load faster than text files. Furthermore, they are not subject to round-off errors from converting numbers to text, and cannot contain arbitrary Python code.  Their one disadvantage is that they are not easily editable.  Binary data files can be loaded into OOF2 with the <b>Load/Data</b> command in the <b>File</b> menu.

Enter a file name, select a data format and click <b>OK</b>. """
    ),

    TutoringItem(
    subject="Homework",
    comments=
"""We have addressed most of the significant issues involving <b>Microstructures</b> and <b>Pixel Selections</b>.  Topics not covered in the tutorials are covered in the manual, and, of course, in the tooltips.  Some relevant topics are:

<b>Active Areas</b>: This is a way of restricting OOF2 operations to a given set of pixels in the Microstructure.

<b>Image Modification Tools</b>: Other techniques for modifying Images before selecting pixels.

<b>Pixel Selection Modification Tools</b>: Techniques for modifying the set of currently selected pixels, in the <b>Pixel Selection</b> page of the main OOF2 window.
    
This is the end of this tutorial. """
    )
    ])
