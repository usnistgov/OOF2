# -*- python -*-
# $RCSfile: skeletonbdy.py,v $
# $Revision: 1.16 $
# $Author: langer $
# $Date: 2014/09/27 21:41:43 $

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
    
    """This tutorial is a simple interactive walkthrough explaining
    how to construct boundaries in skeletons.

    Skeleton boundaries are the places to which boundary conditions
    are applied.  Boundaries created in a skeleton are automatically
    propagated to previous and later BOLD(modifications) of the skeleton,
    and are also created in all of the finite-element BOLD(meshes)
    associated with each of these modifications."""  
    ),
      
    TutoringItem(
    subject="Default Boundaries",

    comments="""When an initial Skeleton is created, it automatically
    constructs BOLD(8) default boundaries, BOLD(4) at each corner and
    BOLD(4) at each bounding edge of the skeleton.  These boundaries
    will be properly preserved throughout the skeleton modification
    processes.

    If you need to apply boundary conditions to places other than
    these, you need to create boundaries yourself, which you will
    learn how to do in this tutorial."""  ),

    TutoringItem(
    subject="Point Boundaries and Edge Boundaries",
    comments=

    """OOF2 provides two kinds of boundaries, BOLD(point boundaries)
    and BOLD(edge boundaries).  A point boundary is merely a
    collection of one or more nodes. An edge boundary is a collection
    of one or more segments with a specified direction."""  ),

    TutoringItem(
    subject="Sample Skeleton",
    comments= """Let us load a sample skeleton.  Locate the file
    BOLD(two_circles.skeleton) within the
    share/oof2/examples directory in your OOF2 installation.

    Choose BOLD(Load/Data) from the BOLD(File) menu in the main OOF2
    window.  Open the file BOLD(two_circles.skeleton).

    Open a graphics window, if you haven't yet.
    """,
    signal = ("new who", "Skeleton")
    ),

    TutoringItem(
    subject="Three Boundaries to Create",
    comments=

    """We'll create three additional boundaries in this skeleton.

    1. A clockwise edge boundary along the circumference of
    the BOLD(red) circle.

    2. A point boundary along the circumference of the BOLD(yellow) circle.

    3. An edge boundary directed left-to-right along the interface
    between BOLD(white) and BOLD(cyan) layers.

    The typical process of creating boundaries involves
    two simple steps. Select source objects such as nodes
    (for point boundaries) and segments (for edge boundaries) and
    create a boundary (with a given direction, if needed).

    Inevitably, you'll need to know how to select objects
    efficiently to minimize the effort involved."""
    ),

    TutoringItem(
    subject="Selecting Elements by Dominant Pixel",
    comments=
    
    """Let us create the first boundary.

    Open the BOLD(Skeleton Selection) toolbox from
    the graphics window.  Make sure that the toolbox is in BOLD(Element)
    mode and select BOLD(ByDominantPixel) from the pull-down menu
    for the parameter BOLD(Method).

    Click on any BOLD(red) pixel to select all the elements inside
    the circle.""",
    signal = "changed element selection"
    ),

    TutoringItem(
    subject="Selected Elements",
    comments=

    """The selected elements should be displayed as dark red and the
    size of the selection should be BOLD(105) (shown at the bottom of
    the toolbox).

    Open the BOLD(Skeleton Boundaries) page in the main OOF2 window."""
    ),        

    TutoringItem(
    subject="Edge Boundary from Selected Elements",
    comments=

    """Click BOLD(New...) in the BOLD(Boundaries) pane on the left
    side of the page to bring up a boundary builder.

    Check the little box that is next to the parameter BOLD(name) and
    type in BOLD(red_circle) for the name of the boundary.

    Select BOLD(Edge boundary from elements) and select BOLD(<selection>)
    for the parameter BOLD(group).  Set BOLD(direction) to be
    BOLD(Clockwise).

    Click BOLD(OK) to create the boundary.""",
    signal = "new boundaries for tutorial"
    ),

    TutoringItem(
    subject="Boundary Display",
    comments=

    """The newly created boundary should be listed and selected in the
    boundary list in the left side of the BOLD(Skeleton Boundaries)
    page.

    Its details are listed in the right side of the page.

    The new boundary is displayed in the graphics window, too."""  ),

    TutoringItem(
    subject="Second Boundary",
    comments=

    """Next is the point boundary along the perimeter of the
    BOLD(yellow) circle.  This one can be constructed in a similar way
    as the first one.

    Just for the sake of practice, let's try a less simple way."""
    ),

    TutoringItem(
    subject="Elements by Dominant Pixel",
    comments=

    """In the BOLD(Skeleton Selection) toolbox in the graphics window,
    select BOLD(ByDominantPixel) for the BOLD(Element) selection method.

    Click on any BOLD(yellow) pixel in the circle.  You should see that
    BOLD(66) elements inside the yellow circle have been selected""",
    signal = "changed element selection"
    ),

    TutoringItem(
    subject="Selecting Nodes from Selected Elements",
    comments=

    """Open the BOLD(Skeleton Selection) task page in the main OOF2
    window.

    Select BOLD(Nodes) for the BOLD(Selection Mode), and pick
    BOLD(Select from Selected Elements) for the parameter
    BOLD(Action).  From two available options, turn only
    BOLD(boundary) on so that only the nodes along the boundary of the
    selected elements will be selected.

    Click BOLD(OK) to make a selection.  The selected nodes will be
    displayed as BOLD(blue) dots in the graphics window.""",
    signal = "changed node selection"
    ),

    TutoringItem(
    subject="Point Boundary from Selected Nodes",
    comments=

    """Go back to the BOLD(Skeleton Boundaries) page and click
    BOLD(New...).

    In the boundary builder, give the name
    BOLD(yellow_circle) for the boundary.

    Select BOLD(Point boundary from nodes) for boundary building
    method and select BOLD(<selection>) for the parameter
    BOLD(group).

    Click BOLD(OK) to create the boundary.""",
    signal = "new boundaries for tutorial"
    ),

    TutoringItem(
    subject="Boundary Displayed",
    comments=

    """You should see the boundary information displayed in the page
    and its graphical representation displayed in the graphics window.

    If done correctly, the boundary should contain BOLD(31)
    points(nodes)."""
    ),

    TutoringItem(
    subject="Third Boundary",
    comments=

    """The third boundary is the edge between the white and the cyan
    material.

    First, we need to select all the segments along the boundary.  In
    the BOLD(Skeleton Selection) toolbox in the graphics window, click
    BOLD(Segment) in the upper part of the toolbox to start selecting
    segments.

    Select BOLD(Rectangle) for the selection method.  This will
    let you select all the segments that are completely
    inside a rectangular box drawn on the canvas.

    Click and drag the mouse to carefully draw a rectangle that
    surrounds all the segments along the interface.

    The selected segments should be displayed as thick BOLD(green)
    lines.  Properly done, BOLD(36) segments should be selected.

    You can always BOLD(Clear) the selection and repeat the process.
    If needed, click and drag while holding the BOLD(shift) (addition)
    or BOLD(ctrl) (toggle) modifier keys.  It may help to BOLD(Zoom)
    the window, using either the BOLD(Viewer) toolbox or the
    BOLD(Settings/Zoom) menu.""",
    
    signal = "changed segment selection"
    ),

    TutoringItem(
    subject="Edge Boundary from Selected Segments",
    comments=

    """Go back to the BOLD(Skeleton Boundaries) page, and click
    BOLD(New...).  Give the boundary a name, BOLD(white_cyan).  Select
    BOLD(Edge boundary from segments) with BOLD(<selection>) selected
    for the parameter BOLD(group).

    Set the direction to be BOLD(Left to right) and click BOLD(OK).""",
    signal = "new boundaries for tutorial"
    ),

    TutoringItem(
    subject="Viewing and Manipulating Boundaries",
    comments=

    """Boundaries, once created, can be modified, renamed, and even
    deleted in the BOLD(Skeleton Boundaries) page.

    Clicking on a boundary name in the list in the BOLD(Boundaries)
    pane selects the boundary.  Its name is highlighted in the list
    and the boundary is displayed in the graphics window.
    Control-clicking on a selected boundary name deselects it.  The
    BOLD(Modify), BOLD(Rename), and BOLD(Delete) buttons act on the
    currently selected boundary.""" ),

    TutoringItem(
    subject="Fin",
    comments=

    """So far, we've covered most of important features concerning
    skeleton boundaries.
    
    Further details, if needed, may be found in the manual.
    
    Thanks for trying out the tutorial."""
    )
    
    ])
