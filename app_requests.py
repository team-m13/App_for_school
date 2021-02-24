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

		url = "https://licei1.000webhostapp.com/get.php"

		f = requests.get(f"{url}?name={self.nam.text}&surname={self.surname.text}&patryonic={self.partyonic.text}&class={self.clas.text}&temperature={self.temp.text}")
		

if __name__ == '__main__':
	MyApp().run()

