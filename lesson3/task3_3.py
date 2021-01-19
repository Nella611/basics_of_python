"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(n1, n2, n3):
    num_list = [n1, n2, n3]
    return sum(num_list) - min(num_list)


print(my_func(2, 5, 10))
