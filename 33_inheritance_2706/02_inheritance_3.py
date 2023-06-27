"""
Виды наследования:
1. Просто наследование подклассом атрибутов родительского класса
2. Полное переопределение в дочернем классе методов родительского класса (переписывание god-object'а)
3 (+). Расширение в дочернем классе методов родителя
"""


class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        #Table.__init__(self, l, w, h)  # вызов создания экземпляра класса СТОЛ внутри класса КУХОННЫЙ СТОЛ
        super().__init__(l, w, h)  # теперь класс-родитель является суперклассом
        # в случае использования super() передача self не нужна, потому что метод вызывается не как функция
        self.places = p  # расширение методов класса-родителя


t1 = KitchenTable(100, 90, 100, 5)
