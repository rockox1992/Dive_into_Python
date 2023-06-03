"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии
в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
"""

names = ("Иван, Марья, Сатурн")
rates = (100, 150, 300)
bonus = ('20.01%, 23.05%, 13.13%')

# rate = [int(i) for i in rates]
# print(rate, type(rate), "rate")
# bon = [float(i.strip()) for i in bonus[:-1].replace(',', '').split('%')]
# print(bon, type(bon), "bon")
# name = names.split(',')
# print(name, type(name), "name")
#


def many(names: str, rates: int, bonus: str) -> dict[str:float]:
    yield {name: rate * bon for name, rate, bon in zip(names.split(','), [int(i / 100) for i in rates],
                                                              [float(i.strip()) for i in
                                                               bonus[:-1].replace(',', '').split('%')])}.items()


print(next(many(names, rates, bonus)))
