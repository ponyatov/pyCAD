from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont

import syntax

class Highlighter(syntax.Highlighter):
    def __init__(self, document):
        super().__init__(document)

        syntax.Number(self.rules)
        syntax.LineComment(self.rules, r'#[^\r\n]*')
        syntax.Keyword(self.rules, [
            'and', 'as', 'assert', 'break', 'class', 'continue',
            'def', 'del', 'elif', 'else', 'except', 'False',
            'finally', 'for', 'from', 'global', 'if', 'import',
            'in', 'is', 'lambda', 'None', 'nonlocal', 'not',
            'or', 'pass', 'raise', 'return', 'True', 'try',
            'while', 'with', 'yield'
        ])
        syntax.StdLib(self.rules, [
            '__name__', 'self', '__init__', 'os', 'sys', 'print'
        ])

        syntax.String(self.rules)
