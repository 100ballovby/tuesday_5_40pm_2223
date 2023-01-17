def task_10_1(path):
    with open(path) as file:
        # print(file.read())  <- прочитать весь файл
        lines = file.readlines()
        arr = []
        for line in lines:
            arr.append(line)
    print(arr)


def task_10_2(path):
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace('Python', 'C++')
            print(line)

task_10_2('learning_python.txt')