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
