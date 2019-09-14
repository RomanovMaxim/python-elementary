# Напишите программу для слияния нескольких словарей в один.

# 1
a = {1:'one', 4:'four', 3:'three', 2:'two'}
b = {5:'five', 6:'six', 7:'seven'}
d = dict()
d.update(a.items())
d.update(b.items())
print(d)

# 2
a = {1:'one', 4:'four', 3:'three', 2:'two'}
b = {5:'five', 6:'six', 7:'seven'}

def union_dict(*args):
    d = dict()
    for elem in args:
        d.update(elem.items())
    return d

c = union_dict(a, b)
print(c)

# 3
a = {1:'one', 4:'four', 3:'three', 2:'two'}
b = {5:'five', 6:'six', 7:'seven'}
c = {**a, **b}
print(c)
