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

TutorialClass(subject="Basics",
              ordering=0,
              tip="The basics of operating OOF2.",
              discussion="""<para>
              This tutorial teaches some of the terminology used in &oof2;,
              and the mechanics of using the program.
              </para>""",
              lessons=[
    TutoringItem(
    subject="Introduction",
    comments=
"""This tutorial is a concise guide to the essential OOF2 components.

It's a good idea to read through this tutorial before you venture into more task-specific ones, just to make yourself familiar with various OOF2 parts.

To go to the next tutorial page, click on the <b>Next</b> button below.  

The <b>Back</b> button below will take you to the previous tutorial page.  The <b>Jump</b> button takes you to the highest numbered page that you've visited in this tutorial session.

Use the <b>Save</b> button to save a tutorial session in a file so that you can resume it later.  To resume a session, load the saved file with the <b>Load Script</b> command in the <b>File</b> menu in the main OOF2 window."""
    ),

    TutoringItem(
    subject="OOF2 Terminology",
    comments=
"""OOF2 creates and manipulates a variety of data structures ("objects", in the lingo), which are described here briefly so that they can be referred to later in the tutorials.

<b>Microstructure</b>: A grid of pixels with Materials assigned to them. Microstructures have a fixed height and width in physical units. Microstructures also contain other data structures, defined below.

<b>Image</b>: Just what it sounds like -- a grid of pixels with colors assigned to them.  Every Image in OOF2 is assigned to a Microstructure. The Image and the Microstructure must have the same size.  A Microstructure can have many Images assigned to it.

<b>Material</b>: A collection of Properties which define the physical behavior of the material at a point in a Microstructure.

<b>Property</b>: Something that contributes somehow to the definition of a material.  Some Properties correspond directly to terms in a constitutive equation (eg, elasticity, thermal conductivity), and some contribute indirectly (eg, orientation). They can also be purely decorative (eg, color).

<b>Skeleton</b>: The geometry of a finite element mesh, specifying where the nodes, edges, and elements are, but without any further information.  Skeletons are created within Microstructures.  A single Microstructure can contain many Skeletons.

<b>Mesh</b>: A full finite element mesh, including information about element type, which fields are defined, which equations are being solved, boundary conditions, etc.

<b>Subproblem</b>: A part of a finite element mesh.  A mesh can contain many subproblems.  Subproblems can differ in the mesh elements included in them, in the fields defined on them, or the equations solved on them.  When a Mesh is created, a default Subproblem that includes all Mesh elements is created automatically."""
    ),

    TutoringItem(
    subject="A Note on Units",
    comments=
"""OOF2 has <b>no</b> preferred set of units.  Enter data in any set of units that you prefer, and the output will be in those units.  Of course, at NIST we prefer that you use SI units (kilograms, meters, and seconds, etc), but if you use slugs, furlongs, and fortnights instead, OOF2 will not complain."""
    ),

    TutoringItem(
    subject="Launching OOF2",
    comments=
"""If you're reading this, you've presumably figured out how to launch OOF2 by typing 'oof2' on the Unix command line.  This starts OOF2 in graphics mode.  To launch it without the graphical user interface, type

<tt>% oof2 --text</tt>

To list all the available options, type

<tt>% oof2 --help</tt>

(For convenience, you only need to type enough of an option to distinguish it from the other options.  <tt>oof2 --he</tt> is equivalent to <tt>oof2 --help</tt>.) """
    ),

    TutoringItem(
    subject="The Main OOF2 window",
    comments=
"""Upon launching, the main OOF2 window and a message window appear.

The main window contains most of the OOF2 controls. The message window displays the output from OOF2 commands, the command history, and error messages.

The main window features two major parts, the menu bar and the task page.

The menu bar contains four menus, <b>File</b>, <b>Settings</b>, <b>Windows</b>, <b>OrientationMap</b>, and <b>Help</b>.

The <b>File</b> menu deals with loading and saving files and quitting OOF2.

The <b>Settings</b> menu lets you select fonts, window themes, and buffer sizes.

From the <b>Windows</b> menu, one can open additional OOF2 windows and raise existing windows.

The <b>OrientationMap</b> menu contains commands for manipulating EBSD data files.

The <b>Help</b> menu contains tools to help you use OOF2 and to help us debug it."""
    ),

    TutoringItem(
    subject="Task Pages",
    comments=
"""Most of the real estate of the main OOF2 window is dedicated to a task page.

There are many task pages available in OOF2. When you first start OOF2, the <b>Introduction</b> page is displayed. To open a specific task page, select it from the pull-down menu labelled <b>Task</b>. The tasks are listed more-or-less in the order in which they must be performed when doing an OOF calculation.  The arrow buttons to the left and right of the <b>Task</b> menu switch to the previous and next tasks in the list.

A brief description of each page is displayed when the mouse cursor is over the page's entry in the task menu. (These are examples of <b>Tooltips</b>.  Most GUI elements in OOF2 have tooltips to help you figure out what they're for.

Open the <b>Microstructure</b> page by selecting <b>Microstructure</b> in the task menu.

Notice that some buttons in the page are grayed out, that is, they are not accessible.  In OOF2, only the buttons that are meaningful at the moment will be clickable. The <b>Delete</b> button, for instance, is useless at this point, since there's no Microstructure to delete."""
    ),

    TutoringItem(
    subject="Task Pages -- continued",
    comments=
"""Now, create a microstructure to see what happens to the grayed-out buttons on the page.

Locate the file <tt>small.ppm</tt> within the <tt>share/oof2/examples</tt>
directory in your OOF2 installation.

Click the <b>New from Image File</b> button.

The dialog box that appears has a column of labels on the left, and boxes corresponding to those labels on the right.  The labels are the names of parameters that need to be set, and the boxes contain the GUI widgets that let you set them.

The file selector widget is in the top box. To navigate, switch directories by typing in the <b>Directory</b> box at the top of the widget, or by using the pull-down menu to its right, which displays the directory hierarchy. Directories are also listed in bold in the list of files below the row of buttons.  Double-clicking on a directory name in the list will take you to that directory.

The <b>Back</b> and <b>Next</b> buttons take you other directories that you've recently visited, and the central <b>Home</b> button takes you to your home directory.

Navigate to the directory containing <tt>small.ppm</tt> and click its name in the list.

The three fields labelled <b>microstructure_name</b>, <b>height</b>, and <b>width</b> are <b>automatic</b> widgets, currently displaying "<i>&lt;automatic&gt;</i>".  If you don't type anything in the widgets, OOF2 will automatically create an appropriate value for them.  In this case, the microstructure name will be set to the name of the image, "small.ppm", and the height and width will be set to the size of the image, in pixels.  If you type anything in an automatic widget, the its value will be the value that you typed.  If you delete all of the text in an automatic widget, the value will revert to "<i>&lt;automatic&gt;</i>".

Leave the automatic widgets set to "<i>&lt;automatic&gt;</i>" and click the <b>OK</b> button.

You should see that all of the buttons in the upper part of the Microstructure page have been turned on, and that a Microstructure called "small.ppm" has been created.

Also, if you bring up the messages window (select Messages/Message 1 in the Windows menu, if necessary), you'll notice that it has logged the menu command for Microstructure creation. """

    ),

    TutoringItem(
    subject="The Graphics Window",
    comments=
"""Open a graphics window with the <b>Graphics/New</b> command in the <b>Windows</b> menu.  The graphics window displays Microstructures, Skeletons, and Meshes and their associated data.

The graphics window is composed of five parts: a menu bar, a toolbox area, a canvas, a contour map, and a layer list.  

The <b>menu bar</b> at the top part of the window contains all the necessary menus to operate the graphics window and it works just like the one in the main OOF2 window.

The <b>toolbox</b> area on the left side of the window is a home of the many toolboxes of OOF2.  Toolboxes are somewhat similar to the task pages in the main OOF2 window but they are designed to perform tasks that are (mostly) driven by mouse clicks in the canvas area.

Any objects that have graphical representations can be drawn on the <b>canvas</b> in the center of the window.  Everything drawn on the canvas is part of a <b>display layer</b>. These layers are enumerated in the <b>layer list</b> at the bottom of the window. (Thin horizontal lines in the layer list correspond to predefined default layers -- to see the full definition of these layers select <b>List All Layers</b> from the <b>Settings</b> menu.)

The <b>contour map</b> in the rightmost pane displays the colors and contour levels used in the contour plot layers (if any) displayed in the canvas.

The toolbox, canvas, contour map, and layer list are separated by dividers that can be dragged with the mouse to change the sizes of the various panes in the window.  Many user interface elements have a minimum size, so you may need to enlarge the entire window before moving some of the dividers."""
    ),

    TutoringItem(
    subject="Adding a Graphics Layer",
    comments=
    
"""The <b>canvas</b> is currently blank, even though a microstructure has been created from an image.

Everything displayed in a graphics window is part of a <b>Layer</b>.  Layers are listed at the bottom of the window. Layers can be shown, hidden, deleted, and reordered by using the <b>Layer</b> menu, or by right-clicking in the layer list.

To display a layer, select <b>New</b> from the <b>Layer</b> menu in the graphics window.

Each layer is defined by three parameters, <b>category</b>, <b>what</b>, and <b>how</b>.  <b>category</b> determines what kind of object is displayed in the layer.  Set <b>category</b> to <b>Image</b>.

<b>what</b> determines which object in the selected category will be displayed.  Images are identified by their name and the name of the Microstructure that contains them.  The upper pull-down menu in the <b>what</b> box selects the Microstructure, and the lower one selects the Image.  We have only one Microstructure (named "small.ppm") and it contains only one Image (also named "small.ppm"), so leave both menus set to "small.ppm"

<b>how</b> determines how the object will be rendered on the canvas.  Leave it set to <b>Bitmap</b> and click <b>OK</b>.

The image now appears on the canvas and its display layer is listed at the bottom of the window."""
    ),

    TutoringItem(
    subject="Activity Viewer and Progress Bars",
    comments=
"""If you're running OOF2 in threaded mode (which is the default) you'll be able to monitor the progress of certain activities and furthermore you'll be able to stop these activities at will.

The <b>Activity Viewer</b> window appears when OOF2 does something that takes longer than two seconds (the exact time can be adjusted in the window's <b>Settings</b> menu), or when opened explicitly with the main window's <b>Windows</b> menu.

Progress bars in the <b>Activity Viewer</b> window indicate how far a process has progressed.  Each bar has a <b>Stop</b> button that will abort the process.

Unfortunately, unless you're using a very slow computer it's impossible to demonstrate the progress bars at this point, because there's nothing that we can do that takes longer than two seconds. """
    ),

    TutoringItem(
    subject="Error Handling",
    comments=

"""Once in a while, you will encounter an error when working with OOF2.  Mostly this is your own damn fault, but sometimes (rarely, we hope) it's ours.

In these cases, OOF2 launches a window that explains what went wrong.  You must close this window before you can continue using any other features of OOF2.

From this <b>OOF2 Error</b> window, you can ignore the error by clicking <b>OK</b>, and OOF2 will try to continue.

If you're interested in tracking down the source of error, you can click the <b>View Traceback</b> button to see what really happened. This traceback can be saved to a file by clicking <b>Save Traceback</b>.
   
Finally, you can choose to abort the program by clicking on the <b>Abort</b> button.  OOF2 will give you a chance to save the session log file before aborting.

If you do encounter an error in the program, please let us know about it by following the advice in the <b>Reporting Bugs</b> section of the OOF2 web site.
"""
    ),

    TutoringItem(
    subject="Error Handling -- continued",
    comments=
"""Generate an error by loading a script that features an erroneous line.

Locate the file <tt>errorgen.log</tt> within the <tt>share/oof2/examples</tt> directory in your OOF2 installation.
    
Select the <b>Load/Script</b> command in the <b>File</b> menu in the main OOF2 window.

In the file selector, navigate to <tt>errorgen.log</tt> and click <b>OK</b>.

Upon loading the file, you should have an <b>OOF2 Error</b> window.

You can explore the options on the window freely, but <i>do not</i> click on the <b>Abort</b> button - you'll lose this tutorial session. """
    ),

    TutoringItem(
    subject="Quitting and Restarting OOF2",
    comments=
    
"""Almost every OOF2 window has a <b>Quit</b> command in its <b>File</b> menu.

If you've executed any commands without saving them, OOF2 will ask if you'd like to save a log file.  The saved script can be loaded later with the <b>Load/Script</b> command in the <b>File</b> menu, or with the <tt>--script</tt> command line option, like this:

    <tt>% oof2 --script=myoof.log</tt>

where <tt>myoof.log</tt> is the name you assigned to the log file. Loading the script will re-execute all the commands that you performed, and thus duplicate your OOF2 session.

To recover an OOF2 session without repeating all the commands, you need to save and reload the data (Microstructure, Skeleton, etc.) instead of the commands.  This can be done with the <b>Save</b> and <b>Load/Data</b>. menus in the <b>File</b> menu.

Thanks for trying out this tutorial!!!""",
    )
    
    ]
              )
