"""
Найти и посчитать количество столбцов, где
есть хотя бы один нулевой элемент.
"""
import random as r

matrix = []
n = r.randint(2, 6)
for i in range(n):
    line = []
    for j in range(n):
        k = r.randint(-5, 5)
        line.append(k)
        print(k, end=', ')
    matrix.append(line)
    print()

col = 0
for line in range(n):  # перебираю строки матрицы
    for elem in range(n):  # перебираю элементы внутри строки
        if matrix[elem][line] == 0:  # если в столбике нашелся один ноль
            col += 1
            break  # выйти из цикла, чтобы не считал лишние нули в столбах
print(col)
