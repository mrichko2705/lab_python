#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import math

sc = float(input("Стартовий капітал: "))
v = float(input("Відсоток: "))
d = float(input("Щорічне(1 - рік),Щомісячне(12 - місяць), Щоденне(365 - день) зростання депозиту: "))
y = float(input("Кількість років: "))

def interest(sc, v, d=12, y=1):
    return sc*(1+v/(100*d))**(d*y)

print("Ви отримаєте ${}".format(interest(sc, v, d, y)))
