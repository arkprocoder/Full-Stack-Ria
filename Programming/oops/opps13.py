class A:
    message="Hello i am class A Varaible"
    def __init__(self):
        self.title="Python Full Stack"
        self.instance="Class A instance"

class B(A):
    message="Hello i am class B Varaible"
    def __init__(self):
        super().__init__()
        self.title="Java Full Stack"
        self.instance="Class B instance"
       
obj=B()
print(obj.title)
print(obj.instance)
print(obj.message)

obj2=A()
print(obj2.title)
print(obj2.instance)
print(obj2.message)