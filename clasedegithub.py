from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton

def show_win():
    victory_win = QMessageBox()
    victory_win.setText('¡Correcto! Ganaste un scooter gyro')
    victory_win.exec_()

def show_lose():
    lose_win = QMessageBox()
    lose_win.setText('No, fue en el 2015 Ganaste un poster de la empresa')
    lose_win.exec_()

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Competicion de Crazy People')
question = QLabel('¿En que año el canal recibio su "boton de reproduccion dorado" de Youtube')
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
my_win.setLayout(layout_main)

btn_answer3.clicked.connect(show_win)
btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)






my_win.setLayout(layout_main)
my_win.show()
app.exec_()