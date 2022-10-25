cars = ['Mercedes', 'Audi', 'BMW']

# .append(obj) - добавляет obj в конец списка
cars.append('Toyota')
cars.append('Ford')
print(cars)
# .insert(index, obj) - добавляет obj на место index
print('Вывожу второй элемент: ', cars[1])
cars.insert(1, 'Porsche')
print(cars)
print('Вывожу второй элемент: ', cars[1])
# .extend(iterable) - вставляет последовательность iterable в конец списка
cars.extend(['Volkswagen', 'Lamborghini', 'LADA', 'GMC'])
print(cars)
# .remove(obj) - удаляет объект object из списка (не по индексу, а по значению)
cars.remove('LADA')
print(cars)
# .pop() - удаляет последний элемент списка
cars.pop()
print(cars)
# .pop(index) - удаляет элемент из списка по индексу
cars.pop(4)
print(cars)

