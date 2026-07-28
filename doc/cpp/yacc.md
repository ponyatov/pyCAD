# bison/yacc
## `lib/cli/src/syntax.yacc`

```yacc
%{
    #include "cli.hpp"
    #include <string>
%}

%defines %union { int n; std::string* s ; }

%token <s> ID
%token <n> INT

%%
syntax:
```
