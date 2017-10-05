#!/usr/bin/env python3
# --*-- coding:utf-8 --*--

string = str(input("Введіть слово англійською мовою: "))
alph = ['a', 'o', 'u', 'i', 'e', 'y']
b = []
for i in string:
	if i.lower() in alph :
		b.append(1)	
print("Кількість голосних в слові = {}".format(len(b)))	

