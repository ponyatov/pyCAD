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
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import code, traceback


class JsonHighlighter(QSyntaxHighlighter): pass
class KiCadHighlighter(QSyntaxHighlighter): pass

import py, xxx

class myDock(QDockWidget):
    def __init__(self, title=None, parent=None):
        if title is None: title = os.getcwd()
        super().__init__(title, parent)
        self.setFloating(False)
        self.setStyleSheet("background-color: #111111;")
        self.font = parent.font; self.setFont(parent.font)

class FileTree(myDock):
    def __init__(self, title=None, parent=None):
        super().__init__(title, parent)
        self.setMinimumWidth(555)
        #
        self.container = QWidget(); self.setWidget(self.container)
        self.layout = QVBoxLayout()
        self.container.setLayout(self.layout)
        #
        self.tree = QTreeView(); self.layout.addWidget(self.tree)
        self.tree.setFont(self.font)
        # self.tree.setFont(QFont('Monospace', 10))
        # self.tree.setHeaderHidden(True)
        # self.tree.setAnimated(False)
        self.tree.setIndentation(15)
        self.tree.setSortingEnabled(True)
        # self.tree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        #
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QDir.currentPath()))
        #
        self.tree.clicked.connect(self.file_click)

    fileSelected = pyqtSignal(str)

    def file_click(self, index):
        path = self.model.filePath(index)
        if os.path.isfile(path): self.fileSelected.emit(path)

class CommandLine(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPlaceholderText(">>")
        self.setFont(QFont("Monospace", 10))
        self.setStyleSheet("background-color: #111111; color: #77FFFF;")
        #
        self.locals = parent.locals
        self.history = {}
        #
        self.completer = QCompleter(self.locals.keys())
        self.setCompleter(self.completer)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.completer.setCompletionMode(
            QCompleter.CompletionMode.PopupCompletion)

    def update(self, cmd):
        if cmd not in self.locals.keys():
            self.history[cmd] = None
        self.completer.model().setStringList(
            list(self.locals.keys()) + list(self.history.keys()))

class PythonShell(QDockWidget):
    def __init__(self, title="Python Console", parent=None, locals=None):
        super().__init__(title, parent)
        self.setFloating(False)
        self.locals = locals or {}
        self.ui()
        self.console = code.InteractiveConsole(locals)

    def eventFilter(self, obj, event):
        match event.type():
            case QEvent.Type.KeyPress:
                match event.key():
                    case Qt.Key.Key_Up:
                        self.history_nav(-1); return True
                    case Qt.Key.Key_Down:
                        self.history_nav(+1); return True
        return super().eventFilter(obj, event)

    def repl(self):
        cmd = self.input.text()
        if cmd:
            self.input.update(cmd)
            self.input.clear()
            self.write(f'>> {cmd}')

        # Redirect output
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = self
        sys.stderr = self

        try:
            more = self.console.push(cmd)
            prompt = "... " if more else ""
        except SystemExit:
            self.write("Cannot exit from embedded console\n")
            prompt = ""
        except:
            traceback.print_exc()
            prompt = ""
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

        self.write(prompt)

    def write(self, text):
        self.output.append(text)

    def ui(self):
        self.container = QWidget()
        self.setWidget(self.container)
        self.layout = QVBoxLayout()
        self.container.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumHeight(100)
        self.output()
        self.input()

    def input(self):
        self.input = CommandLine(self)
        self.layout.addWidget(self.input)
        self.input.returnPressed.connect(self.repl)
        self.input.setFocus()

    def output(self):
        self.output = QTextEdit(self.container)
        self.output.setFont(QFont("Monospace", 10))
        self.output.setStyleSheet(
            "background-color: #111111; color: lightgreen;")
        self.layout.addWidget(self.output)


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle(Info.APP); self.setWindowIcon(app.icon)
        self.showFullScreen()
        #
        self.font = QFont('Monospace', 10); self.setFont(self.font)
        self.settings = QSettings(Info.APP, "Theme")
        self._load_theme()
        #
        self.layout = QHBoxLayout(); self.setLayout(self.layout)
        self.menubar = QMenuBar(); self.setMenuBar(self.menubar)
        self.toolbar = QToolBar("capyBar"); self.addToolBar(self.toolbar)
        self.menu()
        self.status()
        self.init_editor()
        self.filetree()
        self.shell()

    def status(self):
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.statusbar.hello = QLabel(f"{Info.APP} {Info.VERSION}")
        self.statusbar.addPermanentWidget(self.statusbar.hello)

    def init_editor(self):
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setFont(QFont("Monospace", 10))
        self.view(sys.argv[0])

    def view(self, filename):
        assert os.path.isfile(filename)
        self.editor.setReadOnly(True)
        self.editor.setStyleSheet("background-color: #111111;")
        file = QFile(filename)
        file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
        stream = QTextStream(file)
        content = stream.readAll()
        file.close()
        self.editor.setPlainText(content)
        self.syntax(filename)

    def syntax(self, filename):
        if filename.endswith(('.py', '.pyw')):
            self.highlighter = py.Highlighter(self.editor.document())
        elif filename.endswith(('.json',)):
            self.highlighter = JsonHighlighter(self.editor.document())
        elif filename.endswith(('.kicad_sch', '.kicad_pcb')):
            self.highlighter = KiCadHighlighter(self.editor.document())
        elif filename.endswith(('/xxx',)):
            self.highlighter = xxx.Highlighter(self.editor.document())

    def edit(self, filename):
        self.view(filename)
        self.editor.setReadOnly(True)
        self.editor.cursor = self.editor.textCursor()
        self.editor.setTextCursor(self.editor.cursor)
        self.editor.cursor.movePosition(QTextCursor.MoveOperation.Start)
        self.editor.setFocus()

    def shell(self):
        def x(s):
            f = open('tmp/xxx', 'a')
            print(s, file=f)
            f.close()
        self.locals = {
            'x': x,
            'app': self.app,
            'win': self,
            'os': os,
            'sys': sys,
            'files': self.files
        }
        self.shell = PythonShell(os.getcwd(), self, self.locals)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.shell)

    def filetree(self):
        self.files = FileTree(None, self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.files)
        self.files.fileSelected.connect(self.view)

    def menu(self):
        self.menu_file()
        self.sch()
        self.cir()
        self.pcb()
        self.cable()
        self.mech()
        self.lib()
        self.option()
        self.help()

    def menu_file(self):
        self.menubar.file = QMenu('&File', self)
        self.menubar.file.setStatusTip("open/import/export")
        self.menubar.addMenu(self.menubar.file)
        self.menubar.file.exit = QAction("E&xit\tAlt+Q", self)
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
