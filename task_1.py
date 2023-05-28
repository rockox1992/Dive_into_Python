"""
Напишите функцию для транспонирования матрицы
"""
matrix = [[1, 2, 6], [3, 4, 9], [7, 8, 5]]
transpose_matrix = [list(row) for row in zip(*matrix)]
print(transpose_matrix)