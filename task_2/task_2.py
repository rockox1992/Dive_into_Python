"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
# Create a program to find the GCD of two number in python using the Euclid's Algorithm.
def find_hcf(a,b):
    while(b):
        a, a = b, a % b
        return a
a = int(input(" Enter the first number: ") ) # take first no.
b = int(input(" Enter the second number: ")) # take second no.
num = find_hcf(a, b) # call the find_hcf() to get the result
print("  The HCF of two number a and b is ")
print(num) # call num
Источник: https://pythonpip.ru/examples/nod-dvuh-chisel-v-python
"""
import fractions

num_1, num_2 = str(input("Введите первую дробь a/b: ")), str(input("Введите вторую дробь с/d: "))

numerator_1 = int(num_1[0:num_1.find("/")])
denominator_1 = int(num_1[num_1.find("/") + 1:])
numerator_2 = int(num_2[0:num_2.find("/")])
denominator_2 = int(num_2[num_2.find("/") + 1:])

d1 = numerator_1 * numerator_2
d2 = denominator_1 * denominator_2
g1 = numerator_1 * denominator_2 + numerator_2 *denominator_1
g2 = denominator_1 * denominator_2

# Метод нахождения НОД, в функцию не оборачивал, чтобы соответсвтовало пройденому материалу(пришлось погуглить формулу)


def gcd_loop(a, b):
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if(a % i == 0) and (b % i == 0):
            gcd = i
    return gcd


gcd_work = gcd_loop(d1, d2)
gcd_sum = gcd_loop(g1, g2)

print(f'Произведение дробей равно: {int(d1/gcd_work)}/{int(d2/gcd_work)}')
print(f'Сумма дробей равна: {int(g1/gcd_sum)}/{int(g2/gcd_sum)}')

f1 = fractions.Fraction(numerator_1, denominator_1)
f2 = fractions.Fraction(numerator_2, denominator_2)
print(f"{f1 * f2} fractions *")
print(f"{f1 + f2} fractions +")
