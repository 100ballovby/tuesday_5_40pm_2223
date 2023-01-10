import os
import random as r

phrases = ['Hello, Python', 'You can write files!',
           'C++ the best!', 'Есть пробитие!',
           'Командир контужен! Видимость снижена!']
basedir = 'content'
os.mkdir(f'{basedir}/new_папка')
n_d = f'{basedir}/new_папка'

for i in range(20):
    f_name = f'file_{i}.txt'
    filepath = os.path.join(n_d, f_name)
    with open(filepath, 'w') as file:
        file.write(r.choice(phrases))

