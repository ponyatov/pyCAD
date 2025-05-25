#!/usr/bin/env python3
# pyCAD - 2D CAD for Electronics Design
# Copyright (C) 2023-2024 Dmitry Ponyatov <dponyatov@gmail.com>
# MIT License

import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
# from .ui.main_window import MainWindow
# from .core.document import Document

class pyCAD(QApplication):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.win = QMainWindow()

    def run(self):
        self.win.show()
        sys.exit(self.app.exec())

if __name__ == '__main__':
    print(sys.argv)
    pyCAD().run()
