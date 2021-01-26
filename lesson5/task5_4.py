"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

my_file = 'test.txt'
rus_num = ['Один', 'Два', 'Три', 'Четыре']
en_num = ['One', 'Two', 'Three', 'Four']
with open(my_file) as f:
    for line in f:
        line = line.split()
        line[0]= rus_num[en_num.index(line[0])]
        with open('rus_test.txt', 'a') as new_f:
            new_f.writelines(f'{" ".join(line)}\n')
