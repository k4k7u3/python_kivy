from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from random import randint

Window.size = (300, 100)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "Моя первая программа"


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.label = Label(text='Моя программа\nВсе работает!')

    def btn_pressed(self, *args):
        self.label.color = (randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255, 1)
        Window.clearcolor = (randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255, 1)

    def build(self):
        box = BoxLayout()
        btn = Button(text="Нажми на меня")
        btn.bind(on_press=self.btn_pressed)
        box.add_widget(self.label)
        box.add_widget(btn)

        return box


if __name__ == "__main__":
    MyApp().run()


