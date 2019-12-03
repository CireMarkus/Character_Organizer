#============
#imports
#============
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

#creation of the main menu
root = tk.Tk()
root.title('Main Menu') #Window title change later
root.geometry('1200x700')

#Main Menu frame that holds image
topMenu = ttk.LabelFrame(root,text = 'top Menu',height = 600, width = 1000)
topMenu.pack(side = 'top')

#Holds the buttons that 
bottomMenu = ttk.LabelFrame(root,text='bottom Menu',height =200, width = 500)
bottomMenu.pack(side = 'bottom')


#Main menu image 
mainMenuImage = Image.open('mainMenu.BMP') #main menu image
render = ImageTk.PhotoImage(mainMenuImage)
img = tk.Label(topMenu, image = render,height = 600, width = 1000)
img.image = render 
img.place(relx = 0.5, rely=0.55, anchor = 'center')



#Button call backs
def load_character():
	#TODO create move file select and load character

def create_character():
	#TODO creat character creation sequence

def quit_game():
	exit()




#Main menu buttons 
create = ttk.Button(bottomMenu,text = 'Create\nCharacter')
create.place(relx = 0.25, rely=0.37,anchor = 's')

load = ttk.Button(bottomMenu,text='Load\nCharacter')
load.place(relx = .50, rely=.37,anchor = 's')

quit = ttk.Button(bottomMenu, text = 'Quit', command = quit_game)
quit.place(relx = .75, rely = .37, anchor = 's')


#mainloop
root.mainloop()