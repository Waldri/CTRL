from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

class BlueScreenApp(App):
    def build(self):
        # Define a cor de fundo para azul
        Window.clearcolor = (1, 0, 0, 1)
        
        # Crie um layout com um rótulo centralizado
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Tela Cheia Vermelho")
        layout.add_widget(label)
        
        return layout

if __name__ == '__main__':
    BlueScreenApp().run()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

class BlueScreenApp(App):
    def build(self):
        # Define a cor de fundo para azul
        Window.clearcolor = (0, 0, 1, 1)
        
        # Crie um layout com um rótulo centralizado
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Tela Cheia Azul")
        layout.add_widget(label)
        
        return layout

if __name__ == '__main__':
    BlueScreenApp().run()
