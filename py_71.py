#!/usr/bin/env python3
# --*-- coding:utf-8 --*--


def shiftString(string,k):
	s = string[k::] + string[:k:]
	return s 
	
string = str(input("Введіть строку для зсуву - "))
k = int(input("Зсув на k = "))	
print(shiftString(string,k))
