"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ""
        for row in self.matrix:
            for column in row:
                result += str(column) + " "
            result += "\n"
        return result

    def __add__(self, added_matrix):
        new_matrix = list(self.matrix);
        for i, row in enumerate(new_matrix):
            for j, column in enumerate(row):
                new_matrix[i][j] = column + added_matrix.matrix[i][j]
        return Matrix(new_matrix)


m1 = Matrix([[31, 32, 0], [37, 43, 0], [51, 86, 0]])
print("Матрица М1\n", m1)
m2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print("Матрица М2\n", m2)
print("Сумма m1 + m2\n", m1 + m2)


2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани. Проверить на практике
полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
class Clothes(ABC):
    @abstractmethod
    def calculate(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def calculate(self):
        #(V/6.5 + 0.5)
        return self.size / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def calculate(self):
        #(2*H + 0.3)
        return 2 * self.height + 0.3


coat = Coat(42)
suit = Suit(160)
print(f"общий подсчет расхода ткани для пальто: {round(suit.calculate, 2)}")
print(f"общий подсчет расхода ткани для костюма: {round(coat.calculate, 2)}")

"""

from abc import ABC, abstractmethod
#3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
#В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
class Cell():
    def __init__(self, size):
        self.size = size
#В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__())
#Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
    def __add__(self, added):
        return Cell(self.size + added.size)
# вычитание (__sub__())  Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
# нуля, иначе выводить соответствующее сообщение.
    def __sub__(self, subtrahend):
        result = self.size - subtrahend.size
        if result > 0:
            return Cell(result)
        else:
            return "Результат меньше 0"
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
    def __mul__(self, multiply):
        return Cell(self.size * multiply.size)
#Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
    def __truediv__(self, division):
        if division.size == 0:
            return "Не делится"
        else:
            return Cell(self.size // division.size)

    def __str__(self):
        return str(self.size)

    def make_order(self, row_size):
        result = ""
        for i in range(self.size):
            result += "*"
            if (i + 1) % row_size == 0:
                result += "\n"
        return result
"""
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
"""


cell1 = Cell(4)
cell2 = Cell(14)
print(f"Сложение: {cell1} + {cell2} =", cell1 + cell2)
print(f"Вычитание: {cell1} - {cell2} =", cell1 - cell2)
print(f"Умножение: {cell1} * {cell2} =", cell1 * cell2)
print(f"Деление: {cell1} / {cell2} =", cell1 / cell2)
print(cell2.make_order(5))