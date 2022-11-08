import random as r

n = int(input('Строки матрицы: '))
m = int(input('Столбцы матрицы: '))
matrix = []
for i in range(n):  # повторить n раз
    line = []  # создать пустую строку матрицы
    for j in range(m):  # повторить m раз
        line.append(r.randint(1, 100))  # добавить в строку элемент
    matrix.append(line)  # добавить в матрицу строку

print(matrix)


