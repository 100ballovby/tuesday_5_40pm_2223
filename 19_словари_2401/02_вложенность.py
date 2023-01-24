person = {
    "name": "John",  # пара ключ-значение
    "surname": "Doe",
    "age": 28,
    "city": "Warsaw",
    "phone": {
        "work": "+4765234892",
        "private": "+4236472673",
    },
    "email": ["johndoe@example.com", "johnny@gmail.com"]
}  # словарь

print(person["phone"]["private"])
print(person["email"][1])  # сначала ключ, а потом индекс элемента в списке



