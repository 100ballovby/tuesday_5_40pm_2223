person = {
    "name": "John",  # пара ключ-значение
    "surname": "Doe",
    "age": 28,
    "city": "Warsaw",
}  # словарь

for key in person.keys():  # перебрать все ключи словаря person
    print(key)
    # print(person[key])  <- можно получить значения, обращаясь по ключам в переборе ключей словаря

print(len(person))  # вывести количество пар ключ-значения

for value in person.values():  # перебрать все значения словаря person
    print(value)

for key, value in person.items():  # перебрать одновременно ключи и значения словаря
    print(f'Key: "{key}", value: "{value}";')
