from tkinter import *
from tkinter import ttk
import tkinter as tk


root = Tk()
titleScreen = ttk.Frame(master=root, width=450, height=450) # creates a frame widget. padding = size of window
root.title("Snake Game")
for i in range(3):
     titleScreen.grid(row=i, column=i) # creates a 3 x 3 grid

title = ttk.Label(master=root, text="Snake Game", relief="raised",font=("Times New Roman",50)).grid(column=2, row=1)

def rules_list(): # function that is called when the "Rules" Button is Pushed
     rules = Toplevel(root) # create new Toplevel called rules
     rules.title("rules") # set the title to "rules"
     rules.geometry('250x250') # set the size to 550 x 510
     Label(rules, text="rules: 1, 2, 3", font=("Times New Roman",20)).place(x=75,y=0) #label that will show rules
     rules = Button(rules, text="Go Back", command=rules.destroy).place(x=100, y=220) # "go back" button which will close rules window
     
rules = Button(master=root, relief=SUNKEN, text="Rules", font=("Times New Roman", 25), command=rules_list).grid(column=1, row=2) #rules button on main screen
quitGame = Button(root, relief=SUNKEN, text="Quit Game", font=("Times New Roman", 25), command=root.destroy).grid(column=2, row=3)





root.mainloop() # puts everything on display and responds to user input until the program terminates
