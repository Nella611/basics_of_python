"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

try:
    my_file = input('Введите имя файла')
    average_salary = 0
    list_of_less_20 = []
    num_of_employees = 0
    with open(my_file) as f:
        for line in f:
            line = line.split()
            if float(line[1]) < 20000:
                list_of_less_20.append(line[0])
            num_of_employees += 1
            average_salary += float(line[1])
    print(f'Средняя величина дохода сотрудников: {(average_salary/num_of_employees):.2f}')
    print(f'Меньше 20тыс оклад у: {", ".join(list_of_less_20)}')
except FileNotFoundError:
    print('Такого файла не существует')
