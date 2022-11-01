# 1 1 2 3 5 8 13
m = 1
n = 1
a = int(input('До какого числа нужен ряд: '))
tbd = 1
print(tbd, end=', ')
while tbd <= a:
    print(tbd, end=', ')
    tbd = m + n
    n = m
    m = tbd


