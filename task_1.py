"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

text = r"C:\Users\rockox\PycharmProjects\pythonBD\GB_HW_2023\task_5\мвмвм\task_14567апнв.pyпавп"


def ret_name(text: str):
    extension = text.split('.')[1]
    name_full, *_ = text[::-1].split(f'\\')
    name = name_full[:(len(extension)):-1]
    path = "\\".join(text.split(f'.{extension}'))[:(len(text) - len(name_full) - 1)]
    return path, name, extension


print(*ret_name(text))
