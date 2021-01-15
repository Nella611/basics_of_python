"""
6. Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""


def input_products():
    data_structure = list()
    index = 1
    while True:
        product = input('Введите наименование товара или Esc для выхода: ')
        if product == 'Esc':
            break
        price = int(input('Введите цену товара'))
        quantity = int(input('Введите количество товара'))
        unit = input('Введите единицу измерения товара')
        product_set = {'название': product, 'цена': price, 'количество': quantity, 'eд': unit}
        product_tuple = (index, product_set)
        data_structure.append(product_tuple)
        index += 1
    print(data_structure)
    return data_structure


def products_analytics(product_list):
    message = input('Введите категорию для аналитики или all для аналитики всех параметров: ')
    if message == 'all':
        product_analytics = {}
        for i in product_list:
            item_position = i[1]
            for key in item_position:
                if i[0] == 1:
                    product_analytics[key] = [item_position[key]]
                else:
                    product_analytics[key].append(item_position[key])
    elif message in product_list[0][1]:
        product_analytics = {}
        for j in range(len(product_list)):
            for value in product_list[j][1]:
                if j == 0 and message == value:
                    product_analytics[message] = [product_list[j][1][message]]
                elif message == value:
                    product_analytics[message].append(product_list[j][1][message])
    else:
        return print('Такой категории не существует')
    print(product_analytics)
    return product_analytics


products_analytics(input_products())
