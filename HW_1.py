# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint

# объявление переменных
random_list = []
count_number_in_list = 0
bigger_numbers_list = []
smaller_numbers_list = []

length_list = 0
# проверка вводимых данных
while 5 > length_list or 500 < length_list:
    try:
        length_list = int(input('Введите размер массива в диапазоне от 5 до 500: '))
    except ValueError:
        print('Соболезную...')

number_x = 0
while 1 > number_x or 100 < number_x:
    try:
        number_x = int(input('Введите искомое число в диапазоне от 1 до 100: '))
    except ValueError:
        print('Что то пошло не так)')

# создание списка с рандомными числами
for _ in range(length_list):
    random_list.append(randint(1, 100))
print(*random_list)

# поиск максимально близкого по значению числа
for item in random_list:
    if item == number_x:
        count_number_in_list += 1
    elif item > number_x:
        bigger_numbers_list.append(item)
    else:
        smaller_numbers_list.append(item)
else:
    # если такое число есть в списке
    if count_number_in_list > 0:
        print(f'максимально близкое по значению к числу {number_x} = {number_x}')
        print(f'в списке их оказалось {count_number_in_list}')
    # если числа нет в списке
    else:
        max_min_number = max(smaller_numbers_list)
        min_max_number = min(smaller_numbers_list)
        if abs(max_min_number - number_x) > min_max_number - number_x:
            print(f'максимально близкое по значению число: {max_min_number}')
        else:
            print(f'максимально близкое по значению число: {min_max_number}')
