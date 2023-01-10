import os
dir = 'content'
filepath = os.path.join(dir, 'pi_digits.txt')
# ^ путь к файлу, с которым планируем работать
with open(filepath) as file:  # открыть файл, поместить в переменную и закрыть его после окончания отступа
    print(file.read())  # прочитать файл

