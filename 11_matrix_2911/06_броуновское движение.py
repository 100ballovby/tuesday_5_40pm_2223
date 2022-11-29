import random as r
from turtle import *

t = Turtle()
n = Turtle()
t.shape('turtle')
t.speed(0)
t.pensize(4)  # размер пера черепашки
n.shape('turtle')
n.speed(0)
n.pensize(4)  # размер пера черепашки
bgcolor('#000000')  # цвет фона
t.color('#ffffff')
n.color('#f0f0f0')
for i in range(1000):
    t.fd(r.randint(-30, 30))
    t.lt(r.randint(-180, 180))
    n.fd(r.randint(-30, 30))
    n.lt(r.randint(-180, 180))

done()