import turtle as t
from robot.functions import *


t.penup()  # Pulls the turtle's pen up in case it does not start the origin.
t.speed('fast')
print(t.window_width())
print(t.window_height())
t.bgcolor('Dodgerblue')

# feet
t.goto(-100, -150)  # Moves the turtle position.
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')

# legs
t.goto(-25, -50)
rectangle(15, 100, 'grey')
t.goto(-55, -50)
rectangle(-15, 100, 'grey')

# body
t.goto(-90, 100)
rectangle(100, 150, 'green')

# arms
t.goto(-90, 85)
t.setheading(135)
arm('light blue')

t.goto(10, 85)
t.setheading(315)
arm('goldenrod')

# neck
t.goto(-50, 120)
rectangle(15, 20, 'grey')

# head
t.goto(-85, 170)
rectangle(80, 50, 'goldenrod')
t.hideturtle()

# eyes
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-60, 160)
rectangle(5, 5, 'black')
t.goto(-45, 155)
rectangle(5, 5, 'black')

# mouth
t.goto(-65, 135)
rectangle(40, 5, 'black')



t.goto(0, 0)
