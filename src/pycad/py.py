
import syntax

class PyLexer(syntax.Lexer):
    def __init__(self):
        self.tokens += ['QT']
        super().__init__()

    t_COMMENT = r'\#[^\r\n]*'
    t_KEYWORD = r'\b(and|as|assert|break|class|continue|def|del|elif|else|except|False|finally|for|from|global|if|import|in|is|lambda|None|nonlocal|not|or|pass|raise|return|True|try|while|with|yield)\b'
    t_STRING = r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
    t_QT = r'PyQt\d|Qt?[A-Z][A-Za-z]*'
    t_STDLIB = r'\b(os|sys|print|__name__|code|traceback)\b'

from PyQt6.QtGui import *

class QT(syntax.TOKEN):
    color = QColor("#D659C6")

class Highlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.lexer = PyLexer()

    def highlightBlock(self, text):
        self.lexer.lexer.input(text)
        while True:
            tok = self.lexer.lexer.token()
            if not tok:
                break

            start = tok.lexpos
            length = len(tok.value)

            match tok.type:
                case 'KEYWORD':
                    self.setFormat(start, length, syntax.KEYWORD())
                case 'NUMBER':
                    self.setFormat(start, length, syntax.NUMBER())
                case 'STRING':
                    self.setFormat(start, length, syntax.STRING())
                case 'COMMENT':
                    self.setFormat(start, length, syntax.COMMENT())
                case 'OPERATOR':
                    self.setFormat(start, length, syntax.OPERATOR())
                case 'PAREN':
                    self.setFormat(start, length, syntax.PAREN())
                case 'IDENTIFIER':
                    self.setFormat(start, length, syntax.IDENTIFIER())
                case 'STDLIB':
                    self.setFormat(start, length, syntax.STDLIB())
                case 'QT':
                    self.setFormat(start, length, QT())
                case _:
                    self.setFormat(start, length, syntax.TOKEN())
