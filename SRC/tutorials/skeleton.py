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
    subject = "Skeleton",
    ordering=2,
    lessons = [
    TutoringItem(
    subject="Introduction",
    comments=
"""This tutorial is designed to give users an overview of how to create and modify an OOF2 <b>Skeleton</b>.

As you saw in the <b>Simple Example</b> tutorial, you can't create an FE mesh directly from a Microstructure in OOF2.

You need to first create a <b>Skeleton</b>, before you get to the FE mesh.  The Skeleton is a lightweight <b>geometric</b> representation of its FE mesh counterpart.  The main task in creating a Skeleton is adapting it to material boundaries.  """
        
    ),

    TutoringItem(
    subject="Creating a Microstructure from an Image File",
    comments=

"""Get started by creating a Microstructure.

Locate the file <b>small.ppm</b> within the share/oof2/examples directory in your OOF2 installation.

Open the <b>Microstructure</b> page and click <b>New from Image File</b> to create a new microstructure.

In the file selection dialog box, navigate to <b>small.ppm</b>.
    
Click <b>OK</b> to load the Image and create the Microstructure. """,
    ),
    
    TutoringItem(
    subject="Categorizing Pixels",
    comments=
"""The micrograph features <b>eight</b> distinct colors, each corresponding exactly to a microstructural feature.  Since the correspondence between colors and features is trivial, we can group pixels automatically.

Open the <b>Image</b> page and click the <b>Group</b> button.  Click <b>OK</b> in the dialog box.

Go back to the <b>Microstructure</b> page and you will see that <b>8</b> pixel groups have been created for the microstructure. The group names are the hexadecimal representations of the pixel colors in the groups. """
    ),

    TutoringItem(
    subject="The Skeleton Page",
    comments=
"""Now, open the <b>Skeleton</b> page, where we will spend most of the time in this tutorial.
    
The page is comprised of three parts.

The top part contains a <b>Skeleton Selector</b> and administrative features.  The <b>Skeleton Selector</b> is the two pull-down menus labelled <b>Microstructure</b> and <b>Skeleton</b>.  The first lets you choose a Microstructure and the second lets you choose a Skeleton belonging to that Microstructure.

The <b>Skeleton Status</b> pane on the left is a display for Skeleton summary data such as number of nodes and elements.

The <b>Skeleton Modification</b> pane on the right contains a bunch of skeleton modification tools that we will use to adapt a Skeleton to the material boundaries in its Microstructure.  """
    ),

    TutoringItem(
    subject="Creating a New Skeleton",
    comments=
"""Click <b>New...</b> to create an initial skeleton.
    
The <b>name</b> field is an automatic widget.  You can type a name, or leave it set to <i>&lt;automatic&gt;</i>, in which the name "skeleton" or "skeleton&lt;x&gt;" will be used, for some x.

The number of elements in the initial skeleton can be set with the parameters, <b>x_elements</b> and <b>y_elements</b>.

You can choose the element shape with the <b>skeleton_geometry</b> parameter.

For this tutorial, just use the default values for the initial skeleton: <b>x_elements</b>=4, <b>y_elements</b>=4, and <b>skeleton_geometry</b>=QuadSkeleton.  Leave the <b>periodicity</b> arguments set to <b>false</b>.

Click <b>OK</b> to create the Skeleton. """,
    ),

    TutoringItem(
    subject="Heterogeneous Elements",
    comments=
"""In the <b>Settings/Graphics Defaults</b> menu, set <b>New Layer Policy</b> to <b>Single</b>.  This will make new unique graphics layers appear automatically in new graphics windows.

Open a new <b>Graphics</b> window.  It should show the Skeleton on top of the image.  (Note that a graphics window that was opened before you loaded the Image or created the Skeleton won't show them unless you explicitly create a layer with the <b>Layer/New</b> menu item.)

For a Skeleton to be a good representation of a Microstructure, the <b>Elements</b> in the Skeleton must not cross boundaries between different <b>pixel types</b>.  Two pixels are defined to have the same type if they have the same Material assigned to them and if they belong to the same pixel groups.  Since we haven't assigned Materials yet, and since we've assigned groups according to pixel color, in this tutorial pixel color is synonymous with pixel type.

Except for one <b>yellow</b> element at the top-right corner of the skeleton, all the elements are <b>heterogeneous</b>, meaning that these elements contain pixels of two or more pixel types.

We want every element to be as homogeneous as possible."""
    ),

    TutoringItem(
    subject="Refining Elements",
    comments=
"""Let us subdivide these heterogeneous elements as the first step towards making them homogeneous.

In the <b>Skeleton Modification</b> pane in the <b>Skeleton</b> page, set the <b>method</b> pull-down menu to <b>Refine</b>.

Four parameters need to be set.

The parameter <b>targets</b> determines which elements should be refined.  Select <b>Heterogeneous Elements</b> and set its <b>threshold</b> to be <b>1.0</b>, meaning any heterogeneous elements will be refined.  (All elements with a <b>homogeneity</b> less than 1.0 will be refined.  The <b>homogeneity</b> is the largest fraction of an element's area belonging to a single pixel type.)
    
The second parameter <b>divider</b> determines how OOF2 decides to subdivide the edges of an element when refining it.  The choices are <b>Bisection</b> (dividing in two equal pieces), <b>Trisection</b> (Dividing in three equal pieces) or <b>TransitionPoints</b> (dividing at the points where a pixel boundary crosses the element edge). Select <b>Bisection</b>.

The parameter <b>rules</b> determines how OOF2 decides to subdivide the interior of an element after subdividing its edges.  Choosing <b>Quick<b> selects a small set of rules, and <b>Large<b> selects a larger set.  The larger set may produce better answers because it gives the progam more choices, but it's slower to run.  Set <b>rules</b> to <b>Quick</b>.

Finally, the parameter <b>alpha</b> determines how OOF2 compares possible refinements.  When <b>alpha</b> is near zero, oof2 chooses the arrangement that produces elements with the best shapes.  When <b>alpha</b> is near one, it tries to make the elements as homogeneous as possible. Set <b>alpha</b> to 0.5.

Click <b>OK</b> to refine the Skeleton. """,
    ),

    TutoringItem(
    subject="The Refined Skeleton",
    comments=
"""The refined skeleton should be displayed in the graphics window.

Every element (except one in the top-right corner) has been divided into 9 elements.  As a result, a larger fraction of the Microstructure's area is covered by homogeneous elements.

At the bottom of the <b>Skeleton Status</b> pane in the <b>Skeleton</b> page, there is a <b>Homogeneity Index</b>.  This number indicates the homogeneity of the entire skeleton.

As the skeleton becomes more homogeneous and adapts to material boundaries, the Homogeneity Index gets closer to <b>1</b>.

Click <b>Undo</b> and <b>Redo</b>, while checking out Homogeneity Index.

The number has been increased from <b>0.7306</b> to <b>0.8726</b>. """
    ),
    
    TutoringItem(
    subject="Another Refinement",
    comments=
"""We're still one more <b>Refine</b> away from being satisfied.

This time, leave <b>targets</b> set to <b>Heterogeneous Elements</b> and set <b>threshold</b> to <b>0.9</b>, so that only elements less than 90% homogeneous will be refined.

Click <b>OK</b> to start refining.  """,
    ),

    TutoringItem(
    subject="No More Refinements!",
    comments=
"""The Skeleton looks okay -- no material boundary is very far from an element boundary -- but the element boundaries don't really coincide with the material boundaries.  More work is necessary.

At this point, more refinements may not yield a favorable result.

You don't want to refine a skeleton to the point where it inevitably inherits the jagged pixel boundaries of the micrograph.

Thus, we need a different approach to resolve issues with the elements near the material boundaries.  """
    ),

    TutoringItem(
    subject="Moving Nodes to Material Boundaries",
    comments=

"""While <b>refinement</b> is more of a chop-and-hope-for-the-best approach to the heterogeneity issue, the <b>node motion</b> tools deal with the issue directly.

OOF2 provides three different methods of moving nodes in adapting to material boundaries -- <b>Snap Nodes</b>, <b>Anneal</b>, and <b>Move Nodes</b>.

<b>Snap Nodes</b> first looks for boundary points -- intersections between material boundaries and element edges -- and moves nodes to the corresponding points, if the result is favorable.

<b>Anneal</b>, on the other hand, moves nodes to randomly chosen points and accepts only the ones that are beneficial.

The <b>Move Nodes</b> toolbox in the <b>Graphics</b> window allows you to move nodes manually.  """
    ),
      
    TutoringItem(
    subject="Snapping Nodes",
    comments=
"""Select the <b>Snap Nodes</b> method in the <b>Skeleton Modification</b> pane in the <b>Skeleton</b> page.

This tool will move nodes of target elements to the material boundary points along the edges of the elements.

Select <b>Heterogeneous Elements</b> for the <b>targets</b> parameter and set the <b>threshold</b> to be <b>0.9</b>, meaning it will attempt to move nodes of elements with homogeneity less than <b>0.9</b>. 

For the <b>criterion</b> parameter, select <b>Average Energy</b> and set its parameter <b>alpha</b> to be <b>1</b>.

The quality of a Skeleton element is quantified by a functional, E, which is called an "energy" because of its role in the Skeleton annealing process.  E ranges from 0 for good elements to 1 for bad elements.  There are two contributions to E: a shape energy, which is minimized for squares and equilateral triangles; and a homogeneity energy, which is minimized for completely homogeneous elements.  The parameter <b>alpha</b> governs the relative weight of these two terms.  <b>alpha</b>=0 gives all the weight to the shape energy, while <b>alpha</b>=1 ignores shape and emphasizes homogeneity.

By setting <b>alpha</b>=1, we've told the <b>Snap Nodes</b> tool that it's ok if moving a node creates badly shaped elements, as long as doing so makes them more homogeneous. (We'll fix the bad shapes next.)

Click <b>OK</b> to make changes.  Notice that the <b>Homogeneity Index</b> increases from 0.957 to 0.991.""",
    ),

    TutoringItem(
    subject="Rationalizing Elements",
    comments=
"""Because <b>Snap Nodes</b> considered only homogeneity, some elements have been badly distorted while adapting themselves to the material boundaries.
    
Set the <b>Skeleton Modification</b> method to <b>Rationalize</b>.

This modification tool automatically removes badly shaped elements, provided the changes meet a certain criterion.

Set <b>targets</b> to <b>All Elements</b>.

Set <b>criterion</b> to <b>Average Energy</b> and set <b>alpha</b> to <b>0.8</b>.  With this setting, the <b>Rationalize</b> tool will only make changes that lower the average energy E of the affected elements.  <b>alpha</b> determines how E is computed.

For the <b>method</b> parameter, select <b>Specified</b>.

Three rationalization techniques are listed.  Move the mouse pointer over each technique to get more information about it. Make sure all three are selected and click <b>OK</b>, while keeping the default values for their parameters.

The summary for the modification is displayed in the <b>OOF Messages</b> window.  Also, in the graphics window, you will notice that many of the badly shaped elements are gone.  """,
    ),

    TutoringItem(
    subject="The Skeleton Selection Page",
    comments=
"""Open the <b>Skeleton Selection</b> page in the main OOF2 window.  This page provides tools for selecting Skeleton components -- elements, segments, and nodes -- and for manipulating groups of them.

Below the Skeleton selector at the top of the page, set <b>Selection Mode</b> to <b>Elements</b>.

From the <b>Element Selection Operations</b> pane in the right side of the page, select <b>Select By Homogeneity</b> for the parameter <b>Method</b> and set its <b>threshold</b> to be <b>0.9</b>, to select all elements less than 90% homogeneous.

Click <b>OK</b> to make a selection.

We will apply the next modification only to the selected elements. """,
    ),
      
    TutoringItem(
    subject="Splitting Quadrilaterals",
    comments=
"""Return to the <b>Skeleton</b> page and select <b>Split Quads</b> for the modification method.  This tool splits target quadrilaterals into two triangles.  A split is accepted only if it meets a specified criterion.

Select <b>Selected Elements</b> for the parameter <b>targets</b>.

Set <b>criterion</b> to be <b>Average Energy</b> with <b>alpha</b>=<b>0.9</b>.

A quadrilateral element can be split along either of its two diagonals.  The <b>split_how</b> parameter determines how OOF2 decides which diagonal to choose.  <b>Geographic</b> examines the element's neighbors to see if it's likely that there's a material boundary crossing the target element on a diagonal. <b>TrialAndError</b> splits a quadrilateral along the both diagonals and chooses the better of the two.  Set <b>split_how</b> to <b>Geographic</b>.
        
Click <b>OK</b> to modify the skeleton.""",
    ),

    TutoringItem(
    subject="Rationalizing, again",
    comments=
"""A handful of quadrilaterals have been split, but some badly shaped triangles were generated.

Select <b>Rationalize</b> and apply it to the Skeleton with the same settings as before.  """,
    ),

    TutoringItem(
    subject="Skeleton Selection",
    comments=
"""Go back to the <b>Skeleton Selection</b> page and again select elements by homogeneity with the threshold set to <b>0.9</b>.

Notice the reduced number of selected elements. """,
    ),
    
    TutoringItem(
    subject="Annealing",
    comments=
"""Return to the <b>Skeleton</b> page and select <b>Anneal</b> for the modification method.  <b>Anneal</b> moves nodes <b>randomly</b> and accepts or rejects the new positions according to the given criterion.  On each iteration, <b>Anneal</b> attempts to move each node once, but it chooses the nodes in a random order.

Select <b>Selected Elements</b> for its <b>targets</b>, meaning it will attempt to move nodes of the selected elements only.

For <b>criterion</b>, select <b>Average Energy</b> with <b>alpha</b> of <b>0.9</b>.

Set <b>T</b> to be <b>0.0</b> and also set <b>delta</b> to be <b>1.0</b>.  Move the mouse over these parameters to get more information.
    
For <b>iteration</b>, select <b>Conditional Iteration</b>, which stops annealing when certain conditions are met.  Set <b>condition</b> to <b>Acceptance Rate</b>, and set the <b>acceptanceRate</b> parameter to <b>7</b>.  This will terminate the annealing procedure if it starts accepting fewer than 7% of the attempted moves.

Set <b>extra</b> to <b>3</b>, to require that the <b>condition</b> be satisfied for three consecutive iterations before actually terminating the procedure.

Leave <b>maximum</b> set to <b>100</b>, setting an absolute limit on the number of iterations.
        
Click <b>OK</b>.

Watch the <b>Message</b> and <b>Graphics</b> windows to monitor the progress.""",
    ),

    TutoringItem(
    subject="Rationalizing ...",
    comments=
"""If you recall, we set <b>alpha</b> to <b>0.9</b> during the anneal.  This put a strong emphasis on homogeneity, thus many elements may have been distorted severely.

Select <b>Rationalize</b> for the modification method and click <b>OK</b>.  """,
    ),

    TutoringItem(
    subject="Reduced No. of Heterogeneous Elements",
    comments=
"""Open the <b>Skeleton Selection</b> page and select elements by homogeneity with <b>threshold</b> = <b>0.9</b>.

You will notice that the number of elements selected is significantly reduced.  """,
    ),
    
    TutoringItem(
    subject="Annealing Again",
    comments=
"""Return to <b>Skeleton</b> page and do the <b>Anneal</b> one more time with the same settings as before.  """,
    ),
    
    TutoringItem(
    subject="Rationalizing ...",
    comments=
"""Again, we need to <b>Rationalize</b> the skeleton before we move on to the next step.

Use the same settings as before.  """,
    ),        

    TutoringItem(
    subject="Almost Done",
    comments=
"""Open the <b>Skeleton Selection</b> page and select elements by homogeneity with the <b>threshold</b> being <b>0.9</b>.

There should be very few elements selected.  (Because of randomness in some modification methods, your results may vary.)

Set the <b>threshold</b> to be <b>0.8</b> and click <b>OK</b>.

There should be very few elements selected, meaning that most of the elements have been adapted to the material boundaries successfully.""",
    ),        
    
    TutoringItem(
    subject="Skeleton Quality Control",
    comments=
"""Move back to the <b>Skeleton</b> page and check the <b>Homogeneity Index</b>.

It should be almost <b>1</b>, which implies the skeleton is nearly homogeneous.

We'll now turn our attention to elements' quality, more precisely, their shape.

The tools for improving the skeleton's quality include <b>Swap Edges</b>, <b>Merge Triangles</b>, and <b>Smooth</b>.

These tools, however, can potentially affect material boundaries that have been established already.  Thus, we need to be extra careful not to disturb the existing boundaries.  The best way to avoid this potentially sorry situation is to pin down all the nodes along the boundaries.

The next slide will teach you how to do this.  """
    ),

    TutoringItem(
    subject="Pinning Nodes",
    comments=
"""Go to the <b>Pin Nodes</b> page.

In the pull-down menu labelled <b>Method</b>, Select <b>Pin Internal Boundary Nodes</b>. Click <b>OK</b>.

All the nodes along the boundaries should be selected and displayed as <b>yellow</b> dots.  These nodes are not going to move at all, until they are unpinned.

If the dots are too large and are obscuring the Skeleton, you can change their radius by editing their graphics layer.  In the graphics window's <b>Settings</b> menu, check <b>List All Layers</b>.  Make the window and layer list larger if necessary, and double-click the <b>PinnedNodesDisplay</b> line near the top of the layer list. Reduce the radius by changing the <b>size</b> parameter and click <b>OK</b>.  Uncheck <b>List All Layers</b> in the <b>Settings</b> menu. """,
    ),
    
    TutoringItem(
    subject="Swapping edges",
    comments=
"""Go back to the <b>Skeleton</b> page in the OOF2 main window and select <b>Swap Edges</b> for the modification method.  This takes any two neighboring elements and reorients their shared edge.

A swapped edge is accepted only when it meets a certain criterion.

Select <b>All Elements</b> for <b>targets</b>.

Select <b>Average Energy</b> for <b>criterion</b>.

Set <b>alpha</b> to <b>0.5</b>, putting equal emphasis on shape and homogeneity.

Click <b>OK</b> to swap edges.

Try <b>Undo</b>-<b>Redo</b> to see the changes wrought by the edge swap.

Also, it is a good idea to <b>Rationalize</b> the skeleton to remove potential bad elements created by the swap.  """,
    ),

    TutoringItem(
    subject="Merging Triangles",
    comments=
"""In addition to <b>Swap Edges</b>, you can merge two neighboring triangles into a quadrilateral.

Select <b>Merge Triangles</b> for the modification method.

Select <b>All Elements</b> for <b>targets</b> and select <b>Limited Unconditional</b> for <b>criterion</b>.

Set <b>alpha</b> to <b>0.5</b>, <b>homogeneity</b> to <b>0.9</b>, and <b>shape_energy</b> to <b>0.4</b>.

By doing this, you're accepting any changes, unless they produce elements for which the homogeneity drops below the specified value or the shape energy goes above the specified value.
    
Click <b>OK</b> to merge triangles.

Again, use <b>Undo</b>-<b>Redo</b> to see the changes better.  """,
    ),

    TutoringItem(
    subject="Smoothing the Skeleton",
    comments=
"""We're going to give the skeleton finishing touches by applying <b>Smooth</b>.  <b>Smooth</b> works much like <b>Anneal</b>, except that instead of picking node positions randomly, it moves each node to the average position of its neighbors.

Select <b>Smooth</b> for the modification method.

Select <b>All Nodes</b> for <b>targets</b>.

Select <b>Limited Unconditional</b> for <b>criterion</b> and set its parameters <b>alpha</b> to <b>0.5</b>, <b>homogeneity</b> to <b>0.9</b>, and <b>shape_energy</b> to <b>0.4</b>.

Select <b>Fixed Iterations</b> for <b>iteration</b>.  Set the number of <b>iterations</b> to 5.

Click <b>OK</b>.

Updates are reported in the same way as in <b>Anneal</b>.  """,
    ),

    TutoringItem(
    subject="Saving a Skeleton",
    comments=
"""The <b>Save/Skeleton</b> command in the <b>File</b> menu in the main OOF2 window, and the <b>Save</b> button on the <b>Skeleton</b> page both allow you to save Skeletons to a file.

The <b>format</b> parameter in the file selector dialog box was discussed in the <b>Microstructure</b> tutorial.

When you save a Skeleton, its Microstructure is saved with it in the data file.  Loading the data file with the <b>Load/Data</b> or <b>Load/Script</b> commands from the <b>File</b> menu restores both the Microstructure and the Skeleton.  """
    ),

    TutoringItem(
    subject="Homework",
    comments=
    
"""We have covered most of the issues related to Skeleton modifications.
    
Related topics not covered in this tutorial include <b>Active Areas</b>, and the <b>Move Node</b> toolbox.  """
    )
    ])
