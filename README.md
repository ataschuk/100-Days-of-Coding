# 100-Days-of-Coding Logbook

**Day 13: 2/14/23**

- Missed yesterday too. :(

- I'm not really consitent with this, so instead of trying to code for an hour a day, I'm just gonna code whenever I have time.

- Plans for today:

- [X] Redraw snake head and body

- [ ] Change code that draws game board to use `fill` instead of `stamp`

- [ ] Resize main screen that has title screen, rules, play game, and quit button

- I started to replace `stamp` with `fill`, and although I would need to redo the conditions for drawing the entire board, I don't think that `stamp` is the problem because the snake turtle still isnt showing up after part of the board is drawn.

- I give up for the night

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
