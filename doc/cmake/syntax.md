# cmake/syntax.cmake

```cmake
find_package(FLEX     REQUIRED)
find_package(BISON    REQUIRED)
find_package(RAGEL    REQUIRED)
find_package(READLINE REQUIRED)

file(GLOB_RECURSE X CONFIGURE_DEPENDS src/*.l* lib/**/*.l* )
file(GLOB_RECURSE Y CONFIGURE_DEPENDS src/*.y* lib/**/*.y* )
file(GLOB_RECURSE R CONFIGURE_DEPENDS src/*.r* lib/**/*.r* )

foreach(lex ${X})
    get_filename_component(name ${lex} NAME_WE)
    set(cpp "${CMAKE_CURRENT_BINARY_DIR}/${name}.lex.cpp")
    set(hpp "${CMAKE_CURRENT_BINARY_DIR}/${name}.lex.hpp")
    list(APPEND CP ${cpp})
    list(APPEND HP ${hpp})
    add_custom_command(
        OUTPUT  ${cpp} ${hpp}
        DEPENDS ${lex}
        COMMAND ${FLEX_EXECUTABLE} -o${cpp} --header-file=${hpp} ${lex}
    )
endforeach()

foreach(yacc ${Y})
    get_filename_component(name ${yacc} NAME_WE)
    set(cpp "${CMAKE_CURRENT_BINARY_DIR}/${name}.yacc.cpp")
    set(hpp "${CMAKE_CURRENT_BINARY_DIR}/${name}.yacc.hpp")
    list(APPEND CP ${cpp})
    list(APPEND HP ${hpp})
    add_custom_command(
        OUTPUT  ${cpp} ${hpp}
        DEPENDS ${yacc}
        COMMAND ${BISON_EXECUTABLE} -o${cpp} ${yacc}
    )
endforeach()

foreach(ragel ${R})
    get_filename_component(name ${ragel} NAME_WE)
    set(cpp "${CMAKE_CURRENT_BINARY_DIR}/${name}.ragel.cpp")
    set(hpp "${CMAKE_CURRENT_BINARY_DIR}/${name}.ragel.hpp")
    list(APPEND CP ${cpp})
    list(APPEND HP ${hpp})
    add_custom_command(
        OUTPUT  ${cpp} ${hpp}
        DEPENDS ${ragel}
        COMMAND ${RAGEL_EXECUTABLE} -C -G2 -o ${cpp} ${ragel}
    )
endforeach()
```

required:
- cmake/[[FindREADLINE]].cmake
- cmake/[[FindRAGEL]].cmake
