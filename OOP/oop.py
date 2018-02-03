class Auto:
    count = 0
    objects = []
    def __init__(self, number=''):
        self.power = 0
        if number:
            self.number = number

        Auto.count += 1
        Auto.objects.append(self)

    @staticmethod #сообщает, что это метод статичный и относится к классу, а не к объекту
    def set_powers(power):
        for obj in Auto.objects:
            obj.power = power #Перебираем все созданные объекты и задаем каждому power

    def get_number(self):
        return self._number

    def set_number(self, number):
        if number.__len__() != 6:
            print('Number must contain 6 symbols')
        else:
            self._number = number
    def get_tax(self, min_rate=12, max_rate=25):
        rate = min_rate
        if self.power > 100:
            rate = max_rate
        return rate * self.power

    number = property(get_number, set_number) #Мы создали свойство number, которое является объектом класса property
    #тепрь присваивая значение напрямую будет вызываться метод set_number, вместо этого можно использовать декораторы
    #@property и @number.setter
    '''
    @property
    def number(self):   #number вместо get_number
    ...
    
    @number.setter
    @def number(self, number):   #number вместо set_number
    ...
    '''
class Bus(Auto):
    def get_tax(self, min_rate=15, max_rate=15):
        return super().get_tax(min_rate, max_rate) #Позволяет вызывать методы родительского класса

class InterCityBus(Bus):
    def __init__(self):
        self.city = ''
        super().__init__()
    def get_city(self):
        return self.city

class NewObject2():
    x = 1
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return ('[Объект класса NewObject: a=%s, b=%s, c=%s]'
                % (self.a, self.b, self.c))
    def __call__(self, *args, **kwargs): #функтор
        return self.a + self.b + self.c

obj4 = NewObject2(1,2,3)
test = NewObject2(4,5,6).__call__()
print(test)
print(obj4)

auto1 = Auto()
bus1 = Bus()
bus1.power = 101
print(bus1.get_tax())
auto2 = Auto()
print(Auto.count)