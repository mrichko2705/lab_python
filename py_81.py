#!/usr/bin/env python3
# --*-- coding:utf-8 --*--

def camicadze(k,n) :
	boys = [i for i in range(1, k+1)]
	while len(boys) > 1 :
		n1 = n
		while n1 > len(boys) : n1 -= len(boys)
		boys = boys[n1:] + boys[:n1-1]
		#print(boys)
	return boys[0]
		
a = int(input("Кількість камікадзе: "))
c = int(input("Інтервал: "))
print("Останнім залишився {}".format(camicadze(a,c) if a > 0 else "ніхто"))
