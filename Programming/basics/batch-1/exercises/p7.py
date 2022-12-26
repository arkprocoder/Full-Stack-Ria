import math
def circle(r):
    result=r*r*math.pi
    return result

def rectangle(l,b):
    result=l*b
    return result

def square(a):
    res=a*a
    return res

def triangle(b,h):
    res=0.5*b*h
    return res

print("area of the circle")
r=int(input("enter the raidus:\n"))
aoc=circle(r)
print(aoc)