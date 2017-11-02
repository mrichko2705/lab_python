#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import math

class Dot:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
	def len(self,D):
		return math.sqrt((D.y - self.y)**2 + (D.x - self.x)**2) 

class Triangle:
	def __init__(self,a_dot,b_dot,c_dot):
		self.a_dot = a_dot
		self.b_dot = b_dot
		self.c_dot = c_dot
	
	def sides(self):
		ab = math.sqrt((self.b_dot.x - self.a_dot.x)**2 + (self.b_dot.y - self.a_dot.y)**2)
		bc = math.sqrt((self.c_dot.x - self.b_dot.x)**2 + (self.c_dot.y - self.b_dot.y)**2)
		ca = math.sqrt((self.a_dot.x - self.c_dot.x)**2 + (self.a_dot.y - self.c_dot.y)**2) 	
		return [ab,bc,ca]
	
	def perimeter(self):
		return sum(self.sides())
				
	def area(self):
		s = self.sides()
		p = self.perimeter()/2
		return math.sqrt(p*(p - s[0])*(p - s[1])*(p - s[2]))
	
	def exist(self):
		s = self.sides()
		a = s[0]
		b = s[1]
		c = s[2]
		if a+b > c and b+c > a and a+c > b : a ="true"
		else: a ="false"
		return a
		
					
dot_1 = Dot(1,1)
dot_2 = Dot(1,4)
dot_3 = Dot(5,1)
triangle_1 = Triangle(dot_1 , dot_2 , dot_3)
print(dot_1.len(dot_2))
print(triangle_1.perimeter())
print(triangle_1.area())
print(triangle_1.exist())		
		
