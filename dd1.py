import dlib
def rec_to_bb(rect):
    x=rect.left()
    y=rect.top()
    w=rect.right()-x
    h=rect.bottom()-y
    return (x,y,w,h)
