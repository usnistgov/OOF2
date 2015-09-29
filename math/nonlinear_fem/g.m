function Stress = g(x)
%G   Data on the Neumann boundary
%   Y = G(X) returns values of the normal-derivative at N discrete 
%   points on the Neumann boundary. This input data has to be choosen
%   by the user. X has dimension N x 2 and Y has dimension N x 1.
%
%
%   See also FEM2D_NONLINEAR, F, and U_D.

%    J. Alberty, C. Carstensen and S. A. Funken  02-11-99
%    File <g.m> in $(HOME)/acf/fem2d_nonlinear/
%    This Neumann boundary data is used to compute Fig. 5a in 
%    "Remarks around 50 lines of Matlab: Short finite element 
%    implementation"

Stress = zeros(size(x,1),1);
