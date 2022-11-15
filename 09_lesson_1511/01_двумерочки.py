import random as r

matrix = []
n = int(input('Строки: '))
m = int(input('Столбцы: '))
for i in range(n):
    string = []
    for j in range(m):
        u = round(r.uniform(1, 10), 3)
        string.append(u)
    matrix.append(string)
print(matrix)

for i in range(n):  # перебираю строки матрицы
    maxi = matrix[i][0]
    mini = matrix[i][0]
    i_max = 0
    i_min = 0
    for j in range(m):
        if matrix[i][j] > maxi:
            maxi = matrix[i][j]
            i_max = j
        if matrix[i][j] < mini:
            mini = matrix[i][j]
            i_min = j
    matrix[i][i_max] = mini
    matrix[i][i_min] = maxi

print(matrix)
