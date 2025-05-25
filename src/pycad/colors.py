from PyQt6.QtGui import QTextCharFormat, QColor, QFont

class FORMAT(QTextCharFormat):
    color = "#D4D4D4"
    weight = QFont.Weight.Normal
    italic = False

    def __init__(self):
        super().__init__()
        self.setForeground(QColor(self.color))
        self.setFontWeight(self.weight)
        self.setFontItalic(self.italic)

# syntax formats

class KEYWORD(FORMAT): color = "#569CD6"
class NUMBER(FORMAT): color = "#B5CEA8"
class STRING(FORMAT): color = "#CE9178"
class COMMENT(FORMAT): color = "#6A9955"; italic = True
class OPERATOR(FORMAT): color = "#D4D44D"
class PAREN(FORMAT): color = "#4DD4D4"
class IDENTIFIER(FORMAT): color = "#569CD6"
class STDLIB(FORMAT): color = "#D69C56"

# file list formats

class DIR(FORMAT): color = '#4EC9B0'
# CAD
class SCH(FORMAT): color = '#569CD6'
class PCB(FORMAT): color = '#9CDCFE'
# code
class PY(FORMAT): color = '#D7BA7D'
class JSON(FORMAT): color = '#CE9178'
# docs
class TXT(FORMAT): color = '#D4D4D4'
class MD(FORMAT): color = '#6A9955'
