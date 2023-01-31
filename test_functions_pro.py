import random
from collections import Counter

def F(list_names, N):
    random_name = []
    for i in range(N):
        name = random_name.append(random.choice(list_names))
    return random_name


names = (
'Dima', 'Ivan', 'Glen', 'Marina', 'Max', 'Tolya', 'Luda', 'Rita', 'Kristina', 'Larisa', 'Denis', 'Galina', 'Inna',
'Nina', 'Elena', 'Edik', 'Bob', 'Olga', 'Mary', 'Jessica', 'Marat')

random_list_names = F(names, 100)

#print(random_list_names)

def test_function_1():
    list_names_temp = ('Petya', 'Vanya', 'Svetlana')
    N_temp = 40
    random_list_temp = F(list_names_temp, N_temp)
    if N_temp == len(random_list_temp):
        print('Тест 1 успешно выполнен!')
    else:
        print('Тест 1 выполнен с ошибкой!')

test_function_1()

def frequent_name_F():
    most_common_name = Counter(random_list_names).most_common()[0][0]
    return most_common_name

def test_function_2():
    list_temp = ('Petya', 'Vanya', 'Svetlana', 'Vanya')
    common_name_temp = Counter(list_temp).most_common()[0][0]
    print(common_name_temp)
    if common_name_temp == 'Vanya':
        print('Тест 2 успешно выполнен!')
    else:
        print('Тест 2 выполнен с ошибкой!')

test_function_2()