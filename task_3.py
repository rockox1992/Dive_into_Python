"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""


def fibonachi(n: int):
    f_1, f_2 = 0, 1
    for _ in range(n + 1):
        yield f_1
        f_1, f_2 = f_2, f_1 + f_2


print(*fibonachi(7))
fibo = iter(fibonachi(7))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
