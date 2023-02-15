import turtle


def tofront(t):
    t.forward(0)


WIDTH, HEIGHT = 680, 620
"""
screen = Screen() # create a screen
screen.setup(WIDTH + 4, HEIGHT + 8) # setsthe amount of area that the turtle can move. +4 and +8 are to take into account window border and title bar
screen.setworldcoordinates(0, 0, WIDTH,HEIGHT) # sets up a user-defined coordiate system with 0,0 in the bottom right corner and the top right (x,y) as 
                                               # Width and Height
screen.title("Turtle Practice") # sets the title on the window
"""
turtle.screensize(canvwidth=WIDTH, canvheight=HEIGHT)
turtle.setworldcoordinates(0, 0, WIDTH, HEIGHT)
turtle.title("Turtle Practice")

doneDrawOne = False

"""
tile1 = turtle.Turtle()  # create new turtle
# tile1.shapesize(3,3,0) # set the size of the turtle to 60 x 60 pixels
tile1.speed(0)  # this boy fast as hell
tile1.penup()  # hide turtle lines
tile1.setpos(30, 585)  # set turtle position to top right corner
tile1._tracer(0)  # instantly create the drawing without any animation
tile1.fillcolor('green')

for i in range(110):  # function that draws a  green square
    if tile1.xcor() > 661:  # if the turtle gets past a certain coordinate, have it go to the next line down and do a 180 degree turn
        tile1.right(90)
        tile1.forward(61)
        tile1.right(90)
        tile1.forward(61)
    if tile1.xcor() < 30:  # if the turtle gets past a certain coordinate, have it go to the next line down and do a 180 degree turn
        tile1.left(90)
        tile1.forward(61)
        tile1.left(90)
        tile1.forward(61)

    if i % 2 == 0:  # if the turtle is on an "even" square, stamp the square in the turtle's location, then move forward. otherwise, just move forward
        tile1.begin_fill()
        for _ in range(4):
            tile1.forward(61)
            tile1.right(90)
        tile1.forward(61)
        tile1.end_fill()
    else:
        tile1.forward(61)


tile2 = turtle.Turtle()  # create new turtle
tile2.shapesize(3, 3, 0)  # set the size of the turtle to 60 x 60 pixels
tile2.shape('square')  # set turtle shape to a square
tile2.speed(0)  # this boy fast as hell
tile2.penup()  # hide turtle lines
tile2.color('dark green')  # turtle color is green
tile2.setpos(30, 585)  # set turtle position to top right corner
tile2.setheading(0)  # face turtle east
tile2._tracer(0)  # instantly create the drawing without any animation
tile2.fillcolor('dark green')


for j in range(110):  # function that draws a square
    if tile2.xcor() > 661:  # if the turtle gets past a certain coordinate, have it go to the next line down and do a 180 degree turn
        tile2.right(90)
        tile2.forward(61)
        tile2.right(90)
        tile2.forward(61)
    if tile2.xcor() < 30:  # if the turtle gets past a certain coordinate, have it go to the next line down and do a 180 degree turn
        tile2.left(90)
        tile2.forward(61)
        tile2.left(90)
        tile2.forward(61)
    if j % 2 != 0:  # if the turtle is on an "odd" square, stamp the square in the turtle's location, then move forward. otherwise, just move forward
        tile2.begin_fill()
        for _ in range(4):
            tile2.forward(61)
            tile2.left(90)
        tile2.forward(61)
        tile2.end_fill()
    else:
        tile2.forward(61)
"""
"""
snakeHead = turtle.Turtle()  # create new turtle
turtle.register_shape('snake_head.gif')
snakeHead.shapesize(3, 3, 0)  # set the size of the turtle to 60 x 60 pixels
snakeHead.shape('snake_head.gif')
snakeHead.speed(0)  # this boy fast as hell
snakeHead.penup()  # hide turtle lines
snakeHead.setpos(30, 585)  # set turtle position to top right corner
snakeHead.setheading(0)  # face turtle east
snakeHead._tracer(0)  # instantly create the drawing without any animation
turtle.onscreenclick(lambda x, y: tofront(snakeHead))
"""
tile3 = turtle.Turtle()  # create new turtle
turtle.register_shape('snake_head.gif')
tile3.shape('snake_head.gif')
tile3.shapesize(2, 2, 0)  # set the size of the turtle to 60 x 60 pixels
#tile3.color('black')
tile3.speed(0)  # this boy fast as hell

tile3.setpos(30, 585)  # set turtle position to top right corner
tile3._tracer(0)  # instantly create the drawing without any animation


for i in range(110):  # function that draws a  green square
    if tile3.xcor() > 661:  # if the turtle gets past a certain coordinate, have it go to the next line down and do a 180 degree turn
        tile3.right(90)
        tile3.forward(61)
        tile3.right(90)
        tile3.forward(61)
    if tile3.xcor() < 30:  # if the turtle gets past a certain coordinate, have it go to the next line down and do a 180 degree turn
        tile3.left(90)
        tile3.forward(61)
        tile3.left(90)
        tile3.forward(61)

    if i % 2 == 0:  # if the turtle is on an "even" square, stamp the square in the turtle's location, then move forward. otherwise, just move forward
        for _ in range(4):
            tile3.forward(61)
            tile3.right(90)
        tile3.forward(61)
    else:
        tile3.forward(61)

turtle.done()  # keeps the screen open for more than 1 millisecond
