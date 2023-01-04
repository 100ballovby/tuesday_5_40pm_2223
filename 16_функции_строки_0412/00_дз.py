def power(a: int, n: int) -> int:
    p = 1
    for i in range(abs(n)):
        p *= a
    if n < 0:
        return 1 / p
    else:
        return p


print(power(10, -1))


