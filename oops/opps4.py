class Employee:
    company="T.C.S"

    # constructor
    def __init__(self,eName,eAge,eRole,eSalary):
        self.eName=eName
        self.eAge=eAge
        self.eRole=eRole
        self.eSalary=eSalary
        print("i have set the values")

    def employeeDetails(self):
        return f"Employee Company {self.company}\nEmployee Name {self.eName}\nEmployee Age {self.eAge}\ nEmployee Role {self.eRole}\nEmployee Salary {self.eSalary}"

    @classmethod
    def changeCompany(cls,company):
        cls.company=company
        print("i have set new company name")

    @staticmethod
    def greeting():
        print("Good Morning")

employee1= Employee("Mahesh",24,"Front-end-Developer",40000)    
details1=employee1.employeeDetails()
print(details1)


employee2=Employee("Raghu",23,"Back-End-Developer",50000)
details2=employee2.employeeDetails()
print("\n",details2)


print("before setting the company name of employee2 ",employee2.company)
# employee2.changeCompany("Infosys")
Employee.changeCompany("Dell")
# employee2.company="Infosys"
print("After setting the company name of employee2",employee2.company)


# print("\n")
print("company name of employee1 ",employee1.company)
data=employee1.employeeDetails()
print(data)

employee1.greeting()
Employee.greeting()