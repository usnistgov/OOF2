function b = residual(u,params)
% 
% R = RESIDUAL(U,PARAMS)
% 
% Computes the residual of the nonlinear weak form
% for the given U. 
% PARAMS includes some finite element parameters,
% related to the mesh.


coordinates = params.coordinates;
elements3   = params.elements3;
neumann     = params.neumann;

  
% Assembly of nonlinear rhs f(U)
b = sparse( size(coordinates,1), 1 );

for j = 1:size(elements3,1)
    
    elNodes    = elements3(j,:);
    nodeCoords = coordinates(elNodes,:);
    
    b( elNodes ) = b( elNodes ) + local_res( nodeCoords, u(elNodes) );
end

% Volume Forces
for j = 1:size(elements3,1)
    
    elNodes    = elements3(j,:);
    nodeCoords = coordinates(elNodes,:);

    b( elNodes ) = b( elNodes ) + ...
            det([1 1 1; nodeCoords']) * f( sum(nodeCoords)/3 ) / 6;
end

% Neumann conditions
for j = 1 : size(neumann,1)
    
    
    edgeNodes  = neumann(j,:);
    edgeCoords = coordinates( edgeNodes, : );
    edgeLen    = norm( edgeCoords(1,:) - edgeCoords(2,:) );
    
    b( edgeNodes )= b( edgeNodes ) - edgeLen * g( sum(edgeCoords)/2 ) /2;
end
