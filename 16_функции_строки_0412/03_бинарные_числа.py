def to_binary(n: int) -> str:
    bin = ''
    while n > 0:
        bin = str(n % 2) + bin
        """
        Когда пишем += -> bin = bin + что-то символы вставляются в прямом порядке 
        Когда пишем bin = что-то + bin -> элементы идут в обратном порядке 
        """
        n //= 2
    return bin


def to_decimal(n: str) -> int:
    dec = 0
    for i in range(len(n)):
        if n[len(n) - 1 - i] != '0':
            dec += 2 ** i
    return dec

res = to_binary(15)
res1 = to_decimal('1000000')
print(res)
print(res1)


