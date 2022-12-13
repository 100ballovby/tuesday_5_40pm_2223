import random as r
from turtle import *


def x_angle(obj, x, y, length, n):
    obj.up()
    obj.goto(x, y)
    obj.down()
    for i in range(n):
        obj.fd(length)
        obj.lt(180 - (n - 2) * 180 / n)
        #obj.lt(360 / n)

t = Turtle()
t.shape('turtle')
t.speed(0)

x_angle(t, 100, 100, 50, 3)
x_angle(t, -100, -100, 50, 4)
x_angle(t, 200, 200, 50, 5)
x_angle(t, -200, -200, 50, 7)

done()
