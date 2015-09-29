function [u0,params]=init_fem(u0);
%
% [U,PARAMS] = INIT_FEM(U0)
% 
% This function initializes the finite element method
% by reading the mesh information from the files
% coordinates.dat, element3.dat, neumann.dat.
% This information is returned in PARAMS.
% An initial guess U is also returned and is all zeros
% unless specified to be some other value by U0.


load coordinates.dat; coordinates(:,1)=[];
load elements3.dat;   elements3(:,1)=[];

eval('load neumann.dat; neumann(:,1) = [];','neumann=[];');

load dirichlet.dat;   dirichlet(:,1) = [];

params.coordinates = coordinates;
params.elements3   = elements3;
params.dirichlet   = dirichlet;
params.neumann     = neumann;
params.freeNodes   = setdiff( 1:size(coordinates,1), unique(dirichlet) );

u0 = -ones(size(coordinates,1),1);
u0( unique(dirichlet) ) = u_d( coordinates(unique(dirichlet),:) );
