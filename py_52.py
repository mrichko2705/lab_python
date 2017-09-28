#!/usr/bin/env python3
# --*-- coding:utf-8 --*--

h = float(input("Door height: ")) 
w = float(input("Door weight: ")) 
a = float(input("Box side a: ")) 
b = float(input("Box side b: ")) 
c = float(input("Box side c: ")) 

print((a<h and b<w)or(b<h and a<w)or(b<h and c<w)or(c<h and b<w)or(a<h and c<w)or(c<h and a<w))
