"""
Заменить слово в строке
"""
phrase = input('Введи строку: ')
# .split(sep) - превращает строку в список, делит по сепаратору (пробел)
list_phrase = phrase.split()
print(list_phrase)
list_phrase[0] = 'пока'
print(list_phrase)
# .join(list) - превращает список в строку
new_str = ' '  # символ в строках будет подставлен между элементами списка
print(new_str.join(list_phrase))
