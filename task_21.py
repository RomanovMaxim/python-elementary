# Нужно проверить, все ли числа в последовательности уникальны.

lst1 = [34, 60, 44, 15, 99]
lst2 = [34, 60, 34, 15, 99]

print(len(lst1) == len(set(lst1)))
print(len(lst2) == len(set(lst2)))
