"""Режимы работы с файлами
r - read - чтение файла
w - write - запись в файл
a - append - добавление (запись) в файл
b - binary - открыть файл в двоичном формате (используется в сочетании - rb, wb)
x - открытие файла, если не существует, будет выброшено исключение
t - text - открыть файл в текстовом режиме (по умолчанию)
+ - комбинация из (r+) чтение+запись
"""
import os
dir = 'content'
filepath = os.path.join(dir, 'pi_million_digits.txt')
# ^ путь к файлу, с которым планируем работать
with open(filepath) as file:  # открыть файл, поместить в переменную и закрыть его после окончания отступа
    lines = file.readlines()  # превратить файл в список строк
    pi_string = ''  # строка, в которой хранится число π
    for i in range(len(lines)):  # перебор списка строк файла
        pi_string += lines[i].strip()  # добавление очищенной от пробелов строки

print(pi_string)
with open(os.path.join(dir, 'copy_pi.txt'), 'w') as file:
    file.write(pi_string)

birth = input('Введите дату рождения ддммгг: ')
print(birth in pi_string)
