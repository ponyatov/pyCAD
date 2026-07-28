# syntax parser

## lib/cli/inc/syntax.hpp

```cpp
/// @defgroup syntax syntax
/// @ingroup cli
#pragma once

#include <string>

#include "posix.hpp"

extern int yylex();                ///< syntax lexer
extern char* yytext;               ///< lexeme value
extern char* yyfile;               ///< current script file name
extern FILE* yyin;                 ///< current script file handler
extern int yylineno;               ///< current line no
extern int yyparse();              ///< syntax parser
extern void yyerror(const char*);  ///< syntax error callback

#include "syntax.yacc.hpp"         /* tokens definitions from .yacc */
```

## lib/cli/src/syntax.cpp

```cpp
#include "syntax.hpp"

char* yyfile = nullptr;

__attribute__((weak)) FILE* yyin = nullptr;

__attribute__((weak)) void yyerror(const char* msg) {
    fprintf(stderr, "\n\n%s:%i %s [%s]\n\n", yyfile, yylineno, msg, yytext);
    abort();
}
```

## syntax.[[lex]]
## syntax.[[yacc]]
## [[ini]]
