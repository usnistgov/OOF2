function J = jacobian(u,params)
% 
% J = JACOBIAN(U,PARAMS)
% 
% Computes the Jacobian of the nonlinear weak form
% for the given U. 
% PARAMS includes some finite element parameters,
% related to the mesh.


coordinates = params.coordinates;
elements3   = params.elements3;

J = sparse( size(coordinates,1), size(coordinates,1) );

for j = 1:size(elements3,1)
    
    elNodes    = elements3(j,:);
    nodeCoords = coordinates(elNodes,:);
    
    J( elNodes, elNodes ) = J( elNodes, elNodes ) ...
                             + local_jac( nodeCoords, u(elNodes) );
end
