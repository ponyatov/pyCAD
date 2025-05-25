#!/usr/bin/env python3
# pyCAD - 2D CAD for Electronics Design
# Copyright (C) 2023-2024 Dmitry Ponyatov <dponyatov@gmail.com>
# MIT License

APP = 'pyCAD'
ABOUT = '2D CAD for Electronics Design'
AUTHOR = 'Dmitry Ponyatov'
EMAIL = 'dponyatov@gmail.com'
LICENSE = 'MIT'

import os
import sys


from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QStandardPaths, QSettings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = QSettings(APP, "Theme")
        self.style = self.settings.value("style", "Fusion")
        self.palette = self.settings.value("palette", "darker")

class pyCAD(QApplication):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.win = MainWindow()
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
        sys.exit(self.app.exec())

if __name__ == '__main__':
    print(sys.argv)
    pyCAD().run()
