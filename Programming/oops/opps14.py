# operator overloading and dunder methods in python

class Employee:
    no_of_leaves=14
    def __init__(self,name,salary,role,phone):
        self.name=name
        self.salary=salary
        self.role=role
        self.phone=phone
    
    def printDetails(self):
        print(f"Employee Name is {self.name}\nSalary {self.salary}\nRole {self.role}\nPhone Number is {self.phone} No of Leave {self.no_of_leaves}")

    @classmethod
    def change_of_leaves(cls,n):
        cls.no_of_leaves=n

    def __add__(emp1,emp2):
        return emp1.salary+emp2.salary

    def __sub__(emp1,emp2):
        return emp1.salary-emp2.salary

    def __mul__(emp1,emp2):
        return emp1.salary*emp2.salary

    def __truediv__(self,other):
        return self.phone/other.phone

    def __floordiv__(self,other):
        return self.phone//other.phone

    def __str__(self):
        return f"STR: Employee Name is {self.name}\nSalary {self.salary}\nRole {self.role}\nPhone Number is {self.phone}\n No of Leave {self.no_of_leaves} "


    def __repr__(self):
        return f"Repr: Employee Name is {self.name}\nSalary {self.salary}\nRole {self.role}\nPhone Number is {self.phone} No of Leave {self.no_of_leaves}"

    @staticmethod
    def Company():
        print("i am accenture")


emp1=Employee("Mahesh",50000,"developer",9874563210)
emp2=Employee("Rohan",25000,"developer",8745963214)
print(emp1+emp2)
print(emp1/emp2)
print(emp1)
print(emp2.no_of_leaves)
print(emp2.printDetails())
emp1.Company()

emp2.change_of_leaves(50)
print(emp2)