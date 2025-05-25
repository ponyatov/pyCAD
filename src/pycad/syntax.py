from PyQt6.QtGui import *
from PyQt6.QtCore import QRegularExpression

import ply.lex as lex

class Lexer:
    tokens = [
        'KEYWORD',
        'NUMBER',
        'STRING',
        'COMMENT',
        'OPERATOR',
        'PAREN',
        'STDLIB',
        'IDENTIFIER'
    ]

    t_ignore = ' \t'

    t_NUMBER = r'\b[+\-]?\d+(\.\d+)?\b'
    t_OPERATOR = r'[+\-*/%=&|<>!^~]'
    t_PAREN = r'[\(\)\[\]\{\}]'

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = lex.lex(module=self)

class FORMAT(QTextCharFormat):
    color = QColor("#D4D4D4")
    weight = QFont.Weight.Normal
    italic = False

    def __init__(self):
        super().__init__()
        self.setForeground(self.color)
        self.setFontWeight(self.weight)
        self.setFontItalic(self.italic)

class KEYWORD(FORMAT):
    color = QColor("#569CD6")
class NUMBER(FORMAT):
    color = QColor("#B5CEA8")
class STRING(FORMAT):
    color = QColor("#CE9178")
class COMMENT(FORMAT):
    color = QColor("#6A9955")
    italic = True
class OPERATOR(FORMAT):
    color = QColor("#D4D44D")
class PAREN(FORMAT):
    color = QColor("#4DD4D4")
class IDENTIFIER(FORMAT):
    color = QColor("#569CD6")
class STDLIB(FORMAT):
    color = QColor("#D69C56")


class Highlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

    def highlightBlock(self, text):
        self.lexer.lexer.input(text)
        while True:
            tok = self.lexer.lexer.token()
            if not tok: break

            start = tok.lexpos
            length = len(tok.value)

            format = self.format(tok.type) or FORMAT()
            self.setFormat(start, length, format())

    def format(self, tok_type):
        match tok_type:
            case 'KEYWORD': return KEYWORD
            case 'NUMBER': return NUMBER
            case 'STRING': return STRING
            case 'COMMENT': return COMMENT
            case 'OPERATOR': return OPERATOR
            case 'PAREN': return PAREN
            case 'IDENTIFIER': return IDENTIFIER
            case 'STDLIB': return STDLIB
            case _: return None
