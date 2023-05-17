# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

count = 0
for i in range(2, 10):
    for k in range(2, 11):
        print(f"{i} X {k} = {i * k}")
        count += 1
        if count == 9:
            count = 0
            print()
