"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    title = 'blue'
    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки для ручки.')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки для карандаша.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки для маркера.')

a = Stationery()
a.draw()
print(a.title)
b = Pen()
b.draw()
print(b.title)
c = Pencil()
c.draw()
print(c.title)
d = Handle()
d.draw()
print(d.title)