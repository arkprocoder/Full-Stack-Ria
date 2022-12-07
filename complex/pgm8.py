# Join= it is function which can iterate list
# tuple and dictionary using .join using a seprator values like
# ,@,/,(), etc but it should of same data types before joining it

# list

mylist=["mahonar","sriram","bhanu","mahesh","abhishek"]
seprator="/"
res=seprator.join(mylist)
print(res)
print(type(res))

#tuple
mylist=("mahonar","sriram","bhanu","mahesh","abhishek")
seprator="@"
res=seprator.join(mylist)
print(res)
print(type(res))

#dictionary
mydict={"employeName":"Anees","employeeSalary":"12345","isActive":"True"}
seprator="#"
newmydict=seprator.join(mydict.values())
print(newmydict)