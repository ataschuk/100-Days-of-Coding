from tkinter import *
import turtle  
from turtle import *   

width, height = 500, 500

game = Screen() #create game gui
game.setup(width,height) #set screen size to 500 x 500
game.bgcolor("green") # set background color to green
game.title("Snake Game") #set title

background = Turtle(visible = False)
background.shape('square')
background.color('dark green')
background.home()
for i in range((width * height) // 2 ):
    if i % (width * height) // 2 == 0:
        background.stamp
        background.forward(10)
        if i % height == 0:
            if i % width == 0:
                background.right(90)
                background.forward(10)
                background.right(90)
    





snake = turtle.Turtle() #create turtle
snake.shape("circle") #set turtle shape to circle







game.mainloop()



""" Figure this mainscreen bullshit out later

gui = Tk() # tkinter variable

gui.title("Snake Game") # title at top of GUI 
gui.geometry('250x250') # sets GUI size to 500 x 500 pixels
    
# title on screen
gameTitle = Label(gui, text="Snake Game", font=("Calibri",20))
gameTitle.pack()
gameTitle.grid(column=0, row=0)

    # rules
def rulesClicked():
    ruleWindow = Toplevel(gui, height =  100, width= 100)
    ruleWindow.title(text = "Rules")
    ruleList = Message(ruleWindow, text = "1) Rule One \n 2) Rule Two \n 3) Rule 3")
    ruleList.pack()

    
    #rules button
rules = Button(gui, text = "Rules", fg = "black", bd = 2, command = rulesClicked)
rules.grid()

   

    



gui.mainloop() # needed to actually have the GUI show up
"""
