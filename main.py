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
import cProfile
import csv
import os

Window.size = (640, 1136)
Window.clearcolor = (37/255, 41/255, 38/255, 1)


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

class MealPrep(Screen):
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

    def start_timer(self):
        if not self.timer_running:
            Clock.schedule_interval(self.update_timer, 1)
            self.timer_running = True

    def pause_timer(self):
        if self.timer_running:
            Clock.unschedule(self.update_timer)
            self.timer_running = False

    def reset_timer(self):
        self.pause_timer()
        self.seconds_elapsed = 0
        self.update_timer(0)

    def update_timer(self, dt=1):
        if dt == 0:
            minutes = seconds = 0
        else:
            self.seconds_elapsed += dt
            minutes = int(self.seconds_elapsed // 60)
            seconds = int(self.seconds_elapsed % 60)

        self.ids.timer_label.text = f'{minutes:02d}:{seconds:02d}'

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

class WindowManager(ScreenManager):
    pass

Builder.load_file('bg.kv')

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

        return sm
    

if __name__ == '__main__':
    MyApp().run()