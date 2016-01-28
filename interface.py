'''This is a open source project "Chikki". '''
#print "wait! I am starting up.\n"
from gi.repository import Gtk,GObject
import os

class MyWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self,title="Chikki")
		
		self.set_size_request(160,60)
	
		self.grid=Gtk.Grid()
		self.add(self.grid)

		self.entry=Gtk.Entry()
		self.entry.set_text("Hey!type something...")
		self.grid.add(self.entry)


		self.button=Gtk.Button(label="Click Me!")
		self.button.connect("clicked",self.on_button_clicked)

		self.grid.attach(self.button,0,1,1,1)
		

	def on_button_clicked(self,widget):

		os.system("xdg-open /home/atul/abc.png")


win=MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()


