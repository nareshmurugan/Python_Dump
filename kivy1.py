from kivy.app import App
from kivy.uix.label import Label
class mainApp(App):
    def build(self):
        label=Label(text='Hello from Kivy')

        return label
if __name__=='__main__':
    app=mainApp()
    app.run()
