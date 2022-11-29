matrix = [
    [2, 9, 13],
    [78, 22, -9],
    [90, 65, 41],
]
n = 3
m = 3
transported_matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
for i in range(n):
    for j in range(m):
        transported_matrix[i][j] = matrix[j][i]

print(transported_matrix)
