"""
Программа загадывает пользователю число от 1 до 100. И предлагает
ему угадать это число. Если пользователь вводит число, которое меньше
загаданного, нужно вывести "Мое число меньше", если больше - вывести
"Мое число больше". Продолжать работу, пока пользователь не угадает
загаданное число.
"""
import random as r

secret = r.randint(1, 100)
print('Я загадал число от 1 до 100, угадай его.')
guess = 0  # число, которое угадывает пользователь
attempts = 0  # количество попыток

while guess != secret and attempts <= 7:
    attempts += 1
    guess = int(input('Введите число: '))
    if secret < guess:
        print('Мое число меньше!')
    if secret > guess:
        print('Мое число больше!')

if guess == secret:
    print('Молодец! Попытки: ', attempts)
else:
    print('Я загадал число ', secret)