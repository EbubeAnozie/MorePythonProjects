import turtle as t
from random import random, randint


t.Screen().bgcolor("dark blue")
t.speed("fast")

coordinates = [(0, 0), (5, 10), (10, 15), (20, 25), (30, 30), (40, 35), (50, 40), (60)]
for axes in coordinates:
    t.hideturtle()
    t.penup()
    t.goto(axes)
    t.pendown()
    ran_points = randint(2,4) * 2 + 1
    ran_size = randint(10,15)
    ran_color = (random(), random(), random())

    angle = 180 - (180 / ran_points)
    t.color(ran_color)
    t.begin_fill()
    for edge in range(ran_points):
        t.forward(ran_size)
        t.right(angle)
    t.end_fill()