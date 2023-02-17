# 100-Days-of-Coding Logbook

**Day 14: 2/16/23**

- Plans for today:
[X] Get custom snake head working

- Decided to restart back to before I began to try to use a custom turtle head b/c my code got too messy.

- I've narrowed down the issue to 3 lines of code:

```Python
screen.setup(WIDTH + 4, HEIGHT + 8) 
screen.setworldcoordinates(0, 0, WIDTH,HEIGHT)
screen.title("Turtle Practice") 
```

- I'm not sure which line(s) is/are causing the snake head to not show up though.

- So it turns out that those 3 lines were not the issue at all. It was `tile1._tracer(0)` and `tile2._tracer(0)` which was the problem, or rather, the fact that the `snakeHead` turtle doesn't have a `_tracer()` function. `_tracer()` has the parameters *n = None* and *delay = None*. *n* can either be a 0 or a 1 where 0 means automatic screen updates are off and 1 means they're on. If you use a number larger than 1, it will only update every $n^{th}$ time (e.g. if n = 3 only every third update would actually happen). It seems that calling `tile1._tracer(0)` affects all turtles, so `tile2._tracer(0)` actually had no effect at all. `tile1.tracer(0)` has the same effect as `turtle.tracer(0)`, so I changed that. The delay function affects the time between turtle movements (this is different from `turtle.speed()`) and is usually used to control timing of a turtle's movements (`turtle.speed()` is usually used to control turtle movement). The fix to this problem that has taken well over 4 hours of trying to fix out is literally just adding `turtle.tracer(0)` after I create my snakeHead turtle. That's it.

**Day 13: 2/14/23**

- Missed yesterday too. :(

- I'm not really consitent with this, so instead of trying to code for an hour a day, I'm just gonna code whenever I have time.

- Plans for today:

- [X] Redraw snake head and body

![This is the head](/snake/snake_head.gif "Snake Head")
![This is the body](/snake/snake_body.gif "Snake Body")

- [ ] ~~Change code that draws game board to use `fill` instead of `stamp`~~

- [ ] Resize main screen that has title screen, rules, play game, and quit button

- I started to replace `stamp` with `fill`, and although I would need to redo the conditions for drawing the entire board, I don't think that `stamp` is the problem because the snake turtle still isnt showing up after part of the board is drawn.

- I give up for the night: Possible solution for next time: Draw snake head and body using turtle screen (e.g. `screen = turtle.Screen()`)

**Day 12: 2/13/23**

- Missed yesterday. Sorry

- Plans for today:

- ~~[ ] Redraw snake head and body~~

- ~~[ ] Change code that draws game board to use `fill` instead of `stamp`~~

- ~~[ ] Resize main screen that has title screen, rules, play game, and quit button~~

**Day 10: 2/11/23**

- Missed the past 5 days. My fault.

- Today, I got the rules button and screen fully set up, along with the "play" button which will open the green checkered board I finished on the 2/3.

- I drew a custom head and body for the snake which I imported into the python file to use as custom shapes for the turtles.

![This is the head](/snake_head.gif)
![This is the body](/snake_body.gif)

- For some reason, the snake head is being drawn under the checkered turtles so it is not visible. I tried moving around where the turtle is defined and drawn, but it didn't change anything. I think it may have something to do with the fact that the checkered turtles utilize the `stamp` function in python. I might have to replace them with the `fill` function which will be a pain and I'm leaving for next time.

- I also realized that I made both the game board and snake green, so I'll have to redraw the snake body and head tomorrow.

**Day 5: 2/6/23**

- Figured out how to have a button open a new screen when pressed.

- Added a "Back" button that closes the "rules" Toplevel when pressed.

- Added a "Quit Game" button that closes the program when pressed.

- `.grid()` will not work Toplevel (at least I couldn't figure out how to make it work so I'm assuming that only works with windows)

- I have a decent understanding of basic widgets such as `Button`, `Label`, `Frame`, `Title` and what a window is.

**Day 4: 2/5/23**

- Learned about buttons and frames

**Day 3: 2/4/23**

- Read about different tkkinter commands and continued to get a basic understanding of the tkinter syntax

- Began to use the [Official Tk Commands Reference Menu](https://www.tcl.tk/man/tcl8.6/TkCmd/contents.html) to learn about the different commands and widgets tkinter offers

- I also found a solid website with some explinations of [tkinter Widgets](https://www.studytonight.com/tkinter)

- [Official Python Documentation on tkinter](https://docs.python.org/3/library/tkinter.html)

- Got a decent understanding of the label widget down.

**Day 2: 2/3/23**

- Successfully created a checkered board with the turtle module

- Deleted game.py file because I decided to build off of the turtlePractice board.

- Began to learn tkinter

**Day 1:2/2/23**

- Began to understand basic syntax around python (for loops and if statements) and the basics of the turtle module:

  - `turtle.shape, color, speed, goto, setheading, penup/down, stamp,'

 **Day 0: 2/1/23**

- Began to work on Snake game
- Created rough draft of all class, interfaces, ect needed
- Started to learn about tkinter

- Gave up on learning about tkinter for now and moved on to creating the game w/ turtles for now
- Tried to create a checkered pattern w/ turtle for game board. Failed.
