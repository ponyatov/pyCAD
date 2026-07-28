# cmake/FindREADLINE.cmake

```cmake
include(FindPackageHandleStandardArgs)

# ~~~
# - Try to find READLINE include dirs and libraries
#
# Find the READLINE includes and client library
# This module defines:
#  READLINE_FOUND, If false, do not try to use READLINE.
#  READLINE_INCLUDE_DIRS, where to find rte_config.h and rte_version.h
#  READLINE_LIBRARIES, the libraries needed by a READLINE user
#  READLINE_CFLAGS_OTHER, the compile flags to use
#  READLINE_VERSION, the version of the library
# ~~~

find_package(PkgConfig REQUIRED)
pkg_check_modules(READLINE REQUIRED readline>=8.2)

if(READLINE_FOUND)
  message("-- Found READLINE: ${READLINE_LIBRARIES} (found version \"${READLINE_VERSION}\")")
  add_compile_definitions(READLINE_FOUND)

  add_library(READLINE::READLINE INTERFACE IMPORTED)    

  target_include_directories(READLINE::READLINE INTERFACE ${READLINE_INCLUDE_DIRS})
  target_compile_options(READLINE::READLINE INTERFACE ${READLINE_CFLAGS_OTHER})
  target_link_libraries(READLINE::READLINE INTERFACE ${READLINE_LIBRARIES})

endif()

```
