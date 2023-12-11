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

TutorialClass(
    subject = "Moving Nodes",
    ordering=2.1,
    tip="Methods for moving nodes in a skeleton.",
    discussion="""<para>
    This tutorial expands on the discussion of Node Motion in the
    "Skeleton" tutorial.
    </para>""",
    lessons = [

        TutoringItem(
    subject="Introduction",
    comments=
"""This tutorial expands on the discussion of Node Motion in the "Skeleton" tutorial.

OOF2 employs two methods to adapt a Skeleton to a Microstructure's material boundaries -- <b>refinement</b> and <b>node movement</b>.

Refinement, of course, chops target elements into smaller pieces, increasing global homogeneity and at the same time increasing element density along material boundaries.  Refinement is in some sense a blind operation -- it doesn't know exactly where material boundaries are, only that an element or segment needs to be divided.

On the other hand, node movement can place nodes exactly on material boundaries.  This tutorial covers most of the basics regarding node movement. """ ),

    TutoringItem(
    subject="Getting Ready",
    comments=
"""First, in the <b>Settings/Graphics Default</b> menu, set <b>New Layer Policy</b> to <b>Single</b> so that you won't have to manipulate graphics layers too often.

This tutorial uses four example files, <b>composition.skeleton</b>, <b>serendipity.skeleton</b>, <b>triangle.skeleton</b>, and <b>green_corner.skeleton</b>.  Locate them within the share/oof2/examples directory in your OOF2 installation."""
    ),

    TutoringItem(
    subject="Refine or node movement",
    comments=
"""Whenever you have heterogeneous elements, you typically have two choices -- refinement or node movement.

The order of operations actually plays a critical role in the quality of the resulting skeleton.

Let us load a sample skeleton to see the effect.

Choose <b>Load/Data</b> from the <b>File</b> menu in the main OOF2 window.  Open the file <tt>composition.skeleton</tt>.  """,),
    
    TutoringItem(
    subject="Snap Nodes and Refine",
    comments=
"""Open a graphics window to view the skeleton.

Only <b>8</b> out of <b>25</b> elements are homogeneous at this point.  It is tempting to move nodes to create more homogeneous elements cheaply.

Open the <b>Skeleton</b> page from the main OOF2 window. Set the <b>method</b> in the <b>Skeleton Modification</b> pane to <b>Snap Nodes</b> and set <b>targets</b> to be <b>All Nodes</b>.

For <b>criterion</b> select <b>Average Energy</b> and set its <b>alpha</b> to be <b>1</b>.

Click <b>OK</b> to snap nodes.""",),

    TutoringItem(
    subject="Snap Nodes and Refine -- continued",
    comments=
"""Depending on your luck -- we'll get to this later -- you created about <b>8</b> more homogeneous elements.

Not too bad.

At this stage, continuing to move nodes will yield only a marginal improvement.  We need to refine the heterogeneous elements.

Set the Skeleton Modification method to <b>Refine</b>. Set <b>targets</b> to <b>Heterogeneous Elements</b> with <b>threshold</b> = <b>1</b>. Set <b>criterion</b> to <b>Unconditional</b>, and <b>degree</b> to <b>Trisection</b> with <b>rule_set</b> = <b>conservative</b>.

Set <b>alpha</b> = <b>0.5</b>.

Click <b>OK</b> to refine. """,
    ),
      
    TutoringItem(
    subject="Snap Nodes and Refine -- part 3",
    comments=
"""Let us check the homogeneity index for this skeleton, which can be found at the left side of the <b>Skeleton</b> page.  It should be around <b>0.9</b> - <b>0.92</b>. Note that the resulting Skeleton is <b>U-G-L-Y</b>.

Now, Click <b>Undo</b> from the page twice to restore the initial skeleton.

Next time, we'll refine first and move nodes later. """,
    ),
      
    TutoringItem(
    subject="Refine and Snap Nodes",
    comments=
"""<b>Refine</b> the initial skeleton with the same options as before.

And then, do <b>Snap Nodes</b> with the same options. """,
    ),

    TutoringItem(
    subject="Refine and Snap Nodes - Continued",
    comments=
"""The difference is significant.

First of all, the homogeneity index for this skeleton is almost <b>1</b> -- the previous one was in the low <b>0.9</b>'s.
    
Thus, it becomes clear that node movement is most effective after a skeleton has been appropriately refined.

Unfortunately, "appropriately" is a very subjective word and OOF2 doesn't notify users of the best time to start moving nodes.

However, when most of the heterogeneous elements contain only two different pixel materials, a skeleton can be considered to be <b>appropriately</b> refined."""
    ),

    TutoringItem(
    subject="Serendipity",
    comments=
"""OOF2 provides four node moving tools - Snap Nodes, Anneal, Smooth, and manual node motion.

These tools (except for manual node motion) move nodes in a random order to avoid any potential artifacts caused by the internal node (element) ordering of the skeleton.

Thus, two identical node move processes can yield different outcomes.

Let us load a test skeleton and continue on the subject.

Before we load a new skeleton, let's delete the current one.  This isn't absolutely necessary but it simplifies things.

Open the <b>Microstructure</b> page.
    
Click <b>Delete</b> in the row of buttons near the top to delete the existing Microstructure and Skeleton at the same time.

As soon as you confirm the deletion, the graphics window will be emptied.""",
    ),

    TutoringItem(
    subject="Serendipity -- continued",
    comments=
"""Load the file <b>serendipity.skeleton</b> with the <b>Load/Data</b> command in the <b>File</b> menu.

(The new Image and Skeleton should appear automatically in the graphics window, because <b>New Layer Policy</b> is <b>Single</b> and there is only one Image and one Skeleton.  If you didn't delete the previous Image and Skeleton, then the new ones won't appear, unless you had set the <b>New Layer Policy</b> to <b>Always</b>.) """
    ),
    
    TutoringItem(
    subject="Serendipity -- final",
    comments=
"""Open the <b>Skeleton</b> task page in the main OOF2 window.

Select <b>Snap Nodes</b>.  Set <b>targets</b> to <b>All Nodes</b> and <b>criterion</b> to <b>Average Energy</b> with <b>alpha</b>=1.

Click <b>OK</b> to move modes.

Go to the message window and check how many nodes have been moved.

Also, check the result in the graphics window.

Now, <b>Undo</b> the modification and click <b>OK</b> again.

You may see a different result this time.

Repeat the <b>Undo</b>-<b>OK</b> dance, you'll see the effect. """,
    ),

    TutoringItem(
    subject="Anneal or Snap Nodes",
    comments=
"""The <b>Anneal</b> skeleton modifier moves nodes randomly and accepts or rejects the moves based on a given criterion.

Let us try annealing the current skeleton.

Before you go further, restore the skeleton to its initial status by <b>Undo</b>ing repeatedly.

If the <b>Undo</b> button is grayed out, it means the skeleton is in its initial state (or that you made so many moves that the undo/redo stack overflowed, in which case you should delete and reload the Skeleton).

Select <b>Anneal</b> as the Skeleton Modification Method.

Set <b>targets</b> to be <b>Heterogeneous Elements</b> with <b>threshold</b>=1, meaning that only the nodes of the heterogeneous elements will be moving.

Choose <b>Average Energy</b> for <b>criterion</b> and set <b>alpha</b> to be <b>0.95</b>.

Set the <b>iteration</b> parameter to <b>Fixed Iterations</b> and set the number of iterations to <b>50</b>.

For every iteration, each node will be moved to a randomly chosen position.  The move will be accepted only if it lowers the average "energy" of all of the surrounding elements.  (The energy function, described in the "Skeleton" tutorial, optimizes the shape and homogeneity of the elements.)

Click <b>OK</b> to give it a go.
    
Bring up the message window to check the progress. """,
    ),

    TutoringItem(
    subject="Anneal or Snap Nodes -- continued",
    comments=
"""Amazingly, most of the nodes moved to places where you want them to go.

Some elements, however, are still not homogeneous.

The other issue is that most nodes that appear to be correctly placed are actually not exactly on the boundaries, due to the fact that their positions have been randomly generated.

Let us <b>Undo</b> the change and use <b>Snap Nodes</b> this time. """,
    ),
    
    TutoringItem(
    subject="Anneal or Snap Nodes -- continued",
    comments=
"""Select <b>Snap Nodes</b> and give it a go with the same options as before.

Because of the random order in which nodes are moved, different results are possible.  Two of the possible results resolve most of the boundaries completely -- the material boundaries lie beneath an element edge.  One of these cases snaps 14 nodes, and the other snaps 13. (There are possible 13 node snaps that create skinny vertical red elements -- these aren't the snaps we're looking for.)

If you didn't get one of these cases, <b>Undo</b> and try again.

Once you've found one of the two special cases, two or three more <b>Snap Nodes</b> will get the job done.  All the nodes moved should be exactly <b>on</b> the boundaries.  """,
    ),

    TutoringItem(
    subject="Anneal or Snap Nodes - Final",
    comments=
    
"""This shows that some situations are more suited for <b>Snap Nodes</b> than <b>Anneal</b>.

Generally, snapping takes less time than annealing but snapping is a much more limited operation than annealing.  It only works for nodes of elements with certain boundary patterns, whereas annealing works for any nodes.  And of course, in a real example with a larger and more complicated skeleton, it's not feasible to repeatedly undo and repeat the snapping procedure until you get the skeleton you like.

In general, one of the more efficient ways of moving nodes is to <b>Snap</b> first and <b>Anneal</b> later.  This will be presented in the next set of tutorial slides."""
    ),

    TutoringItem(
    subject="Delete the Microstructure and Skeleton, again",
    comments=
"""Open the <b>Microstructure</b> page and <b>delete</b> the microstructure -- the Skeleton will be deleted at the same time. """,
    ),
      
    TutoringItem(
    subject="Annealing Revisited",
    comments=
"""Load a Skeleton from the file <b>triangle.skeleton</b> with the <b>Load/Data</b> command in the <b>File</b> menu. 

The unfinished skeleton for a blue triangle Microstructure should be displayed in the graphics window. """,
    ),

    TutoringItem(
    subject="Annealing Revisited -- continued",
    comments=
"""The Skeleton has been treated with <b>Snap Nodes</b> a few times so far and snapping won't help the situation any more. (Go ahead and try, anyway, if you like.)

The worst problem spot is at the left corner of the triangle.  If you look closely, however, you'll see that the mesh alignment at the other two corners isn't ideal, either.

These spots can be easily fixed by <b>Anneal</b>.

Open the <b>Skeleton</b> task page and select <b>Anneal</b>.

Keep the previous options, except set <b>iterations</b> to <b>20</b> and <b>delta</b> to <b>2</b>.  <b>delta</b> is the width (in pixels) of the gaussian distribution from which the random node motions are generated.  Since the bad node in the Skeleton is quite far from its ideal location, we need to generate large moves.

Click <b>OK</b> to give it a go.

Bring up the message window to monitor the progress, while visually enjoying the transformation of the skeleton.

If you were lucky, the element edges are well aligned with the material boundaries.  However it is likely that you need to do some fine tuning.  Set <b>delta</b> to 1 and iterate some more.""",
    ),

    TutoringItem(
    subject="Annealing Efficiently",
    comments=
"""You may have noticed that the <b>Acceptance Rate</b> reported in the Message window was pitifully low for the later steps of the annealing process.  That's because most of the nodes were already at their ideal positions, so most of the random moves were rejected.  There are various ways in OOF2 of restricting the domain of the annealing operation (and almost all other operations, as well).

<b>Undo</b> all of the Skeleton modifications to get back to the original mesh.  The next few tutorial slides will illustrate different ways of annealing efficiently. """,
    ),

    TutoringItem(
    subject="Annealing Selected Nodes",
    comments=
"""In the <b>Skeleton Selection</b> toolbox in the Graphics window, click on <b>Node</b> in the top row of buttons, to put the window into Node selection mode.

Leave the <b>Method</b> menu set to <b>Single_Node</b>.

    Click on the badly misaligned node near the lower left corner of the Skeleton (it's the one at the second column from the left and third row from the bottom) to select it -- it should appear as a blue dot.""",
    ),

    TutoringItem(
    subject="Annealing Selected Nodes -- continued",
    comments=
"""Back in the <b>Skeleton</b> page, set the <b>targets</b> parameter of the <b>Anneal</b> method to <b>Selected_Nodes</b>.

And set <b>alpha</b> and <b>iteration</b> to be <b>0.7</b> and <b>40</b>, respectively.

Click <b>OK</b> to anneal just the one selected node.

Notice that the process goes quite fast, but that it also doesn't produce a great result.  This is because the node can't move to the vertex of the triangle without creating a badly shaped quadrilateral (one with an interior angle near 180 degrees).

<b>Undo</b> your modification and try again with <b>alpha</b> in the <b>criterion</b> parameter set to <b>0.95</b>, so that shape energy is considered minimally.  The node should move closer to the vertex, but it creates an ugly element (the one to the southwest of the node, with an interior angle that's almost 180 degrees).

<b>Undo</b> this modification.""",
    ),

    TutoringItem(
    subject="Annealing Selected Elements",
    comments=
"""Back in the <b>Skeleton Selection</b> toolbox in the Graphics window, switch into Element Selection mode with the <b>Element</b> button in the top row.  Leave <b>Method</b> set to <b>Single_Element</b>.

Select the element surrounding the troublesome left hand vertex of the triangle.

Now <b>Anneal</b> with <b>targets</b> set to <b>Selected Elements</b>.

Click <b>OK</b>. (Repeat, if you're not satisfied.  Play around with different values of the annealing parameters, and with different sets selected nodes and elements.)

After it's done, click <b>Clear</b> from the <b>Skeleton Selection</b> to get a better view of the skeleton.

The Skeleton should match the Image much better than it did before, because with more nodes moving, the annealing process could avoid creating badly shaped elements.""",
    ),

    TutoringItem(
    subject="Active Areas",
    comments=
"""Sometimes it's necessary to restrict all operations to a portion of the Microstructure.  OOF2 lets you define an <b>Active Area</b>.  When an Active Area is defined, all operations apply only to pixels, nodes, and elements within the area.  This tutorial will use Active Areas to anneal the Skeleton.

<b>Undo</b> all the Skeleton modifications, and <b>Clear</b> the element/node selection.

Active Areas are defined in terms of pixels, so go to the <b>Pixel Selection</b> toolbox in the Graphics window.  Set <b>Method</b> to <b>Circle</b>.

Click and drag to select a circle of pixels in the vicinity of the left hand vertex of the triangle.  Make the circle big enough to enclose four or five elements.  It's ok if part of the circle lies outside the Microstructure.

Shift-click and drag to select a similar circle around the other two corners of the triangle.""",
    ),

    TutoringItem(
    subject="Active Areas -- continued",
    comments=
"""In the <b>Active Area</b> page in the main OOF2 window, set <b>Method</b> to <b>Activate Selection Only</b> in the <b>Active Area Modification</b> pane.

Click <b>OK</b>.

Notice that most of the Image is dimmed, indicating that it's inactive.  This will be more obvious if you <b>Clear</b> the selected pixels.  Go back to the <b>Pixel Selection</b> toolbox and press <b>Clear</b>.  Try selecting more pixels, and notice that only pixels within the active area are selected.""",
    ),

    TutoringItem(
    subject="Active Areas -- recontinued",
    comments=
"""Back in the <b>Skeleton</b> page in the main window, select <b>Anneal</b> again.  Set <b>targets</b> to <b>All Nodes</b>, and press <b>OK</b>.

Notice that only the nodes that start within the Active Area move.""",
    ),

    TutoringItem(
    subject="Active Areas -- closing remarks",
    comments=
"""The <b>Active Area</b> page lets you change the Active Area, save and restore Active Areas, and temporarily <b>Override</b> them.  The <b>Override</b> button, when pressed, makes the whole Microstructure active.  This can be important, for example, when you want to select some currently inactive pixels and add them to the current Active Area. """
    ),

    TutoringItem(
    subject="Manual Node Motion",
    comments=
"""OOF2 allows you to manually move nodes, which can resolve many tricky spots with ease.

Let us load a sample skeleton for this topic.

First, delete the current Microstructure and Skeleton.  Open the <b>Microstructure</b> page and click the <b>Delete</b> button.

Load a skeleton from the file <b>green_corner.skeleton</b>. """,
    ),

    TutoringItem(
    subject="Manual Node Motion -- continued",
    comments=
"""What has to be done for the skeleton is obvious.

Of course, <b>Anneal</b> can take care of this but if you're a control freak or short in the patience department, you can manually move the node to the spot where it has to be.

In the graphics window, open the <b>Move Nodes</b> toolbox.

Click on the bad node and drag it to where it belongs. """,
    ),

    TutoringItem(
    subject="Manual Node Motion -- continued",
    comments=
"""Unless you have unusual mouse-eye coordination, it's impossible to precisely locate a point in <b>mouse</b> mode. <b>Keyboard</b> mode allows more precise node moves.

<b>Undo</b> the move with the <b>Undo</b> button in the toolbox. (The <b>Undo</b> button on the <b>Skeleton</b> page in the main window does the same thing.)

Set the <b>Move with</b> button at the top of the toolbox to <b>Keyboard</b>.

Assuming that the problem node has to be absolutely positively at the corner of the boundary, in <b>keyboard</b> mode all you have to do is to find the position of the corner and type in the numbers. """,
    ),

    TutoringItem(
    subject="Manual Node Motion -- final",
    comments=
"""To find the coordinates of the corner, we need to pay a visit to the <b>Pixel Info</b> toolbox.

Once in the toolbox, click on the green pixel in the corner and you'll see that its pixel position is <b>(20, 11)</b>.

The size of the pixel in physical units is <b>1.0x1.0</b>.

Thus, the position of the corner in physical units is <b>(21.0, 11.0)</b> -- the origin <b>(0, 0)</b> is at the bottom-left corner of the microstructure.


Now, go back to the <b>Move Nodes</b> toolbox and click on the node in question.

It'll be highlighted with a pinkish dot.

Type in <b>21</b> and <b>11</b> in the text boxes next to <b>x</b> and <b>y</b>, respectively.

Now, click <b>Move</b> button to move the node. """,
    ),

    TutoringItem(
    subject="Done moving",
    comments=
"""Many aspects of node movement have been addressed in this tutorial.

The suggestions and opinions provided in the tutorials are <b>merely</b> guidelines, so practice a lot and find the right strategy for you and your Microstructures. """
    )
      
    ])
