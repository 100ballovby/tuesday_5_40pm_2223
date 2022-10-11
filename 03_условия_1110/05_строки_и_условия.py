phrase = input('Введи фразу: ')
symbol = input('Введи символ: ')

if symbol in phrase:
    print('Символ в строке: ', symbol in phrase)
    print('Индекс символа: ', phrase.index(symbol))
else:
    print(symbol, '- отсутствует')