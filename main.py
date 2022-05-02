#showcase my kivy orm 
from kivy.lang import Builder 
from kivy.storage.jsonstore import JsonStore
from kivy.metrics import sp
from kivy.core.window import Window 
from kivy.properties import ListProperty,ObjectProperty,StringProperty
from kivy.clock import Clock 
from kivy.uix.settings import SettingsWithTabbedPanel #some changes
from kivymd.app import MDApp 
#--start of layouts---
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

from kivyorm.uis.behavior import ExtendedThemableBehavior

from kivyorm.uis.popups import LoadingPopup, ExitPopup
#from kivy.uix.behaviors.focus import FocusBehavior 

#opts=FocusBehavior.input_type.options 
#print(opts)

cascading_stylesheet="./stylesheet.kv"

class MainScreen(MDScreen):
	"""
	
	"""
	navbar=ObjectProperty()
	sidebar=ObjectProperty()
	
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		


class ShowcaseApp(MDApp):
	
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.title="up to time"
		self.icon="./media/uptotime_logo_transparent.png"
		
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Brown"
		self.theme_cls.primary_hue = "500"
		self.theme_cls.accent_palette = "BlueGray"
		self.theme_cls.accent_hue = "500"
		Window.softinput_mode="below_target"
		#Window.bind(on_keyboard=self.revert_to_screen)
		kv_file=Builder.load_file(cascading_stylesheet)
		return kv_file

	def show_exiter(self):
		#btm=Clock.get_boottime()
		#print(btm,"from popup open func")
		pop=ExitPopup()
		#(title="base popup",size_hint=(0.5,0.45)) 
		pop.open()
		
	def on_start(self):
		btm=Clock.get_boottime()
		#print(btm,"from on start")





if __name__=="__main__":
	ShowcaseApp().run()