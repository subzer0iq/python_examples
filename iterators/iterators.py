#Собственный класс-итератор
class Fib:
    def __init__(self, max_items=10):
        self.max_items = max_items

    def __next__(self):
        self.item +=1
        if self.max_items == self.item:
            raise StopIteration
        self.fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return self.fib

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.item = -1
        return self

#fib = Fib(5)

for item in Fib(20):
    print(item)

#пример чтения из вайла
with open("fib.txt") as fib_file:
    for fib in fib_file:
        print(fib, end="")