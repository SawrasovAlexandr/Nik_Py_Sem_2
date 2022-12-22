# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from functions import *

def factorial(number):
    if number == 1: return 1
    else: return factorial(number - 1) * number

while (num := get_int('Введите число N: ')) <= 0:
    print('Число должно быть положительным.')
result =[]
for i in range(1, num + 1):
    result.append(factorial(i))
print('Набор произведений чисел от 1 до N:', result)
