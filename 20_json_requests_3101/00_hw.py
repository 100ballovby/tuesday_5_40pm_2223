def make_list_from_file(file):
    with open(file, "r") as file:
        content = file.read().split()
    for i in range(len(content)):  # не обязательно
        content[i] = int(content[i])  # превращаем каждое число в int
    return content

print(make_list_from_file("hw.txt"))


