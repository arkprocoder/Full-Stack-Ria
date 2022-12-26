employeename=input("enter en\n")
employeeage=int(input("enter ea\n"))
employeenumber=int(input("enter enn\n"))
employerole=input("enter role\n")
mydict={
    "employeename":employeename,
    "employeeage":employeeage,
    "employeenumber":employeenumber,
    "employeerole":employerole
}
print(mydict)
print(mydict.keys())
print(mydict.values())
print(mydict.items())