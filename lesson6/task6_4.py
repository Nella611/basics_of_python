"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""



class Car:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'left':
            print('Поворот налево')
        elif direction == 'right':
            print('Поворот направо')

    def show_speed(self, current_speed):
        print(f'Скорость {current_speed} км/ч')

class TownCar(Car):
    def show_speed(self, current_speed):
        super().show_speed(current_speed)
        if int(current_speed) > 60:
            print('Превышение скорости!')


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self, current_speed):
        super().show_speed(current_speed)
        if int(current_speed) > 40:
            print('Превышение скорости!')

class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = True


my_car1 = TownCar('Toyota', 'green', 80)
my_car1.go()
my_car1.stop()
my_car1.turn('left')
my_car1.show_speed(62)
print(my_car1.color)
my_car2 = SportCar('Aston Martin', 'silver', '324')
my_car2.go()
print(my_car2.color)
my_car2.show_speed('300')
my_car3 = WorkCar('RAV4', 'black', 150)
my_car3.show_speed(50)
print(my_car3.name)
print(my_car3.is_police)
my_car4 = PoliceCar('УАЗ', 'gray', 80)
print(my_car4.name)
print(my_car4.is_police)
my_car4.show_speed(100)
