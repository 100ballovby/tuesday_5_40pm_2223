import random as r
from turtle import *
from logic import square, five_angeled_star, triangle

t = Turtle()
t.shape('turtle')
t.speed(0)
t.color('red')

t.begin_fill()  # начать заливку
five_angeled_star(t, 100, 100, 200)
t.end_fill()  # закончить заливку

for i in range(6):
    triangle(t, -200, -200, 100)
    t.lt(60)

t.goto(200, 200)
for i in range(4):
    t.down()
    t.circle(50)
    t.up()
    t.fd(70)


done()