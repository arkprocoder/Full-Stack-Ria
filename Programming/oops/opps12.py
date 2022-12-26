# super method and overriding method

class Employee:
    def printDetails(self):
        print("i am class Employee Details")
    
class Student(Employee):
    pass
    # def printDetails(self):
    #     print("i am student class details")

class Child(Student):
    pass
    # def printDetails(self):
    #     print("i am child class details")


obj1=Student()
obj1.printDetails()
obj2=Student()
obj2.printDetails()
obj3=Child()
obj3.printDetails()