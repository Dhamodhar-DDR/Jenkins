#!/usr/bin/python3
import math

#code for checking if a number is perfect square in given range
def check_perfect_square(n):
    if(n<1):
        return []
    l = []
    for i in range(1,n+1):
        root = int(math.sqrt(i))
        if(root*root == i):
            l.append(i)
    return l
