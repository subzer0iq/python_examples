import time

def infoit(func):
    def decorated(*args, **kwargs):
        print('before')
        args_str = ', '.join([str(x) for x in args])
        result = func(*args, **kwargs)
        print('after')
        print('function {} args is {}'.format(func.__name__, args_str))
        return result
    return decorated

def timeit(func):
    def decorated(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        time.sleep(2)
        print('{} run in {} sec'.format(func.__name__, time.time() - start))
        return res
    return decorated

def s(a,b):
    print(a+b)

s = infoit(s)
s(1, 2)
# более удобный способ обернуть функцию. Декораторы выполняются в порядке близости к телу функции
# вариант без декораторов - mu = timeit(decorator(mu))
@timeit
@infoit
def mu(a,b):
    print (a*b)

mu(2,3)

#===============Декоратор с агрументом===================
# В декоратор можно передавать параметры:
def pause(t): #производит декораторы
    def wrapper(f):
        def tmp(*args, **kwargs):
            time.sleep(t)
            return f(*args, **kwargs)
        return tmp

    return wrapper

@pause(6)
def func(x, y):
    return x + y

print (func(1, 2))
# Можно записать в таком виде:
#func = pause(6)(func)
#функция pause(6) вернет нам wrapper(f) и мы этим декоратором обрабатываем функцию func
#print(func(5,6))