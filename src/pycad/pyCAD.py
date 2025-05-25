#!/usr/bin/env python3
# pyCAD - 2D CAD for Electronics Design
# Copyright (C) 2023-2024 Dmitry Ponyatov <dponyatov@gmail.com>
# MIT License

class Info:
    APP = 'pyCAD'
    ABOUT = '2D CAD for Electronics Design'
    AUTHOR = 'Dmitry Ponyatov'
    EMAIL = 'dponyatov@gmail.com'
    TGRAM = '@dponyatov'
    LICENSE = 'MIT'
    VERSION = '0.0.1'

import os
import sys


from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import QStandardPaths, QSettings, Qt
from PyQt6.QtGui import QPalette, QColor, QKeySequence, QAction, QIcon
from PyQt6.QtWidgets import *

class FileBrowser(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("File Browser", parent)
        self.setObjectName("FileBrowser")
        #
        self.tree = QTreeView()


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle(Info.APP); self.setWindowIcon(app.icon)
        self.settings = QSettings(Info.APP, "Theme")
        self._load_theme()
        self.layout = QHBoxLayout(); self.setLayout(self.layout)
        self.menubar = QMenuBar(); self.setMenuBar(self.menubar)
        self.toolbar = QToolBar("capyBar"); self.addToolBar(self.toolbar)
        self.menu()
        self.status()
        self.edit()
        self.file()

    def status(self):
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.statusbar.hello = QLabel(f"{Info.APP} {Info.VERSION}")
        self.statusbar.addPermanentWidget(self.statusbar.hello)

    def edit(self):
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

    def file(self):
        self.files = QDockWidget('Files', self)
        self.files.tree = QListWidget()
        self.files.tree.addItem('Item1')
        self.files.tree.addItem('Item2')
        self.files.tree.addItem('Item3')
        self.files.tree.addItem('Item4')
        self.files.setWidget(self.files.tree)
        self.files.setFloating(False)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.files)

    def menu(self):
        self.file()
        self.sch()
        self.cir()
        self.pcb()
        self.cable()
        self.mech()
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

    def cir(self):
        self.menubar.cir = QMenu('&Cir', self)
        self.menubar.addMenu(self.menubar.cir)
        self.menubar.cir.op = QAction('&OP', self)
        self.menubar.cir.addAction(self.menubar.cir.op)
        self.menubar.cir.tran = QAction('&TRAN', self)
        self.menubar.cir.addAction(self.menubar.cir.tran)
        self.menubar.cir.ac = QAction('&AC', self)
        self.menubar.cir.addAction(self.menubar.cir.ac)
        self.menubar.cir.dc = QAction('&DC', self)
        self.menubar.cir.addAction(self.menubar.cir.dc)

    def pcb(self):
        self.menubar.pcb = QMenu('&PCB', self)
        self.menubar.addMenu(self.menubar.pcb)

    def cable(self):
        self.menubar.cable = QMenu('C&able', self)
        self.menubar.addMenu(self.menubar.cable)

    def mech(self):
        self.menubar.mech = QMenu('Mechanic', self)
        self.menubar.addMenu(self.menubar.mech)

    def lib(self):
        self.menubar.lib = QMenu('&Lib', self)
        self.menubar.addMenu(self.menubar.lib)
        self.menubar.lib.sym = QAction('&Sym')
        self.menubar.lib.addAction(self.menubar.lib.sym)
        self.menubar.lib.model = QAction('&Model')
        self.menubar.lib.addAction(self.menubar.lib.model)
        self.menubar.lib.pin = QAction('&Pin')
        self.menubar.lib.addAction(self.menubar.lib.pin)
        self.menubar.lib.pad = QAction('&Pad')
        self.menubar.lib.addAction(self.menubar.lib.pad)
        self.menubar.lib.wire = QAction('&Wire')
        self.menubar.lib.addAction(self.menubar.lib.wire)
        self.menubar.lib.board = QAction('&Board')
        self.menubar.lib.addAction(self.menubar.lib.board)
        self.menubar.lib.board = QAction('&Board')
        self.menubar.lib.addAction(self.menubar.lib.board)
        self.menubar.lib.cable = QAction('C&able')
        self.menubar.lib.addAction(self.menubar.lib.cable)
        self.menubar.lib.case = QAction('&Case')
        self.menubar.lib.addAction(self.menubar.lib.case)

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
        QMessageBox.about(self, f"About {Info.APP}", f"""
{Info.APP} {Info.VERSION}
{Info.ABOUT}

(c) {Info.AUTHOR} <{Info.EMAIL}> MIT""")

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
        self.icon = QIcon('doc/logo.png')
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
