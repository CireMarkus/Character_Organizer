import tkinter as Tk
from tkinter import ttk
import os

player_classes_path = os.path.join('Classes','resources')





class Stat_rolling_window(Tk.Frame):
	def __init__(self,master = None):
		super().__init__(master)
		self.master = master
		self.create_widgets()
		self.pack()
		self.class_tips()
		self.core_stats()

	def create_widgets(self):
		self.next_page = Tk.Button(self)
		self.next_page['text'] = 'next'
		self.next_page.grid(row = 2, column = 8)

		self.mainmenu = Tk.Button(self,text = 'Main\nMenu', fg = 'red', command = self.master.destroy)
		self.mainmenu.grid(row = 2, column = 1)
		
	def say_hi(self):
		print('hi there,everyone!')

	def class_tips(self):
		self.classtips_frame = Tk.LabelFrame(self)
		self.classtips_frame['text'] = 'Class tips'
		self.classtips_frame.grid(row = 0, column = 7, columnspan = 7)


		self.class_tipsheader = Tk.ttk.Label(self.classtips_frame,text = 'Class Tips',font =('Times New Roman', 32))
		self.class_tipsheader.grid(row = 0, column = 0 , columnspan = 7)

	def core_stats(self):
		stat_name_file = open(os.path.join('resources', 'Stat_names.txt'),'r')
		stat_names = []
		for i in stat_name_file.read().rstrip().split(';'):
			stat_names.append(i)
		stat_name_file.close()

		print(stat_names)
		corestats_frame = Tk.LabelFrame(self)
		corestats_frame['text'] = 'Core Stats'
		corestats_frame.grid(row = 0, column = 0, columnspan = 7)

		stat_boxes_menus = []
		stat_Boxes = []
		#creates the stat boxes that will hold the players rolls 
		for i in range (6):
			stat_Boxes.append(Tk.Entry(corestats_frame))
			stat_boxes_menus.append(ttk.Combobox(corestats_frame, values = stat_names))

			stat_boxes_menus[i].grid(row = i, column = 0)
			stat_Boxes[i].grid(row = i, column = 1)


class Race(Tk.Frame):
	#TODO create the frame that allows the player to choose a race.
	pass

class Profession(Tk.Frame):
	#TODO create the frame that allows the player to choose their class. 
	pass




root = Tk.Tk()
root.geometry('800x600')
app = Stat_rolling_window(master = root)
app.mainloop()