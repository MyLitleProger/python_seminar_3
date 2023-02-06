# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков
#
#     Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#     Будем считать, что на вход подается только одно слово, которое содержит либо
#     только английские, либо только русские буквы.

import re

dict_ru = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10
}
dict_en = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

while True:
    try:
        word = input('Введите слово: ')
        score = 0
        if word.isalpha():
            word = word.upper()
            # работа с кириллицей
            if re.search('[\u0400-\u04FF]', word) and not re.search('[a-zA-Z]', word):
                for item_word in word:
                    for item_dict_ru in dict_ru:
                        if str(item_word) == str(item_dict_ru):
                            score += dict_ru.get(item_dict_ru, 0)
                print(f'Слово - {word}')
                print(f'Стоимость слова: {score}')
                break
            # работа с латиницей
            elif re.search('[a-zA-Z]', word) and not re.search('[\u0400-\u04FF]', word):
                for item_word in word:
                    for item_dict_en in dict_en:
                        if str(item_word) == str(item_dict_en):
                            score += dict_en.get(item_dict_en, 0)
                print(f'Слово - {word}')
                print(f'Стоимость слова: {score}')
                break
            # если присутствует и кириллица и латиница
            else:
                print('Смешанный алфавит!')
                print('Введите символы только кириллицы или латиницы')
        # если присутствуют недопустимые символы
        else:
            print('Введите символы только кириллицы или латиницы')
    # не знаю что нужно сделать что бы вызвать это!
    except ValueError:
        print('Ошибка')
