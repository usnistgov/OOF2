function b = local_res(vertices,U)
% LOCAL_RES   Computes local functional f(U,V) in considered problem.
%    B = LOCAL_RES(VERTICES,U) computes the discretized local functional f(U,V_j)
%    over the triangle specified by VERTICES for given U and for V_j being the
%    three local hat functions at the vertices of the triangle. VERTICES has
%    dimension 3 X 2 where the first column gives the x-coordinates of the 3
%    vertices and the second column their y-coordinates. U is a 3 x 1
%    dimensional array consisting of the values at the corresponding
%    vertices. B is a 3 x 1 dimensional array returning the value of the
%    functional f(U,V_j) for the three corresponding vertices.


global quad_weight quad_pts phi_at_pts

if isempty( phi_at_pts ),  init_quadrature;  end


Eps  = 1/100;
G    = [ones(1,3);vertices'] \ [zeros(1,2);eye(2)];
Area = det([ones(1,3);vertices']) / 2;


b = Area*(Eps*G*G'-[2,1,1;1,2,1;1,1,2]/12)*U;

% CHANGE THIS LINE TO SPECIFY DIFFERENT NONLINEAR RHS
f = ( phi_at_pts' * U ).^3;

b = b + Area * phi_at_pts * (quad_weight .* f);

% b = b + Area*([4*U(1)^3+ U(2)^3+U(3)^3+3*U(1)^2*(U(2)+U(3))+2*U(1) ...
%       *(U(2)^2+U(3)^2)+U(2)*U(3)*(U(2)+U(3))+2*U(1)*U(2)*U(3);
%   4*U(2)^3+ U(1)^3+U(3)^3+3*U(2)^2*(U(1)+U(3))+2*U(2) ...
%       *(U(1)^2+U(3)^2)+U(1)*U(3)*(U(1)+U(3))+2*U(1)*U(2)*U(3);
%   4*U(3)^3+ U(2)^3+U(1)^3+3*U(3)^2*(U(2)+U(1))+2*U(3) ...
%       *(U(2)^2+U(1)^2)+U(2)*U(1)*(U(2)+U(1))+2*U(1)*U(2)*U(3)]/60);
