import random as r
from turtle import *
from logic import square, triangle, spiral, spider  # импортирую функцию square из файла logic

t = Turtle()
t.shape('turtle')
t.up()
t.speed(0)
square(t, 100, -200, -150, 'red')  # вызов функции
triangle(t, 100, -200, -150, 'red')
square(t, 80, -310, -200, 'blue')
triangle(t, 80, -310, -200, 'blue')
square(t, 30, 100, 100, 'green')
triangle(t, 30, 100, 100, 'green')

for i in range(10):
    triangle(t, 50, 100, 100, 'violet')
    t.lt(36)

spiral(t, 10, 130, -100, -100, 'blue')
spider(t, 150, 100)

q = int(input('Введите количество квадратов: '))
side = 100
x = 0
for i in range(q):
    square(t, side, x, 0, 'red')
    t.fd(side)  #  переходим вперед на сторону квадрата, чтобы нарисовать следующий
    x += side  # увеличиваем x (точку начала рисования квадрата) на длину стороны

done()
