# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

add_subdirectory(color)
add_subdirectory(damping)
add_subdirectory(elasticity)
add_subdirectory(forcedensity)
add_subdirectory(heatcapacity)
add_subdirectory(heatconductivity)
add_subdirectory(heatsource)
add_subdirectory(massdensity)
add_subdirectory(orientation)
add_subdirectory(permittivity)
add_subdirectory(piezoelectricity)
add_subdirectory(planestrain)
add_subdirectory(plasticity)
add_subdirectory(pyroelectricity)
add_subdirectory(skeletonrelaxationrate)
add_subdirectory(stressfreestrain)
add_subdirectory(thermalexpansion)

## TODO: When surface properties are finished, uncomment the next line
## and add CMakeLists.txt files in the subdirectories.
# add_subdirectory(interfaces)
