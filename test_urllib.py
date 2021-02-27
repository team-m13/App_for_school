import urllib.request
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import traceback 

Window.size = (400, 600)

class MyApp(App):

	def build(self):
		self.nam = "rrr"
		self.surname = "rrr"
		self.partyonic = "rrr"
		self.clas = "rrr"
		self.temp = "ee"
		self.lab = Label(size=(400, 100))

		bl = BoxLayout(orientation='vertical')
		bt = Button(on_press=self.submit, text="Отправить")


		bl.add_widget(bt)
		bl.add_widget(self.lab)
		
		return bl

	def submit(self, obj):
		try:
			data = {"name": self.nam,
					"surname": self.surname,
					"patryonic" : self.partyonic,
					"class" : self.clas,
					"temperature" : self.temp}

			enc_data = urllib.parse.urlencode(data)
			url = "https://licei1.000webhostapp.com/get.php"

			f = urllib.request.urlopen(url + "?" + enc_data)
		except Exception as e:
			self.lab.text = traceback.format_exc()
		else:
			self.lab.text = "Good"

if __name__ == '__main__':
	MyApp().run()
