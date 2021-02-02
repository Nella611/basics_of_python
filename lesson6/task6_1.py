"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from itertools import cycle
from time import sleep


class TrafficLight:
    __color__ = ['red', 'yellow', 'green']
    def running(self):
        for color in cycle(self.__color__):
            if color == 'red':
                print(color)
                sleep(7)
            elif color == 'yellow':
                print(color)
                sleep(2)
            else:
                print(color)
                sleep(5)


traffic_light = TrafficLight()
traffic_light.running()


