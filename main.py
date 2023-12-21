from PyQt5.QtCore import Qt
from PIL import Image
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget, QPushButton, QTextEdit,
                             QFileDialog,
                             QLabel, QLineEdit, QListWidget,
                             QVBoxLayout, QHBoxLayout, QInputDialog)

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

class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.dir = None
        self.image = None
        self.save_dir = 'modifed/'
    def loadImage(self,dir,filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def saveImage(self):
        path = os.path.join(os.getcwd(),self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path,self.filename)
        self.image.save(image_path)
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(os.getcwd(),self.save_dir,self.filename)
        self.saveImage()

    def showImage(self, path):
        picture.hide()
        pixmap = QPixmap(path)
        w,h = picture.width(), picture.height()
        pixmap = pixmap.scaled(w , h, Qt.KeepAspectRatio)
        picture.setPixmap(pixmap)
        picture.show()

def showChosenImage():
    if list_picture.curentRow()>=0:
        filename = list_picture.currentItem().text()
        workimage.loadImage(workdir,filename)
        image_path = os.path.join(workimage.dir,workimage.filename)
        workimage.showImage(image_path)

workimage = ImageProcessor()
list_picture.currentRowChanged.connect(showChosenImage)
btn_hb.clicked.connect(workimage.do_bw)
btn_folder.clicked.connect(showFilesnameList)
app.exec_()