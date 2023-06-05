"""
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче
выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки
https://www.easydoit.ru/python/reshenie-zadachi-o-8-ferzyax-s-pomoshhyu-python-bystro-prosto-i-elegantno/
"""
import random


def solve(board, r):
    if r == 8:
        print(board)
        return
    for c in range(8):
        if is_valid(board, r, c):
            board[r] = c
            solve(board, r + 1)
            board[r] = None


def is_valid(board, r, c):
    for i in range(r):
        if board[i] == c or board[i] - i == c - r or board[i] + i == c + r:
            return False
    return True


board = [None] * 8
solve(board, 0)
