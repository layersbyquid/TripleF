from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.textinput import TextInput
Window.size = (720, 1280)

class GetStarted(Screen):
    pass

class LogIn(Screen):
    pass

class LogIn2(Screen):
    pass

class SignUp(Screen):
    pass

class Home(Screen):
    pass

class Workouts(Screen):
    pass

class Settings(Screen):
    pass

class WindowManager(ScreenManager):
    pass

Builder.load_file('bg.kv')

class MyApp(App):
    def build(self):
        self.title = 'Triple F'
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(GetStarted(name='gs'))
        sm.add_widget(LogIn(name='li'))
        sm.add_widget(LogIn2(name='li2'))
        sm.add_widget(SignUp(name='su'))
        sm.add_widget(Home(name='home'))
        sm.add_widget(Workouts(name='wo'))
        sm.add_widget(Settings(name='s'))

        return sm
    
    
if __name__ == '__main__':
    MyApp().run()