# def greeting(name,salary):
#     print("Hello Good Morning",name,"\nYour Salary is credited ",salary)
# greeting("Rohan",20000)
# greeting("mohan",40000)
# greeting("abcd",45000)

def GrossAmount(name,sal,bon):
    print("Hey ",name)
    gross=sal+bon
    return gross

for i in range(5):
    name=input("enter the name :\n")
    sal=int(input("Enter the Salary:\n"))
    bonussal=int(input("Enter the Bonus Salary:\n"))
    gross=GrossAmount(name,sal,bonussal)
    print(f'Gross salary is {gross}')