a=int(input("enter the value a :\n"))
b=int(input("enter the value b :\n"))
try:
    if(b==0):
        print("i am sorry we cant divide with zero")
    c=a/b
    print(c)
except Exception as error:
    print("errors occured is ",error)

finally:
    print("i am chilled person i dont want about try or except")