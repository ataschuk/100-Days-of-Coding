from tkinter import *
from tkinter import ttk
import tkinter as tk
import turtle
from turtle import *


root = Tk()
titleScreen = ttk.Frame(master=root, width=450, height=450) # creates a frame widget. padding = size of window
root.title("Snake Game")


title = ttk.Label(master=root, text="Snake Game", relief="raised",font=("Times New Roman",50)).pack(side=TOP,fill=X,expand=False)

def rules_list(): # function that is called when the "Rules" Button is Pushed
     rules = Toplevel(root) # create new Toplevel called rules
     rules.title("rules") # set the title to "rules"
     rules.geometry('250x250') # set the size to 250 x 250
     Label(rules, text='1. Eat "food" dots to gain length. \n 2. If you run into a wall \n or yourself, you lose. \n 3. To win, the snake must take \
           \n up every spot on the game board. \n 4. WASD for forward, left, \n down, and right',
      font=("Times New Roman",15)).pack(side= TOP, fill= BOTH, expand= True) #label that will show rules
     rules = Button(rules, text="Go Back", relief = SUNKEN, command=rules.destroy).place(x=100, y=220) # "go back" button which will close rules window

def play_btn():

     WIDTH, HEIGHT = 680,620
     screen = Screen() # create a screen
     screen.setup(WIDTH + 4, HEIGHT + 8) # setsthe amount of area that the turtle can move. +4 and +8 are to take into account window border and title bar
     screen.setworldcoordinates(0, 0, WIDTH,HEIGHT) # sets up a user-defined coordiate system with 0,0 in the bottom right corner and the top right (x,y) as 
                                                  # Width and Height
     screen.title("Turtle Practice") # sets the title on the window

     tile1 = Turtle() # create new turtle 
     tile1.shapesize(3,3,0) # set the size of the turtle to 60 x 60 pixels
     tile1.shape('square') # set turtle shape to a square
     tile1.speed(0) # this boy fast as hell
     tile1.penup() #hide turtle lines
     tile1.color('green') #turtle color is green
     tile1.setpos(30, 585) #set turtle position to top right corner
     tile1._tracer(0,0) # instantly create the drawing without any animation
     for i in range(110): # function that draws a  green square
          if tile1.xcor() > 661: # if the turtle gets past a certain coordinate, have it go to the next line down and do a 180 degree turn
               tile1.right(90)
               tile1.forward(61)
               tile1.right(90)
               tile1.forward(61)
          if tile1.xcor() < 30: # if the turtle gets past a certain coordinate, have it go to the next line down and do a 180 degree turn
               tile1.left(90)
               tile1.forward(61)
               tile1.left(90)
               tile1.forward(61)
          if i % 2 == 0: # if the turtle is on an "even" square, stamp the square in the turtle's location, then move forward. otherwise, just move forward
                tile1.stamp()
                tile1.forward(61)
          else:
               tile1.forward(61)
     tile2 = Turtle() # create new turtle 
     tile2.shapesize(3,3,0) # set the size of the turtle to 60 x 60 pixels
     tile2.shape('square') # set turtle shape to a square
     tile2.speed(0) # this boy fast as hell
     tile2.penup() #hide turtle lines
     tile2.color('dark green') #turtle color is green
     tile2.setpos(30, 585) #set turtle position to top right corner
     tile2.setheading(0) # face turtle east
     tile2._tracer(0.0) # instantly create the drawing without any animation
     for j in range(110): # function that draws a square
          if tile2.xcor() > 661: # if the turtle gets past a certain coordinate, have it go to the next line down and do a 180 degree turn
               tile2.right(90)
               tile2.forward(61)
               tile2.right(90)
               tile2.forward(61)
          if tile2.xcor() < 30: # if the turtle gets past a certain coordinate, have it go to the next line down and do a 180 degree turn
               tile2.left(90)
               tile2.forward(61)
               tile2.left(90)
               tile2.forward(61)
          if j % 2 != 0: # if the turtle is on an "odd" square, stamp the square in the turtle's location, then move forward. otherwise, just move forward
               tile2.stamp()
               tile2.forward(61)
          else:
               tile2.forward(61)

rules = Button(master=root, relief=SUNKEN, text="Rules", font=("Times New Roman", 25), command=rules_list).pack(side=LEFT, fill=None, expand=TRUE) #rules button on main screen
quitGame = Button(root, relief=SUNKEN, text="Quit Game", font=("Times New Roman", 25), command=root.destroy).pack(side=BOTTOM,fill=None, expand= False)
play = Button(root, relief=SUNKEN, text = "Play Game",font=("Times New Roman", 25), command= play_btn).pack(side=TOP, fill=None, expand=TRUE)




root.mainloop() # puts everything on display and responds to user input until the program terminates
