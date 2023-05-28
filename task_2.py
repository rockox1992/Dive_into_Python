"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение
ереданного аргумента, а значение - имя аргумента. Если ключ не хешируем, используйте его строковое представление.
"""


def dict_key(data):
    dict_new = {}
    if type(data) == list or type(data) == bytearray or type(data) == dict or type(data) == frozenset:
        dict_new[str(data)] = type(data)
        return dict_new
    else:
        dict_new[data] = type(data)
        return dict_new


print(dict_key({1: 2}))
