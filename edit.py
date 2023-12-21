from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

class Image():
    def __init__(self,filename,listchanged):
        self.filename = filename
        self.listchanged = []
        self.original = None
    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Файл не знайдено!')

    def blur(self):
        picblur=self.original.filter(ImageFilter.BLUR)
        self.listchanged.append(picblur)
    def mirror(self):
        picmirror=self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.listchanged.append(picmirror)
    def bw(self):
        picbw=self.original.convert('L')
        self.listchanged.append(picbw)
    def left(self):
        picleft=self.original.transpose(Image.ROTATE_90)
        self.listchanged.append(picleft)
    def right(self):
        picright=self.original.transpose(Image.ROTATE_90)
        self.listchanged.append(picright)
    def contrast(self):
        piccontrast=ImageEnhance.Contrast(self.original)
        piccontrast=piccontrast.enhance(6.5)
        self.listchanged.append(piccontrast)