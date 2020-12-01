#!/usr/bin/env python3

def primes(m):
    
    zoz=[]
    for n in range(2,m):
        for k in range(2,n//2+1):
            if n % k == 0:
                break
        else:
            zoz.append(n)

    return zoz

print(primes(20))
