sign = input('Введите систему: ').lower()
temperature = float(input('Введите градусы: '))

if sign in 'cс':
    res = 9/5 * temperature + 32
    print(res)
elif sign in 'fаф':
    res = 5/9 * temperature - 32
    print(res)
else:
    print('Неверная система!')
