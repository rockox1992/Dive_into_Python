"""
✔ Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов.
"""

my_list = [1, 2, 3, 4, 1, 3, 4, 3, 1, 2, 0, 33, 33]
new_list = []

for i in my_list:
    if my_list.count(i) >= 2:
        if i not in new_list:
            new_list.append(i)
print(new_list)

for i in my_list:
    if my_list.count(i) >= 2:
        new_list.append(i)
print(list(set(new_list)))
