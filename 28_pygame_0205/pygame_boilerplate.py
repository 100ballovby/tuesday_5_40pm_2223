import sys
import pygame as pg

# определим константу смены кадров в игре
FPS = 60
WIN_WIDTH = 1280
WIN_HEIGHT = 720
WHITE = (255, 255, 255)
BLUE = (3, 157, 252)

width = 50
x = WIN_WIDTH - width
y = WIN_HEIGHT // 2

pg.init()  # инициализация pygame
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # создать игровой экран размером 1280ч720 пикселей
clock = pg.time.Clock()  # отвечает за смену кадров в игре


# если необходимо отобразить на экране какие-то объекты до запуска игрового цикла (меню или подобное)
pg.display.update()  # обновляет кадры на экране игры


while True:
    # включаем FPS
    clock.tick(FPS)
    # диспетчер событий
    for event in pg.event.get():  # этот цикл перебирает все события, которые происходят в игре
        if event.type == pg.QUIT:  # если игру закрыли
            sys.exit()  # завершить процесс

    screen.fill(WHITE)  # залить экран белым
    pg.draw.rect(screen, BLUE, [x, y, width, width])

    # в цикле обновляем изображение на экране
    pg.display.update()

    if x >= WIN_WIDTH + width:  # если переменная х стала больше ширины экрана + размер квадрата
        x = 0 - width  # перемещаем квадрат влево
    else:  # иначе
        x += 10  # увеличивать x на 5
