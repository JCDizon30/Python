from turtle import *

bgcolor('black')
speed(0)
hideturtle()

for i in range(120):
    color('#FF9933')
    circle(100)
    color('#FFFFFF')
    circle(80)
    color('blue')
    circle(50)
    right(3)
    forward(3)
done()

import turtle
import colorsys
t = turtle.Turtle()
t.screen.bgcolor("black")
t.penup()
t.goto(-200,-100)
t.pendown()
t.speed(10)
a=400
h=0
n=100
def triangle():
    global a,n,h
    for i in range(40):
        c = colorsys.hsv_to_rgb(h,1,0.6)
        h=h+(1/n)
        t.color(c)
        t.forward(a)
        t.left(120)
        a=a-10
triangle()
triangle()
t.hideturtle()
turtle.done()


import turtle
import colorsys
t = turtle.Turtle()
t.screen.bgcolor("black")
t.speed(0)
h=0
n=36
for i in range(40):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h+=1/n
    t.color(c)
    t.left(145)
    for i in range(5):
        t.forward(300)
        t.left(150)
turtle.done()



