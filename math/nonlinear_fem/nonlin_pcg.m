function u = nonlin_pcg(u0,init,f,precon)
% 
% U = NONLIN_PCG(U0,INIT,F,PRECON)
% 
% The nonlinear conjugate gradient algorithm to compute
% the solution of the nonlinear equation 
%     F(U) = 0
% The argument U0 is the initial vector for the iterations.
% The argument F is a function that takes a vector of
% the same size as U0 and a special structure PARAMS as input 
% and returns an output vector of the same size.
% The function PRECON, which is the preconditioner function,
% should be defined similarly.

warning('The nonlinear PCG function currently does not work well for the nonlinear FEM problem.');

tol = 10^-5;

i = 0;   i_max = 50;
k = 0;
n = prod(size(u0));

[u,params]  = init(u0);

elements3   = params.elements3;
dirichlet   = params.dirichlet;
freeNodes   = params.freeNodes;
coordinates = params.coordinates;

%     fprintf('%d %d (%3.2e)\n',i,-log2(s),delta_new/delta0)
%     
%     show(elements3,[],coordinates,full(u));
%     pause;

r = -f(u,params);

d = zeros(size(u));
d(unique(dirichlet)) = 0;
d(freeNodes) = r(freeNodes);

delta_new = full(r'*r);
delta0    = delta_new;

while (i < i_max) && (delta_new > tol^2 * delta0)
    
    s = choose_step_size(f,u,d,params);    
    u = u + s*d;
    
    r = -f(u,params);
    
    delta_old = delta_new;
    delta_new = full(r'*r);
    beta = delta_new / delta_old;
    
    d(unique(dirichlet)) = 0;
    d(freeNodes) = r(freeNodes) + beta*d(freeNodes);
    
    k = k+1; 
    if (k == n) || (r'*d <= 0)
        d = r;
        k = 0;
    end

    i = i+1;
    fprintf('%d %d (%3.2e)\n',i,-log2(s),delta_new/delta0)
%     
%     show(elements3,[],coordinates,full(u));
%     pause;
end

show(elements3,[],coordinates,full(u));
    

function s = choose_step_size(f,u0,d,params)

f0 = f(u0,params);

s = 1;  i = 0;  maxiter = 5;

u = u0 + s*d;

while (norm(f(u,params)) >= norm(f(u0,params))) && (i < maxiter)
    s = 1/2^i;  i = i+1;
    u = u0 + s*d;
end
