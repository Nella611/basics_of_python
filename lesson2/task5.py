"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""


def rating(rating_list):
    while True:
        user_num = input('Введите место в рейтинге: ')
        if user_num == 'Esc':
            break
        user_num = int(user_num)
        if user_num in rating_list:
            rating_list.insert(rating_list.index(user_num)+rating_list.count(user_num), user_num)
        else:
            for i in range(len(rating_list)):
                if user_num > rating_list[i]:
                    rating_list.insert(i, user_num)
                    break
                else:
                    if i == len(rating_list) - 1:
                        rating_list.append(user_num)
                    pass
    print(rating_list)


my_list = [7, 5, 3, 3, 2]
rating(my_list)
