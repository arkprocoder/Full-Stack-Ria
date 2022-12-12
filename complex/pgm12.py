# def ria(a):
#     def employee():
#         print("employee function is executed")

#         a(1)     
#         print("After employee function is executed")
#     return employee

# @ria
# def student(b):
#     print("student function is executed",b)

# student()


def Orders(handlerequest):
    def takeOrder():
        print("Order is Saved in DB")

        handlerequest(1005)
        print("Order is Placed")
    return takeOrder

@Orders
def handlerequest(id):
    if id==1005:
        print("Successs")
    else:
        print("Order Failure")

handlerequest()



def Orders(handlerequest):
    def takeOrder():
        print("Order is Saved in DB")

        handlerequest(1005)
        print("Order is Placed")
    return takeOrder

def handlerequest(id):
    if id==1005:
        print("Successs")
    else:
        print("Order Failure")

Orders(handlerequest)