a=25 #global
b=35


def Func1():
    a=15 #local
    global b
    b=b+20
    print(a)
    print(b)

Func1()
print("outside a function")
b=b+20
print(b)