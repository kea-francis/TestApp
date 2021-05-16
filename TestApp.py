import kivy
from kivy.uix.textinput import TextInput
from kivy.app import App 
# The Label widget is for rendering text.  
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
     
# to change the kivy default settings we use this module config 
from kivy.config import Config

from kivy.uix.pagelayout import PageLayout
  
# 0 being off 1 being on as in true / false 
# you can use 0 or 1 && True or False 
Config.set('graphics', 'resizable', True)

# Create the App class
class TutorialApp(App):
     def build(self):
  
        b = BoxLayout(orientation ='horizontal')
        bv = BoxLayout(orientation ='vertical')
  
        # Adding the text input
        t = TextInput(font_size = 15,
                      size_hint_y = None,
                      height = 50)
        t2 = TextInput(font_size = 15, size_hint_y = None, height = 50)
        t3 = TextInput(font_size = 15, size_hint_y = None, height = 50)
          
        #f = FloatLayout()
        # Adding Button and styling
        sb = Button(text ="SAVE", 
                   font_size ="15sp", 
                   background_color =(.67, 1, .33, 1), 
                   size_hint_y = None,
                   color =(1, 1, 1, 1) )
        ssb = Button(text ="SAVE & SUBMIT", 
                   font_size ="15sp", 
                   background_color =(.67, 1, .33, 1), 
                   size_hint_y = None,
                   color =(1, 1, 1, 1) )
        
        # By this you are able to move the Text on the screen to anywhere you want
        s = Scatter()
        
        title = Label(text ="Test", font_size = 40, size_hint_y = None, height = 45)
        l = Label(text ="Entry 1:", font_size = 20, size_hint_y = None, height = 45)
        l2 = Label(text ="Entry 2:", font_size = 20, size_hint_y = None, height = 45)
        l3 = Label(text ="Entry 3:", font_size = 20, size_hint_y = None, height = 45)
  
        #f.add_widget(s)
        #s.add_widget(l)

       # textinput = TextInput(text='Hello world', multiline=True)
       # textinput.bind(on_text_validate=on_enter)
        bv.add_widget(title)
        b.add_widget(l)
        bv.add_widget(t)
        b.add_widget(l2)
        bv.add_widget(t2)
        b.add_widget(l3)
        bv.add_widget(t3)
        bv.add_widget(ssb)
        b.add_widget(sb)
        
  
        # Binding it with the label
        #t.bind(text = l.setter('text'))

          
        return bv
        return b


def on_enter(instance, value):
   print('User pressed enter in', instance)

textinput = TextInput(text='Hello world', multiline=False)
textinput.bind(on_text_validate=on_enter)

def on_text(instance, value):
    print('The widget', instance, 'have:', value)

textinput = TextInput(focus=True)
textinput.bind(text=on_text)

def on_focus(instance, value):
    if value:
        print('User focused', instance)
    else:
        print('User defocused', instance)

textinput = TextInput()
textinput.bind(focus=on_focus)

# Run the App
if __name__ == "__main__":
    TutorialApp().run()
