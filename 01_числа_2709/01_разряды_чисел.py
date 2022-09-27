num = int(input('Введи трехзначное число: '))

hundreds = num // 100  # разряд сотен
tens = num % 100 // 10  # разряд десятков
units = num % 10  # разряд единиц

print(num, '=', hundreds, 'и', tens, 'и', units)
print(num, '=', hundreds + tens + units)
