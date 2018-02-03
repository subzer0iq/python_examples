l1 = [1,2,3]
l2 = [5,6,7,8]
l3 = [4,5]
print(list(zip(l1,l2)))
print(list(map(lambda t: t[0] * t[1], zip(l1,l2))))
print(list(map(lambda t: t[0] * t[1] * t[2], zip(l1,l2,l3))))