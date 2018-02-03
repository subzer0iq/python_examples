# сортирует массив numbers, давая приоритет числам из group
numbers = [8,3,6,9,80,23,50]
group = {80,6,9}

def helper(x):
    if x in group:
        return (0,x)
    return (1,x)

numbers.sort(key=helper)
print(numbers)
###############################
from collections import defaultdict
# Сколько раз встречается нужный элемент в массиве. В данном случае red.
colors = ['red','black','green','red','yellow','blue','red']
d = defaultdict(int)
for color in colors:
    d[color] += 1
print(d['red'])

#Ключами словаря будет колличество опереленного элемента массива
d = defaultdict(list)
for color in colors:
    key = len(color)
    d[key].append(color)
print(d[3])
# ['red', 'red', 'red']