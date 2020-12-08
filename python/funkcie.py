#!/usr/bin/env python3

ccc=3.14

def f(a,b):
   
    global ccc

    x=1
    print("a=",a)
    print("b=",b)
    
    print("x=",x)
    print("ccc=",ccc)
    ccc=6.28


f(1,"slon")
print("ccc=",ccc)

def scitaj(iterovatelne, start_at=0):

    to_return = start_at

    for item in iterovatelne:
        to_return += item

    return to_return

print(scitaj([1,-1,2]))

print(scitaj(range(101)))

print(scitaj(["a", "bc", "de"], ""))

def my_max(*d):

    to_ret = 0

    for num in d:
        if (num > to_ret):
            to_ret = num

    return to_ret

print(my_max(1,2,3,4,-1))
