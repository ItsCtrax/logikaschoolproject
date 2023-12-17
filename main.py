from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget, QPushButton, QTextEdit,
                             QLabel, QLineEdit, QListWidget,
                             QVBoxLayout, QHBoxLayout, QInputDialog)

app = QApplication([])
img_editor = QWidget()
img_editor.setWindowTitle('Easy editor')
img_editor.resize(600,600)

btn_folder = QPushButton('Папка')
list_picture = QListWidget()

picture = QLabel('Картинка')

btn_left = QPushButton('Вліво')
btn_right = QPushButton('Вправо')
btn_mirror = QPushButton('Дзеркало')
btn_sharpness = QPushButton('Різскіть')
btn_hb = QPushButton('Ч/Б')

layout_easy = QVBoxLayout()
col1 = QVBoxLayout()
col1.addWidget(btn_folder)
col1.addWidget(picture)

col2 = QHBoxLayout()
col2.addWidget(btn_left)
col2.addWidget(btn_right)
col2.addWidget(btn_mirror)
col2.addWidget(btn_sharpness)
col2.addWidget(btn_hb)

layout_easy.addLayout(col1)
layout_easy.addLayout(col2)
img_editor.setLayout(layout_easy)

img_editor.show()
app.exec_()