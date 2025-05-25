from PyQt6.QtGui import QSyntaxHighlighter

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

from colors import *

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
