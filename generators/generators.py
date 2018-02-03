def fib(max_num):
    """
    Печатает последовательность Фибоначи до заданного числа
    :param max_num:
    :return:
    """
    a, b = 1, 1
    while a < max_num:
        yield a
        a, b = b, a + b

for i in fib(100):
    print(i)
print('############################')
"""
Два способа печати квадратов списка
"""
a = [1,2,3,4,5,6,7,8,9,10]
sq = [x*2 for x in a if x % 2 == 0]
alt = map(lambda x: x*2, filter(lambda x: x % 2 == 0, a))
print(list(sq))
print(list(alt))
# [4, 8, 12, 16, 20]
# [4, 8, 12, 16, 20]
print('############################')
"""
Меняет местами ключ и значение в словаре
"""
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayene': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
print(rank_dict)
#{1: 'ghost', 2: 'habanero', 3: 'cayene'}
"""
Генерирует множество из словаря
"""
ch_len_set = {len(name) for name in chile_ranks.keys()}
print('############################')

"""
Печатает матрицу в одну строку
"""
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)
flat = [x for row in matrix for x in row]
print(flat)

"""
Печатает квадраты значений матрицы
"""
sq = [[x**2 for x in row] for row in matrix]
print(sq)
#[[1, 4, 9], [16, 25, 36], [49, 64, 81]]

"""
Печатает трехмерную матрицу в строку (два способа)
"""
matrix = [
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]],
]
"""
flat = [x for sublist1 in matrix
        for sublist2 in sublist1
        for x in sublist2]
        """
flat = []
for sublist1 in matrix:
    for sublist2 in sublist1:
        flat.extend(sublist2)
print(flat)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

"""
Берет из списка только числа больше 4 и четные
"""
a = [1,2,3,4,5,6,7,8,9,10]
b = [x for x in a if x > 4 and x % 2 == 0]
c = [x for x in a if x > 4 if x % 2 == 0]
print(b,c)
assert b == c #если проверка не пройдет, будет возбуждено исключение
print('############################')
"""
Печатает только те строки, где сумма элементов больше 10 и только те значения в этих строках, которые делятся на 3
"""
matrix = [[1,2,3], [4,5,6], [7,8,9]]
filtered = [[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]
print(filtered)
# [[6], [9]]
print('############################')
"""
Печатает только те числа, которые делятся на 2 и на 3
"""
a = list(range(100))
b = [x for x in a if x % 2 == 0 if x % 3 == 0]
print(b)
# [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]

"""
Печатает колличество символов в каждой строке
"""
import random

with open('my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

#val = [len(x) for x in open('my_file.txt')] # заменяем на объект генератор
val = (len(x) for x in open('my_file.txt'))
print(next(val))

print('############################')
l = range(1,11)
#генератор списка
l2 = list(map(lambda x: x**2, l))
l3 = [str(x) for x in l if x % 2 == 0]
print(l2)
print(l3)

#генератр словаря
d1 = {x: x ** 2 for x in l}
print(d1)

#генератор множеств
d2 = {x ** 2 for x in l}
print(d2)

#свой генератор
def enumerate2(xs, start=0, step=1):
    for x in xs:
        yield (start, x)
        start += step
list(enumerate2([1,2,3], 5, -1))
#[(5, 1), (4, 2), (3, 3)]
list(enumerate2([1,2,3], 5, -2))
#[(5, 1), (3, 2), (1, 3)]