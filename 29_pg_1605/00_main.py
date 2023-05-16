import sys
import pygame as pg
from pygame.examples.stars import WINSIZE

WIN_WIDTH = 1280
WIN_HEIGHT = 720

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (252, 186, 3)
WHITE = (255, 255, 255)

LEFT = 'left'
RIGHT = 'right'
STOP = 'stop'
motion = STOP

# персонаж
r = 30
x = WIN_WIDTH // 2
y = WIN_HEIGHT // 2

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # создаем экран игры разрешением 1280х720px

screen.fill(WHITE)

while True:  # цикл игры
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()  # отслеживание клавиатуры
    pressed = pg.mouse.get_pressed()  # отслеживание мыши
    pos = pg.mouse.get_pos()  # отслеживание координат, в которых находится курсор

    if keys[pg.K_LEFT]:  # pg.K_a | когда кнопка нажимается, ее статус меняется на true
        motion = LEFT
    elif keys[pg.K_RIGHT]:  # pg.K_d
        motion = RIGHT
    else:
        motion = STOP

    pg.draw.circle(screen, RED, (x, y), r)

    if motion == LEFT and x > 0:
        x -= 5
    elif motion == RIGHT and x < WIN_WIDTH:
        x += 5


    if pressed[0]:  # если нажата ЛКМ
        pg.draw.circle(screen, BLUE, pos, 20)
    elif pressed[2]:  # если нажата ПКМ
        pg.draw.circle(screen, ORANGE, pos, 20)
        pg.draw.rect(screen, GREEN, [pos[0] - 10, pos[1] - 10, 20, 20])
    elif pressed[1]:  # если нажато колесо мыши
        screen.fill(WHITE)

    pg.display.update()
