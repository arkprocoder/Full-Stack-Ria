# dictinary
mydict={
    "EmployeeName":"Rohan",
    "age":25,
    "salary":25000.35,
    "wfh":True,
    "likes":["cricket","football"]

}
print(mydict)
print(type(mydict))
print(mydict["age"])
# print(mydict["age1"])
print(mydict.get("EmployeeName"))
print(mydict.get("EmployeeName1"))
print(mydict["salary"])
print(mydict.keys())
print(mydict.values())
print(mydict.items())
mydict.update({"role":"full stack dev"})
mydict.update({"rage":30})
mydict.pop("rage")
# mydict.clear()

mydict2=mydict.copy()
print(mydict)
print(mydict2)
