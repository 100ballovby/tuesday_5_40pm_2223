import random as r
from turtle import *
from logic import square

t = Turtle()
t.shape('turtle')
t.speed(0)

x = 0
y = 0
zh = 10

for i in range(10):
    zh += 20
    x -= 10
    y -= 10
    square(t, x, y, zh)

done()