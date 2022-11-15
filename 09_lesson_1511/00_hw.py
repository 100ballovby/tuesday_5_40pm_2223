a = 7
while a < 100:
    print(a, end=', ')
    a += 7

print('\nВариант 2')
for i in range(7, 99, 7):
    print(i, end=', ')
print('\n\nВариант 3')
a = [2, 3, 1, 2, 4]
print(a)
print(*a)  # разыменовать

print(*range(7, 100, 7), sep=', ')

