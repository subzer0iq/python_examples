import random
"""
Печатает колличество символов в каждой строке

with open('my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

#val = [len(x) for x in open('my_file.txt')] # заменяем на объект генератор
val = (len(x) for x in open('my_file.txt'))
print(next(val))
"""