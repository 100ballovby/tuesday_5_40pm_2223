# проверить принадлежность числа промежутку [5;15]
a = int(input('Введи число: '))

# вложенные условия (это зло)
if a > 5 and a < 15:
    print(a, 'принадлежит')
else:
    print(a, 'не принадлежит')

# упрощение условия
if 5 < a < 15:
    print(a, 'принадлежит')
else:
    print(a, 'не принадлежит')

