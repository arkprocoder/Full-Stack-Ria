print("__name__ in main1.py is set to ",__name__)

def addNum(a,b):
    return a+b

def greetings(name):
    print("good morning ",name)




if __name__=='__main__':
    print("i am a main function")
    res=addNum(10,20)
    print("sum of two numbers is ",res)
    greetings("ark")