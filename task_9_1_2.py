"""
Напишите следующие функции:
Нахождение корней квадратного уравнения <br>
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.<br>
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.<br>
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.<br>
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
"""
# ЛУЧШИЙ САМОУЧИТЕЛЬ https://metanit.com/python/tutorial/2.28.php
import csv
import random
import json
from typing import Callable


def gen_random_1000():
    """Генерация рандомных чисел от -1000 до 1000"""
    nums = random.randint(-1000, 1000)
    return nums


def gen_rand_csv():
    # Для очистки файла
    with open('quadro.csv', 'w', ) as f:
        f.seek(0)

    count = 1
    while count < random.randint(100, 1001):
        a = str(gen_random_1000())
        b = str(gen_random_1000())
        c = str(gen_random_1000())
        count += 1
        list_a_b_c = [a, b, c]
        # Для проверки, закоментировать при сдаче!
        # print(*enumerate(list_a_b_c, start=count))
        # Построчная запись
        with open('quadro.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(list_a_b_c)
    return None


def read_csv():
    with open('quadro.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for i in reader:
            a = i[0]
            b = i[1]
            c = i[2]
            yield a, b, c


def deco_list(func: Callable):
    def wrapper(*args, **kwargs):
        func(*read_csv())

    return wrapper


def deco_json(func: Callable):
    def wrapper(*args):
        dct_num = []
        dct_result = []
        dct_f = {}
        count_result = 0
        count_num = 0

        for result in func(*args):
            count_result += 1
            dct_result.append([f'result {count_result} {result}'])

        for num in args:
            count_num += 1
            dct_num.append([f'num {count_num} {num}'])

        dct_result = list(zip(dct_num, dct_result))  # Должен быть проще способ.

        for i in dct_result:
            dct_f.update(dict(zip(i[0], i[1])))

        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(dct_f, f, indent=2)

    return wrapper
