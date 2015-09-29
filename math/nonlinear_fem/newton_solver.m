function u = newton_solver(u0,initialize,residual,jacobian)
%
% U = NEWTON_SOLVER(U0,INITIALIZE,RESIDUAL,JACOBIAN)
% 
% This solves the nonlinear weak form specified by the given 
% RESIDUAL and JACOBIAN functions, which are functions of
% U and PARAMS. The function INITIALIZE given as an argument
% initializes the finite element scheme that is used and
% U0 may be given as an initial iterate.
% The solution is returned as U.


max_iter = 50;   tol = 10^-10;

[u,params]  = initialize(u0);

elements3   = params.elements3;
dirichlet   = params.dirichlet;
freeNodes   = params.freeNodes;
coordinates = params.coordinates;

for i=1:max_iter

    J = jacobian( u, params );
    
    r = residual( u, params ); 

    du = zeros( size(coordinates,1), 1 );
    du(unique(dirichlet)) = 0;

    du(freeNodes) = - J(freeNodes,freeNodes) \ r(freeNodes);
    
    u = u + du;

%     show(elements3,[],coordinates,full(u));
%     pause;

    if norm(du) < tol,   break;   end
end

fprintf('\nNewton''s method converged to |du| < %3.2e in %d iterations.\n\n',tol,i);

show(elements3,[],coordinates,full(u));
