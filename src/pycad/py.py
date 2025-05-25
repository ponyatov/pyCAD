
import syntax

class PyLexer(syntax.Lexer):
    tokens = syntax.Lexer.tokens + ['QT']
    t_COMMENT = r'\#[^\r\n]*'
    t_KEYWORD = r'\b(and|as|assert|break|class|continue|def|del|elif|else|except|False|finally|for|from|global|if|import|in|is|lambda|None|nonlocal|not|or|pass|raise|return|True|try|while|with|yield)\b'
    t_STRING = r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
    t_QT = r'PyQt\d|Qt?[A-Z][A-Za-z]*'
    t_STDLIB = r'\b(os|sys|print|__name__|code|traceback)\b'

# from PyQt6.QtGui import *

class QT(syntax.FORMAT):
    color = "#D659C6"

class Highlighter(syntax.Highlighter):
    lexer = PyLexer()

    def format(self, tok_type):
        match tok_type:
            case 'QT': return QT
            case _: return super().format(tok_type)

    # case 'QT':
    #     self.setFormat(start, length, QT())
