from tkinter import *

class GUI:

    gui = Tk() # tkinter variable

    gui.title("Snake Game") # title at top of GUI 
    gui.geometry("500x500") # sets GUI size to 500 x 500 pixels
    
    gameTitle = Label(gui, text="Snake Game").place(x=100,y=100)
   

    



    gui.mainloop() # needed to actually have the GUI show up

