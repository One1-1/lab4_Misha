def task1(V0, a, t):
    '''
    Определить расстояние, пройденное физическим телом за время t, если
    тело движется с постоянным ускорением а и имеет в начальный
    момент времени скорость V0

    :param V0: начальная скорость
    :param a: ускорение
    :param t: время
    :return: None
    '''


    S = V0 * t + 0.5 * a * t ** 2

    print("Форматирование посредством %")
    print("\tСреднегеометрическое = %.2f" % S )
    print("Форматирование посредством format")
    print("\tСреднегеометрическое = {:.2f}".format(S ))
    print("Форматирование посредством f-строк")
    print(f"\tСреднегеометрическое = {S :.2f}")


def IsSpecial_Task2(x):
    '''
    Разницы между соседними разрядами (между 1-м и 2-м, между 2-м и
    3-м, между 3-м и 4-м) целого 4-хзначного числа x по абсолютной
    величине не превышает 3.

    :param x: Вводимое число
    :return isSpecial:
    '''
    a1 = x // 1000 # Находим первую цифрцу числа
    a2 = (x // 100) % 10# Находим вторую цифрцу числа
    a3 = (x // 10) % 10# Находим тнретью цифрцу числа
    a4 = x % 10# Находим четвертую цифрцу числа
    isSpecial=(abs(a1-a2)==3 and abs(a2-a3)==3 and abs(a3-a4)==3)
    return(isSpecial)


def Task3(x, e):
    '''
    Составить программу для вычисления значений функции y = f(x) при
    произвольных значениях x. (a, b – константы)

    :param x: аргумент функции y = f(x)
    :return y: результат
    '''
    from math import sin, sqrt

    a = 7.1
    b = 3.2
    if x <= 0:
        y = a + (e**(-x))/2
    elif 0<x<4:
        y = sin((b**2)*x)
    else:
        y = sqrt((x**2) + (2*a))
    return y

def Task4(n):
    '''
    Составить программу, которая по номеру дня в месяце печатает день недели.
    Считаем, что 1-е число месяца - понедельник.

    :param n: номер дня недели
    :return: None
    '''
    match n:
        case (1|8|15|22|29):
            print('Понедельник')
        case (2|9|16|23|30):
            print('Вторник')
        case (3|10|17|24|31):
            print('Среда')
        case (4|11|18|25):
            print('Четверг')
        case (5|12|19|26):
            print('Пятница')
        case (6|13|20|27):
            print('Суббота')
        case (7|14|21|28):
            print('Воскресенье')
        case _:
            print('Нет такого дня')





