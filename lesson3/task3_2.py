"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(name, surname, year_of_birth, city, email, phone, **kwargs):
    """
    :param name: имя
    :param surname: фамилия
    :param year_of_birth: год рождения
    :param city: город проживания
    :param email: электронная почта
    :param phone: телефон
    :param kwargs: можно добавить параметры
    :return: информацию одной строкой
    """
    print(name, surname, year_of_birth, city, email, phone, **kwargs)

user_data(city='kaliningrad', name='Nella', surname='-', year_of_birth=1985, email='nella611@ya.ru', phone=123)