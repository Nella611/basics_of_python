"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road:

    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def mass_of_asphalt(self, thickness=1, mass_of_asphalt_to_km=25):
        mass_of_asphalt = self._length * self._width * mass_of_asphalt_to_km * thickness
        print(f'{int(mass_of_asphalt/1000)} тонны')

my_road = Road(20, 5000)
my_road.mass_of_asphalt()
my_road.mass_of_asphalt(5)