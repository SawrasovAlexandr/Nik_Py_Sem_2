# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from functions import *

while not is_float(num := input('Введите число: ')):
    print('Ввведенное значение должно быть действительным числом!')
sum = 0
for i in num:
    if i != '.':
        sum += int(i)
print('Сумма цифр введенного числа равна:', sum)

