"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import abstractmethod

class Dress:
    def __init__(self, H):
        self.param = H

    @abstractmethod
    def calc_cloth(self):
        pass

    def __add__(self, other):
        return Dress(self.param.calc_cloth() + other.param.calc_cloth())

class Coat(Dress):
    @property
    def calc_cloth(self):
        return round((self.param/6.5 + 0.5), 2)


class Suit(Dress):
    @property
    def calc_cloth(self):
        return 2 * self.param + 0.3

my_dress = Coat(5)
my_suit = Suit(10)
print(my_suit)
print(my_dress.calc_cloth)
print(my_suit.calc_cloth)
print(my_suit.calc_cloth + my_dress.calc_cloth)