# Отсортируйте словарь по значению в порядке возрастания и убывания.
from operator import itemgetter

d = {'one': 1, 'four':4, 'three': 3, 'two':2}
print(dict(sorted(d.items(), key=itemgetter(1))))
print(dict(sorted(d.items(), key=itemgetter(1), reverse=True)))
