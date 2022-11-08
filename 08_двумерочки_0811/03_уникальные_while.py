import random as r

a = []
l = 20
# нужно наполнить список элементами, которые не будут повторяться
while len(a) < l:
    n = r.randint(1, l)
    if n not in a:
        a.append(n)


print(a)

