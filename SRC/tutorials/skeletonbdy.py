# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


from ooflib.SWIG.common import switchboard
from ooflib.tutorials import tutorial
TutoringItem = tutorial.TutoringItem
TutorialClass = tutorial.TutorialClass


   
def new_boundaries(*args):
    switchboard.notify("new boundaries for tutorial")
switchboard.requestCallback("new boundary created", new_boundaries)

TutorialClass(
    subject = "Skeleton Boundaries",
    ordering=3,
    lessons = [
    TutoringItem(
    subject="Introduction",
    comments=
"""This tutorial is a simple interactive walkthrough explaining how to construct boundaries in skeletons.

Skeleton boundaries are the places to which boundary conditions are applied.  Boundaries created in a skeleton are automatically propagated to previous and later <b>modifications</b> of the skeleton, and are also created in all of the finite-element <b>meshes</b> associated with each of these modifications."""  
    ),
      
    TutoringItem(
    subject="Default Boundaries",
    comments=
"""When an initial Skeleton is created, it automatically constructs <b>8</b> default boundaries, <b>4</b> at each corner and <b>4</b> at each bounding edge of the skeleton.  These boundaries will be properly preserved throughout the skeleton modification processes.

If you need to apply boundary conditions to places other than these, you need to create boundaries yourself, which you will learn how to do in this tutorial."""
    ),

    TutoringItem(
    subject="Point Boundaries and Edge Boundaries",
    comments=
"""OOF2 provides two kinds of boundaries, <b>point boundaries</b> and <b>edge boundaries</b>.  A point boundary is merely a collection of one or more nodes. An edge boundary is a collection of one or more segments with a specified direction."""
    ),

    TutoringItem(
    subject="Sample Skeleton",
    comments=
"""Let us load a sample skeleton.  Locate the file <b>two_circles.skeleton</b> within the share/oof2/examples directory in your OOF2 installation.

Choose <b>Load/Data</b> from the <b>File</b> menu in the main OOF2 window.  Open the file <b>two_circles.skeleton</b>.

Open a graphics window, if you haven't yet.  Create new layers for the Image and the Skeleton (displayed by Edges).  """,
    ),

    TutoringItem(
    subject="Three Boundaries to Create",
    comments=
"""We'll create three additional boundaries in this skeleton.

1. A clockwise edge boundary along the circumference of the <b>red</b> circle.

2. A point boundary along the circumference of the <b>yellow</b> circle.

3. An edge boundary directed left-to-right along the interface between <b>white</b> and <b>cyan</b> layers.

The typical process of creating boundaries involves two simple steps. Select source objects such as nodes (for point boundaries) and segments (for edge boundaries) and create a boundary (with a given direction, if needed).

You'll need to know how to select objects efficiently to minimize the effort involved."""
    ),

    TutoringItem(
    subject="Selecting Elements by Dominant Pixel",
    comments=
"""Let us create the first boundary.

Open the <b>Skeleton Selection</b> toolbox from the graphics window.  Make sure that the toolbox is in <b>Element</b> mode and select <b>ByDominantPixel</b> from the pull-down menu for the parameter <b>Method</b>.

Click on any <b>red</b> pixel to select all the elements inside the circle.

There should be 105 selected elements (shown at the bottom of the toolbox).
    
(The color change for the selected elements is subtle, because the red for selected elements is too similar to the red in the image. You can temporarily hide the image using the check box in the layer list to make the selection more apparent.  You can also edit the display method for selected elements and change their color, by first selecting <b>List All Layers</b> in the <b>Settings</b> menu.)

    """,
    ),

    TutoringItem(
    subject="Edge Boundary from Selected Elements",
    comments=
"""Open the <b>Skeleton Boundaries</b> page in the main OOF2 window.

Click <b>New...</b> in the <b>Boundaries</b> pane on the left side of the page to bring up a boundary builder.

Type in <b>red_circle</b> for the name of the boundary.

Select <b>Edge boundary from elements</b> and select <b>&lt;selection&gt;</b> for the parameter <b>group</b>.  Set <b>direction</b> to be <b>Clockwise</b>.

Click <b>OK</b> to create the boundary.""",
    ),

    TutoringItem(
    subject="Boundary Display",
    comments=
"""The newly created boundary should be listed and selected in the boundary list in the left side of the <b>Skeleton Boundaries</b> page.

Its details are listed in the right side of the page.

The new boundary is displayed in the graphics window with orange arrows. """
    ),

    TutoringItem(
    subject="Second Boundary",
    comments=
"""Next is the point boundary along the perimeter of the <b>yellow</b> circle.  This one can be constructed in a similar way as the first one.

Just for the sake of practice, let's try a less simple way."""
    ),

    TutoringItem(
    subject="Elements by Dominant Pixel",
    comments=
"""In the <b>Skeleton Selection</b> toolbox in the graphics window, select <b>ByDominantPixel</b> for the <b>Element</b> selection method.

Click on any <b>yellow</b> pixel in the circle.  You should see that <b>66</b> elements inside the yellow circle have been selected""",
    ),

    TutoringItem(
    subject="Selecting Nodes from Selected Elements",
    comments=
"""Open the <b>Skeleton Selection</b> task page in the main OOF2 window.

Select <b>Nodes</b> for the <b>Selection Mode</b>, and pick <b>Select from Selected Elements</b> for the parameter <b>Method</b>.  From two available options, turn only <b>boundary</b> on so that only the nodes along the boundary of the selected elements will be selected.

Click <b>OK</b> to make a selection.  The selected nodes will be displayed as <b>blue</b> dots in the graphics window.""",
    ),

    TutoringItem(
    subject="Point Boundary from Selected Nodes",
    comments=
"""Go back to the <b>Skeleton Boundaries</b> page and click <b>New...</b>.

In the boundary builder, give the name <b>yellow_circle</b> for the boundary.

Select <b>Point boundary from nodes</b> for boundary building method and select <b>&lt;selection&gt;</b> for the parameter <b>group</b>.

Click <b>OK</b> to create the boundary.""",
    ),

    TutoringItem(
    subject="Boundary Displayed",
    comments=
"""You should see the boundary information displayed in the page.  If you clear the node selection, you will see the boundary marked with orange dots in the graphics window.

If done correctly, the boundary should contain <b>31</b> points(nodes)."""
    ),

    TutoringItem(
    subject="Third Boundary",
    comments=
"""The third boundary is the edge between the white and the cyan material.

First, we need to select all the segments along the boundary.  In the <b>Skeleton Selection</b> toolbox in the graphics window, click <b>Segment</b> in the upper part of the toolbox to start selecting segments.

Select <b>Rectangle</b> for the selection method.  This will let you select all the segments that are completely inside a rectangular box drawn on the canvas.

Click and drag the mouse to carefully draw a rectangle that surrounds all the segments along the interface.

The selected segments should be displayed as thick <b>green</b> lines.  Properly done, <b>36</b> segments should be selected.

You can always <b>Clear</b> the selection and repeat the process. If needed, click and drag while holding the <b>shift</b> (addition) or <b>ctrl</b> (toggle) modifier keys.  It may help to <b>Zoom</b> the window, using either the <b>Viewer</b> toolbox or the <b>Settings/Zoom</b> menu.""",
    ),

    TutoringItem(
    subject="Edge Boundary from Selected Segments",
    comments=
"""Go back to the <b>Skeleton Boundaries</b> page, and click <b>New...</b>.  Give the boundary a name, <b>white_cyan</b>.  Select <b>Edge boundary from segments</b> with <b>&lt;selection&gt;</b> selected for the parameter <b>group</b>.

Set the direction to be <b>Left to right</b> and click <b>OK</b>.""",
    ),

    TutoringItem(
    subject="Viewing and Manipulating Boundaries",
    comments=
"""Boundaries, once created, can be modified, renamed, and even deleted in the <b>Skeleton Boundaries</b> page.

Clicking on a boundary name in the list in the <b>Boundaries</b> pane selects the boundary.  Its name is highlighted in the list and the boundary is displayed in the graphics window. Control-clicking on a selected boundary name deselects it.  The <b>Modify</b>, <b>Rename</b>, and <b>Delete</b> buttons act on the currently selected boundary."""
    ),

    TutoringItem(
    subject="Fin",
    comments=
"""So far, we've covered most of important features concerning skeleton boundaries.
    
Further details, if needed, may be found in the manual.
    
Thanks for trying out the tutorial."""
    )
    
    ])
