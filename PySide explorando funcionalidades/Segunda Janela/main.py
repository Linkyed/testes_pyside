from PySide6.QtWidgets import QApplication
from janela_principal import janelaPrincipal
import sys


app = QApplication(sys.argv)

window = janelaPrincipal(app)
window.show()

app.exec()  