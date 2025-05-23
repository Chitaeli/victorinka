#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
    )
def show_win():
    victory_window = QMessageBox()
    victory_window.setText('УРА ПАБЕДА')
    victory_window.exec()

def show_lose():
    victory_window = QMessageBox()
    victory_window.setText('На вас повесили несколько кредитов')
    victory_window.exec()


#создание приложения и главного окна
app = QApplication([])
window = QWidget()
window.setWindowTitle('Викторина')
window.resize(800,400)

text = QLabel('Кто является главным злодеем в МГЧД?')
r_btn1 = QRadioButton('Сергей Разумовский')
r_btn1.clicked.connect(show_win)
r_btn2 = QRadioButton('Игорь Гром')
r_btn2.clicked.connect(show_lose)
r_btn3 = QRadioButton('Кирилл Гречкин')
r_btn3.clicked.connect(show_lose)
r_btn4 = QRadioButton('Олег Волков')
r_btn4.clicked.connect(show_lose)
#создание виджетов главного окна
v_line = QVBoxLayout() #глав
h_line1 = QHBoxLayout() #второсепенные
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
#расположение виджетов по лэйаутам
h_line1.addWidget(text, alignment= Qt.AlignCenter)
h_line2.addWidget(r_btn1, alignment= Qt.AlignCenter)
h_line2.addWidget(r_btn2, alignment= Qt.AlignCenter)
h_line3.addWidget(r_btn3, alignment= Qt.AlignCenter)
h_line3.addWidget(r_btn4, alignment= Qt.AlignCenter)

#обработка нажатий на переключатели
 
#отображение окна приложения 
v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)
window.setLayout(v_line)
window.show()
app.exec()