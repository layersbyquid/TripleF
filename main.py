from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.config import Config
from kivymd.app import App
from kivy.core.text import LabelBase
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivymd.uix.carousel import MDCarousel
import cProfile
import csv
import os

Builder.load_file('bg.kv')

Window.size = (640, 1136)
Window.clearcolor = (37/255, 41/255, 38/255, 1)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class GetStarted(Screen):
    pass

class LogIn(Screen):
    pass

class LogIn2(Screen):
    pass

class SignUp(Screen):
    pass
    
#     def build(self):
#         return Builder.load_file('bg.kv')

#     def send_data(self, email, password):
#         from firebase import firebase


#         # Initialize Firebase
#         firebase = firebase.FirebaseApplication('https://triplef-5c975-default-rtdb.firebaseio.com/', None)

#         # Importing Data
#         data = {
#             'Email' : email,
#             'Password' : password
#         }

#         # Post Data
#         # Database Names/Table Name
#         firebase.post('https://triplef-5c975-default-rtdb.firebaseio.com/Users', data)

class Home(Screen):
    pass

class Workouts(Screen):
    pass

class MealPrep(Screen):
    pass

class MealPrep2(Screen):
    pass

class MealPrep3(Screen):
    pass

class MealPrep4(Screen):
    pass

class MealPrep5(Screen):
    pass

class Settings(Screen):
    pass

class Profile(Screen):
    pass

class Cardio(Screen):
    timer_label = ObjectProperty()

    def __init__(self, **kwargs):
        super(Cardio, self).__init__(**kwargs)
        self.timer_running = False
        self.seconds_elapsed = 0

        self.timer_label = Label(text='00:00:00', font_size=100, size_hint=(None, None), font_name="Boogaloo-Regular")
        self.timer_label.pos_hint = {'center_x': 0.5, 'center_y': 0.75}

        self.rect = Rectangle(pos=self.timer_label.pos, size=self.timer_label.size)
        with self.canvas.before:
            Color(0/255, 255/255, 255/255, 0)
            self.rect = Rectangle(pos=self.timer_label.pos, size=self.timer_label.size)

        start_button = Button(text='Start', on_press=self.start_timer, background_color=(0/255, 255/255, 255/255, 1), size_hint=(.8, None), pos_hint={'center_x': 0.5, 'center_y' : 0.2}, font_size=50, font_name="Boogaloo-Regular")
        pause_button = Button(text='Pause', on_press=self.pause_timer, background_color=(0/255, 255/255, 255/255, 1), size_hint=(.8, None), pos_hint={'center_x': 0.5, 'center_y' : 0.2}, font_size=50, font_name="Boogaloo-Regular")
        reset_button = Button(text='Reset', on_press=self.reset_timer, background_color=(0/255, 255/255, 255/255, 1), size_hint=(.8, None), pos_hint={'center_x': 0.5, 'center_y' : 0.2}, font_size=50, font_name="Boogaloo-Regular")

        button_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=150)
        button_layout.add_widget(start_button)
        button_layout.add_widget(pause_button)
        button_layout.add_widget(reset_button)
        button_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.4}

        self.add_widget(self.timer_label)
        self.add_widget(button_layout)

    def start_timer(self, instance):
        if not self.timer_running:
            Clock.schedule_interval(self.update_timer, 0.01)
            self.timer_running = True

    def pause_timer(self, instance):
        if self.timer_running:
            Clock.unschedule(self.update_timer)
            self.timer_running = False

    def reset_timer(self, instance):
        self.pause_timer(instance)
        self.seconds_elapsed = 0
        self.update_timer(0)

    def update_timer(self, dt):
        self.seconds_elapsed += dt
        minutes = int(self.seconds_elapsed // 60)
        seconds = int(self.seconds_elapsed % 60)
        milliseconds = int((self.seconds_elapsed * 100) % 100)

        self.timer_label.text = f'{minutes:02d}:{seconds:02d}:{milliseconds:02d}'
        
        self.rect.pos = self.timer_label.pos
        self.rect.size = self.timer_label.size
        
class UpperBody(Screen):
    pass

class Back(Screen):
    pass

class Chest(Screen):
    pass

class Arms(Screen):
    pass

class LowerBody(Screen):
    pass

class Legs(Screen):
    pass

class Glutes(Screen):
    pass

class Core(Screen):
    pass

class FullBody(Screen):
    pass

class DailyGoal(Screen):
    calories_goal = NumericProperty(0)
    calories_input_disabled = BooleanProperty(False)

    def on_calories_goal(self, instance, value):
        pass

    def set_calories_goal(self, value):
        self.calories_goal = value
        self.calories_input_disabled = True

    def enable_calories_input(self):
        self.ids.calories_input.disabled = False
        self.ids.calories_input.text = ""

    def disable_calories_input(self):
        self.ids.calories_input.disabled = True

    def on_submit(self):
        self.disable_calories_input()
        
    def enable_input(self):
        self.enable_calories_input()



class NumericTextInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if not substring.isdigit():
            return
        return super(NumericTextInput, self).insert_text(substring, from_undo=from_undo)
    
    

class WindowManager(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        
        self.title = 'Triple F'
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(GetStarted(name='gs'))
        sm.add_widget(LogIn(name='li'))
        sm.add_widget(LogIn2(name='li2'))
        sm.add_widget(SignUp(name='su'))
        sm.add_widget(Home(name='home'))
        sm.add_widget(Workouts(name='wo'))
        sm.add_widget(MealPrep(name='mp'))
        sm.add_widget(MealPrep2(name='mp2'))
        sm.add_widget(MealPrep3(name='mp3'))
        sm.add_widget(MealPrep4(name='mp4'))
        sm.add_widget(MealPrep5(name='mp5'))
        sm.add_widget(Settings(name='s'))
        sm.add_widget(Profile(name='p'))
        sm.add_widget(Cardio(name='ca'))
        sm.add_widget(UpperBody(name='ub'))
        sm.add_widget(Back(name='b'))
        sm.add_widget(Chest(name='ch'))
        sm.add_widget(Arms(name='a'))
        sm.add_widget(LowerBody(name='lb'))
        sm.add_widget(Legs(name='l'))
        sm.add_widget(Glutes(name='g'))
        sm.add_widget(Core(name='c'))
        sm.add_widget(FullBody(name='fb'))
        sm.add_widget(DailyGoal(name='dg'))

        return sm
    

if __name__ == '__main__':
    MyApp().run()