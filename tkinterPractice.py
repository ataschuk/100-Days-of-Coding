from tkinter import *
from tkinter import ttk

root = Tk() # create an instance of Tk called "root"
frm = ttk.Frame(root, padding = 80) # creates a frame widget. padding = size of window
frm.grid() #not really sure tbh
ttk.Label(frm, text = "Hello World").grid(column =0, row=0) # creates a label widget holding a certain string 
ttk.Button(frm, text = "Quit", command=root.destroy).grid(column = 1, row=0) # creates a button that says "quit" and calls the "destroy" method when pressed

root.mainloop() # puts everything on display and responds to user input until the program terminates
