from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt6.QtCore import QRegularExpression

import syntax

class Highlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

        self.rules = []

        syntax.LineComment(self.rules,r'#[^\r\n]*')
        syntax.Keyword(self.rules,[
            'and', 'as', 'assert', 'break', 'class', 'continue',
            'def', 'del', 'elif', 'else', 'except', 'False',
            'finally', 'for', 'from', 'global', 'if', 'import',
            'in', 'is', 'lambda', 'None', 'nonlocal', 'not',
            'or', 'pass', 'raise', 'return', 'True', 'try',
            'while', 'with', 'yield'
        ])

        syntax.Number(self.rules)
        syntax.String(self.rules)

    def highlightBlock(self, text):
        for pattern, fmt in self.rules:
            expression = QRegularExpression(pattern)
            match_iterator = expression.globalMatch(text)
            while match_iterator.hasNext():
                found = match_iterator.next()
                self.setFormat(found.capturedStart(),
                               found.capturedLength(), fmt)
