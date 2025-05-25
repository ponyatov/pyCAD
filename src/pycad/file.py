from PyQt6.QtGui import QFileSystemModel, QBrush, QColor
from PyQt6.QtCore import Qt, QFileInfo

import colors

import re

class RegexMatch(str):
    def __eq__(self, pattern):
        return bool(re.search(pattern, self))

class ColoredFileModel(QFileSystemModel):

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):

        if role == Qt.ItemDataRole.ForegroundRole:
            file_info = QFileInfo(self.filePath(index))

            if file_info.isDir():
                return QBrush(QColor(colors.DIR.color))

            def filename2color(file_info):
                match RegexMatch(file_info.fileName()):
                    case r'LICENSE|xxx': return colors.TXT
                    case r'Makefile': return colors.MK
                    case r'CMake.+': return colors.CMAKE
                match file_info.suffix().lower():
                    case 'lex': return colors.LEX
                    case 'yacc': return colors.LEX
                    case 'c': return colors.CPP
                    case 'cpp': return colors.CPP
                    case 'py': return colors.PY
                    case 'md': return colors.MD
                    case 'txt': return colors.TXT
                    case 'mk': return colors.MK
                    case 'cmake': return colors.CMAKE
                return colors.FORMAT

            return QBrush(QColor(filename2color(file_info).color))

        return super().data(index, role)
