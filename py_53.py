#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
import random

a = int(input("Ваш хід - Камінь(1), Ножниці(2), Папір(3): ")) 
b = random.randint(1,3) 

if a == 1: print("Ваш   вибір Камінь")
if a == 2: print("Ваш   вибір Ножниці")
if a == 3: print("Ваш   вибір Папір")

if b == 1: print("Інший вибір Камінь")
if b == 2: print("Інший вибір Ножниці")
if b == 3: print("Інший вибір Папір")

if a == b: print("Нічія")
if a == 1 and b == 2 : print("Ви виграли")
if a == 1 and b == 3 : print("Ви програли")
if a == 2 and b == 1 : print("Ви програли")
if a == 2 and b == 3 : print("Ви виграли")
if a == 3 and b == 1 : print("Ви виграли")
if a == 3 and b == 2 : print("Ви програли")
	
