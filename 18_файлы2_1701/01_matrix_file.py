import random as r


def create_matrix(n, m, start, stop):
    matrix = []
    for i in range(n):
        line = []
        for j in range(m):
            line.append(r.randint(start, stop))
        matrix.append(line)
    return matrix


def matrix_to_file(matrix, n, m, path):
    with open(path, 'w') as file:
        for i in range(n):
            for j in range(m):
                file.write(str(matrix[i][j]) + ' ')
            file.write('\n')

mtrx = create_matrix(5, 5, -100, 100)
matrix_to_file(mtrx, 5, 5, 'matrix.txt')



