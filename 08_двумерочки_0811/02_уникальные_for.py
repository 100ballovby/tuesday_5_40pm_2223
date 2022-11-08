import random as r

a = []
for i in range(10):
    n = r.randint(1, 10)
    if n not in a:
        a.append(n)

print(a)
