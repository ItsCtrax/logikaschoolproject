from PyQt5.QtCore import Qt
import os
from PyQt5.QtWidgets import (QApplication,
                             QWidget, QPushButton, QTextEdit,
                             QFileDialog,
                             QLabel, QLineEdit, QListWidget,
                             QVBoxLayout, QHBoxLayout, QInputDialog)
from . import edit

app = QApplication([])
img_editor = QWidget()
img_editor.setWindowTitle('Easy editor')
img_editor.resize(700,500)

btn_folder = QPushButton('Папка')
list_picture = QListWidget()

picture = QLabel('Картинка')

btn_left = QPushButton('Вліво')
btn_right = QPushButton('Вправо')
btn_mirror = QPushButton('Дзеркало')
btn_sharpness = QPushButton('Різскіть')
btn_hb = QPushButton('Ч/Б')

layout_easy = QHBoxLayout()
col1 = QVBoxLayout()
col1.addWidget(btn_folder)
col1.addWidget(list_picture)

col2 = QVBoxLayout()
col2.addWidget(picture)

btn_tools = QHBoxLayout()
btn_tools.addWidget(btn_left)
btn_tools.addWidget(btn_right)
btn_tools.addWidget(btn_mirror)
btn_tools.addWidget(btn_sharpness)
btn_tools.addWidget(btn_hb)

col2.addLayout(btn_tools)

layout_easy.addLayout(col1, 20)
layout_easy.addLayout(col2, 80)
img_editor.setLayout(layout_easy)

img_editor.show()
workdir=''

def filter(files,ext):
    result=[]
    for f in files:
        for e in ext:
            if f.endswith(e):
                result.append(f)
    return result


def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def showFilesnameList():
    extension=['.jpg','.png','.jpeg','bmp']
    chooseWorkdir()
    fileslist = filter(os.listdir(workdir),extension)
    list_picture.clear()
    for file in fileslist:
        list_picture.addItem(file)


btn_folder.clicked.connect(showFilesnameList)




app.exec_()