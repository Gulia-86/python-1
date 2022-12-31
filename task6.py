"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep

class TrafficLight:
    __color = {"red": 7, "yellow": 2, "green": 3}
    def method_running(self):
        for key, value in TrafficLight.__color.items():
            print(key)
            sleep(value)

tr = TrafficLight()
target=tr.method_running()

"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""
class Road:
    _m = 25
    _hight = 5
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def func(self):
        return self.__width * self.__length * self._m * self._hight

r = Road(10, 20)
print(r.func())

"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


ii = Position('Ivan', 'Ivanov', 'worker', {"wage": 10000, 'bonus': 200})
print(ii.get_full_name(), ii.get_total_income())

"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""
class Car:
    _speed = 0
    is_police = False
    _speed_limit = float('inf')

    def __init__(self, color, name):
        self.color = color
        self.name = name
        print(color, name)

    def go(self):
        self._speed += 20
        if self._speed > self._speed_limit:
            print("Превышение скорости")

    def stop(self):
        self._speed = 0
        print(self.name + ' остановилась ')

    def turn(self, direction):
        print(self.name + ' повернула ' + direction)

    def show_speed(self):
        print(self.name + ' скорость: ' + str(self._speed))


class TownCar(Car):
    _speed_limit = 60


class SportCar(Car):
    _speed_limit = 120


class WorkCar(Car):
    _speed_limit = 40


class PoliceCar(Car):
    is_police = True


car = TownCar('white', 'Jeep')
car.go()
car.show_speed()
car.go()
car.show_speed()
car.go()
car.show_speed()
car.go()
car.show_speed()
car.turn('right')
car.stop()

car = WorkCar('black', 'Лада Калина')
car.go()
car.show_speed()
car.go()
car.show_speed()
car.go()
car.show_speed()
car.turn('left')
car.stop()
"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    title = "канцелярская принадлежность"

    def draw(self):
        print("Запуск отрисовки")

class Pen:
    title = 'Pen'

    def draw(self):
        print(self.title + ' ручка')


class Pencil:
    title = 'Pencil'

    def draw(self):
        print(self.title + ' карандаш')


class Handle:
    title = 'Handle'

    def draw(self):
        print(self.title + ' маркер')


Pen().draw()
Pencil().draw()
Handle().draw()