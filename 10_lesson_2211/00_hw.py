import random as r

matrix = []
n = 3
m = 3

for i in range(n):
    line = []
    for j in range(m):
        line.append(r.randint(-10, 10))
    matrix.append(line)

for i in range(n):
    char_line = 0
    for j in range(m):
        if matrix[i][j] < 0 and matrix[i][j] % 2 == 0:
            char_line += matrix[i][j]
        print(matrix[i][j], end="\t")
    print(f'\t|Line {i}: {char_line}')

# Характеристики столбцов
column = 0
for i in range(n):
    char_col = 0
    for j in range(m):
        if matrix[j][i] < 0 and matrix[j][i] % 2 != 0:
            char_col += abs(matrix[j][i])
    column += 1
    print(f'Column {column}: {char_col}')


