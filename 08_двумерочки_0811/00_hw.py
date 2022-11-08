a = []
length = int(input('Длина списка: '))

for i in range(length):  # повторить <length> раз
    n = int(input('Введите число: '))
    a.append(n)

print(a)
maximum = a[0]  # наибольший по умолчанию первый
minimum = a[0]  # наименьший по умолчанию первый
i_max = 0  # индекс максимального элемента
i_min = 0  # индекс минимального элемента
for i in range(1, len(a)):  # повторить <длина_списка> раз
    if a[i] > maximum:  # если элемент массива больше maximum
        maximum = a[i]  # присвоить maximum значение этого элемента массива
        i_max = i  # сохранить индекс элемента
    if a[i] < minimum:  # если элемент массива меньше minimum
        minimum = a[i]   # присвоить minimum значение этого элемента массива
        i_min = i  # сохранить индекс элемента

print('Максимальный:', maximum)
print('Минимальный:', minimum)
a[i_max] = minimum
a[i_min] = maximum
print(a)


