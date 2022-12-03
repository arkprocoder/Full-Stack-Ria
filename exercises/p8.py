import math

def circle():
    r=int(input("enter the radius:\t"))
    result=r*r*math.pi
    print("area of the circle is ",result)
    operation()
    
def rectangle():
    l=int(input("enter the length:\t"))
    b=int(input("enter the breadth:\t"))
    result=l*b
    print("area of the rectangle is ",result)
    operation()

def square():
    a=int(input("enter the side:\t"))
    res=a*a
    print("area of the square is ",res)
    operation()

def triangle():
    b=int(input("enter the base:\t"))
    h=int(input("enter the height:\t"))
    res=0.5*b*h
    print("area of the triangle is ",res)
    operation()

def exit():
    print("good bye")

def operation():
    print("Choose the following numbers \n1:circle\n2:rectangle\n3:square\n4:triangle\n5:exit")
    n=int(input())
    if(n>0 and n<6):
        if(n==1):
            circle()
        if(n==2):
            rectangle()
        if(n==3):
            square()
        if(n==4):
            triangle()
        if(n==5):
            exit()

    else:
        print("Give the valid input")
        operation()

operation()