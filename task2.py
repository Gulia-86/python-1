"""
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки
типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно
не запрашивать у пользователя, а указать явно, в программе.
"""
elements = ["string", 100, 42.5, True, ['a', 'b', 'c']]
print(elements)
for element in elements:
    print(element, type(element))
"""
2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения
списка элементов нужно использовать функцию input().
"""
list = []
for element in range(int(input('Введите количество элементов списка: '))):
    list.append(input('Введите значение: '))
print(list)

for el in range(0, len(list)-1, 2):
    list[el], list[el+1] = list[el+1], list[el]
print(list)
"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
"""
month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_dict = {"Январь": 1, "Февраль": 2, "Март": 3, "Апрель": 4, "Май": 5, "Июнь": 6, "Июль": 7, "Август": 8,
              "Сентябрь": 9, "Октябрь": 10, "Ноябрь": 11, "Декабрь": 12}

month = int(input('Введите номер месяца:'))
print("Вывод времени года через list")
if month in month_list[:2] or month == month_list[11]:
    print('Зима')
elif month in month_list[2:5]:
    print('Весна')
elif month in month_list[5:8]:
    print('Лето')
elif month in month_list[8:11]:
    print('Осень')
else:
    print('Введено неверное число месяца')

print("Вывод времени года через dict")
if month == month_dict.get('Январь') or month == month_dict.get('Февраль') or month == month_dict.get("Декабрь"):
    print('Зима')
elif month == month_dict.get('Май') or month == month_dict.get("Март") or month == month_dict.get("Апрель"):
    print('Весна')
elif number == month_dict.get("Июнь") or month == month_dict.get("Июль") or month == month_dict.get("Август"):
    print('Лето')
elif month == month_dict.get("Сентябрь") or month == month_dict.get("Октябрь") or month == month_dict.get("Ноябрь"):
    print('Осень')
else:
    print('Введено неверное число месяца')

"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.
"""
edd_str = str(input('Введите несколько слов, разделённых пробелами: '))
list = edd_str.split()
for num, value in enumerate(list, 1):
    print(num, value[:10])
"""
5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""
element = int(input("Введите число: "))
my_list = [7, 5, 3, 3, 2, element]
print(my_list)
my_list.sort(reverse=True)
print(my_list)




