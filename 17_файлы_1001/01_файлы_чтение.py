import os
dir = 'content'
filepath = os.path.join(dir, 'pi_digits.txt')
# ^ путь к файлу, с которым планируем работать
file = open(filepath)  # открыть файл для работы
print(file.read())  # прочитать файл 
file.close()  # закрыть доступ к файлу
