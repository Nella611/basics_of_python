"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
user_num = int(input('Введите целое положительное число'))
i = 10
result = user_num % i

while len(str(i)) <= len(str(user_num)):
    user_num = user_num // i
    if user_num % i > result:
        result = user_num % i


print(result)