"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def division(*args):
    num1 = int(input('введите делимое: '))
    num2 = int(input('введите делитель: '))
    if num2 == 0:
        return 'деление на 0!'
    return  num1 / num2

print(division())