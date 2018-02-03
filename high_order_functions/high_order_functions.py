#Перемножить два списка
print(list(map(lambda x, y: x*y, [1,2,3,4], [10,10,30])))
"""
[10, 20, 90]
"""
#возвращает тру если хоть один элемент списка тру
print(any([True,False, 1, [],"h"]))
"""
True
"""
#возвращает тру если все элементы списка тру
print(all([True,False]))
"""
False
"""
from functools import reduce

l = range(1,6) # создает последовательность от 1 до 5

def mult(x, y):
    return x*y

fac = reduce(mult, l)
""" сначала берет первые два числа, перемножает их с помощью функции
mult, потом берез результат и следующее число из списка l и так же 
перемнодает с помощью функции mult и.т.д.
"""

print(fac)
print('-----')
rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
    {"name": "комната 4", "length": 9, "width": 6}
]

def square_room(square):
    return {"name": square["name"], "sq": square["length"] * square["width"]}

def best_square(square1, square2):
    if square1["sq"] > square2["sq"]:
        return square1
    return square2

#rooms2 = list(map(square_room, rooms))
#print(rooms2)
print(reduce(best_square, map(square_room, rooms)))
"""
Сначала map возвращает новый словарь, в которм вычеслены площади с помошью
функции square_room, потом этот словарь передается в функцию reduce, которая с помощью функции
best_square, вычисляет комнату с самой большой площадью.
"""