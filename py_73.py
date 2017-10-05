#! /usr/bin/env python3
# -*- coding: utf-8 -*-

s = input("Введіть строку: ")
def func(s):
	a = []
	open_d = "{[(<" 
	close_d = "}])>"
	for i in s: 
		if i in open_d: 
			a.append(i)
		elif i in close_d: 
			if not len(a): 
				return False
			elif a.pop() != open_d[close_d.index(i)]: 
				return False
	return not len(a) 

print("{}".format(func(s)))
