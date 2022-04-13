buildswiglibs(
  oof2common
  oof2engine
  ${${PythonVersion}_LIBRARIES}
  )

add_subdirectory(IO)
add_subdirectory(property)
add_subdirectory(elements)
