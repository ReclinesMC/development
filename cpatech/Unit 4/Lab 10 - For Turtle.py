# Sean A
# For Turtle
# Use a for statement to make a unique drawing on turtle


import random
import turtle
from turtle import Screen

t = turtle.Turtle()

Screen().bgcolor("#696969")
t.penup()
t.goto(0, 0)
t.pendown()
t.speed(0)
for art in range(500):
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    #  Screen().colormode(255) # Not needed on trinket
    t.pencolor(r, b, g)
    # Making the square
    t.forward(art)
    t.left(90)
t.penup()
