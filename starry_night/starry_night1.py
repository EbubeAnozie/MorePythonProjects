import turtle as t
from itertools import cycle

def draw_shape(size, angle, shift):
    t.hideturtle()
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_shape(size + 5, angle + 1, shift + 1)


size = 300
points = 41
angle = 180 - (180 / points) # odd number of points is preferred

t.hideturtle()
t.bgcolor("grey")

t.begin_fill()
t.color("purple")
for edge in range(points):
    t.forward(size)
    t.right(angle)
t.end_fill()
t.penup()

t.goto(-122, -122)
t.pendown()
colors = cycle(['purple', 'blue', 'green', 'yellow', 'orange', 'red'])

t.bgcolor('black')
t.speed('fast')
t.pensize(2)
draw_shape(30, 0, 1)