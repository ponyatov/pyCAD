# main()

- `os/linux/inc/main.hpp`
	```cpp
	/// @defgroup main main
	/// @ingroup lib
	/// @{
	#pragma once

	#include "posix.hpp"
	#include "syntax.hpp"

	/// @brief @ref posix entry point
	/// @param argc arguments count
	/// @param argv arguments vector; `argv[0]` program binary path
	/// @returns exit with error code
	extern int main(int argc, char *argv[]);

	/// @brief log single command-line argument
	/// @param argc argument index
	/// @param argv argument string value
	extern void arg(int argc, char *argv  );
	/// @}
	```
- `os/linux/src/main.cpp`
```cpp
#include "main.hpp"

__attribute__((weak)) int main(int argc, char *argv[]) {
    arg(0, argv[0]);
    for (int i = 1; i < argc; i++) {
        arg(i, argv[i]);
        yyfile = argv[i];
        assert(yyin = fopen(yyfile, "r"));
        yyparse();
        fclose(yyin);
        yyfile = nullptr;
    }
    return vm();
}

__attribute__((weak)) void arg(int argc, char *argv) {
    fprintf(stderr, "%i: %s\n", argc, argv);
}
```

- [[cpp/syntax|syntax]]
- [[cli]]
- [[vm]]
