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
    list_csv = []
    with open('quadro.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for i in reader:
            a = i[0]
            b = i[1]
            c = i[2]
            list_csv.append(i)
        return list_csv


