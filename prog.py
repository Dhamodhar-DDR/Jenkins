#!/usr/bin/python3
import math

#code for checking if a number is perfect square in given range
def check_perfect_square():
    n = 35
    if(n<1) return []
    l = []
    for i in range(1,35):
        root = int(math.sqrt(i))
        if(root*root == i):
            l.append(i)
    return l

print(check_perfect_square())

