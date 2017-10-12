#!/usr/bin/env python3
# --*-- coding:utf-8 --*--

def midd(mass):
	a =0
	for i in mass:
		a += i
	b = a/len(mass)
	return b	
	
def med(mass):
	sort_mass = sorted(mass)
	len2 = int(len(sort_mass)/2)
	if len(sort_mass) % 2:	
		a = sort_mass[len2]
	else:
		a = round(sort_mass[len2-1] + sort_mass[len2])/2
	return a			
input_mass = [1,2,3,6,6,5,5,4,4,7,7,8,8,9,9,3,6,5,4,1,2,5,55,44,88,99,66,22,5,2,5,84,65,13,56,24] 
print("Середнє значення = {}".format(midd(input_mass)))
print("Медіана = {}".format(med(input_mass)))
	
	
