## apt for target's uses C/C++

- developer's HOST
    - append `apt.Debian`
        ```
        g++ cmake pkg-config clang-format
        gdb gdbserver valgrind doxygen
        ```
    - always add as we want to read at least .ini files
        ```
        flex bison ragel libreadline-dev
        ```    
- target's
