import sys
import pygame as pg

WIN_WIDTH = 1280
WIN_HEIGHT = 720

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # создаем экран игры разрешением 1280х720px

img = pg.image.load('angry-birds.png')  # загрузить изображение в код
img.convert()  # адаптировать под pygame
img_rect = img.get_rect()  # мы превращаем картинку в игровой объект, у которого есть осязаемые границы
img_rect.center = WIN_WIDTH // 2, WIN_HEIGHT // 2

while True:  # цикл игры
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT] and img_rect.right < WIN_WIDTH:
        img_rect.x += 5
    elif keys[pg.K_LEFT] and img_rect.left > 0:
        img_rect.x -= 5

    screen.fill((255, 255, 255))
    screen.blit(img, img_rect)
    pg.display.update()



