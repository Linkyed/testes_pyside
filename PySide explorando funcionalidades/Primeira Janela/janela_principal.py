from PySide6.QtWidgets import QMainWindow, QPushButton, QSlider, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt

class JanelaPrincipal (QWidget):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle('Python Teste')

        #Botão 1
        self.button1 = QPushButton("Clique Aqui!")
        self.button1.setCheckable(True)
        self.button1.clicked.connect(self.callback_button)

        #Botão 2
        self.button2 = QPushButton("Não Clique Aqui!")
        self.button2.setCheckable(True)
        self.button2.clicked.connect(self.callback_button)

        #Slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        #Botão 3
        self.button3 = QPushButton("Imprimir valor do Slider")
        self.button3.clicked.connect(self.callback_button_slider)

        slider_button_layour = QHBoxLayout()
        slider_button_layour.addWidget(self.slider)
        slider_button_layour.addWidget(self.button3)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addLayout(slider_button_layour)

        self.setLayout(button_layout)

        #self.setCentralWidget(self)

    def callback_button(self, data):
        print("Clicado! Checked Status: ", data)

    def callback_button_slider(self):
        print("Valor atual do Slider: ", self.slider.value())
