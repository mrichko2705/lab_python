#!/usr/bin/env python3
# --*-- coding:utf-8 --*--

a = float(input("Сторона a = "))
b = float(input("Сторона b = "))
c = float(input("Сторона c = "))

if a+b > c and b+c > a and a+c > b : 
	print("Такий трикутник існує")
else : print("Такий трикутник НЕ існує")
