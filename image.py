from PIL import Image

def pixel_info(filepath):
    w,h=Image.open(filepath).size
    return w*h,w,h

def color_info(filepath):
    from collections import defaultdict
    image = Image.open(filepath)
    by_color=defaultdict(int)
    for pixel in image.getdata():
        by_color[pixel]+=1
    return by_color
def get_pixel_color(filepath,x,y):
    image=Image.open(filepath)
    pixel=Image.load()
    return pixel[x,y],pixel.show()
print(f'{pixel_info("D:/498c4e14ef1eda6c89180b9000971a62.jpg")[0]} total pixel')
print(f'{pixel_info("D:/498c4e14ef1eda6c89180b9000971a62.jpg")[1]} width')
print(f'{pixel_info("D:/498c4e14ef1eda6c89180b9000971a62.jpg")[2]} height')
print(color_info("D:/498c4e14ef1eda6c89180b9000971a62.jpg"))
print(f'color of specified pixel is {grt_pixel_color("ss.png",22,22)}')



    
