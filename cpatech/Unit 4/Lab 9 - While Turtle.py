# Sean A
# While turtle 😭
# Use a while statement to make a unique drawing on turtle


import random
import turtle
from turtle import Screen

t = turtle.Turtle()
art = 0

Screen().bgcolor("black")
t.penup()
t.goto(0, -250)
t.pendown()
t.speed(0)
while art < 500:
    r = random.randint(1, 255)
    b = random.randint(1, 255)
    g = random.randint(1, 255)
    t.pencolor(r, b, g)
    t.circle(art)
    art += 1

t.penup()
