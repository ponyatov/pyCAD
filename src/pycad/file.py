from PyQt6.QtGui import QFileSystemModel, QBrush, QColor
from PyQt6.QtCore import Qt, QFileInfo

import colors

class ColoredFileModel(QFileSystemModel):

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """Override data method to apply coloring"""
        if role == Qt.ItemDataRole.ForegroundRole:
            file_info = QFileInfo(self.filePath(index))

            if file_info.isDir():
                return QBrush(QColor(colors.DIR.color))

            match file_info.suffix().lower():
                case _: return QBrush(QColor(colors.FORMAT.color))

        return super().data(index, role)
