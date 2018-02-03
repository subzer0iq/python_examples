import subprocess
import time
import os
import threading

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

#print(list(factorize(21)))
numbers = [5850412, 2817245, 9014286, 6143531]

class FactorizeThread(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))

start = time.time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
    print('Factors: %r' % (thread.factors))

end = time.time()
print('The time was %.3f' % (end - start))
'''
start = time.time()
for number in numbers:
    list(factorize(number))

end = time.time()
print('The time was %.3f' % (end - start))
'''
