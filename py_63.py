#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import math

sc = float(input("Стартовий капітал: "))
cs = float(input("Кінцева сума: "))
v = float(input("Відсоток: "))
d = float(input("Щорічне(1 - рік),Щомісячне(12 - місяць), Щоденне(365 - день) зростання депозиту: "))

def interest(sc, v, d=12, t=1):
    return sc*(1+v/(100*d))**(d*t)

def cal_years(sc, cs, v, d):
    y = 1
    while interest(sc, v, d, y) < cs:
        y += 1
    return y


print("Необхідна сума коштів буде отримана вами за {} років".format(cal_years(sc, cs, v, d)))
