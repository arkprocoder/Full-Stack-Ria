# operators in python
# +,-,==,*,/,%

# And Operation
# True= True False = false 

# if(2<22 and 40>2) 
# (if(True and True))
# if(True)

# if(2>10 and 3>2)
# if(False and True)
# False

# True and True= True 
# True and False=False
# False and True=False
# False and False=False

# Or operation

# True or True = True
# False or True = True
# True or False = True
# False or False= False

# <,>,<=,>=,==,!= //comparison operators

# 2<3=True
# 5>2=True
# 10<=20= True
# 20>=20 =True
# 20==20 = True
# 10!=20=True
# 20!=20=False

# # if else 

# a=int(input("enter the a value :\n"))
# b=int(input("enter the b value :\n"))
# c=int(input("enter the c value :\n"))
# d=int(input("enter the d value :\n"))

# if(a>b and c<d):
#     print("a is greater then b, c is less than d")

# else:
#     print("a is lesser than b")


# a=2
# b=3
# c=10
# d=22

# if(a>b):
#     print(" a>b")   #false

# elif(b<c or d<c): #true
#     print("b<c")   

# elif(d>a and d>c and a>b and c<b): #false
#     print("d>a and d>c")  

# elif(c<a):
#     print("c<a")  #false

# else:
#     print("nothing")



# loops
# 1. For loop

# for i in range(0,20001,100):
#     print(i)

# mylist=[1,2,3,4,5,6,7,8,9,10,11,15,12,13,17,16,19,18,20]
# for i in mylist:
#     print(i)

# import time


# mylist=[]
# for i in range(0,20,5):
#     # time.sleep(1)
#     mylist.append(i)

# print(mylist)

for i in range(0,10):   
    if i==5:
        continue
    print(i)

    # if(i==50):
    #     break

print("finished")