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
            if not tok:
                break

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

#     def highlightBlock(self, text):
#         for pattern, fmt in self.rules:
#             expression = QRegularExpression(pattern)
#             match_iterator = expression.globalMatch(text)
#             while match_iterator.hasNext():
#                 found = match_iterator.next()
#                 self.setFormat(found.capturedStart(),
#                                found.capturedLength(), fmt)

# class AST(QTextCharFormat):
#     weight = QFont.Weight.Normal
#     color = QColor("#777777")
#     regex = None

#     def __init__(self, rules, regex=None):
#         super().__init__()
#         self.setFont(QFont('Monospace', 10))
#         self.setForeground(self.color)
#         self.setFontWeight(self.weight)
#         if regex: rules.append((regex, self))
#         if self.regex: rules.append((regex, self))

# class Number(AST):
#     color = QColor("#6A9955")
#     weight = QFont.Weight.ExtraBold
#     format = r'0x[0-9a-fA-F]+|\d+'
#     regex = r'0x[0-9a-fA-F]+|\d+'

# class Keyword(AST):
#     color = QColor("#569CD6")
#     weight = QFont.Weight.ExtraLight

#     def __init__(self, rules, keywords=[]):
#         super().__init__(rules)
#         for word in keywords:
#             rules.append((fr'\b{word}\b', self))

# class LineComment(AST):
#     color = QColor("#667733")

# class String(AST):
#     color = QColor('#CE9178')

#     def __init__(self, rules, keywords=[]):
#         super().__init__(rules)
#         rules.append((r'\".*?\"', self))
#         rules.append((r'\'.*?\'', self))

# class StdLib(AST):
#     color = QColor("#56D69C")

#     def __init__(self, rules, names=[]):
#         super().__init__(rules)
#         for name in names:
#             rules.append((fr'\b{name}\b', self))
