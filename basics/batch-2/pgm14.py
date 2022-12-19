# '''def func1():
#     print("Hello i am func1")

# def func2():
#     print("Hello i am func2")

# def func3():
#     print("Hello i am func3")

# def func4():
#     print("Hello i am func4")

# func1()
# func2()
# func3()
# func4()
# '''


# def greeting(name,salary):
#     print(f'Hey {name} good morning\n Your Salary is credited {salary} ')

# def eDetails():
#     age=200
#     salary=10000
#     ebonus=2345
#     total=salary+ebonus
#     print("hey",age)
#     greeting("ark",23000)
#     print("i done the greeting task")
#     return total,age


# total,age=eDetails() #myreturnval=12345
# print("total",myreturnval,age)


# # greeting('rohan',5000)
# # greeting('rohit',12000)


# def GrossAmount(name,sal,bon):
#     print("Hey ",name)
#     gross=sal+bon
#     f=open("data.txt","a")
#     f.write(f'\nName is {name}\nGross Salary is {gross}')
#     f.close()
#     return gross

# for i in range(1,12):
#     print(i,"iteration")
#     name=input("enter the name :\n")
#     sal=int(input("Enter the Salary:\n"))
#     bonussal=int(input("Enter the Bonus Salary:\n"))
#     gross=GrossAmount(name,sal,bonussal)
#     print(f'Gross salary is {gross}')
    
fullname="rohanshetty@gmail.com"
print(fullname.split("@")[0])
print(fullname.split("@")[1])