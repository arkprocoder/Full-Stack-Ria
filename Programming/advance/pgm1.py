# try,except,else,finally

try:
    pass #run the code when there is no error

except:
    pass #executes when try block fails

else:
    pass #executes when try block has no errors and except block is not used

finally:
    pass #executes a any cost let try else or except has errors or not

def Divide(a,b):
    try:
        print("i am try block")

    except ZeroDivisionError as e:
        print("i am except block")

    else:
        print("i am else block")

    finally:
        print("i am finally block")

Divide(2,0)
