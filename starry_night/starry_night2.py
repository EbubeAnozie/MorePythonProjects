import turtle as t
from random import randint, random

def draw_star(points=5, size=50, color="purple", x=0, y=0):
    t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(color)
    t.begin_fill()
    for edge in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()


t.Screen().bgcolor("dark blue")
t.speed("fast")
while True:
    ran_points = randint(2,4) * 2 + 1
    ran_size = randint(10,50)
    ran_color = (random(), random(), random())
    ran_x = randint(-450,450)
    ran_y = randint(-350,350)
    
    draw_star(ran_points, ran_size, ran_color, ran_x, ran_y)