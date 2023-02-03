import turtle
from turtle import *


WIDTH, HEIGHT = 680,680

screen = Screen() # create a screen
screen.screensize(WIDTH,HEIGHT) # set width and height of screen to 680 x 680
screen.title("Turtle Practice") # set the title



tile1 = Turtle() # create new turtle 
tile1.shape('square') # set turtle shape to a square
tile1.speed(0) # this boy fast as hell
tile1.penup() #hide turtle lines

tile1.goto(0,0)
tile1.stamp()
tile1.goto(-331,328) # top left corner of screen
tile1.stamp()
tile1.goto(-331, -328)
tile1.stamp()
tile1.goto(331, 328)
tile1.stamp()
tile1.goto(331,-328)
tile1.stamp()
tile1.setheading(0) # face turtle east
'''
switchColor = False
for i in range(34): # function that draws a square
    if i % 2 == 0:
        tile1.color('green')
        tile1.stamp()
        tile1.forward(21)
    if i % 2 != 0:
        tile1.forward(21)
    if tile1.xcor() > 299:
        tile1.right(90)
        tile1.stamp()
        tile1.forward(21)
        tile1.right(90)
        switchColor == True
    elif tile1.xcor() < -299:
        tile1.left(90)
        tile1.stamp()
        tile1.forward(21)
        tile1.left(90)
        switchColor = True
    if switchColor == True:
        tile1.color('dark green')

tile2 = Turtle()
tile2.shape('square')
tile2.speed(0) # this boy fast as hell
tile2.penup() #hide turtle lines
tile2.goto(-331,328) # top left corner of screen
tile2.setheading(0) # face turtle east

for j in range(34): # function that draws a square
    if j % 2 != 0:
        tile2.color('dark green')
        tile2.stamp()
        tile2.forward(21)
    if j % 2 == 0:
        tile2.forward(21)
    if tile2.xcor() > 300:
        tile2.right(90)
        tile2.stamp()
        tile2.forward(21)
        tile2.right(90)
        switchColor == True
    elif tile2.xcor() < -300:
        tile2.left(90)
        tile2.stamp()
        tile2.forward(21)
        tile2.left(90)
        switchColor = True
    if switchColor == True:
        tile2.color('green')
'''

    





turtle.done() # keeps the screen otile1 for more than 1 millisecond