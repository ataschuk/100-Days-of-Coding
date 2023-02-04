import turtle
from turtle import *


WIDTH, HEIGHT = 680,620

screen = Screen() # create a screen
screen.setup(WIDTH + 4, HEIGHT + 8)
screen.setworldcoordinates(0, 0, WIDTH,HEIGHT)
# screen.screensize(WIDTH,HEIGHT) # set width and height of screen to 680 x 680
screen.title("Turtle Practice") # set the title



tile1 = Turtle() # create new turtle 
tile1.shapesize(3,3,0)
tile1.shape('square') # set turtle shape to a square
tile1.speed(0) # this boy fast as hell
tile1.penup() #hide turtle lines
tile1.color('green') #turtle color is green
tile1.setpos(30, 585) #set turtle position to top right corner
tile1.setheading(0) # face turtle east
tile1._tracer(0,0)




for i in range(110): # function that draws a square
    if tile1.xcor() > 661:
        tile1.right(90)
        tile1.forward(61)
        tile1.right(90)
        tile1.forward(61)
    if tile1.xcor() < 30:
        tile1.left(90)
        tile1.forward(61)
        tile1.left(90)
        tile1.forward(61)
    if i % 2 == 0:
        tile1.stamp()
        tile1.forward(61)
    else:
        tile1.forward(61)


tile2 = Turtle() # create new turtle 
tile2.shapesize(3,3,0)
tile2.shape('square') # set turtle shape to a square
tile2.speed(0) # this boy fast as hell
tile2.penup() #hide turtle lines
tile2.color('dark green') #turtle color is green
tile2.setpos(30, 585) #set turtle position to top right corner
tile2.setheading(0) # face turtle east
tile2._tracer(0.0)


for j in range(110): # function that draws a square
    if tile2.xcor() > 661:
        tile2.right(90)
        tile2.forward(61)
        tile2.right(90)
        tile2.forward(61)
    if tile2.xcor() < 30:
        tile2.left(90)
        tile2.forward(61)
        tile2.left(90)
        tile2.forward(61)
    if j % 2 != 0:
        tile2.stamp()
        tile2.forward(61)
    else:
        tile2.forward(61)


    


turtle.done() # keeps the screen open for more than 1 millisecond