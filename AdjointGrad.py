import pandas as pd
from sympy import *
import re
import numpy as np
from BrentMet_var2_help import BrentMet


class AdjointGrad:
    def find(self, z, x, e, flag1, flag2, extr):
        """
        Поиск экстремума функции многих переменных при помощи алгоритма Ньютона-сопряженного градиента
        Parameters
        ===========
        :param z: str
            функция минимизации (максимизации)
        :param x: float
            начальная точка, из которой начинаем спуск
        :param e: float
            точность оптимизации
        :param flag1: int
            Вывод промежуточных результатов? 1 - да / 0 - нет
        :param flag2: int
            запись промежуточных результатов в датасет 1 - да / 0 - нет
        :param extr: int
            экстремум который вы хотите найти 1 - максимум, 0 - минимум
        :return:
            Возвращает точку максимума или минимума, значение функции в точке минимума и датасет с промежуточными
             вычислениями
        """
        func = sympify(z)
        l = Symbol('l')
        lst_xi = np.sort(list(set(re.findall(r'[x]\d', z))))

        df = pd.DataFrame(columns=['Номер итерации', 'Полученные значения'])

        det_func = []
        for i in range(len(lst_xi)):
            det_func.append(func.diff(lst_xi[i]))

        j = 0
        while j < 10:
            i = 0
            podst = []
            calc_det = []
            for k in range(len(lst_xi)):
                podst.append((lst_xi[k], x[k][0]))
            for k in range(len(lst_xi)):
                calc_det.append([det_func[k].subs(podst)])
            S = np.dot(-1, calc_det)

            while i < 10:

                lam = x + np.dot(l, S)
                podst_f_l = []
                for k in range(len(lam)):
                    podst_f_l.append((lst_xi[k], lam[k][0]))
                f_l = str(func.subs(podst_f_l))
                f_l = re.sub(r'l', r'x', f_l)
                lam = BrentMet()
                l_min = lam.find(f_l, -5, 5, e, 100)
                xk = x + np.dot(l_min, S)

                sum_det = 0
                sum_det1 = 0
                for k in range(len(calc_det)):
                    sum_det += (calc_det[k][0]) ** 2
                    sum_det1 += (xk[k][0]) ** 2
                Skj = np.dot(-1, xk) + (sum_det1 / sum_det) * S

                sum_Skj = 0
                for k in range(len(Skj)):
                    sum_Skj += (Skj[k][0]) ** 2

                podst_after = []
                for k in range(len(lst_xi)):
                    podst_after.append((lst_xi[k], xk[k][0]))

                x_ = x
                x = xk
                x_beauty = []
                for k in range(len(x)):
                    x_beauty.append(float(x[k][0]))
                if flag1 == 1:
                    print(f'Итерация №{i}, точка {tuple(x_beauty)}')
                if flag2 == 1:
                    df.loc[i] = [i, tuple(x_beauty)]

                # Написать датасеты использовать x_beauty
                if extr == 0:
                    if (sum_Skj ** (1 / 2) < e) or (abs(sum(xk - x_)[0] ** (1 / 2)) < e):
                        print(f'Минимум в точке {tuple(x_beauty)}')
                        print(f'Значение функции в точке минимума {float(func.subs(podst_after))}')
                        c = 1
                        break
                else:
                    if (sum_Skj ** (1 / 2) < e) or (abs(sum(xk - x_)[0] ** (1 / 2)) < e):
                        print(f'Максимум в точке {tuple(x_beauty)}')
                        print(f'Значение функции в точке максимума {float(func.subs(podst_after))}')
                        c = 1
                        break
                S = Skj
                i += 1
            if c == 1:
                break
            j += 1

        if flag2 == 1:
            print(df)
            df.to_csv('FastGradDescent_results.csv', index=False)
            print('Датасет сохранен в папку проекта в формате csv')


# while True:
#     print("Какой экстремум вы хотите найти? 1 - максимум \ 0 - минимум")
#     q = int(input())
#     if q == 1:
#         extr = 1
#         break
#     elif q == 0:
#         extr = 0
#         break
#     else:
#         print("Такой команды нет. Введите снова")
# print("Введите функцию f(x1, x2, ... , xn). Например: x1**2 + x1*x2**3 + x3**2")
# f = input()
# if extr == 1:
#     f = "- (" + f + ")"
#     print(f)
# count_param = np.sort(list(set(re.findall(r'[x]\d', f))))
# print("Введите шаг. Например: 0.01")
# l = float(input())
# print("Введите начальную точку, из которой начинаем спуск.")
# lst_xi = []
# for i in range(len(count_param)):
#     print(f'Введите {count_param[i]}. Например: 1')
#     xi = [float(input())]
#     lst_xi.append(xi)
#
# while True:
#     print("Хотите ввести точность оптимизации? 1 - да / 0 - нет")
#     q = int(input())
#     if q == 1:
#         print("Введите точность оптимизации. Например: 0.001")
#         e = float(input())
#         break
#     elif q == 0:
#         e = 0.0001
#         break
#     else:
#         print("Такой команды нет. Введите снова")
#
# while True:
#     print("Хотите ввести промежуточные результаты? 1 - да / 0 - нет")
#     q = int(input())
#     if q == 1:
#         flag1 = 1
#         break
#     elif q == 0:
#         flag1 = 0
#         break
#     else:
#         print("Такой команды нет. Введите снова")
#
# while True:
#     print("Хотите записать промежуточные результаты в датасет? 1 - да / 0 - нет")
#     q = int(input())
#     if q == 1:
#         flag2 = 1
#         break
#     elif q == 0:
#         flag2 = 0
#         break
#     else:
#         print("Такой команды нет. Введите снова")
#
# function = AdjointGrad()
# function.find(f, lst_xi, e, flag1, flag2, extr)
