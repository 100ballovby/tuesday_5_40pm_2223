# задача из дз №1
phrase = input('Введи строку: ')

if not len(phrase) < 5:
    print(phrase[:2] + phrase[-2:])
else:
    print('Строка не соответствует условиям')