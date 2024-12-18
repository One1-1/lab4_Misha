"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""


from package_lab4.lab2 import task1, IsSpecial_Task2, Task3, Task4
from package_lab4.lab3 import Task1, Task2, Task3


def menu():
    """
    Функция предлагает выбор номера задания и номера лабораторной работы\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
             choice_lab - выбранный номер лабы
    """
    choice_lab = int(input('Выберите 2 или 3 лабороторная: '))
    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_lab, choice_task

if __name__ == '__main__':
    while True:
        choice = menu()
        if choice[0] == 2:

            match choice[1]:

                case 1:
                    V0 = float(input("Введите начальную скорость V0 (м/с): "))
                    a = float(input("Введите ускорение a (м/с²): "))
                    t = float(input("Введите время t (с): "))
                    task1(V0, a, t)
                case 2:
                    x = int(input('Введите x: '))
                    print(IsSpecial_Task2(x))
                case 3:
                    x = int(input('Введите x: '))
                    e = float(input('Введите e: '))
                    print(Task3(x))
                case 4:
                    n = int(input('Введите номер дня недели: '))
                    Task4(n)
                case _:
                    break

        else:
            match choice[1]:

                case 1:
                    n = int(input('Введите число: '))
                    Task1(n)
                case 2:
                    n = int(input('Введите число: '))
                    print(Task2(n))
                case 3:
                    x = float(input('Введите x: '))
                    eps = float(input('Введите точность: '))
                    Task3(x, eps)
                case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

