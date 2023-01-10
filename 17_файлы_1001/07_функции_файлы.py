def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data


for i in range(20):
    print(f'Файл №{i}')
    print(read_file(f'content/new_папка/file_{i}.txt'))




