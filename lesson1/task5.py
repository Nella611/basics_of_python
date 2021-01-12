"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
revenue = int(input('Выручка: '))
costs = int(input('Издержки: '))
if revenue > costs:
    margin = (revenue - costs) / revenue * 10000
    print(f'Ваша фирма прибыльна! Прибыль составила {margin}')
    number_of_employees = int(input('Введите количество ваших сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника составляеь {margin / number_of_employees}')
else:
    print('Вы работаете в убыток')