from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
class MyRelativeLayout(RelativeLayout):
	pass
class DrawingWindow(App):
	def build(self):
		return MyRelativeLayout()
    canvas:
        Color:
            rgb:1,0,0
        Rectangle:
            pos:400,400
            size:180,180
        Color:
            rgb:0,1,0

        Ellipse:
            angle_start:100
            angle_end:400
            pos:300,300
            size:130,130
        Color:
            rgb:0,0,1
        
        Ellipse:
            segments:3
            pos:210,110
            size:140,140

        Triangle:
            points:310,110,340,190,380,130

        Line:
            points:10,30,90,90,10,10,60

            
                


if __name__ =="__main__":
	window=DrawingWindow()
	window.run()
