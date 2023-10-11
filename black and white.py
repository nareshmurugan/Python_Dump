from PIL import Image
i=Image.open("D:/camera/IMG_20200112_073254.jpg")
b=i.convert("L")
b.save('b.jpg')
b.show()


