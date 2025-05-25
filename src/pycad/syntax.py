from PyQt6.QtGui import *

class AST(QTextCharFormat):
    weight = QFont.Weight.Normal
    color = QColor("#777777")
    regex = None

    def __init__(self, rules, regex=None):
        super().__init__()
        self.setFont(QFont('Monospace', 10))
        self.setForeground(self.color)
        self.setFontWeight(self.weight)
        if regex: rules.append((regex, self))
        if self.regex: rules.append((regex, self))

class Number(AST):
    color = QColor("#6A9955")
    weight = QFont.Weight.ExtraBold
    format = r'0x[0-9a-fA-F]+|\d+'
    regex = r'0x[0-9a-fA-F]+|\d+'

class Keyword(AST):
    color = QColor("#569CD6")
    weight = QFont.Weight.ExtraLight

    def __init__(self, rules, keywords=[]):
        super().__init__(rules)
        for word in keywords:
            rules.append((fr'\b{word}\b', self))

class LineComment(AST):
    color = QColor("#444444")

class String(AST):
    pass
