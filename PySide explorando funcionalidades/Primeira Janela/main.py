import sys
from PySide6.QtWidgets import QApplication, QPushButton
from  janela_principal import JanelaPrincipal

app = QApplication(sys.argv)

window = JanelaPrincipal()
window.show()

app.exec()