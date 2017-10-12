#!/usr/bin/env python3
# --*-- coding:utf-8 --*--

def mySort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        val = arr.pop(i)
        while (j >= 0) and (arr[j] > val):
            j -= 1
        arr.insert(j + 1, val)
    return arr

mass =[1,6,5,3,7,2,8]
print(mySort(mass))		
