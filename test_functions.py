def prime_numbers(x):
    if x>0 and x<1000:
        if x == 1:
            return 'Число ' + str(x) + ' не является простым'
        for i in range(2, (x//2)+1):
            if x % i == 0:
                return 'Число ' + str(x) + ' не является простым'
        else:
            return 'Число ' + str(x) + ' является простым'
    else:
        return 'Ошибка. Пожалуйста введите число от 1 до 1000'

print(prime_numbers(1))

def test_function_1(): # проходит тест успешно если число x_temp простое
    x_temp = 2
    x_res = prime_numbers(x_temp)
    if x_res == 'Число ' + str(x_temp) + ' является простым':
        print('Тест 1 успешно выполнен - число простое!')
    else:
        print('Тест 1 выполнен с ошибкой - число не является простым!')

test_function_1()

def test_function_2(): # проходит тест успешно если число x_temp не простое
    x_temp = 6
    x_res = prime_numbers(x_temp)
    if x_res == 'Число ' + str(x_temp) + ' не является простым':
        print('Тест 2 успешно выполнен - число не является простым!')
    else:
        print('Тест 2 выполнен с ошибкой - число является простым!')

test_function_2()

def test_function_3():
    assert prime_numbers(4) == 'Число ' + str(4) + ' не является простым'
    assert prime_numbers(6) == 'Число ' + str(6) + ' не является простым'
    assert prime_numbers(5) == 'Число ' + str(5) + ' является простым'

def number_divisor(x):
    if x > 0 and x < 1000:
        divisor = []
        for i in range(1, x+1):
            if x % i == 0:
                divisor.append(i)
        result = 'Все делители числа ' + str(x) + ' : ' + str(divisor)
        return result
    else:
        return 'Ошибка. Пожалуйста введите число от 1 до 1000'

#print(number_divisor(10))

def test_function_4():
    x_temp = 8
    x_res = number_divisor(x_temp)
    if x_res == 'Все делители числа ' + str(x_temp) + ' : ' + str([1, 2, 4, 8]):
        print('Тест 4 успешно выполнен!')
    else:
        print('Тест 4 выполнен с ошибкой!')

test_function_4()

def test_function_5():
    assert number_divisor(2) == 'Все делители числа ' + str(2) + ' : ' + str([1, 2])
    assert number_divisor(10) == 'Все делители числа ' + str(10) + ' : ' + str([1, 2, 5, 10])
    assert number_divisor(4) == 'Все делители числа ' + str(2) + ' : ' + str([2])