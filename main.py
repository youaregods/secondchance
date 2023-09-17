from kivy.app import App
from kivy.uix.label import Label
class RecordApp(App):
    def build(self):
        return Label(text='Hello record world')
if __name__ == '__main__':
    RecordApp().run()

