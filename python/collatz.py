#!/usr/bin/env python3

n=79

while n != 1:
    print(n)
    if n % 2 == 0:
        n=n//2 # // celociselne delenie
    else:
        n=3*n+1

print(n)
