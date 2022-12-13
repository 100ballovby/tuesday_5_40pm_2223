def square(obj, x, y, length):
    obj.up()
    obj.goto(x, y)
    obj.down()
    for i in range(4):
        obj.fd(length)
        obj.lt(90)
    obj.up()


def five_angeled_star(obj, x, y, length):
    obj.up()
    obj.goto(x, y)
    obj.down()
    for i in range(5):
        obj.fd(length)
        obj.rt(144)
    obj.up()

def triangle(obj, x, y, length):
    obj.up()
    obj.goto(x, y)
    obj.down()
    for i in range(3):
        obj.fd(length)
        obj.lt(120)
    obj.up()
