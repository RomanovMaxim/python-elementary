# Выведите список файлов в указанной директории.

from os import listdir
from os.path import isfile

# 1
dir_path = 'c:\\'
lst = listdir(path=dir_path)
print(list(filter(lambda f: isfile(f'{dir_path}{f}'), lst)))
