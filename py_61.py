#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
import math
a = float(input("Перша сторона a = "))
b = float(input("Друга сторона b = "))
c = float(input("Третя сторона c = "))
p = (a + b + c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Площа вашого трикутника = {}".format(s))
