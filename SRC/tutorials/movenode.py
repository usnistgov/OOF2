# -*- python -*-
# $RCSfile: movenode.py,v $
# $Revision: 1.21 $
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

TutorialClass(
    subject = "Moving Nodes",
    ordering=2.1,
    lessons = [
    TutoringItem(
    subject="Introduction",
    comments=

    """This tutorial expands on the discussion of Node Motion in the
    "Skeleton" tutorial.

    OOF2 employs two methods to adapt a Skeleton to a Microstructure's
    material boundaries -- BOLD(refinement) and BOLD(node movement).

    Refinement, of course, chops target elements into smaller pieces,
    increasing global homogeneity and at the same time increasing
    element density along material boundaries.  Refinement is in some
    sense a blind operation -- it doesn't know exactly where material
    boundaries are, only that an element or segment needs to be
    divided.

    On the other hand, node movement can place nodes exactly on
    material boundaries.  This tutorial covers most of the basics
    regarding node movement. """ ),

    TutoringItem(
    subject="Getting Ready",
    comments="""
    This tutorial uses four example files, BOLD(green_corner.skeleton)
    BOLD(composition.skeleton), BOLD(serendipity.skeleton), and
    BOLD(triangle.skeleton).  Locate them within the
    share/oof2/examples directory in your OOF2 installation.
    """
    ),

    TutoringItem(
    subject="Refine or node movement",
    comments=

    """Whenever you have heterogeneous elements, you typically have
    two choices -- refinement or node movement.

    The order of operations actually plays a critical role in the
    quality of the resulting skeleton.

    Let us load a sample skeleton to see the effect.

    Choose BOLD(Load/Data) from the BOLD(File) menu in the main OOF2
    window.  Open the file BOLD(composition.skeleton).  """,

    signal = ("new who", "Skeleton")
    ),
    
    TutoringItem(
    subject="Snap Nodes and Refine",
    comments=
    
    """Open a graphics window to view the skeleton.

    Only BOLD(8) out of BOLD(25) elements are homogeneous at this
    point.  It is tempting to move nodes to create more homogeneous
    elements cheaply.

    Open the BOLD(Skeleton) page from the main OOF2 window. Set the
    BOLD(method) in the BOLD(Skeleton Modification) pane to BOLD(Snap
    Nodes) and set BOLD(targets) to be BOLD(All Nodes).

    For BOLD(criterion) select BOLD(Average Energy) and set its
    BOLD(alpha) to be BOLD(1).

    Click BOLD(OK) to snap nodes.""",
        
    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Snap Nodes and Refine -- continued",
    comments=
    
    """Depending on your luck -- we'll get to this later -- you
    created about BOLD(8) more homogeneous elements.

    Not too bad.

    At this stage, continuing to move nodes will yield only a marginal
    improvement.  We need to refine the heterogeneous elements.

    Set the Skeleton Refinement method to BOLD(Refine). Set
    BOLD(targets) set to BOLD(Heterogeneous Elements) with
    BOLD(threshold) = BOLD(1). Set BOLD(criterion) to
    BOLD(Unconditional), and BOLD(degree) to BOLD(Trisection) with
    BOLD(rule_set) = BOLD(conservative).

    Click BOLD(OK) to refine.
    """,
    signal = ("who changed", "Skeleton")
    ),
      
    TutoringItem(
    subject="Snap Nodes and Refine -- part 3",
    comments=

    """Let us check the homogeneity index for this skeleton, which can
    be found at the left side of the BOLD(Skeleton) page.  It should
    be around BOLD(0.9) - BOLD(0.92). Note that the resulting Skeleton
    is BOLD(U-G-L-Y).

    Now, Click BOLD(Undo) from the page repeatedly (actually twice),
    until you restore the initial skeleton in the graphics window.

    This time, we'll refine first and move nodes later.
    """,

    signal = ("who changed", "Skeleton")
    ),
      
    TutoringItem(
    subject="Refine and Snap Nodes",
    comments=

    """BOLD(Refine) the initial skeleton with the same options as
    before.

    And then, do BOLD(Snap Nodes) with the same options.
    """,
    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Refine and Snap Nodes - Continued",
    comments=

    """The difference is significant.

    First of all, the homogeneity index for this skeleton is
    almost BOLD(1) -- the previous one was in the low BOLD(0.9)'s.
    
    Thus, it becomes clear that node movement is most effective
    after a skeleton has been BOLD(appropriately) refined.

    Unfortunately, BOLD('appropriately') is a very subjective word
    and OOF2 doesn't notify users of the best time to start moving
    nodes.

    However, when most of the heterogeneous elements contain only two
    different pixel materials, a skeleton can be considered to be
    BOLD(appropriately) refined."""

    ),

    TutoringItem(
    subject="Serendipity",
    comments=
    
    """OOF2 provides four node moving tools - Snap Nodes, Anneal,
    Smooth, and manual node motion.

    These tools (except for manual node motion) move nodes in a random
    order to avoid any potential artifacts caused by the internal node
    (element) ordering of the skeleton.

    Thus, any two identical node move processes can yield different
    outcomes.

    Let us load a test skeleton and continue on the subject.

    Before we load a new skeleton, let's delete the current one.  This
    isn't absolutely necessary but it simplifies things.

    Open the BOLD(Microstructure) page.
    
    Click BOLD(Delete) to delete the existing Microstructure and
    Skeleton at the same time.

    As soon as you confirm the deletion, the graphics window will be
    emptied.""",

    signal = "remove who"
    ),

    TutoringItem(
    subject="Serendipity -- continued",
    comments=
    
    """Load the file BOLD(serendipity.skeleton) with the
    BOLD(Load/Data) command in the BOLD(File) menu.

    This time, the graphics window will not show the skeleton
    automatically.

    Let us make the graphics window display the Skeleton and the Image
    stored in Microstructure. 
    """,
        
    signal = ("new who", "Skeleton")
    ),

    TutoringItem(
    subject="Serendipity -- recontinued",
    comments=

    """Go to the graphics window and you'll see that the Layer List at
    the bottom of the window shows two display layers.  (You may have
    to scroll or resize the list window to see both layers.)

    Double-click on the first one that says BOLD(SkeletonEdgeDisplay).
    
    A window named BOLD(OOF2 Graphics Layer Editor) will pop up.
        
    In the BOLD(Displayed Object) pane, set BOLD(category) to
    BOLD(Skeleton).

    Since we have only one skeleton available in the system, it's
    automatically chosen.

    Click BOLD(Send) to display the skeleton.

    Now, double-click on the second layer, named BOLD(BitmapDisplayMethod).

    On the later editor, set BOLD(category) to BOLD(Image).

    Click BOLD(Send) to display the Image.

    Close the editor."""),
    
    TutoringItem(
    subject="Serendipity -- final",
    comments=
    
    """Open the BOLD(Skeleton) task page in the main OOF2 window.

    Select BOLD(Snap Nodes).  Set BOLD(targets) to BOLD(All Nodes)
    and BOLD(criterion) to BOLD(Average Energy) with BOLD(alpha)=1.

    Click BOLD(OK) to move modes.

    Go to the message window and check how many nodes have been moved.

    Also, check the result in the graphics window.

    Now, BOLD(Undo) the modification and click BOLD(OK) again.

    You may see a different result this time.

    Repeat the BOLD(Undo)-BOLD(OK) dance, you'll see the effect. """,

    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Anneal or Snap Nodes",
    comments=

    """The BOLD(Anneal) skeleton modifier moves nodes randomly and
    accepts or rejects the moves based on a given criterion.

    Let us try annealing the current skeleton.

    Before you go further, restore the skeleton to its initial status
    by BOLD(Undo)ing repeatedly.

    If the BOLD(Undo) button is grayed out, it means the skeleton is
    in its initial state (or that you made so many moves that the
    undo/redo stack overflowed, in which case you should delete and
    reload the Skeleton).

    Select BOLD(Anneal).

    Set BOLD(targets) to be BOLD(Heterogeneous Elements) with
    BOLD(threshold)=1, meaning that only the nodes of the
    heterogeneous elements will be moving.

    Choose BOLD(Average Energy) for BOLD(criterion) and set
    BOLD(alpha) to be BOLD(0.95).

    Set the BOLD(iteration) parameter to BOLD(Fixed Iterations) and
    set the number of iterations to BOLD(50).

    For every iteration, each node will be moved to a randomly chosen
    position.  The move will be accepted only if it lowers the average
    "energy" of all of the surrounding elements.  (The energy
    function, described in the "Skeleton" tutorial, optimizes the
    shape and homogeneity of the elements.)

    Click BOLD(OK) to give it a go.
    
    Bring up the message window to check the progress.
    """,

    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Anneal or Snap Nodes -- continued",
    comments=

    """Amazingly, most of the nodes moved to places where you want them
    to go.

    Some elements, however, are still not homogeneous.

    The other issue is that most nodes that appear to be correctly
    placed are actually not exactly on the boundaries, due to the fact
    that their positions have been randomly generated.

    Let us BOLD(Undo) the change and use BOLD(Snap Nodes) this time.
    """,

    signal = ("who changed", "Skeleton")
    ),
    
    TutoringItem(
    subject="Anneal or Snap Nodes -- continued",
    comments=
    
    """Select BOLD(Snap Nodes) and give it a go with the same options
    as before.

    Because of the random order in which nodes are moved, different
    results are possible.  Two of the possible results resolve most of
    the boundaries completely -- the material boundaries lie beneath
    an element edge.  One of these cases snaps 14 nodes, and the other
    snaps 13. (There are possible 13 node snaps that create skinny
    vertical red elements -- these aren't the snaps we're looking
    for.)

    If you didn't get one of these cases, BOLD(Undo) and try again.

    Once you've found one of the two special cases, two or three more BOLD(Snap
    Nodes) will get the job done.  All the nodes moved should be
    exactly BOLD(on) the boundaries.  """,

    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Anneal or Snap Nodes - Final",
    comments=
    
    """This shows that some situations are more suited for BOLD(Snap
    Nodes) than BOLD(Anneal).

    Generally, snapping takes less time than annealing but snapping is
    a much more limited operation than annealing.  It only works for
    nodes of elements with certain boundary patterns, whereas
    annealing works for any nodes.  And of course, in a real example
    with a larger and more complicated skeleton, it's not feasible to
    repeatedly undo and repeat the snapping procedure until you get
    the skeleton you like.

    In general, one of the more efficient ways of moving nodes is to
    BOLD(Snap) first and BOLD(Anneal) later.  This will be presented
    in the next set of tutorial slides."""  ),

    TutoringItem(
    subject="Delete the Microstructure and Skeleton, again",
    comments=
    
    """Open the BOLD(Microstructure) page and BOLD(delete) the
    microstructure -- the Skeleton will be deleted at the same time.
    """,
        
    signal = "remove who"
    ),
      
    TutoringItem(
    subject="Annealing Revisited",
    comments=

    """Load a Skeleton from the file BOLD(triangle.skeleton) with
    the BOLD(Load/Data) command in the BOLD(File) menu.  """,
        
    signal = ("new who", "Skeleton")
    ),

    TutoringItem(
    subject="Displaying the New Skeleton",
    comments=

    """To display the loaded skeleton, either repeat the layer editing
    procedure you used earlier, or just close the graphics window and
    open another one. (Graphics layers are created automatically only
    once per window.)
        
    The unfinished skeleton for a blue triangle Microstructure should
    be displayed in the graphics window.""", ),

    TutoringItem(
    subject="Annealing Revisited -- continued",
    comments=

    """The Skeleton has been treated with BOLD(Snap Nodes) a few times
    so far and it is obvious that snapping won't help the situation
    any more. (Go ahead and try, anyway, if you like.)

    The worst problem spot is at the left corner of the triangle.  If
    you look closely, however, you'll see that the mesh alignment at
    the other two corners isn't ideal, either.

    These spots can be easily fixed by BOLD(Anneal).

    Open the BOLD(Skeleton) task page and select BOLD(Anneal).

    Keep the previous options, except set BOLD(iterations) to BOLD(20)
    and BOLD(delta) to BOLD(2).  BOLD(delta) is the width (in pixels)
    of the gaussian distribution from which the random node motions
    are generated.  Since the bad node in the Skeleton is quite far
    from its ideal location, we need to generate large moves.

    Click BOLD(OK) to give it a go.

    Bring up the message window to monitor the progress, while
    visually enjoying the transformation of the skeleton.

    If you were lucky, the element edges are well aligned with the
    material boundaries.  However it is likely that you need to do
    some fine tuning.  Set BOLD(delta) to 1 and iterate some more.""",
        
    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Annealing Efficiently",
    comments=

    """You may have noticed that the BOLD(Acceptance Rate) reported in
    the Message window was pitifully low for the later steps of the
    annealing process.  That's because most of the nodes were already
    at their ideal positions, so most of the random moves were
    rejected.  There are various ways in OOF2 of restricting the
    domain of the annealing operation (and almost all other
    operations, as well).

    BOLD(Undo) all of the Skeleton modifications to get back to the
    original mesh.  The next few tutorial slides will illustrate
    different ways of annealing efficiently. """,

    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Annealing Selected Nodes",
    comments=

    """In the BOLD(Skeleton Selection) toolbox in the Graphics window,
    click on BOLD(Node) in the top row of buttons, to put the window
    into Node selection mode.

    Leave the BOLD(Method) menu set to BOLD(Single_Node).

    Click on the badly misaligned node near the lower left corner of
    the Skeleton (it's the one at the second column from the left and
    third row from the bottom) to select it -- it should appear
    as a blue dot.""",

    signal = "changed node selection"
    ),

    TutoringItem(
    subject="Annealing Selected Nodes -- continued",
    comments=


    """Back in the BOLD(Skeleton) page, set the BOLD(targets)
    parameter of the BOLD(Anneal) method to BOLD(Selected_Nodes).

    And set BOLD(alpha) and BOLD(iteration) to be BOLD(0.7) and BOLD(40),
    respectively.

    Click BOLD(OK) to anneal just the one selected node.

    Notice that the process goes quite fast, but that it also doesn't
    produce a great result.  This is because the node can't move to
    the vertex of the triangle without creating a badly shaped
    quadrilateral (one with an interior angle near 180 degrees).

    BOLD(Undo) your modification and try again with BOLD(alpha) in the
    BOLD(criterion) parameter set to BOLD(0.95), so that shape energy is
    considered minimally.  The node should move closer to the vertex.
    But the creation of an ugly element was unavoidable.

    BOLD(Undo) this modification.""",

    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Annealing Selected Elements",
    comments=

    """Back in the BOLD(Skeleton Selection) toolbox in the Graphics
    window, switch into Element Selection mode with the BOLD(Element)
    button in the top row.  Leave BOLD(Method) set to BOLD(Single_Element).

    Select the element surrounding the troublesome left
    hand vertex of the triangle.

    Now BOLD(Anneal) with BOLD(targets) set to BOLD(Selected Elements).

    Click BOLD(OK). (Repeat, if you're not satisfied.  Play around
    with different values of the annealing parameters, and with
    different sets selected nodes and elements.)

    After it's done, click BOLD(Clear) from the BOLD(Skeleton Selection) to
    get a better view of the skeleton.

    The Skeleton should match the Image much better than it did
    before, because with more nodes moving, the annealing process
    could avoid creating badly shaped elements.""",

    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Active Areas",
    comments=

    """Sometimes it's necessary to restrict all operations to a
    portion of the Microstructure.  OOF2 lets you define an
    BOLD(Active Area).  When an Active Area is defined, all operations
    apply only to pixels, nodes, and elements within the area.  This
    tutorial will use Active Areas to anneal the Skeleton.

    BOLD(Undo) all the Skeleton modifications, and BOLD(Clear) the
    element/node selection.

    Active Areas are defined in terms of pixels, so go to the
    BOLD(Pixel Selection) toolbox in the Graphics window.  Set
    BOLD(Method) to BOLD(Circle).

    Click and drag to select a circle of pixels in the vicinity of the
    left hand vertex of the triangle.  Make the circle big enough to
    enclose four or five elements.  It's ok if part of the circle lies
    outside the Microstructure.

    Shift-click and drag to select a similar circle around the other
    two corners of the triangle.""",

    signal = "pixel selection changed"
    ),

    TutoringItem(
    subject="Active Areas -- continued",
    comments=

    """ In the BOLD(Active Area) page in the main OOF2 window, set
    BOLD(Method) to BOLD(Activate Selection Only) in the BOLD(Active
    Area Modification) pane.

    Click BOLD(OK).

    Notice that most of the Image is dimmed, indicating that it's
    inactive.  This will be more obvious if you BOLD(Clear) the
    selected pixels.  Go back to the BOLD(Pixel Selection) toolbox and
    press BOLD(Clear).  Try selecting more pixels, and notice that
    only pixels within the active area are selected.""",

    signal = "active area modified"
    ),

    TutoringItem(
    subject="Active Areas -- recontinued",
    comments=

    """Back in the BOLD(Skeleton) page in the main window, select
    BOLD(Anneal) again.  Set BOLD(targets) to BOLD(All Nodes), and
    press BOLD(OK).

    Notice that only the nodes that start within the Active Area move.""",

    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Active Areas -- closing remarks",
    comments=

    """The BOLD(Active Area) page lets you change the Active Area,
    save and restore Active Areas, and temporarily BOLD(Override)
    them.  The BOLD(Override) button, when pressed, makes the whole
    Microstructure active.  This can be important, for example, when
    you want to select some currently inactive pixels and add them to
    the current Active Area.
    """
    ),

    TutoringItem(
    subject="Manual Node Motion",
    comments=

    """OOF2 allows you to manually move nodes, which can resolve
    many tricky spots with ease.

    Let us load a sample skeleton for this topic.

    First, delete the current Microstructure and Skeleton.  Open the
    BOLD(Microstructure) page and click the BOLD(Delete) button.

    Load a skeleton from the file BOLD(green_corner.skeleton).

    Again, you need to display the loaded objects in the graphics
    window manually, or open a new graphics window.
    """,
    signal = ("new who", "Skeleton")
    ),

    TutoringItem(
    subject="Manual Node Motion -- continued",
    comments=

    """What has to be done for the skeleton is obvious.

    Of course, BOLD(Anneal) can take care of this but if you're a
    control freak or short in the patience department, you can
    manually move the node to the spot where it has to be.

    In the graphics window, open the BOLD(Move Nodes) toolbox.

    Click on the bad node and drag it to the sweet spot.
    """,
    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Manual Node Motion -- continued",
    comments=

    """It's that simple to move a pain-in-the-butt node.

    The BOLD(keyboard) mode allows more precise node moves.

    BOLD(Undo) the move with the BOLD(Undo) button in the toolbox.
    (The BOLD(Undo) button on the BOLD(Skeleton) page in the main
    window does the same thing.)

    Set the BOLD(Move with) button at the top of the toolbox to
    BOLD(Keyboard).

    Now, assume that this problem node has to be absolutely positively
    at the corner of the boundary.
    
    Unless you're blessed with enormous mouse-eye coordination, it's
    impossible for you to spot the point in BOLD(mouse) mode.

    So, in BOLD(keyboard) mode, all you have to do is to find the
    position of the corner and type in these numbers.
    """,
    
    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Manual Node Motion -- final",
    comments=

    """To find the coordinates of the corner, we need to pay a visit
    to the BOLD(Pixel Info) toolbox.

    Once in the toolbox, click on the green pixel in the corner and
    you'll see that its pixel position is BOLD((20, 11)).

    The size of the pixel in physical units is BOLD(1.0x1.0).

    Thus, the position of the corner in physical units is (BOLD(21.0,
    11.0)) -- the origin (0, 0) is at the bottom-left corner of the
    microstructure.


    Now, go back to the BOLD(Move Nodes) toolbox and click on the node
    in question.

    It'll be highlighted with a pinkish dot.

    Type in BOLD(21) and BOLD(11) in the text boxes next to BOLD(x) and
    BOLD(y), respectively.

    Now, click BOLD(Move) button to move the node.
    """,
    signal = ("who changed", "Skeleton")
    ),

    TutoringItem(
    subject="Done moving",
    comments=

    """Many aspects of node movement have been addressed in this
    tutorial.

    The suggestions and opinions provided in the tutorials are
    BOLD(merely) guidelines, so practice a lot and find the right
    strategy for you and your Microstructures.
    """
    )
      
    ])
