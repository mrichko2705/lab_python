#! /usr/bin/env python3
# -*- coding: utf-8 -*-

string = input("Введіть строку: ")
def shchar(string) :
	s_new = ''
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a']
	alphabet += [a.upper() for a in alphabet]
    	
	for c in string :
		for a in alphabet :
			if c == a :
				s_new += alphabet[alphabet.index(a)+1]
				break
		else:
			s_new += c
	return s_new


print("{}".format(shchar(string)))
