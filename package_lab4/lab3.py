def Task1(n):
    '''
    Дано натуральное число n. Разложить его на простые множители

    :param n: вводимое число
    :return: None
    '''
    for i in range(2,n+1):
        while (n%i==0):
            print(i," ",end="")
            n //= i
        if n == 1:
            break

def Task2(n):
    '''
    Дана последовательность целых чисел, за которой следует ноль.
    Определить среднее арифметическое простых элементов последовательности.

    :param n: вводимая последовательность
    :return sum/k: среднее арифметическое
    '''
    sum = 0
    k = 1
    while n != 0:
        sum += n
        n = int(input())
        k += 1
    return sum/k

def Task3(x, eps):
    '''
    Не используя стандартные функции (за исключением abs), вычислить значение функции

    :param x: аргумент функции
    :param eps: точность
    :return: результат функции
    '''
    from math import log
    while not(0<x<2):
        print("Ошибка ввода.Повторите")
    y = 0
    zn = 1
    sign = 1
    stepen_x=(x-1)
    a = sign*(stepen_x/zn)
    while abs(a > eps):
        y += a
        zn += 1
        sign = -sign
        stepen_x *= (x - 1)
        a = sign*(stepen_x/zn)
    print(f"y = {y:.6f}")
    print(f"log x = {log(x):.6f}")