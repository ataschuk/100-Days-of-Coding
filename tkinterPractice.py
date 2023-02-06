from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk() # create an instance of Tk called "root"
root.geometry('450x450')

frame1= Frame(root, width=450, height=450).pack(side=TOP)
title = Label(root, text="Snake Game",font=("Times New Roman",50)).pack(side=TOP)

'''
titleScreen = ttk.Frame(root, width=450, height=450) # creates a frame widget. padding = size of window

for i in range(3):
     titleScreen.grid(row=i, column=i) # creates a 3 x 3 grid

title = ttk.Label(master=root, text="Snake Game", relief="raised",font=("Times New Roman",50)).grid(column=2, row=1)

def rules_list():
     rulesList = ttk.Frame(master=root, width= 450, height= 450,)
     rule = ttk.Label(master=root, text="Rule 1. /n Rule 2. /n Rule 3.").grid(column=2, row=3)
     titleScreen.lower()
     

     
rules = Button(master=root, relief="sunken", text="Rules", font=("Times New Roman", 25), command=rules_list).grid(column=1, row=2)
'''




#print(titleScreen.configure().keys()) #to find out what configuration options are available for on any widget, call the configure method which returns  
                                      # a dictionary containing a variety of information about each object, including its default and current values. 
                                      # Use keys() to get just the names of each option.

root.mainloop() # puts everything on display and responds to user input until the program terminates
