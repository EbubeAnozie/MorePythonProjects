import turtle as t


def rectangle(horizontal, vertical, color):
    """
    This draws a rectangle
    """
    t.shape('turtle')
    t.setheading(0)
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    # Draw the rectangle
    for counter in range(1, 3):  # Makes the loop run twice.
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()   # Pull tpenhe turtle's  back up.


def arm(color):
    t.pendown()
    t.begin_fill()
    t.color(color)
    t.forward(60)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.end_fill()
    t.penup()
    t.setheading(0)
