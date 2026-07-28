# cmake/FindRAGEL.cmake

```cmake
include(FindPackageHandleStandardArgs)

if(NOT RAGEL_EXECUTABLE)
find_program(RAGEL_EXECUTABLE ragel)
endif()

if(RAGEL_EXECUTABLE)
    execute_process(
            COMMAND "${RAGEL_EXECUTABLE}" -v
            OUTPUT_VARIABLE _version_output
            RESULT_VARIABLE _version_result
            OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    if(_version_result EQUAL 0)
        string(REGEX MATCH "[0-9]+\\.[0-9]+(\\.[0-9]+)*" RAGEL_VERSION "${_version_output}")
        set(RAGEL_FOUND TRUE)
        message("-- Found RAGEL: ${RAGEL_EXECUTABLE} (found version \"${RAGEL_VERSION}\")")
    endif()
endif()
```
