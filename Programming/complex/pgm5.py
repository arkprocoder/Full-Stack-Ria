'''mytup=(1,2,3,4,5,6,7,8,9,10)

def functionArguments(*args):
    # for i in args:
    #     print(i)
    print(args)
    print(type(args))

functionArguments(mytup)'''
'''

mylist=[1,2,3,4,5,6,7,8,9,10]
def functionArguments(name,*args):
    for i in args:
        print(i)
        print(type(i))
    print(args)
    print(type(args))
    print(type(name))
    print(name)

# functionArguments("ark",mylist)


# kwargs
mydict={
"name":"rohan",
"age":25,
"phone":7895463210,
"salary":7894.52
}

def keywordArgsFunction(greet,*args,**kwargs):
    for i in args:
        print(i)

    for k,v in kwargs.items():
        print("key is ",k,"value is ",v)
    
    print(greet,"good morning")


keywordArgsFunction("ark",mylist,mydict)'''



def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')
