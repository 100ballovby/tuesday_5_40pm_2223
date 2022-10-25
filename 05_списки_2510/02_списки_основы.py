my_list = []  # объявление списка
print(type(my_list))  # <class 'str'>
numbers = [2, 4, 1, 6, 7, 12, 8]  # инициализация

numbers[1] = 3 * 2 ** 8 // 10 * 5
print(numbers)
print(numbers[:3])
print(numbers[-3:])
print(numbers[2:5])
new_numbers = numbers[2:5]
print(new_numbers)

# котрежное присваивание
first_4, other = numbers[:5], numbers[4:]
print(first_4)
print(other)


