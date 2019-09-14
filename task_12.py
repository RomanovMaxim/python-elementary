# Напишите программу, которая принимает имя файла и выводит его расширение.
# Если расширение у файла определить невозможно, выбросите исключение.

def get_extension(filename):
    start = filename.rfind('.')
    if (start < 1) or (start == len(filename)-1) or (start != filename.find('.')):
        raise ValueError
    return filename[start:]

try:
    print(get_extension('abc.py'))
    print(get_extension('abc'))  # raises ValueError
    print(get_extension('.abc'))   # raises ValueError
    print(get_extension('.abc.def.'))   # raises ValueError
except ValueError:
    print('У файла нет расширения')
