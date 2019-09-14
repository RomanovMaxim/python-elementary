# Найдите три ключа с самыми высокими значениями в словаре
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

# 1
from operator import itemgetter

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
print(*dict(sorted(my_dict.items(), key=itemgetter(1), reverse=True)[:3]).keys())

# 2
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
print(*sorted(my_dict, key=my_dict.get, reverse=True)[:3])
