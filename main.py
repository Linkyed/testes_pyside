from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt

app = QApplication()
mainWindow = QMainWindow()
base = QWidget()
layout = QVBoxLayout()

menu = mainWindow.menuBar()
arquivo_menu = menu.addMenu('Arquivo')
action = QAction('Print!')
arquivo_menu.addAction(action)

font = QFont()
font.setPixelSize(50)
font.setItalic(True)

label = QLabel('Olá Mundo')
label.setFont(font)
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label)

botao = QPushButton('Aperte Aqui!')
botao.setFont(font)
layout.addWidget(botao)

base.setLayout(layout)

mainWindow.setCentralWidget(base)
mainWindow.setWindowTitle('Application')
mainWindow.show()

app.exec()