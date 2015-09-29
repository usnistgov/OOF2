function show(elements3,elements4,coordinates,u)
%SHOW   Presents two-dimensional piecewise affine function graphically.
%    SHOW(ELEMENTS3,ELEMENTS4,COORDINATES,U) presents a two-dimensional
%    spline function graphically. ELEMENTS3 denotes a set of triangles
%    with dimension (no. of triangles) x 3 and ELEMENTS4 denotes a set of 
%    parallelograms (dimension (no. of parallelograms) x 4. Both arrays 
%    include number of nodes. The nodes have to be counted clockwise.
%    or anti-clockwise. The coordinates of the nodes are stored in an
%    (no. of coordinates) x 2 - dimensional array called COORDINATES.  
%    Its i'th row defines the x- and y- coordinate of the i'th node. U is
%    a (no. of coordinates) x 1 - dimensional array containing in the
%    i'th row the value of the spline function at the i'th node.

%    J. Alberty, C. Carstensen and S. A. Funken  02-11-99
%    File <show.m> in $(HOME)/acf/fem2d/ and
%                  in $(HOME)/acf/fem2d_heat/ and
%                  in $(HOME)/acf/fem2d_nonlinear/.

trisurf(elements3,coordinates(:,1),coordinates(:,2),u','facecolor','interp')
hold on
trisurf(elements4,coordinates(:,1),coordinates(:,2),u','facecolor','interp')
hold off
view(10,40);
title('Solution of the Problem')