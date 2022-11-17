import turtle as t
from robot.functions import *




t.penup()  # Pulls the turtle's pen up in case it does not start the origin.
t.speed('slow')
t.bgcolor('Dodger blue')

#feet
t.goto(-100, -150)  # Moves the turtle position.
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')

#legs
t.goto(-25, -50)
rectangle(15, 100, 'grey')
t.goto(-55, -50)
rectangle(-15, 100, 'grey')

#body
t.goto(-90, 100)
rectangle(100, 150, 'green')

#left arm
t.goto(-150, 70)
rectangle(60, 15, 'grey')
t.goto(-150, 110)
rectangle(15, 40, 'grey')
#right arm
t.goto(10, 70)
rectangle(60, 15, 'grey')
t.goto(55, 110)
rectangle(15, 40, 'grey')


# hands
t.goto(-155, 130)
rectangle(25, 25, 'grey')
t.goto(-150, 130)
rectangle(5, 15, t.bgcolor())
t.goto(-140, 130)
rectangle(5, 15, t.bgcolor())

t.goto(50, 130)
rectangle(25, 25, 'grey')
t.goto(55, 130)
rectangle(5, 15, t.bgcolor())
t.goto(65, 130)
rectangle(5, 15, t.bgcolor())


#neck
t.goto(-50, 120)
rectangle(15, 20, 'grey')

#head
t.goto(-85, 170)
rectangle(80, 50, 'goldenrod')
t.hideturtle()

#eyes
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-55, 155)
rectangle(5, 5, 'black')
t.goto(-40, 155)
rectangle(5, 5, 'black')

#mouth
t.goto(-65, 135)
rectangle(40, 5, 'black')

t.goto(0,0)