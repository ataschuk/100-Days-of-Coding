import turtle
from turtle import *

WIDTH, HEIGHT = 680,620
screen = Screen() # create a screen
screen.setup(WIDTH + 4, HEIGHT + 8) # setsthe amount of area that the turtle can move. +4 and +8 are to take into account window border and title bar
screen.setworldcoordinates(0, 0, WIDTH,HEIGHT) # sets up a user-defined coordiate system with 0,0 in the bottom right corner and the top right (x,y) as Width and Height
screen.title("Turtle Practice") # sets the title on the window

turtle.tracer(0) #draw the board instantly
turtle.speed(0)

tile1 = Turtle() # create new turtle 
tile1.shapesize(3,3,0) # set the size of the turtle to 60 x 60 pixels
tile1.shape('square') # set turtle shape to a square
tile1.penup() #hide turtle lines
tile1.color('green') #turtle color is green

tile1.goto(30, 585) #set turtle position to top right corner


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



tile2 = Turtle() #create new turtle
tile2.shapesize(3,3,0) # set the size of the turtle to 60 x 60 pixels
tile2.shape('square') # set turtle shape to a square
tile2.penup() #hide turtle lines
tile2.color('dark green') #turtle color is green
tile2.goto(30, 585) #set turtle position to top right corner
tile2.setheading(0) # face turtle east



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



screen.register_shape("snake/snake_head.gif")
snakeHead = Turtle()
snakeHead.shape("snake/snake_head.gif")
snakeHead.penup()
snakeHead.showturtle()
snakeHead.goto(300,300)
turtle.tracer(1)



turtle.done()