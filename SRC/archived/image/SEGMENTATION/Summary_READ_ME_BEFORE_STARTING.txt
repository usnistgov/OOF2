This is a summary file of what has been done Summer 07 on Image Segmentation.

Attempted to create an image segmentation function. Ideally a 'one click' function. 
That was not achieved but a bunch of image tools and 'pretty good' thresholding methods were found.  
To RUN/COMPILE this part, add 'seg' option to the ./oof2-build command
Some of the tasks can be added to OOF anytime, and don't necessarily have to do with the segmentation. They can help with how segmentation is done currently (as far as I can tell, just by regular thresholding of an image by intensity). 
These are:
-spread
-shrink
-draw line on image
-delete small 'clumps'
-burn image
-different toGray function
 
How stuff is organized in the files:
-Main explanation of class does in .h file. Functions explained in the .C file. .swg and .spy files do not have explanations
-oldstuff directory might not be necessary. stuff that isn't used now that was used before. might be useful so don't have to rewrite something already written. 
In all the thresholding functions, '1' is an edge and '0' is background. Inside the code .5 often means undecided. 

Main file:
 segmenter.spy: This has all of the starter calls to everything. If you want to decode what happens, go there. 

What do all the files mean:
canny: Implements canny algorithm. Used in thresholding class.
skeletonize: Skeletonize image (thin edges). Has two different ways of skeletonization. 
thresholding: Threshold image in different ways -> simple thresholding, hysteresis thresholding, canny, new gabor, etc
diffusionRHS: Types of timesteps (diffusion) to be taken on an image. Used in thresholding class.
classify: uses burn algorithm to assign neighboring pixels of same color to a separate color
mask: Used by several classes to apply mask to image. Mask is a NxN matrix that is placed around each pixel in an image to apply an operation to the pixels around it.
imageops: Storage place of several different image operations. Shrinking, spreading, draw line on image, etc.
fixborders: After image is thresholded, problems remain in image. This class attempts to connect lines that don't quite connect, and delete 'clumps' that should not be part of the actual image
newgabor: Apply newgabor filter. Used in thresholding class. 
 
Things that work the best right now:
For most images NewGabor (not written by me) works the best. It is best when gaussian blur is applied before (or some other diffusion). The best regular values for the gabor are set as the default. After that 'small clumps must be deleted' which range in size depending on the size of the image. Then usually the white borders are expanded a couple of times, and then shrunk. After that the image is skeletonized, and this produces the best possible result. All of these operations are put together in 'CompleteSegmentation' option in the imagemodifier menu. They can also all be done separately. The fields with BINARY in the front should only be applied to binary images. 
****If looking at an image with very thick borders (like K1_small) then it is good to oversement the image, then shrink it, and then use the old 'edge' imagemodifier in order to pick up the 'edges' of the borders, rather than the center part*****

The available operations added to ImageProcessing:
-CompleteSegmentation: Combination that is usually used in segmentation process. Usually done in that order. Not all have to be used, but the Thresholding step is necessary for the 'binary image' steps that follow it. Might be good to have some requisite that those options are not available until a Thresholding type has been selected. 
-Diffusion: Take a timestep
-DiffusionChange: Show the change in the timestep. Final-original. Good way to figure out where to set a threshold
-Thresholding: All the thresholding options shown here: simple thresholding, canny, new gabor, experimental 
-ThresholdBasedOnChange: Simple thresholding (if greater than threshold then border if not then background) based on the change during the timestep.
-BINARYExpand: Takes all of the white pixels (default, can be set to different color with one of the parameters) and expands to the given amount of pixels out.
-BINARYShrink: For each of the white (by default) pixels, deletes the bordering pixel. Does not preserve connectivity.
-BINARYSkeletonization: Thins the lines in an image to just one pixel. Has two different options of how to do so.
-BINARYChangeBinaryImage: Needs a better name. Deletes 'clumps' that are smaller than given size. Connects pixels within 2 pixels of each other.
-BINARYDrawLineOnImage: Draws a line from start to finish. One pixel width line.
-BINARYBurnImage: Assigns each neighboring color block in an image to a different color. 

Example of how to get a good image: (images stored in images_used folder) Given in newgabor terms because that does work the best. Out of the 'RegularThresholding' the Anti_Geometric is the best, and for Canny, it depends on the image. Both of those run very fast.
-Small_k1
1. CompleteSegmentation:
 - GaussianBlur
 - NewGabor -> 4,3,6,1,.07,.11
 - Fix 30, true
 - Skeletonize -> true, true
 
-Small_K1 in order to do edging
1. Thresholding: NewGabor -> 5,4,6,1,.07,.08
2. Expand
3. Fix -> Delete small clumps, connect neighbors
4. Edge

