# Нужно вывести первые n строк треугольника Паскаля.
# В этом треугольнике на вершине и по бокам стоят единицы, а каждое число
# внутри равно сумме двух расположенных над ним чисел.

# 1
n = 5
a = [1]
print(a)
for i in range(1, n+1):
    a = [1] + [a[i] + a[i+1] for i in range(len(a)-1)] + [1]
    print(a)


# 2
from math import factorial

def c(k, n):
    return factorial(n) // (factorial(k) * factorial(n-k))

def pascal_triangle(lines=4):
    for n in range(lines+1):
        line = [c(k, n) for k in range(n+1)]
        print(line)

pascal_triangle()
