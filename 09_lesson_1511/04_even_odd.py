matrix = [
    [4, -2, -5, 7],
    [-2, -9, -3, 1],
    [10, 8, -1, 7],
    [8, -10, 7, -10],
    [8, -10, -9, -6]
]

for i in range(0, len(matrix), 2):  # перебираю ТОЛЬКО четные строки матрицы
    summ = 0
    for j in range(3):  # перебираю элементы строки
        summ += matrix[i][j]  # суммирую все элементы между собой
    print('Строка', i, 'сумма:', summ)