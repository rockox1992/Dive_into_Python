"""
Напишите следующие функции:
Нахождение корней квадратного уравнения <br>
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.<br>
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.<br>
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.<br>
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
"""
from math import sqrt
from task_9_1_2 import read_csv
from task_9_1_2 import deco

@deco
def quadratic(*args):
    for ar in args:
        a = int(ar[0])
        b = int(ar[1])
        c = int(ar[2])
        print(a, b, c)
        d = b ** 2 - 4 * a * c
        if d < 0:
            return f'No root'
        elif d == 0:
            x_1 = (- b) / (2 * a)
            return x_1
        elif d > 0:
            x_1 = (- b + sqrt(d)) / (2 * a)
            x_2 = (- b - sqrt(d)) / (2 * a)
            return x_1, x_2


print(quadratic(()))

