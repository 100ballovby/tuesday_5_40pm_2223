def lines(obj, length, n):
    obj.down()
    obj.lt(90)
    for i in range(n):
        obj.fd(length)
        obj.bk(length)
        obj.rt(90)
        obj.up()
        obj.fd(length / 3)
        obj.lt(90)
        obj.down()


def cross(obj, length):
    obj.down()
    for i in range(4):
        obj.lt(90)
        obj.fd(length)
        obj.rt(90)
        obj.fd(length)
        obj.lt(90)
        obj.fd(length)


def cross_curve(obj, length):
    obj.down()
    for i in range(3):
        obj.fd(length)
        obj.rt(90)
        obj.fd(length)
        obj.lt(90)
        obj.fd(length)
        obj.rt(120)

