buildswiglibs(
  oof2common
  oof2engine
  ${${PythonVersion}_LIBRARIES}
  )

add_subdirectory(aniso)
add_subdirectory(iso)
add_subdirectory(largestrain)
add_subdirectory(nonlinear)
add_subdirectory(thermo)
add_subdirectory(visco)
