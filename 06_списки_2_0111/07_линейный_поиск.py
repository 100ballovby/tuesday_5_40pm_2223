"""
Линейный поиск
Нужно просматривать каждый элемент списка, сравнивать его
с искомым значением. Если значение найдено, выйти из цикла и вернуть
индекс найденного элемента в списке. Если не нашли, вернуть -1
"""
a = [31, -72, -59, -50, 91, 0, -65, 88, 89, 16, 0, 21, 98, -46, -43, -56, -46, 8, -71, 96, 38]
key = int(input('Что ищем? '))

for i in range(len(a)):
    if key == a[i]:
        print(i)
        break  # принудительная остановка цикла

if key != a[i]:
    print(-1)


