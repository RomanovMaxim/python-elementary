# Напишите программу, которая выводит чётные числа из заданного списка
# и останавливается, если встречает число 237.
import random

lst = [random.randint(230, 250) for i in range(10)]
print(*lst)

for x in lst:
    if x == 237:
        print('\nНайдено число 237')
        break
    if x % 2 == 0:
        print(x, end=' ')
