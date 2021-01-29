"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

my_file = input('Введите имя файла')
try:
    with open(my_file, 'x') as f:
        my_num = input('Введите числа через пробел: ')
        f.writelines(my_num)
except FileExistsError:
    print('Такой файл уже существует, значения уже введены')
finally:
    with open(my_file) as f_2:
        for line in f_2:
            print(sum([int(x) for x in line.split()]))