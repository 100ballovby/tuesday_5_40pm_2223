# получить n и сложить все цифры числа n
n = int(input('Введи n: '))
summ = 0
while n != 0:  # n = 12; n = 1
    summ += n % 10  # 12 % 10 = 2; 1 % 10 = 1
    n //= 10  # 12 // 10 = 1; 1 // 10 = 0
print(summ)

# вариант 1
n = input('Введи n: ')
summ = 0
for i in n:
    summ += int(i)
print(summ)
