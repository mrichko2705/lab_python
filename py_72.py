#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import re

s = str(input("Введіть строку для перевірки "))

def isPalindr(s):
	s = s.lower()
	s = re.sub('\W+', '', s)
	print(s)
	return True if s == s[::-1] else False

print("{}".format(isPalindr(s)))
