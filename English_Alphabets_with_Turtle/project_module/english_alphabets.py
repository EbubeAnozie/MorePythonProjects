import turtle as t
from random import random


def change_color():
    ran_color = (random(), random(), random())
    scr_ran_color = (random(), random(), random())
    while True:
        if ran_color != scr_ran_color:
            return t.color(ran_color), t.Screen().bgcolor(scr_ran_color)
        else:
            continue


def draw_A(x):
    """
    This draws letter A.
    """
    change_color()
    t.penup()
    t.goto(x,80)
    t.pendown()
    t.setheading(345)
    t.begin_fill()
    for edge in range(2):
        t.forward(20)
        t.right(90)
        t.forward(80)
        t.right(90)
    t.goto(x, 75)
    t.setheading(15)
    for edge in range(2):
        t.forward(20)
        t.right(90)
        t.forward(80)
        t.right(90)
    t.end_fill()
    t.setheading(0)

# draw B
def draw_B(x):
    change_color()
    t.penup()
    t.goto(x,0)
    t.pendown()
    t.begin_fill()
    for edge in range(2):
        t.forward(15)
        t.left(90)
        t.forward(80)
        t.left(90)
    t.penup()
    t.goto(x+25, 0)
    t.setheading(0)
    t.circle(25)
    t.end_fill()
    t.setheading(0)

# draw C
# draw D
def draw_D(x):
    change_color()
    t.penup()
    t.goto(x, 0)
    t.begin_fill()
    t.circle(25)
    t.penup()
    t.goto(x+10,0)
    t.pendown()
    for edge in range(2):
        t.forward(15)
        t.left(90)
        t.forward(80)
        t.left(90)
    t.end_fill()
    t.setheading(0)


# draw E
def draw_E(x):
    change_color()
    t.penup()
    t.goto(x,0)
    t.pendown()
    t.begin_fill()
    t.forward(60)
    for i in range(2):
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(40)
        t.right(90)
        t.forward(5)
        t.right(90)
        t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(70)
    t.end_fill()
    t.goto(x + 60, 0)
    t.setheading(0)

# draw F
# draw G
# draw H

def draw_I(x):
    change_color()
    t.penup()
    t.goto(x,0)
    t.pendown()
    t.begin_fill()
    for edge in range(2):
        t.forward(20)
        t.left(90)
        t.forward(80)
        t.left(90)
    t.end_fill()
    t.setheading(0)

# draw J
# draw K
# draw L
# draw M
# draw N

def draw_O(x):
    change_color()
    t.penup()
    t.goto(x, 0)
    t.penup()
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.setheading(0)

# draw P
# draw Q
# draw R
# draw S
# draw T
# draw U
    
def draw_V(x):
    change_color()
    t.penup()
    t.goto(x,0)
    t.pendown()
    t.setheading(15)
    t.begin_fill()
    for edge in range(2):
        t.forward(20)
        t.left(90)
        t.forward(80)
        t.left(90)
    t.penup()
    t.goto(x,5)
    t.pendown()    
    t.setheading(345)
    for edge in range(2):
        t.forward(20)
        t.left(90)
        t.forward(80)
        t.left(90)
    t.end_fill()
    t.setheading(0)

# draw W
# draw X
# draw Y
# draw Z
            
def draw(message):
    letters = list(message)
    x = 0
    increment = 70
    for letter in letters:
        if letter.lower() == "a":
            draw_A(x)
            x += increment
        elif letter.lower() == "b":
            draw_B(x)
            x += increment
        elif letter.lower() == "c":
            draw_C(x)
            x += increment
        elif letter.lower() == "d":
            draw_D(x)
            x += increment
        elif letter.lower() == "e":
            draw_E(x)
            x += increment
        elif letter.lower() == "f":
            draw_F(x)
            x += increment
        elif letter.lower() == "g":
            draw_G(x)
            x += increment
        elif letter.lower() == "h":
            draw_H(x)
            x += increment
        elif letter.lower() == "i":
            draw_I(x)
            x += increment
        elif letter.lower() == "j":
            draw_J(x)
            x += increment
        elif letter.lower() == "k":
            draw_K(x)
            x += increment
        elif letter.lower() == "l":
            draw_L(x)
            x += increment
        elif letter.lower() == "m":
            draw_M(x)
            x += increment
        elif letter.lower() == "n":
            draw_N(x)
            x += increment
        elif letter.lower() == "o":
            draw_O(x)
            x += increment
        elif letter.lower() == "p":
            draw_P(x)
            x += increment
        elif letter.lower() == "q":
            draw_Q(x)
            x += increment
        elif letter.lower() == "r":
            draw_R(x)
            x += increment
        elif letter.lower() == "s":
            draw_S(x)
            x += increment
        elif letter.lower() == "t":
            draw_T(x)
            x += increment
        elif letter.lower() == "u":
            draw_U(x)
            x += increment
        elif letter.lower() == "v":
            draw_V(x)
            x += increment
        elif letter.lower() == "w":
            draw_W(x)
            x += increment
        elif letter.lower() == "x":
            draw_X(x)
            x += increment
        elif letter.lower() == "y":
            draw_Y(R)
            x += increment
        elif letter.lower() == "z":
            draw_Z(x)
            x += increment
        else:
            continue


if __name__ == "__main__":
    try_sample = 1
    while try_sample:
        draw("e")

