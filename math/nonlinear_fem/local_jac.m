function M = local_jac(vertices,U)
% local_jac  Computes local functional Df(U,V) in considered problem.
%    M = LOCAL_JAC(VERTICES,U) computes the discretized total derivative
%    Df(U,V_j;W_k) of the local functional f(U,V_j) over the triangle
%    specified by VERTICES for given U and for V_j and W_k each being the
%    three local hat functions at the vertices of the triangle. VERTICES has
%    dimension 3 X 2 where the first column gives the x-coordinates of the 3
%    vertices and the second column their y-coordinates. U is a 3 x 1
%    dimensional array consisting of the values at the corresponding
%    vertices. M is a 3 x 3 dimensional array returning the value of
%    Df(U,V_j;W_k).


global quad_weight quad_pts phi_at_pts

if isempty( phi_at_pts ),  init_quadrature;  end


Eps  = 1/100;
G    = [ones(1,3);vertices'] \ [zeros(1,2);eye(2)];
Area = det([ones(1,3);vertices']) / 2;

M = Area*(Eps*G*G'-[2,1,1;1,2,1;1,1,2]/12);

% CHANGE THIS LINE TO SPECIFY DIFFERENT NONLINEAR RHS
f = 3*( phi_at_pts' * U ).^2;

M = M + Area * phi_at_pts * diag((quad_weight .* f)) * phi_at_pts';

% M = M + Area*([12*U(1)^2+2*(U(2)^2+U(3)^2+U(2)*U(3))+6*U(1)*(U(2)+U(3)),...
%       3*(U(1)^2+U(2)^2)+U(3)^2+4*U(1)*U(2)+2*U(3)*(U(1)+U(2)),...
%       3*(U(1)^2+U(3)^2)+U(2)^2+4*U(1)*U(3)+2*U(2)*(U(1)+U(3));
%   3*(U(1)^2+U(2)^2)+U(3)^2+4*U(1)*U(2)+2*U(3)*(U(1)+U(2)),...
%       12*U(2)^2+2*(U(1)^2+U(3)^2+U(1)*U(3))+6*U(2)*(U(1)+U(3)),...
%       3*(U(2)^2+U(3)^2)+U(1)^2+4*U(2)*U(3)+2*U(1)*(U(2)+U(3));
%   3*(U(1)^2+U(3)^2)+U(2)^2+4*U(1)*U(3)+2*U(2)*(U(1)+U(3)),...
%       3*(U(2)^2+U(3)^2)+U(1)^2+4*U(2)*U(3)+2*U(1)*(U(2)+U(3)),...
%       12*U(3)^2+2*(U(1)^2+U(2)^2+U(1)*U(2))+6*U(3)*(U(1)+U(2))]/60);
