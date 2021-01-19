"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
# через list с проверкой на корректный ввод


def what_season():
    winter = ['12', '1', '2']
    spring = ['3', '4', '5']
    summer = ['6', '7', '8']
    autumn = ['9', '10', '11']
    user_month = input('Введите число от 1 до 12: ')
    if user_month in winter:
        print('Время года зима')
    elif user_month in spring:
        print('Время года весна')
    elif user_month in summer:
        print('Время года лето')
    elif user_month in autumn:
        print('Время года осень')
    else:
        print('Вы ввели некорректное значение')
        what_season()


what_season()


#через dict без проверки на некорректный код

season = {'зима': ['12', '1', '2'],
          'осень': ['9', '10', '11'],
          'лето': ['6', '7', '8'],
          'весна': ['3', '4', '5']}


def what_season2():
    user_month = input('Введите число от 1 до 12: ')
    for key in season:
        if user_month in season[key]:
            print(f'Время года {key}')
            break


what_season2()

