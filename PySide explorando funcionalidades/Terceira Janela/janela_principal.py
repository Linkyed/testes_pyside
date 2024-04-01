from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QVBoxLayout, QWidget, QMessageBox



class janelaPrincipal(QWidget):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Testes com QMessageBox")

        buttonHard = QPushButton('Hard')
        buttonHard.clicked.connect(self.hardClicked)
        

        buttonCritical = QPushButton('Critical')
        buttonCritical.clicked.connect(self.criticalClicked)

        buttonQuestion = QPushButton('Question')
        buttonQuestion.clicked.connect(self.questionClicked)

        buttonInformation = QPushButton('Information')
        buttonInformation.clicked.connect(self.informationClicked)

        buttonWarning = QPushButton('Warning')
        buttonWarning.clicked.connect(self.warningClicked)

        buttonAbout = QPushButton('About')
        buttonAbout.clicked.connect(self.aboutClicked)


        layout = QVBoxLayout()          
        layout.addWidget(buttonHard)
        layout.addWidget(buttonCritical)
        layout.addWidget(buttonQuestion)
        layout.addWidget(buttonInformation)
        layout.addWidget(buttonWarning)
        layout.addWidget(buttonAbout)
        self.setLayout(layout)

    def hardClicked(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle('Titulo da mensagem')
        message.setText('Alguma coisa aconteceu')
        message.setInformativeText('Quer fazer algo sobre isso?')
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        ret = message.exec()
        if ret == QMessageBox.Ok:
            print('Usuario escolheu Ok')
        else:
            print('Usuario escolheu Cancel')

    def criticalClicked(self):
        ret = QMessageBox.critical(self, "Titulo da mensagem", "Mensagem critica!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print('Usuario escolheu Ok')
        else:
            print("Usuario escolheu Cancel")

    def questionClicked(self):
        ret = QMessageBox.question(self, "Titulo da mensagem", "Mensagem de questão!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print('Usuario escolheu Ok')
        else:
            print("Usuario escolheu Cancel")

    def informationClicked(self):
        ret = QMessageBox.information(self, "Titulo da mensagem", "Mensagem de informação!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print('Usuario escolheu Ok')
        else:
            print("Usuario escolheu Cancel")

    def warningClicked(self):
        ret = QMessageBox.warning(self, "Titulo da mensagem", "Mensagem de aviso!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print('Usuario escolheu Ok')
        else:
            print("Usuario escolheu Cancel")

    def aboutClicked(self):
        ret = QMessageBox.about(self, "Titulo da mensagem", "Mensagem de sobre!")

        if ret == QMessageBox.Ok:
            print('Usuario escolheu Ok')
        else:
            print("Usuario escolheu Cancel")
    


