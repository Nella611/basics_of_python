"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, list_of_list):
        self.matrix = list_of_list

    def __str__(self):
        l = ''
        for line in self.matrix:
            for num in line:
                if len(str(num)) > len(l):
                    l = str(num)
        l = len(l)
        line_m = ''
        for line in self.matrix:
            for num in line:
                line_m += f'{num: >{l+2}}'
            line_m += '\n'
        return f'{line_m[:-1]}'

    def __add__(self, other):
        new_matrix = []
        try:
            for i, num in enumerate(other.matrix):
                l = []
                for j, num2 in enumerate(num):
                    l.append(other.matrix[i][j] + self.matrix[i][j])
                new_matrix.append(l)
            return  Matrix(new_matrix)
        except IndexError:
            return 'матрицы не совпадают по размеру'



a = [[31, 22], [37, 43], [51, 86]]
b = [[3, 5, 32], [2, 4, 6], [-1, 64, 8]]
c = [[3, 5, 8, 3], [8, 3, 7, 1]]
d = [[3, 5, 8, 3], [-8, -3, -7, -1]]


m1 = Matrix(a)
m2 = Matrix(b)
m3 = Matrix(c)
m4 = Matrix(d)
print(m1)
print(m2)
print(m3)
print(m3.__add__(m1))
print(m3.__add__(m4))



