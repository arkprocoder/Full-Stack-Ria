class A:
    no_of_students=50
    def __init__(self,name):
        self.name=name
    

    def printDetails(self):
        print("Class Name",self.name,"No of students in class ",self.no_of_students)

    @classmethod
    def changeNoStudents(cls,num):
        cls.no_of_students=num

    @staticmethod
    def noOfStudentsinSchool():
        no_of_students=100
        print("Number of students in School ",no_of_students)

a=A("class 7th")
print(a.no_of_students)
print(a.name)
a.printDetails()

print(A.no_of_students)
A.noOfStudentsinSchool() # static method

b=A("class 8th")
b.changeNoStudents(250)
b.printDetails()

c=A("class 9th")
c.no_of_students=150
c.printDetails()

# note:
'''
1. @classmethod is going to take cls as self arguement and it can be passed other args as well like (cls,arg1,arg2,arg3....)
2.@staticmethod is  class level methods which is not related with
objects of the class without creating a objects we can call the static methods 
3.when we call @classmethod to change class level varaibles it is going to change the varaible of class as well in above program i.e no_of_students

'''