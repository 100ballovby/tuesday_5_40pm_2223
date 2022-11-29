import random as r
from turtle import *

t = Turtle()
t.shape('turtle')

# нарисуем квадрат
for i in range(4):
    t.fd(100)
    t.rt(90)

# нарисовать треугольник
for i in range(3):
    t.fd(100)
    t.lt(120)

# нарисуем прямоугольник
for i in range(2):
    t.fd(100)
    t.rt(90)
    t.fd(200)
    t.rt(90)

done()