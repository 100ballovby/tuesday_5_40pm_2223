import random as r
from turtle import *

t = Turtle()
t.shape('turtle')
t.speed(0)

colors = ['#fcba03', '#e3cb88', '#80620f', '#ffe7a6',
          '#ffb2a6', '#f5715d', '#7738ff', '#cbb3ff',
          '#615b6e', '#5514e0', '#ff00fb', '#f060ed',
          '#f5113f', '#870721', '#8591ff', '#97f7ea',
          '#e3fffb', '#e3ffe4', '#0af211', '#ffea03']

for i in range(1000):
    x = r.randint(-450, 450)
    y = r.randint(-450, 450)
    d = r.randint(20, 80)
    t.up()
    t.goto(x, y)
    t.down()
    t.color(r.choice(colors))  # цвет черепашки - случайное значение из списка цветов
    t.dot(d)


done()