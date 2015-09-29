function VolumeForce = f(x);
%F   Volume force in considered domain.
%   Y = F(X) returns values of forces at N discrete points 
%   in the considered domain. This input data has to be choosen
%   by the user. X has dimension N x 2 and Y has dimension N x 1.
%
%
%   See also FEM2D_NONLINEAR, U_D, and G.
%

%    J. Alberty, C. Carstensen and S. A. Funken  11-19-98
%    File <f.m> in $(HOME)/acf/fem2d_nonlinear/
%    This program and corresponding files give Fig. 5a in 
%    "Remarks around "50 lines of Matlab: Short finite element 
%    implementation".

VolumeForce = zeros(size(x,1),1);
