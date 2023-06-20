class LuhnAlgorithm:
    def __init__(self, card_number):
        self.card_number = card_number

    def validate(self):
        card_number = self.card_number.replace(' ', '').replace('-', '')

        if not card_number.isdigit():  # проверяем, что номер карты состоит только из цифр
            return False
        card_number = list(card_number)
        for n in range(0, len(card_number), 2):
            digit = int(card_number[n])  # фиксируем число
            if digit * 2 > 9:
                card_number[n] = digit * 2 - 9
            else:
                card_number[n] = digit * 2
        res = map(int, card_number)  # к каждому элементу списка применить функцию int
        summ = sum(list(res))  # посчитать сумму элементов списка
        return summ % 10 == 0  # вернуть результат проверки кратности 10


v = LuhnAlgorithm('5208130000436505')
print(v.validate())




