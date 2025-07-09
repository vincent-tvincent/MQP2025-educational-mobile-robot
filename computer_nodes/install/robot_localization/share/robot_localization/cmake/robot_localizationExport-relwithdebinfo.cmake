#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "robot_localization::rl_lib" for configuration "RelWithDebInfo"
set_property(TARGET robot_localization::rl_lib APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(robot_localization::rl_lib PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELWITHDEBINFO "yaml-cpp::yaml-cpp"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/librl_lib.so"
  IMPORTED_SONAME_RELWITHDEBINFO "librl_lib.so"
  )

list(APPEND _cmake_import_check_targets robot_localization::rl_lib )
list(APPEND _cmake_import_check_files_for_robot_localization::rl_lib "${_IMPORT_PREFIX}/lib/librl_lib.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
