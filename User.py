from sympy import *
import numpy as np
from mnog_opt.AdjointGrad import *
from mnog_opt.BrentMet_var2_help import *
from mnog_opt.FastGradDesent import *
from mnog_opt.GradDesentConstStep import *
from mnog_opt.GradDesentDrobStep import *



class User:
    def userAnswer(self):
        """
        Функция создана дл упрощения работы пользователя с данной программой, тут представлены подсказки и премеры ввода
        данных.

        Returns
        ===========
        Обращается к нужной функции метода и передает ей необходимые параметры.
        """
        print(
            "Каким методом для нахождения экстремумов хотите воспользоваться?\n"
            "1 - Mетод градиентного спуска с постоянным шагом\n"
            "2 - Метод градиентного спуска с дроблением шага\n"
            "3 - Метод наискорейшего градиентного спуска\n"
            "4 - Алгоритм Ньютона-сопряженного градиента\n")
        user_answer = int(input())

        # Mетод градиентного спуска с постоянным шагом
        if user_answer == 1:
            while True:
                print("Какой экстремум вы хотите найти? 1 - максимум \ 0 - минимум")
                q = int(input())
                if q == 1:
                    extr = 1
                    break
                elif q == 0:
                    extr = 0
                    break
                else:
                    print("Такой команды нет. Введите снова")
            print("Введите функцию f(x1, x2, ... , xn). Например: x1**2 + x1*x2**3 + x3**2")
            f = input()
            if extr == 1:
                f = "- (" + f + ")"
                print(f)
            count_param = np.sort(list(set(re.findall(r'[x]\d', f))))
            print("Введите шаг. Например: 0.01")
            l = float(input())
            print("Введите начальную точку, из которой начинаем спуск.")
            lst_xi = []
            for i in range(len(count_param)):
                print(f'Введите {count_param[i]}. Например: 1')
                xi = [float(input())]
                lst_xi.append(xi)
            while True:
                print("Хотите ввести число итераций? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    print("Введите кол-во итераций. Например: 500")
                    iter = int(input())
                    break
                elif q == 0:
                    iter = 500
                    break
                else:
                    print("Такой команды нет. Введите снова")
            while True:
                print("Хотите ввести точность оптимизации? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    print("Введите точность оптимизации. Например: 0.001")
                    e = float(input())
                    break
                elif q == 0:
                    e = 0.0001
                    break
                else:
                    print("Такой команды нет. Введите снова")

            while True:
                print("Хотите ввести промежуточные результаты? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    flag1 = 1
                    break
                elif q == 0:
                    flag1 = 0
                    break
                else:
                    print("Такой команды нет. Введите снова")

            while True:
                print("Хотите записать промежуточные результаты в датасет? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    flag2 = 1
                    break
                elif q == 0:
                    flag2 = 0
                    break
                else:
                    print("Такой команды нет. Введите снова")

            function = GradDesentConstStep()
            function.find(f, l, lst_xi, iter, e, flag1, flag2, extr)

        # Метод градиентного спуска с дроблением шага
        elif user_answer == 2:

            while True:
                print("Какой экстремум вы хотите найти? 1 - максимум \ 0 - минимум")
                q = int(input())
                if q == 1:
                    extr = 1
                    break
                elif q == 0:
                    extr = 0
                    break
                else:
                    print("Такой команды нет. Введите снова")
            print("Введите функцию f(x1, x2, ... , xn). Например: x1**2 + x1*x2**3 + x3**2")
            f = input()
            if extr == 1:
                f = "- (" + f + ")"
                print(f)
            count_param = np.sort(list(set(re.findall(r'[x]\d', f))))
            print("Введите шаг. Например: 0.01")
            l = float(input())
            print("Введите начальную точку, из которой начинаем спуск.")
            lst_xi = []
            for i in range(len(count_param)):
                print(f'Введите {count_param[i]}. Например: 1')
                xi = [float(input())]
                lst_xi.append(xi)
            while True:
                print("Хотите ввести число итераций? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    print("Введите кол-во итераций. Например: 500")
                    iter = int(input())
                    break
                elif q == 0:
                    iter = 500
                    break
                else:
                    print("Такой команды нет. Введите снова")
            while True:
                print("Хотите ввести точность оптимизации? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    print("Введите точность оптимизации. Например: 0.001")
                    e = float(input())
                    break
                elif q == 0:
                    e = 0.0001
                    break
                else:
                    print("Такой команды нет. Введите снова")

            while True:
                print("Хотите вывести промежуточные результаты? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    flag1 = 1
                    break
                elif q == 0:
                    flag1 = 0
                    break
                else:
                    print("Такой команды нет. Введите снова")

            while True:
                print("Хотите записать промежуточные результаты в датасет? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    flag2 = 1
                    break
                elif q == 0:
                    flag2 = 0
                    break
                else:
                    print("Такой команды нет. Введите снова")

            while True:
                print("Хотите ввести значение параметра оценки? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    print("Введите значение в интервале (0;1). Например: 0.1")
                    pe = float(input())
                    if 0 < pe < 1:
                        break
                    else:
                        print("Введите корректное значение")
                elif q == 0:
                    pe = 0.1
                    break
                else:
                    print("Такой команды нет. Введите снова")

            while True:
                print("Хотите ввести значение параметра дробления? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    print("Введите значение в интервале (0;1). Например: 0.1")
                    delta = float(input())
                    if 0 < delta < 1:
                        break
                    else:
                        print("Введите корректное значение")
                elif q == 0:
                    delta = 0.95
                    break
                else:
                    print("Такой команды нет. Введите снова")

            function = GradDesentDrobStep()
            function.find(f, l, lst_xi, iter, e, flag1, flag2, extr, pe, delta)

        # Метод наискорейшего градиентного спуска
        elif user_answer == 3:

            while True:
                print("Какой экстремум вы хотите найти? 1 - максимум \ 0 - минимум")
                q = int(input())
                if q == 1:
                    extr = 1
                    break
                elif q == 0:
                    extr = 0
                    break
                else:
                    print("Такой команды нет. Введите снова")
            print("Введите функцию f(x1, x2, ... , xn). Например: x1**2 + x1*x2**3 + x3**2")
            f = input()
            if extr == 1:
                f = "- (" + f + ")"
                print(f)
            count_param = np.sort(list(set(re.findall(r'[x]\d', f))))
            print("Введите начальную точку, из которой начинаем спуск.")
            lst_xi = []
            for i in range(len(count_param)):
                print(f'Введите {count_param[i]}. Например: 1')
                xi = [float(input())]
                lst_xi.append(xi)
            while True:
                print("Хотите ввести число итераций? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    print("Введите кол-во итераций. Например: 500")
                    iter = int(input())
                    break
                elif q == 0:
                    iter = 500
                    break
                else:
                    print("Такой команды нет. Введите снова")
            while True:
                print("Хотите ввести точность оптимизации? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    print("Введите точность оптимизации. Например: 0.001")
                    e = float(input())
                    break
                elif q == 0:
                    e = 0.0001
                    break
                else:
                    print("Такой команды нет. Введите снова")

            while True:
                print("Хотите ввести промежуточные результаты? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    flag1 = 1
                    break
                elif q == 0:
                    flag1 = 0
                    break
                else:
                    print("Такой команды нет. Введите снова")

            while True:
                print("Хотите записать промежуточные результаты в датасет? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    flag2 = 1
                    break
                elif q == 0:
                    flag2 = 0
                    break
                else:
                    print("Такой команды нет. Введите снова")

            function = FastGradDesent()
            function.find(f, lst_xi, iter, e, flag1, flag2, extr)

        # Алгоритм Ньютона-сопряженного градиента
        elif user_answer == 4:

            while True:
                print("Какой экстремум вы хотите найти? 1 - максимум \ 0 - минимум")
                q = int(input())
                if q == 1:
                    extr = 1
                    break
                elif q == 0:
                    extr = 0
                    break
                else:
                    print("Такой команды нет. Введите снова")
            print("Введите функцию f(x1, x2, ... , xn). Например: x1**2 + x1*x2**3 + x3**2")
            f = input()
            if extr == 1:
                f = "- (" + f + ")"
                print(f)
            count_param = np.sort(list(set(re.findall(r'[x]\d', f))))
            print("Введите шаг. Например: 0.01")
            l = float(input())
            print("Введите начальную точку, из которой начинаем спуск.")
            lst_xi = []
            for i in range(len(count_param)):
                print(f'Введите {count_param[i]}. Например: 1')
                xi = [float(input())]
                lst_xi.append(xi)

            while True:
                print("Хотите ввести точность оптимизации? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    print("Введите точность оптимизации. Например: 0.001")
                    e = float(input())
                    break
                elif q == 0:
                    e = 0.0001
                    break
                else:
                    print("Такой команды нет. Введите снова")

            while True:
                print("Хотите ввести промежуточные результаты? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    flag1 = 1
                    break
                elif q == 0:
                    flag1 = 0
                    break
                else:
                    print("Такой команды нет. Введите снова")

            while True:
                print("Хотите записать промежуточные результаты в датасет? 1 - да / 0 - нет")
                q = int(input())
                if q == 1:
                    flag2 = 1
                    break
                elif q == 0:
                    flag2 = 0
                    break
                else:
                    print("Такой команды нет. Введите снова")

            function = AdjointGrad()
            function.find(f, lst_xi, e, flag1, flag2, extr)

        else:
            print('Введен неверный номер')
