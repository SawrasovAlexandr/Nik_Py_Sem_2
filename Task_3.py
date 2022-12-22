#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

from functions import *

while (num := get_int('Введите число N: ')) <= 0:
    print('Число должно быть положительным.')
result =[]
for n in range(1, num + 1):
    result.append(round((1 + 1 / n) ** n, 2))
print(result)
sum = 0
for item in result: 
    sum += item
print('Сумма чисел последовательности (1+1/n)^n, при n = ', num, ': ', sum)
