# Вы принимаете от пользователя последовательность чисел, разделённых запятой.
# Составьте список и кортеж с этими числами.

string = '1, 2, 3, 4, 5'
print(list(map(int, string.split(', '))))
print(tuple(map(int, string.split(', '))))
