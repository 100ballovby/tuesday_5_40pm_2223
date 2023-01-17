import random as r


def create_array(size, start, stop):
    arr = []
    for i in range(size):
        arr.append(r.randint(start, stop))
    return arr


def array_to_file(arr, size, path):
    with open(path, 'a') as file:
        for i in range(size):
            file.write(str(arr[i]) + ' ')
        file.write('\n')


array1 = create_array(40, -100, 100)
array2 = create_array(40, -100, 100)
array3 = create_array(40, -100, 100)

array_to_file(array1, 40, 'sample.txt')
array_to_file(array2, 40, 'sample.txt')
array_to_file(array3, 40, 'sample.txt')



