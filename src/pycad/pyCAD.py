#!/usr/bin/env python3
# pyCAD - 2D CAD for Electronics Design
# Copyright (C) 2023-2024 Dmitry Ponyatov <dponyatov@gmail.com>
# MIT License

APP = 'pyCAD'
ABOUT = '2D CAD for Electronics Design'
AUTHOR = 'Dmitry Ponyatov'
EMAIL = 'dponyatov@gmail.com'
TGRAM = '@dponyatov'
LICENSE = 'MIT'

import os
import sys


from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QStandardPaths, QSettings
from PyQt6.QtGui import QPalette, QColor, QKeySequence, QAction
from PyQt6.QtWidgets import QMenuBar, QMenu, QToolBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle(APP)
        self.app = app
        self.settings = QSettings(APP, "Theme")
        self._load_theme()
        self.menubar = QMenuBar()
        self.setMenuBar(self.menubar)
        self.toolbar = QToolBar("capyBar")
        self.addToolBar(self.toolbar)
        self.menu()

    def menu(self):
        self.file()
        self.sch()
        self.sym()
        self.pcb()
        self.lib()
        self.option()
        self.help()

    def file(self):
        self.menubar.file = QMenu('&File', self)
        self.menubar.file.setStatusTip("open/import/export")
        self.menubar.addMenu(self.menubar.file)
        self.menubar.file.exit = QAction("E&xit\tCtrl+Q", self)
        self.menubar.file.addAction(self.menubar.file.exit)
        self.menubar.file.exit.triggered.connect(self.close)

    def sch(self):
        self.menubar.sch = QMenu('&Sch', self)
        self.menubar.addMenu(self.menubar.sch)

    def sym(self):
        self.menubar.sym = QMenu('Sy&m', self)
        self.menubar.addMenu(self.menubar.sym)

    def pcb(self):
        self.menubar.pcb = QMenu('&PCB', self)
        self.menubar.addMenu(self.menubar.pcb)

    def lib(self):
        self.menubar.lib = QMenu('&Lib', self)
        self.menubar.addMenu(self.menubar.lib)

    def option(self):
        self.menubar.option = QMenu('&Option', self)
        self.menubar.addMenu(self.menubar.option)

    def help(self):
        self.menubar.help = QMenu('&Help', self)
        self.menubar.addMenu(self.menubar.help)
        self.menubar.help.about = QAction("&About\tF1", self)
        self.menubar.help.addAction(self.menubar.help.about)
        self.menubar.help.about.triggered.connect(self.about)

    def about(self):
        print(self)

    def _load_theme(self):
        self.style = self.settings.value("style", "Fusion")
        self.palette = self.settings.value("palette", "darker")
        # self.app.setStyle(self.style)
        # if self.palette == 'darker': self._apply_darker()

    def _apply_darker(self):
        # dark_palette = QPalette()
        # dark_palette.setColor(QPalette.ColorRole.Window,
        #                       QColor(0x22, 0x22, 0x22))
        self.app.setPalette(self.dark_palette)

class pyCAD(QApplication):
    def __init__(self):
        QApplication.__init__(self, sys.argv)
        self.win = MainWindow(self)
        self.setQuitOnLastWindowClosed(True)
        self.config()
        self.theme()

    def config(self):
        self.home = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.HomeLocation
            # QStandardPaths.StandardLocation.ConfigLocation)
            # QStandardPaths.StandardLocation.AppConfigLocation)
            # QStandardPaths.StandardLocation.GenericConfigLocation)
        )
        self.etc = f'{self.home}/pyCAD/etc'
        print(self.etc)

    def theme(self):
        # force qt6ct as platform theme
        os.environ["QT_QPA_PLATFORMTHEME"] = "qt6ct"
        os.environ["QT6CT_CONFIG"] = f"{self.etc}/qt6ct.conf"

    def run(self):
        self.win.show()
        sys.exit(self.exec())

if __name__ == '__main__':
    print(sys.argv)
    pyCAD().run()
