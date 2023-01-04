def check_palin(string: str) -> bool:
    return string[::].lower() == string[::-1].lower()


def check_palin2(string: str) -> bool:
    is_palin = True
    string = string.lower()  # привести все слово в нижний регистр для безопасности 
    for i in range(len(string)):
        start = string[i]  # буква в начале строки
        end = string[len(string) - 1 - i]  # буква в конце строки
        if start != end:  # если буквы не совпали
            is_palin = False  # слово не палиндром
            break   # выйти из цикла
    return is_palin


print(check_palin2('мама'))
print(check_palin2('шалаш'))
