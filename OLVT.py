import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('desFile.kv')

class MyGridLayout(Widget):
    
    name = ObjectProperty(None)
    rocket = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        rocket = self.rocket.text
        color = self.color.text

        print(f'Hello {name}, you like the {rocket} rocket in the color {color}')
        #self.add_widget(Label(text=f'Hello {name}, you like the {rocket} rocket in the color {color}'))

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()