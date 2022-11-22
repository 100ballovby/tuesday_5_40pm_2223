import random as r

matrix = []
n = 4
m = 4

for i in range(n):
    line = []
    for j in range(m):
        line.append(r.randint(-10, 10))
    matrix.append(line)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end="\t")
    print()

summ = 0
mult = 1
for i in range(n):
    summ += matrix[i][i]
    mult *= matrix[i][n - i - 1]
print(f'Сумма главной диагонали: {summ}')
print(f'Произведение побочной диагонали: {mult}')
