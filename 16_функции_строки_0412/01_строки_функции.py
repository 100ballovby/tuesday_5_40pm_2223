def length(iterable: iter) -> int:
    """
    Функция измеряет длину объекта iterable
    :param iterable: последовательность (итерабельная)
    :return: число-длина
    """
    counter = 0
    for elem in iterable:  # перебирая каждый элемент из объекта
        counter += 1  # увеличивать счетчик на единицу
    return counter

obj = input('Введите что-то: ')
print(f'Длина {obj} = {length(obj)}')
print(length([4, 5, 2, 1, 7, 8]))

