"""
Напишите следующие функции:
Нахождение корней квадратного уравнения <br>
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.<br>
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.<br>
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.<br>
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
"""
import csv
import random
import json
from math import sqrt
from typing import Callable

def gen_random_1000():
    """Генерация рандомных чисел от -1000 до 1000"""
    nums = random.randint(-1000, 1000)
    return nums


def gen_rand_csv():
    # Для очистки файла
    with open('quadro.csv', 'w',) as f:
        f.seek(0)

    count = 1
    while count < random.randint(100, 1001):
        a = str(gen_random_1000())
        b = str(gen_random_1000())
        c = str(gen_random_1000())
        count += 1
        list_a_b_c = [a, b, c]
        # Для проверки, закоментировать при сдаче!
        #print(*enumerate(list_a_b_c, start=count))
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
    with open(f'{func.__name__}.json', 'w') as f:
        final_dict = json.load(f)

    def wrapper(*args, **kwargs):
        for result in func(*args, **kwargs):
            if result:
                dct = {'value': args, 'result': result}
                final_dict = json.load(dct)
            with open(f'{func.__name__}.json', 'w') as f:
                json.dump(final_dict, f, indent=2)

    return wrapper


#@deco_json
@deco_list
def quadratic(*args):
    for ar in args:
        a = int(ar[0])
        b = int(ar[1])
        c = int(ar[2])
        #print(a, b, c)
        d = b ** 2 - 4 * a * c
        #print(d)
        if d < 0:
            #return f'No root' с retern не работает, не понятно почему
            print(f'No root')
        elif d == 0:
            x_1 = (- b) / (2 * a)
            print(x_1)
            #return x_1 с retern не работает, не понятно почему, через принт работает.
        elif d > 0:
            x_1 = (- b + sqrt(d)) / (2 * a)
            x_2 = (- b - sqrt(d)) / (2 * a)
            print(x_1, x_2)
            #return x_1, x_2 с retern не работает, не понятно почему


quadratic()

print(quadratic(()))

