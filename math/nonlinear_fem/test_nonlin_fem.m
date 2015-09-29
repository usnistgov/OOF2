
u0 = [];

u = newton_solver( u0, @init_fem, @residual, @jacobian );


% no_preconditioner = [];
% 
% u = nonlin_pcg( u0, @init_fem, @residual, no_preconditioner );
