"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
import copy


def change_list(list):
    new_list = copy.deepcopy(list)
    if len(new_list) > 1:
        for i in range(0, len(new_list), 2):
            if i == len(new_list) - 1:
                break
            else:
                new_el = new_list[i]
                new_list[i] = new_list[i + 1]
                new_list[i + 1] = new_el
    return new_list


def create_list():
    answer = True
    user_list = []
    while answer:
        user_answer = input('введите значение нового элемента списка или Esc для выхода: ')
        if user_answer == 'Esc':
            answer = False
        else:
            user_list.append(user_answer)
    return change_list(user_list)


print(create_list())
