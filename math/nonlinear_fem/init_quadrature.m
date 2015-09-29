function init_quadrature

global quad_weight quad_pts phi_at_pts

if isempty( phi_at_pts )

    quad_order = 4;
    
    phi1 = @(x) 1 - x(:,1) - x(:,2);
    phi2 = @(x) x(:,1);
    phi3 = @(x) x(:,2);

    switch quad_order
        case 1
            quad_weight = 1;
            quad_pts    = [ 1/3 1/3 ];
        case 2
            quad_weight = [ 1; 1; 1 ] / 3;
            quad_pts    = [ 2/3 1/6; 1/6 2/3; 1/6 1/6 ];
        case 3
            quad_weight = [ -0.5625;  25/48;  25/48;  25/48 ];
            quad_pts    = [ 1/3 1/3; 0.6 0.2; 0.2 0.6; 0.2, 0.2 ];
        case 4
            quad_weight = [ 0.223381589678011; 0.223381589678011; 0.223381589678011; ...
                            0.109951743655322; 0.109951743655322; 0.109951743655322 ];
            quad_pts    = [ 0.108103018168070, 0.445948490915965; ...
                            0.445948490915965, 0.108103018168070; ...
                            0.445948490915965, 0.445948490915965; ...
                            0.816847572980459, 0.091576213509771; ...
                            0.091576213509771, 0.816847572980459; ...
                            0.091576213509771, 0.091576213509771 ];
        otherwise
            error('Quadrature order should be one of 1,2,3,4!');
    end
    
    phi_at_pts = [ phi1( quad_pts ) phi2( quad_pts ) phi3( quad_pts ) ]';

end
