def sum_num(path):
    with open(path) as file:
        lines = file.readlines()  # список со строками из файла
        summary = 0  # здесь считаем сумму чисел
        for line in lines:
            line = line.strip().split(' ')  # превратить строку из файла в список чисел, разделитель - пробел
            for num in line:  # перебираю значения из списка line (сами числа)
                summary += eval(num)  # преобразую число в правильный тип и суммирую
    return summary

res = sum_num('matrix.txt')
print(res)  # вывеси сумму всех чисел в файле с матрицей



