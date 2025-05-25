from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt6.QtCore import QRegularExpression

class Highlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        keywords = ['as']
        self.rules = []

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))
        keyword_format.setFontWeight(QFont.Weight.Bold)
        for word in keywords:
            self.rules.append((fr'\b{word}\b', keyword_format))

        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#6A9955"))
        self.rules.append((r'\d+', number_format))

    def highlightBlock(self, text):
        for pattern, fmt in self.rules:
            expression = QRegularExpression(pattern)
            match_iterator = expression.globalMatch(text)
            while match_iterator.hasNext():
                found = match_iterator.next()
                self.setFormat(found.capturedStart(), found.capturedLength(), fmt)
