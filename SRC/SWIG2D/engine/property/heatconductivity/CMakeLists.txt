buildswiglibs(
  oof2common
  oof2engine
  ${${PythonVersion}_LIBRARIES}
  )

add_subdirectory(nonlinear)
