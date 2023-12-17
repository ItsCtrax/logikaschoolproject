from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open('image.png') as pic_original:
    print("Розмір картинки",pic_original.size)
    print("Формат картинки", pic_original.format)
    print("Тип картинки", pic_original.mode)
    #pic_original.show()

    #pic_gray = pic_original.convert('L')
    #pic_gray.save("m5f90.png")
    #pic_gray.show()

    #pic_blur = pic_original.filter(ImageFilter.BLUR)
    #pic_blur.save("blured.png")
    #pic_blur.show()

    #pic_mirror = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    #pic_mirror.save("mirror.png")
    #pic_mirror.show()

    #pic_left = pic_original.transpose(Image.ROTATE_90)
    #pic_left.save('left.png')
    #pic_left.show()

    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(6.5)
    pic_contrast.save("contrast.png")
    pic_contrast.show()

