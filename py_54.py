#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
import math
import cmath

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print("{}x^2 + {}x + {}".format(a,b,c))

D = b**2 - 4*a*c
if D > 0 : 
	d = math.sqrt(D)
	x1 = (-b + d)/2*a
	x2 = (-b - d)/2*a
	print("x1 = {}, x2 = {}".format(x1,x2))
elif D == 0 :
	x1 = (-b/2*a) 
elif D < 0 : 
	d = cmath.sqrt(D)
	x1 = (-b + d)/2*a
	x2 = (-b - d)/2*a
	print("x1 = {}, x2 = {}".format(x1,x2))
