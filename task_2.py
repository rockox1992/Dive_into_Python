"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение
ереданного аргумента, а значение - имя аргумента. Если ключ не хешируем, используйте его строковое представление.
"""


class DICT_KEY:
    dict_new = {}

    def __init__(self, nothing):
        self.list = nothing

    def dict_key(self):

        if type(self.list) == list or type(self.list) == bytearray or type(self.list) == dict \
                or type(self.list) == frozenset:
            self.dict_new[str(self.list)] = type(self.list)
            return self.dict_new
        else:
            self.dict_new[self.list] = type(self.list)
            return self.dict_new


a = DICT_KEY({1: 2})
print(f'{a.dict_key()}')
