# flex lexer file
## `lib/cli/src/syntax.lex`

```lex
%{
    #include "cli.hpp"
%}

%option noyywrap yylineno

%%
"//".*                                      // line comment
"/*"([^*]|"*"[^/])*"*/"                     // block comment

[A-Za-z_][A-Za-z0-9_]*  { yylval.s = new std::string(yytext); return ID; }
[0-9]+                  { yylval.n = atoi(yytext);           return INT; }

[ \t\r\n]+                                  // drop whitespaces
.                       { yyerror(""); }    // any undetected char
```
