buildswiglibs(
  CFLAGS
  ${MAGICK_CFLAGS}
  LIBS
  oof2common
  oof2image
  ${MAGICK_LINK_LIBRARIES}
  ${${PythonVersion}_LIBRARIES}
  )

