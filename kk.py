import random as r

num = r.randint(1000, 9999)
thousands = num // 1000
hundreds = num % 1000 // 100  # разряд сотен
tens = num % 100 // 10  # разряд десятков
units = num % 10  # разряд единиц

print(num)
print(thousands, hundreds, tens, units)
