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
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
     
# to change the kivy default settings we use this module config 
from kivy.config import Config

from kivy.uix.pagelayout import PageLayout
from kivy.uix.stacklayout import StackLayout
  
# Adding the text input
t = TextInput(font_size = 15, size_hint_y = None, height = 50)
t2 = TextInput(font_size = 15, size_hint_y = None, height = 50)
t3 = TextInput(font_size = 15, size_hint_y = None, height = 50)

def saveBtn(instance):
    #test = open("Test.txt","w")
    print(t.text)

     
def ssBtn(instance):
    test = open("Test.txt","w")
    
    test.write(t.text)
    test.write("\n")
    test.write(t2.text)
    test.write("\n")
    test.write(t3.text)

    t.text = ""
    t2.text = ""
    t3.text = ""

# Create the App class
class TutorialApp(App):
    
    def build(self):
        lo = GridLayout(cols = 2,rows = 5, row_default_height = 40, spacing = 10)
        SL = StackLayout(orientation ='lr-tb')
        b = BoxLayout(orientation ='horizontal')
        bv = BoxLayout(orientation ='vertical')
  
          
        #f = FloatLayout()
        # Adding Button and styling
        sb = Button(text ="SAVE", 
                   font_size ="15sp", 
                   background_color =(.67, 1, .33, 1), 
                   size_hint_y = None,
                   height = 30,
                   width = 5,
                   color =(1, 1, 1, 1))
              
        
        ssb = Button(text ="SAVE & SUBMIT", 
                   font_size ="15sp", 
                   background_color =(.67, 1, .33, 1), 
                   size_hint_y = None,
                   height = 30,
                   width = 5,
                   color =(1, 1, 1, 1))
        
        title = Label(text ="TEST", font_size = 40, size_hint_y = None, height = 45)
        empty = Label(text ="", font_size = 40, size_hint_y = None, height = 45)
        l = Label(text ="Entry 1:", font_size = 20, size_hint_y = None, height = 45)
        l2 = Label(text ="Entry 2:", font_size = 20, size_hint_y = None, height = 45)
        l3 = Label(text ="Entry 3:", font_size = 20, size_hint_y = None, height = 45)

        sb.bind(on_press = saveBtn)
        ssb.bind(on_press = ssBtn)
        
        lo.add_widget(title)
        lo.add_widget(empty)
        lo.add_widget(l)
        lo.add_widget(t)
        lo.add_widget(l2)
        lo.add_widget(t2)
        lo.add_widget(l3)
        lo.add_widget(t3)
        lo.add_widget(sb)
        lo.add_widget(ssb)
  
        # Binding it with the label
        #t.bind(text = l.setter('text'))
        #return value
        
        return lo  


# Run the App
if __name__ == "__main__":
    TutorialApp().run()
