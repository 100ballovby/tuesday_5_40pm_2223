def square(obj, side, x, y, col):
    """
    Функция рисует квадрат черепашкой в определенном месте
    :param obj: черепашка (кто рисует)
    :param side: длина стороны квадрата
    :param x: координата х
    :param y: координата у
    :param col: цвет
    :return: None
    """
    obj.goto(x, y)
    obj.down()
    obj.color(col)
    for i in range(4):
        obj.fd(side)  # функция считает, что у параметра obj эта функция уже есть
        obj.rt(90)
    obj.up()  # при следующем вызове функции перо должно быть поднято


def triangle(obj, side, x, y, col):
    """
    Функция рисует квадрат черепашкой в определенном месте
    :param obj: черепашка (кто рисует)
    :param side: длина стороны квадрата
    :param x: координата х
    :param y: координата у
    :param col: цвет
    :return: None
    """
    obj.goto(x, y)
    obj.down()
    obj.color(col)
    for i in range(3):
        obj.fd(side)  # функция считает, что у параметра obj эта функция уже есть
        obj.lt(120)
    obj.up()  # при следующем вызове функции перо должно быть поднято


def spiral(obj, side, deg, x, y, col):
    """
    Функция рисует квадрат черепашкой в определенном месте
    :param obj: черепашка (кто рисует)
    :param side: длина стороны квадрата
    :param deg: количество градусов поворота
    :param x: координата х
    :param y: координата у
    :param col: цвет
    :return: None
    """
    obj.goto(x, y)
    obj.down()
    obj.color(col)
    for i in range(100):
        obj.fd(side + i * 2)  # функция считает, что у параметра obj эта функция уже есть
        obj.rt(deg)
    obj.up()  # при следующем вызове функции перо должно быть поднято


def spider(obj, length, n):
    obj.down()
    for i in range(n):
        obj.fd(length)
        obj.stamp()  # оставить отпечаток черепашки
        obj.bk(length)

        obj.lt(360 / n)
    obj.up()
