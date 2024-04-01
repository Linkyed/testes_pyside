from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar



class janelaPrincipal(QMainWindow):
    def __init__ (self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Testes com QMainWindow")

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("File")
        quitAction = fileMenu.addAction("Quit")
        quitAction.triggered.connect(self.quit)

        editMenu = menuBar.addMenu("Edit")
        editMenu.addAction("Copy")
        editMenu.addAction("Cut")
        editMenu.addAction("Paste")
        editMenu.addAction("Undo")
        editMenu.addAction("Redo")

        toolbar = QToolBar("Toolbar principal")
        toolbar.setIconSize(QSize(16,16))
        toolbar.addAction(quitAction)
        self.addToolBar(toolbar)

        action1 = QAction("Alguma ação", self)
        action1.setStatusTip("Mensagem de status para alguma ação")
        action1.triggered.connect(self.toolbarClick)
        toolbar.addAction(action1)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Aqui"))

        self.setStatusBar(QStatusBar(self))
    
    def quit(self):
        self.app.quit()

    def toolbarClick(self):
        self.statusBar().showMessage("StatusBar funcionando!", 3000)
