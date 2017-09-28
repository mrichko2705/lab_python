#!/usr/bin/env python3
# --*-- coding:utf-8 --*--

a = int(input("Введіть число, яке на вашу думку є степенем двійки: "))
q = a & (a-1)
print("true" if q ==0 else "false")
