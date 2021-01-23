"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def addition():
    sum_all_nums = 0
    ind = True
    while ind:
        nums_list = input('введите числа через пробел или Q для выхода: ').split()
        for i in nums_list:
            if i.upper() == 'Q':
                ind = False
                break
            try:
                float(i)
            except ValueError:
                print(f'{i}  это не число')
            else:
                sum_all_nums += float(i)
        print(sum_all_nums)
    return sum_all_nums


addition()
