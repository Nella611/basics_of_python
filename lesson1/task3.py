"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
user_num = int(input('Введите число от 1 до 9: '))
sum_result = user_num * 3 + user_num * 10 * 2 + user_num * 100

print(sum_result)
