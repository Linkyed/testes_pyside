from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt
from qdarktheme import load_stylesheet



class Window (QMainWindow):
    def __init__(self):
        super().__init__()
        base = QWidget()
        layout = QVBoxLayout()

        menu = self.menuBar()
        arquivo_menu = menu.addMenu('Arquivo')
        action = QAction('Print!')
        arquivo_menu.addAction(action)

        font = QFont()
        font.setPixelSize(50)
        font.setItalic(True)

        self.label = QLabel('0')
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        botao = QPushButton('Aumentar numero')
        botao.setFont(font)
        botao.clicked.connect(self.printTerminal)
        layout.addWidget(botao)

        base.setLayout(layout)
        self.setCentralWidget(base)
        self.setWindowTitle('Application')

    def printTerminal(self):
        numeroAtual = self.label.text()
        if numeroAtual.isnumeric() == True:
            numeroAtual = int(numeroAtual)
            numeroAtual += 1
        else:
            numeroAtual = 'Erro!'
        
        self.label.setText(str(numeroAtual))


app = QApplication()
app.setStyleSheet(load_stylesheet())
mainWindow = Window()
mainWindow.show()

app.exec()