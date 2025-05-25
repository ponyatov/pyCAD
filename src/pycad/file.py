from PyQt6.QtGui import QFileSystemModel, QBrush, QColor
from PyQt6.QtCore import Qt, QFileInfo

import colors

class ColoredFileModel(QFileSystemModel):

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):

        if role == Qt.ItemDataRole.ForegroundRole:
            file_info = QFileInfo(self.filePath(index))

            if file_info.isDir():
                return QBrush(QColor(colors.DIR.color))

            def ext2color(file_info):
                match file_info.suffix().lower():
                    case 'py': return colors.PY
                    case _: return colors.FORMAT

            return QBrush(QColor(ext2color(file_info).color))

        return super().data(index, role)
