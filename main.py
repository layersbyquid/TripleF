from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.uix.textinput import TextInput
import csv
import os

Window.size = (640, 1136)
Window.clearcolor = (147/255, 190/255, 230/255, 1)

class GetStarted(Screen):
    pass

class LogIn(Screen):
    pass

class LogIn2(Screen):
    pass

class SignUp(Screen):
    email = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def on_signup_button_press(self):
        # Get user input
        email = self.email.text
        username = self.username.text
        password = self.password.text

        # Update login.csv file
        csv_file = 'login.csv'
        fieldnames = ['Email', 'Username', 'Password']

        # Check if the file exists, and write header if not
        file_exists = os.path.isfile(csv_file)
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({'Email': email, 'Username': username, 'Password': password})

        # Navigate to Home screen
        self.manager.current = 'home'

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
        sm = ScreenManager(transition=SwapTransition())
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