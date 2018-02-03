def print_dict(**kwargs):
    #переданные агрументы помещаются в словарь kwargs, имена используются в качестве ключей, а значения в качестве значений
    for item in kwargs.items():
        # перебираются все пары ключ-значение т.е. на каждой итерации в item содержится кортеж из двух элементов
        print(*item, sep=": ")
        #или print(item[0], item[1], sep=": ")

fn = "Ivan"
ln = "Petrov"
p = "Sidorovich"
print_dict(last_name=ln, patronymic=p)