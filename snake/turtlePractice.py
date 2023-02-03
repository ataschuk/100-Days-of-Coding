import turtle
from turtle import *


WIDTH, HEIGHT = 680,680

screen = Screen() # create a screen
screen.bgcolor('green')
screen.title("Turtle Practice") # set the title
screen.setup(HEIGHT, WIDTH)



pen = Turtle() # create new turtle 
pen.shape('square') # set turtle shape to a square
pen.color('dark green') # set the color to dark green

pen.speed(0) # this boy fast as hell
pen.penup()

pen.goto(-328,329) # put the turtle in the top left of the screen
pen.setheading(0)




for i in range(68): # function that draws a square
    pen.stamp()
    pen.forward(42) # moves the turtle 100 pixels forward and draws a line
    if i == 17:
        pen.right(90)
        pen.right(90)
        continue
 
    





turtle.done() # keeps the screen open for more than 1 millisecond