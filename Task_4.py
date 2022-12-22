# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
from functions import get_int

num = get_int('Введите количество элементов списка: ')
if num == 0: num = 1
numbers = [randint(-1 * num, num) for _ in range(num)]
print('Исходный список:', numbers)
with open('file.txt', 'w') as data:
    for i in range(1, randint(1, num)):
        data.write(str(randint(0, num - 1)) + '\n')
data = open('file.txt', 'r')
mult_indexes = [int(i) for i in data]
data.close()
print('Индексы перемножаемых элементов:', mult_indexes)
prod = 1
for i in mult_indexes:
    prod *= numbers[i]
print('Произведение указанных элементов равно:', prod)


