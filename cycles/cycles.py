#else выполняется только в том случае, если цыкл вайл не был прерван
numbers = [1,3,5,8]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('found even number', number)
        break
    position += 1
else:
    print('not found')
##########
for line in textData.splitlines():
    pass