# n: int - функция ожидает параметр n целочисленного типа
# -> int - ожидается, что функция вернет целое число
def power(n: int, exp: int) -> int:
    return n ** exp


def division(a: int, b: int) -> float:
    try:  # попытайся
        return a / b  # вернуть результат деления a на b
    except ZeroDivisionError:  # в случае деления на 0
        return 0


def multiply(a: int, b: int) -> int:
    return a * b


action = input('Choose action: **, /, *: ')
n1 = int(input('Number 1: '))
n2 = int(input('Number 2: '))

if action == '**':
    res = power(n1, n2)
    print(res)
elif action == '/':
    res = division(n1, n2)
    print(res)
elif action == '*':
    res = multiply(n1, n2)
    print(res)
else:
    print('Некорректное действие')



