from random import randint

"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” 
или “меньше” после каждой попытки.
"""
L_L = 0
U_L = 1000
num = randint(L_L, U_L)
print(num)
count = 1
while count != 11:
  i_num = int(input("Введите число: "))
  count += 1
  if num > i_num:
    print("Загаданое число больше;)")
  elif num < i_num:
    print("Загаданое число меньше;)")
  else:
    print("Вы выйграли")
    break
print("Вы проиграли")