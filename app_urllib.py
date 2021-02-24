import urllib.request
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from functools import partial

from kivy.config import Config
Config.set('graphics', 'resizable', 0)

from kivy.core.window import Window
Window.size = (400, 600)


class MyApp(App):

	def build(self):
		self.nam = TextInput()
		self.surname = TextInput()
		self.partyonic = TextInput()
		self.clas = TextInput()
		self.temp = TextInput()
		l = GridLayout(cols=2)
		bl = BoxLayout(orientation='vertical')
		bt = Button(on_press=self.submit, text="Отправить")
		#bt = Button(on_press=self.callback) #on_press=partial(self.callback, temp)
		#bt.bind(on_press=self.callback)
		
		l.add_widget(Label(text="Введите своё Имя"))
		l.add_widget(self.nam)
    	
		l.add_widget(Label(text="Введите свою Фамилию"))
		l.add_widget(self.surname)
    	
		l.add_widget(Label(text="Введите своё Отчество"))
		l.add_widget(self.partyonic)
    	
		l.add_widget(Label(text="Введите свой Класс"))
		l.add_widget(self.clas)

		l.add_widget(Label(text="Введите свою темпиратуру"))
		l.add_widget(self.temp)

		bl.add_widget(l)
		bl.add_widget(bt)
		
		return bl

	def submit(self, obj):
		data = {"name": self.nam.text,
				"surname": self.surname.text,
				"patryonic" : self.partyonic.text,
				"class" : self.clas.text,
				"temperature" : self.temp.text}

		enc_data = urllib.parse.urlencode(data)
		url = "https://licei1.000webhostapp.com/get.php"

		f = urllib.request.urlopen(url + "?" + enc_data)


if __name__ == '__main__':
	MyApp().run()
