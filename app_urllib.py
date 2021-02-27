import urllib.request
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import traceback 

Window.size = (400, 600)

class MyApp(App):

	def build(self):
		self.nam = TextInput()
		self.surname = TextInput()
		self.partyonic = TextInput()
		self.clas = TextInput()
		self.temp = TextInput()
		self.lab = Label(size=(400, 100))
		l = GridLayout(cols=2)
		bl = BoxLayout(orientation='vertical')
		bt = Button(on_press=self.submit, text="Отправить")
		
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
		bl.add_widget(self.lab)
		
		return bl

	def submit(self, obj):
		try:
			data = {"name": self.nam.text,
					"surname": self.surname.text,
					"patryonic" : self.partyonic.text,
					"class" : self.clas.text,
					"temperature" : self.temp.text}

			enc_data = urllib.parse.urlencode(data)
			url = "https://licei1.000webhostapp.com/get.php"

			f = urllib.request.urlopen(url + "?" + enc_data)
		except Exception as e:
			self.lab.text = traceback.format_exc()

if __name__ == '__main__':
	MyApp().run()
