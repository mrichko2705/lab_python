#!/usr/bin/env python3
# --*-- coding:utf-8 --*--


def shiftString(string,k):
	s = string[k::] + string[:k:]
	return s 
	
string = str(input())
k = int(input())	
print(shiftString(string,k))
