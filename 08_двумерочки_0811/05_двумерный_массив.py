# дана целочисленная матрица NxM, перебрать элементы
matrix = [
    [3, 4, 2],
    [0, 12, 6],
    [7, 8, 3],
]
n = 3  # строки матрицы
m = 3  # количество элементов в строке матрицы
for line in range(n):  # перебираю строки матрицы
    for elem in range(m):  # перебираю элементы внутри строки
        print(matrix[line][elem], end=' ')
    print()



