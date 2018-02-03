# Инструкция finally всегда выполняется при выходе из блока try,
# не смотря на то, было исключение или нет.
import sys
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except:
        print("Unexpected error:", sys.exc_info()[0])
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)

# При самостоятельном возбуждении исключений можно использовать переменные:

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # <class 'Exception'>
    print(inst.args)     # аргументы хранятся в .args
    print(inst)          # __str__ выводит .args
    x, y = inst.args     # распаковываем аргументы
    print('x =', x)
    print('y =', y)


# Создание собственных исключений
# Ислючения должны наследоваться от класса Exception или его потомков

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)