"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

with open('firms') as f:
    firms_dict = {}
    average_profit = 0
    ind = 0
    for line in f:
        line = line.split()
        firm = line[0]
        proceeds = int(line[2])
        costs = int(line[3])
        firms_dict[firm] = proceeds - costs
        if proceeds>costs:
            ind += 1
            average_profit += proceeds - costs


list_of_firms = [firms_dict, {'average_profit': int(average_profit/ind)}]

with open('my_file.json', 'w') as f_json:
    json.dump(list_of_firms, f_json)

