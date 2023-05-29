#Greg Brewer
# 5/28/2023
# Problem 5 draw turtle

import turtle
def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

wn.exitonclick()
