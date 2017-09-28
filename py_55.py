#!/usr/bin/env python3
# --*-- coding:utf-8 --*--

def is_Simple(a, i=2):
    while a > i:
        if a % i == 0:
            return False
        i += 1
    return True if a > 1 else False

a = int(input("Введіть число: "))
print("Число {} {}".format(a, "є просте" if is_Simple(a) else "НЕ є просте"))


