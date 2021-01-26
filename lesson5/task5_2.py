"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

try:
    my_file = input('Введите имя файла: ')
    num_lines = 0
    num_words = 0
    with open(my_file) as f:
        for line in f:
            num_lines += 1
            num_words += len(line.split())
    print(f'Количество строк: {num_lines}')
    print(f'Количество слов: {num_words}')
except FileNotFoundError:
    print('Такого файла не существует')
