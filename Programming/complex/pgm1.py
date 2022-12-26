def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

n=int(input("enter the number to find its factorial :\n"))
res=factorial(n)
print("factorial",res)


















'''
# flow control of pgm
input is 5

1st iteration
def factorial(5):
    if 5==0 or 5==1:
        return 1 #false
    else:
        return n * factorial(n-1)
        return 5 *factorial(5-1)
        return 5 * factorial(4)

2st iteration
def factorial(4):
    if 4==0 or 4==1:
        return 1 #false
    else:
        return n * factorial(4)
        return 5 * 4 factorial(4-1)
        return 5 * 4 factorial(3)

3rd iteration
def factorial(3):
    if 3==0 or 3==1:
        return 1 #false
    else:
        return n * factorial(3-1)
        return 5 * 4 *3 factorial(2)

4th iteration
def factorial(2):
    if 2==0 or 2==1:
        return 1 #false
    else:
        return n * factorial(2-1)
        return 5 * 4 *3 *2* factorial(1)
5th iteration
def factorial(1):
    if 1==0 or 1==1:
        return 1 #false
    else:
        return n * factorial(1)
        return 5 * 4 *3 *2* factorial(1)
        return 5 * 4 *3 *2* 1
        return 120

res=factorial(n)
res=120
print("factorial",120)
'''