-grains
1. Complete Segmentation:
  NewGabor -> 5,7,8,0,.08,.1
  Fix -> 1, connect neighbors
2. Fix -> Delete clump 200
3. Spread x 3
4. Skeletonization

-alternate grains
1. Complete Segmentation:
   New Gabor -> 5, 6, 6, 0, .075, .09
   Fix -> 200, connect neighbors
2. Spread x 2
3. Skeletonization

-raw
1. Complete Segmentation:
    NewGabor -> 4,4,8,1,.08, .1
   Fix -> clump 20, true
2. Spread x 2
3. Skeletonize

-composite
1. CompleteSegmentation
   NewGabor -> 3,5,6,1,.02,.025
   ChangeImage -> 100, not connect
2. Expand
3. Skeletonize

Ideas I have tried and do NOT work:
 -Adaptive thresholding. 
 -Region merging
 -Any other line-thinning algorithms. I have tried about 10. Wikipedia has a nice article about skeletonization, and list of all different algorithms possible, I have the ones that work the best up.
 -Merging regions by color similarity -> its all about the change in color
 -Look through image/GRAINBDY directory. Has implementation of other different types of gabor, sobel, etc. Lots of useful stuff that doesn't need to be rewritten if things go in that direction.
 -Image operations through matrices: matrices are slow. Way too slow for practicality (for small image operations can take up to a minute, so this will not work at all for larger images).
 
Ideas for the future:
 1.Find a way to connect edges: AFTER you threshold... and AFTER you skeletonize etc, you still have some edges that are not found, and can sort of be seen as one twig going toward another twig. So find a way for them to be connected. Maybe zoom in on that area, and do an adaptive thresholding routine around that area.
 
 2. The 'ExperimentalThresholding' is me playing with region merging. I feel like this has potential. The concept is that you undersegment the image, and then the areas that are not classified are then merged with adjacent areas. Currently this crashes for some reason. Also will need to find some way to break up the 'unclassified' regions into smaller ones, so that more precise merging because now when regions get merged, they are really parts of regions and some of them are borders and parts aren't and it would be better if there was a threshold set for how large a region for merging can be, so larger ones are split into smaller regions. 
 
 3. All of the thresholding is +/- a couple of pixels. One of the reasons is that when it is found whether certain pixel is part of an edge, it is considered edge if it is above certain value, therefore discounting the lower. So when there are no special black or white edges, then the lighter side is favored at an edge of two different colors. Need to correct that. Also become off by a couple of pixels in skeletonization, based on which direction is examined first.
 
 4. So maybe a one-click-button is impossible, but we can get closer? Have several different combinations of parameters for a type of image. Examples: different colors, for thick lines, for thin lines, for all image similar colors. Saved profiles for easier location of correct or almost correct values. Also for 'delete small clumps' to adjust to the size of the image.
 
 5. If NewGabor is used, which seems the best option, some work might be put in to attempting to make it more efficient. It takes quite a while to run for large images. 
 
 6. Some sort of tag should be added to images stating whether they are color, black and white, or binary. Then the operations that are not applicable to that type of image will not show up in the image processing menu.
 
 7. Two different types of grayify image functions should be present. One as the regular .3,.3,.3 which just weighs all colors equally, and one as a .2,.3,.5, which weighs red much less than blue, because the eye perceives red to be much higher in intensity than blue. This makes all colors be recognized better when grayed (see serendipity image for example of such). All of the segmenter functions use the .2,.3,.5 filter. 
 
 8. It will also be good to rename and maybe reorganize how things appear in the ImageModifier. 
 
 9. It would be good to have a function that would allow for selected pixels from 'pixelselection' menu to be made a certain color. This would allow 'drawing on an image'. True, this make it more of an 'image drawing' program, but sometimes edges cannot be found and it is easier to just draw them on there rather than having to fiddle. Also, the 'drawLineOnImage' function might have x and y messed up.

10. I am not 100% sure geometric diffusion works quite right. 

11. Maybe incorporate working directly from color images to a segmented image, so as to not lose the color in the segmentation. This may involve putting all of the filters through each of the three colors.

12. Some way of combining burn and spread so that the lines separating the different regions can be deleted. (burn so that each region can be of a different color). This would give maximal area to the actual material. This should be optional in case the 'borders' are themselves a material. 

13. The newgabor seems to favor the right top of each edge. This is probably something about what is checked first. I checked the code and I can't see where this might come from. This is similar to when skeletonize is called, the upper direction is favored. 

14. Incorporate the 'edge' function from the old image segmentation options into the 'skeletonization' as a different way to skeletonize (so when there are thick 'edges' that are materials themselves, they will be registered as such, rather than divided in the skeletonization step and given to the neighboring materials).