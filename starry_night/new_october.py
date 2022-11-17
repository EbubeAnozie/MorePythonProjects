import turtle as t
from random import random
# draw letter H
def draw_rectangle(horizontal, vertical, heading, x, y):
    t.hideturtle()
    t.setheading(heading)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for edge in range(2):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()

def draw_circle(size, x, y):
    t.penup()
    t.goto(x,y)
    t.penup()
    t.begin_fill()
    t.circle(size)
    t.end_fill()

def change_color():
    ran_color = (random(), random(), random())
    scr_ran_color = (random(), random(), random())
    while True:
        if ran_color != scr_ran_color:
            return t.color(ran_color), t.Screen().bgcolor(scr_ran_color)
        else:
            continue

# draw H
change_color()
draw_rectangle(20, 80, 0, -380, 40)
draw_rectangle(40, 20, 0, -360, 10)
draw_rectangle(20, 80, 0, -320, 40)

# draw A
change_color()

# draw P
change_color()
draw_rectangle(20, 80, 0, -220, 40)
while True:
    draw_circle(25, -197, 0)